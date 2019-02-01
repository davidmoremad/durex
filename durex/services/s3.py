# -*- coding: utf-8 -*-
import re
from botocore.exceptions import ClientError
from durex.helpers import ThreadPool

class S3(object):

    ACL_ANY_USER = 'http://acs.amazonaws.com/groups/global/AllUsers'
    ACL_AWS_USER = 'http://acs.amazonaws.com/groups/global/AuthenticatedUsers'

    
    def bucket_public_access(self, permission):
        '''Get public buckets to internet or AWS authenticated users
        
        Args:
            permission (str): Valid values: READ, WRITE, READ_ACP, WRITE_ACP, FULL_CONTROL
        
        Returns:
            list: List of public buckets
        '''
        public_buckets = []
        buckets = self.s3.get_buckets()
        
        def worker(bucket):
            try:
                acl = self.s3.get_bucket_acl(bucket['Name'])
                for grant in acl:
                    if ( 
                        grant['Grantee']['Type'] == 'Group' and
                        grant['Grantee']['URI'] in [self.ACL_ANY_USER, self.ACL_AWS_USER] and
                        grant['Permission'] in permission
                    ):
                        bucket['Grant'] = grant
                        public_buckets.append(bucket)
                        break
            except ClientError as ex:
                if ex.response['Error']['Code'] == 'NoSuchBucket':
                    pass
                else:
                    raise ex

        [self.pool.add_task(worker, bucket) for bucket in buckets]
        self.pool.wait_completion()

        return public_buckets
        
    def bucket_public_fullcontrol_access(self):
        return self.bucket_public_access('FULL_CONTROL')

    def bucket_public_read_access(self):
        return self.bucket_public_access('READ')

    def bucket_public_readacp_access(self):
        return self.bucket_public_access('READ_ACP')

    def bucket_public_write_access(self):
        return self.bucket_public_access('WRITE')

    def bucket_public_writeacp_access(self):
        return self.bucket_public_access('WRITE_ACP')

    def bucket_encryption(self):
        no_encryption_buckets = []
        buckets = self.s3.get_buckets()

        def worker(bucket):
            try:
                self.s3.client.get_bucket_encryption(Bucket=bucket['Name'])['ServerSideEncryptionConfiguration']
            except ClientError as e:
                if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                    no_encryption_buckets.append(bucket)

        [self.pool.add_task(worker, bucket) for bucket in buckets]
        self.pool.wait_completion()

        return no_encryption_buckets

    def __init__(self, client):
        self.s3 = client.service.s3
        self.pool = ThreadPool(30)
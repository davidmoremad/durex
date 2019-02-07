# -*- coding: utf-8 -*-
import re
from botocore.exceptions import ClientError
from .base import Base
from durex.decorators import low, medium, high, critical

class IAM(Base):

    @low 
    def inactive_access_keys(self):
        'Unnecesary inactive access keys'
        users = self.iam.get_users()
        unused_keys = []
        def worker(user):
            keys = self.iam.get_access_keys(user['UserName'])
            for key in keys:
                if key['Status'] == 'Inactive':
                    unused_keys.append(key)
        [self.pool.add_task(worker, u) for u in users]
        self.pool.wait_completion()
        return unused_keys

    @low
    def inactive_users(self):
        'Users who have not logged in AWS since 1 year'
        return self.iam.get_inactive_users()


    def __init__(self, client):
        self.iam = client.service.iam
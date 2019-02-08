# -*- coding: utf-8 -*-
import re
from durex.decorators import low, medium, high, critical
from .base import Base

class EC2(Base):

    def _get_used_security_groups(self, security_groups, regions):
        '''Filter security groups attached to an instance
        
        Args:
            security_groups (list): Security groups to filter
            regions (list): List of regions to locate the used security-groups
        
        Returns:
            list: Security groups which are being used for an instance
        '''

        instances = self.ec2.get_instances(regions=regions)
        all_insecure_sgs = set([sg['GroupName'] for sg in security_groups])
        ec2_insecure_sgs = set([sg['GroupName'] for inst in instances for sg in inst['SecurityGroups']])
        return filter(lambda x: x in ec2_insecure_sgs, all_insecure_sgs)

    @classmethod 
    def _unrestricted_port(cls, security_groups, port):
        results = [] 
        
        for sgroup in security_groups:
            for rule in sgroup['IpPermissions']:
                if ( 
                    rule.get('ToPort') and rule.get('FromPort') and
                    rule['ToPort'] >= port and rule['FromPort'] <= port and
                    '0.0.0.0/0' in set(map(lambda x: x['CidrIp'], rule['IpRanges']))
                    ):
                    results.append(sgroup)
                    break

        return results

    @low
    def instances_naming_convention(self, regions=None):
        'EC2 Instance Naming Conventions'
        regpat = r'^((?!([a-zA-Z0-9_]*\-){3}).)*$'
        instances = self.ec2.get_instances(regions=regions)
        results = filter(lambda x: re.search(regpat, x['TagName']) ,instances)
        return results

    @high
    def unrestricted_access(self, regions=None):
        'Unrestricted access'
        insecure_sgs = self.ec2.get_secgroups_by(filters={'protocol': '-1', 'range':'0.0.0.0/0'}, regions=regions)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @medium
    def unrestricted_ICMP_access(self, regions=None):
        'Unrestricted imcp access'
        insecure_sgs = self.ec2.get_secgroups_by(filters={'protocol': 'icmp', 'range':'0.0.0.0/0'}, regions=regions)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_FTP_access(self, regions=None):
        'Unrestricted ftp access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 21)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_SSH_access(self, regions=None):
        'Unrestricted ssh access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 22)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @medium
    def unrestricted_SMTP_access(self, regions=None):
        'Unrestricted smtp access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 25)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @medium
    def unrestricted_ElasticSearch_access(self, regions=None):
        'Unrestricted elasticsearch access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 9200)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @medium
    def unrestricted_DNS_access(self, regions=None):
        'Unrestricted dns access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 53)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_Netbios_access(self, regions=None):
        'Unrestricted netbios access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 139)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_SMB_access(self, regions=None):
        'Unrestricted smb access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 389)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_CIFS_access(self, regions=None):
        'Unrestricted cifs access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 445)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_MsSQL_access(self, regions=None):
        'Unrestricted mssql access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 1433)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_Oracle_access(self, regions=None):
        'Unrestricted oracle access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 1521)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_MySQL_access(self, regions=None):
        'Unrestricted mysql access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 3306)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_PostgreSQL_access(self, regions=None):
        'Unrestricted postgresql access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 5432)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_MongoDB_access(self, regions=None):
        'Unrestricted mongodb access'
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 27017)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @high
    def unrestricted_RDP_access(self, regions=None):
        'Unrestricted rdp access'
        secgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(secgroups, 3389)
        used_insecure_sgs = self._get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    @low
    def instances_with_scheduled_events(self, regions=None):
        'Instances with scheduled events'
        events = ['instance-reboot', 'system-reboot', 'system-maintenance', 'instance-retirement', 'instance-stop']
        instances = self.ec2.get_instances_status_by({'event': events}, regions=regions)
        return instances


    def __init__(self, client):
        self.ec2 = client.service.ec2
# -*- coding: utf-8 -*-
import re

class EC2(object):

    def get_used_security_groups(self, security_groups, regions):
        instances = self.ec2.get_instances(regions=regions)
        all_insecure_sgs = set([sg['GroupName'] for sg in security_groups])
        ec2_insecure_sgs = set([sg['GroupName'] for inst in instances for sg in inst['SecurityGroups']])
        
        return filter(lambda x: x not in ec2_insecure_sgs, all_insecure_sgs)

    @classmethod 
    def _unrestricted_port(cls, security_groups, port):
        results = [] 
        
        for sgroup in security_groups:
            for rule in sgroup['IpPermissions']:
                if ( 
                    rule.get('ToPort') and rule.get('FromPort') and
                    rule['ToPort'] >= port and rule['FromPort'] <= port
                    ):
                    results.append(sgroup)
                    break

        return results

    def instances_naming_convention(self, regions=None):
        regpat = r'^((?!([a-zA-Z0-9_]*\-){3}).)*$'
        instances = self.ec2.get_instances(regions=regions)
        results = filter(lambda x: re.search(regpat, x['TagName']) ,instances)
        return results

    def unrestricted_access(self, regions=None):
        insecure_sgs = self.ec2.get_secgroups_by(filters={'protocol': '-1', 'range':'0.0.0.0/0'}, regions=regions)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_imcp_access(self, regions=None):
        insecure_sgs = self.ec2.get_secgroups_by(filters={'protocol': 'icmp', 'range':'0.0.0.0/0'}, regions=regions)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_ftp_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 21)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_ssh_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 22)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_smtp_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 25)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_elasticsearch_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 9200)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_dns_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 53)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_netbios_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 139)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_smb_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 389)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_cifs_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 445)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_mssql_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 1433)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_oracle_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 1521)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_mysql_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 3306)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_postgresql_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 5432)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_mongodb_access(self, regions=None):
        sgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(sgroups, 27017)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unrestricted_rdp_access(self, regions=None):
        secgroups = self.ec2.get_secgroups_by(filters={'protocol': 'tcp', 'range':'0.0.0.0/0'}, regions=regions)
        insecure_sgs = self._unrestricted_port(secgroups, 3389)
        used_insecure_sgs = self.get_used_security_groups(insecure_sgs, regions)
        return used_insecure_sgs

    def unused_security_groups(self, regions=None):
        secgroups = self.ec2.get_secgroups(regions=regions)
        instances = self.ec2.get_instances(regions=regions)

        all_sgs = set([sg['GroupName'] for sg in secgroups])
        ec2_sgs = set([sg['GroupName'] for instance in instances for sg in instance['SecurityGroups']])
        unused = all_sgs - ec2_sgs

        return unused


    def __init__(self, client):
        self.ec2 = client.service.ec2
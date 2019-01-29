import durex

durex = durex.Durex('cyber')

instances = durex.ec2.ec2_instances_naming_convention()

for x in instances:
    print(x['Region']['RegionName'], x['TagName']) 
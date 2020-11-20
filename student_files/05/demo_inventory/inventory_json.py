#!/usr/bin/env python

import os
import json

output = {
    '_meta': {'hostvars': {}}
}

path_to_inventory = os.getenv('INVENTORY_SRC', '/etc/inventory.json')
with open(path_to_inventory, 'r') as f:
    mydata = json.load(f)

for group_name, group_params in mydata.items():
  output[group_name] = {'hosts':[], "vars": group_params['vars']}
  for hostname, host_vars in group_params['hosts'].items():
      output[group_name]['hosts'].append(hostname)
      output['_meta']['hostvars'][hostname] = host_vars

print json.dumps(output)

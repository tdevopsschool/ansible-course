#!/usr/bin/env python

'''
Example custom dynamic inventory plugin for Ansible, in Python.
'''

import json

from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable

class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):

    NAME = 'jsn' # used internally by Ansible, it should match the file name but not required

    def verify_file(self, path):
        ''' return true/false if this is possibly a valid file for this plugin to consume '''
        if super(InventoryModule, self).verify_file(path):
            # base class verifies that file exists and is readable by current user
            if path.endswith('.json'):
                return True
        return False

    def parse(self, inventory, loader, path, cache=True):

        # call base method to ensure properties are available for use with other helper methods
        super(InventoryModule, self).parse(inventory, loader, path, cache)

        # make requests to get data to feed into inventory
        with open(path) as f:
            mydata = json.load(f)

        for group_name in mydata.keys():
            self.display.warning('Found group %s' % group_name)
            group = self.inventory.add_group(group_name)
            self.display.warning('Parse hosts list')
            for hostname, host_vars in mydata[group_name]['hosts'].items():
                self.display.warning('Found host %s' % hostname)
                self.inventory.add_host(hostname, group)
                for var, value in host_vars.items():
                    self.inventory.set_variable(hostname, var, value)
            self.display.warning('Parse group vars list')
            for var, value in mydata[group_name]['vars'].items():
                self.inventory.set_variable(group, var, value)

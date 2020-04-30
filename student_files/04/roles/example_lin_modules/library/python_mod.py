#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

def hello():
    return "Hello, World! (in Python)"

module = AnsibleModule(argument_spec={})
module.exit_json(msg=hello())

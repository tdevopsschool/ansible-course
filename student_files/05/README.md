# Homework

1. Create inventory plugin or inventory for CSV format.
2. Create molecule tests for role webserver.
3. Create role for configuring SNMPD.
4. Publish SNMPD role to the galaxy

## How to run

```bash
ANSIBLE_PRIVATE_ROLE_VARS=True ANSIBLE_CONFIG=/vagrant/ansible.cfg ansible-playbook -vvv -c local -i 'asd,' /vagrant/provision_me.yml
```

# Homework

1. Create training environment.
2. Compare the bash script & Ansible playbook.
3. Play the 2048 game.
4. Modify vagrantfile and provision VM via Ansible.
5. If we run run_me.sh twice, will it fail?
    * What’s about run_me.yml?

## Prepare training environment

### Install Software

* git
* [virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [vagrant](https://www.vagrantup.com/)

#### Prepare vagrant if you use proxy

```bash
vagrant plugin install vagrant-proxyconf
```

### Set up VM

```bash
vagrant up
```

#### DEBUG

```bash
env:VAGRANT_LOG=info
vagrant up --debug
```

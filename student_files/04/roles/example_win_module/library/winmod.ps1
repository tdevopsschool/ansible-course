#!powershell

#Requires -Module Ansible.ModuleUtils.Legacy.psm1

$result = @{
    msg = 'Hello from windows'
}

Exit-Json -obj $result

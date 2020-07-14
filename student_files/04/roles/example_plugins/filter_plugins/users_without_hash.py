#!/usr/bin/python
class FilterModule(object):
  def filters(self):
    return {
      'users_without_hash': self.a_users_without_hash
    }

  def a_users_without_hash(self, users_input):
    users_output = []
    for user in users_input:
      if 'password_hash' not in user:
        users_output.append(user['login'])
    return users_output

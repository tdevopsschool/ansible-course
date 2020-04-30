#!/usr/bin/python
class FilterModule(object):
  def filters(self):
    return {
      'users_without_email': self.a_users_without_email
    }

  def a_users_without_email(self, users_input):
    users_output = []
    for user in users_input:
      if 'email' not in user:
        users_output.append(user['login'])
    return users_output

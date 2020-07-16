#!/usr/bin/python
class FilterModule(object):
  def filters(self):
    return {
      'users_without_hash': self.a_users_without_hash
    }
    
  def a_users_without_hash(self, users_input):
    users_output = []
    users = "" + users_input
    for user in users.splitlines():
      if user.find(":") > 0: 
            users_output.append(user[0 : user.find(":")])
      else:
	    users_output.append(user)
    return users_output
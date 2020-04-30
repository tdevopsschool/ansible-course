class TestModule:
  def tests(self):
    return {
      'has_email': lambda i: 'email' not in i
    }

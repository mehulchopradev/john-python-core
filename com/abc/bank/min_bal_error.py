class MinBalNotMaintainedError(Exception):
  def __init__(self, msg, account=None):
    super().__init__(msg)
    self.account = account

  def get_account(self):
    return self.account
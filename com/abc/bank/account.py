from .min_bal_error import MinBalNotMaintainedError

class Account:
  min_balance = 1000

  def __init__(self, acc_no, acc_type, acc_balance):
    self.acc_no = acc_no
    self.acc_type = acc_type
    self.acc_balance = acc_balance

  def deposit(self, amt):
    self.acc_balance += amt
    return self.acc_balance

  def withdraw(self, amt):
    print('Program starts...')

    try:
      if amt <= 0:
        raise ValueError('Amt to withdraw must be non zero positive')

      if self.acc_balance - amt < Account.min_balance:
        raise MinBalNotMaintainedError('Amt to wihdraw causing min bal to go down', self)

      self.acc_balance -= amt
      return self.acc_balance
    finally:
      # executes always irrespective of whatever happens in the corresponding try block
      print('Program ends')

  def __str__(self):
    return 'Acc No: {0}\nBalance: {1}'.format(self.acc_no, self.acc_balance)
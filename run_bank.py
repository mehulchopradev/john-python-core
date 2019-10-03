from com.abc.bank.account import Account
from com.abc.bank.min_bal_error import MinBalNotMaintainedError
from traceback import print_exc

a = Account(1001, 'Savings', 9000)

try:
  ub = a.withdraw(8500)
except MinBalNotMaintainedError as e:
  print(e.get_account())
  print_exc()
except ValueError:
  print_exc()
else:
  print(ub)
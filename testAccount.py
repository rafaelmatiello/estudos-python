from bank import Account, Bank3Account

contaRafael = Account(10)
print(contaRafael.__class__)
print(type(contaRafael))


contabb = Bank3Account(10, '123')
contabb.deposit(500.00)
print(contabb.get_total())
contabb.withdraw(50.00)
print(contabb.get_total())
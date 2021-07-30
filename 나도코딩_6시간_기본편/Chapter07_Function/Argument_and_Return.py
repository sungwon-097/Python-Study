def deposit(balande, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balande+money))
    return balande+money

balance=0
balance=deposit(balance, 1000)

def withdraw(balance, money):
    if balance>=money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance=1000
balance=withdraw(balance, 500)
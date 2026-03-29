bank_details = [{
    'acc_username' : 'Dikshant',
    'acc_no' : 123456789,
    'acc_type' : 'Savings',
    'acc_balance' : 10000,
    'open_date' : '20-3-2026'
},
{
    'acc_username' : 'darshan',
    'acc_no' : 987654321,
    'acc_type' : 'Current',
    'acc_balance' : 20000,
    'open_date' : '10-3-2026'
}
]

class account:

    def __init__(self,acc_username,acc_no,acc_type,acc_balance,open_date):
        self.acc_username = acc_username
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.acc_balance = acc_balance
        self.open_date = open_date

    def bankacc_details(self):
        print('-'*10)
        print(f'Account user : {self.acc_username}')
        print(f'Account No : {self.acc_no}')
        print(f'Account type : {self.acc_type}')
        print(f'Account balance : {self.acc_balance}')
        print(f'Account opening date : {self.open_date}')
        print('-'*10)

class acc_details(account):

    def __init__(self, details_acc):
        super().__init__(details_acc.get('acc_username'),details_acc.get('acc_no'),details_acc.get('acc_type'),details_acc.get('acc_balance'),details_acc.get('open_date'))
        print('This is Account details')

class money_deposit(account):

    def __init__(self, details):
        super().__init__(details.get('acc_username'),details.get('acc_no'),details.get('acc_type'),details.get('acc_balance'),details.get('open_date'))

    def deposit(self,amount):
        self.acc_balance = self.acc_balance + amount
        print(f'account number : {self.acc_no} deposited with {amount}')
        
m1 = money_deposit(bank_details[1])
m1.bankacc_details()
m1.deposit(3000)
m1.bankacc_details()









class Account:
    def __init__(self,Accname,intileBalance):
        self.name = Accname
        self.balance = intileBalance

        print(f'\nAccount "{self.name}" was created with a balance of ${self.balance:.2f} ')



class Transaction(Account):
    def __init__(self,title,amount,type,note=''):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note


    def display(self):
        print(f'Transaction...\nExpense:{self.title}\nAmount:${self.amount:.2f}\nType:{self.type}\nNote:{self.note}')
 
    def __repr__(self):
        return f'\nExpense:{self.title}\nAmount:${self.amount:.2f}\nType:{self.type}\nNote:{self.note}'


class Bank:
    def __init__(self):
        self.wallet = []

    #add trasanction to wallet
    def addTrans(self,transaction):
        self.wallet.append(transaction)
        print(f'\nSuccesfully added')


    #remove transaction/Title from wallet
    def removeTrans(self,title):
        found = False
        for obeject in self.wallet:
            if obeject.title == title:
                self.wallet.remove(obeject)
                print(f'\n{title} has been removed')
                found = True
                break
            if not found:
                print(f'\n{title} was not found')


    #display all the transaction's
    def displayTransactions(self):
        if not self.wallet:
            print(f'\nYours transactions is empty')
        else:
            print(f'\nTransaction log\n')
            for trans in self.wallet:
                print(trans)

    




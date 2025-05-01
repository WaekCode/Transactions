from TransactionBankStatemnet import *

Wallet_Transactions = Bank()

run = True
while run:
    print('====BankSystem====')
    print('1.add')
    print('2.remove')
    print('3.display')
    print('4.exit')
    choice = int(input('/:'))
    if choice == 1:
        title =input('title: ')
        try:
            amount = float(input('amount: '))
        except ValueError as f:
            print('Amount need to be a float')
            continue
        type = input('type: ')
        note = input('note: ')
        Trans = Transaction(title,amount,type,note)
        Wallet_Transactions.addTrans(Trans) 

    elif choice == 2:
        Removed_title = input('what title would you like to remove: ').lower()
        Wallet_Transactions.removeTrans(Removed_title)
    elif choice ==3:
        Wallet_Transactions.displayTransactions()

    elif choice == 4:
        break

        

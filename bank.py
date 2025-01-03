# bank account system 
def account_holder(name):
    account = { 
        "name" :name,
        "balance" : 0,
        "transection" :[] 
    }
    return account
def deposit (ammount,account):
    try:
        if ammount < 0:
            print("Invalid amount! must be in positive")
        else:
            print(f"deposited ! before deposit balance is : {account['balance']}")
            account['balance'] += ammount
            account['transection'].append(f"Type : deposit ; deposit ammount {ammount} ;new balance => {account['balance']}")
            with open("transection.txt" , 'a+') as transection_details :
                transection_details.write(f"Type : deposit ; deposit ammount {ammount} ;new balance => {account['balance']} \n")
            return account
    except ValueError as VE:
        print(VE)
    except Exception as E:
        print(f"unknown error occures :{E}")
    
def withdraw(ammount,account):
    try:
        if ammount > account['balance']:
            print(f"insufficent balance")
            return account
        print(f"withdrawal ! before withdraw balance is : {account['balance']}")
        if account['balance'] > 0 :
            account['balance'] -= ammount
            account['transection'].append(f"Type : withdraw ; withdraw ammount {ammount} ; new balance => {account['balance']}")

        with open("transection.txt" , 'a+') as transection_details :
            transection_details.write(f"Type : withdraw ; deposit ammount {ammount} ;new balance => {account['balance']} \n")
        
        return account
    except ValueError as VE:
        print(VE)
    except Exception as E:
        print(f"unknown error occures :{E}")
    
def check_balance(account):
    try:
    
        print(f"your balance is : {account['balance']}")
    except Exception as E: 
        print(f"unknown error occures :{E}")

def show_account_details(account):
    try:
        print(f"account holder name : {account['name']}")
        print(f"account balance : {account['balance']}")
        if not account['transection']:
            print("no transection occured!")
        else:
            with open("transection.txt","a+") as transection_details:
                transection_details.write(f"account holder name:{account['name']}")
            for transection in account['transection']:
                print(transection)
    except Exception as E:
        print(f"unknown error occures :{E}")

useraccount = account_holder("hanzala")
check_balance(useraccount)
withdraw(0,useraccount)
show_account_details(useraccount)


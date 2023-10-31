#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os


# In[17]:


def initialize_balance():
    balance = 0 
    file_path = 'transaction_history.txt'
    
    
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            transactions = file.read().splitlines()
            for transaction in transactions:
                if transaction.replace(".", "", 1).isdigit():
                    amount = float(transaction)
                    balance += amount
                    
    return balance


# In[24]:


def save_transaction(amount):
    with open('transaction_history.txt', 'a') as file:
        file.write(str(amount) + '\n')


# In[25]:


def veiw_balance():
    balance = initialize_balance()
    print(f'current balance: ${balance:.2f}')


# In[36]:


def add_debit():
    amount_str = input("enter the amount to withdraw: $")
    if amount_str.replace(".", "", 1).isdigit():
        amount = float(amount_str)
        if amount > 0:
            balance = initialize_balance()
            save_transaction(-amount)
            print(f"withdrew ${amount:.2f}. Current balance: ${balance - amount:.2f}")
        else:
            print("invalid amount, enter a positive number.")
    else:
        print("invalid input, enter a valid number.")


# In[40]:


def add_credit():
    amount_str = input("Enter the amount to deposit: $")
    if amount_str.replace(".", "", 1).isdigit():
        amount = float(amount_str)
        if amount > 0:
            save_transaction(amount)
            balance = initialize_balance()
            print(f"Deposited ${amount:.2f}. Current balance: ${balance + amount:.2f}")
        else:
            print("invalid amount, enter a positive number.")
    else:
        print("invalid input, enter a valid number.")

    


# In[41]:


#interface part 


# In[42]:


while True:
    print('Welcome to your termial checkbook\n \nWhat would you like to do? \n')
    
    print('1.Veiw current balance')
    print('2.add a debit (withdraw)')
    print('3.add a credit(deposite)')
    print('4.exit')
    choice = input('select one of the option above ')
    
    
    if choice =='1':
        veiw_balance()
    elif choice == '2':
        add_debit()
    elif choice == '3':
        add_credit()
    elif choice == '4':
        print('shutting down')
        break
    else:
        print('choice one of the four choice you have')
                            


# In[ ]:





# In[ ]:





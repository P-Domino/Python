### Functions define code which is executed Later (and possibly Multiple Times)
### Building Functions for our blockchain

# blockchain = []
# def add_value(): 
#     blockchain.append(12.3) # adding value to the list 
#     print(blockchain)
#
# add_value()
 
# blockchain = [[1]]
#
# def add_value(): # if it works only, it will have a given value on the start of the list
#     blockchain.append(blockchain[0], 12.3) # adding value to choosen place on the list 
#     print(blockchain)

# add_value()

# number with minus operator in list indicatng the last element of the list 
# ex blockchain[-1] - last element of the list

# blockchain = [[1]]
# 
# def add_value(): 
#     blockchain.append([blockchain[-1], 12.3]) # accessing list from the right  
#     print(blockchain)

# add_value()
# add_value()
# add_value()

### Last element will be old blockchainn

# blockchain = [[1]]
# 
# Passing arguments to the function
# def add_value(transaction_amount): 
#     blockchain.append([blockchain[-1], transaction_amount]) # accessing list from the right  
#     print(blockchain)
#
# add_value(0.1)
# add_value(1)
# add_value(12.2)


# # Passing and return value from function
# blockchain = [[1]]
# 
#  def get_last_blockchain_value():
#     return blockchain[-1] # accessing list from the right 
#
# ### We should have two blank spaces between functions in python
#
# def add_value(transaction_amount): 
#     blockchain.append([get_last_blockchain_value(),transaction_amount])  
#
#
# add_value(1)
# add_value(0.1)
# add_value(123)
#
# print(blockchain)



# Using Default values 
# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1] # accessing list from the right 

# ### We should have two blank spaces between functions in python

# def add_value(transaction_amount, last_transaction = [1]): 
#     blockchain.append([last_transaction, transaction_amount])  
    

# add_value(1) 
# add_value(0.1, get_last_blockchain_value())
# add_value(123, get_last_blockchain_value())

# print(blockchain)

# Using Keyword Arguments (kwargs)

# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1] # accessing list from the right 

# ### We should have two blank spaces between functions in python

# def add_value(transaction_amount, last_transaction = [1]): 
#     blockchain.append([last_transaction, transaction_amount])  
    

# add_value(1) 
# add_value(last_transaction = get_last_blockchain_value(), transaction_amount = 0.1) 
# add_value(123, get_last_blockchain_value())

# print(blockchain)

# Getting some input 

# blockchain = []

# def get_last_blockchain_value():
#     return blockchain[-1] # accessing list from the right 

# ### We should have two blank spaces between functions in python

# def add_value(transaction_amount, last_transaction = [1]): 
#     blockchain.append([last_transaction, transaction_amount])  
    

# # User input
# # Everything treated with input will be treated as text -> string
# tx_amount = float(input('Your transaction amount please:'))
# add_value(tx_amount)

# tx_amount = float(input('Your transaction amount please:'))
# add_value(tx_amount)

# tx_amount = float(input('Your transaction amount please:'))
# add_value(tx_amount)

# print(blockchain)

# avoiding repetition with new function
blockchain = []

def get_last_blockchain_value():
    return blockchain[-1] # accessing list from the right 

### We should have two blank spaces between functions in python

def add_value(transaction_amount, last_transaction = [1]): 
    blockchain.append([last_transaction, transaction_amount])  
    

def get_user_input():
    return float(input('Your transaction amount please:'))

# User input
# Everything treated with input will be treated as text -> string
tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount)

print(blockchain)
#Initializing our (empty) blockchain list
from opcode import hascompare

MINNINGREWARD = 10 

genesisBlock = {
    'previousHash': '', 
    'index': 0, 
    'transactions': []
}
blockchain = [genesisBlock]
openTransactions = []
owner = 'Dominik'
participants = {'Dominik'}

def hashBlock(block):
    return '-'.join([str(block[key]) for key in block])


def getBalance(participant):
    txSender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amountSent = 0
    for tx in txSender:
        if len(tx) > 0:
            amountSent += tx[0]
    txRecipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amountReceived = 0
    for tx in txRecipient:
        if len(tx) > 0:
            amountReceived += tx[0]
    balance = amountReceived - amountSent
    return balance
    

def getLastBlockchainValue():
    """Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

""" This function accepts two arguments.
    One required (transactionAmount) and one optional one (lastTransaction)
    The Optional one is optional because it has a default value => [1]
"""

def addTransaction(recipient, sender = owner, amount = 1.0):
    """Append a new value as well as the last blockchain value to the blockchain

       Arguments:

        :sender: sender of the coins.
        :recipient: The recipient of the coins .
        :amount: The amount of the coins sent with the transaction (default = 1.0).
    """
    transaction = {
        'sender': sender,
        'recipient': recipient, 
        'amount': amount
    }
    openTransactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)

def mineBlock():
    lastBlock = blockchain[-1]
    hashedBlock = hashBlock
    print(hashedBlock)
    # the same as above with use of for loop 
    # for key in lastBlock:
    #     value = lastBlock[key]
    #     hashedBlock = hashedBlock + str(value)
    print(hashedBlock)
    rewardTransaction = {
        'sender': 'MINNING',
        'recipient': owner,
        'amount': MINNINGREWARD 
    }
    block = {
        'previousHash': 'XYZ', # entered dummy for educational purposes 
        'index': len(blockchain), 
        'transactions': openTransactions,
    } 
    blockchain.append(block)
    return True


def getTransactionValue():
    """Returns the input of the user (a new transaction amount) as a float."""
    # Get the user input, transform it from a string to a float and store it
    txRecipient = str(input('Enter the recipient of the transaction: '))
    txAmount = float(input('Your transaction value: '))
    return txRecipient, txAmount

def getUserChoice():
    """Prompts User for its choice and return it."""
    userInput = input('Your choice: ')
    return userInput 

def printBlockchainElements():
    """Output all  blocks of the blockchain."""
    for block in blockchain:
        print('Outputting block!')
        print(block)
        print('-'*20)

def verifyChain():
    """Verify the current blockchain and return True if it's valid, false..."""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previousHash'] != hashBlock(blockchain[index-1]):
            return False
    return True

    
    # Old Logic
    # isValid = True
    # for blockIndex in range(len(blockchain)):
    #     if blockIndex == 0:
    #         # If we're checking the first block, we should skip iteration
    #         continue
    #     # Check the previous block (the entire one) vs the first element of the blockchain
    #     elif blockchain[blockIndex][0] == blockchain[blockIndex - 1]:
    #         isValid = True
    #     else:
    #         isValid = False
    # return isValid


waitingForUserInput = True

""" A while loop for the user input interface
    It's a loop that exists once waitingForUserInput becomes False or when break encountered
"""
while waitingForUserInput:
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2. Mine a new block')
    print('3. Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    userChoice = getUserChoice()
    if userChoice ==  '1':
        txData = getTransactionValue()
        recipient, amount = txData
        # Add the transaction to the blockchain
        addTransaction(recipient, amount = amount)
        print(openTransactions)
    elif userChoice == '2':
        if mineBlock():
            openTransactions = []
    elif userChoice == '3':
        printBlockchainElements()
    elif userChoice == '4':
        print(participants)
    elif userChoice == 'h':
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previousHash': '', 
                'index': 0, 
                'transactions': [{
                    'sender': 'Jacob',
                    'recipient': owner, 
                    'amount': 123.12
                }]
            }
    elif userChoice == 'q':
        waitingForUserInput = False
    else:
        print('Invalid input, please choose one from the list.')
    if not verifyChain():
        printBlockchainElements()
        print('Invalid blockchain!')
        break
    print(getBalance('Dominik'))
else:
    print('User Left!')


print('Done!')
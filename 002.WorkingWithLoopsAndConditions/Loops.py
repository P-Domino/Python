# initialiazing our (empty) blockchain list
blockchain = []

def getLastBlockchainValue():
    """Returns the last value of the currnet blockchain"""
    if len(blockchain) < 1:
        return None # simply used to tell program there is nothing
    return blockchain[-1]


# This function accept two arguments.
# One required one (transactionAmount) and one optional one (lastTransaction)
# The optional one is optional because it has default value => [1]
def addTransaction(transactionAmount, lastTransaction = [1]):
    """ Append a new value as well as the last blockchain value to the blockchain

        Arguments:
            :transactionAmount: The amount that should be added.
            :lastAmount: The last blockchain transaction (default [1])
    """
    if lastTransaction == None:
        lastTransaction = [1]
    blockchain.append([lastTransaction, transactionAmount])
    

def getTransactionValue():
    """Returns the user input, transform it from a string to a float and store it"""
    userInput = float(input('Your transaction amount value: '))
    return userInput

def getUserChoice():
    userInput = raw_input('Your Choice: ')
    if type(userInput) is str:
        return userInput
    else:
        return str(userInput)


def printBlockchainElements():
    # Output the blockchain to the console 
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verifyChain():
    # blockIndex = 0
    isValid = True
    for blockIndex in range(len(blockchain)):
        if blockIndex == 0:
            continue
        if blockchain[blockIndex][0] == blockchain[blockIndex - 1]: 
            isValid = True
        else:
            isValid = False
            break
    # Old loop without using range
    # for block in blockchain:
    #     if blockIndex is 0:
    #         blockIndex =+ 1
    #         continue
    #     print(block)
    #     if block[0] is blockchain[blockIndex - 1]: 
    #         isValid = True
    #     else:
    #         isValid = False
    #         break
    #     blockIndex += 1
    return isValid


waitingForInput = True

while waitingForInput:
    print('Please choose')
    print('1: Add new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    userChoice = getUserChoice()
    if userChoice == '1':
        txAmount = getTransactionValue()
        addTransaction(txAmount, getLastBlockchainValue())
    elif userChoice == '2':
        printBlockchainElements()
    elif userChoice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif userChoice == 'q':
        writingTheInput = False
    else:
        print('Invalid input, please choose one from the list.')
    if not verifyChain():
        printBlockchainElements()
        print('Invalid blockchain!')
        break

print('Done!')
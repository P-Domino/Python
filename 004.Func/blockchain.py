import functools
# The reward we give to miners (for creating a new block)
MINING_REWARD = 10

# Our starting block for the blockchain
genesisBlock = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
# Initializing our (empty) blockchain list
blockchain = [genesisBlock]
# Unhandled transactions
openTransactions = []
# We are the owner of this blockchain node, hence this is our identifier (e.g. for sending coins)
owner = 'Dominik'
# Registered participants: Ourself + other people sending/ receiving coins
participants = {'Dominik'}



def hashBlock(block):
    """Hashes a block and returns a string representation of it.
    
    Arguments:
        :block: The block that should be hashed.
    """
    return '-'.join([str(block[key]) for key in block])


def getBalance(participant):
    """Calculate and return the balance for a participant.

    Arguments:
        :participant: The person for whom to calculate the balance.
    """
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of transactions that were already included in blocks of the blockchain
    txSender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of open transactions (to avoid double spending)
    openTxSender = [tx['amount'] for tx in openTransactions if tx['sender'] == participant]
    txSender.append(openTxSender)
    amountSent = functools.reduce(lambda txSum, txAmt: txSum + sum(txAmt) if len(txAmt) > 0 else txSum + 0, txSender, 0)
    # Calculate the total amount of coins sent
    # This fetches received coin amounts of transactions that were already included in blocks of the blockchain
    # We ignore open transactions here because you shouldn't be able to spend coins before the transaction was confirmed + included in a block
    txRecipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amountReceived = functools.reduce(lambda txSum, txAmt: txSum + sum(txAmt) if len(txAmt) > 0 else txSum + 0, txRecipient, 0)
    # Return the total balance
    return amountReceived - amountSent


def getLastBlockchainValue():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verifyransaction(transaction):
    """Verify a transaction by checking whether the sender has sufficient coins.

    Arguments:
        :transaction: The transaction that should be verified.
    """
    senderBalance = getBalance(transaction['sender'])
    return senderBalance >= transaction['amount']

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def addTransaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verifyransaction(transaction):
        openTransactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mineBlock():
    """Create a new block and add open transactions to it."""
    # Fetch the currently last block of the blockchain
    last_block = blockchain[-1]
    # Hash the last block (=> to be able to compare it to the stored hash value)
    hashed_block = hashBlock(last_block)
    # Miners should be rewarded, so let's create a reward transaction
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    # Copy transaction instead of manipulating the original openTransactions list
    # This ensures that if for some reason the mining should fail, we don't have the reward transaction stored in the open transactions
    copied_transactions = openTransactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True


def getTransactionValue():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    txRecipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return txRecipient, tx_amount


def getUserChoice():
    """Prompts the user for its choice and return it."""
    user_input = input('Your choice: ')
    return user_input


def printBlockchainElements():
    """ Output all blocks of the blockchain. """
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verifyChain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hashBlock(blockchain[index - 1]):
            return False
    return True


def verifyTransactions():
    """Verifies all open transactions."""
    return all([verifyransaction(tx) for tx in openTransactions])


waitingForInput = True

# A while loop for the user input interface
# It's a loop that exits once waitingForInput becomes False or when break is called
while waitingForInput:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    userChoice = getUserChoice()
    if userChoice == '1':
        txData = getTransactionValue()
        recipient, amount = txData
        # Add the transaction amount to the blockchain
        if addTransaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(openTransactions)
    elif userChoice == '2':
        if mineBlock():
            openTransactions = []
    elif userChoice == '3':
        printBlockchainElements()
    elif userChoice == '4':
        print(participants)
    elif userChoice == '5':
        if verifyTransactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif userChoice == 'h':
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Dominik', 'amount': 100.0}]
            }
    elif userChoice == 'q':
        # This will lead to the loop to exist because it's running condition becomes False
        waitingForInput = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verifyChain():
        printBlockchainElements()
        print('Invalid blockchain!')
        # Break out of the loop
        break
    print('Balance of {}: {:6.2f}'.format('Dominik', getBalance('Dominik')))
else:
    print('User left!')


print('Done!')

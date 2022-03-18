import functools
import hashlib as hl
from collections import OrderedDict

from hashUtil import hashBlock, hashString256
# The reward we give to miners (for creating a new block)
MININGREWARD = 10

# Our starting block for the blockchain
genesisBlock = {
    'previousHash': '',
    'index': 0,
    'transactions': [],
    'proof': 100 # dummy value
}
# Initializing our (empty) blockchain list
blockchain = [genesisBlock]
# Unhandled transactions
openTransactions = []
# We are the owner of this blockchain node, hence this is our identifier (e.g. for sending coins)
owner = 'Dominik'
# Registered participants: Ourself + other people sending/ receiving coins
participants = {'Dominik'}





def validProof(transactions, lastHash, proof):
    guess = str(transactions) + str(lastHash) + str(proof).encode()
    guessHash = hl.sha256(guess).hexdigest
    print(guessHash)
    return guessHash[0:2] == '00'   # check to determine if hash(proof) is valid


def proofOfWork():
    lastBlock = blockchain[-1]
    lastHash = hashBlock(lastBlock)
    proof = 0
    while not validProof(openTransactions, lastHash, proof):
        proof += 1
    return proof


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

    Arguments
        :transaction: The transaction that should be verified.
    """
    senderBalance = getBalance(transaction['sender'])
    return senderBalance >= transaction['amount']

# This function accepts two arguments.
# One required one (transactionAmount) and one optional one (lastTransaction)
# The optional one is optional because it has a default value => [1]


def addTransaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    # old transaction dictionary logic
    # transaction = {
    #     'sender': sender,
    #     'recipient': recipient,
    #     'amount': amount
    # }
    transaction = OrderedDict([
            ('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verifyransaction(transaction):
        openTransactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mineBlock():
    """Create a new block and add open transactions to it."""
    # Fetch the currently last block of the blockchain
    lastBlock = blockchain[-1]
    # Hash the last block (=> to be able to compare it to the stored hash value)
    hashedBlock = hashBlock(lastBlock)
    proof = proofOfWork()

    # Miners should be rewarded, so let's create a reward transaction
    # Old Logic
    # rewardTransaction = {
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MININGREWARD
    # }
    rewardTransaction = OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MININGREWARD)])
    # Copy transaction instead of manipulating the original openTransactions list
    # This ensures that if for some reason the mining should fail, we don't have the reward transaction stored in the open transactions
    copiedTransactions = openTransactions[:]
    copiedTransactions.append(rewardTransaction)
    block = {
        'previousHash': hashedBlock,
        'index': len(blockchain),
        'transactions': copiedTransactions,
        'proof': proof
    }
    blockchain.append(block)
    return True


def getTransactionValue():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in userInput
    txRecipient = input('Enter the recipient of the transaction: ')
    txAmount = float(input('Your transaction amount please: '))
    return txRecipient, txAmount


def getUserChoice():
    """Prompts the user for its choice and return it."""
    userInput = input('Your choice: ')
    return userInput


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
        if block['previousHash'] != hashBlock(blockchain[index - 1]):
            return False
        if not validProof(block['transactions'][:-1], block['previousHash'], block['proof']):
            print('Proof of work is invalid')
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
                'previousHash': '',
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

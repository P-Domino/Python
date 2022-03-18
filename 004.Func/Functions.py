def unlimitedArguments(*args, **keywordArgs):  # Asterix allows unpacking functions arguments
    print(keywordArgs)                         # We can handle named arguments with double asterix synthax, it gives us dicitionary
    for k,argument in keywordArgs.items():
        print(k, argument)

unlimitedArguments(1,2,3,4)

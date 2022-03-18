# Write a normal function that accepts another fucntion as an argument. Output the result of that other function in your "normal" function.
def transformData(fn):
    print(fn(10))
# Call your "normal" function by passing a lambda function - which performs any operation of your choice - as an arg.
transformData(lambda data: data + 5)
# Tweak your normal function by allowing an infinite amount of argumnents on which your lambda will be executed.
def transformData2(fn, *args):
    for arg in args:
        print('Result: {:^20.2f}'.format(fn(arg)))


transformData2(lambda data: data / 5, 10 ,15, 20, 25)
# Format the output of your "normal" functions such that numbers look nice and are centered in a 20 character column.
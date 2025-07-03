import hashlib


unknown_hash = str(input('enter the hash: '))

chars = list(map(chr, range(33, 127))) # it's list of chars 
n = len(chars)
for i in range(n**4):
    combo = []
    num = i
    for _ in range(4):
        combo.append(chars[num % n])
        num = num // n
    x = ''.join(combo)
    print(x)
    test_hash_pre = hashlib.sha256(x .encode()) # in this line and text line I hash guess
    test_hash = test_hash_pre.hexdigest()
    if test_hash == unknown_hash:
        # this if check the the hash of char and main hash
        print('your password is :',x)
        break



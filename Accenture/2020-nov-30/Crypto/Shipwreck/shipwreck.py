import binascii

a = 0x446a5f657957656562705f71676a7b
b = 0x42685d6377556363606e5d6f656879
c = 0x40665b61755361615e6c5b6d636677

d = 0x3864595f73515f5f5c6a596b616475
e = 0x3662575d714f5d5d5a6857695f6273
f = 0x3460555b6f4d5b5b586655675d6071

g = 0x325e53596d4b5959566453655b5e6f
h = 0x305c51576b49575754625163595c6d
i = 0x285a4f556947555552604f61575a6b

lst = [a, b, c, d, e, f, g, h, i]
ones = 0x010101010101010101010101010101
twos = ones + ones

for i in range(len(lst) - 1):
    # print(lst[i] - lst[i + 1])
    x = lst[i]
    print(bytearray.fromhex(hex(x)[2:]).decode())
    print(bytearray.fromhex(hex(x + twos)[2:]).decode())

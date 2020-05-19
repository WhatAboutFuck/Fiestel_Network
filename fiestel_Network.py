from bitarray import bitarray


def move(lst,steps):
    return lst[steps:] + lst[:steps]



def crypt(number,keys,flag):
    l,r = number[:len(number)//2],number[len(number)//2:]
    if flag == False:
        for key in keys:
            lst = r ^ move(l,key)
            r = l
            l = lst
        return r + l
    elif flag == True:
        for key in reversed(keys):
            lst = r ^ move(l,key)
            r = l
            l = lst
        return r + l

def bloks(num, block_size,keys,flag):
    len_num = num.bit_length()
    num = bin(num)[2::]
    if  len_num < block_size:
        return int(crypt(bitarray(((block_size - len_num)*'0' + num)),keys,flag).to01(),2)
    elif len_num == block_size:
        return int(crypt(bitarray(num),keys,flag).to01(),2)
    else:
        full_num = (block_size - len_num % block_size)*'0' + num
        answer = []
        for i in range(0, len(full_num), block_size):
            answer.append(crypt(bitarray(full_num[i:i+block_size]),keys,flag).to01())
        return int(''.join(answer),2)

print(bloks(222,18,[1,2,3,4],False))
print(bloks(140865,18,[1,2,3,4],True))

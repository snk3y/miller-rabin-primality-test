from random import randrange
import sys


def is_probably_prime(very_long_num, num_of_loop=8):
    if very_long_num == 2:
        return True
    #num & 1 は偶数を弾くことができる。
    if very_long_num < 2 or very_long_num & 1 == 0:
        return False
        
    #2**s * d のdを求める。
    rest = (very_long_num - 1) >> 1
    while rest & 1 == 0:
        rest = rest >> 1

    for i in range(num_of_loop):
        if is_composite(rest, very_long_num):
            return False
    return True


def is_composite(rest, very_long_num):
    a = randrange(1, very_long_num)
    if pow(a, rest, very_long_num) == 1:
        return False
    #r <- 0 to s-1 においてa**(2**r * d) % n != -1かどうかを確かめる。
    exponent = rest#r = 0
    while exponent < very_long_num - 1:
        if pow(a, exponent, very_long_num) == very_long_num - 1:
            return False
        exponent = exponent << 1
    return True


if __name__ == "__main__":
    input_list = sys.argv
    if len(input_list) != 2 or not input_list[1].isdigit():
        print("USAGE: python3 %s <number>" % input_list[0])
        sys.exit()

    if is_probably_prime(int(input_list[1])):
        print("It is probably a prime number!!!!")
    else:
        print("It's not a prime number.")

Set swap bit(src)
# I wouldn't recommend writing this as one line due to complex order of ops
         Bit odd = (src & 10_10_10_10) >> 1
         Biteven = (src & 01_01_01_01) << 1
         Swap1 = bitodd or biteven
         
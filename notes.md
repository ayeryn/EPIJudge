# Notes on problem sets

## count_bits.py
- `x & 1`: checks if the last bit is set

## parity.py
### Drop to lowest setting bit   
```
x & ( x - 1)
```

Example:
```
25 = (1101)
24 = (1100)
  1101
& 1100
--------
  1100
```

### XOR is associative
```
Let P be the parity function.

# end is inclusive in the following notation
P(b[0:63]) = P(b[0:31]) XOR P(b([32:63]))
```
### Breakdown of the most optimal parity function
We will illustrate with an 8-bit integer `n = (11010111)`

#### Round 1: Compute the parity of the higher half and lower half (`b[0:3] ^ b[4:7]`)
```
n = n ^ ( n >> 4)
n      = (11010111)
n >> 4 = (00001101)

   11010111
 ^ 00001101
 ----------
   11011010   

n = (11011010)
```
>**Note:** the higher half of the *new `n`* carries the *old* higher half bits. This is ok because **only the lowest bit** will be observed and compared at the end. 

> To visually emphasize the meaningful bits, we will mark the non-import bits with x ==> `n = xxxx1010`

#### Round 2: Compute the parity of the lower half of `n` by further halving the bits (`b[4:5] ^ b[6:7]`)
```
n = n ^ ( n >> 2)
n      = (xxxx1010)
n >> 2 = (xxxxxx10)

   xxxx1010
 ^ xxxxxx10
 ----------
   xxxxxx00   

n = (xxxxxx00)
```

#### Round 3: Repeat (`b[6] ^ b[7]`)
```
n = n ^ ( n >> 1)
n      = (xxxxxx00)
n >> 1 = (xxxxxxx0)

   xxxxxx00
 ^ xxxxxxx0
 ----------
   xxxxxxx0   

n = (xxxxxxx0)
```
#### Final: Observe the last bit
Now we have computed the parity of `n` by repeatedly taking performing XOR on the higher and lower half of the meaningful bits of `n` and updating `n`. We need to find out what the final bit is. Everything `& 1` is itself. Therefore we get the value of `n` by `n = n & 0x1`

> Remember that the leading bits are meaningless to us, thus the "`1`" we use at the end has leading `0`s
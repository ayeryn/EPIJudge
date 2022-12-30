# Notes on problem sets

## count_bits.py (4.0)
- `x & 1`: checks if the last bit is set

## parity.py (4.1)
Let `P` be the parity function.
### Drop to lowest setting bit   
```
x & ( x - 1)
```

Example:
```
13 = (1101)
12 = (1100)
  1101
& 1100
--------
  1100
```
### Important Property
- The logic of parity is the same of `XOR`. `XOR` of the same bits results in `0`, meaning
    - `P(00) = 0` since there are no `1`s
    - `p(11) = 0` since the number os `1`s is even

- XOR is associative: `a ^ b ^ c = (a ^ b) ^ c = a ^ (b ^ c) = c ^ b ^ a`

Therefore, 
```
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

## power_x_y.py (4.7)
To improve the performance, we reduce the amount of multiplication done per step.

### Properties of exponentiation
> <code>x<sup>(a+b)</sup> = x<sup>a</sup>x<sup>b</sup></code>

Example:

<code>x = 10 = (1010)<sub>2</sub>

x<sup>(1010)<sub>2</sub></sup> = x<sup>(101)<sub>2</sub>+(101)<sub>2</sub></sup> = x<sup>(101)<sub>2</sub></sup>·x<sup>(101)<sub>2</sub></sup>  

x<sup>(101)<sub>2</sub></sup> = x<sup>(100)<sub>2</sub>+(1)<sub>2</sub></sup> = x<sup>(10)<sub>2</sub></sup>·x<sup>(10)<sub>2</sub></sup>·x<sup>(1)<sub>2</sub></sup>
</code>


Generalizing - 
- if `y >= 1`
    - if `y` is even, <code>x<sup>y</sup> = x<sup>(y/2)*2</sup></code>
    - if `y` is odd, <code>x<sup>y</sup> = x<sup>(y/2)*2</sup>·x</code>

- if `y < 0`
> **Note**: <code>x<sup>y</sup> = 1/x<sup>|y|</sup></code><br>
Because the *inverse of multiplication is **division***  

Example:  
<code>x = 10 = (1010)<sub>2</sub>

x<sup>-(1010)<sub>2</sub></sup><br> = 1/x<sup>(1010)<sub>2</sub></sup>
= 1/x<sup>(101)<sub>2</sub>+(101)<sub>2</sub></sup> = 1/x<sup>(101)<sub>2</sub></sup>·x<sup>(101)<sub>2</sub></sup>  

x<sup>-(101)<sub>2</sub></sup><br>
= 1/x<sup>(101)<sub>2</sub></sup>
= 1/x<sup>(100)<sub>2</sub>+(1)<sub>2</sub></sup> = 1/x<sup>(10)<sub>2</sub></sup>·x<sup>(10)<sub>2</sub></sup>·x<sup>(1)<sub>2</sub></sup>
</code>

- if `y` is even, <code>x<sup>y</sup> = 1/x<sup>(|y|/2)*2</sup></code>
- if `y` is odd, <code>x<sup>y</sup> = 1/x<sup>(|y|/2)*2</sup>·x</code>

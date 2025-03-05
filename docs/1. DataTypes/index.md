# DataTypes

## Number Systems
There are 4 main number systems used in computing:

1. **Decimal**: Base 10, uses digits 0-9.
2. **Binary**: Base 2, uses digits 0 and 1.
3. **Hexadecimal**: Base 16, uses digits 0-9 and letters A-F.
4. **Octal**: Base 8, uses digits 0-7.

We will focus on the first three number systems in this course.

??? Extension "Octal"
    The octal number system is used most commonly in Unix-based systems, such as Linux and macOS to define file permissions. Octal numbers represent execution, read and write permissions respectively. For example, the number 7 in octal represents read, write and execute permissions for a file. The number 5 represents read and execute permissions only.

    eg: A file with permissions `755` in octal means that the owner has read, write and execute permissions (7), while the group and others have only read and execute permissions (5).

The table below represents the first 16 numbers in each number system

| Decimal | Hexadecimal | Binary   |
|---------|-------------|----------|
| 0       | 0x0         | 0000     |
| 1       | 0x1         | 0001     |
| 2       | 0x2         | 0010     |
| 3       | 0x3         | 0011     |
| 4       | 0x4         | 0100     |
| 5       | 0x5         | 0101     |
| 6       | 0x6         | 0110     |
| 7       | 0x7         | 0111     |
| 8       | 0x8         | 1000     |
| 9       | 0x9         | 1001     |
| 10      | 0xA         | 1010     |
| 11      | 0xB         | 1011     |
| 12      | 0xC         | 1100     |
| 13      | 0xD         | 1101     |
| 14      | 0xE         | 1110     |
| 15      | 0xF         | 1111     |

## Decimal
- Decimals are a core numerical type in the majority of software languages. 
- They are used to represent whole numbers and can be positive or negative.
- Integers, floats, doubles, and longs are all types of decimals.
    - Integer (int) - 5, -5, 45792
    - Float (float) - 5.2, -3.4
    - Double (double) - 5.234, -3.456789
    - Long (long) - 523456789, -34567890

!!! Note
    - In Python you only need to use `int` and `float`. There is no inbuilt `long` or `double` type.

## Binary
Binary is a base 2 number system. It uses only two digits: 0 and 1. Binary is used in computing because it can be easily represented by electronic circuits, which have two states: on or off. Every line of code you write as a software engineer is converted into binary code that the computer can understand. Any technology that you use today that is labelled as being digital is based on binary.

- To represent a decimal value in binary, you can use the built-in function `bin()` in Python. For example:
```python
print(bin(10))  # Output: '0b1010'
```
- Notice the `0b` prefix. This is used to indicate that the number is in binary format.

- The reverse is also possible. You can convert binary to decimal using the built-in function `int()` with base 2. For example:
```python
print(int('1010', 2))  # Output: 10
```

To count in binary, you can use the following table:

| Decimal | Binary |
|---------|--------|
| 0       | 0      |
| 1       | 1      |
| 2       | 10     |
| 3       | 11     |
| 4       | 100    |
| 5       | 101    |
| 6       | 110    |
| 7       | 111    |
| 8       | 1000   |
| 9       | 1001   |
| 10      | 1010   |

Take the number 10 for example. It is the sum of 2^3 + 2^1. So in binary, it is represented as `1010`.

### 2s Complement
2s complement is a way to represent signed integers in binary. It allows you to represent both positive and negative numbers using the same number of bits. The most significant bit (MSB) represents the sign of the number, where `0` indicates a positive number and `1` indicates a negative number.

In the example above, the number 10 is represented as `01010` in 2s complement, notice the `0` at the beginning. To represent -10 in 2s complement, you need to invert all the bits starting from the first `1` from the left. In this case, it would be `10110`. 

The key think to note here is that when there are `n` bits to represent a number, the range is from `-2^(n-1)` to `2^(n-1)-1`. For example, with 4 bits, the range is from -8 to 7.

### Bitwise Operations

One of the most versatile operations in programming is bitwise operations. It allows you to manipulate individual bits of a number. Typically they are used to perform low-level operations on data, such as setting or clearing bits in a register, flags for features being on or off, complex yet fast matching of patterns, separating communications data and compressing data.

#### AND (&)
This operation compares each bit of its first operand to the corresponding bit of its second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, it is set to 0. A good example of this 

#### OR (|)
This operation compares each bit of its first operand to the corresponding bit of its second operand. If either bit is 1, the corresponding result bit is set to 1. Otherwise, it is set to 0. A good example of this is when you want to turn on a specific feature in a program.

Your binary data might be `0100` with each bit representing a feature flag. The example here indicates that the first feature is on. To turn on the second feature, you would use `0100 | 0010 = 0110` and to check if first feature is on, you would use `0100 & 0100 != 0`. 

#### XOR (^)
This operation called "exclusive or" compares each bit of its first operand to the corresponding bit of its second operand. If the bits are different, the corresponding result bit is set to 1. Otherwise, it is set to 0. This is used in cryptography to scramble data by using a key to change only certain bits. If you have the same data encrypted twice with different keys, you can XOR them to get back the original data. Another use is in parity checks to ensure data is not corrupted.

#### NOT (~)
This operation is the bitwise negation of its operand. It flips all the bits in a binary number. For example, `~0100` is `1011`. You can use this to to quickly convert a binary number to its two's complement representation, which is the bitwise not of the value minus 1. 

#### Left (<<) and Right Shift (>>)
These are commonly used in games to do integer division/multiplication by powers of 2, as well as in graphics programming to manipulate pixel data.

??? Extension "Endianess"

    Different uses of binary have different endianess. Endianess refers to the order in which bytes are stored in memory, either from most significant byte (MSB) to least significant byte (LSB), or vice versa. There are two types of endianness: little-endian and big-en`dian. For example, Intel uses little-endian, while ARM uses big-endian. This means that the most significant bit (MSB) may be on the left or right depending on the system.

## Hexadecimal
The most common use of hexadecimals is in colour codes, where each colour component (red, green, blue) is represented by a two-digit hexadecimal number. For example, the colour white is represented as `FFFFFF` in hexadecimal. The reason for using hexadecimals is that it allows us to represent a large range of values with a smaller number of digits, making it easier to read and write.

### Rainbow Colours

|                   | Red   | Orange  | Yellow | Green  | Blue  | Indigo  | Violet |
|-------------------|-------|---------|--------|--------|-------|---------|--------|
| Header 1          | #FF0000 | #FF7F00 | #FFFF00 | #00FF00 | #0000FF | #4B0082 | #9400D3 |
| Data Row 1        | #FF6347 | #FFA500 | #FFFF45 | #90EE90 | #ADD8E6 | #5F9EA0 | #AB82BF |
| Data Row 2        | #FF4500 | #FFD700 | #ADFF2F | #F0FFF0 | #E6E6FA | #708090 | #BC8F8F |

## Char (character) and String
Python doesn't have a built-in `char` type, but you can use a string of length 1 to represent a character. A string is a sequence of characters, so you can also use strings to represent multiple characters. Originally, Python used ASCII encoding for its `char` type, but now it uses Unicode encoding. Unicode encoding allows Python to represent a wide range of characters from different languages. Unicode is backward compatible with ASCII, so you can still use ASCII characters in your strings. 

- The decimal value for `a` is 97, which corresponds to the ASCII code for lowercase 'a'.
- The decimal value for `A` is 65, which corresponds to the ASCII code for uppercase 'A'.
- You can convert a character to its corresponding ASCII value using the `ord()` function.  
- You can convert an ASCII value back to a character using the `chr()` function. For example:

## Boolean
Boolean values are represented as either `True` or `False`. In Python, you can use the `bool()` function to convert other data types to boolean values. 

## Real
Real numbers are represented as floating-point numbers in Python. You can use the `float()` function to convert other data types to real numbers. 

## Single Precision Float
Single precision float is a type that uses 32 bits to represent a floating-point number in some computer languages like C or Java. You can also have double precision float which uses 64 bits to represent a floating-point number as it is double the size of a single precision float. 

Python does not differentiate between single and double precision floats, as it uses the `float()` type for both.

## Integer
Integers are represented as whole numbers in Python. You can use the `int()` function to convert other data types to integers.

## Date and Time
Date and time representation in most languages is done using built-in libraries or modules. For example, in Python, you can use the `datetime` module to work with dates and times. The most common way to represent a date and time is using an epoch timestamp, which represents the number of seconds since January 1, 1970, at midnight UTC. 

!!! Note
    - Date and time representation in different languages may vary depending on the library or module used.
    - It is also important to note that date and time representation can be affected by time zones.
    - They can be one of the most common bug in software development, so it's essential to handle them correctly.
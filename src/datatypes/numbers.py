# Example starter code
def binary_to_decimal_visual(binary_num):
    """Convert a binary number to decimal and show the calculation steps"""
    # Your code here - show each power of 2 and how it contributes to the final sum
    # Example output for "10101011":
    # 1 * 2^7 = 128
    # 0 * 2^6 = 0
    # 1 * 2^5 = 32
    # ...and so on
    # then sum up all the values to get the final decimal number
    pass

def decimal_to_binary_visual(decimal_num):
    """Convert a decimal number to binary and show the division steps"""
    # Your code here - show each division by 2 and the remainder
    # Example output for 171:
    # 171 ÷ 2 = 85 remainder 1
    # 85 ÷ 2 = 42 remainder 1
    # ...and so on
    # then reverse the remainders to display the binary number

    pass

if __name__ == "__main__":

    # Test with the example number
    binary_example = "10101011"
    print(f"Converting {binary_example} to decimal:")
    result_decimal = binary_to_decimal_visual(binary_example)
    print(f"Final result: {result_decimal}")

    decimal_example = 171
    print(f"\nConverting {decimal_example} to binary:")
    result_binary = decimal_to_binary_visual(decimal_example)
    print(f"Final result: {result_binary}")
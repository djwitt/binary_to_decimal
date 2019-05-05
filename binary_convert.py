def binary_to_dec(bin_nums):
    """the native function `bin()` will achieve the exact same result"""

    base_two = 2
    bin_len = len(bin_nums)
    bin_list = (int(digit) for digit in str(bin_nums))

    # Generate reversed exponent list based off the length of binary input
    exponents = list(reversed(range(bin_len)))

    decimal_output = (
        digit * base_two ** expo for digit, expo in zip(bin_list, exponents)
    )

    return sum(decimal_output)
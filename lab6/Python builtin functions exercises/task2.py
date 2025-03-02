def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    print("Upper case letters:", upper_count)
    print("Lower case letters:", lower_count)


count_case("Hello World!")

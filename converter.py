def converter(ops, value):
    if ops == "km":
        print(f"{value * 1000} м")
    elif ops == "m":
        print(f"{value / 1000} км")
    else:
        print("Enter only 'km' or 'm'.")
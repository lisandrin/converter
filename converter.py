def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

print("Converter:")
print("1. KM to M")
print("2. M to KM")

choice = input("Choose which one (1 or 2): ")

if choice == "1":
    km = float(input("The result in KM: "))
    print(f"{km} км = {km_to_m(km)} м")
elif choice == "2":
    m = float(input("The result in M: "))
    print(f"{m} м = {m_to_km(m)} км")
else:
    print("Error. try again")

print("Hello\n")
import math

q = int(input("Enter Prime number, q: "))
print("Primitive root of q are: ")

coprime_set = []
for i in range(1, q):
    if math.gcd(i, q) == 1:
        coprime_set.append(i)
coprime_set = set(coprime_set)  # conerted into set because we have to compare coprime set and test set
for i in range(1, q):
    test_set = []
    for j in range(1, q):
        test_set.append(pow(i, j, q))
    test_set = set(test_set)
    if test_set == coprime_set:
        print(i, end=" ")
print()
alpha = int(input("Select a Primitive root of q: "))

xa = int(input("select User A Privet Key: "))
assert xa < q, "Error"
xb = int(input("select User B Privet Key: "))
assert xb < q, "Error"

public_key_of_user_a = pow(alpha, xa) % q
public_key_of_user_b = pow(alpha, xb) % q

secret_key_of_user_a = pow(public_key_of_user_b, xa) % q
secret_key_of_user_b = pow(public_key_of_user_a, xb) % q

print("USER A Secret key = ", secret_key_of_user_a)
print("USER B Secret key = ", secret_key_of_user_b)

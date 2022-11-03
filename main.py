n1_str = input("Digite o primeiro número:\n")
n2_str = input("Digite o segundo número:\n")
n3_str = input("Digite o terceiro número:\n")

n1 = int(n1_str)
n2 = int(n2_str)
n3 = int(n3_str)

if (n1 > n2 and n1 > n3):
    print("O maior valor digitado é {}".format(n1))
elif (n2 > n1 and n2 > n3):
    print("O maior valor digitado é {}".format(n2))
elif (n3 > n1 and n3 > n2):
    print("O maior valor digitaddo é {}".format(n3))

if (n1 < n2 and n1 < n3):
        print("O menor valor digitado é {}".format(n1))
elif (n2 < n1 and n2 < n3):
        print("O menor valor digitado é {}".format(n2))
elif (n3 < n1 and n3 < n2):
        print("O menor valor digitaddo é {}".format(n3))


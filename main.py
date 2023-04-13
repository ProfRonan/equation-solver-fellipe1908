print("Digite o grau para essa variável: ")
nmr = int(input(">>"))

if nmr < 1 or nmr > 2:
    print("Grau inválido")

elif nmr == 1:
    print("A equação é do primeiro grau")
    print("Digite o primeiro valor: ")
    a = int(input(">>"))
    if a == 0:
        print("Valor de a inválido")
    elif nmr > 0:
        print("Digite o segundo número")
        b = int(input(">> "))
        print(f"{-b/a:.2f}")

elif nmr == 2:
    print("A equação é do segundo grau")
    print("Digite o primeiro número: ")
    a = int(input(">"))
    
    if a == 0:
        print("Valor de a inválido")
    else:
        print("Digite o Segundo número")
        b = int(input(">> "))
        print("Digite o Terceiro número")
        c = int(input(">> "))
        r = int(b * b)
        r2 = int(a*c*4)
        if r < (a*c*(4)):
            print("A equação não possui raízes reais")
        elif r == r2 :
            print("A equação possui apenas uma raiz real")
            print(f"{(-b + 0)/(2*a):.2f}")
        else :
            r2 = int(b**2-4*a*c)
            print("A equação possui duas raízes reais")
            print(f"{(-b - r2**0.5)/(2*a):.2f}")
            print(f"{(-b + r2**0.5)/(2*a):.2f}")
      
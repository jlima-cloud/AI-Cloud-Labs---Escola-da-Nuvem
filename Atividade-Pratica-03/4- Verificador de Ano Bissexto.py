"""Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400."""

#ano = int(input("Digite um ano: "))
#if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):   
#    print(f"O ano {ano} é bissexto.")
#else:

#    print(f"O ano {ano} não é bissexto.")
#print("\nFim do Programa!")

ano = int(input("Digite o ano que deseja verificar: "))


if ano % 400 == 0:
    bissexto = True
elif ano % 100 == 0:
    bissexto = False
elif ano % 4 == 0:
    bissexto = True
else:
    bissexto = False


if bissexto:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"\nO ano {ano} não é bissexto.") 



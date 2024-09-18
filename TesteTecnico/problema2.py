def verificar_letra_a(string):
    contador_a = string.lower().count('a')
    
    if contador_a > 0:
        print(f"A letra 'a' aparece {contador_a} vez(es) na string informada.")
    else:
        print("A letra 'a' não aparece na string informada.")

# Adicionar a string manualmente
string_informada = "Arthur Antunes Santos Silva"
#string_informada = "Teste sem "
verificar_letra_a(string_informada)

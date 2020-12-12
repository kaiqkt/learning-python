"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funcoes built-in len, abs, type, print, etc
Essas funcoes podem ser usadas diretamente em cada tipo.
"""
# pos+ [012345678]
text = 'Python s2'
# neg- [987654321]

print(text[1])
print(text[-9])


nova_string = text[0:6]
nova_string_2 = text[0:8:2]

print(nova_string)
print(nova_string_2)

for let in text:
    print(let)
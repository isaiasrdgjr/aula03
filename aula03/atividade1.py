# desconto 13%
desconto = 13/100
vlcamiseta = float(input('Informe o valor da camiseta '))

vldesconto = vlcamiseta * desconto
vlfinal = vlcamiseta - vldesconto


print('O valor da camiseta com desconto é: R$' + str(vlfinal))
print('Parabéns você ganhou R$' + str(vldesconto), 'de desconto na sua compra')

import string

lpp = []
lpp = ["Lojas Tabajara"]
#saida = open("aula_6_ex1_saida.txt", "w")

produto = 1
total = 0
preco = 1

while (preco != 0):
    preco = 0
    preco = float(input("Digite um número: "))
    produto_preco = "Produto " + str(produto) + ": R$ " + "%0.2f" % preco
    lpp.append(produto_preco)
    produto = produto + 1
    total = total + preco
else:
    dinheiro = float(input("Digite o valor recebido: "))
    dinheiro_format = "Dinheiro: R$ " + "%0.2f" % dinheiro
    lpp.append(dinheiro_format)
    troco = "Troco: R$ " + "%0.2f" %(dinheiro - total)
    lpp.append(troco)
    lpp = '\n'.join(lpp)
    #saida.write('%s'%(lpp))
    print (lpp)
    
#saida.close()

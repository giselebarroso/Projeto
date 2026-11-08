#das 0h às 9h — 50% de desconto no valor do minuto.
#das 9h01 às 18h — 0% de desconto no valor do minuto.
#das 18h01 às 21h — 30% de desconto no valor do minuto.
#das 21h01 às 23h59 — 40% de desconto no valor do minuto.

#das 0m às 540m — 50% de desconto no valor do minuto.
#das 541m às 1080m — 0% de desconto no valor do minuto.
#das 1081 às 1260m — 30% de desconto no valor do minuto.
#das 1261 às 1440m — 40% de desconto no valor do minuto.

def valida_input():
    if (len(hora_incio)  == 5) and (len(hora_fim) == 5):
        return "valido"
    else:
        print(f"Formato de horário incorreto. Tente novamente")


resposta = "s"

while resposta.lower() == "s":

    hora_incio = input("Digite a hora inicial (AA:MM): ")

    hora_fim = (input("Digite a hora final (AA:MM): "))
    #minuto_fim = int(input("Digite os minutos da hora final (:Y(minutos)m)"))

    valida_input()

    while valida_input() == "valido":

        inicio = hora_incio.split(':')
        hora1 = int(inicio[0] * 60)
        min1 = int(inicio[1])
        soma1 = hora1 + min1

        fim = hora_fim.split(':')
        hora2 = int(fim[0] * 60)
        min2 = int(fim[1])
        soma2 = hora2 + min2
        #inicio = ( hora_incio * 60 ) + minuto_incio
        #fim = ( hora_fim * 60 ) + minuto_fim

        valor_minuto = 2.0

    #delta = fim - inicio
    #valor_ligacao = delta * valor_minuto

    #print('inicio', inicio)
    #print('fim', fim)
    
    #print('delta', delta)
    #print('valor_ligacao', valor_ligacao)

    #hora_incio = 1
    #minuto_incio = 1

    #hora_fim = 3
    #minuto_fim = 21

    #das 0m às 540m — 50% de desconto no valor do minuto.
    #das 541m às 1080m — 0% de desconto no valor do minuto.
    #das 1081 às 1260m — 30% de desconto no valor do minuto.
    #das 1261 às 1440m — 40% de desconto no valor do minuto.

        if fim < 540:

            delta = soma2 - soma1
            valor_normal = delta * ( valor_minuto)

            
            valor_ligacao = delta * ( valor_minuto * 0.50)

            print('inicio', inicio)
            print('inicio', fim)

            print('delta', delta)
            print('valor_normal', valor_normal)
            print('valor_ligacao', valor_ligacao)

        elif fim < 1080:

            if inicio > 540:
                delta = soma2 - soma1
                valor_normal = delta * ( valor_minuto)

                
                valor_ligacao = delta * ( valor_minuto * 1.00 )

                print('inicio', inicio)
                print('inicio', fim)
    
                print('delta', delta)
                print('valor_normal', valor_normal)
                print('valor_ligacao', valor_ligacao)

            else:
    
                valor_ligacao = ( ( 540 - inicio ) * ( valor_minuto * 0.50 ) )
                valor_ligacao += ( ( fim - 540 ) * ( valor_minuto * 1.00 ) )

        elif fim < 1260:

            if inicio > 1080:
    
                delta = soma2 - soma1
                valor_normal = delta * ( valor_minuto)

                
                valor_ligacao = delta * ( valor_minuto * 0.30 )

                print('inicio', inicio)
                print('inicio', fim)
                print('valor_normal', valor_normal)
                print('delta', delta)
                print('valor_ligacao', valor_ligacao)


            else:

                delta = soma2 - soma1
                valor_normal = delta * ( valor_minuto)

                
                valor_ligacao = delta * ( valor_minuto * 0.40 )

                print('inicio', inicio)
                print('inicio', fim)
                print('valor_normal', valor_normal)
                print('delta', delta)
                print('valor_ligacao', valor_ligacao)

    resposta = input("deseja tentar novamente? (s ou n)? ")
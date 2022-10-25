
var = True
try:
    while var:
        print("A seguir, você informá um número DDD e será dito sua cidade")

        d = int(input("Digite um DDD e será informado sua respectiva cidade:"))
        if d == 61:
            print("Para DDD", d, "tem-se a cidade de Brasília")
        elif d == 71:
            print("Para DDD", d, "tem-se a cidade de Salvador")
        elif d == 11:
            print("Para DDD", d, "tem-se a cidade de São Paulo")
        elif d == 21:
            print("Para DDD", d, "tem-se a cidade de Rio de Janeiro")
        elif d == 32:
            print("Para DDD", d, "tem-se a cidade de Juiz de Fora")
        elif d == 19:
            print("Para DDD", d, "tem-se a cidade de Campinas")
        elif d == 27:
            print("Para DDD", d, "tem-se a cidade de Vitória")
        elif d == 31:
            print("Para DDD", d, "tem-se a cidade de Belo Horizonte")
        else:
            print("O DDD informado não consta no nosso banco de dados, tente outro")


        a = str(
            input("QUer verificar outro DDD ou quer encerrar consulta (Digite S para continuar ou F para encerrar :"))
        if a == "s" or "S":
            var = True
        elif a == "f" or "F":
            break
            print("Consulta encerrada. Obrigado!")


except:
        print("Valor informado é invalido, favor informar apenas números")


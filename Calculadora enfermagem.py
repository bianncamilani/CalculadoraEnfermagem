def ler_float(texto):
    valor = input(texto).replace(",", ".")
    return float(valor)


def arredondar(valor):
    decimal = valor - int(valor)

    if decimal > 0.5:
        return int(valor) + 1
    else:
        return int(valor)


def regra_de_tres(a, b, c):
    return (b * c) / a


def rediluicao(c1, c2, v2):
    v1 = (c2 * v2) / c1
    diluente = v2 - v1
    return v1, diluente


def calculo_insulina(seringa, prescricao, frasco):
    return (seringa * prescricao) / frasco


def penicilina(ui_frasco, volume_total, ui_prescrita):
    return (volume_total * ui_prescrita) / ui_frasco


def infusao_horas_macrogotas(volume_total, tempo_horas):
    return (volume_total / tempo_horas) * 3


def infusao_horas_microgotas(volume_total, tempo_horas):
    return volume_total / tempo_horas


def infusao_minutos_macrogotas(volume_total, tempo_minutos):
    return (volume_total * 20) / tempo_minutos


def infusao_minutos_microgotas(volume_total, tempo_minutos):
    return (volume_total * 60) / tempo_minutos


def converter_massa():
    print("\n=== CONVERSOR DE MASSA ===")
    print("1 - Tonelada para kg")
    print("2 - Kg para gramas")
    print("3 - Gramas para mg")
    print("4 - Mg para microgramas")

    opcao = input("Escolha uma opção: ")
    valor = ler_float("Digite o valor: ")

    if opcao == "1":
        print(f"Resultado: {valor * 1000} kg")
    elif opcao == "2":
        print(f"Resultado: {valor * 1000} g")
    elif opcao == "3":
        print(f"Resultado: {valor * 1000} mg")
    elif opcao == "4":
        print(f"Resultado: {valor * 1000} microgramas")
    else:
        print("Opção inválida.")


def converter_volume():
    print("\n=== CONVERSOR DE VOLUME ===")
    print("1 - Litro para mL")
    print("2 - mL para gotas")
    print("3 - Gotas para mcg")
    print("4 - mL para UI")
    print("5 - UI para mL")

    opcao = input("Escolha uma opção: ")
    valor = ler_float("Digite o valor: ")

    if opcao == "1":
        print(f"Resultado: {valor * 1000} mL")
    elif opcao == "2":
        print(f"Resultado: {valor * 20} gotas")
    elif opcao == "3":
        print(f"Resultado: {valor * 3} mcg")
    elif opcao == "4":
        print(f"Resultado: {valor * 100} UI")
    elif opcao == "5":
        print(f"Resultado: {valor / 100} mL")
    else:
        print("Opção inválida.")


def converter_tempo():
    print("\n=== CONVERSOR DE TEMPO ===")
    print("1 - Horas para minutos")
    print("2 - Minutos para segundos")
    print("3 - Minutos para horas")
    print("4 - Segundos para minutos")

    opcao = input("Escolha uma opção: ")
    valor = ler_float("Digite o valor: ")

    if opcao == "1":
        print(f"Resultado: {valor * 60} minutos")
    elif opcao == "2":
        print(f"Resultado: {valor * 60} segundos")
    elif opcao == "3":
        print(f"Resultado: {valor / 60} horas")
    elif opcao == "4":
        print(f"Resultado: {valor / 60} minutos")
    else:
        print("Opção inválida.")


def conversor_unidades():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1 - Massa")
    print("2 - Volume")
    print("3 - Tempo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        converter_massa()
    elif opcao == "2":
        converter_volume()
    elif opcao == "3":
        converter_tempo()
    else:
        print("Opção inválida.")


def mostrar_menu():
    print("+-------------------------------------------+")
    print("|        CALCULADORA DA ENFERMAGEM          |")
    print("+-------------------------------------------+")
    print("| 1 - Regra de três                         |")
    print("| 2 - Rediluição                            |")
    print("| 3 - Cálculo de insulina                   |")
    print("| 4 - Cálculo de penicilina                 |")
    print("| 5 - Infusão em horas                      |")
    print("| 6 - Infusão em minutos                    |")
    print("| 7 - Conversor de unidades                 |")
    print("| 0 - Sair                                  |")
    print("+-------------------------------------------+")


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            print("\n=== REGRA DE TRÊS ===")
            a = ler_float("Digite o valor de A: ")
            b = ler_float("Digite o valor de B: ")
            c = ler_float("Digite o valor de C: ")

            resultado = regra_de_tres(a, b, c)
            print(f"Resultado: {resultado:.2f}")

        elif opcao == "2":
            print("\n=== REDILUIÇÃO ===")
            c1 = ler_float("Concentração inicial C1: ")
            c2 = ler_float("Concentração final desejada C2: ")
            v2 = ler_float("Volume final desejado V2 em mL: ")

            v1, diluente = rediluicao(c1, c2, v2)
            print(f"Usar {v1:.2f} mL da solução inicial")
            print(f"Adicionar {diluente:.2f} mL de diluente")

        elif opcao == "3":
            print("\n=== CÁLCULO DE INSULINA ===")
            seringa = ler_float("Capacidade da seringa em UI: ")
            prescricao = ler_float("Prescrição em UI: ")
            frasco = ler_float("Quantidade do frasco em UI: ")

            resultado = calculo_insulina(seringa, prescricao, frasco)
            print(f"Você deve aspirar {resultado:.2f} na seringa")

        elif opcao == "4":
            print("\n=== CÁLCULO DE PENICILINA ===")
            print("Exemplo: frasco de 5.000.000 UI em 10 mL")
            ui_frasco = ler_float("Quantidade de UI do frasco: ")
            volume_total = ler_float("Volume total após diluição em mL: ")
            ui_prescrita = ler_float("Quantidade de UI prescrita: ")

            resultado = penicilina(ui_frasco, volume_total, ui_prescrita)
            print(f"Você deve aspirar {resultado:.2f} mL")

        elif opcao == "5":
            print("\n=== INFUSÃO EM HORAS ===")
            volume_total = ler_float("Volume total em mL: ")
            tempo_horas = ler_float("Tempo em horas: ")

            print("1 - Macrogotas")
            print("2 - Microgotas")
            tipo = input("Escolha o tipo: ")

            if tipo == "1":
                resultado = infusao_horas_macrogotas(volume_total, tempo_horas)
                print(f"Resultado: {arredondar(resultado)} gotas por minuto")
            elif tipo == "2":
                resultado = infusao_horas_microgotas(volume_total, tempo_horas)
                print(f"Resultado: {arredondar(resultado)} microgotas por minuto")
            else:
                print("Opção inválida.")

        elif opcao == "6":
            print("\n=== INFUSÃO EM MINUTOS ===")
            volume_total = ler_float("Volume total em mL: ")
            tempo_minutos = ler_float("Tempo em minutos: ")

            print("1 - Macrogotas")
            print("2 - Microgotas")
            tipo = input("Escolha o tipo: ")

            if tipo == "1":
                resultado = infusao_minutos_macrogotas(volume_total, tempo_minutos)
                print(f"Resultado: {arredondar(resultado)} gotas por minuto")
            elif tipo == "2":
                resultado = infusao_minutos_microgotas(volume_total, tempo_minutos)
                print(f"Resultado: {arredondar(resultado)} microgotas por minuto")
            else:
                print("Opção inválida.")

        elif opcao == "7":
            conversor_unidades()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")

    except ValueError:
        print("Erro: digite apenas números válidos.")
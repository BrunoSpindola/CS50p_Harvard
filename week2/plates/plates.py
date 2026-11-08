def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def valid_size(s):
    # Regra 1: a placa deve ter entre 2 e 6 caracteres.
    # Como a expressão "2 <= len(s) <= 6" já é True/False,
    # não precisamos de if/else: só devolvemos o resultado direto.
    return 2 <= len(s) <= 6


def start_with_letters(s):
    # Regra 2: os 2 primeiros caracteres da placa devem ser letras.
    two_letters = s[0:2]

    # len(two_letters) == 2 garante que a placa realmente TEM 2 caracteres
    # no início (evita o bug de placas com só 1 caractere, tipo s = "A",
    # onde s[0:2] viraria só "A" e .isalpha() daria True por engano).
    return len(two_letters) == 2 and two_letters.isalpha()


def no_letters_after_number(s):
    # Regra 3: números só podem aparecer no final (não pode ter
    # uma letra vindo DEPOIS de um número já ter aparecido).
    found_number = False        # vira True assim que vemos o 1º dígito
    letter_after_number = False # vira True se acharmos letra após número

    for i in s:
        if i.isdigit():
            # achamos um dígito -> a partir daqui, "found_number" fica
            # True para sempre (não existe linha que volte pra False)
            found_number = True
        elif i.isalpha():
            # é uma letra: só é um problema se já tivermos visto
            # um número ANTES dela
            if found_number:
                letter_after_number = True

    # A variável guarda quando algo deu ERRADO (True = tem problema).
    # Mas a função deve responder se a regra foi RESPEITADA,
    # por isso invertemos com "not".
    # Caso a placa não tenha número nenhum (ex: "NRVOUS"), found_number
    # nunca vira True, logo letter_after_number nunca vira True,
    # e a função retorna True (regra respeitada por "verdade vacuosa").
    return not letter_after_number


def firs_number_not_zero(s):
    # Regra 4: se existir número na placa, o PRIMEIRO dígito
    # que aparece não pode ser '0'.
    found_number = False    # ainda não processamos nenhum dígito
    number_is_zero = False  # vira True só se o 1º dígito for '0'

    for i in s:
        if i.isdigit():
            if not found_number:
                # Este é o PRIMEIRO dígito da string (found_number
                # ainda é False) -> é aqui que decidimos o veredito.
                if i == '0':
                    number_is_zero = True
                found_number = True  # "gasta" a condição de 1º dígito
                break  # já decidimos tudo que precisávamos, não
                       # precisa continuar olhando o resto da string

    # Se não houver número nenhum na placa, o loop nunca entra no
    # "if i.isdigit()", number_is_zero fica False, e a função
    # retorna True (regra respeitada, verdade vacuosa de novo).
    return not number_is_zero


def only_letters_numbers(s):
    # Regra 5: só pode ter letras e números — nada de espaço,
    # ponto ou qualquer símbolo de pontuação.
    return s.isalnum()


def is_valid(s):
    # A placa só é válida se TODAS as 5 regras forem verdadeiras ao
    # mesmo tempo (por isso usamos "and" entre todas as funções).
    return (
        valid_size(s)
        and start_with_letters(s)
        and no_letters_after_number(s)
        and firs_number_not_zero(s)
        and only_letters_numbers(s)
    )


main()

def lasso_letter(letter, shifter_amo):
    # translate ASCII - traduzindo para ASCII
    letter_code = ord(letter.lower())
    # CALCULANDO CRIPT
    #### decoded_letter_code = letter_code + shifter_amo ---
    a_ascii = ord("a")
    alphabet_size = 26

    # Calculando cripto -- verdadeira letra / real letter based on script - explicaçao abaixo ou readme - to answers
    true_letter_code = a_ascii + (
        ((letter_code - a_ascii) + shifter_amo) % alphabet_size
    )

    # TRADUZINDO DE ASCII - TRANSLATE FROM ASCII
    decoded_letter = chr(true_letter_code)

    return decoded_letter


# DECODE WORDS // Decodando palavras
def lasso_word(word, shift_amo):
    decoded_word = ""

    for letter in word:
        decoded_letter = lasso_letter(letter, shift_amo)
        # printar a variavel que a letras da palavra está sendo/ foi atribuida ----- bug resolvido
        # print(decoded_letter)
        decoded_word = decoded_word + decoded_letter

    return decoded_word


# ASCII CARACTER - function py
# ord("a")
# print(ord("a"))
# TRANSLATE FROM ASCII TO CARACTER - TRADUZINDO DE ASCII PARA CARACTERE - funçao py
# chr(decode_letter_code)

# print(lasso_letter("a", 2))

# SE FOR PRINTAR A FUNÇÃO USAR O RETURN ---- SE EU PRECISAR DA IMPRESSÃO AUTOMATICA USAR O PRINT NA DEFINIÇAO DELA
# print(lasso_word("terra", 13))


char = input("Escreva o a palavra para ser decryptada:")
nun = int(input("\n Escreva o numero: "))

print(lasso_word(char, nun))


# FINISH - FIM

def validar_abertura_conta(idade, score_credito):
    if idade < 18:
        raise ValueError("Idade inválida.")

    if score_credito < 500:
        return "Score Insuficiente."

    return "Conta aprovada."

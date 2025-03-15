def romanToInt(s: str) -> int:
    # Dicionário com os valores dos caracteres romanos
    valores = {
        "I": 1, 
        "V": 5, 
        "X": 10, 
        "L": 50, 
        "C": 100, 
        "D": 500, 
        "M": 1000
    }
    
    total = 0
    
    # Percorre a string com índices
    for i in range(len(s)):
        # Se não é o último caractere e o atual é menor que o próximo
        # (casos como IV, IX, XL, CM etc.)
        if i < len(s) - 1 and valores[s[i]] < valores[s[i+1]]:
            # Subtrai o valor atual (regra da notação romana)
            total -= valores[s[i]]
        else:
            # Adiciona o valor atual
            total += valores[s[i]]
    
    return total

# Testes para verificar se a função funciona corretamente
testes = [
    ("III", 3),         # 1+1+1
    ("IV", 4),          # -1+5
    ("IX", 9),          # -1+10
    ("LVIII", 58),      # 50+5+1+1+1
    ("MCMXCIV", 1994),  # 1000-100+1000-10+100-1+5
]

for entrada, esperado in testes:
    resultado = romanToInt(entrada)
    print(f"{entrada} = {resultado} (esperado: {esperado})")
    assert resultado == esperado, f"Erro: {entrada} deveria ser {esperado}, obtido {resultado}"

print("Todos os testes passaram!") 
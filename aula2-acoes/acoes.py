# pip install yfinance pyautogui matplotlib

import yfinance

ticker = input("Digite o código da ação desejada: ") # PETR4.SA
start = input("Data de inicio do período: ") # 2024-06-01
end = input("Data do fim do período: ") # 2024-06-10

dados = yfinance.Ticker(ticker).history(start=start, end=end)

fechamento = dados.Close

maximo = round(fechamento.max(), 2)
minimo = round(fechamento.min(), 2)
medio = round(fechamento.mean(), 2)

print(maximo)
print(minimo)
print(medio)


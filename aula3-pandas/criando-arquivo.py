# pip install faker

from faker import Faker
import pandas as pd

fake_data = Faker(locale="pt_BR")

nome = []
empresa = []
cidade = []
funcao = []

for i in range(0,10):
    nome.append(fake_data.name())
    empresa.append(fake_data.company())
    cidade.append(fake_data.city())
    funcao.append(fake_data.job())

df = pd.DataFrame(
    {
        'nome': nome,
        'empresa': empresa,
        'cidade': cidade,
        'funcao': funcao
    }
)

df.to_excel("fakerdata.xlsx")

print("Arquivo criado com sucesso !!!")
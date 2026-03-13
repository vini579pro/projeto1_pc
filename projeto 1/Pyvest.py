import math
import random
import datetime
import statistics
import locale 

locale.setlocale(locale.LC_ALL, "pt_br.UTF-8")
#entradas
capital= float(input("capital_inicial: "))
aporte= float(INPUT("aporte mensal: "))
meses= int(input("prazo(meses): "))
cdi_anual= float(input("cdi anual (%)"))/100
perc_cdb= float(input("percentual do cdi (%)"))/100
perc_lci= float(input("percentual do cdb (%)"))/100
taxa_FII= float(input("rentabilidade mensal fil (%)"))/100
meta= float(input("meta finaceira (R$)"))

#conversão CDI
cdi_mensal= math.pow((1 + cdi_anual), 1/12) -1

#total investido
total_investido= capital + (aporte * meses)

#CDB
taxa_cdb= cdi_mensal * perc_cdb
montante_cdb= (capital * math.pow((1 + taxa_cdb), meses) + (aporte * meses))
lucro_cdb= montante_cdb - total_investido
montante_cdb_liquido= total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci= cdi_mensal * perc_lci
montante_lci= (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses))

#poupança
taxa_poupanca= 0.005
montante_poupanca= (capital * math.pow((1 + taxa_poupanca), meses) + (aporte * meses))

#fil - simulações 

montante = (capital * math.pow((1 + taxa_FII), meses) + (aporte * meses))

variacao = random.uniform(-0.03, 0.03)
valor_final = montante * (1 + variacao)

# simulações FII
variacao_1 = random.uniform(-0.03, 0.03)
variacao_2 = random.uniform(-0.03, 0.03)
variacao_3 = random.uniform(-0.03, 0.03)
variacao_4 = random.uniform(-0.03, 0.03)
variacao_5 = random.uniform(-0.03, 0.03)

FII1 = (capital * math.pow((1 + taxa_FII), meses) + (aporte * meses)) * (1 + variacao_1)
FII2 = (capital * math.pow((1 + taxa_FII), meses) + (aporte * meses)) * (1 + variacao_2)
FII3 = (capital * math.pow((1 + taxa_FII), meses) + (aporte * meses)) * (1 + variacao_3)
FII4 = (capital * math.pow((1 + taxa_FII), meses) + (aporte * meses)) * (1 + variacao_4)
FII5 = (capital * math.pow((1 + taxa_FII), meses) + (aporte * meses)) * (1 + variacao_5)

taxa_FII_lista = [FII1, FII2, FII3, FII4, FII5]

# estatísticas
media_FII = statistics.mean(taxa_FII_lista)
mediana_FII = statistics.median(taxa_FII_lista)
desvio_FII = statistics.stdev(taxa_FII_lista)

# datas
data_simulacao = datetime.datetime.now()
dias = meses * 30
data_resgate = data_simulacao + datetime.timedelta(days=dias)

# meta
meta_atingida = media_FII >= meta

# formatação moeda
total_format = locale.currency(total_investido, grouping=True)
cdb_format = locale.currency(montante_cdb_liquido, grouping=True)
lci_format = locale.currency(montante_lci, grouping=True)
poup_format = locale.currency(montante_poupanca, grouping=True)

media_format = locale.currency(media_FII, grouping=True)
mediana_format = locale.currency(mediana_FII, grouping=True)
desvio_format = locale.currency(desvio_FII, grouping=True)

# gráfico ASCII
graf_cdb = "█" * int(montante_cdb_liquido / 1000)
graf_lci = "█" * int(montante_lci / 1000)
graf_poup = "█" * int(montante_poupanca / 1000)
graf_FII = "█" * int(media_FII / 1000)

# relatório
print("Relatório de investimento")

print("Data de simulação:", data_simulacao.strftime("%d/%m/%y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%y"))

print("Total investido:", total_format)

print("\nResultados")
print("CDB:", cdb_format)
print("LCI:", lci_format)
print("Poupança:", poup_format)
print("FII (média):", media_format)

print("\nEstatísticas FII")
print("Média:", media_format)
print("Mediana:", mediana_format)
print("Desvio padrão:", desvio_format)

print("\nMeta financeira atingida:", meta_atingida)

print("\nGráfico comparativo")
print("CDB:", graf_cdb)
print("LCI:", graf_lci)
print("Poupança:", graf_poup)
print("FII:", graf_FII)

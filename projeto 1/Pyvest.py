import math
import random
import datetime
import statistics
import locale 

locale.setlocale(locale.LC_ALL, "pt_br.UTF-8")
#entradas
capital= float(input("capital_inicial: "))
aporte= float("aporte mensal: ")
meses= int(input("prazo(meses): "))
cdi_anual= float(input("cdi anual (%)"))/100
perc_cdb= float(input("percentual do cdi (%)"))/100
perc_lci= float(input("percentual do cdb (%)"))/100
taxa_fil= float(input("rentabilidade mensal fil (%)"))/100
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
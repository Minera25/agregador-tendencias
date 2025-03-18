from pytrends.request import TrendReq
import pandas as pd

# Conectar ao Google Trends
pytrends = TrendReq(hl='pt-BR', tz=0)

# Buscar tendências do dia no Brasil
tendencias_diarias = pytrends.trending_searches(pn="brazil")

# Exibir os tópicos mais pesquisados
print("🔎 Tendências de pesquisa no Brasil (Últimas 24h):")
print(tendencias_diarias)

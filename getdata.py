import requests
from bs4 import BeautifulSoup
import json


mystocks = ['itsa4' , 'bbas3' , 'elet3' , 'jbss3' , 'ggbr4']
mystocks = ['bbas3']
myetfs = ['xina11']
myfiis = ['galg11' , 'hgpo11' , 'jsre11' , 'xplg11' , 'pvbi11']
myfiinfras = ['juro11']

stockdata = []
etfsdata = []
fiisdata = []
fiinfrasdata = []


def getData(tipo , simbolo):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    url = f'https://statusinvest.com.br/{tipo}/{simbolo}'
    r = requests.get(url , headers = headers)
    soup = BeautifulSoup(r.text , 'html.parser')


    papel = simbolo
    preco = soup.find(string='Valor atual').find_next('strong').text
    min = soup.find(string='Min. 52 semanas').find_next('strong').text
    max = soup.find(string='Máx. 52 semanas').find_next('strong').text

    if soup.find(string='Últimos 12 meses'):
        dy = soup.find(string='Últimos 12 meses').find_previous('strong').text + '%'
    else:
        pass
    
    if soup.find(string='P/VP'):
        pvp = soup.find(string='P/VP').find_next('strong').text
    else:
        pass

    if soup.find(string='P/EBITDA'):
        pebitda = soup.find(string='P/EBITDA').find_next('strong').text
    else:
        pass

    if soup.find(string='P/EBIT'):
        pebit = soup.find(string='P/EBIT').find_next('strong').text
    else:
        pass

    if soup.find(string='VPA'):
        vpa = soup.find(string='VPA').find_next('strong').text
    else:
        pass

    if soup.find(string='P/Ativo'):
        pativo = soup.find(string='P/Ativo').find_next('strong').text
    else:
        pass

    if soup.find(string='Patrimônio'):
        valorpatrimonial = soup.find(string='Patrimônio').find_previous('strong').text
    else:
        pass

    if soup.find(string='Segmento ANBIMA'):
        segmento = soup.find(string='Segmento ANBIMA').find_next('strong').text
    else:
        pass


    if tipo == 'acoes':
        papel = {
            'papel': papel,
            'preco': preco,
            'min': min,
            'max': max,
            'dy': dy,
            'p/vp': pvp,
            'p/ebitda': pebitda,
            'p/ebit': pebit,
            'vpa': vpa,
            'p/ativo': pativo,
        }
    elif tipo == 'etfs':
        papel = {
            'papel': papel,
            'preco': preco,
            'min': min,
            'max': max,   
        }
    elif tipo == 'fundos-imobiliarios':
        papel = {
            'papel': papel,
            'preco': preco,
            'min': min,
            'max': max,
            'dy': dy,
            'valor patrimonial': valorpatrimonial,
            'p/vp': pvp,
            'segmento': segmento,
        }
    elif tipo == 'fiinfras':
        papel = {
            'papel': papel,
            'preco': preco,
            'min': min,
            'max': max,
            'dy': dy,
        }
    else:
        pass


    return papel


for item in mystocks:
    stockdata.append(getData('acoes' , item))

for item in myetfs:
    etfsdata.append(getData('etfs' , item))

for item in myfiis:
    fiisdata.append(getData('fundos-imobiliarios' , item))

for item in myfiinfras:
    fiinfrasdata.append(getData('fiinfras' , item))



print(f'Stocks: {stockdata}')
print(f'ETFS: {etfsdata}')
print(f'FIIS: {fiisdata}')
print(f'Fiinfras: {fiinfrasdata}')


#with open('D:/OneDrive/Documentos/PROGRAMAÇÃO/VSCODE/CARTEIRA INVEST/Data/stockdata.json' , 'w') as f:
#    json.dump(stockdata , f)

#with open('D:/OneDrive/Documentos/PROGRAMAÇÃO/VSCODE/CARTEIRA INVEST/Data/etfsdata.json' , 'w') as f:
#    json.dump(etfsdata , f)

#with open('D:/OneDrive/Documentos/PROGRAMAÇÃO/VSCODE/CARTEIRA INVEST/Data/fiisdata.json' , 'w') as f:
#    json.dump(fiisdata , f)

#with open('D:/OneDrive/Documentos/PROGRAMAÇÃO/VSCODE/CARTEIRA INVEST/Data/fiinfras.json' , 'w') as f:
#    json.dump(fiinfrasdata , f)

print('Fin.')
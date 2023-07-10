import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_formatting import cellFormat, color, format_cell_range, textFormat, batch_updater
import time

scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pessoas = {}
with open("pessoas.txt", "r", encoding="utf8") as t:
    linhas = t.readlines()
    for i in range(len(linhas)):
        pessoas[linhas[i].replace("\n", "")] = []

def readTask():
    credenciais = ServiceAccountCredentials.from_json_keyfile_name(f'reader.json'
                , scope)
    gc = gspread.authorize(credenciais)
    planilha = gc.open('Prestação de contas')

    pag = planilha.get_worksheet(0)
    info = pag.get_all_values()

    #Organizar informações da primeira planilha em dicts
    pessoasAlteradas = []
    for l in range(1, len(info)):
        p = info[l][1]
        for c in range(2, len(info[0])-3):
            if info[l][c] != '':
                for n in info[l][c].split(", "):
                    número = 10*(c-2) + int(n)
                    if número not in pessoas[p]:
                        pessoas[p].append(número)
                        if p not in pessoasAlteradas:
                            pessoasAlteradas.append(p)
        pessoas[p].sort()
    return pessoasAlteradas

def updateTask(force=False, reset=-1):
    credenciais = []
    planilha = []
    gc = []
    pagf = []
    pag = []
    batch = []

    pessoasAlteradas = readTask()
    if reset != -1:
        pessoas[list(pessoas.keys())[reset]] = []

    for w in range(3):
        credenciais.append(ServiceAccountCredentials.from_json_keyfile_name(f'worker{w+1}.json'
                , scope))

        gc.append(gspread.authorize(credenciais[w]))
        planilha.append(gc[w].open('Rifa de 100 pontos'))
        pagf.append(planilha[w].get_worksheet(0))
        pag.append(planilha[w].get_worksheet(1))
        batch.append(batch_updater(pag[w].spreadsheet))

    infof = pagf[0].get_all_values()
    info2 = pag[0].get_all_values()

    verdinho = cellFormat(
    backgroundColor=color(.576, .768, .49),
    textFormat=textFormat(bold=False, foregroundColor=color(1, 1, 1))
    )
    vermelho = cellFormat(
    backgroundColor=color(.85, .917, .827),
    textFormat=textFormat(bold=False, foregroundColor=color(0, 0, 0))
    )



    #Atualizar coisas na segunda planilha
    ii = 0
    if pessoasAlteradas or force:
        #Planilha de cartelas
        for l in range(len(info2)):
            for c in range(len(info2[0])):
                if c in [0, 11, 22] and (l+12)%12==0:
                    if ii == 45:
                        break
                    pessoa = list(pessoas.keys())[ii]
                    #pag.update_cell(l+1, c+1, pessoa)

                    if pessoa in pessoasAlteradas or force:
                        for i in range(100):
                            cor = verdinho if int(str(ii*100 + i+1)[-2::]) in pessoas[pessoa] else vermelho
                            coord = f"{alfabeto[c + i%10]}{l+2 + i//10}" if c + i%10 < 26 else f"A{alfabeto[c + i%10-26]}{l+2 + i//10}"
                            for w in range(3):
                                if ii >= w*15 and ii < 15+w*15:
                                    batch[w].format_cell_range(pag[w], coord, cor)
                                    #pag[w].update_cell(l+2 + i//10, c+1 + i%10, ii*100 + i+1)
                            #time.sleep(0.333)
                        for w in range(3):
                            try:
                                batch[w].execute()
                            except:
                                pass
                    ii += 1

        #Atualizar na segunda planilha
        for l in range(2, 45+2):
            pessoa = list(pessoas.keys())[l-2]
            if pessoa in pessoasAlteradas or force:
                for w in range(3):
                    if l > w*15 and l <= 15+w*15+1:
                        pagf[w].update_cell(l, 3, len(pessoas[pessoa]))


if __name__ == '__main__':
    updateTask()

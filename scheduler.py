import planilha
import time
while True:
    pA = planilha.readTask()
    planilha.pessoasAlteradas = pA
    if pA:
        planilha.updateTask()
    time.sleep(1200)
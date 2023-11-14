#ex2

def find(wze,ew):
    with open('meine_datei.txt','r') as f:
        text = f.read()
        nr = text.count(wze)
        text_nou = text.replace(wze, ew)
    with open('meine_datei.txt','w') as f:
        f.write(text_nou)
    if nr==0:
        print(f' Kein Ersatzwort gefunden')
    else:
        print(f'Ersetzt {wze} durch {ew} an {nr} Stellen')

wze=input('wort zu ersetzen=')
ew=input('Ersatzwort=')
find(wze,ew)



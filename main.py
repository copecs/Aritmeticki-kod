def izdvoji_simbole(sentence):
    simboli = []
    for char in sentence:
        if char not in simboli:
            simboli.append(char)
    verovatnoce = {simb:0 for simb in simboli}
    ukupno = 0
    for char in sentence:
        verovatnoce[char]+=1
        ukupno+=1
    for key in verovatnoce.keys():
        verovatnoce[key]/=ukupno
    return simboli,verovatnoce

def aritmeticki_kodiraj(sentence,verovatnoce):
    low = 0
    high = 1
    for char in sentence:
        interval = high - low
        for key in verovatnoce.keys():
            if(key == char) : break
            else: low+=verovatnoce[key]*interval
        found = 0
        for key in verovatnoce.keys():
            if(key == char) :
                found = 1
                continue
            if(found): high-=verovatnoce[key]*interval
        #print("char:{} high:{} low:{} interva:{}".format(char,high,low,interval));

    return (high+low)/2

def aritmeticki_dekodiraj(sifra,verovatnoce,duzina):
    low = 0
    high = 1
    poruka = ""
    for i in range(duzina):
        interval = high - low
        newlow = low
        newhigh = high
        for key in verovatnoce.keys():
            newhigh = newlow+verovatnoce[key]*interval
            if(sifra>=newlow and sifra <=newhigh):
                poruka+=key
                break
            newlow = newhigh
        low=newlow
        high=newhigh
    return poruka

sentence = "BACA ABAC BACA"
simboli,verovatnoce = izdvoji_simbole(sentence)
kodirana_poruka = aritmeticki_kodiraj(sentence,verovatnoce)
print(kodirana_poruka)
dekodirana_poruka = aritmeticki_dekodiraj(kodirana_poruka,verovatnoce,len(sentence))
print(dekodirana_poruka)
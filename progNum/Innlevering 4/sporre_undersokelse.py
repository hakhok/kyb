from sys import exit


antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0

run = True
while run:
    while True:
        kjonn = input("\nMan eller dame? m/d ")
        if kjonn == "d":
            antall_kvinner += 1
        elif kjonn == "m":
            antall_menn += 1
        elif kjonn == "hade":
            run = False
            break
        alder = input("Alder? ")
        if alder == "hade":
            run = False
            break
        if not 16 <= int(alder) <= 25:
            break
        svar = " "
        while svar not in ["j", "n", "hade"]:
            svar = input("Tar du fag? ")
        if svar == "j":
            antall_fag += 1
        elif svar == "hade":
            run = False
            break
        if int(alder) < 22:
            medlem_ITGK = input("Tar du ITGK? j/n ")
        else:
            medlem_ITGK = input("Tar virkelig du ITGK? j/n ")
        if medlem_ITGK == "j":
            antall_ITGK += 1
        elif medlem_ITGK == "hade":
            run = False
            break
        timer_lekser = input("Hvor mange timer lekser gjør du i snitt hver dag? ")
        if timer_lekser == "hade":
            run = False
            break
        antall_timer_lekser += float(timer_lekser)

try:
    print(f"\nAntall kvinner: {antall_kvinner}")
    print(f"Antall menn: {antall_menn}")
    print(f"Antall personer som tar fag: {antall_fag}")
    print(f"Antall personer som tar ITGK: {antall_ITGK}")
    print(f"Antall timer i snitt brukt på lekser: {antall_timer_lekser/(antall_kvinner+antall_menn)}")
except:
    pass

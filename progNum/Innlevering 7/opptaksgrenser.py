import csv

with open('poenggrenser_2011.csv') as csvfile:
    csvreader = csv.reader(csvfile)

    number_of_alle = 0
    number_of_others = 0.0
    total_score = 0.0
    min_score = 100
    min_studie = ""
    study_dict = {}
    for row in csvreader:
        if row[1]=='Alle':
            number_of_alle += 1
        elif row[0][0:4]=="NTNU":
            number_of_others+=1
            total_score+=float(row[1])
        if row[1] != 'Alle' and float(row[1]) < min_score:
            min_score = float(row[1])
            min_studie = row[0]
        school = row[0].split(' ')[0]
        if not school in study_dict:
            study_dict[school] = []
        
        study_dict[school].append({row[0].split(' ')[2]: row[1]})

    print(f"Antall studier der alle kom inn: {number_of_alle}")
    print(f"Gjennomsnittelig poengrense: {round(total_score/number_of_others, 2)}")
    print(f"{min_studie} hadde minst opptakskrav med {min_score}")
    for school in study_dict:
        print(school, study_dict[school])

import csv
import os

# Target folder for CSV files
target_folder = "db"
os.makedirs(target_folder, exist_ok=True)

# Pseudo data for 10 people: each answer is a separate string
data = [
    ["Dass ich lustig bin.", 
     "Wahrscheinlich, dass ich manchmal etwas faul bin und Dinge gerne aufschiebe. Ich komme auch oft zu spät.", 
     "Alleine zu sein.", 
     "Mein Hund, meine Freunde und Musik.", 
     "Menschen, die Hinter dem Rücken anderer über sie reden."],

    ["Dass ich immer für meine Freunde und Familie da bin.", 
     "Dass ich ungeduldig bin. Meine Eltern sagen auch, dass ich manchmal zu viel rede.", 
     "Spinnen.", 
     "Meine Familie, meine Freundinnen, Tiere (besonders Katzen) und Musik. Ich mag es auch, zu malen oder draußen zu sein, wenn das Wetter schön ist.", 
     "Leute, die andere ärgern oder gemein sind. Ich finde es total doof, wenn jemand ausgelacht oder ausgeschlossen wird."],

    ["Dass ich ruhig und ausgeglichen bin und während stressigen Situationen meist gelassen bleibe.", 
     "Dass ich manchmal zu zurückgezogen bin und lange brauche, um mit Menschen warm zu werden.", 
     "Ich habe Angst, Fehler zu machen und von anderen falsch verstanden zu werden.", 
     "Meine Familie und Freunde.", 
     "Leute, die laut und respektlos sind. Ich finde es unangenehm, wenn jemand immer im Mittelpunkt stehen will und andere dabei übergeht."],

    ["Dass ich nett und lustig bin.", 
     "Dass ich manchmal meine Hausaufgaben nicht mache.", 
     "Im Dunkeln zu sein.", 
     "Fußball spielen und mein Hund.", 
     "Kinder, die gemein sind und andere ärgern."],

    ["Meine Mutter sagt oft, dass ich ehrgeizig bin.", 
     "Manchmal bin ich schnell genervt weil ich ungeduldig bin.", 
     "Ich habe Angst davor, dass meinen Eltern etwas schlimmes passiert.", 
     "Meine Familie und Bücher.", 
     "Leute, die andere mobben. Ich mag auch keine Lügner und Angeber."]
]

# Column headers
headers = ["ID", "Q1", "Q2", "Q3", "Q4", "Q5"]

# Create CSV files
for i, responses in enumerate(data, start=1):
    person_id = str(i).zfill(5)
    filename = os.path.join(target_folder, f"{person_id}.csv")
    
    # Write CSV with quotes around every field (handles commas inside answers)
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)
        writer.writerow([person_id] + responses)

print(f"Created {len(data)} CSV files in '{target_folder}' folder with proper quoting for commas.")

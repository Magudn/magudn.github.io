import csv
import os

# Target folder for CSV files
target_folder = "db"
os.makedirs(target_folder, exist_ok=True)

# Pseudo data for 10 people: each answer is a separate string
data = [
    ["Ich bin zuverlässig und ehrlich. Wenn ich etwas verspreche, halte ich es auch. Außerdem kann man mit mir immer gut lachen.", 
     "Ich bin manchmal zu ungeduldig. Wenn etwas nicht sofort klappt, verliere ich schnell die Lust. Und ich kann ziemlich stur sein.", 
     "Ich habe Angst davor, wichtige Menschen zu verlieren. Manchmal auch davor, zu scheitern oder nicht gut genug zu sein. Das beschäftigt mich öfter, als ich zugeben möchte.", 
     "Lange Gespräche mit Freunden, gutes Essen und Musik. Ich liebe Spaziergänge bei Sonnenuntergang. Und wenn es regnet, bleibe ich gern mit einem Buch zu Hause.", 
     "...sich ständig über andere lustig machen. Arroganz und Respektlosigkeit finde ich furchtbar. Ein bisschen Demut steht jedem gut."],

    ["Ich bin hilfsbereit und immer für meine Freunde da. Außerdem bin ich ziemlich kreativ und habe immer neue Ideen.", 
     "Manchmal bin ich faul und schiebe Dinge vor mir her. Außerdem rede ich manchmal zu viel.", 
     "Ich habe Angst davor, vor anderen blöd dazustehen. Auch vor Prüfungen bin ich manchmal richtig nervös.", 
     "Videospiele spielen, Musik hören und draußen Sport machen. Ich liebe es auch, Zeit mit meinen Freunden zu verbringen.", 
     "Leute, die andere mobben oder ständig gemein sind. Auch Fake-Freundlichkeit nervt mich."],

    ["Ich bin loyal und halte meine Versprechen. Meine Freunde sagen, ich sei lustig und positiv.", 
     "Ich kann manchmal ziemlich stur sein und will immer Recht haben. Außerdem vergesse ich manchmal Dinge.", 
     "Ich habe Angst davor, allein zu sein oder dass etwas Schlimmes meiner Familie passiert.", 
     "Fußball spielen, Serien schauen und mit Freunden quatschen. Ich liebe auch Pizza und Schokolade.", 
     "Leute, die arrogant sind oder andere runterziehen. Ich mag keine Lügner."],

    ["Ich bin freundlich und geduldig. Viele sagen, ich sei ein guter Zuhörer.", 
     "Ich bin oft zu schüchtern und traue mich nicht, meine Meinung zu sagen. Manchmal überlege ich zu viel.", 
     "Ich habe Angst davor, meine Ziele nicht zu erreichen. Auch davor, dass Freunde mich enttäuschen, mache ich mir Sorgen.", 
     "Zeichnen, lesen und Musik hören. Ich liebe auch Spaziergänge mit meinem Hund.", 
     "Leute, die unfreundlich oder egoistisch sind. Ich mag keine Menschen, die andere ständig kritisieren."],

    ["Ich bin lustig und sportlich. Meine Freunde sagen, ich bin loyal und ehrlich.", 
     "Ich kann schnell genervt sein und verliere manchmal die Geduld. Auch zu faul sein passiert öfter.", 
     "Ich habe Angst davor, etwas Wichtiges zu verpassen oder zu versagen.", 
     "Skateboard fahren, Musik hören und mit Freunden chillen. Ich liebe auch Pizza und Filme.", 
     "Leute, die andere mobben oder nur an sich denken. Ich mag keine Lügner und Angeber."]
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

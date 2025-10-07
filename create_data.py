import csv
import os

# Target folder for CSV files
target_folder = "db"
os.makedirs(target_folder, exist_ok=True)

# Pseudo data for 10 people: each answer is a separate string
data = [
    ["Öffentlich freundlich, hilfsbereit, humorvoll", "Ungeduldig, stur", "Höhen", "Musik hören, wandern, lesen", "Unhöfliche Menschen"],
    ["Zuverlässig, aufmerksam, ehrlich", "Schüchtern, nervös", "Spinnen", "Kochen, Freunde treffen", "Lügner"],
    ["Kreativ, motiviert, neugierig", "Unorganisiert, vergesslich", "Enge Räume", "Filme schauen, reisen", "Ignorante Menschen"],
    ["Hilfsbereit, geduldig, freundlich", "Zögerlich, unentschlossen", "Dunkelheit", "Fotografie, Musik", "Rücksichtlose Autofahrer"],
    ["Ehrlich, loyal, humorvoll", "Ungeduldig, nervös", "Schlangen", "Sport, Lesen, Musik", "Egoistische Menschen"],
    ["Zuverlässig, freundlich, offen", "Schnell gestresst, stur", "Spinnen", "Wandern, Kochen", "Unzuverlässige Kollegen"],
    ["Kreativ, lustig, hilfsbereit", "Schnell abgelenkt, ungeduldig", "Höhen", "Videospiele, Filme, Freunde", "Unhöfliche Menschen"],
    ["Motiviert, ruhig, freundlich", "Schüchtern, introvertiert", "Dunkelheit", "Lesen, Musik, Yoga", "Lügner"],
    ["Neugierig, offen, ehrlich", "Vergesslich, nervös", "Enge Räume", "Reisen, Fotografie", "Ignoranz"],
    ["Lustig, loyal, kreativ", "Ungeduldig, stur", "Spinnen", "Filme, Freunde, Sport", "Rücksichtslosigkeit"]
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

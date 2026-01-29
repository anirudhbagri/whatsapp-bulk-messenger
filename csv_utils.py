import csv
import re

def load_numbers_from_csv(csv_path):
    numbers = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for cell in row:
                cell = cell.strip().replace(" ", "")
                # + ile başlıyorsa baştaki + işaretini kaldır
                if cell.startswith("+"):
                    cell = cell[1:]
                # Sadece rakamlardan oluşan ve 8-15 haneli olanları al (ülke kodu başta olacak şekilde)
                if re.fullmatch(r"\d{8,15}", cell):
                    numbers.append(cell)
    return numbers

if __name__ == "__main__":
    # Örnek kullanım
    csv_path = 'Numaralar.csv'  # CSV dosya yolunuzu buraya yazın
    numbers = load_numbers_from_csv(csv_path)
    print(numbers)
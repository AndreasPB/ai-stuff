# Job for selecting only the reviews from a Steam Review dataset from Kaggle
# https://www.kaggle.com/datasets/andrewmvd/steam-reviews?resource=download
import csv


with open("dataset.csv") as file_one, open("steam_reviews.txt", "w") as file_two: 
    reader = csv.reader(file_one, delimiter=",")

    line_count = 0
    for row in reader:
        file_two.write(f"{row[2]}\n\n")

        if line_count == 100000:
            break        

        line_count += 1

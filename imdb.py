from bs4 import BeautifulSoup
import requests

import csv

url = 'https://www.imdb.com/chart/toptv/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')

tv_shows = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent')

print(len(tv_shows))

csv_filename = "tv_shows_data1.csv"


with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    # Write the header row
    header = ['Rank', 'Name', 'Year', 'Rating']
    writer.writerow(header)

    # Write data for each movie in the list
    for show in tv_shows:
        name = show.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title').a.text.split('.')[1]
        rank = show.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title').a.text.split('.')[0]
        year = show.find('div', class_='sc-b0691f29-7 hrgukm cli-title-metadata').span.text
        rating = show.find('div', class_='sc-e2dbc1a3-0 ajrIH sc-b0691f29-2 bhhtyj cli-ratings-container').span.text

        # Write the data row for the current movie directly to the CSV file
        writer.writerow([rank, name, year, rating])

print("Data has been written to the CSV file:", csv_filename)
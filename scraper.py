# Import libraries
from collections import defaultdict
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# Convert titles and data into lists of stings
def main():
    print('Starting up')
    title_list = header()
    data_list = new_data()
    print(title_list)
    print(data_list)
    
    matrix = defaultdict(list)
    for title_i, title_v in enumerate(title_list):
        print(title_i, title_v)
        print(len(title_list))
        for i, v in enumerate(data_list):
            if (i) % (len(title_list)) == (title_i):
                matrix[title_v].append(v)
    
    write(matrix)
    
    print('Done!')

# Specify a URL max offset = 3625, current date range: 1 Jan 2016 - 18 June 2018
def soup(offset = 0):
    quote_page = f'https://incidentreports.uchicago.edu/incidentReportArchive.php?startDate=1451628000&endDate=1528952400&offset={offset}'
    print('Fetching html code...')
    page = urlopen(quote_page)
    print('Generating soup...')
    soup = BeautifulSoup(page, 'html.parser')
    print('Returning soup...')
    return soup

# Generate table headers
def header():
    print('Fetching headers...')
    s = soup(0)
    titles = s.find_all('th')
    title_list = []
    print('Generating titles...')
    for t in titles:
        title_list.append(t.get_text())
    print('Return titles...')
    return title_list

# Gather data from table on website [DEFUNCT]
def data():
    print('Fetching crime data...')
    data_list = []
    for o in range(0, 6, 5):
        print(f'Offset = {o}')
        s = soup(o)
        print('Compiling data into list...')
        data = s.find_all('td')
        for d in data:
            data_list.append(d.get_text())
    print('Returning data...')
    return data_list

# Gather data from table on website, filtering void or false incident reports, adding blank strings to missing entries
def new_data():
    print('Fetching crime data...')
    data_list = []
    for o in range(0, 3626, 5):
        print(f'Offset = {o}')
        s = soup(o)
        print('Compiling data into list...')
        data = s.find_all('tr')
        for d in data:
            for content in d.contents:
                if content.name == 'td' and content.string is None:
                    data_list.append('')
                elif content.name == 'td' and content.string.lower() == 'void' or content.string == ':':
                    break
                elif content.name == 'td' and 'No Incident' in content.string:
                    break
                elif content.name == 'td':
                    data_list.append(content.string)
    return data_list

# Write the scraped table to a CSV file
def write(matrix):
    with open('crime.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter = ',')
        writer.writerow(matrix.keys())
        for v in matrix.values():
            num_incidents = range(len(v))
            break
        print('Writing')
        for n in num_incidents:
            row = []
            for k in matrix.keys():
                row.append(matrix[k][n])
            writer.writerow(row)

if __name__ == '__main__': main()
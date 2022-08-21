from pathlib import Path
from requests import get
from time import sleep

# table_nums = ['22', '10', '35']
# BASE_URL= f'https://ucr.fbi.gov/crime-in-the-u.s/{YEAR}/crime-in-the-u.s.-{YEAR}/tables/table-{TABLE_NUM}/table-{TABLE_NUM}.xls/output.xls'

for year in range(1995,2020):
    table_num = 1
    while True:
        filename = Path(f'./downloads/table-{table_num}_{year}.xls')
        url = f'https://ucr.fbi.gov/crime-in-the-u.s/{year}/crime-in-the-u.s.-{year}/tables/table-{table_num}/table-{table_num}.xls/output.xls'

        response = get(url)

        if 'this page does not seem to exist' in response.text.lower():
            print('no table at ' + url)
            break

        elif 'aggravated assault' in response.text.lower():
            print('downloading table from ' + url)
            filename.write_bytes(response.content)
        sleep(2)
        table_num += 1

print('done')
import pandas as pd
import json
from bs4 import BeautifulSoup
def import_data(filepath):
    reports = []
    with open(filepath) as f:
        for i in f:
            reports.append(json.loads(i))
    return reports
def parse_data(soup):
    features = ['YEAR', 'SEASON', 'MONTH', 'STATE', 'COUNTY', 'LOCATION DETAILS',
       'NEAREST TOWN', 'NEAREST ROAD', 'OBSERVED', 'ALSO NOTICED',
       'OTHER WITNESSES', 'OTHER STORIES', 'TIME AND CONDITIONS',
       'ENVIRONMENT', 'DATE']
    d = dict()
    d['id'] = soup.title.text.split(':')[0].split(' ')[-1]
    for i in range(len(soup.find_all('p'))):
        try:
            split_text = soup.find_all('p')[i].text.split(':',1)
            if split_text[0] in features:
                d[split_text[0]] = split_text[1].strip(' ')
        except:
            pass
    d['submitted_date'] = ' '.join(soup.find_all('span', {'class': 'field'})[0].text.split(',')[1:]).replace('\xa0', '-').replace(' ','').strip('-').strip('.')
    return d
def create_dataframe(reports):
    reports_df = pd.DataFrame()
    for report in reports:
        try:
            soup = BeautifulSoup(report['html'], 'html.parser')
            report_dict = parse_data(soup)
            report_df = pd.DataFrame(report_dict, index=[0])
            reports_df = reports_df.append(report_df, ignore_index=True)
        except:
            print('error in report')
    return reports_df
def get_data(filepath):
    reports = import_data(filepath)
    data = create_dataframe(reports)
    data['text'] = (data['OBSERVED'].astype(str)
                + data['OTHER STORIES'].astype(str)
                + data['OTHER WITNESSES'].astype(str)
                + data['TIME AND CONDITIONS'].astype(str)
                + data['ALSO NOTICED'].astype(str)
                + data['LOCATION DETAILS'].astype(str)
                + data['ENVIRONMENT'].astype(str))
    csv_path = filepath.replace('json','csv')
    data.to_csv(csv_path, sep='\t')
    return data
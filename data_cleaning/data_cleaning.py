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
    
    d = dict()
    d['id'] = soup.title.text.split(':')[0].split(' ')[-1]
    for i in range(len(soup.find_all('p'))-4):
        try:
            split_text = soup.find_all('p')[i].text.split(':',1)
            d[split_text[0]] = split_text[1]#.strip(' ')
        except:
            pass
    try:
        d['Follow Up from Investigator'] = soup.find_all('p')[-3].text
        d['About Investigator'] = soup.find_all('p')[-1].text
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
            reports_df = reports_df.append(report_df)
        except:
            print('error in report')
    
    return reports_df

def get_data(filepath):
    
    reports = import_data(filepath)
    return create_dataframe(reports)
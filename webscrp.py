import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

# df = pd.read_excel('isis_major_code_list.xlsx', 'Major Codes')
# majorsOnly = df.copy()[['Diploma Title']]
# majorsOnly = majorsOnly.dropna().reset_index(drop=True)

df = pd.read_excel('isis_major_code_list.xlsx', 'Major Codes')

majors_only = df.copy()[['Diploma Title']]

majors_only = majors_only.dropna().reset_index(drop=True)

# htmlDf = majorsOnly.to_html()
# htmlDf

text_file = open("htmldf.html", "w")
text_file.write(htmlDf)
text_file.close()


# Marshall Test
marshall_url = 'https://marshall.ucsd.edu/academics/general-education-requirements.html'
res = requests.get(marshall_url)
soup = BeautifulSoup(res.text)

doc = soup.find_all('li', attrs={"class":"dropdown open"})[3]
doc = [doc_class.text for doc_class in doc.find_all('li') if 'DOC ' and ':' in doc_class.text]

content = soup.find('div', attrs = {'class':'drawer dark-theme'})
marsh_classes = content.find_all('ul', attrs = {'class':'list-group'})

marsh_bio = marsh_classes[0]
marsh_bio = [bio_class.text for bio_class in marsh_bio.find_all('li')]

marsh_chem = marsh_classes[1]
marsh_chem = [chem_class.text for chem_class in marsh_chem.find_all('li')]

marsh_phys = marsh_classes[2]
marsh_phys = [phys_class.text for phys_class in marsh_phys.find_all('li')]

# options a, b, c
marsh_math = marsh_classes[3]
marsh_math = [math_class.text for math_class in marsh_math.find_all('li')]

marsh_stats = marsh_classes[4]
marsh_stats = [stat_class.text for stat_class in marsh_stats.find_all('li')]

marsh_log = marsh_classes[5]
marsh_log = [log_class.text for log_class in marsh_log.find_all('li')]

# 2
marsh_hum = marsh_classes[6]
marsh_hum = [hum_class.text for hum_class in marsh_hum.find_all('li')]

# 1
marsh_art = marsh_classes[7]
marsh_art = [art_class.text for art_class in marsh_art.find_all('li')]

marshall_ges = [marsh_bio, marsh_chem, marsh_phys, 
               marsh_math, marsh_stats, marsh_log,
               marsh_hum,
               marsh_art]

clean_marshall_ges = []

for req in marshall_ges:
    
    these = []
    
    for option in range(len(req)):
        
        if len(req[option].split(',')) > 1:
            
            course_code = req[option].split(',')[0].split()[0]
            listed = ([req[option].split(',')[0]] + 
                      [(course_code + course_num.replace('or', '')) 
                       for course_num in req[option].replace('or', ',or').split(',')[1:]]
                     )
            
            these += listed
            
        elif len(req[option].split('or')) > 1:
            
            course_code = req[option].split('or')[0].split()[0]
            listed = [req[option].split('or')[0], course_code + req[option].split('or')[1]]
            these += listed
            
        else:
            these.append(req[option])
            
    clean_marshall_ges.append(these)

subdivs = content.find_all('h3', attrs={'class':'panel-title'})
docless = [sub.text for sub in subdivs][3:]
marshall_docless_ges = dict(zip(docless, clean_marshall_ges))
marshall_docless_ges

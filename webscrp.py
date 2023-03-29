import pandas as pd
import numpy as np

df = pd.read_excel('isis_major_code_list.xlsx', 'Major Codes')

majorsOnly = df.copy()[['Diploma Title']]

majorsOnly = majorsOnly.dropna().reset_index(drop=True)

htmlDf = majorsOnly.to_html()

htmlDf

text_file = open("htmldf.html", "w")
text_file.write(htmlDf)
text_file.close()

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import matplotlib.pyplot as plt
import matplotlib

# total summmary 
# start
def summmary():
        r = requests.get('https://covid19.mohp.gov.np/covid/api/confirmedcases').json()
        df=pd.DataFrame(r)
        df=df['nepal']
        return(df)

        






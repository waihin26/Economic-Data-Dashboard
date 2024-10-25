import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

def continued_claims(start_date =None, end_date=None):
    if not start_date:
        start_date = '2015-01-01'
    if not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d') #today
    name, code = 'Continued Claims', 'CCSA'
    df = web.DataReader(code, 'fred', start_date, end_date)
    df.columns = [name]
    return df



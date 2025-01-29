import pandas as pd
import numpy as np
from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
file_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'
await download(file_path, "auto.csv")
file_name="auto.csv"
df = pd.read_csv(file_name)
print("The bottom 10 rows are: ")
df.tail(10)
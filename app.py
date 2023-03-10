import pandas as pd

import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout='wide')

def file_to_df(file):
    
    fn = file.name
    
    if fn.endswith('.csv'):
        df = pd.read_csv(file)
        return df
        
    elif fn.endswith('.xls') or fn.endswith('.xlsx'):
        df = pd.read_excel(file,  engine = 'openpyxl')
        return df
        
    elif fn.endswith('.txt'):
        df = pd.read_csv(file, sep = "\t", engine='python', encoding = "cp949")
        return df
    
    else:
        message = "파일 업로드 불가"
        st.exception(message)
        
def main():          
    file = st.sidebar.file_uploader("데이터 파일을 업로드하시오.", type={"xlsx", "xls", "csv", "txt"})
    
    if file is not None:
        df = file_to_df(file)     
        pr = df.profile_report()
        st_profile_report(pr)


if __name__ == '__main__':
    main()
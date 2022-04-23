import glob                       #glob is used for searching and selecting files
import pandas as pd               #I have used pandas for ETL Process
import os
#path='D:\etl\sample_data'
d_path = os.path.abspath(os.curdir)+'\sample_data'

#PART 1

  # Extract / Read for txt files from sample data
textFiles=glob.glob(d_path+'\*.txt')     
for file_ in textFiles:

    
    df=pd.read_csv(file_)   
    
    
    # Transormation for capitalize each word in txt files
    df.columns=df.columns.str.title()
   
  

    # Load for txt files
    txt_name=os.path.basename(file_)
    df.to_csv(d_path+'_sol_'+txt_name);  
    
#PART 2

    # Extract / Read for csv files from sample data
csvFiles=glob.glob(d_path+'\*.csv')
for file_ in csvFiles:
    df=pd.read_csv(file_)
    
    # Transormation for word count of csv files  
    df=(df.apply(pd.Series.value_counts))
  
    

    # Load for csv files
    csv_name=os.path.basename(file_)
    df.to_csv(d_path+'_sol_'+csv_name); 




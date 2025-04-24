import numpy as np
import pandas as pd
import joblib
from category_encoders import TargetEncoder

encoder = joblib.load('target_encoder.pkl')
def preprocess_input(df):
  # convert_cols=['ChronicCond_Alzheimer',
  #      'ChronicCond_Heartfailure', 'ChronicCond_KidneyDisease',
  #      'ChronicCond_Cancer', 'ChronicCond_ObstrPulmonary',
  #      'ChronicCond_Depression', 'ChronicCond_Diabetes',
  #      'ChronicCond_IschemicHeart', 'ChronicCond_Osteoporasis',
  #      'ChronicCond_rheumatoidarthritis', 'ChronicCond_stroke']
  # for i in convert_cols:
  #     df[i]=df[i].map({1:0,2:1})
  #Converting RenalDiseaseIndicator to 0 and 1    
  # df['RenalDiseaseIndicator']=df['RenalDiseaseIndicator'].map({'Y':1,'0':0}) 
  df['DOB']=pd.to_datetime(df['DOB']).dt.year
  df['age']=2009-df['DOB']
  df.drop('DOB',axis=1,inplace=True)
  df['ClaimStartDt']=pd.to_datetime(df['ClaimStartDt'])
  df['ClaimEndDt']=pd.to_datetime(df['ClaimEndDt'])
  df['clm_duration']=(df['ClaimEndDt']-df['ClaimStartDt']).dt.days 
  df.drop(['ClaimStartDt','ClaimEndDt'],axis=1,inplace=True)
  df['AdmissionDt']=pd.to_datetime(df['AdmissionDt'],errors='coerce') 
  df['DischargeDt']=pd.to_datetime(df['DischargeDt'],errors='coerce')  
  df['LOS']=(df['DischargeDt']-df['AdmissionDt']).dt.days
  df['LOS'].fillna(0,inplace=True)
  df.drop(['AdmissionDt','DischargeDt'],axis=1,inplace=True)
  # encoding_cols=['Provider','BeneID','AttendingPhysician','ClmDiagnosisCode_1']
  encoding_cols=['Provider','BeneID','AttendingPhysician']
  df[encoding_cols]=encoder.transform(df[encoding_cols])
  
  return df
  

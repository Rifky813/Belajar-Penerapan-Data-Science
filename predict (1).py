import joblib
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

pipe_lr = joblib.load("/content/drive/MyDrive/Colab Notebooks/Penerapan-Data-Science_First-Submission /model_lr.pkl")

df_to_predict = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Penerapan-Data-Science_First-Submission /df_to_predict.csv')

df_to_predict = df_to_predict.drop(columns=['EmployeeCount', 'StandardHours', 'Over18', 'EmployeeId', 'Attrition'])

prediction = pipe_lr.predict(df_to_predict)

prediction = pd.DataFrame(prediction, columns=['Attrition_Predicted'], index=df_to_predict.index)
prediction.head(10)

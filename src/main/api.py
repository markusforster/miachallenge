import torch
import numpy as np
import pandas as pd

from fastapi import FastAPI, Body
import uvicorn
from transformers import AutoTokenizer

app = FastAPI()

model = torch.load('../../icd.pt')
df = pd.read_csv('../../icd.csv',delimiter=';',header=None)

tokenizer = AutoTokenizer.from_pretrained('distilbert-base-german-cased') 

no_to_label = {i:x[1] for i,x in enumerate(df.iloc())}

@app.get("/")
async def root():
    return {"message": "MIA Challenge API v0.01"}

@app.post("/predict_icd")
async def predict_icd(payload: dict = Body(...)):
    token = tokenizer(payload["payload"].lower(), max_length=10,
    padding='max_length', truncation=True, return_tensors='pt')
    toke = token.to(device='cuda')
    output = no_to_label[(np.argmax(model(**token).logits.detach().cpu().numpy()))]
    return output 
    

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')


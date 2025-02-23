
from fastapi import FastAPI, HTTPException
from langchain_groq import ChatGroq
from all_keys import groq_api_key
from langchain.prompts import PromptTemplate

app = FastAPI()


llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key = groq_api_key,
    temperature = 0.6
)

prompt_features = PromptTemplate(
    input_variables = ["company","Budget"],
    template = ''' 
     suggest mobile phones of {company} for the price range of {Budget},

    ### INSTRUCTIONS
    - list should include camera , battery_capacity, processor, price on 2 diff platforms
    - Strictly no preamble
'''
)




@app.get("/")

def home():
    return "welcome to api bhai"

@app.get("/search")

async def search(company : str, price_range : str):

    query = prompt_features.format(company=company,Budget = price_range)
    response = llm.invoke(query)

    return {"fetched results" : response}
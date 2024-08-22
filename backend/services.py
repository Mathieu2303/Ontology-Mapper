import os
from openai import AzureOpenAI
from config import CRITERIA_CONFIG
import config
#import json
from datetime import date
from testFind import getPromptFromCriteria, filteringForQueryAndInput, getChemblID, storingResultData
from langchain_core.utils.json import parse_json_markdown



client = AzureOpenAI(
    api_key=config.AZURE_OPENAI_API_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
)


def callAzureAiService(prompt, AiCriteria):
   # print(config.AZURE_OPENAI_API_KEY)
   # print(config.AZURE_OPENAI_ENDPOINT)
    response = client.chat.completions.create(
        model="nlp-poc",  # model = "deployment_name".
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": str(AiCriteria)},
        ],
    )
   # print(response.model_dump_json(indent=2))
   # print(response.choices[0].message.content)

    return response.choices[0].message.content


def mrnQuery(body):
   # print("calling MRN query function")
    dbCritera = filteringForQueryAndInput(body)
    prompt = getPromptFromCriteria(body["desc"])  # gets prompt
    response = callAzureAiService(
        prompt, dbCritera["criteria"]
    )  # calls ai chat services with the prompt and criteria needed mro

    
    resp = {}
    resp["azure"] = parse_json_markdown(response)#[{"chemblid": "3423", "preferred medication name": "abx"}]
    #saving result data to db
    if body["desc"]  == "Medication":
        for medication in resp["azure"]:
            medication["calculated_chemblid"] = getChemblID(medication["Preferred Medication Name"])
    resp["city_of_hope"] = dbCritera["result"]
    resp["ai_input"] = dbCritera["criteria"]
    storingResultData(body, resp["azure"])
    return resp


def getAllDescriptions():
    namesList = []
    for name in CRITERIA_CONFIG:
        namesList.append({"desc":name["desc"]})
    print(namesList)
    return namesList


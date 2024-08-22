import pyodbc
import config
from config import CRITERIA_CONFIG, SERVER, DATABASE, USERNAME, PASSWORD
import json
# Construct the connection string
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};"


def filteringForQueryAndInput(body):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    First = True
    inputVariables = definingInputParameters(body["desc"])  # [ex: "mrn", date]
    dynamic_sql_query = getQueryFromCriteria(
        body["desc"]
    )  # given name will pull associated query (dynamic_sql_query = Function)
    convertedStringQuery = StringConvertion(dynamic_sql_query)
    parameterValues = []
    for input in inputVariables:
        parameterValues.append(body[input])
        if First == True:
            convertedStringQuery += f" @{input}=?"
            First = False
        else:
            convertedStringQuery += f", @{input}=?"

    cursor.execute(
        convertedStringQuery, parameterValues
    )  # will execute with given input
    rows = cursor.fetchall()
    criteria_array = []
    result_array = []
    criteria = {}
    result = {}
    response = {}
    values = getCriteriaConfig(body["desc"]) #returns the dict

    for row in rows:
        for resultData in values["result"]:
            result[resultData] = getattr(row, resultData)
        for criteriaData in values["criteria"]:
            criteria[criteriaData] = getattr(row, criteriaData)
        result_array.append(result)
        result = {}
        criteria_array.append(criteria)
        criteria = {}
        
    response["criteria"] = criteria_array
    response["result"] = result_array

    return response


def storingResultData(body, ai_response):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    mrn = body["mrn"]
    name = body["desc"]
    formated_ai_results = json.dumps(ai_response)
    print("ai_reponse: ", formated_ai_results)
    cursor.execute("EXEC dbo.SaveAiResults @mrn = ?, @category = ?, @ai_result = ?", (mrn, name, formated_ai_results))
    print("SUCCESS EXECUTION")
    conn.commit()
    cursor.close()



def getChemblID(cheMBLID):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("EXEC dbo.GetPreferredName @prefered_term= ?", (cheMBLID,))
    rows = cursor.fetchall()
    prefName = ""
    for row in rows:
        prefName = getattr(row, "chembl_id")
    
    cursor.close()
    conn.close()
    return prefName






def getPromptFromCriteria(description):
    for dict in CRITERIA_CONFIG:
        if dict["desc"] == description:
            return dict["prompt"]


def getQueryFromCriteria(description):
    for dict in CRITERIA_CONFIG:
        if dict["desc"] == description:
            return dict["sql_query"]


def definingInputParameters(description):
    for dict in CRITERIA_CONFIG:
        if dict["desc"] == description:
            return dict["input"]


def StringConvertion(sql_query):
    newWord = "EXEC dbo." + sql_query
    print(newWord)
    return newWord


def getCriteriaConfig(description):
    for dict in CRITERIA_CONFIG:
        if dict["desc"] == description:
            return dict
    return None





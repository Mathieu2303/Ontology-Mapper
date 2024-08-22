import os

ENVIRONMENT = "local machine"

if "ENVIRONMENT" in os.environ:
    ENVIRONMENT = os.environ["ENVIRONMENT"]


AZURE_OPENAI_API_KEY = None

if "AZURE_OPENAI_API_KEY" in os.environ:
    AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]

AZURE_OPENAI_ENDPOINT = None

if "AZURE_OPENAI_ENDPOINT" in os.environ:
    AZURE_OPENAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]


SERVER = None

if "SERVER" in os.environ:
    SERVER = os.environ["SERVER"]


DATABASE = None

if "DATABASE" in os.environ:
    DATABASE = os.environ["DATABASE"]

USERNAME = None

if "USERNAME" in os.environ:
    USERNAME = os.environ["USERNAME"]


PASSWORD = None

if "PASSWORD" in os.environ:
    PASSWORD = os.environ["PASSWORD"]


CRITERIA_CONFIG = [
    {
        "desc": "Histology",
        "prompt": 'You are an AI assistant who provides the ICDO3 site codes for the input The output should only be in JSON format like [{\"Primary_Site_ICDO3:\": \"C16.2\", \"Histology_ICDO3:\": \"81453\"}]."',
        "sql_query": """GetTumorDetailsByMRN""",
        "input" : ["mrn"],
        "criteria": [
            "Histology_Text",
            "Behavior_Description",
            "Laterality_Description",
            "Primary_Site_Text",
        ],
        "result": [
            "Primary_Site_ICDO3",
            "Histology_ICDO3"
        ]
    },
    {
        "desc": "Medication",
        "prompt": "You are an AI assistant who provides the ChEMBL id and the preferred medication name for the input The output should only be in JSON format like [{\"ChEMBLID:\": \"CHEMBL1200338\",\"Preferred Medication Name:\": \"PINACIDIL\" }].",
        "sql_query": """GetMedicationDetails""",
        "input": ["mrn", "date"],
        "criteria": [
            "order_description"
        ],
        "result": [
            "ChEMBLID"
        ]
    },
    {
        "desc": "Surgery",
        "prompt": "You are an AI assistant who provides the ICD10 code and CPT code for the given input. The output should only be in a JSON format like [{\"procedure\": \"Umbilical Hernia Repair\", \"ICD10_code\": \"K42.9\", \"CPT_code\": \"49587\"}, {\"procedure\": \"Hysterectomy, Abdominal Total (TAH)\", \"ICD10_code\": \"Q51.5\", \"CPT_code\": \"58150\"}]",
        "sql_query": """GetSurgeryDetails""",
        "input": ["mrn"],
        "criteria": ["procedure"],
        "result": [
            
        ]
    }
]

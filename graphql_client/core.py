import requests
from config import GRAPHQL_URL

def execute_query(query: str, variables: dict = None) -> dict:
    payload = {"query": query, "variables": variables}
    response = requests.post(GRAPHQL_URL, json=payload)
    return response.json()

def execute_mutation(mutation: str, variables: dict = None) -> dict:
    payload = {"query": mutation, "variables": variables}
    response = requests.post(GRAPHQL_URL, json=payload)
    return response.json()
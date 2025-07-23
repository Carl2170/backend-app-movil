from flask import Blueprint, request, jsonify
from graphql_client.core import execute_query, execute_mutation
from graphql_client.queries import (
    ACCOUNTING_ACCOUNTS_QUERY,
    ACCOUNTING_ACCOUNT_BY_ID_QUERY,
    ACCOUNTING_ACCOUNTS_BY_CHART_QUERY,
    ACCOUNTING_ACCOUNTS_BY_PARENT_QUERY
)
from graphql_client.mutations import (
    CREATE_ACCOUNTING_ACCOUNT_MUTATION,
    UPDATE_ACCOUNTING_ACCOUNT_MUTATION,
    DELETE_ACCOUNTING_ACCOUNT_MUTATION
)

bp = Blueprint('accounting_accounts', __name__, url_prefix='/accounting-accounts')

# GET /accounting-accounts/
@bp.route('/', methods=['GET'])
def listar_todas():
    result = execute_query(ACCOUNTING_ACCOUNTS_QUERY)
    return jsonify(result)

# GET /accounting-accounts/<id>
@bp.route('/<id>', methods=['GET'])
def obtener_por_id(id):
    variables = {"id": id}
    result = execute_query(ACCOUNTING_ACCOUNT_BY_ID_QUERY, variables)
    return jsonify(result)

# GET /accounting-accounts/chart/<chart_id>
@bp.route('/chart/<chart_id>', methods=['GET'])
def obtener_por_chart(chart_id):
    variables = {"chartOfAccountId": chart_id}
    result = execute_query(ACCOUNTING_ACCOUNTS_BY_CHART_QUERY, variables)
    return jsonify(result)

# GET /accounting-accounts/parent/<parent_id>
@bp.route('/parent/<parent_id>', methods=['GET'])
def obtener_por_padre(parent_id):
    variables = {"parentId": parent_id}
    result = execute_query(ACCOUNTING_ACCOUNTS_BY_PARENT_QUERY, variables)
    return jsonify(result)

# POST /accounting-accounts/
@bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    variables = {
        "input": {
            "accountNatureId": data["accountNatureId"],
            "chartOfAccountId": data["chartOfAccountId"],
            "parentAccountId": data.get("parentAccountId"),
            "code": data["code"],
            "name": data["name"],
            "description": data.get("description"),
            "level": data["level"],
            "isActive": data.get("isActive", True),
            "isTransactional": data.get("isTransactional", True)
        }
    }
    result = execute_mutation(CREATE_ACCOUNTING_ACCOUNT_MUTATION, variables)
    return jsonify(result)

# PUT /accounting-accounts/<id>
@bp.route('/<id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    variables = {
        "id": id,
        "input": {
            "accountNatureId": data["accountNatureId"],
            "chartOfAccountId": data["chartOfAccountId"],
            "parentAccountId": data.get("parentAccountId"),
            "code": data["code"],
            "name": data["name"],
            "description": data.get("description"),
            "level": data["level"],
            "isActive": data.get("isActive", True),
            "isTransactional": data.get("isTransactional", True)
        }
    }
    result = execute_mutation(UPDATE_ACCOUNTING_ACCOUNT_MUTATION, variables)
    return jsonify(result)

# DELETE /accounting-accounts/<id>
@bp.route('/<id>', methods=['DELETE'])
def eliminar(id):
    variables = {"id": id}
    result = execute_mutation(DELETE_ACCOUNTING_ACCOUNT_MUTATION, variables)
    return jsonify(result)
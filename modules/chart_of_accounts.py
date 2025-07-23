from flask import Blueprint, request, jsonify
from graphql_client.core import execute_query, execute_mutation
from graphql_client.queries import (
    CHART_OF_ACCOUNTS_QUERY,
    CHART_OF_ACCOUNT_BY_ID_QUERY,
    DEFAULT_CHART_OF_ACCOUNT_QUERY
)
from graphql_client.mutations import (
    CREATE_CHART_OF_ACCOUNT_MUTATION,
    UPDATE_CHART_OF_ACCOUNT_MUTATION,
    DELETE_CHART_OF_ACCOUNT_MUTATION
)

bp = Blueprint('chart_of_accounts', __name__, url_prefix='/chart-of-accounts')

# GET /chart-of-accounts/
@bp.route('/', methods=['GET'])
def listar_todas():
    result = execute_query(CHART_OF_ACCOUNTS_QUERY)
    return jsonify(result)

# GET /chart-of-accounts/default
@bp.route('/default', methods=['GET'])
def obtener_por_defecto():
    result = execute_query(DEFAULT_CHART_OF_ACCOUNT_QUERY)
    return jsonify(result)

# GET /chart-of-accounts/<id>
@bp.route('/<id>', methods=['GET'])
def obtener_por_id(id):
    variables = {"id": id}
    result = execute_query(CHART_OF_ACCOUNT_BY_ID_QUERY, variables)
    return jsonify(result)

# POST /chart-of-accounts/
@bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    variables = {
        "input": {
            "name": data["name"],
            "description": data.get("description"),
            "isDefault": data.get("isDefault", False)
        }
    }
    result = execute_mutation(CREATE_CHART_OF_ACCOUNT_MUTATION, variables)
    return jsonify(result)

# PUT /chart-of-accounts/<id>
@bp.route('/<id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    variables = {
        "id": id,
        "input": {
            "name": data["name"],
            "description": data.get("description"),
            "isDefault": data.get("isDefault", False)
        }
    }
    result = execute_mutation(UPDATE_CHART_OF_ACCOUNT_MUTATION, variables)
    return jsonify(result)

# DELETE /chart-of-accounts/<id>
@bp.route('/<id>', methods=['DELETE'])
def eliminar(id):
    variables = {"id": id}
    result = execute_mutation(DELETE_CHART_OF_ACCOUNT_MUTATION, variables)
    return jsonify(result)
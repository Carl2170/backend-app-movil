from flask import Blueprint, request, jsonify
from graphql_client.core import execute_query, execute_mutation
from graphql_client.queries import (
    ACCOUNT_NATURES_QUERY,
    ACCOUNT_NATURE_QUERY_BY_ID
)
from graphql_client.mutations import (
    CREATE_ACCOUNT_NATURE_MUTATION,
    UPDATE_ACCOUNT_NATURE_MUTATION,
    DELETE_ACCOUNT_NATURE_MUTATION
)

bp = Blueprint('account_nature', __name__, url_prefix='/account-natures')

# GET /account-natures
@bp.route('/', methods=['GET'])
def listar_todas():
    result = execute_query(ACCOUNT_NATURES_QUERY)
    return jsonify(result)

# GET /account-natures/<id>
@bp.route('/<id>', methods=['GET'])
def obtener_por_id(id):
    variables = {"id": id}
    result = execute_query(ACCOUNT_NATURE_QUERY_BY_ID, variables)
    return jsonify(result)

# POST /account-natures
@bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    variables = {
        "input": {
            "name": data["name"],
            "defaultBalanceType": data["defaultBalanceType"]
        }
    }
    result = execute_mutation(CREATE_ACCOUNT_NATURE_MUTATION, variables)
    return jsonify(result)

# PUT /account-natures/<id>
@bp.route('/<id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    variables = {
        "id": id,
        "input": {
            "name": data["name"],
            "defaultBalanceType": data["defaultBalanceType"]
        }
    }
    result = execute_mutation(UPDATE_ACCOUNT_NATURE_MUTATION, variables)
    return jsonify(result)

# DELETE /account-natures/<id>
@bp.route('/<id>', methods=['DELETE'])
def eliminar(id):
    variables = {"id": id}
    result = execute_mutation(DELETE_ACCOUNT_NATURE_MUTATION, variables)
    return jsonify(result)
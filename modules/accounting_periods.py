from flask import Blueprint, request, jsonify
from graphql_client.core import execute_query, execute_mutation
from graphql_client.queries import (
    ACCOUNTING_PERIODS_QUERY,
    ACCOUNTING_PERIOD_BY_ID_QUERY,
    ACCOUNTING_PERIODS_BY_STATUS_QUERY
)
from graphql_client.mutations import (
    CREATE_ACCOUNTING_PERIOD_MUTATION,
    UPDATE_ACCOUNTING_PERIOD_MUTATION,
    DELETE_ACCOUNTING_PERIOD_MUTATION
)

bp = Blueprint('accounting_periods', __name__, url_prefix='/accounting-periods')

# GET /accounting-periods/
@bp.route('/', methods=['GET'])
def listar_todos():
    result = execute_query(ACCOUNTING_PERIODS_QUERY)
    return jsonify(result)

# GET /accounting-periods/<id>
@bp.route('/<id>', methods=['GET'])
def obtener_por_id(id):
    variables = {"id": id}
    result = execute_query(ACCOUNTING_PERIOD_BY_ID_QUERY, variables)
    return jsonify(result)

# GET /accounting-periods/status/<status>
@bp.route('/status/<status>', methods=['GET'])
def obtener_por_estado(status):
    variables = {"status": status}
    result = execute_query(ACCOUNTING_PERIODS_BY_STATUS_QUERY, variables)
    return jsonify(result)

# POST /accounting-periods/
@bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    variables = {
        "input": {
            "name": data["name"],
            "startDate": data["startDate"],
            "endDate": data["endDate"],
            "status": data["status"]
        }
    }
    result = execute_mutation(CREATE_ACCOUNTING_PERIOD_MUTATION, variables)
    return jsonify(result)

# PUT /accounting-periods/<id>
@bp.route('/<id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    variables = {
        "id": id,
        "input": {
            "name": data["name"],
            "startDate": data["startDate"],
            "endDate": data["endDate"],
            "status": data["status"]
        }
    }
    result = execute_mutation(UPDATE_ACCOUNTING_PERIOD_MUTATION, variables)
    return jsonify(result)

# DELETE /accounting-periods/<id>
@bp.route('/<id>', methods=['DELETE'])
def eliminar(id):
    variables = {"id": id}
    result = execute_mutation(DELETE_ACCOUNTING_PERIOD_MUTATION, variables)
    return jsonify(result)
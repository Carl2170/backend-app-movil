from flask import Blueprint, request, jsonify
from graphql_client.core import execute_query, execute_mutation
from graphql_client.queries import (
    JOURNAL_ENTRY_DETAILS_QUERY,
    JOURNAL_ENTRY_DETAIL_BY_ID_QUERY,
    JOURNAL_ENTRY_DETAILS_BY_ENTRY_QUERY,
    JOURNAL_ENTRY_DETAILS_BY_ACCOUNT_QUERY,
    ACCOUNT_BALANCE_QUERY
)
from graphql_client.mutations import (
    CREATE_JOURNAL_ENTRY_DETAIL_MUTATION,
    UPDATE_JOURNAL_ENTRY_DETAIL_MUTATION,
    DELETE_JOURNAL_ENTRY_DETAIL_MUTATION
)

bp = Blueprint('journal_details', __name__, url_prefix='/journal-details')

# GET /journal-details/
@bp.route('/', methods=['GET'])
def listar_todos():
    result = execute_query(JOURNAL_ENTRY_DETAILS_QUERY)
    return jsonify(result)

# GET /journal-details/<id>
@bp.route('/<id>', methods=['GET'])
def obtener_por_id(id):
    variables = {"id": id}
    result = execute_query(JOURNAL_ENTRY_DETAIL_BY_ID_QUERY, variables)
    return jsonify(result)

# GET /journal-details/entry/<entry_id>
@bp.route('/entry/<entry_id>', methods=['GET'])
def obtener_por_asiento(entry_id):
    variables = {"journalEntryId": entry_id}
    result = execute_query(JOURNAL_ENTRY_DETAILS_BY_ENTRY_QUERY, variables)
    return jsonify(result)

# GET /journal-details/account/<account_id>
@bp.route('/account/<account_id>', methods=['GET'])
def obtener_por_cuenta(account_id):
    variables = {"accountId": account_id}
    result = execute_query(JOURNAL_ENTRY_DETAILS_BY_ACCOUNT_QUERY, variables)
    return jsonify(result)

# GET /journal-details/account/<account_id>/balance
@bp.route('/account/<account_id>/balance', methods=['GET'])
def consultar_balance(account_id):
    variables = {"accountId": account_id}
    result = execute_query(ACCOUNT_BALANCE_QUERY, variables)
    return jsonify(result)

# POST /journal-details/
@bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    variables = {"input": data}
    result = execute_mutation(CREATE_JOURNAL_ENTRY_DETAIL_MUTATION, variables)
    return jsonify(result)

# PUT /journal-details/<id>
@bp.route('/<id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    variables = {"id": id, "input": data}
    result = execute_mutation(UPDATE_JOURNAL_ENTRY_DETAIL_MUTATION, variables)
    return jsonify(result)

# DELETE /journal-details/<id>
@bp.route('/<id>', methods=['DELETE'])
def eliminar(id):
    variables = {"id": id}
    result = execute_mutation(DELETE_JOURNAL_ENTRY_DETAIL_MUTATION, variables)
    return jsonify(result)
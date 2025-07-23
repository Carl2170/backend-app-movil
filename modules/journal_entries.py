from flask import Blueprint, request, jsonify
from graphql_client.core import execute_query, execute_mutation
from graphql_client.queries import (
    JOURNAL_ENTRIES_QUERY,
    JOURNAL_ENTRY_BY_ID_QUERY,
    JOURNAL_ENTRIES_BY_PERIOD_QUERY,
    JOURNAL_ENTRIES_BY_STATUS_QUERY,
    JOURNAL_ENTRIES_BY_DATE_RANGE_QUERY
)
from graphql_client.mutations import (
    CREATE_JOURNAL_ENTRY_MUTATION,
    UPDATE_JOURNAL_ENTRY_MUTATION,
    POST_JOURNAL_ENTRY_MUTATION,
    DELETE_JOURNAL_ENTRY_MUTATION
)

bp = Blueprint('journal_entries', __name__, url_prefix='/journal-entries')

# GET /journal-entries/
@bp.route('/', methods=['GET'])
def listar_todos():
    result = execute_query(JOURNAL_ENTRIES_QUERY)
    return jsonify(result)

# GET /journal-entries/<id>
@bp.route('/<id>', methods=['GET'])
def obtener_por_id(id):
    variables = {"id": id}
    result = execute_query(JOURNAL_ENTRY_BY_ID_QUERY, variables)
    return jsonify(result)

# GET /journal-entries/period/<period_id>
@bp.route('/period/<period_id>', methods=['GET'])
def obtener_por_periodo(period_id):
    variables = {"periodId": period_id}
    result = execute_query(JOURNAL_ENTRIES_BY_PERIOD_QUERY, variables)
    return jsonify(result)

# GET /journal-entries/status/<status>
@bp.route('/status/<status>', methods=['GET'])
def obtener_por_estado(status):
    variables = {"status": status}
    result = execute_query(JOURNAL_ENTRIES_BY_STATUS_QUERY, variables)
    return jsonify(result)

# GET /journal-entries/range?start=YYYY-MM-DD&end=YYYY-MM-DD
@bp.route('/range', methods=['GET'])
def obtener_por_rango():
    start = request.args.get("start")
    end = request.args.get("end")
    variables = {"startDate": start, "endDate": end}
    result = execute_query(JOURNAL_ENTRIES_BY_DATE_RANGE_QUERY, variables)
    return jsonify(result)

# POST /journal-entries/
@bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    variables = {"input": data}
    result = execute_mutation(CREATE_JOURNAL_ENTRY_MUTATION, variables)
    return jsonify(result)

# PUT /journal-entries/<id>
@bp.route('/<id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    variables = {"id": id, "input": data}
    result = execute_mutation(UPDATE_JOURNAL_ENTRY_MUTATION, variables)
    return jsonify(result)

# POST /journal-entries/<id>/post
@bp.route('/<id>/post', methods=['POST'])
def publicar(id):
    variables = {"id": id}
    result = execute_mutation(POST_JOURNAL_ENTRY_MUTATION, variables)
    return jsonify(result)

# DELETE /journal-entries/<id>
@bp.route('/<id>', methods=['DELETE'])
def eliminar(id):
    variables = {"id": id}
    result = execute_mutation(DELETE_JOURNAL_ENTRY_MUTATION, variables)
    return jsonify(result)
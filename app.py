
from flask import Flask
from modules import (
    account_nature,
    chart_of_accounts,
    accounting_periods,
    accounting_accounts,
    journal_entries,
    journal_details
)

app = Flask(__name__)
app.register_blueprint(account_nature.bp)
app.register_blueprint(chart_of_accounts.bp)
app.register_blueprint(accounting_periods.bp)
app.register_blueprint(accounting_accounts.bp)
app.register_blueprint(journal_entries.bp)
app.register_blueprint(journal_details.bp)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
# ─── Account Nature Mutations ───────────────────────

CREATE_ACCOUNT_NATURE_MUTATION = """
mutation($input: AccountNatureInput!) {
  createAccountNature(input: $input) {
    id
    name
    defaultBalanceType
  }
}
"""

UPDATE_ACCOUNT_NATURE_MUTATION = """
mutation($id: ID!, $input: AccountNatureInput!) {
  updateAccountNature(id: $id, input: $input) {
    id
    name
    defaultBalanceType
  }
}
"""

DELETE_ACCOUNT_NATURE_MUTATION = """
mutation($id: ID!) {
  deleteAccountNature(id: $id)
}
"""



# ─── Chart of Account Mutations ─────────────────────

CREATE_CHART_OF_ACCOUNT_MUTATION = """
mutation($input: ChartOfAccountInput!) {
  createChartOfAccount(input: $input) {
    id
    name
    description
    isDefault
  }
}
"""

UPDATE_CHART_OF_ACCOUNT_MUTATION = """
mutation($id: ID!, $input: ChartOfAccountInput!) {
  updateChartOfAccount(id: $id, input: $input) {
    id
    name
    description
    isDefault
  }
}
"""

DELETE_CHART_OF_ACCOUNT_MUTATION = """
mutation($id: ID!) {
  deleteChartOfAccount(id: $id)
}
"""

# ─── Accounting Period Mutations ────────────────────

CREATE_ACCOUNTING_PERIOD_MUTATION = """
mutation($input: AccountingPeriodInput!) {
  createAccountingPeriod(input: $input) {
    id
    name
    startDate
    endDate
    status
  }
}
"""

UPDATE_ACCOUNTING_PERIOD_MUTATION = """
mutation($id: ID!, $input: AccountingPeriodInput!) {
  updateAccountingPeriod(id: $id, input: $input) {
    id
    name
    startDate
    endDate
    status
  }
}
"""

DELETE_ACCOUNTING_PERIOD_MUTATION = """
mutation($id: ID!) {
  deleteAccountingPeriod(id: $id)
}
"""

# ─── Accounting Account Mutations ───────────────────

CREATE_ACCOUNTING_ACCOUNT_MUTATION = """
mutation($input: AccountingAccountInput!) {
  createAccountingAccount(input: $input) {
    id
    name
    code
    level
    isActive
    isTransactional
  }
}
"""

UPDATE_ACCOUNTING_ACCOUNT_MUTATION = """
mutation($id: ID!, $input: AccountingAccountInput!) {
  updateAccountingAccount(id: $id, input: $input) {
    id
    name
    code
    level
    isActive
    isTransactional
  }
}
"""

DELETE_ACCOUNTING_ACCOUNT_MUTATION = """
mutation($id: ID!) {
  deleteAccountingAccount(id: $id)
}
"""

# ─── Journal Entry Mutations ───────────────────────

CREATE_JOURNAL_ENTRY_MUTATION = """
mutation($input: JournalEntryInput!) {
  createJournalEntry(input: $input) {
    id
    entryDate
    description
    status
    totalDebits
    totalCredits
    isBalanced
  }
}
"""

UPDATE_JOURNAL_ENTRY_MUTATION = """
mutation($id: ID!, $input: JournalEntryInput!) {
  updateJournalEntry(id: $id, input: $input) {
    id
    entryDate
    description
    status
    totalDebits
    totalCredits
    isBalanced
  }
}
"""

POST_JOURNAL_ENTRY_MUTATION = """
mutation($id: ID!) {
  postJournalEntry(id: $id) {
    id
    status
    postedAt
  }
}
"""

DELETE_JOURNAL_ENTRY_MUTATION = """
mutation($id: ID!) {
  deleteJournalEntry(id: $id)
}
""" 

# ─── Journal Entry Detail Mutations ─────────────────

CREATE_JOURNAL_ENTRY_DETAIL_MUTATION = """
mutation($input: JournalEntryDetailInput!) {
  createJournalEntryDetail(input: $input) {
    id
    description
    debitAmount
    creditAmount
  }
}
"""

UPDATE_JOURNAL_ENTRY_DETAIL_MUTATION = """
mutation($id: ID!, $input: JournalEntryDetailInput!) {
  updateJournalEntryDetail(id: $id, input: $input) {
    id
    description
    debitAmount
    creditAmount
  }
}
"""

DELETE_JOURNAL_ENTRY_DETAIL_MUTATION = """
mutation($id: ID!) {
  deleteJournalEntryDetail(id: $id)
}
"""
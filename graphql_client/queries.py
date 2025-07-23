# ─── Account Nature Queries ─────────────────────────

ACCOUNT_NATURES_QUERY = """
query {
  accountNatures {
    id
    name
    defaultBalanceType
  }
}
"""

ACCOUNT_NATURE_QUERY_BY_ID = """
query($id: ID!) {
  accountNature(id: $id) {
    id
    name
    defaultBalanceType
  }
}
"""


# ─── Chart of Account Queries ───────────────────────

CHART_OF_ACCOUNTS_QUERY = """
query {
  chartOfAccounts {
    id
    name
    description
    isDefault
    createdAt
    updatedAt
  }
}
"""

CHART_OF_ACCOUNT_BY_ID_QUERY = """
query($id: ID!) {
  chartOfAccount(id: $id) {
    id
    name
    description
    isDefault
    createdAt
    updatedAt
  }
}
"""

DEFAULT_CHART_OF_ACCOUNT_QUERY = """
query {
  defaultChartOfAccount {
    id
    name
    description
    isDefault
    createdAt
    updatedAt
  }
}
"""
# ─── Accounting Period Queries ──────────────────────

ACCOUNTING_PERIODS_QUERY = """
query {
  accountingPeriods {
    id
    name
    startDate
    endDate
    status
    createdAt
    updatedAt
  }
}
"""

ACCOUNTING_PERIOD_BY_ID_QUERY = """
query($id: ID!) {
  accountingPeriod(id: $id) {
    id
    name
    startDate
    endDate
    status
    createdAt
    updatedAt
  }
}
"""

ACCOUNTING_PERIODS_BY_STATUS_QUERY = """
query($status: String!) {
  accountingPeriodsByStatus(status: $status) {
    id
    name
    startDate
    endDate
    status
    createdAt
    updatedAt
  }
}
"""

# ─── Accounting Account Queries ─────────────────────

ACCOUNTING_ACCOUNTS_QUERY = """
query {
  accountingAccounts {
    id
    name
    code
    level
    isActive
    isTransactional
    accountNature {
      id
      name
      defaultBalanceType
    }
    chartOfAccount {
      id
      name
    }
    parentAccount {
      id
      name
    }
    childAccounts {
      id
      name
    }
  }
}
"""

ACCOUNTING_ACCOUNT_BY_ID_QUERY = """
query($id: ID!) {
  accountingAccount(id: $id) {
    id
    name
    code
    level
    isActive
    isTransactional
    accountNature {
      id
      name
    }
    chartOfAccount {
      id
      name
    }
    parentAccount {
      id
      name
    }
    childAccounts {
      id
      name
    }
  }
}
"""

ACCOUNTING_ACCOUNTS_BY_CHART_QUERY = """
query($chartOfAccountId: ID!) {
  accountingAccountsByChartOfAccount(chartOfAccountId: $chartOfAccountId) {
    id
    name
    code
  }
}
"""

ACCOUNTING_ACCOUNTS_BY_PARENT_QUERY = """
query($parentId: ID!) {
  accountingAccountsByParent(parentId: $parentId) {
    id
    name
    code
  }
}
"""

# ─── Journal Entry Queries ──────────────────────────

JOURNAL_ENTRIES_QUERY = """
query {
  journalEntries {
    id
    entryDate
    description
    status
    totalDebits
    totalCredits
    isBalanced
    accountingPeriod {
      id
      name
    }
    details {
      id
      debitAmount
      creditAmount
    }
  }
}
"""

JOURNAL_ENTRY_BY_ID_QUERY = """
query($id: ID!) {
  journalEntry(id: $id) {
    id
    entryDate
    description
    status
    totalDebits
    totalCredits
    isBalanced
    accountingPeriod {
      id
      name
    }
    details {
      id
      debitAmount
      creditAmount
    }
  }
}
"""

JOURNAL_ENTRIES_BY_PERIOD_QUERY = """
query($periodId: ID!) {
  journalEntriesByPeriod(periodId: $periodId) {
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

JOURNAL_ENTRIES_BY_STATUS_QUERY = """
query($status: JournalEntryStatus!) {
  journalEntriesByStatus(status: $status) {
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

JOURNAL_ENTRIES_BY_DATE_RANGE_QUERY = """
query($startDate: String!, $endDate: String!) {
  journalEntriesByDateRange(startDate: $startDate, endDate: $endDate) {
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

# ─── Journal Entry Detail Queries ───────────────────

JOURNAL_ENTRY_DETAILS_QUERY = """
query {
  journalEntryDetails {
    id
    description
    debitAmount
    creditAmount
    journalEntry {
      id
      description
    }
    account {
      id
      name
      code
    }
    createdAt
  }
}
"""

JOURNAL_ENTRY_DETAIL_BY_ID_QUERY = """
query($id: ID!) {
  journalEntryDetail(id: $id) {
    id
    description
    debitAmount
    creditAmount
    journalEntry {
      id
    }
    account {
      id
      name
    }
    createdAt
  }
}
"""

JOURNAL_ENTRY_DETAILS_BY_ENTRY_QUERY = """
query($journalEntryId: ID!) {
  journalEntryDetailsByEntry(journalEntryId: $journalEntryId) {
    id
    description
    debitAmount
    creditAmount
  }
}
"""

JOURNAL_ENTRY_DETAILS_BY_ACCOUNT_QUERY = """
query($accountId: ID!) {
  journalEntryDetailsByAccount(accountId: $accountId) {
    id
    description
    debitAmount
    creditAmount
  }
}
"""

ACCOUNT_BALANCE_QUERY = """
query($accountId: ID!) {
  accountBalance(accountId: $accountId) {
    accountId
    totalDebits
    totalCredits
    balance
  }
}
"""
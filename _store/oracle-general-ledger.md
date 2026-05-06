---
aid: oracle-general-ledger
name: Oracle General Ledger
description: Oracle Fusion Cloud General Ledger provides REST APIs for managing core financial accounting operations within Oracle Cloud ERP. These APIs enable programmatic access to journal entries, ledger balances, accounting periods, currency rates, intercompany transactions, budgetary controls, and chart of accounts configurations used by finance teams for enterprise accounting, reporting, and close processes.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-general-ledger/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-03-16'
specificationVersion: '0.19'
tags:
  - Accounting
  - Balances
  - Cloud
  - ERP
  - Finance
  - General Ledger
  - Journals
apis:
  - name: Oracle General Ledger Journal Batches REST API
    description: REST API for managing journal batches in Oracle Fusion Cloud General Ledger. The journal batches resource allows viewing journal batches, updating batch completion status and reversal attributes, and deleting journal batches. Child resources provide access to journal headers, journal lines, attachments, action logs, descriptive flexfields, and error details.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Accounting
      - General Ledger
      - Journal Batches
      - Journals
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/25b/farfa/api-journal-batches.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle General Ledger Ledger Balances REST API
    description: REST API for querying account balances in Oracle Fusion Cloud General Ledger. The ledger balances resource allows viewing balance amounts for any account combination or accounts defined as part of an account group. Supports finders for account balance by combination, account group balance, and primary key lookup across ledgers, currencies, and accounting periods.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Account Balances
      - Balances
      - Financial Reporting
      - General Ledger
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/api-ledger-balances.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle General Ledger Accounting Period Status REST API
    description: REST API for viewing accounting period statuses in Oracle Fusion Cloud General Ledger. The accounting period status list of values resource provides period details in a calendar, including ledger identification, period name, and closing status values such as Open, Closed, Future Enterable, Never Opened, Permanently Closed, and Close Pending.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Accounting Periods
      - Financial Close
      - General Ledger
      - Period Close
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/op-accountingperiodstatuslov-get.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle General Ledger Currency Rates REST API
    description: REST API for retrieving currency exchange rate information in Oracle Fusion Cloud General Ledger. The currency rates resource provides information on currency rates for source and target currency combinations, supporting daily rates, corporate rates, and user-defined rate types used in multi-currency accounting and foreign currency translation.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Currency Rates
      - Exchange Rates
      - Foreign Currency
      - General Ledger
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle General Ledger Ledger Options REST API
    description: REST API for accessing ledger configuration options in Oracle Fusion Cloud General Ledger. The ledger options resource provides access to ledger setup details including chart of accounts identifiers, balancing segment names, accounted period types, budgetary control settings, and document numbering configurations used to define how a ledger processes accounting data.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Chart of Accounts
      - General Ledger
      - Ledger Options
      - Ledger Setup
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/24c/farfa/op-fedledgeroptions-get.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle General Ledger Budgetary Control REST API
    description: REST API for managing budgetary controls in Oracle Fusion Cloud General Ledger. The budgetary control resources enable viewing budget execution controls, budget impact results, and control budget periods. These APIs support organizations that use budget accounts to control expenditures against defined appropriation limits and enterprise performance management budget transactions.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Appropriations
      - Budgetary Control
      - Budgets
      - General Ledger
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/25d/farfa/op-fedbudgetexecutioncontrols-get.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle General Ledger Chart of Accounts Filters REST API
    description: REST API for managing chart of accounts filter configurations in Oracle Fusion Cloud General Ledger. The chart of accounts filters resource returns filter ID values for chart of accounts filter criteria, enabling control over which account combinations are available for journal entry and financial reporting based on defined filter rules and criteria.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Account Combinations
      - Account Filters
      - Chart of Accounts
      - General Ledger
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Intercompany Transactions REST API
    description: REST API for managing intercompany transactions in Oracle Fusion Cloud Financials. The intercompany resources support agreement-based intercompany transactions, intercompany transaction source documents, intercompany agreements with transfer authorization groups, and intercompany organization lookups. These APIs enable automated cross-charge processing and intercompany balancing within the general ledger.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Cross-Charge
      - General Ledger
      - Intercompany
      - Transfer Pricing
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/25c/farfa/automated-intercompany-cross-charge-of-payables-invoices-using-rest-apis.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Joint Venture General Ledger Transactions REST API
    description: REST API for managing joint venture general ledger transactions in Oracle Fusion Cloud Financials. The joint venture GL transactions and joint venture subledger transactions resources enable viewing and updating transactions related to joint venture accounting, supporting partnership accounting workflows that integrate with the general ledger.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - General Ledger
      - Joint Venture
      - Partnership Accounting
      - Subledger Accounting
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/24c/farfa/op-jointventuregltransactions-get.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle General Ledger ERP Integrations REST API
    description: REST API for automating bulk data import and export flows with Oracle Fusion Cloud General Ledger. The ERP integrations resource supports loading journal data files, submitting Enterprise Scheduler Service jobs for journal import, and running the accounting engine for subledger journal processing. Also provides access to ERP business events and ERP process status details.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Data Import
      - ERP Integration
      - General Ledger
      - Journal Import
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/25b/farfa/op-erpintegrations-operationname-get.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
      - type: Change Log
        url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
common:
  - type: Portal
    url: https://docs.oracle.com/en/cloud/saas/financials/26a/api.html
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
  - type: Change Log
    url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
  - type: Support
    url: https://support.oracle.com
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: TermsOfService
    url: https://www.oracle.com/corporate/contracts/cloud-services/
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: Website
    url: https://www.oracle.com/erp/general-ledger/
  - type: Sign Up
    url: https://www.oracle.com/cloud/free/
  - type: Login
    url: https://cloud.oracle.com/
  - type: Blog
    url: https://blogs.oracle.com/cloud-infrastructure/
  - type: GitHubOrganization
    url: https://github.com/oracle
  - type: Community
    url: https://community.oracle.com/customerconnect/
  - type: Implementation Guide
    url: https://docs.oracle.com/en/cloud/saas/financials/26a/faigl/index.html
  - type: User Guide
    url: https://docs.oracle.com/en/cloud/saas/financials/26a/faugl/index.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

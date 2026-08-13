---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Oracle General Ledger Agentic Access
  operation_count: 12
  slug: oracle-general-ledger-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 18
apis:
- description: 'REST API for managing journal batches in Oracle Fusion Cloud General Ledger. The journal batches resource allows viewing journal batches, updating batch completion status and reversal attributes, and '
  name: Oracle General Ledger Journal Batches REST API
  slug: oracle-general-ledger-journal-batches-rest-api
- description: 'REST API for querying account balances in Oracle Fusion Cloud General Ledger. The ledger balances resource allows viewing balance amounts for any account combination or accounts defined as part of an '
  name: Oracle General Ledger Ledger Balances REST API
  slug: oracle-general-ledger-ledger-balances-rest-api
- description: REST API for viewing accounting period statuses in Oracle Fusion Cloud General Ledger. The accounting period status list of values resource provides period details in a calendar, including ledger iden
  name: Oracle General Ledger Accounting Period Status REST API
  slug: oracle-general-ledger-accounting-period-status-rest-api
- description: REST API for retrieving currency exchange rate information in Oracle Fusion Cloud General Ledger. The currency rates resource provides information on currency rates for source and target currency comb
  name: Oracle General Ledger Currency Rates REST API
  slug: oracle-general-ledger-currency-rates-rest-api
- description: 'REST API for accessing ledger configuration options in Oracle Fusion Cloud General Ledger. The ledger options resource provides access to ledger setup details including chart of accounts identifiers, '
  name: Oracle General Ledger Ledger Options REST API
  slug: oracle-general-ledger-ledger-options-rest-api
- description: REST API for managing budgetary controls in Oracle Fusion Cloud General Ledger. The budgetary control resources enable viewing budget execution controls, budget impact results, and control budget peri
  name: Oracle General Ledger Budgetary Control REST API
  slug: oracle-general-ledger-budgetary-control-rest-api
- description: REST API for managing chart of accounts filter configurations in Oracle Fusion Cloud General Ledger. The chart of accounts filters resource returns filter ID values for chart of accounts filter criter
  name: Oracle General Ledger Chart of Accounts Filters REST API
  slug: oracle-general-ledger-chart-of-accounts-filters-rest-api
- description: REST API for managing intercompany transactions in Oracle Fusion Cloud Financials. The intercompany resources support agreement-based intercompany transactions, intercompany transaction source documen
  name: Oracle Intercompany Transactions REST API
  slug: oracle-intercompany-transactions-rest-api
- description: REST API for managing joint venture general ledger transactions in Oracle Fusion Cloud Financials. The joint venture GL transactions and joint venture subledger transactions resources enable viewing a
  name: Oracle Joint Venture General Ledger Transactions REST API
  slug: oracle-joint-venture-general-ledger-transactions-rest-api
- description: REST API for automating bulk data import and export flows with Oracle Fusion Cloud General Ledger. The ERP integrations resource supports loading journal data files, submitting Enterprise Scheduler Se
  name: Oracle General Ledger ERP Integrations REST API
  slug: oracle-general-ledger-erp-integrations-rest-api
- description: The Accounting Periods API from Oracle General Ledger — 1 operation(s) for accounting periods.
  name: Oracle General Ledger Accounting Periods API
  slug: oracle-general-ledger-accounting-periods-api
- description: The Budgetary Control API from Oracle General Ledger — 1 operation(s) for budgetary control.
  name: Oracle General Ledger Budgetary Control API
  slug: oracle-general-ledger-budgetary-control-api
- description: The Currency Rates API from Oracle General Ledger — 1 operation(s) for currency rates.
  name: Oracle General Ledger Currency Rates API
  slug: oracle-general-ledger-currency-rates-api
- description: The ERP Integrations API from Oracle General Ledger — 1 operation(s) for erp integrations.
  name: Oracle General Ledger ERP Integrations API
  slug: oracle-general-ledger-erp-integrations-api
- description: The Intercompany API from Oracle General Ledger — 1 operation(s) for intercompany.
  name: Oracle General Ledger Intercompany API
  slug: oracle-general-ledger-intercompany-api
- description: The Journal Batches API from Oracle General Ledger — 2 operation(s) for journal batches.
  name: Oracle General Ledger Journal Batches API
  slug: oracle-general-ledger-journal-batches-api
- description: The Ledger Balances API from Oracle General Ledger — 1 operation(s) for ledger balances.
  name: Oracle General Ledger Ledger Balances API
  slug: oracle-general-ledger-ledger-balances-api
- description: The Ledger Options API from Oracle General Ledger — 1 operation(s) for ledger options.
  name: Oracle General Ledger Ledger Options API
  slug: oracle-general-ledger-ledger-options-api
artifact_total: 25
collections:
- collection_type: open
  name: Oracle General Ledger REST API
  slug: open-oracle-general-ledger
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-general-ledger-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-general-ledger-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-general-ledger-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.oracle.com/en/cloud/saas/financials/26a/api.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/Authentication.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/corporate/contracts/cloud-services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/erp/general-ledger/
- group: start
  title: ''
  type: Signup
  url: https://www.oracle.com/cloud/free/
- group: start
  title: ''
  type: Login
  url: https://cloud.oracle.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/cloud-infrastructure/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: operate
  title: ''
  type: Community
  url: https://community.oracle.com/customerconnect/
- group: docs
  title: ''
  type: Implementation Guide
  url: https://docs.oracle.com/en/cloud/saas/financials/26a/faigl/index.html
- group: docs
  title: ''
  type: User Guide
  url: https://docs.oracle.com/en/cloud/saas/financials/26a/faugl/index.html
created: '2024-01-15'
description: Oracle Fusion Cloud General Ledger provides REST APIs for managing core financial accounting operations within Oracle Cloud ERP. These APIs enable programmatic access to journal entries, ledger balances, accounting periods, currency rates, intercompany transactions, budgetary controls, and chart of accounts configurations used by finance teams for enterprise accounting, reporting, and close processes.
finops:
- name: Oracle General Ledger Finops
  service_category: API
  slug: oracle-general-ledger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-general-ledger.png
layout: provider
modified: '2026-03-16'
name: Oracle General Ledger
nav: Providers
network: true
overview: 'Oracle General Ledger publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounting Periods API, Budgetary Control API, Currency Rates API, and 5 more. Tagged areas include Accounting, Balances, Cloud, ERP, and Finance.


  Oracle General Ledger''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, support, signup flow, and 13 more developer resources.'
plans:
- name: Oracle General Ledger Plans Pricing
  plan_count: 3
  slug: oracle-general-ledger-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Oracle General Ledger Rate Limits
  slug: oracle-general-ledger-rate-limits
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.2
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-general-ledger/refs/heads/main/screenshots/oracle-general-ledger-2026-06-20T191133.png
security:
- kind: authentication
  name: Oracle General Ledger Authentication
  slug: oracle-general-ledger-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Oracle General Ledger Domain Security
  slug: oracle-general-ledger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-general-ledger
tags:
- Accounting
- Balances
- Cloud
- ERP
- Finance
- General Ledger
- Journals
website: https://www.oracle.com/erp/general-ledger/
---

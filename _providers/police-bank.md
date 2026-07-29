---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Police Bank Agentic Access
  operation_count: 19
  slug: police-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Police Bank Banking Account Balances API
  slug: police-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Police Bank Banking Account Direct Debits API
  slug: police-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Police Bank Banking Account Scheduled Payments API
  slug: police-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Police Bank Banking Account Transactions API
  slug: police-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Police Bank Banking Accounts API
  slug: police-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Police Bank Banking Payees API
  slug: police-bank-banking-payees-api
- description: Banking Product endpoints
  name: Police Bank Banking Products API
  slug: police-bank-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/police-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/police-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.policebank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.policebank.com.au/open-banking
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.policebank.com.au/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.policebank.com.au/contact-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://product.api.policebank.com.au/
- group: auth
  title: ''
  type: Authentication
  url: authentication/police-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/police-bank-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/police-bank-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/police-bank-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/police-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/police-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/police-bank-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/police-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/police-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/police-bank-llms.txt
created: '2026-07-20'
description: Police Bank is a mutual, member-owned Australian bank (ABN 95 087 650 799, ACN 087 650 799, AFSL / Australian Credit Licence No. 240018) founded to serve the New South Wales police community and their families and now open to the wider public. As an Authorised Deposit-taking Institution it participates in Australia's Consumer Data Right (Open Banking) regime as an active data holder - it publishes an unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards, and lets members share their banking data with ACCC-accredited data recipients. Police Bank states it is in the process of gaining ACCC accreditation to also receive data as an Accredited Data Recipient.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/police-bank.png
layout: provider
mcp_servers:
- description: ''
  name: police-bank-mcp.yml
  slug: police-bank-mcpyml
modified: '2026-07-21T12:00:00Z'
name: Police Bank
nav: Providers
network: true
overview: 'Police Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Police Bank''s developer surface includes documentation, support, authentication, and 15 more developer resources.'
random_paper: 66
scopes:
- name: Police Bank Scopes
  scope_count: 5
  slug: police-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 34.9
  delta: -5.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.0
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/police-bank/refs/heads/main/screenshots/police-bank-2026-07-21T114745.png
security:
- kind: authentication
  name: Police Bank Authentication
  slug: police-bank-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Police Bank Domain Security
  slug: police-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: police-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.policebank.com.au/
---

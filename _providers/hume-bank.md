---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hume Bank Agentic Access
  operation_count: 2
  slug: hume-bank-agentic-access
  summary_line: 2 operations
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Hume Bank Banking Account Balances API
  slug: hume-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Hume Bank Banking Account Direct Debits API
  slug: hume-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Hume Bank Banking Account Scheduled Payments API
  slug: hume-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Hume Bank Banking Account Transactions API
  slug: hume-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Hume Bank Banking Accounts API
  slug: hume-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Hume Bank Banking Payees API
  slug: hume-bank-banking-payees-api
- description: Banking Product endpoints
  name: Hume Bank Banking Products API
  slug: hume-bank-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-hume-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-hume-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-hume-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-hume-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-hume-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-hume-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-hume-bank-banking-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hume-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hume-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hume-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hume-bank-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hume-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hume-bank-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hume-bank-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hume-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hume-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hume-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hume-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/hume-bank-product-lookup.md
- group: company
  title: ''
  type: Website
  url: https://www.humebank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.humebank.com.au/tools-help/open-banking/
- group: docs
  title: ''
  type: Documentation
  url: https://www.humebank.com.au/tools-help/open-banking/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#consumer-data-standards-banking-apis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.humebank.com.au/interest-rates/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.humebank.com.au/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.humebank.com.au/terms-of-use/
- group: start
  title: ''
  type: Login
  url: https://ibank.humebank.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.humebank.com.au/tools-help/get-in-touch/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/humebank
created: '2026-07-20'
description: Hume Bank is a customer-owned (mutual) Australian bank headquartered in Albury, New South Wales. Founded in 1955 as the Hume Co-operative Building & Investment Society, it became Hume Building Society and then Hume Bank on 1 July 2014, serving roughly 65,000 customers with around A$1.70 billion in assets. As an authorised deposit-taking institution (ADI) it participates in Australia's Consumer Data Right (CDR / Open Banking) regime, exposing a public, unauthenticated Product Reference Data (PRD) API built to the Consumer Data Standards for its retail and business deposit and credit card products, alongside the accredited-data-recipient consent flows required of a CDR data holder.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hume-bank.png
layout: provider
mcp_servers:
- description: ''
  name: hume-bank-mcp.yml
  slug: hume-bank-mcpyml
modified: '2026-07-22'
name: Hume Bank
nav: Providers
network: true
overview: 'Hume Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Hume Bank''s developer surface includes authentication, documentation, API reference, pricing, support, and 17 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 39.5
  delta: 0.7
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 51.0
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 38.8
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
    score: 31.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hume-bank/refs/heads/main/screenshots/hume-bank-2026-07-21T114727.png
security:
- kind: authentication
  name: Hume Bank Authentication
  slug: hume-bank-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Hume Bank Domain Security
  slug: hume-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hume-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual
- Product Reference Data
website: https://www.humebank.com.au/
---

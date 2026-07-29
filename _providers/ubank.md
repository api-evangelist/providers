---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agentic_access: false
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
  score: 36.3
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: ubank Banking Account Balances API
  slug: ubank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: ubank Banking Account Direct Debits API
  slug: ubank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: ubank Banking Account Scheduled Payments API
  slug: ubank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: ubank Banking Account Transactions API
  slug: ubank-banking-account-transactions-api
- description: Banking Account endpoints
  name: ubank Banking Accounts API
  slug: ubank-banking-accounts-api
- description: Banking Payee endpoints
  name: ubank Banking Payees API
  slug: ubank-banking-payees-api
- description: Banking Product endpoints
  name: ubank Banking Products API
  slug: ubank-banking-products-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ubank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ubank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ubank-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ubank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ubank.com.au/
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/ubank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ubank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ubank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ubank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ubank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ubank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ubank.com.au/cdr/apis
- group: operate
  title: ''
  type: Support
  url: https://www.ubank.com.au/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ubank.com.au/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ubank
created: '2026-07-20'
description: ubank is an Australian digital-only bank offering savings accounts and home loans online and over the phone. Launched in 2008 as the online banking brand of National Australia Bank (NAB), ubank operates under NAB's authorised deposit-taking institution (ADI) licence and is registered in the Consumer Data Right (CDR) ecosystem as the "UBank" data holder brand under NAB (ABN 12 004 044 937). After NAB acquired neobank 86 400 in 2021, its customers and technology were migrated onto the 86 400 platform, which is why ubank's public CDR API surface is hosted at public.cdr-api.86400.com.au. As a CDR data holder, ubank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards, while authenticated consumer banking data is shared only with accredited data recipients under the CDR's OAuth2/OIDC (FAPI) authorization model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ubank.png
layout: provider
mcp_servers:
- description: ''
  name: ubank-mcp.yml
  slug: ubank-mcpyml
modified: '2026-07-21'
name: ubank
nav: Providers
network: true
overview: 'ubank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Banking, Open Banking, and CDR.


  ubank''s developer surface includes authentication, documentation, support, and 16 more developer resources.'
random_paper: 43
scopes:
- name: Ubank Scopes
  scope_count: 9
  slug: ubank-scopes
  summary_line: 9 scopes
score:
  band: thin
  composite: 35.1
  delta: -6.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.0
    developer_ergonomics: 27.7
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 41.1
  provenance:
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
screenshot: https://raw.githubusercontent.com/api-evangelist/ubank/refs/heads/main/screenshots/ubank-2026-07-21T114753.png
security:
- kind: authentication
  name: Ubank Authentication
  slug: ubank-authentication
  summary_line: none/oauth2/openIdConnect · 0 schemes
- kind: domain-security
  name: Ubank Domain Security
  slug: ubank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ubank
tags:
- Financial
- Banks
- Banking
- Open Banking
- CDR
- Consumer Data Right
- Product Reference Data
- Digital Bank
- Consumer Banking
- Australia
website: https://www.ubank.com.au/
---

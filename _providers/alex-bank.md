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
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Alex Bank Agentic Access
  operation_count: 19
  slug: alex-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Alex Bank Banking Account Balances API
  slug: alex-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Alex Bank Banking Account Direct Debits API
  slug: alex-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Alex Bank Banking Account Scheduled Payments API
  slug: alex-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Alex Bank Banking Account Transactions API
  slug: alex-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Alex Bank Banking Accounts API
  slug: alex-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Alex Bank Banking Payees API
  slug: alex-bank-banking-payees-api
- description: Banking Product endpoints
  name: Alex Bank Banking Products API
  slug: alex-bank-banking-products-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: List Alex Bank's public CDR banking products, then retrieve the full detail of the first product. Runs against the public unauthenticated PRD endpoint - no credentials.
  name: Browse Alex Bank products and fetch one product's detail
  slug: alex-bank-browse-products
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alex-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alex-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alex.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alex.bank/legal/open-banking/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#get-products
- group: company
  title: ''
  type: Blog
  url: https://www.alex.bank/blog/
- group: operate
  title: ''
  type: Support
  url: https://consent.cdr.alex.com.au
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alex.bank/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alex.bank/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alex.bank/legal/consumer-data-right-cdr-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/alex-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alex-bank-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alex-bank-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alex-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alex-bank-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alex-bank-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alex-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: DataModel
  url: data-model/alex-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alex-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alex-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/alex-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/alex-bank-lookup-products.md
- group: design
  title: ''
  type: Arazzo
  url: arazzo/alex-bank-browse-products.yml
created: '2026-07-20'
description: Alex Bank (Alex Bank Pty Ltd, ABN 13 627 244 848) is an Australian digital bank headquartered in Brisbane, founded in 2018 by former Suncorp bankers Simon Beitz and Craig Fenwick. It is a shareholder-owned, venture-backed authorised deposit-taking institution (ADI) - not a customer-owned mutual - that received its Restricted ADI licence from APRA in July 2021 and a full banking licence in December 2021, and joined the Reserve Bank of Australia's RITS as an Exchange Settlement Account holder in 2025. Alex offers consumer lending (personal, green, car and EV loans) and deposit products (term deposits and a savings account). As an active ADI, Alex is a Consumer Data Right (CDR) data holder - it publishes an unauthenticated Product Reference Data API under the DSB Consumer Data Standards, runs a CDR consent-management portal, and supports accredited-data-recipient sharing of savings, term deposit and personal loan data.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alex-bank.png
layout: provider
mcp_servers:
- description: ''
  name: alex-bank-mcp.yml
  slug: alex-bank-mcpyml
modified: '2026-07-21T12:00:00Z'
name: Alex Bank
nav: Providers
network: true
overview: 'Alex Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  Alex Bank''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 19 more developer resources.'
random_paper: 63
scopes:
- name: Alex Bank Scopes
  scope_count: 12
  slug: alex-bank-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: thin
  composite: 41.9
  delta: -2.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 50.0
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 70.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alex-bank/refs/heads/main/screenshots/alex-bank-2026-07-21T114701.png
security:
- kind: authentication
  name: Alex Bank Authentication
  slug: alex-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Alex Bank Domain Security
  slug: alex-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alex-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Digital Bank
- Product Reference Data
website: https://www.alex.bank/
---

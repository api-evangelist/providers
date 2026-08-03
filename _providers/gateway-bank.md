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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gateway Bank Agentic Access
  operation_count: 19
  slug: gateway-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Gateway Bank Banking Account Balances API
  slug: gateway-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Gateway Bank Banking Account Direct Debits API
  slug: gateway-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Gateway Bank Banking Account Scheduled Payments API
  slug: gateway-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Gateway Bank Banking Account Transactions API
  slug: gateway-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Gateway Bank Banking Accounts API
  slug: gateway-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Gateway Bank Banking Payees API
  slug: gateway-bank-banking-payees-api
- description: Banking Product endpoints
  name: Gateway Bank Banking Products API
  slug: gateway-bank-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gateway-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gateway-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gateway-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gateway-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gateway-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gateway-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gateway-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gatewaybank.com.au/important-information/consumer-data-right-cdr/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gateway-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gateway-bank-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gateway-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/gateway-bank-browse-products.md
- group: design
  title: ''
  type: DataModel
  url: data-model/gateway-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gateway-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gateway-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.gatewaybank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gatewaybank.com.au/important-information/consumer-data-right-cdr/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gatewaybank.com.au/important-information/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/gateway-bank-ltd
created: '2026-07-20'
description: Gateway Bank Ltd is a 100% customer-owned Australian mutual bank headquartered in Sydney, New South Wales. Founded in 1955 as Gateway Credit Union and rebranded to Gateway Bank in 2018, it is an APRA-regulated Authorised Deposit-taking Institution (ADI) serving more than 30,000 members with over one billion dollars in assets across transaction and savings accounts, home, personal and car loans, reverse and commercial mortgages, term deposits and Visa debit cards. As an active ADI, Gateway Bank is a designated data holder under Australia's Consumer Data Right (CDR / Open Banking) and implements the full Data Standards Body (DSB) Consumer Data Standards Banking API surface - a public, unauthenticated Product Reference Data (PRD) API plus the consumer-authorized Accounts, Balances, Transactions, Direct Debits, Scheduled Payments and Payees endpoints accessed through the CDR Accredited Data Recipient model. Its registered CDR public base URI is https://public.cdr-api.gatewaybank.com.au.
  As a small customer-owned mutual, Gateway Bank does not operate a broader self-serve first-party developer portal beyond these CDR obligations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gateway-bank.png
layout: provider
mcp_servers:
- description: ''
  name: gateway-bank-mcp.yml
  slug: gateway-bank-mcpyml
modified: '2026-07-21'
name: Gateway Bank
nav: Providers
network: true
overview: 'Gateway Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Gateway Bank''s developer surface includes authentication, documentation, and 18 more developer resources.'
random_paper: 71
scopes:
- name: Gateway Bank Scopes
  scope_count: 5
  slug: gateway-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 54.3
    developer_ergonomics: 23.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 40.3
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
    score: 72.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gateway-bank/refs/heads/main/screenshots/gateway-bank-2026-07-21T114722.png
security:
- kind: authentication
  name: Gateway Bank Authentication
  slug: gateway-bank-authentication
  summary_line: none/oauth2/openIdConnect · 0 schemes
- kind: domain-security
  name: Gateway Bank Domain Security
  slug: gateway-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gateway-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Mutual Bank
- Customer Owned
- Australia
- Product Reference Data
website: https://www.gatewaybank.com.au/
---

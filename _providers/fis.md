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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Fis Agentic Access
  operation_count: 8
  slug: fis-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 7
apis:
- description: FIS (Fidelity National Information Services) provides core banking platforms including the Systematics suite. APIs bridge mainframe-based account processing, transaction management, and loan servicing
  name: FIS Core Banking API
  slug: fis-core-banking-api
- description: FIS wealth management APIs enable integration with portfolio management, account aggregation, trading, and advisory systems for wealth management platforms and financial advisors.
  name: FIS Wealth Management API
  slug: fis-wealth-management-api
- description: Account information and balance inquiries
  name: FIS Global Accounts API
  slug: fis-accounts-api
- description: ACH (Automated Clearing House) payment operations
  name: FIS Global ACH API
  slug: fis-ach-api
- description: Initiate and manage payment transactions
  name: FIS Global Payments API
  slug: fis-payments-api
- description: Transaction history and status
  name: FIS Global Transactions API
  slug: fis-transactions-api
- description: Domestic and international wire transfer operations
  name: FIS Global Wire Transfers API
  slug: fis-wire-transfers-api
artifact_total: 18
collections:
- collection_type: open
  name: FIS Payments API
  slug: open-fis-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fis-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FISGlobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fis
description: FIS (Fidelity National Information Services) is a global leader in financial technology providing APIs for core banking, payments, wealth management, and capital markets through the CodeConnect API marketplace. APIs connect financial institutions, fintechs, and enterprises to FIS banking and payment infrastructure.
finops:
- name: Fis Finops
  service_category: Financial Services Software
  slug: fis-finops
image: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/image.png
json_schemas:
- name: FIS Payment
  property_count: 15
  slug: fis-payment
jsonld:
- class_count: 12
  name: Fis Context
  property_count: 10
  slug: fis-context
layout: provider
modified: '2026-04-28'
name: FIS Global
nav: Providers
network: true
overview: 'FIS Global publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, ACH API, Payments API, and 2 more. Tagged areas include Banking, Core Banking, Financial Services, Payments, and Fintech.


  The FIS Global catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FIS Global''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Fis Plans Pricing
  plan_count: 3
  slug: fis-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Fis Rate Limits
  slug: fis-rate-limits
rules:
- name: FIS Global API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fis-jsonschema-spectral-rules
scopes:
- name: Fis Scopes
  scope_count: 3
  slug: fis-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 44.7
  delta: -5.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.5
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/screenshots/fis-2026-06-20T181251.png
security:
- kind: authentication
  name: Fis Authentication
  slug: fis-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fis Domain Security
  slug: fis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fis
tags:
- Banking
- Core Banking
- Financial Services
- Payments
- Fintech
---

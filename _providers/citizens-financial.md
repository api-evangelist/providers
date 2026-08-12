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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Citizens Financial Agentic Access
  operation_count: 4
  slug: citizens-financial-agentic-access
  summary_line: 4 operations
api_count: 4
apis:
- description: The Citizens Pay API enables merchants and partners to integrate Citizens Pay point-of-sale financing into their applications and checkout experiences. Citizens Pay provides consumer financing solutio
  name: Citizens Pay API
  slug: citizens-pay-api
- description: Retrieve account information
  name: Citizens Financial Accounts API
  slug: citizens-financial-accounts-api
- description: Search and retrieve ATM location data
  name: Citizens Financial ATM Locations API
  slug: citizens-financial-atm-locations-api
- description: Retrieve transaction history
  name: Citizens Financial Transactions API
  slug: citizens-financial-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: Citizens Bank Accounts API
  slug: open-citizens-bank-accounts-api
- collection_type: open
  name: Citizens Bank ATM Locator API
  slug: open-citizens-bank-atm-locator-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/citizens-financial-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citizens-financial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/citizens-financial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/citizens-financial-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rbs-citizens-financial-group
- group: company
  title: ''
  type: Website
  url: https://www.citizensbank.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.citizensbank.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandboxdeveloper.citizensbank.com/api
- group: operate
  title: ''
  type: Support
  url: https://developer.citizensbank.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citizensbank.com/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/citizens-financial-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/citizens-financial-rules.yml
created: '2026-03-21'
description: Citizens Financial Group is one of the oldest and largest financial institutions in the United States, providing retail and commercial banking products and services to individuals, small businesses, middle-market companies, and large corporations. Citizens exposes its programmable surface through the Citizens developer portal at developer.citizensbank.com, with REST APIs for deposit account and transaction data, ATM location services, and point-of-sale consumer financing through Citizens Pay. Authentication is OAuth 2.0 and the portal provides both sandbox and production environments.
finops:
- name: Citizens Financial Finops
  service_category: Banking
  slug: citizens-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citizens-financial.png
jsonld:
- class_count: 14
  name: Citizens Financial Context
  property_count: 0
  slug: citizens-financial-context
layout: provider
modified: '2026-05-19'
name: Citizens Financial
nav: Providers
network: true
overview: 'Citizens Financial publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, ATM Locations API, and Transactions API. Tagged areas include Accounts, ATMs, Banking, Open Banking, and Payments.


  The Citizens Financial catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citizens Financial''s developer surface includes authentication, developer portal, sandbox, support, and 8 more developer resources.'
plans:
- name: Citizens Financial Plans Pricing
  plan_count: 2
  slug: citizens-financial-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 2
  name: Citizens Financial Rate Limits
  slug: citizens-financial-rate-limits
rules:
- name: Citizens Financial API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: citizens-financial-rules
scopes:
- name: Citizens Financial Scopes
  scope_count: 2
  slug: citizens-financial-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 40.0
  delta: -5.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 68.7
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/citizens-financial/refs/heads/main/screenshots/citizens-financial-2026-06-20T174412.png
security:
- kind: authentication
  name: Citizens Financial Authentication
  slug: citizens-financial-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Citizens Financial Domain Security
  slug: citizens-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citizens-financial
tags:
- Accounts
- ATMs
- Banking
- Open Banking
- Payments
- Point of Sale
- Transactions
website: https://www.citizensbank.com/
---

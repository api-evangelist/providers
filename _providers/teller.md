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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Teller Agentic Access
  operation_count: 10
  slug: teller-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 4
apis:
- description: Bank account management
  name: Teller Accounts API
  slug: teller-accounts-api
- description: Account holder identity information
  name: Teller Identity API
  slug: teller-identity-api
- description: Supported financial institutions
  name: Teller Institutions API
  slug: teller-institutions-api
- description: Account transaction history
  name: Teller Transactions API
  slug: teller-transactions-api
artifact_total: 22
asyncapis:
- description: AsyncAPI specification describing Teller's outbound webhook surface. Teller sends signed HTTPS POST callbacks to a developer-configured endpoint when notable events occur on enrollments and accounts (
  name: Teller Webhooks
  slug: teller-webhooks-asyncapi
collections:
- collection_type: open
  name: Teller API
  slug: open-teller
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teller-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teller-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teller-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hello-teller
- group: company
  title: ''
  type: Website
  url: https://teller.io/
- group: docs
  title: ''
  type: Documentation
  url: https://teller.io/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://teller.io/docs/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tellerhq
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tellerhq/teller-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tellerhq/teller-connect-react
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tellerhq/iOS-SDK
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tellerhq/teller-connect-android
- group: company
  title: ''
  type: Blog
  url: https://teller.io/blog
description: Teller is a unified banking API providing real-time access to bank accounts, transactions, balances, identity data, and payment initiation across US financial institutions. Connect to thousands of banks and credit unions through a single integration. Teller uses mutual TLS (mTLS) for application authentication and access tokens obtained via Teller Connect for per-account authorization.
examples:
- key_count: 4
  name: Teller Get Balances Example
  slug: teller-get-balances-example
- key_count: 4
  name: Teller List Accounts Example
  slug: teller-list-accounts-example
- key_count: 4
  name: Teller List Transactions Example
  slug: teller-list-transactions-example
finops:
- name: Teller Finops
  service_category: API
  slug: teller-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teller.png
json_schemas:
- name: Teller Account
  property_count: 10
  slug: teller-account
- name: Teller Transaction
  property_count: 10
  slug: teller-transaction
json_structures:
- name: Teller Banking Structure
  property_count: 0
  slug: teller-banking-structure
jsonld:
- class_count: 2
  name: Teller Context
  property_count: 7
  slug: teller-context
layout: provider
modified: '2026-05-30'
name: Teller
nav: Providers
network: true
overview: 'Teller publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Identity API, Institutions API, and 1 more. Tagged areas include Banking, Financial Data, FinTech, Open Banking, and Transactions.


  The Teller catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Teller''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Teller Plans Pricing
  plan_count: 3
  slug: teller-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Teller Rate Limits
  slug: teller-rate-limits
rules:
- name: Teller API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: teller-asyncapi-spectral-rules
- name: Teller API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: teller-jsonschema-spectral-rules
- name: Teller API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 5
  slug: teller-rules
score:
  band: developing
  composite: 47.9
  delta: -5.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.1
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Teller Authentication
  slug: teller-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Teller Domain Security
  slug: teller-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teller
tags:
- Banking
- Financial Data
- FinTech
- Open Banking
- Transactions
- Unified API
website: https://teller.io/
---

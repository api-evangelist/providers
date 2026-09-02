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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Teller Agentic Access
  operation_count: 10
  slug: teller-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
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
artifact_total: 27
asyncapis:
- description: AsyncAPI specification describing Teller's outbound webhook surface. Teller sends signed HTTPS POST callbacks to a developer-configured endpoint when notable events occur on enrollments and accounts (
  name: Teller Webhooks
  slug: teller-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teller Accounts API
  slug: open-teller-accounts-api
- collection_type: open
  name: Teller Accounts Identity API
  slug: open-teller-identity-api
- collection_type: open
  name: Teller Accounts Institutions API
  slug: open-teller-institutions-api
- collection_type: open
  name: Teller Accounts Transactions API
  slug: open-teller-transactions-api
- collection_type: open
  name: Teller API
  slug: open-teller
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/teller-capability-edges.yml
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
overview: 'Teller publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Identity API, Institutions API, and 1 more. Tagged areas include Banking, Financial Data, Fintech, Open Banking, and Transaction.


  The Teller catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Teller''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Teller Plans Pricing
  plan_count: 3
  slug: teller-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Teller Rate Limits
  slug: teller-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Teller API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: teller-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Teller API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: teller-jsonschema-spectral-rules
- effective_rule_count: 12
  extends: []
  name: Teller API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 5
  slug: teller-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 66.3
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 40.7
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
- Fintech
- Open Banking
- Transaction
- Unified-API
website: https://teller.io/
---

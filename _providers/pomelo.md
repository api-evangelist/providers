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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Pomelo Agentic Access
  operation_count: 20
  slug: pomelo-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 6
apis:
- description: OAuth 2.0 client-credentials token issuance.
  name: Pomelo Authentication API
  slug: pomelo-authentication-api
- description: Card account balances, activities, and movements.
  name: Pomelo Card Accounts API
  slug: pomelo-card-accounts-api
- description: Issuing and lifecycle of physical and virtual cards.
  name: Pomelo Cards API
  slug: pomelo-cards-api
- description: Processed transactions, summaries, and history.
  name: Pomelo Transactions API
  slug: pomelo-transactions-api
- description: Money movement and settlements across card accounts.
  name: Pomelo Transfers API
  slug: pomelo-transfers-api
- description: Cardholder records and KYC/KYB identity verification.
  name: Pomelo Users API
  slug: pomelo-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pomelo Authentication API
  slug: open-pomelo-authentication-api
- collection_type: open
  name: Pomelo Authentication Card Accounts API
  slug: open-pomelo-card-accounts-api
- collection_type: open
  name: Pomelo Authentication Cards API
  slug: open-pomelo-cards-api
- collection_type: open
  name: Pomelo Authentication Transactions API
  slug: open-pomelo-transactions-api
- collection_type: open
  name: Pomelo Authentication Transfers API
  slug: open-pomelo-transfers-api
- collection_type: open
  name: Pomelo Authentication Users API
  slug: open-pomelo-users-api
- collection_type: open
  name: Pomelo API
  slug: open-pomelo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pomelo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pomelo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pomelo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pomelo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pomelo-la
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pomelo-la
- group: company
  title: ''
  type: Website
  url: https://www.pomelo.la
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pomelo.la
- group: commercial
  title: ''
  type: Plans
  url: plans/pomelo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pomelo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pomelo-finops.yml
created: '2026-06-21'
description: Pomelo (pomelo.la) is a Latin American card-issuing and embedded-finance platform. Its REST API lets fintechs and enterprises onboard users (KYC/KYB), issue physical and virtual cards, manage card accounts and balances, process and query transactions, move money with transfers and settlements, and authorize transactions in real time over a synchronous authorization webhook.
finops:
- name: Pomelo Finops
  service_category: Financial Services
  slug: pomelo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pomelo.png
layout: provider
modified: '2026-06-21'
name: Pomelo
nav: Providers
network: true
overview: 'Pomelo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Card Accounts API, Cards API, and 3 more. Tagged areas include Fintech, Card Issuing, Embedded Finance, Payments, and Latin America.


  Pomelo''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Pomelo Plans Pricing
  plan_count: 2
  slug: pomelo-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Pomelo Rate Limits
  slug: pomelo-rate-limits
scopes:
- name: Pomelo Scopes
  scope_count: 0
  slug: pomelo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.3
  delta: 2.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.9
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Pomelo Authentication
  slug: pomelo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pomelo Domain Security
  slug: pomelo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pomelo
tags:
- Fintech
- Card Issuing
- Embedded Finance
- Payments
- Latin America
website: https://www.pomelo.la
---

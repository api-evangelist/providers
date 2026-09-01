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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Quiltt Agentic Access
  operation_count: 15
  slug: quiltt-agentic-access
  summary_line: 15 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Single GraphQL endpoint for reading an end-user's unified financial data - Profile, Connections, Accounts, Balances, Account Owners and Numbers, Transactions, Investment Holdings, and Statements - aut
  name: Quiltt GraphQL Data API
  slug: quiltt-graphql-data-api
- description: Manage a Profile's aggregator Connections.
  name: Quiltt Connections API
  slug: quiltt-connections-api
- description: Manage end-user Profiles.
  name: Quiltt Profiles API
  slug: quiltt-profiles-api
- description: Issue, verify, and revoke Profile-scoped session tokens.
  name: Quiltt Session Tokens API
  slug: quiltt-session-tokens-api
- description: Manage webhook subscriptions for real-time events.
  name: Quiltt Webhooks API
  slug: quiltt-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quiltt Admin & Auth REST Connections API
  slug: open-quiltt-connections-api
- collection_type: open
  name: Quiltt Admin & Auth REST Connections Profiles API
  slug: open-quiltt-profiles-api
- collection_type: open
  name: Quiltt Admin & Auth REST Connections Session Tokens API
  slug: open-quiltt-session-tokens-api
- collection_type: open
  name: Quiltt Admin & Auth REST Connections Webhooks API
  slug: open-quiltt-webhooks-api
- collection_type: open
  name: Quiltt Admin & Auth REST API
  slug: open-quiltt
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quiltt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quiltt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quiltt-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quiltt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quiltt
- group: company
  title: ''
  type: Website
  url: https://www.quiltt.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.quiltt.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/quiltt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quiltt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quiltt-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.quiltt.io/blog
created: '2026-07-01'
description: Quiltt is a fintech data platform and abstraction layer over open-banking aggregators like Plaid, MX, and Finicity. It exposes a unified GraphQL API for reading end-user financial data (profiles, connections, accounts, balances, transactions, investment holdings, statements) plus a REST Admin/Auth API for profiles, connections, session tokens, and webhooks, and an embeddable Connector UI for account linking.
finops:
- name: Quiltt Finops
  service_category: Financial Data and Open Banking
  slug: quiltt-finops
graphqls:
- description: 'Quiltt is a fintech data platform that unifies open-banking aggregators (Plaid, MX, Finicity) behind a single GraphQL API. Clients query an end-user''s Profile to read Connections, Accounts, Balances, '
  name: Quiltt GraphQL Data API
  slug: quiltt-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quiltt.png
layout: provider
modified: '2026-07-01'
name: Quiltt
nav: Providers
network: true
overview: 'Quiltt publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Profiles API, Session Tokens API, and 1 more. Tagged areas include Fintech, Open Banking, Financial Data, Aggregation, and GraphQL.


  Quiltt''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Quiltt Plans Pricing
  plan_count: 3
  slug: quiltt-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Quiltt Rate Limits
  slug: quiltt-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.1
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
    score: 15.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Quiltt Authentication
  slug: quiltt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quiltt Domain Security
  slug: quiltt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: quiltt
tags:
- Fintech
- Open Banking
- Financial Data
- Aggregation
- GraphQL
website: https://www.quiltt.io/
---

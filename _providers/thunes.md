---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Thunes Agentic Access
  operation_count: 34
  slug: thunes-agentic-access
  summary_line: 34 operations · 11 acting
api_count: 9
apis:
- description: Real-time cross-border money transfer to bank accounts, mobile wallets, cash pickup, and cards.
  name: Thunes Money Transfer API
  slug: thunes-money-transfer-api
- description: Accept payments globally via local methods, mobile money and bank transfers.
  name: Thunes Collection API
  slug: thunes-collection-api
- description: The Account Management API from Thunes — 7 operation(s) for account management.
  name: Thunes Account Management API
  slug: thunes-account-management-api
- description: The Connectivity API from Thunes — 1 operation(s) for connectivity.
  name: Thunes Connectivity API
  slug: thunes-connectivity-api
- description: The Credit Parties API from Thunes — 2 operation(s) for credit parties.
  name: Thunes Credit Parties API
  slug: thunes-credit-parties-api
- description: The Discovery API from Thunes — 6 operation(s) for discovery.
  name: Thunes Discovery API
  slug: thunes-discovery-api
- description: The Quotations API from Thunes — 3 operation(s) for quotations.
  name: Thunes Quotations API
  slug: thunes-quotations-api
- description: The Simulation API from Thunes — 3 operation(s) for simulation.
  name: Thunes Simulation API
  slug: thunes-simulation-api
- description: The Transactions API from Thunes — 10 operation(s) for transactions.
  name: Thunes Transactions API
  slug: thunes-transactions-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Thunes Money Transfer Account Management API
  slug: open-thunes-account-management-api
- collection_type: open
  name: Thunes Money Transfer Account Management Connectivity API
  slug: open-thunes-connectivity-api
- collection_type: open
  name: Thunes Money Transfer Account Management Credit Parties API
  slug: open-thunes-credit-parties-api
- collection_type: open
  name: Thunes Money Transfer Account Management Discovery API
  slug: open-thunes-discovery-api
- collection_type: open
  name: Thunes Money Transfer Account Management Quotations API
  slug: open-thunes-quotations-api
- collection_type: open
  name: Thunes Money Transfer Account Management Simulation API
  slug: open-thunes-simulation-api
- collection_type: open
  name: Thunes Money Transfer Account Management Transactions API
  slug: open-thunes-transactions-api
- collection_type: open
  name: Thunes Money Transfer API
  slug: open-thunes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thunes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thunes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thunes-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thunespayments
- group: company
  title: ''
  type: Website
  url: https://www.thunes.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/thunes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thunes-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thunes-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.thunes.com/llms.txt
created: '2026-05-08'
description: Thunes is a global cross-border payments network reaching 80+ countries via mobile wallets, bank accounts, cards, and cash. Powers send-money, accept-money, and direct-to-card flows.
finops:
- name: Thunes Finops
  service_category: Fintech
  slug: thunes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thunes.png
layout: provider
modified: '2026-05-08'
name: Thunes
nav: Providers
network: true
overview: 'Thunes publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Connectivity API, Credit Parties API, and 4 more. Tagged areas include Fintech, Cross-Border, Payments, FX, and Mobile Money.


  Thunes'' developer surface includes authentication and 8 more developer resources.'
plans:
- name: Thunes Plans Pricing
  plan_count: 1
  slug: thunes-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Thunes Rate Limits
  slug: thunes-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: 1.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Thunes Authentication
  slug: thunes-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Thunes Domain Security
  slug: thunes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thunes
tags:
- Fintech
- Cross-Border
- Payments
- FX
- Mobile Money
website: https://www.thunes.com/
---

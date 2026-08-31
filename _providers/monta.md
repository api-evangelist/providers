---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Monta Agentic Access
  operation_count: 17
  slug: monta-agentic-access
  summary_line: 17 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'Signed webhook payloads deliver real-time platform events without polling, covering charge transactions, OCPP messages, sites, teams, wallet transactions, and more. Webhook subscription configuration '
  name: Monta Webhooks
  slug: webhooks
- description: The Authentication API from Monta — 3 operation(s) for authentication.
  name: Monta Authentication API
  slug: monta-authentication-api
- description: The Charge Points API from Monta — 5 operation(s) for charge points.
  name: Monta Charge Points API
  slug: monta-charge-points-api
- description: The Charges API from Monta — 4 operation(s) for charges.
  name: Monta Charges API
  slug: monta-charges-api
- description: The Utilities API from Monta — 1 operation(s) for utilities.
  name: Monta Utilities API
  slug: monta-utilities-api
- description: The Wallet Transactions API from Monta — 3 operation(s) for wallet transactions.
  name: Monta Wallet Transactions API
  slug: monta-wallet-transactions-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Monta Public Authentication API
  slug: open-monta-authentication-api
- collection_type: open
  name: Monta Public Authentication Charge Points API
  slug: open-monta-charge-points-api
- collection_type: open
  name: Monta Public Authentication Charges API
  slug: open-monta-charges-api
- collection_type: open
  name: Monta Public Authentication Utilities API
  slug: open-monta-utilities-api
- collection_type: open
  name: Monta Public Authentication Wallet Transactions API
  slug: open-monta-wallet-transactions-api
- collection_type: open
  name: Monta Public API
  slug: open-monta
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/monta-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monta-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monta-app
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/montaapp
- group: company
  title: ''
  type: Website
  url: https://www.monta.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.public-api.monta.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/monta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/monta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/monta-finops.yml
created: '2026-06-21'
description: Monta is an EV-charging software platform that operates charge points, a consumer driver app, and back-office tools for installers, businesses, and charge point operators. The Monta Public API exposes charge points, charges (charging sessions), EVSE availability and pricing, and wallet transactions via a REST interface secured with OAuth2 client-credentials bearer tokens, plus signed webhooks for real-time platform events.
finops:
- name: Monta Finops
  service_category: EV Charging and Energy
  slug: monta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monta.png
layout: provider
modified: '2026-06-21'
name: Monta
nav: Providers
network: true
overview: 'Monta publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Charge Points API, Charges API, and 2 more. Tagged areas include EV Charging, Electric Vehicles, Charge Points, Energy, and Mobility.


  Monta''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Monta Plans Pricing
  plan_count: 2
  slug: monta-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Monta Rate Limits
  slug: monta-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.6
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
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monta/refs/heads/main/screenshots/monta-2026-08-07T184221.png
security:
- kind: authentication
  name: Monta Authentication
  slug: monta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Monta Domain Security
  slug: monta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: monta
tags:
- EV Charging
- Electric Vehicles
- Charge Points
- Energy
- Mobility
website: https://www.monta.com
---

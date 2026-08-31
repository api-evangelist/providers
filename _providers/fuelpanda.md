---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fuelpanda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fleetpanda.com
- group: start
  title: ''
  type: Login
  url: https://app.fleetpanda.com
- group: company
  title: ''
  type: Blog
  url: https://fleetpanda.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://fleetpanda.freshdesk.com/support/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fleetpanda
- group: commercial
  title: ''
  type: Pricing
  url: https://fleetpanda.com/get-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fleetpanda.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fleetpanda.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://fleetpanda.com/blog/protecting-what-matters-fleetpanda-achieves-soc-2---type-1-compliance
- group: design
  title: ''
  type: Conformance
  url: conformance/fuelpanda-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fuelpanda-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fuelpanda-llms.txt
created: '2026-07-17'
description: FleetPanda is a cloud-based dispatch and delivery platform for fuel distributors, describing itself as "the operating system for fuel distributors." It manages fuel distribution operations across multiple business lines including tank wagon / wet hosing, truck & trailer, transport, lubricants, and propane delivery. The platform provides a dispatch dashboard with real-time driver and inventory visibility, order management, same-day billing and invoicing with auto-BOL linking, automated reconciliation, pricing and fee management, reporting and analytics, an iOS/Android driver app, and a customer portal. FleetPanda is SOC 2 Type 1 compliant and is backed by 500 Global. The company is catalogued in the API Evangelist network; it does not currently publish a public API, developer portal, or SDKs.
image: https://fleetpanda.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: FleetPanda
nav: Providers
network: true
overview: 'FleetPanda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fuel Distribution, Fleet Management, Dispatch, and Delivery Logistics.


  FleetPanda''s developer surface includes engineering blog, support, pricing, and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 20.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fuelpanda/refs/heads/main/screenshots/fuelpanda-2026-07-25T215251.png
security:
- kind: domain-security
  name: Fuelpanda Domain Security
  slug: fuelpanda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fuelpanda
tags:
- Company
- Fuel Distribution
- Fleet Management
- Dispatch
- Delivery Logistics
- Energy
- Transportation
- Software-as-a-Service
website: https://fleetpanda.com
---

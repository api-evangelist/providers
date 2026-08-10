---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Esimgo Agentic Access
  operation_count: 22
  slug: esimgo-agentic-access
  summary_line: 22 operations · 6 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Browse data bundles available to your organisation.
  name: eSIM Go Catalogue API
  slug: esimgo-catalogue-api
- description: Manage eSIMs, bundle assignments, and install details.
  name: eSIM Go eSIMs API
  slug: esimgo-esims-api
- description: View and refund unassigned bundle inventory.
  name: eSIM Go Inventory API
  slug: esimgo-inventory-api
- description: Per-country network coverage data.
  name: eSIM Go Networks API
  slug: esimgo-networks-api
- description: Validate, place, and retrieve bundle orders.
  name: eSIM Go Orders API
  slug: esimgo-orders-api
- description: Organisation account details and balance.
  name: eSIM Go Organisation API
  slug: esimgo-organisation-api
artifact_total: 13
collections:
- collection_type: open
  name: eSIM Go API
  slug: open-esimgo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/esimgo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/esimgo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/esimgo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/esim-go
- group: company
  title: ''
  type: Website
  url: https://www.esim-go.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.esim-go.com
- group: commercial
  title: ''
  type: Plans
  url: plans/esimgo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/esimgo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/esimgo-finops.yml
created: '2026-06-21'
description: eSIM Go is an eSIM connectivity and travel-data platform that lets resellers and brands launch their own eSIM products. Its REST API aggregates tier-1 telecom services across 190+ countries, exposing a data-bundle catalogue, order placement, eSIM assignment, install/QR provisioning, inventory, network coverage, and usage webhooks.
finops:
- name: Esimgo Finops
  service_category: Telecommunications
  slug: esimgo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/esimgo.png
layout: provider
modified: '2026-06-21'
name: eSIM Go
nav: Providers
network: true
overview: 'eSIM Go publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalogue API, eSIMs API, Inventory API, and 3 more. Tagged areas include eSIM, Connectivity, Travel Data, Telecom, and Mobile.


  eSIM Go''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Esimgo Plans Pricing
  plan_count: 4
  slug: esimgo-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 2
  name: Esimgo Rate Limits
  slug: esimgo-rate-limits
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.0
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
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/esimgo/refs/heads/main/screenshots/esimgo-2026-07-25T213621.png
security:
- kind: authentication
  name: Esimgo Authentication
  slug: esimgo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Esimgo Domain Security
  slug: esimgo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: esimgo
tags:
- eSIM
- Connectivity
- Travel Data
- Telecom
- Mobile
website: https://www.esim-go.com
---

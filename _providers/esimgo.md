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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Esimgo Agentic Access
  operation_count: 22
  slug: esimgo-agentic-access
  summary_line: 22 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.esim-go.com/v2.4
  baseurl_source: declared
  description: Browse data bundles available to your organisation.
  name: eSIM Go Catalogue API
  slug: esimgo-catalogue-api
- baseURL: https://api.esim-go.com/v2.4
  baseurl_source: declared
  description: Manage eSIMs, bundle assignments, and install details.
  name: eSIM Go eSIMs API
  slug: esimgo-esims-api
- baseURL: https://api.esim-go.com/v2.4
  baseurl_source: declared
  description: View and refund unassigned bundle inventory.
  name: eSIM Go Inventory API
  slug: esimgo-inventory-api
- baseURL: https://api.esim-go.com/v2.4
  baseurl_source: declared
  description: Per-country network coverage data.
  name: eSIM Go Networks API
  slug: esimgo-networks-api
- baseURL: https://api.esim-go.com/v2.4
  baseurl_source: declared
  description: Validate, place, and retrieve bundle orders.
  name: eSIM Go Orders API
  slug: esimgo-orders-api
- baseURL: https://api.esim-go.com/v2.4
  baseurl_source: declared
  description: Organisation account details and balance.
  name: eSIM Go Organisation API
  slug: esimgo-organisation-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: eSIM Go Catalogue API
  slug: open-esimgo-catalogue-api
- collection_type: open
  name: eSIM Go Catalogue eSIMs API
  slug: open-esimgo-esims-api
- collection_type: open
  name: eSIM Go Catalogue Inventory API
  slug: open-esimgo-inventory-api
- collection_type: open
  name: eSIM Go Catalogue Networks API
  slug: open-esimgo-networks-api
- collection_type: open
  name: eSIM Go Catalogue Orders API
  slug: open-esimgo-orders-api
- collection_type: open
  name: eSIM Go Catalogue Organisation API
  slug: open-esimgo-organisation-api
- collection_type: open
  name: eSIM Go API
  slug: open-esimgo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/esimgo-capability-edges.yml
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


  eSIM Go''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Esimgo Plans Pricing
  plan_count: 4
  slug: esimgo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Esimgo Rate Limits
  slug: esimgo-rate-limits
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.7
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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

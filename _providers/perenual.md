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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Perenual Agentic Access
  operation_count: 5
  slug: perenual-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Plant care guides
  name: Perenual Care API
  slug: perenual-care-api
- description: Hardiness map data
  name: Perenual Maps API
  slug: perenual-maps-api
- description: Pest and disease data
  name: Perenual Pests API
  slug: perenual-pests-api
- description: Plant species data
  name: Perenual Species API
  slug: perenual-species-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Perenual Care API
  slug: open-perenual-care-api
- collection_type: open
  name: Perenual Care Maps API
  slug: open-perenual-maps-api
- collection_type: open
  name: Perenual API
  slug: open-perenual-perenual
- collection_type: open
  name: Perenual Care Pests API
  slug: open-perenual-pests-api
- collection_type: open
  name: Perenual Care Species API
  slug: open-perenual-species-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/perenual-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/perenual-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perenual-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/perenual-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://perenual.com
- group: docs
  title: ''
  type: Documentation
  url: https://perenual.com/docs/api
- group: agent
  title: ''
  type: LlmsText
  url: https://perenual.com/llms.txt
created: '2025-02-24'
description: Perenual provides a comprehensive plant database API offering access to over 10,000+ plant species, including details on care, watering, sunlight, edibility, toxicity, pests, diseases, and care guides.
finops:
- name: Perenual Finops
  service_category: API
  slug: perenual-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perenual.png
layout: provider
modified: '2026-05-19'
name: Perenual
nav: Providers
network: true
overview: 'Perenual publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Care API, Maps API, Pests API, and 1 more. Tagged areas include Plants, Botany, Gardening, and Horticulture.


  Perenual''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Perenual Plans Pricing
  plan_count: 3
  slug: perenual-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Perenual Rate Limits
  slug: perenual-rate-limits
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 21.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perenual/refs/heads/main/screenshots/perenual-2026-06-20T191559.png
security:
- kind: authentication
  name: Perenual Authentication
  slug: perenual-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Perenual Domain Security
  slug: perenual-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Perenual Vulnerability Disclosure
  slug: perenual-vulnerability-disclosure
  summary_line: disclosure policy published
slug: perenual
tags:
- Plants
- Botany
- Gardening
- Horticulture
website: https://perenual.com
---

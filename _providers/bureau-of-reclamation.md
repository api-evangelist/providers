---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Reclamation Agentic Access
  operation_count: 17
  slug: bureau-of-reclamation-agentic-access
  summary_line: 17 operations
api_count: 6
apis:
- description: The Catalog API from Bureau of Reclamation — 5 operation(s) for catalog.
  name: Bureau of Reclamation Catalog API
  slug: bureau-of-reclamation-catalog-api
- description: The Locations API from Bureau of Reclamation — 2 operation(s) for locations.
  name: Bureau of Reclamation Locations API
  slug: bureau-of-reclamation-locations-api
- description: The Model Runs API from Bureau of Reclamation — 3 operation(s) for model runs.
  name: Bureau of Reclamation Model Runs API
  slug: bureau-of-reclamation-model-runs-api
- description: The Parameters API from Bureau of Reclamation — 2 operation(s) for parameters.
  name: Bureau of Reclamation Parameters API
  slug: bureau-of-reclamation-parameters-api
- description: The Reference Data API from Bureau of Reclamation — 4 operation(s) for reference data.
  name: Bureau of Reclamation Reference Data API
  slug: bureau-of-reclamation-reference-data-api
- description: The Results API from Bureau of Reclamation — 1 operation(s) for results.
  name: Bureau of Reclamation Results API
  slug: bureau-of-reclamation-results-api
artifact_total: 12
collections:
- collection_type: open
  name: Reclamation Information Sharing Environment (RISE) API
  slug: open-bureau-of-reclamation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-reclamation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-reclamation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usbr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-reclamation
- group: company
  title: ''
  type: Website
  url: https://www.usbr.gov
- group: start
  title: ''
  type: Portal
  url: https://data.usbr.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usbr.gov/privacy.html
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=usbr-gov
created: '2024-11-30'
description: Established in 1902, the Bureau of Reclamation is best known for the dams, powerplants, and canals it constructed in the 17 western states. These water projects led to homesteading and promoted the economic development of the West. Reclamation has constructed more than 600 dams and reservoirs including Hoover Dam on the Colorado River and Grand Coulee on the Columbia River.
finops:
- name: Bureau Of Reclamation Finops
  service_category: API
  slug: bureau-of-reclamation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-reclamation.png
layout: provider
modified: '2026-05-19'
name: Bureau of Reclamation
nav: Providers
network: true
overview: 'Bureau of Reclamation publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Locations API, Model Runs API, and 3 more. Tagged areas include Energy, Federal Government, Infrastructure, Water, and Hydrology.


  Bureau of Reclamation''s developer surface includes developer portal and 7 more developer resources.'
plans:
- name: Bureau Of Reclamation Plans Pricing
  plan_count: 3
  slug: bureau-of-reclamation-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Bureau Of Reclamation Rate Limits
  slug: bureau-of-reclamation-rate-limits
score:
  band: emerging
  composite: 25.7
  delta: -7.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 47.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.7
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
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-reclamation/refs/heads/main/screenshots/bureau-of-reclamation-2026-06-20T173820.png
security:
- kind: domain-security
  name: Bureau Of Reclamation Domain Security
  slug: bureau-of-reclamation-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: bureau-of-reclamation
tags:
- Energy
- Federal Government
- Infrastructure
- Water
- Hydrology
- Reservoirs
website: https://www.usbr.gov
---

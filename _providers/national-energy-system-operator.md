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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Energy System Operator Agentic Access
  operation_count: 9
  slug: national-energy-system-operator-agentic-access
  summary_line: 9 operations
api_count: 4
apis:
- description: Query tabular data with filters or PostgreSQL-style SQL.
  name: National Energy System Operator Datastore API
  slug: national-energy-system-operator-datastore-api
- description: Discovery endpoints for organizations, datasets, and tags.
  name: National Energy System Operator Discovery API
  slug: national-energy-system-operator-discovery-api
- description: Retrieve metadata for datasets and resources.
  name: National Energy System Operator Metadata API
  slug: national-energy-system-operator-metadata-api
- description: Search endpoints for datasets and resources.
  name: National Energy System Operator Search API
  slug: national-energy-system-operator-search-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NESO Data Portal Datastore API
  slug: open-national-energy-system-operator-datastore-api
- collection_type: open
  name: NESO Data Portal Datastore Discovery API
  slug: open-national-energy-system-operator-discovery-api
- collection_type: open
  name: NESO Data Portal Datastore Metadata API
  slug: open-national-energy-system-operator-metadata-api
- collection_type: open
  name: NESO Data Portal Datastore Search API
  slug: open-national-energy-system-operator-search-api
- collection_type: open
  name: NESO Data Portal API
  slug: open-national-energy-system-operator
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-energy-system-operator-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/national-energy-system-operator-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-energy-system-operator-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neso-energy
- group: company
  title: ''
  type: Website
  url: https://www.neso.energy/
- group: start
  title: ''
  type: Portal
  url: https://www.neso.energy/data-portal
- group: docs
  title: ''
  type: Documentation
  url: https://www.neso.energy/data-portal/api-guidance
created: '2026-03-16'
description: The National Energy System Operator (NESO) is the independent operator responsible for planning and operating Great Britain's electricity and gas networks. NESO publishes operational, market, and forecasting datasets through its Data Portal, which exposes a CKAN v3 API for programmatic access to energy system data including wind forecasts, demand predictions, balancing services, and transmission constraints.
finops:
- name: National Energy System Operator Finops
  service_category: API
  slug: national-energy-system-operator-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-energy-system-operator.png
layout: provider
modified: '2026-05-19'
name: National Energy System Operator
nav: Providers
network: true
overview: 'National Energy System Operator publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datastore API, Discovery API, Metadata API, and 1 more. Tagged areas include Energy, Electricity, Grid, Open Data, and United Kingdom.


  National Energy System Operator''s developer surface includes developer portal, documentation, and 5 more developer resources.'
plans:
- name: National Energy System Operator Plans Pricing
  plan_count: 3
  slug: national-energy-system-operator-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: National Energy System Operator Rate Limits
  slug: national-energy-system-operator-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.2
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
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-energy-system-operator/refs/heads/main/screenshots/national-energy-system-operator-2026-06-20T190011.png
security:
- kind: domain-security
  name: National Energy System Operator Domain Security
  slug: national-energy-system-operator-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: National Energy System Operator Vulnerability Disclosure
  slug: national-energy-system-operator-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: national-energy-system-operator
tags:
- Energy
- Electricity
- Grid
- Open Data
- United Kingdom
website: https://www.neso.energy/
---

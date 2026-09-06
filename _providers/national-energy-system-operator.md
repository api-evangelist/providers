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
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Energy System Operator Agentic Access
  operation_count: 9
  slug: national-energy-system-operator-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.neso.energy/api/3/action/
  baseurl_source: declared
  description: Query tabular data with filters or PostgreSQL-style SQL.
  name: National Energy System Operator Datastore API
  slug: national-energy-system-operator-datastore-api
- baseURL: https://api.neso.energy/api/3/action/
  baseurl_source: declared
  description: Discovery endpoints for organizations, datasets, and tags.
  name: National Energy System Operator Discovery API
  slug: national-energy-system-operator-discovery-api
- baseURL: https://api.neso.energy/api/3/action/
  baseurl_source: declared
  description: Retrieve metadata for datasets and resources.
  name: National Energy System Operator Metadata API
  slug: national-energy-system-operator-metadata-api
- baseURL: https://api.neso.energy/api/3/action/
  baseurl_source: declared
  description: Search endpoints for datasets and resources.
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
  composite: 23.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 23.3
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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

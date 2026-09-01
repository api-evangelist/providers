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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: CKAN API for Neolaiacampus Open Data, ~70 datasets.
  name: Neolaiacampus Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-neolaiacampus-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.neolaiacampus.eu
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-neolaiacampus-eu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-neolaiacampus-eu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-neolaiacampus-eu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://neolaiacampus.eu/feed/
created: '2026-06-07'
description: Neolaiacampus Open Data is a organization open-data portal running CKAN. It exposes the CKAN catalog API over approximately 70 datasets.
finops:
- name: Data Neolaiacampus Eu Finops
  service_category: ''
  slug: data-neolaiacampus-eu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-neolaiacampus-eu.png
layout: provider
modified: '2026-06-07'
name: Neolaiacampus Open Data
nav: Providers
network: true
overview: 'Neolaiacampus Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  Neolaiacampus Open Data''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Data Neolaiacampus Eu Plans Pricing
  plan_count: 0
  slug: data-neolaiacampus-eu-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Data Neolaiacampus Eu Rate Limits
  slug: data-neolaiacampus-eu-rate-limits
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-neolaiacampus-eu/refs/heads/main/screenshots/data-neolaiacampus-eu-2026-06-20T175556.png
security:
- kind: domain-security
  name: Data Neolaiacampus Eu Domain Security
  slug: data-neolaiacampus-eu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: data-neolaiacampus-eu
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- Europe
website: https://data.neolaiacampus.eu
---

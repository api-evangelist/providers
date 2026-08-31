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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: CKAN API for Maggioli Cloud Open Data, ~6,061 datasets.
  name: Maggioli Cloud Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-maggioli-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opendata.maggioli.cloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-maggioli-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-maggioli-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-maggioli-cloud-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Maggioli Cloud Open Data is a organization open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 6,061 datasets.
finops:
- name: Opendata Maggioli Cloud Finops
  service_category: ''
  slug: opendata-maggioli-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-maggioli-cloud.png
layout: provider
modified: '2026-06-07'
name: Maggioli Cloud Open Data
nav: Providers
network: true
overview: 'Maggioli Cloud Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  Maggioli Cloud Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Maggioli Cloud Plans Pricing
  plan_count: 0
  slug: opendata-maggioli-cloud-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Opendata Maggioli Cloud Rate Limits
  slug: opendata-maggioli-cloud-rate-limits
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-maggioli-cloud/refs/heads/main/screenshots/opendata-maggioli-cloud-2026-06-20T190943.png
security:
- kind: domain-security
  name: Opendata Maggioli Cloud Domain Security
  slug: opendata-maggioli-cloud-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opendata-maggioli-cloud
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- Italy
website: https://www.opendata.maggioli.cloud
---

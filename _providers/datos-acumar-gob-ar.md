---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'CKAN Action API for Datos Abiertos ACUMAR, a consistent JSON-over-HTTP interface over a catalog of 27 datasets. Standard actions include package_search, package_show, package_list, organization_list, '
  name: Datos Abiertos ACUMAR CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-acumar-gob-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.acumar.gob.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-acumar-gob-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-acumar-gob-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-acumar-gob-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Datos Abiertos ACUMAR is a government agency open-data portal for Argentina running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 27 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Acumar Gob Ar Finops
  service_category: Open Data
  slug: datos-acumar-gob-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-acumar-gob-ar.png
layout: provider
modified: '2026-06-04'
name: Datos Abiertos ACUMAR
nav: Providers
network: true
overview: 'Datos Abiertos ACUMAR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Datos Abiertos ACUMAR''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Acumar Gob Ar Plans Pricing
  plan_count: 1
  slug: datos-acumar-gob-ar-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Datos Acumar Gob Ar Rate Limits
  slug: datos-acumar-gob-ar-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-acumar-gob-ar/refs/heads/main/screenshots/datos-acumar-gob-ar-2026-06-20T175710.png
security:
- kind: domain-security
  name: Datos Acumar Gob Ar Domain Security
  slug: datos-acumar-gob-ar-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: datos-acumar-gob-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Argentina
website: https://datos.acumar.gob.ar
---

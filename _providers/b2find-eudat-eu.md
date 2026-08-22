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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: CKAN Action API for EUDAT B2FIND, a consistent JSON-over-HTTP interface over a catalog of 1,466,694 datasets. Standard actions include package_search, package_show, package_list, organization_list, gr
  name: EUDAT B2FIND CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/b2find-eudat-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://b2find.eudat.eu
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/b2find-eudat-eu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/b2find-eudat-eu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/b2find-eudat-eu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: EUDAT B2FIND is a organization open-data portal for European Union running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,466,694 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: B2Find Eudat Eu Finops
  service_category: Open Data
  slug: b2find-eudat-eu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/b2find-eudat-eu.png
layout: provider
modified: '2026-06-04'
name: EUDAT B2FIND
nav: Providers
network: true
overview: 'EUDAT B2FIND publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  EUDAT B2FIND''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: B2Find Eudat Eu Plans Pricing
  plan_count: 1
  slug: b2find-eudat-eu-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: B2Find Eudat Eu Rate Limits
  slug: b2find-eudat-eu-rate-limits
score:
  band: emerging
  composite: 15.7
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/b2find-eudat-eu/refs/heads/main/screenshots/b2find-eudat-eu-2026-06-20T172914.png
security:
- kind: domain-security
  name: B2Find Eudat Eu Domain Security
  slug: b2find-eudat-eu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: b2find-eudat-eu
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- European Union
website: https://b2find.eudat.eu
---

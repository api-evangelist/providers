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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: CKAN Action API for open NRW, a consistent JSON-over-HTTP interface over a catalog of 10,579 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_lis
  name: open NRW CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-nrw-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-nrw-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open.nrw
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/open-nrw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-nrw-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-nrw-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: open NRW is a open data portal open-data portal for Germany running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 10,579 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Open Nrw Finops
  service_category: Open Data
  slug: open-nrw-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-nrw.png
layout: provider
modified: '2026-06-04'
name: open NRW
nav: Providers
network: true
overview: 'open NRW publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  open NRW''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Open Nrw Plans Pricing
  plan_count: 1
  slug: open-nrw-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Open Nrw Rate Limits
  slug: open-nrw-rate-limits
score:
  band: emerging
  composite: 17.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-nrw/refs/heads/main/screenshots/open-nrw-2026-06-20T190846.png
security:
- kind: domain-security
  name: Open Nrw Domain Security
  slug: open-nrw-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Open Nrw Vulnerability Disclosure
  slug: open-nrw-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-nrw
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Germany
website: https://open.nrw
---

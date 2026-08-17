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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: CKAN Action API for UK Government Open Data, a consistent JSON-over-HTTP interface over a catalog of 57,791 datasets. Standard actions include package_search, package_show, package_list, organization_
  name: UK Government Open Data CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-gov-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.data.gov.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-gov-uk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-gov-uk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-gov-uk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: UK Government Open Data is a national government open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 57,791 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Gov Uk Finops
  service_category: Open Data
  slug: data-gov-uk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-uk.png
layout: provider
modified: '2026-06-07'
name: UK Government Open Data
nav: Providers
network: true
overview: 'UK Government Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  UK Government Open Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Data Gov Uk Plans Pricing
  plan_count: 1
  slug: data-gov-uk-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Data Gov Uk Rate Limits
  slug: data-gov-uk-rate-limits
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
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-uk/refs/heads/main/screenshots/data-gov-uk-2026-06-20T175540.png
security:
- kind: domain-security
  name: Data Gov Uk Domain Security
  slug: data-gov-uk-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Data Gov Uk Vulnerability Disclosure
  slug: data-gov-uk-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: data-gov-uk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- United Kingdom
website: https://www.data.gov.uk
---

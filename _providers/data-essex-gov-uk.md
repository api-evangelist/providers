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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: CKAN Action API for Essex Open Data, a consistent JSON-over-HTTP interface over a catalog of an open datasets. Standard actions include package_search, package_show, package_list, organization_list, g
  name: Essex Open Data CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-essex-gov-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-essex-gov-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.essex.gov.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-essex-gov-uk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-essex-gov-uk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-essex-gov-uk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Essex Open Data is a local council open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately an open datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Essex Gov Uk Finops
  service_category: Open Data
  slug: data-essex-gov-uk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-essex-gov-uk.png
layout: provider
modified: '2026-06-04'
name: Essex Open Data
nav: Providers
network: true
overview: 'Essex Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Essex Open Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Data Essex Gov Uk Plans Pricing
  plan_count: 1
  slug: data-essex-gov-uk-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Data Essex Gov Uk Rate Limits
  slug: data-essex-gov-uk-rate-limits
score:
  band: emerging
  composite: 17.9
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-essex-gov-uk/refs/heads/main/screenshots/data-essex-gov-uk-2026-06-20T175526.png
security:
- kind: domain-security
  name: Data Essex Gov Uk Domain Security
  slug: data-essex-gov-uk-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Data Essex Gov Uk Vulnerability Disclosure
  slug: data-essex-gov-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: data-essex-gov-uk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Local Council
- United Kingdom
website: https://data.essex.gov.uk
---

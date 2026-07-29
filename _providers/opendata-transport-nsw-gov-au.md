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
- description: CKAN Action API for Transport for NSW Open Data Hub, a consistent JSON-over-HTTP interface over a catalog of 230 datasets. Standard actions include package_search, package_show, package_list, organiza
  name: Transport for NSW Open Data Hub CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opendata-transport-nsw-gov-au-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-transport-nsw-gov-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.transport.nsw.gov.au
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-transport-nsw-gov-au-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-transport-nsw-gov-au-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-transport-nsw-gov-au-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://opendata.transport.nsw.gov.au/blog
created: '2026-06-04'
description: Transport for NSW Open Data Hub is a open data portal open-data portal for Australia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 230 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Transport Nsw Gov Au Finops
  service_category: Open Data
  slug: opendata-transport-nsw-gov-au-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-transport-nsw-gov-au.png
layout: provider
modified: '2026-06-04'
name: Transport for NSW Open Data Hub
nav: Providers
network: true
overview: 'Transport for NSW Open Data Hub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Transport for NSW Open Data Hub''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Opendata Transport Nsw Gov Au Plans Pricing
  plan_count: 1
  slug: opendata-transport-nsw-gov-au-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Opendata Transport Nsw Gov Au Rate Limits
  slug: opendata-transport-nsw-gov-au-rate-limits
score:
  band: emerging
  composite: 18.3
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-transport-nsw-gov-au/refs/heads/main/screenshots/opendata-transport-nsw-gov-au-2026-06-20T190950.png
security:
- kind: domain-security
  name: Opendata Transport Nsw Gov Au Domain Security
  slug: opendata-transport-nsw-gov-au-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Opendata Transport Nsw Gov Au Vulnerability Disclosure
  slug: opendata-transport-nsw-gov-au-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: opendata-transport-nsw-gov-au
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Australia
website: https://opendata.transport.nsw.gov.au
---

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
- description: CKAN Action API for California Natural Resources Agency, a consistent JSON-over-HTTP interface over a catalog of 21,080 datasets. Standard actions include package_search, package_show, package_list, o
  name: California Natural Resources Agency CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-cnra-ca-gov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-cnra-ca-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.cnra.ca.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-cnra-ca-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-cnra-ca-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-cnra-ca-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: California Natural Resources Agency is a state government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 21,080 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Cnra Ca Gov Finops
  service_category: Open Data
  slug: data-cnra-ca-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-cnra-ca-gov.png
layout: provider
modified: '2026-06-04'
name: California Natural Resources Agency
nav: Providers
network: true
overview: 'California Natural Resources Agency publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  California Natural Resources Agency''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Data Cnra Ca Gov Plans Pricing
  plan_count: 1
  slug: data-cnra-ca-gov-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 1
  name: Data Cnra Ca Gov Rate Limits
  slug: data-cnra-ca-gov-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/data-cnra-ca-gov/refs/heads/main/screenshots/data-cnra-ca-gov-2026-06-20T175519.png
security:
- kind: domain-security
  name: Data Cnra Ca Gov Domain Security
  slug: data-cnra-ca-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Data Cnra Ca Gov Vulnerability Disclosure
  slug: data-cnra-ca-gov-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: data-cnra-ca-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State Government
- United States
website: https://data.cnra.ca.gov
---

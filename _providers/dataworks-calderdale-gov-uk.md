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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: CKAN Action API for Calderdale Data Works, a consistent JSON-over-HTTP interface over a catalog of an open datasets. Standard actions include package_search, package_show, package_list, organization_l
  name: Calderdale Data Works CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dataworks-calderdale-gov-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dataworks-calderdale-gov-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataworks.calderdale.gov.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dataworks-calderdale-gov-uk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dataworks-calderdale-gov-uk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dataworks-calderdale-gov-uk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Calderdale Data Works is a local council open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately an open datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dataworks Calderdale Gov Uk Finops
  service_category: Open Data
  slug: dataworks-calderdale-gov-uk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dataworks-calderdale-gov-uk.png
layout: provider
modified: '2026-06-04'
name: Calderdale Data Works
nav: Providers
network: true
overview: 'Calderdale Data Works publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Calderdale Data Works'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Dataworks Calderdale Gov Uk Plans Pricing
  plan_count: 1
  slug: dataworks-calderdale-gov-uk-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 1
  name: Dataworks Calderdale Gov Uk Rate Limits
  slug: dataworks-calderdale-gov-uk-rate-limits
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
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dataworks-calderdale-gov-uk/refs/heads/main/screenshots/dataworks-calderdale-gov-uk-2026-06-20T175653.png
security:
- kind: domain-security
  name: Dataworks Calderdale Gov Uk Domain Security
  slug: dataworks-calderdale-gov-uk-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dataworks Calderdale Gov Uk Vulnerability Disclosure
  slug: dataworks-calderdale-gov-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dataworks-calderdale-gov-uk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Local Council
- United Kingdom
website: https://dataworks.calderdale.gov.uk
---

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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: CKAN Action API for NSW Government Open Data, a consistent JSON-over-HTTP interface over a catalog of 16,907 datasets. Standard actions include package_search, package_show, package_list, organization
  name: NSW Government Open Data CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-nsw-gov-au-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-nsw-gov-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.nsw.gov.au/data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-nsw-gov-au-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-nsw-gov-au-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-nsw-gov-au-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: NSW Government Open Data is a state government open-data portal for Australia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 16,907 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Nsw Gov Au Finops
  service_category: Open Data
  slug: data-nsw-gov-au-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-nsw-gov-au.png
layout: provider
modified: '2026-06-04'
name: NSW Government Open Data
nav: Providers
network: true
overview: 'NSW Government Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  NSW Government Open Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Data Nsw Gov Au Plans Pricing
  plan_count: 1
  slug: data-nsw-gov-au-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Data Nsw Gov Au Rate Limits
  slug: data-nsw-gov-au-rate-limits
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 17.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-nsw-gov-au/refs/heads/main/screenshots/data-nsw-gov-au-2026-06-20T175600.png
security:
- kind: domain-security
  name: Data Nsw Gov Au Domain Security
  slug: data-nsw-gov-au-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Data Nsw Gov Au Vulnerability Disclosure
  slug: data-nsw-gov-au-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: data-nsw-gov-au
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- Australia
website: https://data.nsw.gov.au/data
---

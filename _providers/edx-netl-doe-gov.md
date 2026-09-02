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
- description: CKAN Action API for DOE NETL Energy Data Exchange, a consistent JSON-over-HTTP interface over a catalog of 17,982 datasets. Standard actions include package_search, package_show, package_list, organiz
  name: DOE NETL Energy Data Exchange CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edx-netl-doe-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edx.netl.doe.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/edx-netl-doe-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edx-netl-doe-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/edx-netl-doe-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: DOE NETL Energy Data Exchange is a federal government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 17,982 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Edx Netl Doe Gov Finops
  service_category: Open Data
  slug: edx-netl-doe-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edx-netl-doe-gov.png
layout: provider
modified: '2026-06-04'
name: DOE NETL Energy Data Exchange
nav: Providers
network: true
overview: 'DOE NETL Energy Data Exchange publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  DOE NETL Energy Data Exchange''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Edx Netl Doe Gov Plans Pricing
  plan_count: 1
  slug: edx-netl-doe-gov-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Edx Netl Doe Gov Rate Limits
  slug: edx-netl-doe-gov-rate-limits
score:
  band: emerging
  composite: 15.7
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
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edx-netl-doe-gov/refs/heads/main/screenshots/edx-netl-doe-gov-2026-06-20T180504.png
security:
- kind: domain-security
  name: Edx Netl Doe Gov Domain Security
  slug: edx-netl-doe-gov-domain-security
  summary_line: DNSSEC · DMARC
slug: edx-netl-doe-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Federal-Government
- United States
website: https://edx.netl.doe.gov
---

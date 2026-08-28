---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: CKAN Action API for dataset.gov.md, a consistent JSON-over-HTTP interface over a catalog of roughly 1,275 datasets. Standard actions include package_search, package_show, package_list, organization_li
  name: dataset.gov.md CKAN Action API
  slug: catalog
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dataset-gov-md-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataset.gov.md/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/2.10/api/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: dataset.gov.md is the national government open-data catalog for the Republic of Moldova (Portalul Datelor Deschise). The landing portal at date.gov.md links out to this catalog, which runs CKAN 2.10.4 and exposes the standard CKAN Action API over approximately 1,275 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. No API key is required for read endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dataset-gov-md.png
layout: provider
modified: '2026-06-23'
name: dataset.gov.md (Portalul Datelor Deschise)
nav: Providers
network: true
overview: 'dataset.gov.md (Portalul Datelor Deschise) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  dataset.gov.md (Portalul Datelor Deschise)''s developer surface includes documentation and 3 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dataset-gov-md/refs/heads/main/screenshots/dataset-gov-md-2026-07-25T211354.png
security:
- kind: domain-security
  name: Dataset Gov Md Domain Security
  slug: dataset-gov-md-domain-security
  summary_line: TLSv1.2 · HSTS
slug: dataset-gov-md
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Moldova
- Europe
website: https://dataset.gov.md/
---

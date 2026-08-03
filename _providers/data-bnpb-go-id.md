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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: CKAN Action API for Satu Data Bencana Indonesia (BNPB), a consistent JSON-over-HTTP interface over a catalog of 2,830 datasets. Standard actions include package_search, package_show, package_list, org
  name: Satu Data Bencana Indonesia (BNPB) CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-bnpb-go-id-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.bnpb.go.id
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-bnpb-go-id-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-bnpb-go-id-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-bnpb-go-id-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Satu Data Bencana Indonesia (BNPB) is a government agency open-data portal for Indonesia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 2,830 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Bnpb Go Id Finops
  service_category: Open Data
  slug: data-bnpb-go-id-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-bnpb-go-id.png
layout: provider
modified: '2026-06-04'
name: Satu Data Bencana Indonesia (BNPB)
nav: Providers
network: true
overview: 'Satu Data Bencana Indonesia (BNPB) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Satu Data Bencana Indonesia (BNPB)''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Bnpb Go Id Plans Pricing
  plan_count: 1
  slug: data-bnpb-go-id-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 1
  name: Data Bnpb Go Id Rate Limits
  slug: data-bnpb-go-id-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
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
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-bnpb-go-id/refs/heads/main/screenshots/data-bnpb-go-id-2026-06-20T175522.png
security:
- kind: domain-security
  name: Data Bnpb Go Id Domain Security
  slug: data-bnpb-go-id-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: data-bnpb-go-id
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Indonesia
website: https://data.bnpb.go.id
---

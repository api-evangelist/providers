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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: CKAN Action API for Donnees Quebec, a consistent JSON-over-HTTP interface over a catalog of 1,608 datasets. Standard actions include package_search, package_show, package_list, organization_list, grou
  name: Donnees Quebec CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donneesquebec-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.donneesquebec.ca
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/donneesquebec-ca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/donneesquebec-ca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/donneesquebec-ca-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.donneesquebec.ca/feed/
created: '2026-06-04'
description: Donnees Quebec is a provincial government open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,608 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Donneesquebec Ca Finops
  service_category: Open Data
  slug: donneesquebec-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donneesquebec-ca.png
layout: provider
modified: '2026-06-04'
name: Donnees Quebec
nav: Providers
network: true
overview: 'Donnees Quebec publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Donnees Quebec''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Donneesquebec Ca Plans Pricing
  plan_count: 1
  slug: donneesquebec-ca-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Donneesquebec Ca Rate Limits
  slug: donneesquebec-ca-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/donneesquebec-ca/refs/heads/main/screenshots/donneesquebec-ca-2026-06-20T180149.png
security:
- kind: domain-security
  name: Donneesquebec Ca Domain Security
  slug: donneesquebec-ca-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: donneesquebec-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Provincial Government
- Canada
website: https://www.donneesquebec.ca
---

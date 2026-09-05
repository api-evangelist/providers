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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: CKAN Action API for Yukon Open Data, a consistent JSON-over-HTTP interface over a catalog of 3,773 datasets. Standard actions include package_search, package_show, package_list, organization_list, gro
  name: Yukon Open Data CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-yukon-ca-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-yukon-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open.yukon.ca
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/open-yukon-ca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-yukon-ca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-yukon-ca-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Yukon Open Data is a territorial government open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 3,773 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Open Yukon Ca Finops
  service_category: Open Data
  slug: open-yukon-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-yukon-ca.png
layout: provider
modified: '2026-06-04'
name: Yukon Open Data
nav: Providers
network: true
overview: 'Yukon Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Yukon Open Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Open Yukon Ca Plans Pricing
  plan_count: 1
  slug: open-yukon-ca-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Open Yukon Ca Rate Limits
  slug: open-yukon-ca-rate-limits
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-yukon-ca/refs/heads/main/screenshots/open-yukon-ca-2026-06-20T190859.png
security:
- kind: domain-security
  name: Open Yukon Ca Domain Security
  slug: open-yukon-ca-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Open Yukon Ca Vulnerability Disclosure
  slug: open-yukon-ca-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-yukon-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Territorial Government
- Canada
website: https://open.yukon.ca
---

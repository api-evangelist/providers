---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: The Environmental Conservation Online System (ECOS) is the USFWS portal for threatened and endangered species data, critical habitat designations, recovery plans, and Section 7 consultations. ECOS exp
  name: USFWS Environmental Conservation Online System (ECOS)
  slug: ecos
- description: The Service Catalog (ServCat) is the USFWS reference library for reports, datasets, and other documents produced by or for the agency. ServCat is backed by an internal services layer; while the catalo
  name: USFWS Service Catalog (ServCat)
  slug: servcat
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fish-and-wildlife-service/refs/heads/main/plans/fish-and-wildlife-service-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fish-and-wildlife-service-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fish-and-wildlife-service/refs/heads/main/rate-limits/fish-and-wildlife-service-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fish-and-wildlife-service-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fish-and-wildlife-service/refs/heads/main/finops/fish-and-wildlife-service-finops.yml
  title: ''
  type: FinOps
  url: finops/fish-and-wildlife-service-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.fws.gov/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fws.gov/news/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fish-and-wildlife-service/refs/heads/main/security/fish-and-wildlife-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fish-and-wildlife-service-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USFWS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usfws
- group: company
  title: ''
  type: Website
  url: https://www.fws.gov
- group: other
  title: ''
  type: Data
  url: https://www.fws.gov/library/collections/data
- group: other
  title: ''
  type: ECOS
  url: https://ecos.fws.gov/ecp/
- group: other
  title: ''
  type: IPaC
  url: https://ipac.ecosphere.fws.gov/
- group: other
  title: ''
  type: ServCat
  url: https://ecos.fws.gov/ServCat/
created: '2024-12-03'
description: The U.S. Fish and Wildlife Service (USFWS) is the federal agency responsible for conserving, protecting, and enhancing fish, wildlife, plants, and their habitats for the continuing benefit of the American people. USFWS programs cover migratory birds, endangered species, interjurisdictional fish and marine mammals, and inland sport fisheries. Public-facing data is shared primarily through web tools and downloadable datasets such as the Environmental Conservation Online System (ECOS), Information for Planning and Consultation (IPaC), and the Service Catalog (ServCat) rather than a consolidated public API program.
finops:
- has_sources: false
  method: generated
  name: Fish And Wildlife Service Finops
  primary_unit: ''
  service_category: API
  slug: fish-and-wildlife-service-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fish-and-wildlife-service.png
layout: provider
modified: '2026-10-06'
name: U.S. Fish and Wildlife Service
nav: Providers
network: true
overview: 'U.S. Fish and Wildlife Service is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Conservation, Endangered Species, Federal Government, Fisheries, and Wildlife.


  U.S. Fish and Wildlife Service''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Fish And Wildlife Service Plans Pricing
  plan_count: 3
  slug: fish-and-wildlife-service-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Fish And Wildlife Service Rate Limits
  slug: fish-and-wildlife-service-rate-limits
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/fish-and-wildlife-service/refs/heads/main/screenshots/fish-and-wildlife-service-2026-06-20T181254.png
security:
- kind: domain-security
  name: Fish And Wildlife Service Domain Security
  slug: fish-and-wildlife-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fish-and-wildlife-service
tags:
- Conservation
- Endangered Species
- Federal Government
- Fisheries
- Wildlife
website: https://www.fws.gov
---

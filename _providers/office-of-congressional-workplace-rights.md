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
api_count: 1
apis:
- description: Office of Congressional Workplace Rights. The mission of the Office of Congressional Workplace Rights is to advance workplace rights, safety and health, and accessibility in the legislative branch. Su
  name: Office of Congressional Workplace Rights
  slug: office-of-congressional-workplace-rights
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/office-of-congressional-workplace-rights/refs/heads/main/plans/office-of-congressional-workplace-rights-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/office-of-congressional-workplace-rights-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/office-of-congressional-workplace-rights/refs/heads/main/rate-limits/office-of-congressional-workplace-rights-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/office-of-congressional-workplace-rights-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/office-of-congressional-workplace-rights/refs/heads/main/finops/office-of-congressional-workplace-rights-finops.yml
  title: ''
  type: FinOps
  url: finops/office-of-congressional-workplace-rights-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ocwr.gov/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ocwr.gov/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/office-of-congressional-workplace-rights/refs/heads/main/security/office-of-congressional-workplace-rights-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/office-of-congressional-workplace-rights-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ocwr
created: '2024-12-03'
description: The Office of Congressional Workplace Rights is responsible for enforcing workplace rights for employees of the United States Congress. This includes overseeing the administration of laws such as the Congressional Accountability Act, which guarantees certain rights and protections for congressional staff members.
finops:
- has_sources: false
  method: generated
  name: Office Of Congressional Workplace Rights Finops
  primary_unit: ''
  service_category: API
  slug: office-of-congressional-workplace-rights-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/office-of-congressional-workplace-rights.png
layout: provider
modified: '2026-10-06'
name: Office of Congressional Workplace Rights
nav: Providers
network: true
overview: 'Office of Congressional Workplace Rights is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government.


  Office of Congressional Workplace Rights'' developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Office Of Congressional Workplace Rights Plans Pricing
  plan_count: 3
  slug: office-of-congressional-workplace-rights-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Office Of Congressional Workplace Rights Rate Limits
  slug: office-of-congressional-workplace-rights-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/office-of-congressional-workplace-rights/refs/heads/main/screenshots/office-of-congressional-workplace-rights-2026-06-20T190637.png
security:
- kind: domain-security
  name: Office Of Congressional Workplace Rights Domain Security
  slug: office-of-congressional-workplace-rights-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: office-of-congressional-workplace-rights
tags:
- Federal Government
---

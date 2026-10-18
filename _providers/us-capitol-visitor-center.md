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
- description: The US Capitol Visitor Center provides visitor information, guided tours, educational programs, and specialty tours of the United States Capitol building. While no public developer API is available, t
  name: US Capitol Visitor Center
  provenance: unpublished
  slug: us-capitol-visitor-center
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/us-capitol-visitor-center/refs/heads/main/plans/us-capitol-visitor-center-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/us-capitol-visitor-center-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/us-capitol-visitor-center/refs/heads/main/rate-limits/us-capitol-visitor-center-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/us-capitol-visitor-center-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/us-capitol-visitor-center/refs/heads/main/finops/us-capitol-visitor-center-finops.yml
  title: ''
  type: FinOps
  url: finops/us-capitol-visitor-center-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.visitthecapitol.gov/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/us-capitol-visitor-center/refs/heads/main/security/us-capitol-visitor-center-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/us-capitol-visitor-center-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-capitol-visitor-center
created: '2024-12-03'
description: The US Capitol Visitor Center (CVC) serves as the main entrance for visitors to the United States Capitol, providing resources and information to enhance the visitor experience. The Center offers guided tours of the Capitol building, allowing visitors to explore the historic rooms and learn about the legislative process. It also houses exhibits and educational materials that highlight the history and significance of the Capitol and its role in American democracy. The CVC operates under the Architect of the Capitol and offers free guided tours, specialty tours, virtual tours, and educational programs for students and visitors from around the world.
finops:
- has_sources: false
  method: generated
  name: Us Capitol Visitor Center Finops
  primary_unit: ''
  service_category: API
  slug: us-capitol-visitor-center-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-capitol-visitor-center.png
jsonld:
- class_count: 4
  name: Us Capitol Visitor Center Context
  property_count: 26
  slug: us-capitol-visitor-center-context
layout: provider
modified: '2026-10-06'
name: US Capitol Visitor Center
nav: Providers
network: true
overview: 'US Capitol Visitor Center publishes no API. The 1 entry listed on the [APIs.io](https://apis.io/) network are product areas recorded for completeness, each marked as not an API. Tagged areas include Federal Government, Legislative Branch, Tourism, Education, and US Capitol.


  The US Capitol Visitor Center catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Us Capitol Visitor Center Plans Pricing
  plan_count: 3
  slug: us-capitol-visitor-center-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Us Capitol Visitor Center Rate Limits
  slug: us-capitol-visitor-center-rate-limits
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/us-capitol-visitor-center/refs/heads/main/screenshots/us-capitol-visitor-center-2026-06-20T200616.png
security:
- kind: domain-security
  name: Us Capitol Visitor Center Domain Security
  slug: us-capitol-visitor-center-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: us-capitol-visitor-center
tags:
- Federal Government
- Legislative Branch
- Tourism
- Education
- US Capitol
---

---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Power your digital workflows using comprehensive property and location intelligence data from LightBox.
  name: LightBox
  slug: lightbox
- baseURL: https://api.lightboxre.com/v1
  baseurl_source: declared
  description: Zoning lookups by parcel, address, or geometry
  name: LightBox Zoning API
  slug: lightbox-zoning-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/lightbox/plans/lightbox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lightbox-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lightbox/rate-limits/lightbox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lightbox-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lightbox/finops/lightbox-finops.yml
  title: ''
  type: FinOps
  url: finops/lightbox-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lightboxre.com/insights/
- group: company
  title: ''
  type: Website
  url: https://lightboxre.com
- group: auth
  href: https://artifacts.apis.io/lightbox/security/lightbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lightbox-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightbox-re
created: '2025-02-17'
description: Power your digital workflows using comprehensive property and location intelligence data from LightBox.
finops:
- has_sources: false
  method: generated
  name: Lightbox Finops
  primary_unit: request
  service_category: API
  slug: lightbox-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightbox.png
layout: provider
modified: '2026-10-06'
name: LightBox
nav: Providers
network: true
overview: 'LightBox publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Zoning API, and 1 more. Tagged areas include Location Intelligence, Property Data, and Real Estate.


  The LightBox catalog on APIs.io includes 1 Spectral governance ruleset.


  LightBox''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Lightbox Plans Pricing
  plan_count: 3
  slug: lightbox-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Lightbox Rate Limits
  slug: lightbox-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: LightBox API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: lightbox-rules
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.5
    catalog_earned_first_party: 0.0
    catalog_gap: 82.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 45.3
    developer_ergonomics: 21.4
    discoverability: 39.3
    operational_transparency: 7.9
  previous_composite: 21.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lightbox/lightbox-2026-06-20T184513.png
security:
- kind: domain-security
  name: Lightbox Domain Security
  slug: lightbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightbox
tags:
- Location Intelligence
- Property Data
- Real Estate
website: https://lightboxre.com
---

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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Hitachi Construction Machinery Telematics API provides operational data about construction equipment including location, fuel consumption, operating hours, and diagnostic information, compliant wi
  name: Hitachi Construction Machinery Telematics API
  slug: telematics-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: Security
  url: https://www.hitachicm.com/global/en/vulnerability-disclosure-policy/
- group: auth
  href: https://artifacts.apis.io/hitachi-construction-machinery/security/hitachi-construction-machinery-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hitachi-construction-machinery-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/hitachi-construction-machinery/conformance/hitachi-construction-machinery-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hitachi-construction-machinery-conformance.yml
- group: other
  href: https://artifacts.apis.io/hitachi-construction-machinery/hosts/hitachi-construction-machinery-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hitachi-construction-machinery-hosts.yml
- group: other
  href: https://artifacts.apis.io/hitachi-construction-machinery/vendors/hitachi-construction-machinery-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hitachi-construction-machinery-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.hitachicm.com/global/en/news/
- group: commercial
  href: https://artifacts.apis.io/hitachi-construction-machinery/plans/hitachi-construction-machinery-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hitachi-construction-machinery-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/hitachi-construction-machinery/finops/hitachi-construction-machinery-finops.yml
  title: ''
  type: FinOps
  url: finops/hitachi-construction-machinery-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hitachicm.com/global/en/news/
- group: auth
  href: https://artifacts.apis.io/hitachi-construction-machinery/security/hitachi-construction-machinery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hitachi-construction-machinery-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hitachi-construction-machinery
- group: company
  title: ''
  type: Website
  url: https://www.hitachicm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hitachicm.com/global/en/solutions/telematics-api/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hitachicm.com/global/en/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hitachicm.com/global/en/termofuse/
- group: operate
  title: ''
  type: Support
  url: https://www.hitachicm.com/global/en/contact-us/
coverage:
  checked: '2026-10-20'
  detail: The Telematics API (ISO 15143-3 / AEMP 2.0) page publishes no reference or contract and directs owners to contact their Hitachi dealer for models, data elements and regions; api.hitachicm.com does not resolve.
  evidence:
  - status: 200
    url: https://www.hitachicm.com/global/en/solutions/telematics-api/
  reason: customer-only-docs
  state: gated
created: '2025-02-12'
description: Hitachi Construction Machinery provides operational data about machines and equipment on construction sites through the Telematics API, which complies with the ISO 15143-3 (AEMP 2.0) standard. The API enables higher efficiency, productivity, and safety while reducing life cycle costs. API access, data elements and supported regions are arranged through Hitachi dealers; no public API reference or machine-readable contract is published.
finops:
- has_sources: false
  method: generated
  name: Hitachi Construction Machinery Finops
  primary_unit: request
  service_category: API
  slug: hitachi-construction-machinery-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hitachi-construction-machinery.png
layout: provider
modified: '2026-10-06'
name: Hitachi Construction Machinery
nav: Providers
network: true
overview: 'Hitachi Construction Machinery is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Equipment, IoT, ISO 15143-3, and Telematics.


  Hitachi Construction Machinery''s developer surface includes engineering blog, documentation, support, and 13 more developer resources.'
plans:
- name: Hitachi Construction Machinery Plans Pricing
  plan_count: 0
  slug: hitachi-construction-machinery-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Hitachi Construction Machinery Rate Limits
  slug: hitachi-construction-machinery-rate-limits
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 10.5
  previous_composite: 18.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hitachi-construction-machinery/hitachi-construction-machinery-2026-10-11T190532.png
security:
- kind: domain-security
  name: Hitachi Construction Machinery Domain Security
  slug: hitachi-construction-machinery-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Hitachi Construction Machinery Vulnerability Disclosure
  slug: hitachi-construction-machinery-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hitachi-construction-machinery
tags:
- Construction
- Equipment
- IoT
- ISO 15143-3
- Telematics
- Heavy Equipment
website: https://www.hitachicm.com/
---

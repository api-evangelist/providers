---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/spiras-health/hosts/spiras-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spiras-health-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spirashealth.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://spirashealth.com/news/
- group: company
  title: ''
  type: Blog
  url: https://spirashealth.com/blog/
- group: auth
  href: https://artifacts.apis.io/spiras-health/security/spiras-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spiras-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spirashealth.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://spirashealth.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Spiras Health offers a nurse practitioner‑led program that delivers 36 home‑based touchpoints each year for members with complex chronic conditions such as CHF, hypertension, diabetes, and COPD. The service is aimed at health plans, providers, and patients to increase access to care, reduce emergency‑room and hospital utilization, and improve health outcomes.
image: https://spirashealth.com/wp-content/uploads/2023/11/spiras_health_female_nurse_female_patient_cane_home_couch.webp
layout: provider
modified: '2026-10-26'
name: Spiras Health
nav: Providers
network: true
overview: 'Spiras Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Home-based care, Nurse practitioner services, Health Plans, and Patient Services.


  Spiras Health''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 40.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spiras-health/spiras-health-2026-11-03T143637.png
security:
- kind: domain-security
  name: Spiras Health Domain Security
  slug: spiras-health-domain-security
  summary_line: TLSv1.2 · DMARC
slug: spiras-health
tags:
- Home-based care
- Nurse practitioner services
- Health Plans
- Patient Services
website: https://spirashealth.com/
---

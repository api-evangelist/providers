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
  href: https://artifacts.apis.io/carenation/hosts/carenation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carenation-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carenation.in/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carenation.in/privacy-policy.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.carenation.in/
- group: auth
  href: https://artifacts.apis.io/carenation/security/carenation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carenation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carenation.in
coverage:
  checked: '2026-10-07'
  detail: No public API documentation or machine‑readable specification was found on the provider's sites.
  evidence:
  - status: 200
    url: https://dev.carenation.in/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carenation is a scalable telehealth platform that enables complete remote care delivery. It provides virtual consultations, COVID‑19 home care programs, and a suite of digital health services across multiple countries including India, Spain, Greece, Peru, Bangladesh, Mexico, and Nepal. The platform is built to world‑class standards, offering patients and providers a comprehensive, secure, and user‑friendly experience for pediatric, adolescent, and adult care.
layout: provider
modified: '2026-10-07'
name: Carenation
nav: Providers
network: true
overview: 'Carenation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telehealth, Healthcare, Remote Care, Digital Health, and Platform.


  Carenation''s developer surface includes documentation and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 10.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/carenation/carenation-2026-11-03T123335.png
security:
- kind: domain-security
  name: Carenation Domain Security
  slug: carenation-domain-security
  summary_line: TLSv1.2
slug: carenation
tags:
- Telehealth
- Healthcare
- Remote Care
- Digital Health
- Platform
website: https://carenation.in
---

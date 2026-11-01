---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bestshotcare-com/hosts/bestshotcare-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestshotcare-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rescripted.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rescripted.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://rescripted.com/media/stories
- group: start
  title: ''
  type: Login
  url: https://rescripted.com/login
- group: auth
  href: https://artifacts.apis.io/bestshotcare-com/security/bestshotcare-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestshotcare-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestshotcare.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://bestshotcare.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Rescripted operates a holistic women’s health platform that delivers expert‑reviewed content and AI‑powered guidance through its Clara companion. It provides resources and personalized information for users across the lifecycle—from menstrual health and sexual health to fertility, pregnancy, and chronic conditions such as PCOS and endometriosis. The service targets women seeking comprehensive, science‑backed health insights and tools to manage their well‑being.
layout: provider
modified: '2026-10-24'
name: Rescripted
nav: Providers
network: true
overview: Rescripted is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Menstrual Health, Sexual Health, Fertility, Pregnancy, and Wellness.
random_paper: 19
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestshotcare Com Domain Security
  slug: bestshotcare-com-domain-security
  summary_line: TLSv1.3
slug: bestshotcare-com
tags:
- Menstrual Health
- Sexual Health
- Fertility
- Pregnancy
- Wellness
- AI Health Companion
- Health Platform
website: https://bestshotcare.com/
---

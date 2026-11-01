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
  href: https://artifacts.apis.io/lifestyleshealthcare-com/hosts/lifestyleshealthcare-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lifestyleshealthcare-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lifestyleshealthcare-com/vendors/lifestyleshealthcare-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lifestyleshealthcare-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lifestylesglobal.com/terms
- group: company
  title: ''
  type: Newsroom
  url: https://www.lifestylesglobal.com/Home/news
- group: auth
  href: https://artifacts.apis.io/lifestyleshealthcare-com/security/lifestyleshealthcare-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lifestyleshealthcare-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lifestylesglobal.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.lifestylesglobal.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: LifeStyles Healthcare is a health technology company focused on providing integrated digital health solutions, including telemedicine platforms, patient engagement tools, and data analytics services. The company aims to improve healthcare accessibility and outcomes through innovative software and services for providers and patients alike. It is backed by Hillhouse and part of a broader portfolio of health-focused ventures.
layout: provider
modified: '2026-10-22'
name: LifeStyles Healthcare
nav: Providers
network: true
overview: LifeStyles Healthcare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include HealthTech, Telemedicine, PatientEngagement, DataAnalytics, and DigitalHealth.
random_paper: 1
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lifestyleshealthcare Com Domain Security
  slug: lifestyleshealthcare-com-domain-security
  summary_line: TLSv1.3
slug: lifestyleshealthcare-com
tags:
- HealthTech
- Telemedicine
- PatientEngagement
- DataAnalytics
- DigitalHealth
- Company
website: https://www.lifestylesglobal.com
---

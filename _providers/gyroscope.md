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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/gyroscope/llms/gyroscope-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gyroscope-llms.txt
- group: other
  href: https://artifacts.apis.io/gyroscope/hosts/gyroscope-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gyroscope-hosts.yml
- group: other
  href: https://artifacts.apis.io/gyroscope/vendors/gyroscope-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gyroscope-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://gyrosco.pe/press/v8/
- group: start
  title: ''
  type: Login
  url: https://gyrosco.pe/signin/
- group: docs
  title: ''
  type: Documentation
  url: https://gyrosco.pe/guides/
- group: auth
  href: https://artifacts.apis.io/gyroscope/security/gyroscope-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gyroscope-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gyrosco.pe
- group: company
  title: ''
  type: Blog
  url: https://gyrosco.pe/blog/
- group: operate
  title: ''
  type: Support
  url: https://gyrosco.pe/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gyrosco.pe/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gyrosco.pe/terms/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://gyrosco.pe/api/mcp
  - status: 200
    url: https://gyrosco.pe
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Gyroscope is a personal health and life tracking platform offering AI‑driven coaching, nutrition, sleep, workout and health‑score monitoring. The app integrates data from wearables and manual entries to provide actionable insights and personalized recommendations.
image: https://media.gyrosco.pe/images/icons/app-icon-96.png
layout: provider
modified: '2026-10-24'
name: Gyroscope
nav: Providers
network: true
overview: 'Gyroscope is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Tracking, AI, and Wellness.


  Gyroscope''s developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gyroscope Domain Security
  slug: gyroscope-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gyroscope
tags:
- Company
- Health
- Tracking
- AI
- Wellness
website: https://gyrosco.pe
---

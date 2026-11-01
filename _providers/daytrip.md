---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Daytrip provides a platform for booking private transfers, day trips, and hourly drivers via its API.
  name: Daytrip API
  slug: daytrip-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/daytrip/llms/daytrip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daytrip-llms.txt
- group: agent
  href: https://artifacts.apis.io/daytrip/well-known/daytrip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daytrip-well-known.yml
- group: other
  href: https://artifacts.apis.io/daytrip/hosts/daytrip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daytrip-hosts.yml
- group: other
  href: https://artifacts.apis.io/daytrip/vendors/daytrip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daytrip-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daytrip.com/en/terms
- group: start
  title: ''
  type: SignUp
  url: https://daytrip.com/en/travel-agent/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daytrip.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://services.daytrip.com/press
- group: company
  title: ''
  type: Blog
  url: https://blog.daytrip.com
- group: auth
  href: https://artifacts.apis.io/daytrip/security/daytrip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daytrip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daytrip.com
coverage:
  checked: '2026-10-22'
  detail: Main website returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 202
    url: https://daytrip.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Daytrip provides a platform for booking private transfers, day trips, and hourly drivers. It offers an API that enables developers to integrate travel booking, pricing, and scheduling functionalities into their applications, catering to both B2C and B2B use cases across the travel and transportation industry.
image: https://images.daytrip.com/site/daytrip-og.jpg?w=1200&h=630
layout: provider
modified: '2026-10-22'
name: Daytrip
nav: Providers
network: true
overview: 'Daytrip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Transportation, Booking, and Platform.


  Daytrip''s developer surface includes signup flow, engineering blog, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Daytrip Domain Security
  slug: daytrip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: daytrip
tags:
- Travel
- Transportation
- Booking
- Platform
website: https://daytrip.com
---

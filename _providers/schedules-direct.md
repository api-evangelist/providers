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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/schedules-direct/hosts/schedules-direct-hosts.yml
  title: ''
  type: Hosts
  url: hosts/schedules-direct-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://schedulesdirect.org/news
- group: auth
  href: https://artifacts.apis.io/schedules-direct/security/schedules-direct-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/schedules-direct-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://schedulesdirect.org/
- group: docs
  title: ''
  type: Documentation
  url: https://schedulesdirect.org/aboutus
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/SchedulesDirect/JSON-Service/wiki/API-20141201
- group: commercial
  title: ''
  type: TermsOfService
  url: https://schedulesdirect.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://schedulesdirect.org/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://schedulesdirect.org/contact
- group: operate
  title: ''
  type: Forum
  url: https://forums.schedulesdirect.org/
- group: start
  title: ''
  type: SignUp
  url: https://schedulesdirect.org/signup
coverage:
  checked: '2026-10-28'
  detail: No public documentation host or machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found despite probing known hosts.
  evidence:
  - status: 200
    url: https://schedulesdirect.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Schedules Direct is a non‑profit organization dedicated to supporting open‑source software projects by providing TV listings data and funding. It offers membership, grants, and resources for developers of applications like MythTV and XMLTV, and aims to promote open‑source solutions in the media space. The service supplies data via XML SOAP and JSON APIs, and encourages community involvement through its programs and partnerships.
layout: provider
modified: '2026-10-28'
name: Schedules Direct
nav: Providers
network: true
overview: 'Schedules Direct is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nonprofit, OpenSource, TVListings, and Community.


  Schedules Direct''s developer surface includes documentation, API reference, support, signup flow, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.6
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
    developer_ergonomics: 21.4
    discoverability: 46.4
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
  name: Schedules Direct Domain Security
  slug: schedules-direct-domain-security
  summary_line: TLSv1.3 · DMARC
slug: schedules-direct
tags:
- Company
- Nonprofit
- OpenSource
- TVListings
- Community
website: https://schedulesdirect.org/
---

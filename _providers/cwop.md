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
- group: other
  href: https://artifacts.apis.io/cwop/hosts/cwop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cwop-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cwop/security/cwop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cwop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.wxqa.com/
- group: start
  title: ''
  type: GettingStarted
  url: http://www.wxqa.com/SIGN-UP.html
coverage:
  checked: '2026-10-28'
  detail: The CWOP website provides weather data but offers no developer program or API documentation.
  evidence:
  - status: 200
    url: http://www.wxqa.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: The Citizen Weather Observer Program (CWOP) is a public‑private partnership that collects weather observations contributed by citizen volunteers worldwide. It makes these data available to weather services, homeland security, and researchers, while providing contributors feedback on data quality. The program operates through the wxqa.com website, offering maps, station lists, data quality tools, and resources for weather enthusiasts and amateur radio operators.
layout: provider
modified: '2026-10-28'
name: Citizen Weather Observer Program
nav: Providers
network: true
overview: 'Citizen Weather Observer Program is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, CitizenScience, DataCollection, PublicPrivatePartnership, and Community.


  Citizen Weather Observer Program''s developer surface includes getting-started guide and 3 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cwop Domain Security
  slug: cwop-domain-security
  summary_line: no transport/DNS hardening detected
slug: cwop
tags:
- Weather
- CitizenScience
- DataCollection
- PublicPrivatePartnership
- Community
website: http://www.wxqa.com/
---

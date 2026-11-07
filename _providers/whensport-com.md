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
- group: agent
  href: https://artifacts.apis.io/whensport-com/llms/whensport-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whensport-com-llms.txt
- group: other
  href: https://artifacts.apis.io/whensport-com/hosts/whensport-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whensport-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/whensport-com/vendors/whensport-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whensport-com-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://whensport.com/events/polo-2026/team/bta
- group: auth
  href: https://artifacts.apis.io/whensport-com/security/whensport-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whensport-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whensport.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whensport.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whensport.com/terms
- group: operate
  title: ''
  type: Support
  url: https://whensport.com/contact
coverage:
  checked: '2026-10-29'
  detail: The site provides sports schedules but offers no public developer program or API documentation.
  evidence:
  - status: 404
    url: https://whensport.com/openapi.json
  - status: 0
    url: https://api.whensport.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: whensport.com provides live schedules for a wide range of sports events, automatically converting start times to the user's local timezone. Covering football, Formula 1, cricket, rugby, tennis, golf, horse racing, and many more, the platform aggregates official match times and presents them in an easy-to-read format, eliminating the need for manual timezone calculations. Users can browse events by sport, competition, or date, and access detailed information such as venue, participating teams, and live streaming links where available. The service aims to enhance fan engagement by ensuring that fans worldwide never miss a match due to timezone confusion.
image: https://whensport.com/og.png
layout: provider
modified: '2026-10-29'
name: whensport-com
nav: Providers
network: true
overview: 'whensport-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, LiveSchedules, TimezoneConversion, and Data.


  whensport-com''s developer surface includes support and 8 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 47.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/whensport-com/whensport-com-2026-11-03T150145.png
security:
- kind: domain-security
  name: Whensport Com Domain Security
  slug: whensport-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: whensport-com
tags:
- Sports
- LiveSchedules
- TimezoneConversion
- Data
website: https://whensport.com/
---

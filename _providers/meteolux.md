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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/meteolux/security/meteolux-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/meteolux-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/meteolux/hosts/meteolux-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meteolux-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.meteolux.lu/fr/rss/news
- group: auth
  href: https://artifacts.apis.io/meteolux/security/meteolux-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/meteolux-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/meteolux/security/meteolux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meteolux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meteolux.lu/
- group: docs
  title: ''
  type: Documentation
  url: https://www.meteolux.lu/fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.meteolux.lu/fr/aide/contact/
- group: operate
  title: ''
  type: Support
  url: https://www.meteolux.lu/fr/aide/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.meteolux.lu/fr/actualites/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but provide no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.meteolux.lu/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: MeteoLux provides comprehensive weather forecasting, climate monitoring, and meteorological data services for Luxembourg and the broader European region. Operating from Luxembourg, the company offers real-time observations, forecasts, aviation weather, and climate analyses through its online platform, serving both public and private sector needs.
layout: provider
modified: '2026-10-28'
name: MeteoLux
nav: Providers
network: true
overview: 'MeteoLux is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Forecast, Climate, and Luxembourg.


  MeteoLux''s developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 46.4
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Meteolux Domain Security
  slug: meteolux-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Meteolux Vulnerability Disclosure
  slug: meteolux-vulnerability-disclosure
  summary_line: no policy recorded
slug: meteolux
tags:
- Company
- Weather
- Forecast
- Climate
- Luxembourg
- Europe
website: https://meteolux.lu/
---

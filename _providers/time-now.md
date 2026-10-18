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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Developer API from Time.now — 4 operation(s) for developer.
  name: Time.now Developer API
  slug: time-now-developer-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/time-now/refs/heads/main/rules/time-now-rules.yml
  title: ''
  type: Spectral
  url: rules/time-now-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/time-now/refs/heads/main/conformance/time-now-conformance.yml
  title: ''
  type: Conformance
  url: conformance/time-now-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/time-now/refs/heads/main/hosts/time-now-hosts.yml
  title: ''
  type: Hosts
  url: hosts/time-now-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://time.now/info/terms-privacy
- group: start
  title: ''
  type: Login
  url: https://time.now/login/
- group: company
  title: ''
  type: Blog
  url: https://time.now/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/time-now/refs/heads/main/security/time-now-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/time-now-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://time.now
- group: docs
  title: ''
  type: Documentation
  url: https://time.now/developer
- group: start
  title: ''
  type: DeveloperPortal
  url: https://time.now/developer
- group: docs
  title: ''
  type: APIReference
  url: https://time.now/developer
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://time.now/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Time.now provides a simple, free World Time API delivering current date and time information for any timezone. The service returns JSON data with fields such as datetime, timezone, utc_offset, and day_of_week, enabling developers to integrate accurate time data into applications without managing their own time zone databases. The API is publicly accessible, supports CORS, and offers endpoints like /api/timezone/{area}/{location} for worldwide coverage.
image: https://time.now/static/time-now.png
layout: provider
modified: '2026-10-12'
name: Time.now
nav: Providers
network: true
overview: 'Time.now is listed with 1 API on the [APIs.io](https://apis.io/) network: Developer API. Tagged areas include World Time API, Developer Tools, IoT, Web Applications, and Timezone.


  The Time.now catalog on APIs.io includes 1 Spectral governance ruleset.


  Time.now''s developer surface includes engineering blog, documentation, API reference, and 8 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Time.now API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: time-now-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.6
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Time Now Domain Security
  slug: time-now-domain-security
  summary_line: TLSv1.3
slug: time-now
tags:
- World Time API
- Developer Tools
- IoT
- Web Applications
- Timezone
- Geolocation
website: https://time.now
---

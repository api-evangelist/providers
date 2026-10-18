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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/community-broadcasters/refs/heads/main/hosts/community-broadcasters-hosts.yml
  title: ''
  type: Hosts
  url: hosts/community-broadcasters-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://commbroadcasters.com/category/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/community-broadcasters/refs/heads/main/security/community-broadcasters-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/community-broadcasters-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://commbroadcasters.com/
coverage:
  checked: '2026-10-09'
  detail: OpenAPI spec endpoints returned 404 on both primary and API hosts, and no documentation host was identified.
  evidence:
  - status: 404
    url: https://commbroadcasters.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Community Broadcasters is a U.S.-based radio broadcasting group that owns and operates over 100 radio stations across multiple markets. Founded in 2006, the company combines traditional broadcasting with an in‑house full‑service advertising agency, MITTCOM, to offer omnichannel marketing solutions. Their portfolio includes stations in New York, South Carolina, and other regions, focusing on local community engagement and brand partnerships.
layout: provider
modified: '2026-10-09'
name: Community Broadcasters
nav: Providers
network: true
overview: 'Community Broadcasters is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Community Broadcasters'' developer surface includes engineering blog and 3 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 2.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Community Broadcasters Domain Security
  slug: community-broadcasters-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: community-broadcasters
tags:
- Company
website: https://commbroadcasters.com/
---

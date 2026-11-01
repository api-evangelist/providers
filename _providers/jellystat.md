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
api_count: 1
apis:
- description: Jellystat provides a free and open‑source analytics platform for Jellyfin media servers, offering detailed statistics via a web dashboard.
  name: Jellystat API
  slug: jellystat-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/jellystat/hosts/jellystat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jellystat-hosts.yml
- group: auth
  href: https://artifacts.apis.io/jellystat/security/jellystat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jellystat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jellystat.com
- group: docs
  title: ''
  type: Documentation
  url: https://jellystat.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://jellystat.com/new-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jellystat.com/tos
coverage:
  checked: '2026-10-28'
  detail: Documentation exists at https://jellystat.com/docs but provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://jellystat.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Jellystat provides a free and open‑source analytics platform for Jellyfin media servers, offering detailed statistics on library usage, user activity, watch history, and session monitoring. The service includes a web dashboard with visualizations of language distribution, referrers, and session trends, and it can be self‑hosted with a modern architecture using Node.js and optional PostgreSQL backend. It aims to give Jellyfin administrators clear insights into how their media libraries are consumed.
layout: provider
modified: '2026-10-28'
name: Jellystat
nav: Providers
network: true
overview: 'Jellystat is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, OpenSource, Media, and Jellyfin.


  Jellystat''s developer surface includes documentation, getting-started guide, and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Jellystat Domain Security
  slug: jellystat-domain-security
  summary_line: TLSv1.3
slug: jellystat
tags:
- Company
- Analytics
- OpenSource
- Media
- Jellyfin
website: https://jellystat.com
---

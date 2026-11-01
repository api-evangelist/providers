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
  href: https://artifacts.apis.io/cockos-reaper/hosts/cockos-reaper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cockos-reaper-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cockos-reaper/security/cockos-reaper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cockos-reaper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reaper.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://www.reaper.fm/userguide.php
- group: start
  title: ''
  type: GettingStarted
  url: https://www.reaper.fm/download.php
- group: operate
  title: ''
  type: Support
  url: https://forum.cockos.com/
- group: company
  title: ''
  type: Blog
  url: https://www.reaper.blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reaper.fm/purchase.php
coverage:
  checked: '2026-10-28'
  detail: Provider documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.reaper.fm/userguide.php
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: REAPER is a powerful digital audio workstation (DAW) developed by Cockos. It offers a full‑featured, flexible audio production environment used by professionals and hobbyists alike, supporting recording, editing, mixing, and mastering across Windows, macOS, and Linux. REAPER provides unlimited updates, a customizable interface, extensive plugin support, and a 60‑day evaluation period, all without artificial limitations or DRM.
layout: provider
modified: '2026-10-28'
name: REAPER
nav: Providers
network: true
overview: 'REAPER is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Digital Audio Workstation, Music Production, Windows, and macOS.


  REAPER''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 3 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
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
  name: Cockos Reaper Domain Security
  slug: cockos-reaper-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cockos-reaper
tags:
- Audio
- Digital Audio Workstation
- Music Production
- Windows
- macOS
- Linux
website: https://www.reaper.fm/
---

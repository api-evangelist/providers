---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Formula 1 data and services as described on the official site.
  name: Formula 1 API
  slug: formula-1-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/formula-1/refs/heads/main/well-known/formula-1-f1store-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/formula-1-f1store-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/formula-1/refs/heads/main/well-known/formula-1-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/formula-1-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/formula-1/refs/heads/main/hosts/formula-1-hosts.yml
  title: ''
  type: Hosts
  url: hosts/formula-1-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/formula-1/refs/heads/main/vendors/formula-1-vendors.yml
  title: ''
  type: Vendors
  url: vendors/formula-1-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.formula1.com/en/information/legal-notices.7egvZU48hzrypubGBNcQKt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/formula-1/refs/heads/main/security/formula-1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/formula-1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.formula1.com
coverage:
  checked: '2026-10-14'
  detail: Main site returns a JavaScript shell and no machine‑readable API documentation was found.
  evidence:
  - status: 200
    url: https://www.formula1.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Formula 1 (F1) is the premier international auto racing sport, governed by the FIA. It features a series of Grand Prix races across the globe, showcasing cutting‑edge automotive technology, elite drivers, and massive fan engagement. The sport’s official website provides news, race schedules, results, live timing, ticketing, merchandise, and a rich media experience for fans worldwide.
image: https://www.formula1.com/etc/designs/fom-website/social/f1-default-share.jpg
layout: provider
modified: '2026-10-13'
name: Formula 1
nav: Providers
network: true
overview: Formula 1 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Motorsports, Racing, and Entertainment.
random_paper: 16
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Formula 1 Domain Security
  slug: formula-1-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: formula-1
tags:
- Company
- Sports
- Motorsports
- Racing
- Entertainment
- Media
website: https://www.formula1.com
---

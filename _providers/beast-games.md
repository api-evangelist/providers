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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beast-games/refs/heads/main/well-known/beast-games-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beast-games-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beast-games/refs/heads/main/well-known/beast-games-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beast-games-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beast-games/refs/heads/main/hosts/beast-games-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beast-games-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beast-games/refs/heads/main/vendors/beast-games-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beast-games-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beast-games/refs/heads/main/security/beast-games-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beast-games-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beast-games/refs/heads/main/security/beast-games-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beast-games-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beastgames.com/
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at api.beastgames.com or any discovered host.
  evidence:
  - status: 0
    url: https://api.beastgames.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Beast Games is a reality‑competition entertainment brand created by MrBeast, featuring large‑scale physical and mental challenges with a $5 million grand prize. The platform showcases elite strength, intelligence and strategy contests, partnering with major brands and streaming on Amazon Prime Video.
layout: provider
modified: '2026-09-27'
name: Beast Games
nav: Providers
network: true
overview: Beast Games is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Competitions, Gaming, and Streaming.
random_paper: 19
score:
  band: minimal
  composite: 5.3
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
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beast Games Domain Security
  slug: beast-games-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Beast Games Vulnerability Disclosure
  slug: beast-games-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: beast-games
tags:
- Company
- Entertainment
- Competitions
- Gaming
- Streaming
website: https://www.beastgames.com/
---

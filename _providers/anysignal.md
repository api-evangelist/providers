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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysignal/refs/heads/main/hosts/anysignal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anysignal-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anysignal/refs/heads/main/vendors/anysignal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anysignal-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AnySignal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anysignal/refs/heads/main/security/anysignal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anysignal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anysignal.com/
- group: company
  title: ''
  type: Blog
  url: https://www.anysignal.com/news/
coverage:
  checked: '2026-09-25'
  detail: API host https://api.anysignal.com did not return a spec and no docs host is identified.
  evidence:
  - status: timeout
    url: https://api.anysignal.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: AnySignal delivers an end‑to‑end RF platform that provides spectrum supremacy for mission‑critical environments across space, land, air, and sea. Their solutions combine hardware, software, and orchestration tools to enable reliable, low‑latency communications for aerospace, defense, and national security customers. The platform includes capabilities such as communications, electronic warfare, autonomous systems, radar, and a resilient network, supporting both commercial and government missions.
image: https://www.anysignal.com/og-default.png
layout: provider
modified: '2026-09-25'
name: AnySignal
nav: Providers
network: true
overview: 'AnySignal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RF, Spectrum, Aerospace, and Defense.


  AnySignal''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anysignal Domain Security
  slug: anysignal-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: anysignal
tags:
- Company
- RF
- Spectrum
- Aerospace
- Defense
website: https://www.anysignal.com/
---

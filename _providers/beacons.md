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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beacons/refs/heads/main/llms/beacons-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beacons-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beacons/refs/heads/main/well-known/beacons-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beacons-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacons/refs/heads/main/hosts/beacons-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beacons-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beacons/refs/heads/main/vendors/beacons-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beacons-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beacons/refs/heads/main/security/beacons-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beacons-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beacons.ai/
coverage:
  checked: '2026-09-27'
  detail: Main site returns 403 and docs are not publicly accessible.
  evidence:
  - status: 403
    url: https://beacons.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beacons provides a platform for creators to build mobile websites, link-in-bio pages, and monetization tools. It offers customizable landing pages, e‑commerce integration, and analytics, helping creators grow their audience and revenue through a single, easy‑to‑use interface.
layout: provider
modified: '2026-09-27'
name: Beacons
nav: Providers
network: true
overview: Beacons is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, Creators, Link in Bio, and Monetization.
random_paper: 5
score:
  band: minimal
  composite: 4.6
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
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
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
  name: Beacons Domain Security
  slug: beacons-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beacons
tags:
- Company
- Mobile
- Creators
- Link in Bio
- Monetization
website: https://beacons.ai/
---

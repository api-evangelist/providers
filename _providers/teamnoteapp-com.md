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
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/teamnoteapp-com/well-known/teamnoteapp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teamnoteapp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/teamnoteapp-com/hosts/teamnoteapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teamnoteapp-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/teamnoteapp-com/security/teamnoteapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teamnoteapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://teamnoteapp.com
coverage:
  checked: '2026-10-29'
  detail: The homepage returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 202
    url: http://teamnoteapp.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: 'Teamnote is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by y-combinator) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-29'
name: Teamnote
nav: Providers
network: true
overview: Teamnote is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 10
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Teamnoteapp Com Domain Security
  slug: teamnoteapp-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teamnoteapp-com
tags:
- Company
website: http://teamnoteapp.com
---

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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://example.com/security/policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/politico/refs/heads/main/well-known/politico-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/politico-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/politico/refs/heads/main/well-known/politico-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/politico-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/politico/refs/heads/main/hosts/politico-hosts.yml
  title: ''
  type: Hosts
  url: hosts/politico-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/politico/refs/heads/main/vendors/politico-vendors.yml
  title: ''
  type: Vendors
  url: vendors/politico-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/politico
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/politico/refs/heads/main/security/politico-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/politico-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/politico/refs/heads/main/security/politico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/politico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://politico.com/
created: '2026-10-12'
description: Politico illuminates the forces shaping global power. Since 2007, we have delivered intelligence that anticipates tomorrow’s headlines, not reports on yesterday’s news. Our 1,100+ publishing professionals across key democratic capitals provide premier politics and policy newsroom, offering analysis for leaders and decision‑makers.
layout: provider
modified: '2026-10-12'
name: Politico
nav: Providers
network: true
overview: Politico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, News, Politics, and Journalism.
random_paper: 9
score:
  band: minimal
  composite: 6.9
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
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Politico Domain Security
  slug: politico-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Politico Vulnerability Disclosure
  slug: politico-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: politico
tags:
- Company
- Media
- News
- Politics
- Journalism
website: https://politico.com/
---

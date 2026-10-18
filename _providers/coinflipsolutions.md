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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation is behind a login portal and not publicly accessible.
  name: CoinFlip API
  slug: coinflip-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinflipsolutions/refs/heads/main/llms/coinflipsolutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinflipsolutions-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinflipsolutions/refs/heads/main/well-known/coinflipsolutions-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinflipsolutions-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinflipsolutions/refs/heads/main/hosts/coinflipsolutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinflipsolutions-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinflipsolutions/refs/heads/main/vendors/coinflipsolutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinflipsolutions-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinflipsolutions/refs/heads/main/security/coinflipsolutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinflipsolutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinflip.tech
created: '2026-10-09'
description: 'Coinflipsolutions is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-09'
name: Coinflipsolutions
nav: Providers
network: true
overview: Coinflipsolutions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 12
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 42.9
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
  name: Coinflipsolutions Domain Security
  slug: coinflipsolutions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coinflipsolutions
tags:
- Company
website: https://coinflip.tech
---

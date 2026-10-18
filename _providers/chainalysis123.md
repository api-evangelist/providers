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
    dynamic_client_registration: false
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
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chainalysis123/refs/heads/main/llms/chainalysis123-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chainalysis123-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chainalysis123/refs/heads/main/well-known/chainalysis123-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chainalysis123-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chainalysis123/refs/heads/main/well-known/chainalysis123-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chainalysis123-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chainalysis123/refs/heads/main/hosts/chainalysis123-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chainalysis123-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chainalysis123/refs/heads/main/vendors/chainalysis123-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chainalysis123-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chainalysis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chainalysis.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.chainalysis.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.chainalysis.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chainalysis123/refs/heads/main/security/chainalysis123-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainalysis123-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chainalysis.com
coverage:
  checked: '2026-10-08'
  detail: API host https://api.chainalysis.com returns HTTP 410 with no OpenAPI spec.
  evidence:
  - status: 410
    url: https://api.chainalysis.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Chainalysis123 is a leading blockchain data platform providing investigative, compliance, and analytics solutions for law enforcement, financial institutions, and businesses. It offers tools such as Reactor, Wallet Scan, KYT monitoring, and AI-driven agents to trace crypto transactions, assess risk, and prevent fraud across the cryptocurrency ecosystem.
image: https://www.chainalysis.com/wp-content/uploads/2025/02/meta-image-chainalysis.jpg
layout: provider
modified: '2026-10-07'
name: Chainalysis123
nav: Providers
network: true
overview: 'Chainalysis123 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include blockchain analytics, crypto compliance, investigations, financial institutions, and law enforcement.


  Chainalysis123''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 14.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chainalysis123 Domain Security
  slug: chainalysis123-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chainalysis123
tags:
- blockchain analytics
- crypto compliance
- investigations
- financial institutions
- law enforcement
- Exchange
- Security
- data solutions
website: https://www.chainalysis.com
---

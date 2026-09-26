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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tbo/refs/heads/main/hosts/tbo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tbo-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.tbo.com/engagement/media/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tbo/refs/heads/main/security/tbo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tbo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tbo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tbo.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tbo.com/terms-and-conditions
created: '2026-09-23'
description: TBO.com is a leading global travel distribution platform that simplifies travel business operations for agents, enterprises, and travel providers. Offering a comprehensive suite of products including hotels, packages, transfers, rail, cargo, marine, and more, TBO.com provides robust APIs that enable partners to integrate travel services, manage bookings, and expand their offerings worldwide.
image: https://www.tbo.com/img/oglogo.png
layout: provider
modified: '2026-09-23'
name: TBO.com
nav: Providers
network: true
overview: TBO.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Distribution, B2B, and Platform.
random_paper: 17
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  previous_composite: 8.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tbo Domain Security
  slug: tbo-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC
slug: tbo
tags:
- Travel
- Distribution
- B2B
- Platform
website: https://tbo.com/
---

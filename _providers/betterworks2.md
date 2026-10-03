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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betterworks2/refs/heads/main/security/betterworks2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterworks2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.betterworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.betterworks.com/resources-library
- group: company
  title: ''
  type: Blog
  url: https://www.betterworks.com/magazine
- group: operate
  title: ''
  type: Support
  url: https://support.betterworks.com
created: '2026-09-28'
description: Betterworks provides real-time performance management and talent intelligence solutions for organizations. Their platform helps align goals, deliver continuous feedback, and drive employee engagement through OKRs, performance reviews, surveys, and analytics. Betterworks enables companies to improve talent development, retention, and overall business results with data-driven insights and integrated HR tools.
layout: provider
modified: '2026-09-28'
name: Betterworks2
nav: Providers
network: true
overview: 'Betterworks2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Performance Management, Talent Intelligence, OKRs, Employee Engagement, and HR Software.


  Betterworks2''s developer surface includes documentation, engineering blog, support, and 2 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Betterworks2 Domain Security
  slug: betterworks2-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: betterworks2
tags:
- Performance Management
- Talent Intelligence
- OKRs
- Employee Engagement
- HR Software
website: https://www.betterworks.com
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/saaspec/hosts/saaspec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saaspec-hosts.yml
- group: auth
  href: https://artifacts.apis.io/saaspec/security/saaspec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saaspec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saaspec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.saaspec.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.saaspec.com/docs
- group: other
  title: ''
  type: Dashboard
  url: https://www.saaspec.com/dashboard
coverage:
  detail: Unable to retrieve any API documentation or machine‑readable specification from the provider's hosts.
  evidence:
  - status: 0
    url: https://api.saaspec.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: SaaSpec provides a platform for discovering, comparing, and analyzing SaaS products. It aggregates data on software-as-a-service offerings, offering detailed specifications, pricing, feature comparisons, and user reviews to help businesses make informed purchasing decisions. The service aims to simplify the SaaS selection process through comprehensive data, searchable catalogs, and analytical tools, catering to enterprises seeking optimal software solutions.
layout: provider
modified: '2026-10-18'
name: SaaSpec
nav: Providers
network: true
overview: 'SaaSpec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, Analytics, Monitoring, Pricing, and Comparison.


  SaaSpec''s developer surface includes documentation, getting-started guide, and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/saaspec/saaspec-2026-11-03T142634.png
security:
- kind: domain-security
  name: Saaspec Domain Security
  slug: saaspec-domain-security
  summary_line: no transport/DNS hardening detected
slug: saaspec
tags:
- Software-as-a-Service
- Analytics
- Monitoring
- Pricing
- Comparison
website: https://saaspec.com/
---

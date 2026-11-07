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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/alto-life/well-known/alto-life-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alto-life-well-known.yml
- group: other
  href: https://artifacts.apis.io/alto-life/hosts/alto-life-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alto-life-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altolife.com/privacy-policy-2/
- group: company
  title: ''
  type: Blog
  url: https://altolife.com/category/blog/
- group: auth
  href: https://artifacts.apis.io/alto-life/security/alto-life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alto-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altolife.com/
created: '2026-09-24'
description: 'Alto Life is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-24'
name: Alto Life
nav: Providers
network: true
overview: 'Alto Life is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Disability, Community, and Advantage Club.


  Alto Life''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 26.8
    operational_transparency: 0.0
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/alto-life/alto-life-2026-10-11T093746.png
security:
- kind: domain-security
  name: Alto Life Domain Security
  slug: alto-life-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alto-life
tags:
- Disability
- Community
- Advantage Club
website: https://altolife.com/
---

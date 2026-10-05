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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alto-life/refs/heads/main/well-known/alto-life-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alto-life-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alto-life/refs/heads/main/hosts/alto-life-hosts.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/alto-life/refs/heads/main/security/alto-life-domain-security.yml
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
random_paper: 13
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 26.8
    operational_transparency: 0.0
  previous_composite: 4.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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

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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/clairvoyint/well-known/clairvoyint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clairvoyint-well-known.yml
- group: other
  href: https://artifacts.apis.io/clairvoyint/hosts/clairvoyint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clairvoyint-hosts.yml
- group: other
  href: https://artifacts.apis.io/clairvoyint/vendors/clairvoyint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clairvoyint-vendors.yml
- group: auth
  href: https://artifacts.apis.io/clairvoyint/security/clairvoyint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clairvoyint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clairvoyint.ai/
- group: company
  title: ''
  type: Blog
  url: https://clairvoyintai.substack.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.clairvoyint.ai/mcp
  - status: 200
    url: https://www.clairvoyint.ai/
  reason: partner-login
  state: gated
created: '2026-10-23'
description: Clairvoyint provides AI‑driven analytical agents that turn expert methodology into reusable, reliable tools. Their platform enables complex analysis to be repeatable, defensible, and auditable across industries such as geospatial operations, infrastructure risk, sports analytics, environmental monitoring, and commodity markets. By offering a beta application and extensive documentation, they help users integrate evidence‑grounded agents into workflows.
image: https://clairvoyint.ai/img/clairvoyint-og-image.jpg
layout: provider
modified: '2026-10-23'
name: Clairvoyint
nav: Providers
network: true
overview: 'Clairvoyint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Analytics, Evidence, Platform, and Geospatial.


  Clairvoyint''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clairvoyint Domain Security
  slug: clairvoyint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clairvoyint
tags:
- AI
- Analytics
- Evidence
- Platform
- Geospatial
website: https://www.clairvoyint.ai/
---

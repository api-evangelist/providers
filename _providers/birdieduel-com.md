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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for BirdieDuel platform (no public contract discovered)
  name: BirdieDuel API
  slug: birdieduel-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/birdieduel-com/llms/birdieduel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/birdieduel-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/birdieduel-com/well-known/birdieduel-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/birdieduel-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/birdieduel-com/hosts/birdieduel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/birdieduel-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://birdieduel.com/login
- group: auth
  href: https://artifacts.apis.io/birdieduel-com/security/birdieduel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birdieduel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://birdieduel.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.birdieduel.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BirdieDuel is a mobile and web application that helps golfers record their rounds, track statistics, and compete in duels and tournaments with friends. The platform offers free round logging, performance analytics, and social features to engage users in competitive golf experiences.
image: https://birdieduel.com/landing-hero.webp
layout: provider
modified: '2026-11-02'
name: BirdieDuel
nav: Providers
network: true
overview: BirdieDuel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Golf, Mobile App, Statistics, Social, and Competitions.
random_paper: 21
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Birdieduel Com Domain Security
  slug: birdieduel-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: birdieduel-com
tags:
- Golf
- Mobile App
- Statistics
- Social
- Competitions
website: https://birdieduel.com/
---

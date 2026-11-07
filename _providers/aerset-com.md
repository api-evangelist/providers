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
- group: agent
  href: https://artifacts.apis.io/aerset-com/llms/aerset-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerset-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aerset-com/hosts/aerset-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aerset-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aerset-com/security/aerset-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerset-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aerset.com/
- group: company
  title: ''
  type: Blog
  url: https://aerset.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aerset.com/precios
- group: start
  title: ''
  type: SignUp
  url: https://aerset.com/signup
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://aerset.com/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: Aerset provides a comprehensive back‑office platform for drone operators in Spain, handling flight planning, legal compliance, airspace notifications, weather data, and portfolio management. The service is currently in private beta, accessible by invitation, and aims to streamline the regulatory process for aerial filming and commercial drone use.
image: https://aerset.com/og.jpg
layout: provider
modified: '2026-10-31'
name: Aerset
nav: Providers
network: true
overview: 'Aerset is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Drone, Aviation, Compliance, Planning, and Spain.


  Aerset''s developer surface includes engineering blog, pricing, signup flow, and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 8.7
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
security:
- kind: domain-security
  name: Aerset Com Domain Security
  slug: aerset-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aerset-com
tags:
- Drone
- Aviation
- Compliance
- Planning
- Spain
website: https://aerset.com/
---

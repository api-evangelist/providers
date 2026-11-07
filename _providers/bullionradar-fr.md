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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bullionradar-fr/llms/bullionradar-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bullionradar-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/bullionradar-fr/well-known/bullionradar-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bullionradar-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/bullionradar-fr/hosts/bullionradar-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bullionradar-fr-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://bullionradar.fr/docs/petit-guide-du-stacker.pdf
- group: auth
  href: https://artifacts.apis.io/bullionradar-fr/security/bullionradar-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bullionradar-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bullionradar.fr/
coverage:
  checked: '2026-11-03'
  detail: MCP endpoint requires POST, which is disallowed by policy, preventing contract retrieval.
  evidence:
  - status: 405
    url: https://bullionradar.fr/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-03'
description: BullionRadar is an independent price comparison platform for gold and silver investment coins in France. It aggregates real‑time pricing from over 11 dealers, providing detailed data on weight, purity, liquidity, and premium for each coin. The service is free for users and transparently funded through affiliate commissions, ensuring unbiased listings. BullionRadar continuously updates prices multiple times daily, offering calculators for premiums and resale taxes, and publishes guides on coin investing and storage.
image: https://bullionradar.fr/images/og-bullionradar.jpg
layout: provider
modified: '2026-11-03'
name: BullionRadar
nav: Providers
network: true
overview: 'BullionRadar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Precious Metals, Price Comparison, Investment, and France.


  BullionRadar''s developer surface includes documentation and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bullionradar Fr Domain Security
  slug: bullionradar-fr-domain-security
  summary_line: TLSv1.3
slug: bullionradar-fr
tags:
- Finance
- Precious Metals
- Price Comparison
- Investment
- France
website: https://bullionradar.fr/
---

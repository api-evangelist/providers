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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/asientouno-com/llms/asientouno-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asientouno-com-llms.txt
- group: other
  href: https://artifacts.apis.io/asientouno-com/hosts/asientouno-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asientouno-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asientouno-com/vendors/asientouno-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asientouno-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/asientouno-com/security/asientouno-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asientouno-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asientouno.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asientouno.com/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://asientuno.com/precios
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://asientouno.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Asiento Uno provides free public access to Spanish company registry data, aggregating official sources such as BORME, BDNS, PLACSP, sanctions lists, and court records. Users can search identities, charges, acts, subsidies, public contracts, and risk signals, all linked to original official documents.
image: https://asientouno.com/opengraph-image
layout: provider
modified: '2026-11-01'
name: Asiento Uno
nav: Providers
network: true
overview: 'Asiento Uno is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Spain, Registry, and Public.


  Asiento Uno''s developer surface includes documentation, pricing, and 5 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 39.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 7.4
  provenance:
    mcp: derived
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
  name: Asientouno Com Domain Security
  slug: asientouno-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asientouno-com
tags:
- Data
- Spain
- Registry
- Public
website: https://asientouno.com/
---

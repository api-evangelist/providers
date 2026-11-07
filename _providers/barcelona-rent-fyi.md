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
api_count: 1
apis:
- description: Data API providing JSON endpoints for Barcelona rental statistics and tools.
  name: Barcelona Rent API
  slug: barcelona-rent-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/barcelona-rent-fyi/llms/barcelona-rent-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barcelona-rent-fyi-llms.txt
- group: other
  href: https://artifacts.apis.io/barcelona-rent-fyi/hosts/barcelona-rent-fyi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barcelona-rent-fyi-hosts.yml
- group: other
  href: https://artifacts.apis.io/barcelona-rent-fyi/vendors/barcelona-rent-fyi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barcelona-rent-fyi-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.barcelona-rent.fyi/data/quickstart
- group: auth
  href: https://artifacts.apis.io/barcelona-rent-fyi/security/barcelona-rent-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barcelona-rent-fyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.barcelona-rent.fyi/
- group: company
  title: ''
  type: Blog
  url: https://www.barcelona-rent.fyi/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.barcelona-rent.fyi/privacy-policy
coverage:
  checked: '2026-11-02'
  detail: Provider offers JSON data endpoints but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are published.
  evidence:
  - status: 200
    url: https://www.barcelona-rent.fyi/api/data/latest.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Barcelona Rent provides up-to-date rental price data for Barcelona neighborhoods, sourced from official INCASOL statistics and the Generalitat de Catalunya. The platform offers tools to compare rents, calculate mortgage offers, and track market trends, updating quarterly with official data. It aims to help residents and prospective renters understand fair pricing across the city.
image: https://www.barcelona-rent.fyi/api/og?title=Barcelona+Rent+Prices+2026+%7C+Compare+by+Neighborhood+%26+District
layout: provider
modified: '2026-11-02'
name: Barcelona Rent
nav: Providers
network: true
overview: 'Barcelona Rent is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Data, Housing, Spain, and Barcelona.


  Barcelona Rent''s developer surface includes getting-started guide, engineering blog, and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barcelona Rent Fyi Domain Security
  slug: barcelona-rent-fyi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: barcelona-rent-fyi
tags:
- Real Estate
- Data
- Housing
- Spain
- Barcelona
- Rentals
website: https://www.barcelona-rent.fyi/
---

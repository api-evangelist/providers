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
- description: Public API for property valuation via MCP
  name: Bolig Tracker Online
  slug: bolig-tracker-online
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bolig-tracker-online/hosts/bolig-tracker-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bolig-tracker-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/bolig-tracker-online/vendors/bolig-tracker-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bolig-tracker-online-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://bolig-tracker.online/signin
- group: auth
  href: https://artifacts.apis.io/bolig-tracker-online/security/bolig-tracker-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bolig-tracker-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bolig-tracker.online/
- group: docs
  title: ''
  type: APIReference
  url: https://bolig-tracker.online/mcp-info
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bolig-tracker.online/privatliv
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known hosts.
  evidence:
  - status: 405
    url: https://bolig-tracker.online/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bolig Tracker provides free, data‑driven property valuation for Danish homes. Using publicly available sales data, it offers statistical market‑value estimates, price trends by area, and property‑tax calculations. The service is openly accessible without login, and includes a public MCP server for AI assistants to query valuations. It aggregates data from Boligsiden, Datafordeleren, BBR, VUR and DAWA, and is hosted on Vercel.
image: https://bolig-tracker.online/opengraph-image?d2341d9973d2d4c9
layout: provider
modified: '2026-11-02'
name: Bolig Tracker
nav: Providers
network: true
overview: 'Bolig Tracker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Valuation, Denmark, and Open Data.


  Bolig Tracker''s developer surface includes API reference and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - denmark
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bolig Tracker Online Domain Security
  slug: bolig-tracker-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bolig-tracker-online
tags:
- Company
- Real Estate
- Valuation
- Denmark
- Open Data
website: https://bolig-tracker.online/
---

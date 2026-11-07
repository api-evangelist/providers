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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for BrickTrack property management platform
  name: BrickTrack API
  slug: bricktrack-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bricktrack-au/llms/bricktrack-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bricktrack-au-llms.txt
- group: agent
  href: https://artifacts.apis.io/bricktrack-au/well-known/bricktrack-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bricktrack-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/bricktrack-au/hosts/bricktrack-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bricktrack-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/bricktrack-au/vendors/bricktrack-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bricktrack-au-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bricktrack.au/terms
- group: operate
  title: ''
  type: Support
  url: https://www.bricktrack.au/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bricktrack.au/privacy
- group: start
  title: ''
  type: Login
  url: https://www.bricktrack.au/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bricktrack.au/help/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.bricktrack.au/help/guides
- group: company
  title: ''
  type: Blog
  url: https://www.bricktrack.au/blog
- group: auth
  href: https://artifacts.apis.io/bricktrack-au/security/bricktrack-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bricktrack-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bricktrack.au/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are public HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.bricktrack.au/help/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BrickTrack provides a cloud‑based investment property tracker that lets owners monitor equity, cash flow, rent and loans across their portfolio without using spreadsheets. The platform offers real‑time analytics, automated reporting, and tools for budgeting and forecasting, aiming to simplify property management for investors and landlords.
image: https://www.bricktrack.au/og-image.png
layout: provider
modified: '2026-11-03'
name: BrickTrack
nav: Providers
network: true
overview: 'BrickTrack is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Property Management, Investment, and Software-as-a-Service.


  BrickTrack''s developer surface includes support, getting-started guide, documentation, engineering blog, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bricktrack Au Domain Security
  slug: bricktrack-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bricktrack-au
tags:
- Company
- Real Estate
- Property Management
- Investment
- Software-as-a-Service
website: https://www.bricktrack.au/
---

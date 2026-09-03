---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST APIs providing Australian property intelligence — address suggestion and matching, property and listing data, sold-transaction search (including point-and-radius queries), automated valuations (A
  name: PropTrack APIs
  slug: proptrack-apis
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proptrack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.proptrack.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.proptrack.com.au/docs/apis/home
- group: docs
  title: ''
  type: Documentation
  url: https://developer.proptrack.com.au/docs/apis/home
- group: other
  title: ''
  type: ProductOverview
  url: https://www.proptrack.com.au/property-data/property-data-apis/
- group: operate
  title: ''
  type: Support
  url: https://www.proptrack.com.au/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://kmmfkblgkhnf.statuspage.io/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/proptrack-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/proptrack-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/proptrack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.rea-group.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/proptrack-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/proptrack-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/proptrack-llms.txt
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.rea-group.com/
created: '2026-07-24'
description: PropTrack is an Australian property data, analytics, and automated valuation business, part of REA Group. It supplies residential property data, an industry-leading AI-powered Automated Valuation Model (AVM), the PropTrack Home Price Index, and market insights drawn from more than a trillion property data points across some twelve million Australian residential properties. Its raw data is sourced from public records (State/Territory land titles offices, Valuers General, and Geoscape Australia) and proprietary sources including the realestate.com.au listing portal. PropTrack exposes this through a developer program of REST APIs — covering address suggestion and matching, property and listing data, sold-transaction search (including point-and-radius queries), automated valuations, and market metrics — documented on a hosted Stoplight developer portal and secured with OAuth 2.0. The APIs are aimed at banks, lenders, brokers, proptech platforms, and other enterprise customers integrating
  Australian property intelligence.
image: https://www.proptrack.com.au/wp-content/uploads/2021/10/proptrack_-_pos.png
layout: provider
modified: '2026-07-24'
name: PropTrack
nav: Providers
network: true
overview: 'PropTrack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Property Data, Real-Estate, Automated Valuation, and Property Valuation.


  PropTrack''s developer surface includes documentation, support, authentication, and 12 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/proptrack/refs/heads/main/screenshots/proptrack-2026-07-27T125354.png
security:
- kind: authentication
  name: Proptrack Authentication
  slug: proptrack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Proptrack Domain Security
  slug: proptrack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Proptrack Vulnerability Disclosure
  slug: proptrack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: proptrack
tags:
- Company
- Property Data
- Real-Estate
- Automated Valuation
- Property Valuation
- Australia
- Market Data
- Data & Analytics
- PropTech
website: https://www.proptrack.com.au/
---

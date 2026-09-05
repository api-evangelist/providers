---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://betterview.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.nearmap.com/products/betterview — a different registrable domain (betterview.com -> nearmap.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
  score: 3.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Order and retrieve property profiles (RSI, peril risks, flags, Partner Connect), manage PropertyPulse monitoring, and query PropertyNow datasets by address or coordinates. Bearer-token authenticated; '
  name: Betterview Property Intelligence API
  slug: betterview-property-intelligence-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://betterview.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.betterview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.betterview.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.betterview.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.betterview.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://dev.betterview.com/discuss
- group: auth
  title: ''
  type: Authentication
  url: authentication/betterview-marketplace-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/betterview-marketplace-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/betterview-marketplace-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/betterview-marketplace-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betterview-marketplace-domain-security.yml
created: '2026-07-17'
description: Betterview is a market-leading Property Intelligence platform that delivers actionable insights to property & casualty insurance underwriters, agents, and insureds to increase efficiency and profitability. Its API lets carriers order and retrieve property profiles enriched with the Roof Spotlight Index (RSI), peril risks, flags, and third-party Partner Connect data, subscribe properties to PropertyPulse monitoring, and query PropertyNow pre-processed datasets by address or coordinates. Betterview integrates with core insurance systems including Guidewire (a Marketplace accelerator for PolicyCenter 10), Duck Creek, and Socotra, and supports SSO, Secure FTP, ImageRight drop, an embeddable geospatial iframe UI, and an External Data Warehouse (EDW) SQL connection.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betterview-marketplace.png
layout: provider
modified: '2026-07-18'
name: BetterView Marketplace
nav: Providers
network: true
overview: 'BetterView Marketplace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Property Intelligence, Insurance, Insurtech, and Geospatial.


  BetterView Marketplace''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.3
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betterview-marketplace/refs/heads/main/screenshots/betterview-marketplace-2026-07-25T202815.png
security:
- kind: authentication
  name: Betterview Marketplace Authentication
  slug: betterview-marketplace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Betterview Marketplace Domain Security
  slug: betterview-marketplace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: betterview-marketplace
tags:
- Company
- Property Intelligence
- Insurance
- Insurtech
- Geospatial
- Underwriting
- Property Data
- Risk
website: https://betterview.com
---

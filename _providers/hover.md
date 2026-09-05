---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for creating and managing property capture jobs, retrieving 3D models and measurement deliverables, inspections, estimates, instant-design leads, and webhooks. OAuth 2.0 authenticated. Versio
  name: HOVER API
  slug: hover-api
artifact_total: 6
asyncapis:
- description: ''
  name: Hover Webhooks
  slug: hover-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hover.to
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hover.to
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hover.to/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hover.to/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hover.to/docs/creating-and-managing-integrations
- group: operate
  title: ''
  type: Support
  url: https://help.hover.to
- group: company
  title: ''
  type: Blog
  url: https://hover.to/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hoverinc
- group: commercial
  title: ''
  type: Pricing
  url: https://hover.to/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hover.to/onboarding/start
- group: start
  title: ''
  type: Login
  url: https://hover.to/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hover.to/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hover.to/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.hover.to
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.hover.to/docs/release-notes
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hover-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hover-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hover-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hover-well-known.yml
created: '2026-07-17'
description: HOVER turns smartphone photos of a property into an accurate, interactive 3D model with complete exterior and interior measurements for the construction, roofing, insurance, and home-services industries. The HOVER API lets partners programmatically create and manage jobs, send capture requests that invite a homeowner or field technician to photograph a structure, receive real-time status updates via webhooks, and retrieve 3D models and measurement deliverables in JSON, PDF, XLSX, SKP, ESX, FML, and XML formats. Additional endpoints cover inspections, estimates and material lists, instant-design images and leads, blueprint reconstruction, job sharing, notes, users, wallets and payments. Authentication is OAuth 2.0 (authorization code + refresh), and a hosted MCP server exposes the same surface to AI agents. HOVER is backed by GV and Menlo Ventures.
image: https://hover.to/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: HOVER MCP Server
  slug: hover-mcp-server
modified: '2026-07-19'
name: HOVER
nav: Providers
network: true
overview: 'HOVER publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Construction, Roofing, and Insurance.


  The HOVER catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HOVER''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 2
  name: Hover Rate Limits
  slug: hover-rate-limits
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 47.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hover/refs/heads/main/screenshots/hover-2026-07-25T221536.png
security:
- kind: authentication
  name: Hover Authentication
  slug: hover-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hover Domain Security
  slug: hover-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hover
tags:
- Company
- Enterprise
- Construction
- Roofing
- Insurance
- 3D Modeling
- Property Data
- Measurements
- Home Services
- Geospatial
website: https://hover.to
---

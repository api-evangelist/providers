---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-02'
api_count: 4
apis:
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Authentication API from Emerge — 3 operation(s) for authentication.
  name: Emerge Authentication API
  slug: emerge-authentication-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Awards API from Emerge — 2 operation(s) for awards.
  name: Emerge Awards API
  slug: emerge-awards-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Network Partners API from Emerge — 2 operation(s) for network partners.
  name: Emerge Network Partners API
  slug: emerge-network-partners-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Opportunities API from Emerge — 6 operation(s) for opportunities.
  name: Emerge Opportunities API
  slug: emerge-opportunities-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Options API from Emerge — 2 operation(s) for options.
  name: Emerge Options API
  slug: emerge-options-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Shipments API from Emerge — 1 operation(s) for shipments.
  name: Emerge Shipments API
  slug: emerge-shipments-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Tender API from Emerge — 1 operation(s) for tender.
  name: Emerge Tender API
  slug: emerge-tender-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: The Tenders API from Emerge — 3 operation(s) for tenders.
  name: Emerge Tenders API
  slug: emerge-tenders-api
- baseURL: https://api.emergemarket.io/v1
  baseurl_source: declared
  description: Webhooks are used to provide updates to the TMS when award or option events are generated within the Emerge system. </br></br>If our webhook message cannot be accepted by the webhook endpoint due to n
  name: Emerge Webhooks API
  slug: emerge-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Emerge Webhooks
  slug: emerge-webhooks
collections:
- collection_type: open
  name: Emerge Carrier API
  slug: open-emerge-carrier-api
- collection_type: open
  name: Emerge Public API
  slug: open-emerge-public-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/emerge-public-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emerge-carrier-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.emergemarket.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.emergemarket.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.emergemarket.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.emergemarket.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.emergemarket.io/#section/Get-Started
- group: operate
  title: ''
  type: Support
  url: https://help.emergemarket.io/en/
- group: company
  title: ''
  type: Blog
  url: https://www.emergemarket.com/company/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.emergemarket.com/legal/fees
- group: start
  title: ''
  type: Login
  url: https://login.emergemarket.io/
- group: start
  title: ''
  type: SignUp
  url: https://www.emergemarket.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.emergemarket.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emergemarket.com/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/emergetms/emergetms-s-public-workspace
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emergemarket.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://api-docs.emergemarket.io/#section/Get-Started/Compatibility-Policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.emergemarket.com/
- group: auth
  title: ''
  type: Security
  url: https://api.emergemarket.io/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/emerge-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/emerge-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emerge-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/emerge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/emerge-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emerge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/emerge-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/emerge-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/emerge-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emerge-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/emerge-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/emerge-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/emerge-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/emerge-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/emerge-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/emerge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/emerge-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emerge-domain-security.yml
created: '2026-08-12'
description: Emerge (EmergeTech, Inc.) is a Scottsdale, Arizona freight procurement and transportation spend management platform — marketed as ProcureOS — that moves full truckload, volume/partial truckload and drop-trailer freight sourcing out of spreadsheets and email into a single system. The platform combines contract procurement (annual RFPs, mini-bids, awarding scenarios, carrier scorecards), spot procurement (quoting, tendering, Dynamic Book It Now, tracking and visibility), Emerge AI rate benchmarking and lane intelligence (Rate Pulse), and the Emerge Marketplace of 45,000+ pre-vetted asset-based carriers across the US, Canada and Mexico. Emerge publishes two public REST APIs — a Shipper (public) API for opportunities, options, awards, tenders, shipments, network partners and webhook subscriptions, and a Carrier API for capacity/integration providers responding to rate requests and tenders — plus a documented webhook event catalog, a testing sandbox, and TMS integrations with Project44,
  E2open, MercuryGate and Capacity Link partners.
image: https://cdn.prod.website-files.com/66ad43d7385c00622859db37/66b8fd0eb48dad5fa020dc5c_website_share.png
layout: provider
mcp_servers:
- description: ''
  name: Emerge MCP Server
  slug: emerge-mcp-server
modified: '2026-08-12'
name: Emerge
nav: Providers
network: true
overview: 'Emerge publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Awards API, Network Partners API, and 6 more. Tagged areas include Freight, Logistics, Transportation, Supply Chain, and Procurement.


  The Emerge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Emerge''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Emerge Plans Pricing
  plan_count: 0
  slug: emerge-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Emerge Rate Limits
  slug: emerge-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 62.9
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 47.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emerge/refs/heads/main/screenshots/emerge-2026-08-17T080921.png
security:
- kind: authentication
  name: Emerge Authentication
  slug: emerge-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Emerge Domain Security
  slug: emerge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Emerge Vulnerability Disclosure
  slug: emerge-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Emerge Trust Center
  slug: emerge-trust-center
  summary_line: trust center published
slug: emerge
tags:
- Freight
- Logistics
- Transportation
- Supply Chain
- Procurement
- Trucking
- Freight Marketplace
- Transportation Management
- Shipping
- rate-benchmarking
- Webhook
- B2B Marketplace
website: https://www.emergemarket.com/
---

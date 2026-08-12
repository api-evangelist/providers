---
access_model:
  confidence: high
  label: Paid · Commercial onboarding required · Public documentation
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Landmark Information Agentic Access
  operation_count: 51
  slug: landmark-information-agentic-access
  summary_line: 51 operations · 32 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Compliance ordering API used to place and retrieve Landmark compliance product orders — AML individual and company checks, UK and international AML with facial recognition, Persons with Significant Co
  name: Landmark Order Experience API
  slug: landmark-order-experience-api
- description: Panel conveyancing API for quoting, instructing and managing conveyancing work through Landmark Optimus. Introducers create quotes, choose a conveyancer and instruct on a client's behalf; conveyancers
  name: Landmark Conveyancing Experience API
  slug: landmark-conveyancing-experience-api
- description: Case creation and management API for the Intelliworks legal case management system, letting third-party systems create and update cases outside the Intelliworks UI for Sale, Purchase, New Build Purcha
  name: Landmark Intelliworks APIs
  slug: landmark-intelliworks-api
- description: API behind Contract Pack Vault — creates a secure, shareable container of transaction documents, adds and removes files (virus-scanned and analysed asynchronously, status Pending then Available or Qua
  name: Landmark Document Vault API
  slug: landmark-document-vault-api
- description: 'Callback registration API for valuation transaction milestone notifications on the Landmark Secure Panel Network (SPN). Consumers register, update and delete callback URLs that Landmark then calls as '
  name: Landmark Milestone Notification Service API
  slug: landmark-milestone-notification-service-api
- description: RESTful planning-application data API combining Barbour ABI project information with Landmark geospatial data, covering UK and Republic of Ireland planning applications from 1 January 2017 (with histo
  name: Landmark Planning API (powered by Barbour ABI)
  slug: landmark-planning-api
- description: On-demand raster mapping tile service delivered against the Open Geospatial Consortium Web Map Tile Service (OGC WMTS) standard, with 20 zoom levels spanning Ordnance Survey MasterMap through national
  name: Landmark Geodata Web Map Tile Service (WMTS)
  slug: landmark-geodata-web-map-tile-service
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a Document Vault, add a document, set the recipient organisation and a recipient, and read back the vault and its activity trail.
  name: Assemble a Contract Pack Vault
  slug: landmark-information-assemble-contract-pack
- description: Place a compliance product order, poll it to completion, read the result and download the result document.
  name: Order a Landmark compliance check and collect the result
  slug: landmark-information-order-compliance-check
- description: Create a conveyancing quote, complete it with a person, property address and product details, produce the quote PDF and instruct a panel conveyancer.
  name: Quote to conveyancing instruction
  slug: landmark-information-quote-to-instruction
- description: Register a callback endpoint for Secure Panel Network valuation milestones, update its configuration, then remove it.
  name: Subscribe to valuation milestone notifications
  slug: landmark-information-subscribe-valuation-milestones
artifact_total: 19
asyncapis:
- description: ''
  name: Landmark Information Webhooks
  slug: landmark-information-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.landmarkcloudservices.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.landmarkcloudservices.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.landmarkcloudservices.com/conveyances-experience-api.html#section/Getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.landmark.co.uk/our-group/contact/
- group: design
  title: ''
  type: Conventions
  url: conventions/landmark-information-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/landmark-information-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/landmark-information-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/landmark-information-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/landmark-information-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/landmark-information-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/landmark-information-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/landmark-information-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/landmark-information-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/landmark-information-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/landmark-information-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/landmark-information-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/landmark-information-agentic-access.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landmark-information-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/landmark-information-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/landmark-information-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.landmark.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.landmarkcloudservices.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/landmark-information-openid-configuration.json
- group: start
  title: ''
  type: SignUp
  url: https://www.landmark.co.uk/our-group/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.landmark.co.uk/news-insights/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.landmark.co.uk/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.landmark.co.uk/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.landmark.co.uk/terms-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Landmark-Information-Group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/landmark-information-group
- group: company
  title: ''
  type: Careers
  url: https://www.landmark.co.uk/careers/
- group: company
  title: ''
  type: Partners
  url: https://www.landmark.co.uk/partners-suppliers/
created: '2026-07-26'
description: 'Landmark Information Group is a United Kingdom property and land data business, part of Daily Mail and General Trust (DMGT), that sits in the middle of the UK residential and commercial property transaction rather than at the listing end of it. Founded in 1995 and headquartered in Exeter, it aggregates 700+ datasets from nearly 400 suppliers — Ordnance Survey mapping and AddressBase/UPRN addressing, environmental and flood and mining risk, historical maps, planning applications, and Barbour ABI project data — and sells them as conveyancing search reports (SearchFlow, Envirocheck, RiskView, SiteSolutions), estate agency compliance and material information products (LandmarkAgent, Metropix floor plans), case management software for property lawyers (Optimus, Intelliworks, Ochresoft, Vantage), and lender/surveyor valuation infrastructure (Secure Panel Network SPN and SPN+, Q-Guard). The UK has no MLS and no RESO equivalent — residential listings are controlled by the Rightmove/Zoopla
  duopoly and reached through agency CRMs — so Landmark is not a listings company; it is the transaction-data and workflow layer beneath conveyancers, lenders, surveyors, and agents. Its API posture is unusually honest for this sector: Landmark runs a genuinely public, un-gated API documentation portal at landmarkcloudservices.com that publishes full OpenAPI 3.x contracts for its Compliance/Order, Conveyancing, Intelliworks, Document Vault, and Milestone Notification APIs, plus a public HTML technical pack for the Barbour ABI-powered Planning API. Reading the contracts is open to anyone; calling them is not. Every API is OAuth 2.0 client-credentials against Landmark''s Auth0 tenant with a client ID and secret issued only after a commercial account is onboarded ("your Landmark contact will confirm what''s available to you"), and the Planning API requires a paid subscription or pay-as-you-go agreement plus an API key issued by Landmark. There is no RESO Web API certification, no RESO Data
  Dictionary posture, no OData $metadata document and no Universal Property Identifier anywhere in Landmark''s surface — RESO is a North American MLS construct and is simply absent from the UK market. Landmark publishes no open data of its own; the open UK property layer belongs to HM Land Registry and Ordnance Survey, both of which are Landmark suppliers rather than Landmark products.'
image: https://www.landmarkcloudservices.com/assets/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: landmark-information-mcp.yml
  slug: landmark-information-mcpyml
modified: '2026-07-26'
name: Landmark Information Group
nav: Providers
network: true
overview: 'Landmark Information Group publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Landmark Order Experience API, Landmark Conveyancing Experience API, Landmark Intelliworks APIs, and 2 more. Tagged areas include Real Estate, United Kingdom, PropTech, Property Data, and Conveyancing.


  The Landmark Information Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Landmark Information Group''s developer surface includes API reference, getting-started guide, support, changelog, sandbox, authentication, documentation, and 27 more developer resources.'
random_paper: 105
rate_limits:
- limit_count: 2
  name: Landmark Information Rate Limits
  slug: landmark-information-rate-limits
scopes:
- name: Landmark Information Scopes
  scope_count: 0
  slug: landmark-information-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.8
  delta: -0.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 68.9
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/landmark-information/refs/heads/main/screenshots/landmark-information-2026-08-07T171441.png
security:
- kind: authentication
  name: Landmark Information Authentication
  slug: landmark-information-authentication
  summary_line: http/oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Landmark Information Domain Security
  slug: landmark-information-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: landmark-information
tags:
- Real Estate
- United Kingdom
- PropTech
- Property Data
- Conveyancing
- Land Registry
- Geospatial
- Valuation
- Anti-Money Laundering
- Planning Data
- Mortgage
website: https://www.landmark.co.uk/
---

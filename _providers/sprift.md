---
access_model:
  confidence: high
  label: Paid subscription · Book a demo, then request API access from Customer Success · Additional agreement may apply
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - knowledge-base
  - openapi
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sprift Agentic Access
  operation_count: 27
  slug: sprift-agentic-access
  summary_line: 27 operations · 3 acting
api_count: 7
apis:
- description: The Property tag of the published Sprift v1 contract — the largest family in the harvested Swagger document, with ten operations. POST /property/search generates a Sprift property report for a UPRN an
  name: Sprift Property API
  slug: sprift-property-api
- description: The Property V2 tag of the published Sprift v1 contract — eight operations that resolve and decompose a property into single-purpose reads rather than one large record. GET /property/{uprn}/search ret
  name: Sprift Property V2 API
  slug: sprift-property-v2-api
- description: The Search tag of the published Sprift v1 contract — three operations for finding a property before you can read it. GET /search takes a free-text phrase, GET /search/postcode/{postcode} returns addre
  name: Sprift Search API
  slug: sprift-search-api
- description: 'The Insider tag of the published Sprift v1 contract — two operations exposing the market intelligence product that sits behind sprift.com/insider. GET /insider/{outcode} searches active properties by '
  name: Sprift Insider API
  slug: sprift-insider-api
- description: 'The Share tag of the published Sprift v1 contract — a single POST /share operation that produces a shareable link to a Sprift report for a given property ID and report type, with the same report type '
  name: Sprift Report Share API
  slug: sprift-share-api
- description: The User tag of the published Sprift v1 contract — two operations, POST /user/login and GET /user/logout, that exist specifically for embedding. The contract is explicit that this is not the authentic
  name: Sprift User API
  slug: sprift-user-api
- description: The API family Sprift advertises on its Data and API product page, recorded here as advertised and NOT as verified. The page names ten REST endpoint paths — /api/v2/property/{uprn} (300 data point pro
  name: Sprift Data and API (v2, advertised)
  slug: sprift-data-and-api-v2
arazzos:
- description: Resolve a held address to a UPRN and Sprift property ID, then enrich with EPC, council tax, nearby schools, nearby transport, TV availability and imagery.
  name: Sprift — enrich a CRM record with property data
  slug: sprift-crm-enrichment
- description: Read active and withdrawn market stock for a UK postcode outcode from the Sprift Insider surface.
  name: Sprift — market activity for a postcode outcode
  slug: sprift-market-intelligence
- description: Resolve a UK postcode to a UPRN and pull the Material Information disclosure set for it.
  name: Sprift — Material Information for a UK property
  slug: sprift-material-information
- description: Resolve a UK postcode to a UPRN, generate a Sprift property report for it, and create a shareable link to that report.
  name: Sprift — address to shareable property report
  slug: sprift-property-report
- description: Resolve a UPRN to Sprift's internal property ID, then collect the price estimate, unified comparables, recently sold evidence and live for-sale stock.
  name: Sprift — valuation evidence pack
  slug: sprift-valuation-evidence
artifact_total: 18
asyncapis:
- description: ''
  name: Sprift Webhooks
  slug: sprift-webhooks
collections:
- collection_type: open
  name: Sprift API
  slug: open-sprift
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sprift-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sprift-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sprift-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sprift-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sprift-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sprift-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sprift-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/sprift-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sprift-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sprift-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sprift-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sprift-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sprift-openapi-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sprift-property-report.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sprift-material-information.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sprift-valuation-evidence.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sprift-market-intelligence.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sprift-crm-enrichment.yml
- group: company
  title: ''
  type: Website
  url: https://sprift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sprift.com/data-and-api
- group: docs
  title: ''
  type: APIReference
  url: https://sprift.com/dashboard/api-doc/
- group: docs
  title: ''
  type: OpenAPI
  url: https://sprift.com/dashboard/api-doc/sprift.json
- group: auth
  title: ''
  type: Authentication
  url: https://sprift.com/en/livechatacademy/api-key
- group: start
  title: ''
  type: Login
  url: https://sprift.com/dashboard/login
- group: start
  title: ''
  type: GettingStarted
  url: https://sprift.com/data-and-api
- group: commercial
  title: ''
  type: Pricing
  url: https://sprift.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sprift.com/terms-and-conditions
- group: start
  title: ''
  type: Demo
  url: https://sprift.com/book-demo-sprift
- group: operate
  title: ''
  type: Support
  url: https://sprift.com/academy
- group: company
  title: ''
  type: Partners
  url: https://sprift.com/partnerships
- group: company
  title: ''
  type: About
  url: https://sprift.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://sprift.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://sprift.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sprift.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sprift
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sprift/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SpriftProperty/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/SpriftProperty/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/spriftproperty/
created: '2026-07-26'
description: 'Sprift is a United Kingdom property data aggregator, operated by Sprift Technologies Ltd and founded in 2016 by Matt Gilpin, that assembles up to 300 data points on more than 30 million UK residential properties from public and private sources — Royal Mail, Ordnance Survey, the Environment Agency, HM Land Registry, Ofcom, Historic England, Ofsted, Google Maps, the Valuation Office Agency and the ONS — and links every one of them to a UPRN, the UK''s definitive property identifier. It sells that layer to estate and letting agents, surveyors, mortgage professionals, conveyancers and investors as shareable property dashboards, branded reports, Material Information packs, comparables, off-market prospecting and market intelligence. In a market with no MLS, Sprift occupies the aggregation seam: it does not own listings (Rightmove and Zoopla do) and it does not originate records (HM Land Registry and Ordnance Survey do), it enriches and resells the join between them. Its API posture
  is genuinely documented but commercially gated. A public, unauthenticated Swagger UI at sprift.com/dashboard/api-doc serves a real Swagger 2.0 contract (sprift.json, version 1.3.9, 27 paths, 76 definitions) for the v1 API at https://sprift.com/dashboard/api/v1, harvested verbatim here — that is the only machine-readable contract Sprift publishes. Every operation in it requires a SPRIFT-API-KEY header, and the API base returns HTTP 401 to anonymous callers. There is no self-serve signup anywhere: /dashboard/register and /dashboard/signup both return 404, pricing is not published, and Sprift''s own knowledge base instructs prospective API users to email Customer Success with their company, use case and target systems for review, noting that access "may require an additional agreement depending on your subscription". A larger v2 API family is advertised on the Data and API product page with named endpoint paths, webhook alerts and bulk queries, but no contract for it is published and no host
  for it was confirmed. No RESO Web API or Data Dictionary certification, no OData service root or $metadata document, and no Universal Property Identifier appears anywhere in Sprift''s surface — RESO is a North American, NAR-driven construct and the UK has no MLS to certify against. The UK''s standards seam is instead the Open Property Data Association and its Property Data Trust Framework, of which Sprift claims founding and accredited membership. Sprift publishes no open data of its own; the open UK property layer belongs to HM Land Registry and Ordnance Survey, which are among its inputs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: sprift-mcp.yml
  slug: sprift-mcpyml
modified: '2026-07-26'
name: Sprift
nav: Providers
network: true
overview: 'Sprift publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Property API, Property V2 API, Search API, and 3 more. Tagged areas include Real Estate, United Kingdom, PropTech, Property Data, and Property Listings.


  The Sprift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sprift''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, engineering blog, and 34 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 42.1
  delta: -1.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 55.9
    developer_ergonomics: 49.4
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sprift/refs/heads/main/screenshots/sprift-2026-08-17T082046.png
security:
- kind: authentication
  name: Sprift Authentication
  slug: sprift-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sprift Domain Security
  slug: sprift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sprift
tags:
- Real Estate
- United Kingdom
- PropTech
- Property Data
- Property Listings
- Valuation
- AVM
- Land Registry
- Conveyancing
- Rentals
- Mortgage
website: https://sprift.com/
---

---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The agent-facing commerce surface of Aptera Motors' branded merchandise storefront at shop.aptera.us. It is a Model Context Protocol server (protocol 2025-06-18) answering anonymously at /api/mcp with
  name: Aptera Shop Storefront Agent Commerce API
  slug: aptera-shop-storefront-agent-commerce-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptera-motors-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aptera-motors-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aptera-motors-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aptera-motors-shop-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aptera-motors-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aptera-motors-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aptera-motors-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aptera-motors-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://aptera.us/
- group: company
  title: ''
  type: Blog
  url: https://aptera.us/updates/
- group: company
  title: ''
  type: BlogRSS
  url: https://aptera.us/updates/feed/
- group: operate
  title: ''
  type: Support
  url: https://aptera.us/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://aptera.us/discovery-center/
- group: commercial
  title: ''
  type: Pricing
  url: https://aptera.us/reserve/
- group: start
  title: ''
  type: SignUp
  url: https://aptera.us/reserve/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aptera.us/terms-of-service/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://aptera.us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aptera.us/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://aptera.us/careers/
- group: company
  title: ''
  type: PressRoom
  url: https://aptera.us/media-room/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.aptera.us/
- group: other
  title: ''
  type: Store
  url: https://shop.aptera.us/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/aptera-motors_stock/
created: '2026-08-02'
description: 'Aptera Motors Corp. (Nasdaq: SEV) is a Carlsbad, California solar electric vehicle manufacturer founded by Steve Fambro and Chris Anthony. The company builds a three-wheeled, two-seat enclosed autocycle covered in roughly 700 watts of integrated solar cells, designed to add up to 40 miles of range per day from sunlight alone and to travel up to 10,000 miles a year on free solar power, with a 400-mile battery range on the Launch Edition, over 320 MPGe efficiency, a ~2,200 lb curb weight and 0-60 mph in under six seconds. Aptera sells reservations direct to consumers through its own configurator, runs a branded Shopify merchandise storefront, and has committed to open-source driver assistance by integrating comma.ai openpilot into the vehicle. Aptera publishes no public developer program, API documentation, or machine-readable API contract as of this enrichment pass.'
image: https://i0.wp.com/aptera.us/wp-content/uploads/2026/04/website_pic_og.jpg
layout: provider
mcp_servers:
- description: ''
  name: aptera-motors-mcp.yml
  slug: aptera-motors-mcpyml
modified: '2026-08-02'
name: Aptera Motors
nav: Providers
network: true
overview: 'Aptera Motors publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Electric Vehicles, Solar, and Manufacturing.


  Aptera Motors'' developer surface includes authentication, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 82
scopes:
- name: Aptera Motors Scopes
  scope_count: 4
  slug: aptera-motors-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 24.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aptera-motors/refs/heads/main/screenshots/aptera-motors-2026-08-07T161526.png
security:
- kind: authentication
  name: Aptera Motors Authentication
  slug: aptera-motors-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Aptera Motors Domain Security
  slug: aptera-motors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aptera-motors
tags:
- Company
- Automotive
- Electric Vehicles
- Solar
- Manufacturing
- Clean Energy
- Transportation
- Consumer Products
- Mobility
website: https://aptera.us/
---

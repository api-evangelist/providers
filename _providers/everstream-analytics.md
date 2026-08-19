---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Everstream Analytics platform API surface (marketed as the Reveal API for real-time incident risk on entities, locations and lanes, and the Explore API for long-range planning data). It powers the
  name: Everstream Analytics Platform API
  slug: everstream-analytics-platform-api
artifact_total: 5
asyncapis:
- description: ''
  name: Everstream Analytics Webhooks
  slug: everstream-analytics-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/everstream-analytics-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everstream-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.everstream.ai/
- group: other
  title: ''
  type: Company
  url: https://www.everstream.ai/company/about-everstream/
- group: company
  title: ''
  type: Blog
  url: https://www.everstream.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.everstream.ai/feed/
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.everstream.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.everstream.ai/company/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Everstream-Analytics
- group: start
  title: ''
  type: Login
  url: https://us1.apps.everstream.ai/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.everstream.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: ServiceAgreement
  url: https://www.everstream.ai/everstream-analytics-service-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.everstream.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.everstream.ai/articles/everstreams-new-soc-2-compliance-enhances-supply-chain-security/
- group: design
  title: ''
  type: Conformance
  url: conformance/everstream-analytics-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/everstream-analytics-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/everstream-analytics-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/everstream-analytics-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/everstream-analytics-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/everstream-analytics-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/everstream-analytics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everstream-analytics-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/everstream-analytics_stock/
created: '2026-08-04'
description: Everstream Analytics is a supply chain risk analytics and intelligence company whose platform — grown out of DHL's innovation labs — continuously monitors global supply networks and scores risk across suppliers, sites, materials, lanes and shipments. The platform spans global monitoring and alerting, risk assessment and scoring, sub-tier and n-tier network mapping, applied meteorology and weather intelligence, and regulatory/ESG compliance screening (LkSG, CSDDD, UFLPA, CTPAT). Risk intelligence is delivered into customer systems through an Insights-to-Action integration layer offering API connectivity with bidirectional flows, event-driven webhooks, and SFTP batch transfer, with named connectors into SAP Integrated Business Planning, SAP Business Network for Logistics, Oracle TMS, Kinaxis and other planning, sourcing and visibility systems. The API surface (marketed as the Reveal API and Explore API) is documented for customers behind authentication; no public OpenAPI, developer
  portal or SDK has been published as of this profile.
image: https://www.everstream.ai/wp-content/uploads/2022/06/cropped-everstream-favicon-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: everstream-analytics-mcp.yml
  slug: everstream-analytics-mcpyml
modified: '2026-08-04'
name: Everstream Analytics
nav: Providers
network: true
overview: 'Everstream Analytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Supply Chain Risk, Risk Management, and Logistics.


  The Everstream Analytics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Everstream Analytics'' developer surface includes engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 33.3
  delta: -4.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 37.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everstream-analytics/refs/heads/main/screenshots/everstream-analytics-2026-08-07T165038.png
security:
- kind: authentication
  name: Everstream Analytics Authentication
  slug: everstream-analytics-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Everstream Analytics Domain Security
  slug: everstream-analytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: everstream-analytics
tags:
- Company
- Supply Chain
- Supply Chain Risk
- Risk Management
- Logistics
- Analytics
- Weather Intelligence
- Procurement
- Compliance
- Artificial Intelligence
website: https://www.everstream.ai/
---

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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Fever Agentic Access
  operation_count: 13
  slug: fever-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 5
apis:
- description: This endpoint is used to authenticate a user. It requires a username and password to be passed in the request body. If the user is authenticated successfully, a token is returned in the response body.
  name: Fever Authentication API
  slug: fever-authentication-api
- description: These endpoints provide an interface to extract the data available in FeverZone reports. The delay of the data is less than 15 minutes from reality. The route `/feverzone/sales-by-reseller` allows the
  name: Fever FeverZone API
  slug: fever-feverzone-api
- description: 'These endpoints enable to access order-item data. ## Filtering Options The endpoint supports filtering by: | Parameter | Type | Description | |-----------|------|-------------| | `order_ids` | array[i'
  name: Fever Order Items API
  slug: fever-order-items-api
- description: 'The goal of the Plan endpoint is to provide all information about the plans/events/experiences/listings organised by a partner. The delay of the data is less than 10 minutes from reality. ## Model doc'
  name: Fever Plans API
  slug: fever-plans-api
- description: 'The goal of the Session Endpoint is to provide all information about the session (or ticket types) of a plan. The delay of the data is less than 10 minutes from reality. ## Request filters `POST /v1/s'
  name: Fever Sessions API
  slug: fever-sessions-api
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.feverup.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.feverup.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://data-reporting-api.prod.feverup.com/v1/redoc
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fever-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fever-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fever-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/fever-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fever-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fever-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fever-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fever-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fever-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.data-reporting-api.prod.feverup.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/fever-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fever-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fever-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://fever.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://feverup.com/legal/terms_en.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://feverup.com/legal/privacy_en.html
- group: company
  title: ''
  type: Website
  url: https://www.feverup.com
created: '2026-07-17'
description: 'Fever is a global live-entertainment discovery and ticketing platform that helps millions of people find events, activities and experiences in their city, and gives venues and partners the tools to sell and analyze tickets. For developers Fever exposes two public surfaces: an official Model Context Protocol (MCP) server over its real-time global event catalog (tools search_cities and search_events, OAuth 2.0 with PKCE), and a partner-facing Reporting API delivering in-depth event sales data (orders, tickets, financials, plan and session details) for CRM, BI, data-warehouse and ERP integration. Fever is backed by Accel and General Catalyst.'
image: https://feverup.com/_astro/og-image-fever.PfP_3GVw.jpg
layout: provider
mcp_servers:
- description: ''
  name: fever-mcp.yml
  slug: fever-mcpyml
modified: '2026-07-19'
name: Fever
nav: Providers
network: true
overview: 'Fever publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, FeverZone API, Order Items API, and 2 more. Tagged areas include Company, Consumer, Live Entertainment, Events, and Ticketing.


  Fever''s developer surface includes documentation, API reference, authentication, support, and 17 more developer resources.'
random_paper: 74
rate_limits:
- limit_count: 0
  name: Fever Rate Limits
  slug: fever-rate-limits
score:
  band: thin
  composite: 38.7
  delta: -0.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 55.1
    developer_ergonomics: 49.5
    discoverability: 74.1
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/screenshots/fever-2026-07-25T214354.png
security:
- kind: authentication
  name: Fever Authentication
  slug: fever-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Fever Domain Security
  slug: fever-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fever
tags:
- Company
- Consumer
- Live Entertainment
- Events
- Ticketing
- Experiences
- Reporting
- MCP
website: https://www.feverup.com
---

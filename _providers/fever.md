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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fever Agentic Access
  operation_count: 13
  slug: fever-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 1
apis:
- baseURL: https://data-reporting-api.prod.feverup.com/v1
  baseurl_source: declared
  description: This endpoint is used to authenticate a user. It requires a username and password to be passed in the request body. If the user is authenticated successfully, a token is returned in the response body.
  name: Fever Authentication API
  slug: fever-authentication-api
- baseURL: https://data-reporting-api.prod.feverup.com/v1
  baseurl_source: declared
  description: These endpoints provide an interface to extract the data available in FeverZone reports. The delay of the data is less than 15 minutes from reality. The route `/feverzone/sales-by-reseller` allows the
  name: Fever FeverZone API
  slug: fever-feverzone-api
- baseURL: https://data-reporting-api.prod.feverup.com/v1
  baseurl_source: declared
  description: 'These endpoints enable to access order-item data. ## Filtering Options The endpoint supports filtering by: | Parameter | Type | Description | |-----------|------|-------------| | `order_ids` | array[i'
  name: Fever Order Items API
  slug: fever-order-items-api
- baseURL: https://data-reporting-api.prod.feverup.com/v1
  baseurl_source: declared
  description: 'The goal of the Plan endpoint is to provide all information about the plans/events/experiences/listings organised by a partner. The delay of the data is less than 10 minutes from reality. ## Model doc'
  name: Fever Plans API
  slug: fever-plans-api
- baseURL: https://data-reporting-api.prod.feverup.com/v1
  baseurl_source: declared
  description: 'The goal of the Session Endpoint is to provide all information about the session (or ticket types) of a plan. The delay of the data is less than 10 minutes from reality. ## Request filters `POST /v1/s'
  name: Fever Sessions API
  slug: fever-sessions-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fever - Reporting Authentication API
  slug: open-fever-authentication-api
- collection_type: open
  name: Fever - Reporting Authentication FeverZone API
  slug: open-fever-feverzone-api
- collection_type: open
  name: Fever - Reporting Authentication Order Items API
  slug: open-fever-order-items-api
- collection_type: open
  name: Fever - Reporting Authentication Plans API
  slug: open-fever-plans-api
- collection_type: open
  name: Fever - Reporting Authentication Sessions API
  slug: open-fever-sessions-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/overlays/fever-reporting-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fever-reporting-api-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/mcp/fever-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fever-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/well-known/fever-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fever-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/llms/fever-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fever-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/authentication/fever-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fever-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/agentic-access/fever-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fever-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/errors/fever-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fever-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/conventions/fever-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fever-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/rate-limits/fever-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fever-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/lifecycle/fever-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fever-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.data-reporting-api.prod.feverup.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/conformance/fever-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fever-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/data-model/fever-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fever-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fever/refs/heads/main/security/fever-domain-security.yml
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
- description: Official Fever MCP server exposing Fever's global live-entertainment event catalog to MCP-compatible clients (Claude Desktop, Cursor, Windsurf, Claude Code). Data is real-time, updated at the same rat
  name: Fever MCP Server
  slug: fever-mcp-server
modified: '2026-07-19'
name: Fever
nav: Providers
network: true
overview: 'Fever publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, FeverZone API, Order Items API, and 2 more. Tagged areas include Company, Consumer, Live Entertainment, Event, and Ticketing.


  Fever''s developer surface includes documentation, API reference, authentication, support, and 18 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 2
  name: Fever Rate Limits
  slug: fever-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 45.3
    developer_ergonomics: 25.6
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 33.1
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Event
- Ticketing
- Experience
- Reporting
- MCP
website: https://www.feverup.com
---

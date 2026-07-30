---
access_model:
  confidence: high
  label: Free · Self-serve registration
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - authentication
  - documentation
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: RESTful access to ERCOT Market Information List (EMIL) public data products — 106 documented endpoints spanning real-time and day-ahead locational marginal prices, settlement point prices, SCED system
  name: ERCOT Public Data API
  slug: ercot-public-data-api
- description: Energy Storage Resource public data, launched May 29, 2025 per the ERCOT Public Data API release notes, beginning with four-second ESR charging MW telemetry (GET /rptesr-m/4_sec_esr_charging_mw). Docu
  name: ERCOT ESR Public Data API
  slug: ercot-esr-public-data-api
- description: ERCOT's SOAP web-services estate for Nodal market participants — the Market Information Service, Market Transaction Service (bid and offer submission via BidSet), Resource Parameter Transaction Servic
  name: ERCOT Web Services (EWS)
  slug: ercot-web-services
- description: SOAP API over MarkeTrak, ERCOT's retail-market issue tracking system, supporting QueryList, QueryDetail, Update, and Submit operations against retail transaction issues. Applications must pass ERCOT c
  name: ERCOT MarkeTrak API
  slug: ercot-marketrak-api
- description: 'SOAP web service supporting Texas Standard Electronic Transactions (TX SET) between ERCOT, Transmission and Distribution Service Providers, and Retail Electric Providers — the machinery behind retail '
  name: ERCOT Retail API
  slug: ercot-retail-api
artifact_total: 11
asyncapis:
- description: ''
  name: Ercot Ews Notifications
  slug: ercot-ews-notifications
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ercot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ercot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ercot-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ercot-well-known.yml
- group: other
  title: ''
  type: OpenIDConfiguration
  url: well-known/ercot-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/ercot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ercot-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ercot-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ercot-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.ercot.com/applications/pubapi/deprecation-notices/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ercot-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ercot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ercot-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ercot-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ercot-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ercot-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ercot-ews-notifications.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ercot-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ercot.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ercot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ercot.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apiexplorer.ercot.com/api-details#api=pubapi-apim-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ercot.com/applications/pubapi/user-guide/registration-and-authentication/
- group: other
  title: ''
  type: APIExplorer
  url: https://apiexplorer.ercot.com/
- group: start
  title: ''
  type: SignUp
  url: https://apiexplorer.ercot.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.ercot.com/support/support/
- group: operate
  title: ''
  type: Community
  url: https://developer.ercot.com/discussion_forums/discussion/
- group: commercial
  title: ''
  type: Plans
  url: https://apiexplorer.ercot.com/products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ercot.com/help/terms/data-portal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ercot.com/help/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ercot
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ercot/api-specs
- group: other
  title: ''
  type: OpenData
  url: https://data.ercot.com/
- group: other
  title: ''
  type: OpenData
  url: https://www.ercot.com/mp/data-products
- group: operate
  title: ''
  type: Issues
  url: https://github.com/ercot/api-specs/issues
created: '2026-07-27'
description: 'The Electric Reliability Council of Texas (ERCOT) is the independent system operator that manages the flow of electric power to roughly 27 million Texas customers on the ERCOT Interconnection, running the wholesale Day-Ahead and Real-Time energy markets, ancillary services, congestion revenue rights, and retail switching for the competitive Texas market. Its home market is the United States (Texas). ERCOT sits at the wholesale/system-operator layer of the energy value chain, upstream of the transmission and distribution utilities (Oncor, CenterPoint, AEP Texas, TNMP) and the retail electric providers that serve end customers. Its API posture is a clean split: market and grid data are genuinely open — ERCOT publishes a real, versioned OpenAPI 3.0 for the Public Data API covering 106 EMIL data-product endpoints (locational marginal prices, settlement point prices, system load, wind and solar production, ancillary services, outage capacity), and the Market Information System still
  serves public report archives anonymously with no account at all. Consumer energy data is a different story: ERCOT operates no consumer usage API and implements no Green Button / ESPI surface. Texas residential interval data lives in Smart Meter Texas, which is operated by the joint Transmission and Distribution Utilities under PUCT oversight, not by ERCOT. The market-participant SOAP estate (ERCOT Web Services, MarkeTrak, Retail API) is documented publicly on GitHub but reachable only by certified market participants.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: ercot-mcp.yml
  slug: ercot-mcpyml
modified: '2026-07-27'
name: ERCOT
nav: Providers
network: true
overview: 'ERCOT publishes 1 API on the [APIs.io](https://apis.io/) network: Public Data API. Tagged areas include Energy, United States, Electricity, Energy Markets, and Grid.


  The ERCOT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ERCOT''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, signup flow, support, and 29 more developer resources.'
random_paper: 49
rate_limits:
- limit_count: 2
  name: Ercot Rate Limits
  slug: ercot-rate-limits
scopes:
- name: Ercot Scopes
  scope_count: 3
  slug: ercot-scopes
  summary_line: 3 scopes · password
score:
  band: developing
  composite: 49.1
  delta: -5.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 53.8
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 57.9
  previous_composite: 55.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Ercot Authentication
  slug: ercot-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Ercot Domain Security
  slug: ercot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ercot
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- System Operator
- Texas
- Renewables
- Demand Response
- Open Data
website: https://www.ercot.com/
---

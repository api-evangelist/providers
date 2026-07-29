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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
api_count: 12
apis:
- description: The Analytics API from Base Operations — 2 operation(s) for analytics.
  name: Base Operations Analytics API
  slug: base-operations-analytics-api
- description: The Base Score API from Base Operations — 9 operation(s) for base score.
  name: Base Operations Base Score API
  slug: base-operations-base-score-api
- description: The Change Detection API from Base Operations — 13 operation(s) for change detection.
  name: Base Operations Change Detection API
  slug: base-operations-change-detection-api
- description: The Key Takeaways API from Base Operations — 4 operation(s) for key takeaways.
  name: Base Operations Key Takeaways API
  slug: base-operations-key-takeaways-api
- description: The Public Charts API from Base Operations — 4 operation(s) for public charts.
  name: Base Operations Public Charts API
  slug: base-operations-public-charts-api
- description: The Radius Charts API from Base Operations — 9 operation(s) for radius charts.
  name: Base Operations Radius Charts API
  slug: base-operations-radius-charts-api
- description: The Saved Location Charts API from Base Operations — 10 operation(s) for saved location charts.
  name: Base Operations Saved Location Charts API
  slug: base-operations-saved-location-charts-api
- description: The Saved Location Radius Charts API from Base Operations — 6 operation(s) for saved location radius charts.
  name: Base Operations Saved Location Radius Charts API
  slug: base-operations-saved-location-radius-charts-api
- description: The Saved Locations API from Base Operations — 4 operation(s) for saved locations.
  name: Base Operations Saved Locations API
  slug: base-operations-saved-locations-api
- description: The Source Categories API from Base Operations — 2 operation(s) for source categories.
  name: Base Operations Source Categories API
  slug: base-operations-source-categories-api
- description: The Threat Categories API from Base Operations — 2 operation(s) for threat categories.
  name: Base Operations Threat Categories API
  slug: base-operations-threat-categories-api
- description: The Threats API from Base Operations — 6 operation(s) for threats.
  name: Base Operations Threats API
  slug: base-operations-threats-api
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.baseoperations.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.baseoperationsenterprise.com/public
- group: docs
  title: ''
  type: Documentation
  url: https://api.baseoperationsenterprise.com/public
- group: docs
  title: ''
  type: APIReference
  url: https://api.baseoperationsenterprise.com/public
- group: commercial
  title: ''
  type: Pricing
  url: https://www.baseoperations.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.baseoperations.com/demo
- group: start
  title: ''
  type: Login
  url: https://www.baseoperationsenterprise.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@baseoperations.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baseoperations.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baseoperations.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.drata.com/trust/2945944b-fdb8-4878-b807-03eea4229b8d
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baseoperations
- group: company
  title: ''
  type: Blog
  url: https://www.baseoperations.com/resources
- group: auth
  title: ''
  type: Authentication
  url: authentication/base-operations-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/base-operations-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/base-operations-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/base-operations-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/base-operations-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/base-operations-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/base-operations-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/base-operations-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/base-operations-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/base-operations-llms.txt
created: '2026-07-17'
description: Base Operations provides street-level threat intelligence for corporate, government, and law-enforcement security teams. Its platform validates crime, violence, unrest, and sUAS-incursion data from 25,000+ OSINT sources across 5,000+ global cities (99% of the US) and distills it into BaseScore, a transparent 0-100 risk metric comparable at country, city, district, and sub-mile (0.1 mile) granularity. The Customer API exposes BaseScore ratings, threat summaries, time-series trends, forecasting, change analysis, and saved locations over a REST interface authenticated with an X-API-KEY header, returning JSON so teams can integrate standardized risk scores directly into their own risk models, travel-security, event-security, and site-selection workflows.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/base-operations.png
layout: provider
mcp_servers:
- description: ''
  name: base-operations-mcp.yml
  slug: base-operations-mcpyml
modified: '2026-07-18'
name: Base Operations
nav: Providers
network: true
overview: 'Base Operations publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Base Score API, Change Detection API, and 9 more. Tagged areas include Company, Threat Intelligence, Security, Risk Management, and Physical Security.


  Base Operations'' developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 28
score:
  band: developing
  composite: 42.8
  delta: -2.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 52.2
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 45.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/base-operations/refs/heads/main/screenshots/base-operations-2026-07-25T202413.png
security:
- kind: authentication
  name: Base Operations Authentication
  slug: base-operations-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Base Operations Domain Security
  slug: base-operations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Base Operations Trust Center
  slug: base-operations-trust-center
  summary_line: trust center published
slug: base-operations
tags:
- Company
- Threat Intelligence
- Security
- Risk Management
- Physical Security
- Crime Data
- Geospatial
- Public Safety
- Risk Scoring
website: https://www.baseoperations.com/
---

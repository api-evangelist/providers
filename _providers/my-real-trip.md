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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Marketing-partner REST API for MyRealTrip. Search flights (domestic and international, lowest-fare calendars), accommodations, and tours/tickets; generate trackable MyLink short URLs; and retrieve rev
  name: MyRealTrip Partner API
  slug: myrealtrip-partner-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.myrealtrip.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.myrealtrip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.myrealtrip.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.myrealtrip.com/#gettingstarted
- group: operate
  title: ''
  type: Support
  url: https://support.myrealtrip.com/inquiry
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myrealtrip
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auth.myrealtrip.com/terms/policyAgreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auth.myrealtrip.com/terms/common/privacy
- group: start
  title: ''
  type: SignUp
  url: https://partner.myrealtrip.com/welcome
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/my-real-trip-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/my-real-trip-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/my-real-trip-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/my-real-trip-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/my-real-trip-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/my-real-trip-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/my-real-trip-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/my-real-trip-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/my-real-trip-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/my-real-trip-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: My Real Trip (마이리얼트립) is South Korea's largest online travel platform, founded in 2012, selling flights, stays, tours, tickets, and activities across 680+ cities in 80+ countries to roughly 5 million monthly active users. For developers it publishes a Partner API (partner-ext-api.myrealtrip.com) that lets marketing/affiliate partners search products, generate trackable MyLink short links, and pull revenue and reservation reports, secured with a Bearer API key. It also operates an official public Model Context Protocol (MCP) server that exposes real-time flight, stay, and tour/activity search to AI assistants such as Claude, Cursor, and Gemini CLI.
image: https://dffoxz5he03rp.cloudfront.net/logos/mrt_main_og_image.png
layout: provider
mcp_servers:
- description: ''
  name: my-real-trip-mcp.yml
  slug: my-real-trip-mcpyml
modified: '2026-07-20'
name: My Real Trip
nav: Providers
network: true
overview: 'My Real Trip publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Travel, Tourism, and Flights.


  My Real Trip''s developer surface includes documentation, getting-started guide, support, signup flow, authentication, sandbox, and 14 more developer resources.'
random_paper: 144
rate_limits:
- limit_count: 14
  name: My Real Trip Rate Limits
  slug: my-real-trip-rate-limits
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 60.3
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 31.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/my-real-trip/refs/heads/main/screenshots/my-real-trip-2026-08-07T184503.png
security:
- kind: authentication
  name: My Real Trip Authentication
  slug: my-real-trip-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: My Real Trip Domain Security
  slug: my-real-trip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: my-real-trip
tags:
- Company
- Consumer
- Travel
- Tourism
- Flights
- Accommodation
- Tours and Activities
- Affiliate
- MCP
- South Korea
website: https://www.myrealtrip.com/
---

---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The HyperTrack REST API for Orders, Workers, Places, Routes, Visits, Geotags, Nearby search, Tracking views and Export jobs. Authenticated with OAuth 2.0 client_credentials (or HTTP Basic with Account
  name: HyperTrack API
  slug: hypertrack-api
artifact_total: 7
asyncapis:
- description: ''
  name: Hypertrack Events Webhooks
  slug: hypertrack-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://hypertrack.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hypertrack.com/docs/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://hypertrack.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://hypertrack.com/reference/get-orders
- group: start
  title: ''
  type: GettingStarted
  url: https://hypertrack.com/docs/build-your-app
- group: operate
  title: ''
  type: Support
  url: https://hypertrack.com/contact
- group: company
  title: ''
  type: Blog
  url: https://stories.hypertrack.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://stories.hypertrack.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hypertrack
- group: commercial
  title: ''
  type: Pricing
  url: https://hypertrack.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.hypertrack.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.hypertrack.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hypertrack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hypertrack.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hypertrack.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/hypertrack/hypertrack/documentation/krztgzd/hypertrack-api
- group: build
  title: ''
  type: Packages
  url: packages/hypertrack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hypertrack-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hypertrack-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hypertrack-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hypertrack-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hypertrack-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hypertrack-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hypertrack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hypertrack-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hypertrack-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hypertrack-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/hypertrack-components.yml
created: '2026-08-22'
description: HyperTrack is a location-intelligence platform for shift work, field service and last-mile delivery. Its mobile SDKs (iOS, Android, React Native, Flutter, Expo, Ionic Capacitor and .NET MAUI) collect ground-truth location from a worker's device, and its REST API — the HyperTrack API at https://v3.api.hypertrack.com — turns that stream into Orders, Workers, Places, Routes, Visits, Geotags and Nearby search, plus webhooks for order, route, worker, geofence, outage and trip events. Companies use it to verify time and attendance, detect no-call-no-show risk, plan and optimise routes, and close out shifts for pay and billing. HyperTrack publishes a machine-readable OpenAPI 3.0.3 definition, an llms.txt index, an npm-distributed MCP server, and an open-source Agent Skill for coding agents.
image: https://hypertrack.com/images/og-home.png
layout: provider
mcp_servers:
- description: ''
  name: HyperTrack MCP Server
  slug: hypertrack-mcp-server
modified: '2026-08-22'
name: HyperTrack
nav: Providers
network: true
overview: 'HyperTrack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location, Geolocation, Tracking, and Logistics.


  The HyperTrack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HyperTrack''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Hypertrack Plans Pricing
  plan_count: 7
  slug: hypertrack-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Hypertrack Rate Limits
  slug: hypertrack-rate-limits
score:
  band: strong
  composite: 59.1
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 30.3
    contract_quality: 60.0
    developer_ergonomics: 66.7
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 34.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Hypertrack Authentication
  slug: hypertrack-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Hypertrack Domain Security
  slug: hypertrack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hypertrack
tags:
- Company
- Location
- Geolocation
- Tracking
- Logistics
- Last Mile Delivery
- Field Service
- Workforce
- Time and Attendance
- Mobile SDK
- Geofencing
- Routing
website: https://hypertrack.com/
---

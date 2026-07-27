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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Kadence Agentic Access
  operation_count: 27
  slug: kadence-agentic-access
  summary_line: 27 operations · 6 acting
api_count: 11
apis:
- description: The Bookable Day API from Kadence — 2 operation(s) for bookable day.
  name: Kadence Bookable Day API
  slug: kadence-bookable-day-api
- description: The Bookable Onsite Pass API from Kadence — 1 operation(s) for bookable onsite pass.
  name: Kadence Bookable Onsite Pass API
  slug: kadence-bookable-onsite-pass-api
- description: The Bookable Space API from Kadence — 1 operation(s) for bookable space.
  name: Kadence Bookable Space API
  slug: kadence-bookable-space-api
- description: The Booking API from Kadence — 6 operation(s) for booking.
  name: Kadence Booking API
  slug: kadence-booking-api
- description: The Building API from Kadence — 2 operation(s) for building.
  name: Kadence Building API
  slug: kadence-building-api
- description: The Floor API from Kadence — 2 operation(s) for floor.
  name: Kadence Floor API
  slug: kadence-floor-api
- description: The Neighborhood API from Kadence — 2 operation(s) for neighborhood.
  name: Kadence Neighborhood API
  slug: kadence-neighborhood-api
- description: The Space API from Kadence — 2 operation(s) for space.
  name: Kadence Space API
  slug: kadence-space-api
- description: The User API from Kadence — 3 operation(s) for user.
  name: Kadence User API
  slug: kadence-user-api
- description: The Visit API from Kadence — 2 operation(s) for visit.
  name: Kadence Visit API
  slug: kadence-visit-api
- description: The Visitor API from Kadence — 2 operation(s) for visitor.
  name: Kadence Visitor API
  slug: kadence-visitor-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://kadence.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.kadence.co/kb/en/api-318752
- group: docs
  title: ''
  type: Documentation
  url: https://help.kadence.co/kb/en/api-318752
- group: docs
  title: ''
  type: APIReference
  url: https://api.kadence.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.kadence.co/kb/en/guide/api-getting-started-developer-guide-yUYh7DBxBW/
- group: operate
  title: ''
  type: Support
  url: https://help.kadence.co
- group: company
  title: ''
  type: Blog
  url: https://kadence.co/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wearekadence
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/wearekadence/kadence-public-api-examples
- group: commercial
  title: ''
  type: Pricing
  url: https://kadence.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.onkadence.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kadence.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kadence.co/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kadence.co
- group: auth
  title: ''
  type: Compliance
  url: https://kadence.co/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/kadence-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kadence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kadence-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kadence-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kadence-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kadence-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kadence-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kadence-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kadence-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kadence-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kadence-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/kadence-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kadence-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kadence-domain-security.yml
created: '2026-07-17'
description: Kadence is a workplace management platform for hybrid work, helping organizations coordinate people, spaces, and workplace strategy through desk and room booking, visitor management, space management, and workplace analytics. Its Public API (OpenAPI 3.1, v1.2.0) lets applications read and manage buildings, floors, neighborhoods, spaces, bookings, check-ins and check-outs, users, visits, and visitors. The API is an API Platform (Hydra / JSON-LD) service secured with OAuth 2.0 client-credentials (scope "public"), with production hosts at api.onkadence.co and api.us.onkadence.co. Kadence was surfaced as a Techstars portfolio company and enriched into the API Evangelist network from its public developer surface.
image: https://kadence.co/wp-content/uploads/2025/05/kadence-social-share-image.png
layout: provider
mcp_servers:
- description: ''
  name: kadence-mcp.yml
  slug: kadence-mcpyml
modified: '2026-07-19'
name: Kadence
nav: Providers
network: true
overview: 'Kadence publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Bookable Day API, Bookable Onsite Pass API, Bookable Space API, and 8 more. Tagged areas include Company, Workplace, Hybrid Work, Desk Booking, and Room Booking.


  Kadence''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 35
scopes:
- name: Kadence Scopes
  scope_count: 1
  slug: kadence-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.1
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 53.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kadence/refs/heads/main/screenshots/kadence-2026-07-25T223408.png
security:
- kind: authentication
  name: Kadence Authentication
  slug: kadence-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Kadence Domain Security
  slug: kadence-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Kadence Trust Center
  slug: kadence-trust-center
  summary_line: SOC 2 Type II, ISO 27001, Cyber Essentials, GDPR, CCPA, OWASP MASVS
slug: kadence
tags:
- Company
- Workplace
- Hybrid Work
- Desk Booking
- Room Booking
- Space Management
- Visitor Management
- Workplace Analytics
- Facilities
- OAuth
website: https://kadence.co/
---

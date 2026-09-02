---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Lafourchette Agentic Access
  operation_count: 21
  slug: lafourchette-agentic-access
  summary_line: 21 operations · 10 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Booking flow API from LaFourchette — 8 operation(s) for booking flow.
  name: LaFourchette Booking flow API
  slug: lafourchette-booking-flow-api
- description: The Data API from LaFourchette — 4 operation(s) for data.
  name: LaFourchette Data API
  slug: lafourchette-data-api
- description: The Phone API from LaFourchette — 3 operation(s) for phone.
  name: LaFourchette Phone API
  slug: lafourchette-phone-api
- description: The Review flow API from LaFourchette — 3 operation(s) for review flow.
  name: LaFourchette Review flow API
  slug: lafourchette-review-flow-api
- description: The v1 API from LaFourchette — 3 operation(s) for v1.
  name: LaFourchette V1 API
  slug: lafourchette-v1-api
artifact_total: 13
asyncapis:
- description: ''
  name: Lafourchette Webhooks
  slug: lafourchette-webhooks
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/tripadvisor/
- group: other
  title: ''
  type: Overlay
  url: overlays/lafourchette-b2b-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lafourchette-pos-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lafourchette-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lafourchette-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lafourchette-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.thefork.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.thefork.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thefork.io/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thefork.io/B2B-API/API%20specifications/get-v-1-customers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thefork.io/getting-started
- group: other
  title: ''
  type: BestPractices
  url: https://docs.thefork.io/best-practices
- group: operate
  title: ''
  type: Support
  url: https://support.theforkmanager.com/s/?language=en_GB
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lafourchette
- group: commercial
  title: ''
  type: Pricing
  url: https://www.theforkmanager.com/en/restaurant-software-price
- group: start
  title: ''
  type: SignUp
  url: https://www.theforkmanager.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.thefork.io/pdf/LaFourchette-Partners-API-Licence-2.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thefork.com/legal
- group: build
  title: ''
  type: Packages
  url: packages/lafourchette-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lafourchette-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lafourchette-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lafourchette-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/lafourchette-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lafourchette-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lafourchette-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.thefork.io/getting-started
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lafourchette-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lafourchette-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lafourchette-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lafourchette-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lafourchette-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lafourchette-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lafourchette-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lafourchette-rate-limits.yml
created: '2026-08-17'
description: 'LA FOURCHETTE SAS, trading as TheFork, is the European restaurant-booking and restaurant-management platform founded in Paris in 2007 and acquired by TripAdvisor in 2014. It runs the consumer marketplace at thefork.com across a dozen European markets and the TheFork Manager (TFM) SaaS that restaurants use for reservations, table and floor management, reviews, loyalty ("Yums"), preset menus and payments. Its developer surface is published at docs.thefork.io and consists of two REST APIs: the B2B / Partners API (api.thefork.io/manager) used by restaurant groups, CRM platforms and booking-funnel partners to read customers, reservations and reviews and to drive availabilities, offers, timeslots and reservation lifecycle; and the POS API v1 (api.thefork.io/pos) used by point-of-sale vendors to register a POS instance and push closed-bill data back onto a reservation. A push webhook flow delivers customer, reservation and review events to partner endpoints. Credentials are issued
  by the integrations team; the B2B API uses an Auth0 client-credentials access token and the POS API an X-Api-Key header.'
image: https://docs.thefork.io/img/thefork_logo_2023_secondary.svg
layout: provider
mcp_servers:
- description: ''
  name: LaFourchette MCP Server
  slug: lafourchette-mcp-server
modified: '2026-08-17'
name: LaFourchette
nav: Providers
network: true
overview: 'LaFourchette publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Booking flow API, Data API, Phone API, and 2 more. Tagged areas include Company, Consumer, Restaurant, Reservations, and Booking.


  The LaFourchette catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LaFourchette''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Lafourchette Plans Pricing
  plan_count: 2
  slug: lafourchette-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Lafourchette Rate Limits
  slug: lafourchette-rate-limits
scopes:
- name: Lafourchette Scopes
  scope_count: 0
  slug: lafourchette-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 20.3
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Lafourchette Authentication
  slug: lafourchette-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Lafourchette Domain Security
  slug: lafourchette-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lafourchette
tags:
- Company
- Consumer
- Restaurant
- Reservations
- Booking
- Hospitality
- Point-of-Sale
- Reviews
- Marketplace
- Travel and Dining
- Webhook
- France
website: https://www.thefork.com/
---

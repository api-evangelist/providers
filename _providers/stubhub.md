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
    asyncapi_events: true
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
  score: 75.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Stubhub Agentic Access
  operation_count: 81
  slug: stubhub-agentic-access
  summary_line: 81 operations · 37 acting
api_count: 15
apis:
- description: The Addressess API from StubHub — 2 operation(s) for addressess.
  name: StubHub Addressess API
  slug: stubhub-addressess-api
- description: The Categories API from StubHub — 1 operation(s) for categories.
  name: StubHub Categories API
  slug: stubhub-categories-api
- description: The E-Tickets API from StubHub — 12 operation(s) for e-tickets.
  name: StubHub E-Tickets API
  slug: stubhub-e-tickets-api
- description: The Events API from StubHub — 7 operation(s) for events.
  name: StubHub Events API
  slug: stubhub-events-api
- description: The ListingConstraints API from StubHub — 3 operation(s) for listingconstraints.
  name: StubHub ListingConstraints API
  slug: stubhub-listingconstraints-api
- description: The PaymentMethods API from StubHub — 3 operation(s) for paymentmethods.
  name: StubHub PaymentMethods API
  slug: stubhub-paymentmethods-api
- description: The Payments API from StubHub — 3 operation(s) for payments.
  name: StubHub Payments API
  slug: stubhub-payments-api
- description: The Sales API from StubHub — 3 operation(s) for sales.
  name: StubHub Sales API
  slug: stubhub-sales-api
- description: The SellerEvents API from StubHub — 2 operation(s) for sellerevents.
  name: StubHub SellerEvents API
  slug: stubhub-sellerevents-api
- description: The SellerListings API from StubHub — 9 operation(s) for sellerlistings.
  name: StubHub SellerListings API
  slug: stubhub-sellerlistings-api
- description: The Shipments API from StubHub — 6 operation(s) for shipments.
  name: StubHub Shipments API
  slug: stubhub-shipments-api
- description: The TicketHolders API from StubHub — 1 operation(s) for ticketholders.
  name: StubHub TicketHolders API
  slug: stubhub-ticketholders-api
- description: The User API from StubHub — 1 operation(s) for user.
  name: StubHub User API
  slug: stubhub-user-api
- description: The Venues API from StubHub — 2 operation(s) for venues.
  name: StubHub Venues API
  slug: stubhub-venues-api
- description: The Webhooks API from StubHub — 3 operation(s) for webhooks.
  name: StubHub Webhooks API
  slug: stubhub-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Stubhub Webhooks
  slug: stubhub-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stubhub-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stubhub-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stubhub-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stubhub-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.stubhub.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.stubhub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.stubhub.com/docs/overview/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.stubhub.com/api-reference/account
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.stubhub.com/docs/authentication/basic-steps
- group: company
  title: ''
  type: Blog
  url: https://developer.stubhub.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:api.support@stubhub.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viagogo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stubhub.com/legal/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stubhub.com/
- group: build
  title: ''
  type: Packages
  url: packages/stubhub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stubhub-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stubhub-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stubhub-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/stubhub-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stubhub-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stubhub-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stubhub-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stubhub-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stubhub-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stubhub-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/stubhub-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stubhub-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: StubHub is the world's largest secondary-market ticket marketplace, connecting buyers and sellers of tickets to sports, concerts, theater, and live events. Its official developer platform (developer.stubhub.com, migrated to a v2 API in 2022 on api.stubhub.net) exposes five partner-gated REST APIs — Account, Catalog, Inventory, Sales, and Webhooks — that let approved affiliate and seller-integration partners search events, create and manage seller listings, upload e-tickets, fulfill sales and shipments, view payments, and subscribe to event webhooks. All resources use the application/hal+json (HAL) media type and OAuth2 (client-credentials and authorization-code flows). StubHub is a viagogo company and its official GogoKit SDKs (.NET, Ruby) target the shared HAL API.
image: https://www.stubhub.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: stubhub-mcp.yml
  slug: stubhub-mcpyml
modified: '2026-07-21'
name: StubHub
nav: Providers
network: true
overview: 'StubHub publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Addressess API, Categories API, E-Tickets API, and 12 more. Tagged areas include Company, Marketplaces, Tickets, Events, and Ticketing.


  The StubHub catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StubHub''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, sandbox, and 21 more developer resources.'
random_paper: 0
scopes:
- name: Stubhub Scopes
  scope_count: 9
  slug: stubhub-scopes
  summary_line: 9 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 63.7
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 49.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Stubhub Authentication
  slug: stubhub-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Stubhub Domain Security
  slug: stubhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stubhub
tags:
- Company
- Marketplaces
- Tickets
- Events
- Ticketing
- Live Events
- Secondary Market
- E-commerce
- Sports
- Concerts
website: https://www.stubhub.com/
---

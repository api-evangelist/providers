---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: The Addresses API from viagogo — 2 operation(s) for addresses.
  name: viagogo Addresses API
  slug: viagogo-addresses-api
- description: View categories on the viagogo platform
  name: viagogo Categories API
  slug: viagogo-categories-api
- description: The E-Tickets API from viagogo — 13 operation(s) for e-tickets.
  name: viagogo E Tickets API
  slug: viagogo-e-tickets-api
- description: View events on the viagogo platform
  name: viagogo Events API
  slug: viagogo-events-api
- description: Manage instant liquidity offers (buyer bids) on the viagogo platform
  name: viagogo Listing Offers API
  slug: viagogo-listing-offers-api
- description: The ListingConstraints API from viagogo — 3 operation(s) for listingconstraints.
  name: viagogo Listing Constraints API
  slug: viagogo-listingconstraints-api
- description: The PaymentMethods API from viagogo — 1 operation(s) for paymentmethods.
  name: viagogo Payment Methods API
  slug: viagogo-paymentmethods-api
- description: The Payments API from viagogo — 3 operation(s) for payments.
  name: viagogo Payments API
  slug: viagogo-payments-api
- description: View your sales details and fulfill your sales.
  name: viagogo Sales API
  slug: viagogo-sales-api
- description: The SellerEvents API from viagogo — 2 operation(s) for sellerevents.
  name: viagogo Seller Events API
  slug: viagogo-sellerevents-api
- description: List tickets, update your listings and search your inventory.
  name: viagogo Seller Listings API
  slug: viagogo-sellerlistings-api
- description: Manage your inventory using identifiers from an external inventory management system.
  name: viagogo SellerListings (External Id) API
  slug: viagogo-sellerlistings-external-id-api
- description: Preview the changes you want to make to your inventory.
  name: viagogo SellerListings (Preview) API
  slug: viagogo-sellerlistings-preview-api
- description: The Shipments API from viagogo — 6 operation(s) for shipments.
  name: viagogo Shipments API
  slug: viagogo-shipments-api
- description: The TicketHolders API from viagogo — 1 operation(s) for ticketholders.
  name: viagogo Ticket Holders API
  slug: viagogo-ticketholders-api
- description: The TransferStatusProof API from viagogo — 1 operation(s) for transferstatusproof.
  name: viagogo Transfer Status Proof API
  slug: viagogo-transferstatusproof-api
- description: The User API from viagogo — 1 operation(s) for user.
  name: viagogo User API
  slug: viagogo-user-api
- description: View venue configurations on the viagogo platform
  name: viagogo Venue Configurations API
  slug: viagogo-venue-configurations-api
- description: View venues on the viagogo platform
  name: viagogo Venues API
  slug: viagogo-venues-api
- description: The Webhooks API from viagogo — 3 operation(s) for webhooks.
  name: viagogo Webhooks API
  slug: viagogo-webhooks-api
- description: When configuring a webhook, you can choose the topics you would like to receive payloads for. You should only subscribe to the specific topics that you plan on handling so that you can limit the numbe
  name: viagogo Topics API
  slug: viagogo-topics-api
artifact_total: 47
asyncapis:
- description: ''
  name: Viagogo Webhooks
  slug: viagogo-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: viagogo Account Addresses API
  slug: open-viagogo-addresses-api
- collection_type: open
  name: viagogo Catalog Categories API
  slug: open-viagogo-categories-api
- collection_type: open
  name: Viagogo E Tickets API
  slug: open-viagogo-e-tickets-api
- collection_type: open
  name: viagogo Catalog Events API
  slug: open-viagogo-events-api
- collection_type: open
  name: viagogo Catalog Listing Offers API
  slug: open-viagogo-listing-offers-api
- collection_type: open
  name: viagogo Inventory Listing Constraints API
  slug: open-viagogo-listingconstraints-api
- collection_type: open
  name: viagogo Account Payment Methods API
  slug: open-viagogo-paymentmethods-api
- collection_type: open
  name: viagogo Sales Payments API
  slug: open-viagogo-payments-api
- collection_type: open
  name: viagogo Sales API
  slug: open-viagogo-sales-api
- collection_type: open
  name: viagogo Inventory Seller Events API
  slug: open-viagogo-sellerevents-api
- collection_type: open
  name: viagogo Inventory Seller Listings API
  slug: open-viagogo-sellerlistings-api
- collection_type: open
  name: viagogo Inventory SellerListings (External Id) API
  slug: open-viagogo-sellerlistings-external-id-api
- collection_type: open
  name: Viagogo Shipments API
  slug: open-viagogo-shipments-api
- collection_type: open
  name: viagogo Sales Ticket Holders API
  slug: open-viagogo-ticketholders-api
- collection_type: open
  name: viagogo Webhooks Topics API
  slug: open-viagogo-topics-api
- collection_type: open
  name: viagogo Sales Transfer Status Proof API
  slug: open-viagogo-transferstatusproof-api
- collection_type: open
  name: viagogo Account User API
  slug: open-viagogo-user-api
- collection_type: open
  name: viagogo Catalog Venue Configurations API
  slug: open-viagogo-venue-configurations-api
- collection_type: open
  name: viagogo Catalog Venues API
  slug: open-viagogo-venues-api
- collection_type: open
  name: viagogo Webhooks API
  slug: open-viagogo-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/viagogo-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/viagogo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/viagogo-account-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.viagogo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.viagogo.net/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.viagogo.net/docs/overview/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.viagogo.net/api-reference/inventory
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.viagogo.net/docs/authentication/basic-steps
- group: operate
  title: ''
  type: Support
  url: https://support.viagogo.com/
- group: company
  title: ''
  type: Blog
  url: https://developer.viagogo.net/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viagogo
- group: start
  title: ''
  type: Login
  url: https://my.viagogo.com/secure/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viagogo.com/secure/help/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viagogo.com/secure/help/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/viagogo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/viagogo-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/viagogo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/viagogo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/viagogo-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/viagogo-openid-configuration.json
- group: start
  title: ''
  type: Sandbox
  url: sandbox/viagogo-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/viagogo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/viagogo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/viagogo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/viagogo-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/viagogo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/viagogo-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viagogo-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/viagogo-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viagogo-llms.txt
created: '2026-08-05'
description: viagogo is a global online ticket marketplace for live events — concerts, sport and theatre — operating in more than 90 countries and, since the 2020 acquisition of StubHub, part of StubHub Holdings. viagogo publishes a public developer program at developer.viagogo.net covering five OAuth2-secured HTTP APIs — Catalog (events, venues, categories and instant-liquidity listing offers), Account (users, addresses, payment methods), Inventory (seller listings, listing constraints, e-tickets and shipments), Sales (sales, payments, ticket holders, transfer proof) and Webhooks (topic subscriptions) — all served from api.viagogo.net over application/hal+json with a matching sandbox.api.viagogo.net environment, official GogoKit client libraries for .NET, Python, Ruby and PHP, and machine-readable OpenAPI 3.0 definitions synced nightly from the API host into the public docs repository.
image: https://img.vggcdn.net/img/assets/logo/viagogo_logo_apidocs.png
layout: provider
mcp_servers:
- description: ''
  name: viagogo MCP Server
  slug: viagogo-mcp-server
modified: '2026-08-05'
name: viagogo
nav: Providers
network: true
overview: 'viagogo publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Categories API, E Tickets API, and 18 more. Tagged areas include Company, Ticketing, Event, Marketplace, and Entertainment.


  The viagogo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  viagogo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 24 more developer resources.'
random_paper: 13
scopes:
- name: Viagogo Scopes
  scope_count: 17
  slug: viagogo-scopes
  summary_line: 17 scopes
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 57.3
    developer_ergonomics: 73.2
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 45.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/viagogo/refs/heads/main/screenshots/viagogo-2026-08-17T082740.png
security:
- kind: authentication
  name: Viagogo Authentication
  slug: viagogo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Viagogo Domain Security
  slug: viagogo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: viagogo
tags:
- Company
- Ticketing
- Event
- Marketplace
- Entertainment
- Secondary Market
- Commerce
- Travel And Leisure
website: https://www.viagogo.com/
---

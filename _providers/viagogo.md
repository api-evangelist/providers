---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: 'Read the viagogo event catalog — search and list categories, events and venues, resolve events by external platform identifier, map inbound event/venue/category requests onto the platform, read venue '
  name: viagogo Catalog API
  slug: viagogo-catalog-api
- description: Manage the authenticated viagogo user — read and update the user profile, list, create, update and delete addresses, and list the payment methods available for a listing.
  name: viagogo Account API
  slug: viagogo-account-api
- description: Manage seller inventory on the viagogo platform — create, preview, update and delete seller listings (by viagogo id or by your own external id), read listing constraints, create seller and requested e
  name: viagogo Inventory API
  slug: viagogo-inventory-api
- description: 'Work the seller side of a viagogo sale — list and read sales and recent updates, confirm, update or reject a sale, read ticket holder details, upload e-tickets and proof of transfer, print and update '
  name: viagogo Sales API
  slug: viagogo-sales-api
- description: 'Subscribe a server application to viagogo platform topics — create, read, update, delete and ping webhooks, each configured with a callback url, an Authorization header value and a set of topics such '
  name: viagogo Webhooks API
  slug: viagogo-webhooks-api
artifact_total: 9
asyncapis:
- description: ''
  name: Viagogo Webhooks
  slug: viagogo-webhooks
common:
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
modified: '2026-08-05'
name: viagogo
nav: Providers
network: true
overview: 'viagogo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Account API, Inventory API, and 2 more. Tagged areas include Company, Ticketing, Events, Marketplace, and Entertainment.


  The viagogo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  viagogo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 21 more developer resources.'
random_paper: 70
scopes:
- name: Viagogo Scopes
  scope_count: 17
  slug: viagogo-scopes
  summary_line: 17 scopes
score:
  band: developing
  composite: 49.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.9
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
- Events
- Marketplace
- Entertainment
- Secondary Market
- Commerce
- Travel and Leisure
website: https://www.viagogo.com/
---

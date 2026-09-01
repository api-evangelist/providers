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
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Blackbird Agentic Access
  operation_count: 25
  slug: blackbird-agentic-access
  summary_line: 25 operations · 5 acting
api_count: 1
apis:
- description: The App API from Blackbird — 1 operation(s) for app.
  name: Blackbird App API
  slug: blackbird-app-api
- description: The Challenges API from Blackbird — 1 operation(s) for challenges.
  name: Blackbird Challenges API
  slug: blackbird-challenges-api
- description: Filtered visit records.
  name: Blackbird Check-ins API
  slug: blackbird-check-ins-api
- description: Physical venues and open hours.
  name: Blackbird Locations API
  slug: blackbird-locations-api
- description: Per-(member, restaurant) loyalty records carrying check-in counts and tiers.
  name: Blackbird Memberships API
  slug: blackbird-memberships-api
- description: Payment Intents for FLY-funded payments.
  name: Blackbird Payments API
  slug: blackbird-payments-api
- description: Brand-level restaurant discovery.
  name: Blackbird Restaurants API
  slug: blackbird-restaurants-api
- description: The Rewards API from Blackbird — 2 operation(s) for rewards.
  name: Blackbird Rewards API
  slug: blackbird-rewards-api
- description: The Specials API from Blackbird — 1 operation(s) for specials.
  name: Blackbird Specials API
  slug: blackbird-specials-api
- description: The authenticated member — profile, status, wallets, tags, and check-in history. Subject resolved from the token.
  name: Blackbird Users API
  slug: blackbird-users-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flynet App API
  slug: open-blackbird-app-api
- collection_type: open
  name: Flynet App Challenges API
  slug: open-blackbird-challenges-api
- collection_type: open
  name: Flynet App Check-ins API
  slug: open-blackbird-check-ins-api
- collection_type: open
  name: Flynet App Locations API
  slug: open-blackbird-locations-api
- collection_type: open
  name: Flynet App Memberships API
  slug: open-blackbird-memberships-api
- collection_type: open
  name: Flynet App Payments API
  slug: open-blackbird-payments-api
- collection_type: open
  name: Flynet App Restaurants API
  slug: open-blackbird-restaurants-api
- collection_type: open
  name: Flynet App Rewards API
  slug: open-blackbird-rewards-api
- collection_type: open
  name: Flynet App Specials API
  slug: open-blackbird-specials-api
- collection_type: open
  name: Flynet App Users API
  slug: open-blackbird-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/blackbird-flynet-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://blackbird.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flynet.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flynet.org
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flynet.org/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flynet.org/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.flynet.org/resources/support
- group: company
  title: ''
  type: Blog
  url: https://www.thesupersonic.blackbird.xyz
- group: start
  title: ''
  type: SignUp
  url: https://docs.flynet.org/resources/request-access
- group: auth
  title: ''
  type: Authentication
  url: authentication/blackbird-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blackbird-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blackbird-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/blackbird-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blackbird-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blackbird-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/blackbird-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blackbird-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blackbird-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/blackbird-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/blackbird-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blackbird-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/blackbird-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blackbird-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blackbird-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blackbird-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blackbird-domain-security.yml
created: '2026-07-17'
description: Blackbird Labs is the membership network for restaurant lovers, founded by Eater and Resy co-founder Ben Leventhal. Its consumer app lets diners earn status, perks, and points at world-class restaurants and pay their check in FLY, Blackbird's loyalty token. Blackbird's developer platform is the Flynet API — read access to the dining network (restaurants, locations, check-ins, member identity, and memberships) plus FLY Payment Intents modeled on Stripe — backed by an OpenAPI spec, first-party TypeScript SDKs (@flynetdev/core and @flynetdev/react), two MCP servers, a published agent skill, and llms.txt. Flynet is a layer-3 network built on Coinbase's Base chain. Backed by a16z, dcvc, and multicoin-capital.
image: https://www.blackbird.xyz/opengraph-image.png
layout: provider
mcp_servers:
- description: Flynet (Blackbird) ships two official MCP servers. The Docs MCP is a hosted, remote HTTP server (Mintlify-hosted, no credentials) that lets any MCP-aware agent search the live Flynet docs. The API MCP
  name: Blackbird MCP Server
  slug: blackbird-mcp-server
modified: '2026-07-18'
name: Blackbird
nav: Providers
network: true
overview: 'Blackbird publishes 10 APIs on the [APIs.io](https://apis.io/) network, including App API, Challenges API, Check-ins API, and 7 more. Tagged areas include Company, Restaurant, Loyalty, Payments, and Dining.


  Blackbird''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 2
scopes:
- name: Blackbird Scopes
  scope_count: 9
  slug: blackbird-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blackbird/refs/heads/main/screenshots/blackbird-2026-07-25T203240.png
security:
- kind: authentication
  name: Blackbird Authentication
  slug: blackbird-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Blackbird Domain Security
  slug: blackbird-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blackbird
tags:
- Company
- Restaurant
- Loyalty
- Payments
- Dining
- Membership
- Crypto
- Blockchain
- Web3
website: https://blackbird.xyz
---

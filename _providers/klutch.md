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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Klutch Public API is a GraphQL API for the Klutch programmable credit card. It exposes enriched transaction history with filtering, cursor pagination and group-by aggregation; user-defined transac
  name: Klutch Public API
  slug: klutch-public-api
artifact_total: 6
asyncapis:
- description: ''
  name: Klutch Webhooks
  slug: klutch-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://klutchcard.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.klutchcard.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.klutchcard.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.klutchcard.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.klutchcard.com/tutorials
- group: build
  title: ''
  type: Postman
  url: https://api-docs.klutchcard.com/
- group: operate
  title: ''
  type: Support
  url: https://help.klutchcard.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.klutchcard.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.klutchcard.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KlutchCard
- group: commercial
  title: ''
  type: Pricing
  url: https://www.klutchcard.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.klutch.cards/apply/signup
- group: start
  title: ''
  type: Login
  url: https://app.klutch.cards/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klutchcard.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klutchcard.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/klutch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/klutch-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/klutch-cli.yml
- group: design
  title: ''
  type: Components
  url: components/klutch-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/klutch-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klutch-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klutch-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klutch-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/klutch-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klutch-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klutch-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klutch-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klutch-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/klutch-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/klutch-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/klutch-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klutch-domain-security.yml
created: '2026-07-17'
description: Klutch (Klutch Card) is a US consumer fintech that issues an "app-powered" programmable credit card — Klutch Credit (unsecured) and Klutch Spend (collateralized prepaid) — whose behavior is extended by user-installable Mini Apps. Its public GraphQL API lets developers and Mini App builders list and group enriched card transactions (including acquirer metadata such as MCC, entry mode, terminal type and card-present flags), create and lock virtual cards, author server-side transaction rules that accumulate or decline spend by filter, day of week or time of day, read balances, initiate ACH card payments, and render Mini App panels back into the Klutch mobile experience. Klutch ships a production and a sandbox GraphQL endpoint with transaction simulation mutations, OAuth 2.1 with PKCE and dynamic client registration, transaction webhooks, a developer CLI, a first-party JavaScript SDK and Mini App component library, and a remote MCP server that lets Claude and ChatGPT operate the
  card in natural language.
image: https://cdn.prod.website-files.com/660d6194e5d7f9c60a769ac1/664dff628523869c6ec161ad_image%2B2.jpg
layout: provider
mcp_servers:
- description: ''
  name: Klutch MCP Server
  slug: klutch-mcp-server
modified: '2026-07-19'
name: Klutch
nav: Providers
network: true
overview: 'Klutch publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Financial-Services, Fintech, Credit Cards, and Payments.


  The Klutch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Klutch''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 0
scopes:
- name: Klutch Scopes
  scope_count: 4
  slug: klutch-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 76.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 45.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klutch/refs/heads/main/screenshots/klutch-2026-07-25T223951.png
security:
- kind: authentication
  name: Klutch Authentication
  slug: klutch-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Klutch Domain Security
  slug: klutch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: klutch
tags:
- Company
- Financial-Services
- Fintech
- Credit Cards
- Payments
- Card Issuing
- Virtual Cards
- Transaction
- Spend Management
- Personal Finance
- GraphQL
- Embedded Finance
- Agents
website: https://klutchcard.com
---

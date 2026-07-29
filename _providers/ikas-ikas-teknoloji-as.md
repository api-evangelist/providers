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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Public GraphQL Admin API for ikas stores — read and write products, variants, orders, transactions, customers, price lists, campaigns, coupons, stock locations, sales channels, storefronts, and webhoo
  name: ikas Admin API
  slug: ikas-admin-api
artifact_total: 6
asyncapis:
- description: ''
  name: Ikas Ikas Teknoloji As Webhooks
  slug: ikas-ikas-teknoloji-as-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://ikas.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ikas.dev
- group: docs
  title: ''
  type: Documentation
  url: https://ikas.dev/docs/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://ikas.dev/docs/api/getting-started/authentication
- group: start
  title: ''
  type: Sandbox
  url: https://ikas.dev/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://ikas.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ikascom
- group: auth
  title: ''
  type: Authentication
  url: authentication/ikas-ikas-teknoloji-as-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ikas-ikas-teknoloji-as-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ikas-ikas-teknoloji-as-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ikas-ikas-teknoloji-as-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://builders.ikas.com/docs/app-development
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ikas-ikas-teknoloji-as-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ikas-ikas-teknoloji-as-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/ikas-ikas-teknoloji-as-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ikas-ikas-teknoloji-as-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ikas-ikas-teknoloji-as-cli.yml
- group: design
  title: ''
  type: Components
  url: components/ikas-ikas-teknoloji-as-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ikas-ikas-teknoloji-as-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ikas-ikas-teknoloji-as-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ikas-ikas-teknoloji-as-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ikas-ikas-teknoloji-as-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ikas-ikas-teknoloji-as-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ikas-ikas-teknoloji-as-llms.txt
created: '2026-07-17'
description: ikas (IKAS Teknoloji AS) is an all-in-one e-commerce platform, headquartered in Turkey and backed by 500 Global, that lets merchants build online stores, manage products, inventory, orders, customers, and campaigns, and sell across multiple sales channels. For developers and partners, ikas exposes a public GraphQL Admin API at api.myikas.com that covers products, variants, orders, transactions, customers, price lists, campaigns, coupons, stock locations, sales channels, storefronts, and webhooks. Apps authenticate with OAuth 2.0 (client_credentials for private/store apps and authorization_code for public admin apps) using scoped permissions such as read_products/write_products and read_orders/write_orders. ikas also ships a TypeScript SDK, an ikas CLI, an App Bridge for embedded dashboard apps, a theme development kit, and an official MCP server for its code components.
image: https://ikas.dev/img/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: ikas-ikas-teknoloji-as-mcp.yml
  slug: ikas-ikas-teknoloji-as-mcpyml
modified: '2026-07-19'
name: Ikas, IKAS Teknoloji AS
nav: Providers
network: true
overview: 'Ikas, IKAS Teknoloji AS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Retail, Storefront, and Orders.


  The Ikas, IKAS Teknoloji AS catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ikas, IKAS Teknoloji AS''s developer surface includes documentation, getting-started guide, sandbox, pricing, authentication, CLI, and 19 more developer resources.'
random_paper: 10
scopes:
- name: Ikas Ikas Teknoloji As Scopes
  scope_count: 10
  slug: ikas-ikas-teknoloji-as-scopes
  summary_line: 10 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 40.6
  delta: 6.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 34.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ikas-ikas-teknoloji-as/refs/heads/main/screenshots/ikas-ikas-teknoloji-as-2026-07-25T222057.png
security:
- kind: authentication
  name: Ikas Ikas Teknoloji As Authentication
  slug: ikas-ikas-teknoloji-as-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ikas Ikas Teknoloji As Domain Security
  slug: ikas-ikas-teknoloji-as-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ikas-ikas-teknoloji-as
tags:
- Company
- E-commerce
- Retail
- Storefront
- Orders
- Products
- Inventory
- GraphQL
- Webhooks
- OAuth
- SDK
- MCP
website: https://ikas.com
---

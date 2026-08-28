---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.2
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: The Medusa Store API is the customer-facing REST surface of a Medusa application. It exposes products, variants, categories, collections, regions, carts, checkout, payment collections, shipping option
  name: Medusa Store API
  slug: medusa-store-api
- description: The Medusa Admin API is the merchant/operations REST surface of a Medusa application. It covers products, inventory, price lists, promotions and campaigns, orders, draft orders, order edits, claims, e
  name: Medusa Admin API
  slug: medusa-admin-api
- description: Medusa's GraphQL surface over the store data core. The schema in this repo was derived from the OAS output schemas published in the medusajs/medusa repository; Medusa does not publish a hosted, intros
  name: Medusa GraphQL API
  slug: medusa-graphql-api
- description: Medusa hosts a Streamable HTTP Model Context Protocol server at https://docs.medusajs.com/mcp. It exposes the Medusa documentation to coding agents plus curated implementation-guide tools for data mig
  name: Medusa MCP Remote Server
  slug: medusa-mcp-server
artifact_total: 13
asyncapis:
- description: ''
  name: Medusa Events
  slug: medusa-events
common:
- group: company
  title: ''
  type: Website
  url: https://medusajs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.medusajs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.medusajs.com/learn
- group: docs
  title: ''
  type: APIReference
  url: https://docs.medusajs.com/api/store
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.medusajs.com/learn/installation
- group: operate
  title: ''
  type: Support
  url: https://medusajs.com/contact/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/medusajs
- group: company
  title: ''
  type: Blog
  url: https://medusajs.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/medusajs
- group: commercial
  title: ''
  type: Pricing
  url: https://medusajs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.medusajs.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medusajs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medusajs.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.medusajs.com
- group: auth
  title: ''
  type: Security
  url: https://github.com/medusajs/medusa/security/policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medusa-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/medusa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/medusa-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medusa-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medusa-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/medusa-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medusa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medusa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medusa-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/medusa-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medusa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/medusa-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medusa-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/medusa-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/medusa-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medusa-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/medusa-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/medusa-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/medusa-cli.yml
- group: design
  title: ''
  type: Components
  url: components/medusa-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medusa-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/medusa-events.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/medusa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medusa-rate-limits.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/medusa-graphql.md
created: '2026-07-22'
description: 'Medusa is an open-source, MIT-licensed digital commerce platform built around a modular architecture: a suite of Commerce Modules (cart, products, orders, pricing, promotions, tax, inventory, fulfillment, payment), a Framework for building custom API routes, data models, workflows and integrations, and a customizable Medusa Admin dashboard. Medusa ships two first-party REST APIs — a Store API for storefronts and an Admin API for merchant operations — both documented with published OpenAPI 3.0 specifications generated from the codebase. Medusa is self-hosted by default; MedusaJS, Inc. also operates Medusa Cloud, a managed PaaS, and a remote MCP server plus published Claude Code agent skills for agentic development.'
graphqls:
- description: Medusa is an open-source headless commerce platform with a modular architecture that enables developers to build custom commerce applications. The GraphQL API exposes the full store surface for buildi
  name: Medusa GraphQL API
  slug: medusa-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medusa.png
layout: provider
mcp_servers:
- description: 'Medusa operates one official MCP server. It is REMOTE ONLY — a Streamable HTTP endpoint at https://docs.medusajs.com/mcp. There is no npm/stdio package: @medusajs/mcp does not exist on npm (404, check'
  name: Medusa MCP Server
  slug: medusa-mcp-server
modified: '2026-08-26'
name: Medusa
nav: Providers
network: true
overview: 'Medusa publishes 2 APIs on the [APIs.io](https://apis.io/) network: Store API and Admin API. Tagged areas include E-Commerce, Headless Commerce, Open-Source, Commerce, and Storefront.


  The Medusa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Medusa''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Medusa Plans Pricing
  plan_count: 4
  slug: medusa-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Medusa Rate Limits
  slug: medusa-rate-limits
scopes:
- name: Medusa Scopes
  scope_count: 0
  slug: medusa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.0
  delta: 51.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 60.4
    developer_ergonomics: 85.7
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 63.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 15.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/medusa/refs/heads/main/screenshots/medusa-2026-08-07T172412.png
security:
- kind: authentication
  name: Medusa Authentication
  slug: medusa-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Medusa Domain Security
  slug: medusa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medusa Vulnerability Disclosure
  slug: medusa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: medusa
tags:
- E-Commerce
- Headless Commerce
- Open-Source
- Commerce
- Storefront
- Order Management
- Node.js
- GraphQL
- Agentic Commerce
- MCP
website: https://medusajs.com/
---

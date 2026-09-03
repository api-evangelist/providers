---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Medusa Js Agentic Access
  operation_count: 18
  slug: medusa-js-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- description: Official TypeScript / JavaScript SDK wrapping the Store and Admin REST APIs - typed clients, auth helpers, and ergonomic resource methods. Distributed via npm as @medusajs/js-sdk with shared @medusajs
  name: Medusa JS SDK (@medusajs/js-sdk)
  slug: js-sdk
- description: Server-side framework primitives for extending Medusa - custom API Routes, Modules with their own data models (DML), Module Links, Workflows for transactional business logic, Subscribers and Scheduled
  name: Medusa Framework (Modules, Workflows, Routes)
  slug: framework
- description: First-party domain modules that compose into a Medusa application - Cart, Payment, Customer, Pricing, Promotion, Product, Order, Inventory, Fulfillment, Stock Location, Region, Sales Channel, Tax, Cur
  name: Medusa Commerce Modules
  slug: commerce-modules
- description: Command-line tooling for scaffolding new Medusa projects, generating modules and migrations, running the server in dev, and managing common project tasks.
  name: Medusa CLI (create-medusa-app)
  slug: cli
- description: Reference Next.js storefront talking to the Medusa Store API - cart, checkout, account, product browse, payments, and search. Used as the canonical starting point for headless storefronts.
  name: Medusa Next.js Storefront Starter
  slug: nextjs-starter
- description: Remote Model Context Protocol server exposing the Medusa documentation to LLM-powered coding assistants - lets agents look up commerce modules, framework concepts, and APIs while writing Medusa code.
  name: Medusa Docs MCP Server
  slug: mcp-server
- description: Monorepo with the Medusa server, Admin, Commerce Modules, Framework, and packages. MIT-licensed reference for self-hosting and for building modules and plugins.
  name: Medusa Core Repository
  slug: core-repo
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Auth API from Medusa — 2 operation(s) for auth.
  name: Medusa Auth API
  slug: medusa-js-auth-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Carts API from Medusa — 3 operation(s) for carts.
  name: Medusa Carts API
  slug: medusa-js-carts-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Categories API from Medusa — 1 operation(s) for categories.
  name: Medusa Categories API
  slug: medusa-js-categories-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Collections API from Medusa — 1 operation(s) for collections.
  name: Medusa Collections API
  slug: medusa-js-collections-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Customers API from Medusa — 2 operation(s) for customers.
  name: Medusa Customers API
  slug: medusa-js-customers-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Orders API from Medusa — 2 operation(s) for orders.
  name: Medusa Orders API
  slug: medusa-js-orders-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Payments API from Medusa — 1 operation(s) for payments.
  name: Medusa Payments API
  slug: medusa-js-payments-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Products API from Medusa — 2 operation(s) for products.
  name: Medusa Products API
  slug: medusa-js-products-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Regions API from Medusa — 2 operation(s) for regions.
  name: Medusa Regions API
  slug: medusa-js-regions-api
- baseURL: https://docs.medusajs.com/api/store
  baseurl_source: declared
  description: The Shipping API from Medusa — 1 operation(s) for shipping.
  name: Medusa Shipping API
  slug: medusa-js-shipping-api
artifact_total: 69
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Medusa Store Auth API
  slug: open-medusa-js-auth-api
- collection_type: open
  name: Medusa Store Auth Carts API
  slug: open-medusa-js-carts-api
- collection_type: open
  name: Medusa Store Auth Categories API
  slug: open-medusa-js-categories-api
- collection_type: open
  name: Medusa Store Auth Collections API
  slug: open-medusa-js-collections-api
- collection_type: open
  name: Medusa Store Auth Customers API
  slug: open-medusa-js-customers-api
- collection_type: open
  name: Medusa Store Auth Orders API
  slug: open-medusa-js-orders-api
- collection_type: open
  name: Medusa Store Auth Payments API
  slug: open-medusa-js-payments-api
- collection_type: open
  name: Medusa Store Auth Products API
  slug: open-medusa-js-products-api
- collection_type: open
  name: Medusa Store Auth Regions API
  slug: open-medusa-js-regions-api
- collection_type: open
  name: Medusa Store Auth Shipping API
  slug: open-medusa-js-shipping-api
- collection_type: open
  name: Medusa Store API
  slug: open-medusa-js
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/medusajs/medusa/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/medusajs/medusa/blob/develop/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/medusajs/medusa/blob/develop/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/medusa-js-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medusa-js-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medusa-js-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://medusajs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.medusajs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.medusajs.com/api/store
- group: docs
  title: ''
  type: APIReference
  url: https://docs.medusajs.com/api/admin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/medusajs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/medusajs/medusa
- group: commercial
  title: ''
  type: Pricing
  url: https://medusajs.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://medusajs.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/medusajs
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.medusajs.com/llms.txt
- group: commercial
  title: ''
  type: License
  url: https://github.com/medusajs/medusa/blob/develop/LICENSE
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medusajs/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/medusajs/medusa/releases
created: '2026-05-23'
description: Medusa is an open-source headless commerce platform written in Node.js and TypeScript, distributed under the MIT license. The Medusa server exposes two REST APIs - a public Store API consumed by storefronts and end-customer clients, and a privileged Admin API consumed by the Medusa Admin dashboard and back-office tooling - both documented with OpenAPI. Around the server the project ships a modular Framework (API Routes, Modules, Module Links, Workflows, Subscribers, Scheduled Jobs, Admin Extensions), the Commerce Modules (cart, payment, customer, pricing, promotion, product, order, inventory, fulfillment, stock location, region, sales channel, tax, currency, API keys, user, auth), the @medusajs/js-sdk TypeScript client, the Medusa CLI (create-medusa-app), the Next.js storefront starter, a remote MCP server that exposes the docs to LLM coding assistants, and Medusa Cloud as an optional managed hosting offering with predictable per-environment pricing and no GMV fees.
features:
- description: First-party domain modules (cart, order, product, inventory, pricing, promotion, payment, fulfillment, region, sales channel, tax, currency, auth) that can be swapped or extended.
  name: Modular Commerce Modules
- description: Transactional, durable business-logic workflows with compensation steps for orchestrating multi-step commerce operations.
  name: Workflows Engine
- description: Customizable React-based Medusa Admin UI with first-class admin extensions for adding screens, widgets, and routes.
  name: Admin Dashboard
- description: Two distinct REST surfaces - public Store API and privileged Admin API - both described with OpenAPI.
  name: Store and Admin REST APIs
- description: Typed JS SDK (@medusajs/js-sdk) for both Store and Admin APIs with shared types from @medusajs/types.
  name: JS / TypeScript SDK
- description: Reference Next.js storefront wired to the Store API as a launchpad for custom storefronts.
  name: Next.js Starter
- description: create-medusa-app and the Medusa CLI for scaffolding projects, running dev servers, and managing migrations.
  name: CLI Tooling
- description: Remote MCP server exposing the docs and a Development Agent that lets LLM coding assistants build on Medusa.
  name: Agentic Development (MCP)
- description: Optional managed hosting with GitHub-based deploys, autoscaling, and no GMV-based fees.
  name: Medusa Cloud
- description: Permissive open-source license with no vendor lock-in and the ability to self-host the full stack.
  name: MIT License
finops:
- name: Medusa Js Finops
  service_category: API
  slug: medusa-js-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medusa-js.png
integrations:
- description: Official Next.js storefront starter (nextjs-starter-medusa) wired to the Store API.
  name: Next.js
- description: Payment provider integration for card payments and saved methods via the Payment module.
  name: Stripe
- description: PayPal payment provider integration via the Payment module.
  name: PayPal
- description: Search integrations for product catalog indexing and storefront search.
  name: Algolia / MeiliSearch / Typesense
- description: Notification providers for transactional email through the Notification module.
  name: SendGrid / Resend
- description: File storage providers for product images and assets.
  name: AWS S3 / MinIO
- description: Primary supported database engine for the Medusa server.
  name: PostgreSQL
- description: Used for caching, event bus, and queues in production deployments.
  name: Redis
- description: Remote MCP server exposes the Medusa docs to Claude, Cursor, and other MCP-aware coding assistants.
  name: Model Context Protocol (MCP)
- description: GitHub-based deployments and source-of-truth for Medusa Cloud environments.
  name: GitHub
layout: provider
modified: '2026-05-25'
name: Medusa
nav: Providers
network: true
overview: 'Medusa publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Carts API, Categories API, and 7 more. Tagged areas include Commerce, Headless, E-Commerce, Open-Source, and Node.js.


  Medusa''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, release notes, and 12 more developer resources.'
plans:
- name: Medusa Js Plans Pricing
  plan_count: 1
  slug: medusa-js-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Medusa Js Rate Limits
  slug: medusa-js-rate-limits
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 44.2
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 85.0
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medusa-js/refs/heads/main/screenshots/medusa-js-2026-06-20T185127.png
security:
- kind: authentication
  name: Medusa Js Authentication
  slug: medusa-js-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Medusa Js Domain Security
  slug: medusa-js-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: medusa-js
solutions:
- description: Free, MIT-licensed open-source server, Admin, framework, and commerce modules deployable to any Node.js host.
  name: Medusa Core (Self-Hosted)
- description: Entry managed tier with GitHub deploys, dev agent, and a shared server starting at $29/mo.
  name: Medusa Cloud - Develop
- description: Production-ready managed tier with autoscaling, custom domains, automatic backups, and zero-downtime deploys at $99/mo.
  name: Medusa Cloud - Launch
- description: Growth tier with background workers, priority support, and higher edge request quotas at $299/mo.
  name: Medusa Cloud - Scale
- description: SLA-backed enterprise tier with core-team access, custom agentic workflows, and implementation support.
  name: Medusa Cloud - Enterprise
- description: Curated partner network of agencies and consultancies delivering Medusa implementations.
  name: Medusa Experts
tags:
- Commerce
- Headless
- E-Commerce
- Open-Source
- Node.js
- TypeScript
- Framework
- Modules
- Workflows
- MCP
use_cases:
- description: Power Next.js / React Native / native storefronts for direct-to- consumer brands using the Store API and JS SDK.
  name: Headless DTC Storefronts
- description: Build company-account, quoting, and approval flows on top of the Commerce Modules and Workflows engine.
  name: B2B Commerce
- description: Use sales channels, regions, and stock locations to model multi- vendor and multi-store marketplaces.
  name: Marketplaces
- description: Replace Shopify, BigCommerce, or Magento with a fully owned, self-hostable commerce backend.
  name: Composable Commerce Replatforming
- description: Drive merchandising, support, and operations from LLM agents using the MCP server and admin tooling.
  name: AI-Native Commerce
- description: Implement bespoke checkout, payment, and pricing flows by composing modules and workflows.
  name: Custom Checkout Experiences
- description: Model stock locations, fulfillment, and regions for last-mile and on-demand delivery models.
  name: Quick Commerce & Logistics
- description: Stand up an internal commerce backbone for catalog, orders, and fulfillment shared across brands or business units.
  name: Internal Commerce Platforms
website: https://medusajs.com/
---

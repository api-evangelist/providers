---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Wix Agentic Access
  operation_count: 19
  slug: wix-agentic-access
  summary_line: 19 operations · 14 acting
api_count: 1
apis:
- description: The Wix REST API provides full programmatic access to all Wix platform capabilities via standard HTTP REST endpoints. The API covers eCommerce (stores, orders, catalog, payments, gift cards), bookings
  name: Wix REST API
  slug: rest-api
- description: 'The Wix JavaScript SDK provides modular npm packages for accessing Wix business solutions and site data from JavaScript code. It supports Wix Sites, Wix Apps, and Wix Headless projects. Modules cover '
  name: Wix JavaScript SDK
  slug: javascript-sdk
- description: Wix Headless enables developers to use Wix business solutions as a backend while building custom frontends with any framework. It provides managed commerce, CRM, and content APIs accessible from any t
  name: Wix Headless
  slug: headless
- description: The Wix webhook surface delivers signed JWT events to subscriber URLs registered in the Wix Dev Center. Events cover Stores (products, inventory, collections, variants), eCommerce (cart, checkout, aba
  name: Wix Webhooks
  slug: webhooks
- description: The Cart API from Wix — 3 operation(s) for cart.
  name: Wix Cart API
  slug: wix-cart-api
- description: The Checkout API from Wix — 2 operation(s) for checkout.
  name: Wix Checkout API
  slug: wix-checkout-api
- description: The OAuth API from Wix — 3 operation(s) for oauth.
  name: Wix OAuth API
  slug: wix-oauth-api
- description: The Orders API from Wix — 3 operation(s) for orders.
  name: Wix Orders API
  slug: wix-orders-api
- description: The Products API from Wix — 4 operation(s) for products.
  name: Wix Products API
  slug: wix-products-api
artifact_total: 49
asyncapis:
- description: AsyncAPI specification for the documented Wix webhook surface. Wix delivers webhook events as signed JSON Web Tokens (JWTs) POSTed to subscriber URLs registered in the Wix Dev Center. The JWT body dec
  name: Wix Webhooks
  slug: wix-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wix REST Cart API
  slug: open-wix-cart-api
- collection_type: open
  name: Wix REST Cart Checkout API
  slug: open-wix-checkout-api
- collection_type: open
  name: Wix REST Cart OAuth API
  slug: open-wix-oauth-api
- collection_type: open
  name: Wix REST Cart Orders API
  slug: open-wix-orders-api
- collection_type: open
  name: Wix REST Cart Products API
  slug: open-wix-products-api
- collection_type: open
  name: Wix REST API
  slug: open-wix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wix-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wix-com
- group: company
  title: ''
  type: Website
  url: https://www.wix.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.wix.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.wix.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.wix.com/docs/rest/articles/getting-started/introduction
- group: start
  title: ''
  type: Signup
  url: https://users.wix.com/signin
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wix
- group: build
  title: Wix MCP Server
  type: Tools
  url: https://github.com/wix/wix-mcp
- group: company
  title: ''
  type: Blog
  url: https://dev.wix.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.wix.com
- group: operate
  title: ''
  type: Forums
  url: https://www.wix.com/forum/corvid-tips-questions-and-answers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wix
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/wix/wix-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/wix/skills
created: '2025-02-08'
description: Wix is a cloud-based web development platform that allows users to create professional websites and online businesses. The Wix developer platform provides a comprehensive REST API, JavaScript SDK, and CLI for building custom apps, headless storefronts, and site extensions across eCommerce, CRM, bookings, blog, events, and more. Developers can customize Wix sites, build marketplace apps, and integrate Wix capabilities into any frontend.
features:
- description: Full store management including products, orders, payments, gift cards, and shipping via REST and SDK.
  name: eCommerce APIs
- description: Manage site contacts, members, forms, automations, and loyalty programs.
  name: CRM APIs
- description: Service booking, staff scheduling, resources, and pricing plan management.
  name: Bookings APIs
- description: Use Wix as a backend commerce engine with a custom frontend on any framework.
  name: Headless Commerce
- description: Build and publish apps to the Wix App Market using OAuth 2.0 and webhooks.
  name: App Marketplace
- description: Model Context Protocol server that bridges AI clients to Wix APIs and documentation.
  name: Wix MCP Server
- description: Modular npm packages for accessing Wix capabilities from JavaScript applications.
  name: JavaScript SDK
- description: Full-stack JavaScript development platform for adding custom functionality to Wix sites.
  name: Velo by Wix
finops:
- name: Wix Finops
  service_category: API
  slug: wix-finops
graphqls:
- description: The Wix GraphQL API exposes the full Wix platform as a single unified GraphQL schema, providing an alternative to the REST API for querying and mutating Wix site data. It is well-suited for applicatio
  name: Wix GraphQL API
  slug: wix-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wix.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Wix
nav: Providers
network: true
overview: 'Wix publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Cart API, Checkout API, and 3 more. Tagged areas include CMS, E-Commerce, Headless, and Website Builder.


  The Wix catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Wix''s developer surface includes authentication, documentation, getting-started guide, signup flow, GitHub presence, tooling, engineering blog, and 12 more developer resources.'
plans:
- name: Wix Plans Pricing
  plan_count: 3
  slug: wix-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Wix Rate Limits
  slug: wix-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Wix API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: wix-asyncapi-spectral-rules
scopes:
- name: Wix Scopes
  scope_count: 0
  slug: wix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 74.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 56.7
    developer_ergonomics: 38.1
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wix/refs/heads/main/screenshots/wix-2026-06-20T201529.png
security:
- kind: authentication
  name: Wix Authentication
  slug: wix-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Wix Domain Security
  slug: wix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wix Vulnerability Disclosure
  slug: wix-vulnerability-disclosure
  summary_line: disclosure policy published
skill_count: 8
skills:
- name: wix-app
  slug: wix-app-2
- name: wix-app
  slug: wix-app
- name: wix-design-system
  slug: wix-design-system-2
- name: wix-design-system
  slug: wix-design-system
- name: wix-headless
  slug: wix-headless-2
- name: wix-headless
  slug: wix-headless
- name: wix-manage
  slug: wix-manage-2
- name: wix-manage
  slug: wix-manage
slug: wix
tags:
- CMS
- E-Commerce
- Headless
- Website Builder
use_cases:
- description: Build a headless storefront with custom UI while using Wix for catalog, orders, and payments.
  name: Custom eCommerce Storefront
- description: Develop and publish apps to the Wix App Market that install on Wix sites.
  name: App Development
- description: Sync contacts, members, and orders with external CRM systems via REST API.
  name: CRM Integration
- description: Build custom booking experiences for service businesses using Wix Bookings API.
  name: Booking System
- description: Use the Wix MCP Server to manage Wix sites through AI assistants and agents.
  name: AI-Powered Site Management
website: https://www.wix.com
---

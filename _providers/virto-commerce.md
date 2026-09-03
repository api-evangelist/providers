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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 283
  human_in_the_loop: 9
  name: Virto Commerce Agentic Access
  operation_count: 426
  slug: virto-commerce-agentic-access
  summary_line: 426 operations · 283 acting · 9 human-in-the-loop
api_count: 14
apis:
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Easily manage your products, categories, variations, and properties
  name: Virto Commerce Catalog API
  slug: virto-commerce-catalog-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Managing customers contacts and organizations
  name: Virto Commerce Companies and Contacts API
  slug: virto-commerce-companies-and-contacts-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Simplify inventory management functionality
  name: Virto Commerce Inventory API
  slug: virto-commerce-inventory-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Marketing system with dynamic contents and promotions management
  name: Virto Commerce Marketing API
  slug: virto-commerce-marketing-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Document based flexible order management system.
  name: Virto Commerce Order Management API
  slug: virto-commerce-order-management-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Robust pricing management functionality based on price list and dynamic evaluation
  name: Virto Commerce Pricing API
  slug: virto-commerce-pricing-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: 'Quoter enables business users to execute quote requests online. Once initiated, an online conversation takes place with internal users who interact with the business user''s request. The internal user '
  name: Virto Commerce Quotes API
  slug: virto-commerce-quotes-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Shopping cart / checkout functionality
  name: Virto Commerce Shopping Cart API
  slug: virto-commerce-shopping-cart-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Multi store management with individual store settings
  name: Virto Commerce Store API
  slug: virto-commerce-store-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: B2B Innovation Platform
  name: Virto Commerce VirtoCommerce Platform API
  slug: virto-commerce-virtocommerce-platform-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Register HTTP webhooks against the platform domain-event catalog, compose the payload from selected entity properties (including previous values), fire test deliveries, and audit every delivery attemp
  name: Virto Commerce Webhooks API
  slug: virto-commerce-webhooks-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: 'Return management: search returns, read a return by id, create or update a return against an order, and read the quantities still available to return.'
  name: Virto Commerce Returns API
  slug: virto-commerce-returns-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: The module enables you to be notified of new messages or changes via a Message Queue of your choice
  name: Virto Commerce Event Bus module API
  slug: virto-commerce-event-bus-module-api
artifact_total: 35
asyncapis:
- description: ''
  name: Virto Commerce Webhooks
  slug: virto-commerce-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VirtoCommerce.Cart Catalog API
  slug: open-virto-commerce-catalog-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Companies and Contacts API
  slug: open-virto-commerce-companies-and-contacts-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Inventory API
  slug: open-virto-commerce-inventory-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Marketing API
  slug: open-virto-commerce-marketing-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Order Management API
  slug: open-virto-commerce-order-management-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Pricing API
  slug: open-virto-commerce-pricing-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Quotes API
  slug: open-virto-commerce-quotes-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Shopping Cart API
  slug: open-virto-commerce-shopping-cart-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Store API
  slug: open-virto-commerce-store-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog VirtoCommerce Platform API
  slug: open-virto-commerce-virtocommerce-platform-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/virto-commerce-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/VirtoCommerce/vc-module-catalog/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/VirtoCommerce/vc-module-catalog/releases
- group: other
  title: ''
  type: Overlay
  url: overlays/virto-commerce-event-bus-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virto-commerce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virto-commerce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virto-commerce-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/virto-commerce-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://virtocommerce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtocommerce.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VirtoCommerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virto-commerce/
- group: company
  title: ''
  type: Blog
  url: https://virtocommerce.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://virtocommerce.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/VirtoCommerce
- group: commercial
  title: ''
  type: Plans
  url: plans/virto-commerce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virto-commerce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/virto-commerce-finops.yml
- group: docs
  title: ''
  type: SwaggerUI
  url: https://virtostart-demo-admin.govirto.com/docs/index.html
- group: operate
  title: ''
  type: Support
  url: https://help.virtocommerce.com/support/home
- group: operate
  title: ''
  type: Community
  url: https://www.virtocommerce.org/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.virtocommerce.org/c/news-digest/14
- group: build
  title: ''
  type: Packages
  url: packages/virto-commerce-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/virto-commerce-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/virto-commerce-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virto-commerce-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/virto-commerce-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virto-commerce-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/virto-commerce-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/virto-commerce-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virto-commerce-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virto-commerce-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virto-commerce-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virto-commerce-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/virto-commerce-cli.yml
- group: design
  title: ''
  type: Components
  url: components/virto-commerce-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virto-commerce-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/virto-commerce-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/virto-commerce-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/virto-commerce-schema.graphql
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.virtocommerce.org/platform/developer-guide/
- group: docs
  title: ''
  type: APIReference
  url: https://virtostart-demo-admin.govirto.com/docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/VirtoCommerce/start-local
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtocommerce.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtocommerce.com/privacy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Virtocommerce/videos
created: '2026-06-13'
description: Virto Commerce is an open-source, API-first B2B e-commerce platform built on .NET Core. It provides REST and GraphQL APIs for catalog management, pricing, inventory, order management, customer organizations, marketing, payments, shipping, subscriptions, and complex B2B purchasing workflows including quotes, contracts, and approval routing. The modular architecture offers 100+ independently deployable modules covering the full commerce stack for enterprise deployments.
finops:
- name: Virto Commerce Finops
  service_category: ''
  slug: virto-commerce-finops
graphqls:
- description: Virto Commerce exposes a unified GraphQL API (the "Experience API" or xAPI) as the primary interface for headless storefronts. Built on top of the GraphQL.NET library, the xAPI aggregates catalog, car
  name: Virto Commerce GraphQL API
  slug: virto-commerce-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/virto-commerce.png
jsonld:
- class_count: 15
  name: Virto Commerce Context
  property_count: 0
  slug: virto-commerce-context
layout: provider
mcp_servers:
- description: Virto Commerce ships a real, published MCP surface, and it is a LOCAL STDIO one. The supported path is the Commerce Operations Foundation (COF) MCP server run over stdio with Virto's own adapter (@vir
  name: Virto Commerce MCP
  slug: virto-commerce-mcp
modified: '2026-08-13'
name: Virto Commerce
nav: Providers
network: true
overview: 'Virto Commerce publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Companies and Contacts API, Inventory API, and 10 more. Tagged areas include B2B eCommerce, Catalog Management, Order Management, Pricing, and Inventory.


  The Virto Commerce catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Virto Commerce''s developer surface includes authentication, documentation, engineering blog, pricing, support, changelog, CLI, and 40 more developer resources.'
plans:
- name: Virto Commerce Plans Pricing
  plan_count: 3
  slug: virto-commerce-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Virto Commerce Rate Limits
  slug: virto-commerce-rate-limits
scopes:
- name: Virto Commerce Scopes
  scope_count: 84
  slug: virto-commerce-scopes
  summary_line: 84 scopes · password/clientCredentials
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 30
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.9
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 57.9
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/screenshots/virto-commerce-2026-06-20T201036.png
security:
- kind: authentication
  name: Virto Commerce Authentication
  slug: virto-commerce-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Virto Commerce Domain Security
  slug: virto-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virto-commerce
tags:
- B2B eCommerce
- Catalog Management
- Order Management
- Pricing
- Inventory
- Shopping Cart
- Customer Management
- Marketing
- Payments
- Shipping
- Subscription
- Headless Commerce
- Open-Source
- .NET
- Webhook
- Event-Driven
- CloudEvents
- GraphQL
- Returns
- MCP
- B2B Quotes
website: https://virtocommerce.com/
---

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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Rentle Agentic Access
  operation_count: 28
  slug: rentle-agentic-access
  summary_line: 28 operations · 7 acting
api_count: 1
apis:
- description: API Key-related queries
  name: Rentle API Keys API
  slug: rentle-api-keys-api
- description: Category-related queries
  name: Rentle Categories API
  slug: rentle-categories-api
- description: Customer-related queries
  name: Rentle Customers API
  slug: rentle-customers-api
- description: Discount code-related queries
  name: Rentle Discount Codes API
  slug: rentle-discount-codes-api
- description: Inventory-related queries
  name: Rentle Inventory Articles API
  slug: rentle-inventory-articles-api
- description: The Inventory SKUs API from Rentle — 2 operation(s) for inventory skus.
  name: Rentle Inventory SKUs API
  slug: rentle-inventory-skus-api
- description: Merchant-related queries
  name: Rentle Merchant API
  slug: rentle-merchant-api
- description: Order-related queries
  name: Rentle Orders API
  slug: rentle-orders-api
- description: Product-related queries
  name: Rentle Products API
  slug: rentle-products-api
- description: Store-related queries
  name: Rentle Stores API
  slug: rentle-stores-api
- description: 'This section describes API endpoints you can use to configure webhooks. Check the [webhook events section](#tag/WebhooksOverview) for more inforation regarding the webhooks events that Twice delivers '
  name: Rentle Webhooks API
  slug: rentle-webhooks-api
- description: The Order API from Rentle — 0 operation(s) for order.
  name: Rentle Order API
  slug: rentle-order-api
- description: The Product API from Rentle — 0 operation(s) for product.
  name: Rentle Product API
  slug: rentle-product-api
artifact_total: 30
asyncapis:
- description: ''
  name: Rentle Webhooks
  slug: rentle-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Twice Admin API Keys API
  slug: open-rentle-api-keys-api
- collection_type: open
  name: Twice Admin API Keys Categories API
  slug: open-rentle-categories-api
- collection_type: open
  name: Twice Admin API Keys Customers API
  slug: open-rentle-customers-api
- collection_type: open
  name: Twice Admin API Keys Discount Codes API
  slug: open-rentle-discount-codes-api
- collection_type: open
  name: Twice Admin API Keys Inventory Articles API
  slug: open-rentle-inventory-articles-api
- collection_type: open
  name: Twice Admin API Keys Inventory SKUs API
  slug: open-rentle-inventory-skus-api
- collection_type: open
  name: Twice Admin API Keys Merchant API
  slug: open-rentle-merchant-api
- collection_type: open
  name: Twice Admin API Keys Orders API
  slug: open-rentle-orders-api
- collection_type: open
  name: Twice Admin API Keys Products API
  slug: open-rentle-products-api
- collection_type: open
  name: Twice Admin API Keys Stores API
  slug: open-rentle-stores-api
- collection_type: open
  name: Twice Admin API Keys Webhooks API
  slug: open-rentle-webhooks-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/rentle-create-order.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rentle-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rentle-admin-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rentle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.twicecommerce.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.twicecommerce.com/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.twicecommerce.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://api.rentle.io/admin/
- group: operate
  title: ''
  type: Support
  url: https://support.twicecommerce.com
- group: company
  title: ''
  type: Blog
  url: https://www.twicecommerce.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rentle
- group: commercial
  title: ''
  type: Pricing
  url: https://www.twicecommerce.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admin.twicecommerce.com/signup
- group: start
  title: ''
  type: Login
  url: https://admin.twicecommerce.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firebasestorage.googleapis.com/v0/b/rentle-prod.appspot.com/o/rentle-tos-pricing%2Ftos%2FTwice%20Commerce%20Terms%20and%20Conditions%20v.6.4.pdf?alt=media&token=eb7ee536-cb6c-4476-84fd-277e45e4a304
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.twicecommerce.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.twicecommerce.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rentle-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rentle-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/rentle-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rentle-llms.txt
created: '2026-07-17'
description: Rentle, now operating as Twice Commerce, is a Helsinki-founded (2018) circular-commerce platform that lets merchants run rentals, resale, and subscriptions from one system. Its Twice Admin API (OpenAPI 3.0.0, date-based version 2023-02-01) exposes categories, customers, inventory articles, SKUs, products, orders, stores, merchant details, discount codes, API keys, and webhooks over a REST interface authenticated with HTTP Basic API keys. Outbound webhooks cover nine order and product lifecycle events. This profile was enriched by the API Evangelist pipeline from Rentle/Twice Commerce public developer surfaces.
image: https://www.twicecommerce.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Rentle MCP Server
  slug: rentle-mcp-server
modified: '2026-07-20'
name: Rentle
nav: Providers
network: true
overview: 'Rentle publishes 13 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Categories API, Customers API, and 10 more. Tagged areas include Company, Rentals, Commerce, E-Commerce, and Circular Economy.


  The Rentle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rentle''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 15 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 54.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rentle/refs/heads/main/screenshots/rentle-2026-08-17T081515.png
security:
- kind: authentication
  name: Rentle Authentication
  slug: rentle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rentle Domain Security
  slug: rentle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rentle
tags:
- Company
- Rentals
- Commerce
- E-Commerce
- Circular Economy
- Resale
- Subscription
- Bookings
- Webhook
- Software-as-a-Service
website: https://www.twicecommerce.com/
---

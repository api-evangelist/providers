---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Squarespace Agentic Access
  operation_count: 30
  slug: squarespace-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 2
apis:
- description: The Squarespace Orders API provides access to order history for a Squarespace merchant site, supporting both one-time purchases and subscription orders. Developers can retrieve, create, and manage ord
  name: Squarespace Orders API
  slug: squarespace-orders-api
- description: The Squarespace Products API allows developers to manage the product catalog of a Squarespace merchant site. It supports physical products, service products, gift cards, and digital downloads, along w
  name: Squarespace Products API
  slug: squarespace-products-api
- description: The Squarespace Inventory API enables developers to retrieve and update inventory quantities for product variants on a Squarespace merchant site. It supports bulk inventory queries and individual vari
  name: Squarespace Inventory API
  slug: squarespace-inventory-api
- description: The Squarespace Profiles API allows reading customer profiles, mailing list subscribers, and donors for a Squarespace site. It supports filtering by profile type and retrieving individual profile deta
  name: Squarespace Profiles API
  slug: squarespace-profiles-api
- description: The Squarespace Transactions API provides access to financial transaction records for a Squarespace merchant site. Developers can retrieve transaction history, including payment amounts, fees, and ass
  name: Squarespace Transactions API
  slug: squarespace-transactions-api
- description: The Squarespace Webhook Subscriptions API allows developers to manage webhook endpoint subscriptions for a merchant site. It supports creating, listing, updating, and deleting subscriptions that trigg
  name: Squarespace Webhook Subscriptions API
  slug: squarespace-webhook-subscriptions-api
- description: Basic site information and metadata
  name: Squarespace Site API
  slug: squarespace-site-api
- description: Squarespace operates a first-party remote MCP server at https://mcp.squarespace.com/mcp. It answers an unauthenticated JSON-RPC tools/list with HTTP 200 and exposes two tools with full JSON Schema inp
  name: Squarespace MCP Server
  slug: squarespace-mcp
- description: Query analytics for a website
  name: Squarespace Analytics API
  slug: squarespace-analytics-api
- description: 'Manage customer contacts and address book entries for a website: create, read, update, delete, and query contacts; maintain addresses for shipping and fulfillment.'
  name: Squarespace Contacts API
  slug: squarespace-contacts-api
- description: Manage discounts for a website.
  name: Squarespace Discounts API
  slug: squarespace-discounts-api
- description: The WebhookSubscriptions API from Squarespace — 4 operation(s) for webhooksubscriptions.
  name: Squarespace Webhook Subscriptions API
  slug: squarespace-webhooksubscriptions-api
- description: The Websites API from Squarespace — 3 operation(s) for websites.
  name: Squarespace Websites API
  slug: squarespace-websites-api
artifact_total: 44
asyncapis:
- description: The Squarespace webhook system delivers real-time event notifications to registered endpoint URLs when commerce activity occurs on a merchant site. Supported events include order creation, order updat
  name: Squarespace Webhook Events
  slug: squarespace-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Squarespace Commerce API
  slug: open-squarespace-commerce-api
- collection_type: open
  name: Squarespace Commerce Inventory API
  slug: open-squarespace-inventory-api
- collection_type: open
  name: Squarespace Commerce Inventory Orders API
  slug: open-squarespace-orders-api
- collection_type: open
  name: Squarespace Commerce Inventory Products API
  slug: open-squarespace-products-api
- collection_type: open
  name: Squarespace Commerce Inventory Profiles API
  slug: open-squarespace-profiles-api
- collection_type: open
  name: Squarespace Commerce Inventory Site API
  slug: open-squarespace-site-api
- collection_type: open
  name: Squarespace Commerce Inventory Transactions API
  slug: open-squarespace-transactions-api
- collection_type: open
  name: Squarespace Commerce Inventory Webhook Subscriptions API
  slug: open-squarespace-webhook-subscriptions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/squarespace-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/squarespace-commerce-api-v2-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/squarespace-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/squarespace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/squarespace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/squarespace-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/squarespace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/squarespace
- group: company
  title: ''
  type: Website
  url: https://www.squarespace.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.squarespace.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.squarespace.com/commerce-apis/overview
- group: auth
  title: ''
  type: APIKeys
  url: https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.squarespace.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.squarespace.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.squarespace.com
- group: company
  title: ''
  type: Blog
  url: https://www.squarespace.com/blog
- group: auth
  title: ''
  type: Security
  url: security/squarespace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/squarespace-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/squarespace-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/squarespace-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/squarespace-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/squarespace-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/squarespace-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/squarespace-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/squarespace-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/squarespace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/squarespace-problem-types.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/squarespace-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/squarespace-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/squarespace-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/squarespace-lifecycle.yml
- group: design
  title: ''
  type: Versioning
  url: https://developers.squarespace.com/commerce-apis/versioning
- group: design
  title: ''
  type: DataModel
  url: data-model/squarespace-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/squarespace-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/squarespace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/squarespace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/squarespace-finops.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/squarespace-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/squarespace-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.squarespace.com/commerce-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.squarespace.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.squarespace.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.squarespace.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://login.squarespace.com
- group: auth
  title: ''
  type: OAuth
  url: https://developers.squarespace.com/oauth
- group: operate
  title: ''
  type: FAQ
  url: https://developers.squarespace.com/commerce-apis/faq
- group: other
  title: ''
  type: Glossary
  url: https://developers.squarespace.com/commerce-apis/glossary
created: '2026-05-02'
description: Squarespace is an all-in-one website building and e-commerce platform that enables individuals and businesses to create, manage, and scale their online presence. Squarespace provides a suite of Commerce APIs for developers to build integrations managing products, orders, inventory, customer profiles, transactions, and webhook notifications. All APIs use HTTPS REST conventions with API key or OAuth authentication.
examples:
- key_count: 4
  name: Squarespace List Orders Example
  slug: squarespace-list-orders-example
- key_count: 4
  name: Squarespace List Products Example
  slug: squarespace-list-products-example
finops:
- name: Squarespace Finops
  service_category: E-Commerce
  slug: squarespace-finops
image: https://static1.squarespace.com/static/ta/5134cbefe4b0c6fb04df8065/10007/assets/logomark.svg
json_schemas:
- name: Squarespace Order
  property_count: 17
  slug: squarespace-order
- name: Squarespace Product
  property_count: 13
  slug: squarespace-product
- name: Squarespace Webhook Notification
  property_count: 6
  slug: squarespace-webhook-notification
json_structures:
- name: Squarespace Order Structure
  property_count: 0
  slug: squarespace-order-structure
- name: Squarespace Product Structure
  property_count: 0
  slug: squarespace-product-structure
jsonld:
- class_count: 0
  name: Squarespace Context
  property_count: 12
  slug: squarespace-context
layout: provider
mcp_servers:
- description: Squarespace operates a first-party REMOTE MCP server at https://mcp.squarespace.com/mcp. It answers an unauthenticated JSON-RPC tools/list with HTTP 200 and returns two real tools with full JSON Schem
  name: Squarespace MCP Server
  slug: squarespace-mcp-server
modified: '2026-08-13'
name: Squarespace
nav: Providers
network: true
overview: 'Squarespace publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Products API, Inventory API, and 9 more. Tagged areas include Commerce, E-Commerce, Marketing, Payments, and Retail.


  The Squarespace catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Squarespace''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, support, and 41 more developer resources.'
plans:
- name: Squarespace Plans Pricing
  plan_count: 5
  slug: squarespace-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Squarespace Rate Limits
  slug: squarespace-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Squarespace API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: squarespace-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Squarespace API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: squarespace-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Squarespace API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 7
  slug: squarespace-rules
scopes:
- name: Squarespace Scopes
  scope_count: 0
  slug: squarespace-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 74.9
  coverage:
    artifact_dirs: 31
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 33.3
    contract_quality: 73.1
    developer_ergonomics: 58.9
    discoverability: 59.3
    governance: 33.3
    operational_transparency: 81.6
  previous_composite: 74.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/squarespace/refs/heads/main/screenshots/squarespace-2026-06-20T194430.png
security:
- kind: authentication
  name: Squarespace Authentication
  slug: squarespace-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Squarespace Domain Security
  slug: squarespace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Squarespace Vulnerability Disclosure
  slug: squarespace-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Squarespace Trust Center
  slug: squarespace-trust-center
  summary_line: named, note
slug: squarespace
tags:
- Commerce
- E-Commerce
- Marketing
- Payments
- Retail
- Website Builder
- Webhook
website: https://www.squarespace.com
---

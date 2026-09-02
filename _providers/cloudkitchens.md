---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Cloudkitchens Agentic Access
  operation_count: 80
  slug: cloudkitchens-agentic-access
  summary_line: 80 operations · 59 acting
api_count: 1
apis:
- description: Endpoints to manage store onboarding and status
  name: CloudKitchens Account Pairing Endpoints API
  slug: cloudkitchens-account-pairing-endpoints-api
- description: Webhooks to manage store onboarding and status
  name: CloudKitchens Account Pairing Webhooks API
  slug: cloudkitchens-account-pairing-webhooks-api
- description: Endpoints to handle token management.
  name: CloudKitchens Auth Endpoints API
  slug: cloudkitchens-auth-endpoints-api
- description: Endpoints for callback management.
  name: CloudKitchens Callback Endpoints API
  slug: cloudkitchens-callback-endpoints-api
- description: Endpoints to manage delivery.
  name: CloudKitchens Delivery Endpoints API
  slug: cloudkitchens-delivery-endpoints-api
- description: Webhooks from the delivery domain.
  name: CloudKitchens Delivery Webhooks API
  slug: cloudkitchens-delivery-webhooks-api
- description: Endpoints to get orders directly.
  name: CloudKitchens Direct Orders Endpoints API
  slug: cloudkitchens-direct-orders-endpoints-api
- description: Endpoints to handle financial data.
  name: CloudKitchens Finance Endpoints API
  slug: cloudkitchens-finance-endpoints-api
- description: Endpoints to interact with product inventory.
  name: CloudKitchens Inventory Endpoints API
  slug: cloudkitchens-inventory-endpoints-api
- description: Endpoints to manage loyalty.
  name: CloudKitchens Manager Loyalty Endpoints API
  slug: cloudkitchens-manager-loyalty-endpoints-api
- description: Endpoints for applications managing menus related data and operations.
  name: CloudKitchens Manager Menu Endpoints API
  slug: cloudkitchens-manager-menu-endpoints-api
- description: Endpoints for applications that act on the merchant/store side of an order rather than as the ordering marketplace — typically Point-of-Sale (POS) systems, Business Intelligence (BI) tools, and report
  name: CloudKitchens Manager Order Endpoints API
  slug: cloudkitchens-manager-order-endpoints-api
- description: Webhooks delivered to merchant-side applications (POS, BI, and reporting integrations) so they can react to changes in an order as it progresses through its lifecycle.
  name: CloudKitchens Manager Orders Webhooks API
  slug: cloudkitchens-manager-orders-webhooks-api
- description: Endpoints for applications managing storefront related data and operations.
  name: CloudKitchens Manager Storefront Endpoints API
  slug: cloudkitchens-manager-storefront-endpoints-api
- description: The marketintel_endpoints API from CloudKitchens — 1 operation(s) for marketintel_endpoints.
  name: CloudKitchens Marketintel Endpoints API
  slug: cloudkitchens-marketintel-endpoints-api
- description: Endpoints to manage menus.
  name: CloudKitchens Menus Endpoints API
  slug: cloudkitchens-menus-endpoints-api
- description: Webhooks from menus domain.
  name: CloudKitchens Menus Webhooks API
  slug: cloudkitchens-menus-webhooks-api
- description: 'Endpoints used by ordering marketplaces and other order sources to send orders to a store and keep them up to date. This domain lets an order source submit new orders as customers place them, reflect '
  name: CloudKitchens Orders Endpoints API
  slug: cloudkitchens-orders-endpoints-api
- description: Webhooks from orders domains.
  name: CloudKitchens Orders Webhooks API
  slug: cloudkitchens-orders-webhooks-api
- description: Endpoints to interact with with organizations/brands/stores and with integration connections.
  name: CloudKitchens Organization Endpoints API
  slug: cloudkitchens-organization-endpoints-api
- description: Endpoints to ping and test system authentication.
  name: CloudKitchens Ping Endpoints API
  slug: cloudkitchens-ping-endpoints-api
- description: Webhooks to ping and test the system integration.
  name: CloudKitchens Ping Webhooks API
  slug: cloudkitchens-ping-webhooks-api
- description: Endpoints to reports generation operations
  name: CloudKitchens Reports Endpoints API
  slug: cloudkitchens-reports-endpoints-api
- description: Webhooks from the reports generation operations
  name: CloudKitchens Reports Webhooks API
  slug: cloudkitchens-reports-webhooks-api
- description: Endpoints for review operations
  name: CloudKitchens Reviews Endpoints API
  slug: cloudkitchens-reviews-endpoints-api
- description: Endpoints to manage storefront state
  name: CloudKitchens Storefront Endpoints API
  slug: cloudkitchens-storefront-endpoints-api
- description: Webhooks from storefront domain.
  name: CloudKitchens Storefront Webhooks API
  slug: cloudkitchens-storefront-webhooks-api
artifact_total: 35
asyncapis:
- description: ''
  name: Cloudkitchens Webhooks
  slug: cloudkitchens-webhooks
collections:
- collection_type: open
  name: Public API
  slug: open-cloudkitchens-public-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cloudkitchens-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudkitchens-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudkitchens.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cloudkitchens.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-guides.cloudkitchens.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer-guides.cloudkitchens.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-guides.cloudkitchens.com/docs/onboard-application/
- group: operate
  title: ''
  type: Support
  url: https://support.cloudkitchens.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://cloudkitchens.com/faq
- group: company
  title: ''
  type: Blog
  url: https://cloudkitchens.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudkitchens.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudkitchens.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudkitchens-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/cloudkitchens-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloudkitchens-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudkitchens-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudkitchens-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudkitchens-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudkitchens-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudkitchens-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer-guides.cloudkitchens.com/api-reference/
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudkitchens-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cloudkitchens-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudkitchens-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cloudkitchens-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloudkitchens-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cloudkitchens-public-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudkitchens-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudkitchens-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudkitchens-domain-security.yml
created: '2026-08-01'
description: 'CloudKitchens, operated by City Storage Systems, builds and runs delivery-only "ghost kitchen" facilities and the restaurant technology stack that runs them, with sites across roughly 30 countries. For integration partners it publishes the CloudKitchens Public API — an OpenAPI 3.0.1 contract of 80 operations and 27 webhook events, secured with OAuth 2.0 across 29 scopes and two flows (client credentials and authorization code), backed by an OpenID Connect identity provider at iam.cloudkitchens.com. The API spans order injection and fulfillment, menu upsert and publishing, storefront pause/resume, delivery dispatch callbacks, finance and payout reporting, inventory, reviews, loyalty, and organization/brand/store pairing. Access is partner-gated rather than self-serve: applications, webhook endpoints, and stores are onboarded manually by a CloudKitchens Account Representative, who issues the Application ID and Client Secret for the production and staging environments and provisions
  the partner-specific API base URL.'
image: https://developer.cloudkitchens.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: CloudKitchens MCP Server
  slug: cloudkitchens-mcp-server
modified: '2026-08-01'
name: CloudKitchens
nav: Providers
network: true
overview: 'CloudKitchens publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Account Pairing Endpoints API, Account Pairing Webhooks API, Auth Endpoints API, and 24 more. Tagged areas include Restaurant, Ghost Kitchens, Food Delivery, Order Management, and Menu Management.


  The CloudKitchens catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CloudKitchens'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 24 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 3
  name: Cloudkitchens Rate Limits
  slug: cloudkitchens-rate-limits
scopes:
- name: Cloudkitchens Scopes
  scope_count: 31
  slug: cloudkitchens-scopes
  summary_line: 31 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 23
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.2
    developer_ergonomics: 39.9
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudkitchens/refs/heads/main/screenshots/cloudkitchens-2026-08-07T163508.png
security:
- kind: authentication
  name: Cloudkitchens Authentication
  slug: cloudkitchens-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cloudkitchens Domain Security
  slug: cloudkitchens-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cloudkitchens
tags:
- Restaurant
- Ghost Kitchens
- Food Delivery
- Order Management
- Menu Management
- Storefront
- Delivery
- Reporting
- Loyalty
- Real-Estate
website: https://www.cloudkitchens.com/
---

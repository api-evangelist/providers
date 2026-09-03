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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Hosted, remote Model Context Protocol server operated by WoowUp at mcp.woowup.com. Streamable-HTTP transport, OAuth 2.1 bearer authentication with RFC 8414 authorization-server and RFC 9728 protected-
  name: WoowUp MCP Server
  slug: woowup-mcp-server
- description: REST API for syncing customers (multi-ID), purchases, products, categories, branches, coupons, benefits, points, user events, custom attributes, abandoned carts, blacklists, segment exports, and integ
  name: WoowUp API v3
  slug: woowup-api-v3
artifact_total: 9
asyncapis:
- description: ''
  name: Woowup Webhooks
  slug: woowup-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/woowup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.woowup.com
- group: company
  title: ''
  type: Blog
  url: https://www.woowup.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.woowup.com/planes-y-precios
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.woowup.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.woowup.com/legal/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://help.woowup.com/es/
- group: start
  title: ''
  type: Login
  url: https://app.woowup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/woowup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.woowup.com
- group: start
  title: ''
  type: GettingStarted
  url: https://woowup-docs.gitbook.io/woowup-developer-docs/master
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/woowup-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/woowup-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/woowup-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/woowup-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/woowup-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/woowup-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/woowup-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/woowup-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/woowup-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/woowup-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/woowup-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/woowup-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/woowup-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/woowup-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/woowup-plans-pricing.yml
- group: docs
  title: ''
  type: APIReference
  url: https://woowup-docs.gitbook.io/woowup-developer-docs/api/users
created: '2026-07-17'
description: WoowUp is a customer marketing and loyalty CRM platform built for retail and ecommerce brands across Latin America. Founded in Buenos Aires and backed by 500 Global, WoowUp centralizes customer, purchase, and product data from POS and ecommerce platforms (VTEX, Magento, Shopify, WooCommerce, PrestaShop, Tienda Nube) and activates it through segmentation, campaigns, loyalty programs, web push notifications, and abandoned-cart recovery. Its REST API v3 lets developers sync users (multi-ID), purchases, products, coupons, benefits, points, and custom events, with client libraries published in PHP.
image: https://www.woowup.com/hubfs/Logo/favicon_.png
layout: provider
mcp_servers:
- description: 'WoowUp operates two reachable MCP surfaces. The primary one is a first-party hosted server at https://mcp.woowup.com/mcp — remote, streamable-HTTP, OAuth 2.1-protected, and gated: tools/list and initi'
  name: WoowUp MCP Server
  slug: woowup-mcp-server
modified: '2026-08-13'
name: WoowUp
nav: Providers
network: true
overview: 'WoowUp publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Loyalty, Customer Data, and Marketing Automation.


  The WoowUp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WoowUp''s developer surface includes engineering blog, pricing, support, documentation, getting-started guide, authentication, API reference, and 20 more developer resources.'
plans:
- name: Woowup Plans Pricing
  plan_count: 4
  slug: woowup-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Woowup Rate Limits
  slug: woowup-rate-limits
scopes:
- name: Woowup Scopes
  scope_count: 4
  slug: woowup-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials/deviceCode/implicit
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 48.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/woowup/refs/heads/main/screenshots/woowup-2026-08-17T082935.png
security:
- kind: authentication
  name: Woowup Authentication
  slug: woowup-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Woowup Domain Security
  slug: woowup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: woowup
tags:
- Company
- CRM
- Loyalty
- Customer Data
- Marketing Automation
- Retail
- E-Commerce
- Push Notifications
website: https://www.woowup.com
---

---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Everytable Agentic Access
  operation_count: 6
  slug: everytable-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: Everytable's Shopify storefront implements the Universal Commerce Protocol (UCP) and exposes it to agents as a Model Context Protocol (MCP) endpoint at https://everytable.com/api/ucp/mcp. The store ad
  name: Everytable Agentic Commerce API (UCP over MCP)
  slug: everytable-agentic-commerce-api-ucp-over-mcp
- description: 'Read-only product and collection JSON surfaced by the Everytable Shopify storefront and documented by Everytable in its own /llms.txt: product JSON at /products/{handle}.json, collection product JSON '
  name: Everytable Storefront Catalog (JSON)
  slug: everytable-storefront-catalog-json
- description: Shopify Customer Accounts authorization server for Everytable, discoverable anonymously at https://everytable.com/.well-known/openid-configuration and /.well-known/oauth-authorization-server. Issuer h
  name: Everytable Customer Account (OAuth 2.0 / OpenID Connect)
  slug: everytable-customer-account-oauth-20-openid-connect
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://everytable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://everytable.com/agents.md
- group: company
  title: ''
  type: Blog
  url: https://everytable.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://everytable.com/pages/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://everytable.com/pages/subscriptions
- group: start
  title: ''
  type: Login
  url: https://everytable.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://everytable.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://everytable.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://everytable.com/policies/refund-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everytable-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/everytable-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/everytable-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/everytable-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/everytable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/everytable-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/everytable-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/everytable-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/everytable-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/everytable-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/everytable-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/everytable-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everytable-domain-security.yml
created: '2026-08-04'
description: Everytable is a Los Angeles-based food company and social enterprise founded in 2015 by Sam Polk that sells scratch-cooked, ready-to-eat meals — bowls, salads, wraps, sandwiches, soups, kids meals and breakfast — through grab-and-go storefronts across Southern California and New York City, a home meal-delivery subscription, and food-service programs for workplaces (Everytable@WORK) and K-12 schools. Its variable-pricing model sets meal prices against the income level of each neighborhood it serves. Everytable runs no traditional developer program; its machine-readable surface is its Shopify storefront, which publishes agent-facing instructions at /agents.md and /llms.txt and implements the Universal Commerce Protocol (UCP) over an MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout, backed by Shopify Customer Account OAuth 2.0 / OpenID Connect.
image: https://everytable.com/cdn/shop/files/Favicon.png?v=1750436309
layout: provider
mcp_servers:
- description: ''
  name: everytable-mcp.yml
  slug: everytable-mcpyml
modified: '2026-08-04'
name: Everytable
nav: Providers
network: true
overview: 'Everytable publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Restaurants, Meal Delivery, and Ecommerce.


  Everytable''s developer surface includes documentation, engineering blog, support, pricing, authentication, and 18 more developer resources.'
random_paper: 115
rate_limits:
- limit_count: 0
  name: Everytable Rate Limits
  slug: everytable-rate-limits
scopes:
- name: Everytable Scopes
  scope_count: 4
  slug: everytable-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 26.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 26.9
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everytable/refs/heads/main/screenshots/everytable-2026-08-07T165045.png
security:
- kind: authentication
  name: Everytable Authentication
  slug: everytable-authentication
  summary_line: openIdConnect/oauth2/none · 3 schemes
- kind: domain-security
  name: Everytable Domain Security
  slug: everytable-domain-security
  summary_line: TLSv1.3 · DMARC
slug: everytable
tags:
- Company
- Food
- Restaurants
- Meal Delivery
- Ecommerce
- Agentic Commerce
- Shopify
- Social Enterprise
- Nutrition
- Subscriptions
website: https://everytable.com/
---

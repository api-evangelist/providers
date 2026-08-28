---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'The Shopify Storefront GraphQL API served on lemonperfect.com. Introspection is open anonymously: 428 types, 35 query fields and 41 mutations covering products, collections, search, carts, customer ac'
  name: Lemon Perfect Storefront GraphQL API
  slug: lemon-perfect-storefront-graphql-api
- description: A hosted Model Context Protocol endpoint implementing the Universal Commerce Protocol dev.ucp.shopping service (version 2026-04-08) for agent-driven catalog search, cart, checkout, fulfillment and ord
  name: Lemon Perfect UCP Agentic Commerce (MCP)
  slug: lemon-perfect-ucp-agentic-commerce-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://lemonperfect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lemonperfect.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://lemonperfect.com/.well-known/ucp
- group: start
  title: ''
  type: GettingStarted
  url: https://lemonperfect.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://lemonperfect.com/blogs/news
- group: company
  title: ''
  type: BlogRSS
  url: https://lemonperfect.com/blogs/news.atom
- group: operate
  title: ''
  type: Support
  url: https://lemonperfect.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://lemonperfect.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lemonperfect.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lemonperfect.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://lemonperfect.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://lemonperfect.com/policies/shipping-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lemon-perfect-llms.txt
- group: other
  title: ''
  type: AgentsMd
  url: llms/lemon-perfect-agents.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lemon-perfect-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lemon-perfect-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lemon-perfect-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/lemon-perfect-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/lemon-perfect-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lemon-perfect-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lemon-perfect-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lemon-perfect-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lemon-perfect-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemon-perfect-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Lemon Perfect is an Atlanta-based beverage company founded in 2017 by Yanni Hufnagel, making organic, zero-sugar flavored lemon water powered by half a squeezed organic lemon per bottle and 100% daily value vitamin C. It sells direct-to-consumer at lemonperfect.com alongside national retail distribution. It is not a software vendor and publishes no developer program, yet its storefront exposes a substantial machine-readable surface on its own apex domain: a Storefront GraphQL API with open introspection, a hosted Model Context Protocol endpoint implementing the Universal Commerce Protocol for agent-driven search, cart and checkout, OpenID Connect and RFC 8414 discovery for customer accounts, and first-party agent instructions at /agents.md and /llms.txt that set an explicit human-approval-before-payment policy.'
image: https://cdn.shopify.com/s/files/1/0032/0520/2020/files/Product_Lineup_52.jpg
layout: provider
mcp_servers:
- description: ''
  name: Lemon Perfect MCP Server
  slug: lemon-perfect-mcp-server
modified: '2026-08-04'
name: Lemon Perfect
nav: Providers
network: true
overview: 'Lemon Perfect publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Consumer Packaged Goods, E-Commerce, and Retail.


  Lemon Perfect''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 18 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 3
  name: Lemon Perfect Rate Limits
  slug: lemon-perfect-rate-limits
scopes:
- name: Lemon Perfect Scopes
  scope_count: 4
  slug: lemon-perfect-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken/jwtBearer
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 49.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 42.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemon-perfect/refs/heads/main/screenshots/lemon-perfect-2026-08-07T171544.png
security:
- kind: authentication
  name: Lemon Perfect Authentication
  slug: lemon-perfect-authentication
  summary_line: oauth2/openIdConnect/apiKey/agentIdentity · 4 schemes
- kind: domain-security
  name: Lemon Perfect Domain Security
  slug: lemon-perfect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lemon-perfect
tags:
- Company
- Beverages
- Consumer Packaged Goods
- E-Commerce
- Retail
- Direct to Consumer
- Agentic Commerce
- MCP
- GraphQL
- Universal Commerce Protocol
- Shopify
website: https://lemonperfect.com/
---

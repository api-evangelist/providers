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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The store's Universal Commerce Protocol surface — a live MCP endpoint for agent-driven catalog search, cart, checkout, and fulfillment, gated by an agent profile URI and buyer payment approval, plus r
  name: ShopShops Agent Commerce API (UCP)
  slug: shopshops-agent-commerce-api-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://shopshopslive.com
- group: operate
  title: ''
  type: Support
  url: https://www.shopshopslive.com/pages/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopshopslive.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shopshopslive.com/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shopshops-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopshops-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shopshops-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopshops-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shopshops-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopshops-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopshops-domain-security.yml
created: '2026-07-17'
description: 'ShopShops is a livestream commerce marketplace for authenticated pre-owned luxury and designer goods — handbags, jewelry, watches, accessories, and shoes sold through live shopping events and an online store. Buyers shop curated secondhand inventory with authentication (via Entrupy), buy-now-pay-later (Afterpay / Shop Pay), and return assurance (Seel). The storefront runs on Shopify and publishes a live agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile, an MCP endpoint for agent-driven catalog search and buyer-approved checkout, an OIDC/OAuth2 Customer Account API, and an llms.txt describing how AI shopping agents may transact with the store.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopshops.png
layout: provider
mcp_servers:
- description: ''
  name: shopshops-mcp.yml
  slug: shopshops-mcpyml
modified: '2026-07-21'
name: ShopShops
nav: Providers
network: true
overview: 'ShopShops publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Ecommerce, Marketplace, and Live Shopping.


  ShopShops'' developer surface includes support, authentication, and 9 more developer resources.'
random_paper: 47
scopes:
- name: Shopshops Scopes
  scope_count: 4
  slug: shopshops-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Shopshops Authentication
  slug: shopshops-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Shopshops Domain Security
  slug: shopshops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopshops
tags:
- Company
- Commerce
- Ecommerce
- Marketplace
- Live Shopping
- Luxury Resale
- Agent Commerce
- Shopify
website: https://shopshopslive.com
---

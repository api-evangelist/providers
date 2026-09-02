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
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mealsinminutes.co
- group: company
  title: ''
  type: Blog
  url: https://mealsinminutes.co/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://mealsinminutes.co/pages/contact
- group: start
  title: ''
  type: Login
  url: https://mealsinminutes.co/account/login
- group: start
  title: ''
  type: SignUp
  url: https://mealsinminutes.co/account/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mealsinminutes.co/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mealsinminutes.co/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meals-in-minutes-mim-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meals-in-minutes-mim-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meals-in-minutes-mim-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meals-in-minutes-mim-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/meals-in-minutes-mim-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meals-in-minutes-mim-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/meals-in-minutes-mim-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meals-in-minutes-mim-domain-security.yml
created: '2026-07-17'
description: 'Meals In Minutes (MIM) is a direct-to-consumer healthy meal company that sells portioned, prepped, vacuum-packed meal components — mix-and-match proteins, bases, and sides — delivered to the customer''s door. The storefront at mealsinminutes.co runs on Shopify and is backed by 500 Global. While MIM publishes no bespoke developer API, its Shopify store natively exposes an agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a hosted MCP endpoint at /api/ucp/mcp for buyer-approved agent checkout, Shopify Customer Accounts OpenID Connect (with a customer-account-mcp-api scope), a published /llms.txt and /agents.md with agent instructions, and the standard Shopify storefront product/collection JSON endpoints. This profile captures that agent-facing surface for the API Evangelist network.'
image: https://mealsinminutes.co/cdn/shop/files/banner_1.png?v=1762865371
layout: provider
mcp_servers:
- description: Meals In Minutes runs on Shopify and natively exposes a Universal Commerce Protocol (UCP) agent-commerce surface. A hosted MCP server accepts JSON-RPC POSTs at https://mealsinminutes.co/api/ucp/mcp (C
  name: Meals In Minutes UCP MCP
  slug: meals-in-minutes-ucp-mcp
modified: '2026-07-20'
name: Meals In Minutes, MIM
nav: Providers
network: true
overview: 'Meals In Minutes, MIM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Meal Delivery, E-Commerce, and Direct to Consumer.


  Meals In Minutes, MIM''s developer surface includes engineering blog, support, signup flow, authentication, and 12 more developer resources.'
random_paper: 2
scopes:
- name: Meals In Minutes Mim Scopes
  scope_count: 4
  slug: meals-in-minutes-mim-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meals-in-minutes-mim/refs/heads/main/screenshots/meals-in-minutes-mim-2026-08-07T172302.png
security:
- kind: authentication
  name: Meals In Minutes Mim Authentication
  slug: meals-in-minutes-mim-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Meals In Minutes Mim Domain Security
  slug: meals-in-minutes-mim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meals-in-minutes-mim
tags:
- Company
- Food and Beverage
- Meal Delivery
- E-Commerce
- Direct to Consumer
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
website: https://mealsinminutes.co
---

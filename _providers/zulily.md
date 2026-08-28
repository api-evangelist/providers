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
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Zulily's agent-facing commerce API implementing the Universal Commerce Protocol (UCP) over a JSON-RPC MCP endpoint — search the catalog, build a cart, and run a buyer-approved checkout.
  name: Zulily UCP Shopping (MCP)
  slug: zulily-ucp-shopping-mcp
- description: OpenID Connect / OAuth 2.0 authentication and customer-account access for Zulily shoppers, provided by the Shopify Customer Account API, including an MCP-scoped agent surface.
  name: Zulily Customer Account API (Shopify)
  slug: zulily-customer-account-api-shopify
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.zulily.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zulily-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zulily-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: llms/zulily-agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zulily-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zulily-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zulily-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zulily-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zulily-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zulily.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zulily.com/policies/terms-of-service
created: '2026-07-17'
description: 'Zulily is an online retailer of daily deals on apparel, home, toys, and lifestyle goods. After its 2023 shutdown the brand was acquired and relaunched as a Shopify-hosted store. The relaunched storefront is agent-native: it implements the Universal Commerce Protocol (UCP) with a JSON-RPC MCP shopping endpoint, exposes OpenID Connect / OAuth 2.0 authentication via the Shopify Customer Account API (including a customer-account-mcp-api scope), and publishes an llms.txt / agents.md describing how AI shopping agents can discover products and run buyer-approved checkouts. This profile was surfaced as an a16z / Trinity Ventures portfolio company and enriched from Zulily''s real public agent-commerce surface.'
image: https://www.zulily.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Zulily MCP Server
  slug: zulily-mcp-server
modified: '2026-07-21'
name: Zulily
nav: Providers
network: true
overview: 'Zulily publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Shopping, and Commerce.


  Zulily''s developer surface includes authentication and 11 more developer resources.'
random_paper: 9
scopes:
- name: Zulily Scopes
  scope_count: 4
  slug: zulily-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Zulily Authentication
  slug: zulily-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
slug: zulily
tags:
- Company
- E-Commerce
- Retail
- Shopping
- Commerce
- Agent Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://www.zulily.com
---

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
  score: 21.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Shopify-native Universal Commerce Protocol surface for the Shoptiques storefront — agent-driven catalog search, cart, checkout and fulfillment over a published MCP endpoint, with buyer-approved paymen
  name: Shoptiques Agentic Commerce (UCP)
  slug: shoptiques-agentic-commerce-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shoptiques-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shoptiques.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shoptiques-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shoptiques-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shoptiques-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shoptiques-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shoptiques-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shoptiques-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shoptiques.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shoptiques.com/policies/terms-of-service
created: '2026-07-17'
description: 'Shoptiques is an online marketplace that brings thousands of independently owned local boutiques online, letting shoppers discover unique, one-of-a-kind fashion and home decor from over 5,000 stores. Founded in 2012 by Olga Vidisheva, the business rebranded its merchant/POS arm as Material in 2023 while continuing to operate the Shoptiques consumer marketplace. The storefront at shoptiques.com now runs on Shopify and exposes a modern agent-facing commerce surface: a published llms.txt / agents.md, Shopify Customer Account OpenID Connect + OAuth 2.0 authentication, and a Universal Commerce Protocol (UCP) MCP endpoint for buyer-approved, agent-driven shopping and checkout.'
image: https://shoptiques.com/cdn/shop/files/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Shoptiques MCP Server
  slug: shoptiques-mcp-server
modified: '2026-07-21'
name: Shoptiques
nav: Providers
network: true
overview: 'Shoptiques publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Marketplace, and Boutiques.


  Shoptiques'' developer surface includes authentication and 10 more developer resources.'
random_paper: 17
scopes:
- name: Shoptiques Scopes
  scope_count: 4
  slug: shoptiques-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shoptiques/refs/heads/main/screenshots/shoptiques-2026-09-02T155306.png
security:
- kind: authentication
  name: Shoptiques Authentication
  slug: shoptiques-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Shoptiques Domain Security
  slug: shoptiques-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shoptiques
tags:
- Company
- E-Commerce
- Retail
- Marketplace
- Boutiques
- Fashion
- Agentic Commerce
- Shopify
- MCP
- UCP
website: https://shoptiques.com
---

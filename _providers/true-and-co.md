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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the True & Co Shopify storefront: a hosted Universal Commerce Protocol (UCP) MCP endpoint for catalog search, cart, and checkout, backed by Shopify Customer Account O'
  name: True & Co UCP Agent Commerce
  slug: true-co-ucp-agent-commerce
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/true-and-co-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/true-and-co-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/true-and-co-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/true-and-co-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/true-and-co-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/true-and-co-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/true-and-co-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trueandco.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trueandco.com/policies/privacy-policy
created: '2026-07-17'
description: 'True & Co is a direct-to-consumer women''s intimates and lingerie brand, originally venture-backed (Cowboy Ventures, Uncork Capital) and now operating under PVH Corp. It sells bras, underwear, and loungewear online through a Shopify-hosted storefront at trueandco.com. The store exposes no traditional developer API, but it does expose a modern agent-commerce surface: a hosted Universal Commerce Protocol (UCP) MCP endpoint for catalog, cart, and checkout, Shopify Customer Account OAuth 2.0 / OIDC for buyer identity, a public read-only storefront JSON surface, and an agent-facing llms.txt / agents.md.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/true-and-co.png
layout: provider
mcp_servers:
- description: ''
  name: true-and-co-mcp.yml
  slug: true-and-co-mcpyml
modified: '2026-07-21'
name: True & Co
nav: Providers
network: true
overview: 'True & Co publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Apparel.


  True & Co''s developer surface includes authentication and 8 more developer resources.'
random_paper: 54
scopes:
- name: True And Co Scopes
  scope_count: 0
  slug: true-and-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.8
  delta: -0.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.4
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: True And Co Authentication
  slug: true-and-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: True And Co Domain Security
  slug: true-and-co-domain-security
  summary_line: no transport/DNS hardening detected
slug: true-and-co
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Apparel
- Intimates
- Agentic Commerce
- Shopify
- MCP
---

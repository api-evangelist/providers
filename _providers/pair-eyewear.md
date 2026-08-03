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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Shopify-hosted Universal Commerce Protocol shopping service exposed over MCP for agent-driven catalog search, cart, and buyer-approved checkout on the Pair Eyewear storefront.
  name: Pair Eyewear Agent Commerce (UCP/MCP)
  slug: pair-eyewear-agent-commerce-ucpmcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://paireyewear.com
- group: docs
  title: ''
  type: Documentation
  url: https://paireyewear.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://paireyewear.com/pages/help-center
- group: company
  title: ''
  type: Blog
  url: https://paireyewear.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://paireyewear.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paireyewear.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paireyewear.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pair-eyewear-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pair-eyewear-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pair-eyewear-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pair-eyewear-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pair-eyewear-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pair-eyewear-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pair-eyewear-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pair-eyewear-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Pair Eyewear is a direct-to-consumer eyewear brand known for its modular, magnetic Top Frames system: customers pick a base optical or sunglasses frame and swap interchangeable magnetic top frames in hundreds of patterns and licensed collaborations (Disney, Marvel, MLB, and more). Prescription and blue-light lenses are made and hand-assembled in California, with frames starting around $80, free shipping and 30-day returns, and a Pair+ membership. The paireyewear.com storefront runs on Shopify and exposes an agent-native commerce surface — a published agents.md and llms.txt, Shopify Customer Accounts OpenID Connect, and a live Universal Commerce Protocol (UCP) MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout.'
image: https://paireyewear.com/cdn/shop/files/PAIR_SEO-Image.jpg
layout: provider
mcp_servers:
- description: ''
  name: pair-eyewear-mcp.yml
  slug: pair-eyewear-mcpyml
modified: '2026-07-20'
name: Pair Eyewear
nav: Providers
network: true
overview: 'Pair Eyewear publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Eyewear, Ecommerce, and Retail.


  Pair Eyewear''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 11 more developer resources.'
random_paper: 87
scopes:
- name: Pair Eyewear Scopes
  scope_count: 4
  slug: pair-eyewear-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 25.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Pair Eyewear Authentication
  slug: pair-eyewear-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Pair Eyewear Domain Security
  slug: pair-eyewear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pair-eyewear
tags:
- Company
- Consumer
- Eyewear
- Ecommerce
- Retail
- Shopify
- Direct-to-Consumer
- Agent Commerce
- MCP
- UCP
website: https://paireyewear.com
---

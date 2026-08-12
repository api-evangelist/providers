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
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'The footway.com storefront''s agent-facing commerce surface. Built on Shopify, it implements the Universal Commerce Protocol (UCP) for agent-driven commerce: a UCP merchant profile at /.well-known/ucp '
  name: Footway Agent Commerce (UCP)
  slug: footway-agent-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.footway.co.uk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://footway.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://footway.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/footway-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/footway-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/footway-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/footway-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/footway-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/footway-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/footway-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/footway-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://footway.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://footway.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://footway.com/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://footway.com/account
- group: company
  title: ''
  type: Blog
  url: https://about.footway.com
created: '2026-07-17'
description: 'Footway is a Nordic, data-driven e-commerce group (Nasdaq First North Growth Market, Stockholm) that operates the Footway footwear-and-fashion marketplace across roughly 24 European markets, carrying around 800 brands for more than two million customers, alongside its Operations-as-a-Service ("ECOM IN A BOX") merchant infrastructure at footwayplus.com / oaas.footway.com and a merchant portal at merchant.footwayplus.com. The consumer storefront at footway.com runs on Shopify and exposes an agent-native commerce surface: an llms.txt / agents.md agent guide, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a UCP MCP endpoint for buyer-approved agent checkout, and Shopify Customer Account OpenID Connect / OAuth 2.0 authentication.'
image: https://footway.com/cdn/shop/files/Namnlos_presentation_4_245a932a-42a0-441f-bdd5-b609ade84b97.svg?v=1744815789
layout: provider
mcp_servers:
- description: ''
  name: footway-mcp.yml
  slug: footway-mcpyml
modified: '2026-07-19'
name: Footway
nav: Providers
network: true
overview: 'Footway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-commerce, Marketplace, and Retail.


  Footway''s developer surface includes documentation, authentication, support, signup flow, engineering blog, and 12 more developer resources.'
random_paper: 81
scopes:
- name: Footway Scopes
  scope_count: 4
  slug: footway-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.0
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 45.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 26.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/footway/refs/heads/main/screenshots/footway-2026-07-25T214920.png
security:
- kind: authentication
  name: Footway Authentication
  slug: footway-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Footway Domain Security
  slug: footway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: footway
tags:
- Company
- Consumer
- E-commerce
- Marketplace
- Retail
- Footwear
- Fashion
- Shopify
- Agent Commerce
- UCP
- MCP
- Nordic
website: https://www.footway.co.uk
---

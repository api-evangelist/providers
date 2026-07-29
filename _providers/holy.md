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
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'HOLY''s Shopify-powered storefront and its agentic-commerce surface: a hosted Storefront MCP server (product search, cart, policies), a Universal Commerce Protocol (UCP) endpoint, Shopify Customer Acco'
  name: HOLY Storefront & Agentic Commerce
  slug: holy-storefront-agentic-commerce
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://de.holy.com
- group: company
  title: ''
  type: About
  url: https://de.holy.com/pages/our-story
- group: operate
  title: ''
  type: Support
  url: https://de.holy.com/pages/help-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://de.holy.com/pages/help-center
- group: operate
  title: ''
  type: Contact
  url: https://de.holy.com/pages/contact-form
- group: commercial
  title: ''
  type: TermsOfService
  url: https://de.holy.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://de.holy.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://de.holy.com/account
- group: agent
  title: ''
  type: MCPServer
  url: mcp/holy-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/holy-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/holy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/holy-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/holy-openid-configuration.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/holy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/holy-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/holy-domain-security.yml
created: '2026-07-17'
description: 'HOLY is a German direct-to-consumer beverage brand offering sugar-free, powdered and syrup-based drink mixes that customers prepare with water or milk. Its product families span HOLY Energy (caffeine and vitamins), HOLY Iced Tea, HOLY Hydration (isotonic electrolytes), HOLY Milkshake (low-calorie), and HOLY Syrup. Founded by three friends (Matze, Fred, and Phil), the company grew from a shared apartment to 50+ employees, 2 million customers, and 500,000+ social followers, positioned on "great taste with a good conscience." HOLY sells online via a Shopify storefront and exposes a modern agentic-commerce surface: a hosted Storefront MCP server, a Universal Commerce Protocol (UCP) endpoint, llms.txt / agents.md agent instructions, and Shopify Customer Account OAuth/OIDC.'
image: https://de.holy.com/cdn/shop/files/holy-syrup-2.png?v=1775851476
layout: provider
mcp_servers:
- description: ''
  name: holy-mcp.yml
  slug: holy-mcpyml
modified: '2026-07-19'
name: HOLY
nav: Providers
network: true
overview: 'HOLY publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Beverages, Direct-to-Consumer, and Ecommerce.


  HOLY''s developer surface includes support, authentication, and 15 more developer resources.'
random_paper: 39
scopes:
- name: Holy Scopes
  scope_count: 4
  slug: holy-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.6
  delta: -0.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.2
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Holy Authentication
  slug: holy-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Holy Domain Security
  slug: holy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: holy
tags:
- Company
- Consumer
- Beverages
- Direct-to-Consumer
- Ecommerce
- Agentic Commerce
- Shopify
- Germany
website: https://de.holy.com
---

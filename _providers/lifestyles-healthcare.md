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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The LifeStyles US store implements the Universal Commerce Protocol for agent-driven commerce. Agents discover the merchant profile at /.well-known/ucp and then call the JSON-RPC MCP endpoint to search
  name: LifeStyles US UCP Shopping (MCP)
  slug: lifestyles-us-ucp-shopping-mcp
- description: Unauthenticated read-only JSON endpoints over the LifeStyles US Shopify storefront - product listings, individual products, collections, search and cart state - which the store's own agent instruction
  name: LifeStyles US Storefront JSON
  slug: lifestyles-us-storefront-json
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lifestyles-healthcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lifestyles.com
- group: docs
  title: ''
  type: Documentation
  url: https://lifestyles.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lifestyles-healthcare-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lifestyles-healthcare-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lifestyles-healthcare-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lifestyles-healthcare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lifestyles-healthcare-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lifestyles-healthcare-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lifestyles-healthcare-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lifestyles-healthcare-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lifestyles-healthcare-lifecycle.yml
- group: company
  title: ''
  type: Blog
  url: https://lifestyles.com/blogs/sexual-health-safe-sex
- group: operate
  title: ''
  type: Support
  url: https://lifestyles.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lifestyles.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lifestyles.com/policies/privacy-policy
created: '2026-07-17'
description: 'LifeStyles Healthcare Pte Ltd is a global sexual wellness company that owns the LifeStyles condom and personal lubricant brands, tracing its origin to the condom business founded by Eric Ansell in Richmond, Australia in 1905. The company sells a broad range of latex and non-latex condoms, personal lubricants, and pleasure products across North American and international markets, and holds the LifeStyles trademarks and intellectual property across multiple jurisdictions. Its North American direct-to-consumer storefront at lifestyles.com runs on Shopify and exposes a genuinely agent-native commerce surface: a published llms.txt and agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live UCP shopping MCP endpoint for agent-driven catalog search, cart and checkout, and Shopify Customer Accounts OpenID Connect for buyer-scoped access. There is no traditional developer portal or first-party REST API program.'
image: https://cdn.shopify.com/s/files/1/0610/3810/0706/files/lifestyles-logo_726b0e33-aa28-4543-ac4a-34ce08153d2a.png
layout: provider
mcp_servers:
- description: ''
  name: lifestyles-healthcare-mcp.yml
  slug: lifestyles-healthcare-mcpyml
modified: '2026-07-19'
name: LifeStyles Healthcare
nav: Providers
network: true
overview: 'LifeStyles Healthcare publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Sexual Wellness, Consumer Packaged Goods, and E-Commerce.


  LifeStyles Healthcare''s developer surface includes documentation, authentication, engineering blog, support, and 13 more developer resources.'
random_paper: 92
scopes:
- name: Lifestyles Healthcare Scopes
  scope_count: 0
  slug: lifestyles-healthcare-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lifestyles-healthcare/refs/heads/main/screenshots/lifestyles-healthcare-2026-08-07T171647.png
security:
- kind: authentication
  name: Lifestyles Healthcare Authentication
  slug: lifestyles-healthcare-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Lifestyles Healthcare Domain Security
  slug: lifestyles-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lifestyles-healthcare
tags:
- Company
- Healthcare
- Sexual Wellness
- Consumer Packaged Goods
- E-Commerce
- Agentic Commerce
- Model Context Protocol
- Shopify
- Retail
website: https://lifestyles.com
---

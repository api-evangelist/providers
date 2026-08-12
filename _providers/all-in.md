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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.5
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'Agent-native commerce surface on the All In Food Shopify storefront: a UCP merchant profile, a hosted MCP endpoint for catalog/cart/checkout, Customer Account OIDC, and a canonical agents.md instructi'
  name: All In Food Agent Commerce (UCP)
  slug: all-in-food-agent-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://allinfood.com
- group: company
  title: ''
  type: Blog
  url: https://allinfood.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://allinfood.com/pages/faqs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allinfood.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allinfood.com/policies/terms-of-service
- group: auth
  title: ''
  type: DomainSecurity
  url: security/all-in-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/all-in-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/all-in-llms.txt
created: '2026-07-17'
description: 'All In Food makes organic, gluten-free nut & seed snack bars on a social-impact model — every bar purchased helps fund local nutritious-food-access initiatives such as food banks, community gardens, and meal programs across the U.S. The company is backed by Obvious Ventures (a reported $4M raise) and sells through Sprouts and Starbucks as well as its own online store. While All In is a consumer-packaged-goods brand rather than a developer platform, its Shopify storefront exposes a genuine agent-native commerce surface: a canonical agents.md document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live hosted MCP endpoint at /api/ucp/mcp for agent-driven catalog search, cart, checkout and fulfillment, and Shopify Customer Account OpenID Connect for buyer identity. Checkout always requires explicit human buyer approval on payment.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/all-in.png
layout: provider
mcp_servers:
- description: ''
  name: all-in-mcp.yml
  slug: all-in-mcpyml
modified: '2026-07-17'
name: All In
nav: Providers
network: true
overview: 'All In publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Snacks, Nutrition, and Consumer Packaged Goods.


  All In''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 109
scopes:
- name: All In Scopes
  scope_count: 0
  slug: all-in-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.9
  delta: -1.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 17.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/all-in/refs/heads/main/screenshots/all-in-2026-08-07T161209.png
security:
- kind: authentication
  name: All In Authentication
  slug: all-in-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: All In Domain Security
  slug: all-in-domain-security
  summary_line: TLSv1.3 · DMARC
slug: all-in
tags:
- Company
- Food
- Snacks
- Nutrition
- Consumer Packaged Goods
- Commerce
- Agent Commerce
- Shopify
- MCP
website: https://allinfood.com
---

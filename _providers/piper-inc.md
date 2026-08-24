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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Agent-driven commerce for the Piper storefront over the Universal Commerce Protocol (UCP), exposed as an MCP endpoint on the store's Shopify platform (store id 9256256). Catalog search/lookup, cart, c
  name: Piper Commerce (UCP)
  slug: piper-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://playpiper.in
- group: company
  title: ''
  type: Blog
  url: https://www.playpiper.in/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.playpiper.in/pages/getsupport
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.playpiper.in/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.playpiper.in/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/piper-inc-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/piper-inc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/piper-inc-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/piper-inc-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/piper-inc-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/piper-inc-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/piper-inc-domain-security.yml
created: '2026-07-17'
description: 'Piper (Piper Learning, Inc. / Piper LLC) is an educational-technology company that makes hands-on STEM learning kits — most notably the Piper Computer Kit, a buildable wooden computer that teaches circuitry and coding through Minecraft, and Piper Make, a browser-based platform for exploring electronics and Python. Its consumer storefront runs on Shopify and exposes an agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile with an MCP endpoint plus Shopify Customer Account OpenID Connect, letting AI shopping agents search the catalog, build carts, and check out with explicit buyer approval. Surfaced as a 500 Global portfolio company and enriched from its live public agent/discovery surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/piper-inc.png
layout: provider
mcp_servers:
- description: ''
  name: Piper Inc. MCP Server
  slug: piper-inc-mcp-server
modified: '2026-07-20'
name: Piper Inc.
nav: Providers
network: true
overview: 'Piper Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, STEM, and Hardware.


  Piper Inc.''s developer surface includes engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 0
scopes:
- name: Piper Inc Scopes
  scope_count: 4
  slug: piper-inc-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.5
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
  previous_composite: 24.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Piper Inc Authentication
  slug: piper-inc-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Piper Inc Domain Security
  slug: piper-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: piper-inc
tags:
- Company
- Education
- EdTech
- STEM
- Hardware
- E-Commerce
- Agentic Commerce
- MCP
- Shopify
website: https://playpiper.in
---

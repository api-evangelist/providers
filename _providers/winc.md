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
    well_known_catalog: true
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Agentic-commerce API for the Winc storefront, implemented via the Shopify-native Universal Commerce Protocol (UCP). Agents discover capabilities at /.well-known/ucp and call commerce tools over the MC
  name: Winc UCP Commerce MCP
  slug: winc-ucp-commerce-mcp
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://winc.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/winc-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/winc-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/winc-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/winc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/winc-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/winc-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/winc-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.winc.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.winc.com/policies/terms-of-service
created: '2026-07-17'
description: 'Winc is a direct-to-consumer online wine club and retailer (winc.com) offering curated, personalized wine subscriptions and single-bottle purchases matched to a member''s palate profile. The winc.com storefront runs on Shopify and exposes a modern agentic-commerce surface: a hosted UCP (Universal Commerce Protocol) MCP endpoint, Shopify Customer Account API authentication (OpenID Connect), and published /llms.txt and /agents.md agent instructions that let AI shopping assistants discover the catalog, build carts, and drive buyer-approved checkout. Originally surfaced as a VC portfolio company and enriched from its public agent-facing surface by the API Evangelist enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/winc.png
layout: provider
mcp_servers:
- description: ''
  name: winc-mcp.yml
  slug: winc-mcpyml
modified: '2026-07-21'
name: Winc
nav: Providers
network: true
overview: 'Winc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wine, Ecommerce, Retail, and Subscription.


  Winc''s developer surface includes authentication and 10 more developer resources.'
random_paper: 94
scopes:
- name: Winc Scopes
  scope_count: 0
  slug: winc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 21.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 18.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Winc Authentication
  slug: winc-authentication
  summary_line: 1 scheme
slug: winc
tags:
- Company
- Wine
- Ecommerce
- Retail
- Subscription
- Agentic Commerce
- MCP
- Shopify
- UCP
website: https://winc.com
---

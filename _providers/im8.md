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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'The agent-native commerce surface of the IM8 Health Shopify storefront: a Universal Commerce Protocol (UCP) merchant profile with a hosted MCP shopping endpoint (catalog search, cart, checkout, fulfil'
  name: IM8 Health Agent Commerce Surface
  slug: im8-health-agent-commerce-surface
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/im8-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://im8health.com
- group: docs
  title: ''
  type: Documentation
  url: https://im8health.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/im8-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/im8-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/im8-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/im8-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/im8-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/im8-conformance.yml
- group: company
  title: ''
  type: Blog
  url: https://im8health.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://im8health.com/account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://im8health.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://im8health.com/policies/terms-of-service
created: '2026-07-17'
description: 'IM8 Health is a health and wellness company whose flagship product, IM8 Daily Ultimate Essentials, is a clinically studied, third-party tested all-in-one daily supplement combining 90 nutrient-rich ingredients — vitamins, minerals, probiotics, prebiotics, adaptogens and superfoods — into a single drink that replaces roughly 16 capsules. Co-founded by David Beckham and guided by a named scientific advisory board, IM8 sells direct-to-consumer through its Shopify-powered online store at im8health.com. That storefront exposes a modern agent-native commerce surface: a Universal Commerce Protocol (UCP) merchant profile, a hosted Model Context Protocol (MCP) shopping endpoint, an llms.txt / agents.md guide for AI shopping assistants, and Shopify Customer Account OAuth 2.0 / OpenID Connect authentication (including customer-account-mcp-api scopes). IM8 is a General Catalyst portfolio company added to the API Evangelist network and enriched from its public agent-commerce surface.'
image: https://im8health.com/cdn/shop/files/im8-meta-image_1_-min.jpg
layout: provider
mcp_servers:
- description: Hosted Model Context Protocol (MCP) shopping endpoint exposed by the IM8 Health Shopify storefront via the Universal Commerce Protocol (UCP). Discovered from the store's /.well-known/ucp merchant prof
  name: IM8 Health UCP Shopping MCP
  slug: im8-health-ucp-shopping-mcp
modified: '2026-07-19'
name: IM8 Health
nav: Providers
network: true
overview: 'IM8 Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Wellness, Supplements, and Nutrition.


  IM8 Health''s developer surface includes documentation, authentication, engineering blog, and 10 more developer resources.'
random_paper: 18
scopes:
- name: Im8 Scopes
  scope_count: 0
  slug: im8-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.1
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/im8/refs/heads/main/screenshots/im8-2026-08-07T170629.png
security:
- kind: authentication
  name: Im8 Authentication
  slug: im8-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Im8 Domain Security
  slug: im8-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: im8
tags:
- Company
- Health
- Wellness
- Supplements
- Nutrition
- E-Commerce
- Direct to Consumer
- Agentic Commerce
- Shopify
- UCP
- MCP
website: https://im8health.com
---

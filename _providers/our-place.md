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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://fromourplace.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/our-place-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/our-place-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/our-place-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/our-place-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/our-place-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/our-place-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fromourplace.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fromourplace.com/policies/terms-of-service
created: '2026-07-17'
description: 'Our Place is a direct-to-consumer kitchenware and cookware brand, best known for the multi-purpose Always Pan, selling cookware, bakeware, appliances, tableware, and kitchen tools at fromourplace.com. Surfaced as a portfolio company of 8vc, its digital storefront runs on Shopify and exposes a native agentic-commerce surface: a Universal Commerce Protocol (UCP) merchant profile, a hosted Model Context Protocol (MCP) shopping endpoint, Shopify Customer Account OpenID Connect authentication, and an agent-facing llms.txt / agents.md. This profile was enriched by the API Evangelist pipeline from the company''s live public agent surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/our-place.png
layout: provider
mcp_servers:
- description: ''
  name: our-place-mcp.yml
  slug: our-place-mcpyml
modified: '2026-07-20'
name: Our Place
nav: Providers
network: true
overview: 'Our Place is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, Retail, Cookware, and Consumer.


  Our Place''s developer surface includes authentication and 8 more developer resources.'
random_paper: 57
scopes:
- name: Our Place Scopes
  scope_count: 4
  slug: our-place-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 15.0
  delta: 0.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.9
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Our Place Authentication
  slug: our-place-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Our Place Domain Security
  slug: our-place-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: our-place
tags:
- Company
- Ecommerce
- Retail
- Cookware
- Consumer
- Agentic Commerce
- Shopify
website: https://fromourplace.com
---

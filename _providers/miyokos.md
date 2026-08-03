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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://miyokos.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.miyokos.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.miyokos.com/policies/terms-of-service
- group: agent
  title: ''
  type: WellKnown
  url: well-known/miyokos-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/miyokos-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/miyokos-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/miyokos-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/miyokos-domain-security.yml
created: '2026-07-17'
description: 'Miyoko''s Creamery (miyokos.com) is a plant-based dairy company in the planetary-health sector, backed by Obvious Ventures, making vegan butter and cheese from cultured cashews, oats, and legumes. The company does not publish a first-party developer REST API; its digital surface is a Shopify-hosted storefront. That storefront exposes a genuine agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a hosted shopping MCP endpoint for search/cart/checkout, Shopify Customer Account OIDC/OAuth for identity, and an /llms.txt with agent instructions. This profile was enriched by probing that public surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/miyokos.png
layout: provider
mcp_servers:
- description: ''
  name: miyokos-mcp.yml
  slug: miyokos-mcpyml
modified: '2026-07-20'
name: Miyokos
nav: Providers
network: true
overview: 'Miyokos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Planetary Health, Plant-Based, Food and Beverage, and Ecommerce.


  Miyokos'' developer surface includes authentication and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.0
  provenance:
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Miyokos Authentication
  slug: miyokos-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Miyokos Domain Security
  slug: miyokos-domain-security
  summary_line: TLSv1.3 · HSTS
slug: miyokos
tags:
- Company
- Planetary Health
- Plant-Based
- Food and Beverage
- Ecommerce
- Shopify
- Agent Commerce
- UCP
website: https://miyokos.com
---

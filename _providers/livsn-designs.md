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
  url: https://livsndesigns.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/livsn-designs-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/livsn-designs-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/livsn-designs-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/livsn-designs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/livsn-designs-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livsn-designs-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livsndesigns.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.livsndesigns.com/policies/terms-of-service
created: '2026-07-17'
description: 'Livsn Designs is a Techstars-backed outdoor apparel brand that makes durable, minimalist technical clothing (its Flex Canvas pants and multi-use travel and hiking apparel) sold direct-to-consumer from a Shopify storefront at livsndesigns.com. It publishes no first-party developer API or documentation portal. Its only programmatic surface is the agent-commerce layer Shopify serves on the merchant''s own domain: a Universal Commerce Protocol (UCP) shopping MCP endpoint for agent-driven checkout, a Shopify Customer Account OIDC/OAuth2 authorization server, and an llms.txt / agents.md agent-instructions document. This profile captures that real agent surface; there is no bespoke API to catalog.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/livsn-designs.png
layout: provider
mcp_servers:
- description: ''
  name: Livsn Designs UCP shopping MCP
  slug: livsn-designs-ucp-shopping-mcp
modified: '2026-07-20'
name: Livsn Designs
nav: Providers
network: true
overview: 'Livsn Designs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-commerce, Apparel, and Outdoor.


  Livsn Designs'' developer surface includes authentication and 8 more developer resources.'
random_paper: 20
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
  name: Livsn Designs Authentication
  slug: livsn-designs-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Livsn Designs Domain Security
  slug: livsn-designs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: livsn-designs
tags:
- Company
- Retail
- E-commerce
- Apparel
- Outdoor
- Shopify
- Agent Commerce
- UCP
- MCP
website: https://livsndesigns.com/
---

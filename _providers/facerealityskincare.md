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
  score: 24.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Shopify-hosted commerce surface for the Face Reality Skincare store. Exposes a hosted Storefront MCP server for catalog search, product lookup, and cart building, a UCP merchant profile for agent-driv
  name: Face Reality Skincare Commerce (Shopify Storefront MCP)
  slug: face-reality-skincare-commerce-shopify-storefront-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://facerealityskincare.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/facerealityskincare-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/facerealityskincare-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/facerealityskincare-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/facerealityskincare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/facerealityskincare-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/facerealityskincare-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/facerealityskincare-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/facerealityskincare-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://facerealityskincare.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://facerealityskincare.com/policies/terms-of-service
created: '2026-07-17'
description: 'Face Reality Skincare is a professional acne-treatment skincare brand whose online store, at facerealityskincare.com, is built on Shopify. Beyond the consumer storefront, the store publishes a full agent-commerce surface: a hosted Storefront MCP server (5 shop/cart tools), a Universal Commerce Protocol (UCP) merchant profile, a Shopify Customer Account API exposed via OpenID Connect / OAuth 2.0 discovery, and a published llms.txt / agents.md describing how AI shopping agents may browse, build carts, and hand off to a human-approved checkout. Surfaced as a portfolio company of Norwest Venture Partners and enriched into the API Evangelist network from its live public discovery documents.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/facerealityskincare.png
layout: provider
mcp_servers:
- description: ''
  name: facerealityskincare-mcp.yml
  slug: facerealityskincare-mcpyml
modified: '2026-07-19'
name: Face Reality Skincare
nav: Providers
network: true
overview: 'Face Reality Skincare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Skincare, Beauty, Cosmetics, and Ecommerce.


  Face Reality Skincare''s developer surface includes authentication and 11 more developer resources.'
random_paper: 7
scopes:
- name: Facerealityskincare Scopes
  scope_count: 4
  slug: facerealityskincare-scopes
  summary_line: 4 scopes
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Facerealityskincare Authentication
  slug: facerealityskincare-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Facerealityskincare Domain Security
  slug: facerealityskincare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: facerealityskincare
tags:
- Company
- Skincare
- Beauty
- Cosmetics
- Ecommerce
- Shopify
- Commerce
- Agent Commerce
- MCP
website: https://facerealityskincare.com
---

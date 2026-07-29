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
  url: https://circulodebelleza.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/circulo-de-belleza-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/circulo-de-belleza-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/circulo-de-belleza-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/circulo-de-belleza-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/circulo-de-belleza-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/circulo-de-belleza-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circulo-de-belleza-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.circulodebelleza.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.circulodebelleza.com/policies/terms-of-service
created: '2026-07-17'
description: 'Círculo de Belleza is an authorized distributor of professional beauty products in Mexico, operating an e-commerce storefront at circulodebelleza.com. It sells salon-quality hair care, hair color, nail, barbershop, and facial/spa supplies from 40+ professional brands (L''Oréal Professionnel, Olaplex, Wella, Schwarzkopf, Matrix, Alfaparf Milano) at professional pricing with no minimum purchase, same-day fulfillment, and nationwide Mexico delivery. The store is built on Shopify and exposes a native agent-commerce surface: a published llms.txt/agents.md, OpenID Connect and OAuth authorization-server discovery documents, and a Universal Commerce Protocol (UCP) MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/circulo-de-belleza.png
layout: provider
mcp_servers:
- description: ''
  name: Círculo de Belleza UCP/MCP endpoint
  slug: círculo-de-belleza-ucpmcp-endpoint
modified: '2026-07-18'
name: Circulo de Belleza
nav: Providers
network: true
overview: 'Circulo de Belleza is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Cosmetics, E-Commerce, and Retail.


  Circulo de Belleza''s developer surface includes authentication and 9 more developer resources.'
random_paper: 19
scopes:
- name: Circulo De Belleza Scopes
  scope_count: 4
  slug: circulo-de-belleza-scopes
  summary_line: 4 scopes · authorizationCode
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
  name: Circulo De Belleza Authentication
  slug: circulo-de-belleza-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Circulo De Belleza Domain Security
  slug: circulo-de-belleza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circulo-de-belleza
tags:
- Company
- Beauty
- Cosmetics
- E-Commerce
- Retail
- Mexico
- Hair Care
- Professional Beauty Products
- Shopify
- Agent Commerce
website: https://circulodebelleza.com
---

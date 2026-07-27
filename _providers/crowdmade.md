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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Agent-driven commerce over the Universal Commerce Protocol (UCP) served by the crowdmade.com Shopify storefront, plus read-only catalog JSON endpoints and Shopify Customer Accounts OpenID Connect auth
  name: CrowdMade Agent Commerce (UCP)
  slug: crowdmade-agent-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://crowdmade.com
- group: docs
  title: ''
  type: Documentation
  url: https://crowdmade.com/agents.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crowdmade.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crowdmade.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crowdmade-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crowdmade-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crowdmade-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/crowdmade-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crowdmade-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crowdmade-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowdmade-domain-security.yml
created: '2026-07-17'
description: 'CrowdMade partners with online creators from YouTube, Instagram, Snapchat and beyond to design, produce, warehouse, and ship official merchandise their fans are proud to wear. The public storefront at crowdmade.com runs on Shopify and, as of 2026, exposes a machine- and agent-facing commerce surface: a published Universal Commerce Protocol (UCP) MCP shopping endpoint, Shopify Customer Accounts OpenID Connect / OAuth discovery documents, an llms.txt, and an agents.md describing how AI shopping agents can search the catalog, build a cart, and complete a buyer-approved checkout. It was surfaced as a portfolio company of 500 Global and profiled into the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crowdmade.png
layout: provider
mcp_servers:
- description: ''
  name: crowdmade-mcp.yml
  slug: crowdmade-mcpyml
modified: '2026-07-18'
name: CrowdMade
nav: Providers
network: true
overview: 'CrowdMade publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Merchandise, and Creator Economy.


  CrowdMade''s developer surface includes documentation, authentication, and 9 more developer resources.'
random_paper: 66
scopes:
- name: Crowdmade Scopes
  scope_count: 4
  slug: crowdmade-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Crowdmade Authentication
  slug: crowdmade-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Crowdmade Domain Security
  slug: crowdmade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowdmade
tags:
- Company
- Commerce
- E-Commerce
- Merchandise
- Creator Economy
- Shopify
- Agent Commerce
- MCP
- Universal Commerce Protocol
website: https://crowdmade.com
---

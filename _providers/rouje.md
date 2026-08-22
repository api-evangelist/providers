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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Agent-driven commerce surface for the Rouje storefront, implementing the Universal Commerce Protocol (UCP) over MCP: catalog search, cart, checkout, fulfillment, and order tools, with a buyer-approval'
  name: Rouje Agentic Commerce (UCP / MCP)
  slug: rouje-agentic-commerce-ucp-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://int.rouje.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rouje-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rouje-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rouje-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/rouje-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rouje-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.rouje.com/.well-known/openid-configuration
- group: design
  title: ''
  type: Conformance
  url: conformance/rouje-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rouje-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rouje-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rouje.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rouje.com/policies/terms-of-service
created: '2026-07-17'
description: 'Rouje is a Parisian ready-to-wear and beauty brand founded by Jeanne Damas, selling feminine ready-to-wear, shoes, accessories, and the "Les Filles en Rouje" makeup and skincare line direct-to-consumer online and through boutiques across France. Rouje has no first-party developer API, but its Shopify-hosted storefront exposes a native agent-commerce surface: a Universal Commerce Protocol (UCP) MCP endpoint for agent-driven shopping and checkout, a published llms.txt / agents.md with explicit agent instructions, Shopify Customer Account API OpenID Connect discovery, and public read-only product/collection JSON endpoints. Surfaced as a portfolio company of Partech.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rouje.png
layout: provider
mcp_servers:
- description: ''
  name: rouje-mcp.yml
  slug: rouje-mcpyml
modified: '2026-07-21'
name: Rouje
nav: Providers
network: true
overview: 'Rouje publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fashion, Beauty, and Retail.


  Rouje''s developer surface includes authentication and 11 more developer resources.'
random_paper: 3
scopes:
- name: Rouje Scopes
  scope_count: 4
  slug: rouje-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 16.4
  delta: -0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Rouje Authentication
  slug: rouje-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Rouje Domain Security
  slug: rouje-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rouje
tags:
- Company
- Consumer
- Fashion
- Beauty
- Retail
- Ecommerce
- Shopify
- Agentic Commerce
- Paris
website: https://int.rouje.com/
---

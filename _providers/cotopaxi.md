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
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cotopaxi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cotopaxi.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cotopaxi-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cotopaxi-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cotopaxi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cotopaxi-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cotopaxi-conformance.yml
- group: operate
  title: ''
  type: Support
  url: https://help.cotopaxi.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cotopaxi.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cotopaxi.com/policies/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://account.cotopaxi.com
created: '2026-07-17'
description: 'Cotopaxi is a Certified B Corporation outdoor gear and apparel brand (backpacks, jackets, and accessories) known for its "Do Good" mission and Gear for Good model. It sells direct-to-consumer on a Shopify storefront at cotopaxi.com. Cotopaxi publishes no first-party developer API, but its Shopify platform exposes real machine surfaces: OAuth2/OIDC customer authentication (Shopify Customer Accounts) at account.cotopaxi.com, a hosted Storefront MCP server at /api/mcp, and an authenticated Customer Account MCP API. Surfaced as a portfolio company of Forerunner Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cotopaxi.png
layout: provider
mcp_servers:
- description: ''
  name: Cotopaxi Storefront MCP
  slug: cotopaxi-storefront-mcp
modified: '2026-07-18'
name: Cotopaxi
nav: Providers
network: true
overview: 'Cotopaxi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Outdoor, Apparel, and Ecommerce.


  Cotopaxi''s developer surface includes authentication, support, signup flow, and 8 more developer resources.'
random_paper: 16
scopes:
- name: Cotopaxi Scopes
  scope_count: 4
  slug: cotopaxi-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 61.1
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cotopaxi/refs/heads/main/screenshots/cotopaxi-2026-07-25T210504.png
security:
- kind: authentication
  name: Cotopaxi Authentication
  slug: cotopaxi-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cotopaxi Domain Security
  slug: cotopaxi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cotopaxi
tags:
- Company
- Consumer
- Outdoor
- Apparel
- Ecommerce
- Retail
- Shopify
- MCP
website: https://www.cotopaxi.com
---

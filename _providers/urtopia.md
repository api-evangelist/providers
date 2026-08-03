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
api_count: 1
apis:
- description: 'Agent-driven commerce surface served natively on the Shopify-powered Urtopia storefront: UCP discovery at /.well-known/ucp, MCP tools for catalog search, product details, cart management, policies/FAQ'
  name: Urtopia Storefront Agent Commerce (UCP / MCP)
  slug: urtopia-storefront-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urtopia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://newurtopia.com/
- group: operate
  title: ''
  type: Support
  url: https://newurtopia.com/pages/contactus
- group: company
  title: ''
  type: Blog
  url: https://newurtopia.com/blogs/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newurtopia.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newurtopia.com/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/urtopia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urtopia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/urtopia-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urtopia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/urtopia-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/urtopia-conformance.yml
created: '2026-07-17'
description: 'Urtopia designs and sells smart carbon-fiber electric bikes, pairing lightweight frames and premium components with a connected riding experience through the companion Urtopia App. The company is backed by DCM Ventures and sells direct through its Shopify-powered storefront at newurtopia.com (with regional stores for Europe and Australia and a B2B dealer portal), where the store exposes an agent-ready commerce surface: a published llms.txt with agent instructions, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and live MCP endpoints for catalog search, cart, and buyer-approved checkout.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urtopia.png
layout: provider
mcp_servers:
- description: ''
  name: urtopia-mcp.yml
  slug: urtopia-mcpyml
modified: '2026-07-21'
name: Urtopia
nav: Providers
network: true
overview: 'Urtopia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Bikes, Electric Vehicles, and Cycling.


  Urtopia''s developer surface includes support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 12
scopes:
- name: Urtopia Scopes
  scope_count: 4
  slug: urtopia-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Urtopia Authentication
  slug: urtopia-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Urtopia Domain Security
  slug: urtopia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urtopia
tags:
- Company
- Consumer
- E-Bikes
- Electric Vehicles
- Cycling
- Smart Hardware
- Mobility
- eCommerce
website: https://newurtopia.com/
---

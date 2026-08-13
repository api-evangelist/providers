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
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://backbone.com/
- group: operate
  title: ''
  type: Support
  url: https://help.backbone.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backbone.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backbone.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/backbone-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/backbone-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/backbone-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/backbone-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backbone-domain-security.yml
created: '2026-07-17'
description: Backbone is a mobile gaming company that makes the Backbone One controller — a snap-on gamepad for iPhone and Android — and the Backbone app, a mobile gaming platform that unifies a player's game library across cloud gaming, console Remote Play, and streaming services with game discovery, capture, and social features. The company sells hardware and accessories through a Shopify-hosted storefront (backbone.com) that exposes an agent-commerce surface via the Universal Commerce Protocol (UCP) MCP endpoint and Shopify Customer Account OIDC. Backbone is a portfolio company of Index Ventures. This profile was enriched from Backbone's public web surface; the company publishes no first-party developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/backbone.png
layout: provider
mcp_servers:
- description: ''
  name: backbone-mcp.yml
  slug: backbone-mcpyml
modified: '2026-07-18'
name: Backbone
nav: Providers
network: true
overview: 'Backbone is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Gaming, Mobile Gaming, and Gaming Controller.


  Backbone''s developer surface includes support, authentication, and 7 more developer resources.'
random_paper: 101
score:
  band: emerging
  composite: 14.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.7
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backbone/refs/heads/main/screenshots/backbone-2026-08-07T162110.png
security:
- kind: authentication
  name: Backbone Authentication
  slug: backbone-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Backbone Domain Security
  slug: backbone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backbone
tags:
- Company
- Entertainment
- Gaming
- Mobile Gaming
- Gaming Controller
- Consumer Electronics
- Hardware
- Ecommerce
website: https://backbone.com/
---

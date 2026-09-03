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
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-03'
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
  name: Backbone MCP Server
  slug: backbone-mcp-server
modified: '2026-07-18'
name: Backbone
nav: Providers
network: true
overview: 'Backbone is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Gaming, Mobile Gaming, and Gaming Controller.


  Backbone''s developer surface includes support, authentication, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.3
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- E-Commerce
website: https://backbone.com/
---

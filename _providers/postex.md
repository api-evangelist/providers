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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 47.1
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Booking, tracking, and listing shipment orders
  name: PostEx Orders API
  slug: postex-orders-api
- description: Operational cities and merchant address reference data
  name: PostEx Reference API
  slug: postex-reference-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postex.pk
- group: agent
  title: ''
  type: MCPServer
  url: mcp/postex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/postex-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/postex-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postex-authentication.yml
created: '2026-07-17'
description: PostEx is a Pakistani e-commerce logistics, courier, and fintech platform that provides cash-on-delivery parcel fulfilment with instant upfront payments to online merchants, alongside a business suite for expense management, working- capital financing, and the XPay payment gateway. Merchants and order- management systems integrate with PostEx through its merchant Order Integration API (https://api.postex.pk) to book shipments, look up operational cities and pickup addresses, track parcels, and reconcile orders. This profile was enriched by API Evangelist by live-probing the production API host, which confirmed a real merchant integration surface authenticated with a token request header. PostEx is backed by 500 Global.
image: https://postex.pk/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: postex-mcp.yml
  slug: postex-mcpyml
modified: '2026-07-20'
name: PostEx
nav: Providers
network: true
overview: 'PostEx publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Reference API. Tagged areas include Company, Logistics, Courier, Shipping, and E-commerce.


  PostEx''s developer surface includes authentication and 6 more developer resources.'
random_paper: 63
score:
  band: emerging
  composite: 29.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 61.9
    developer_ergonomics: 26.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Postex Authentication
  slug: postex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Postex Domain Security
  slug: postex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postex
tags:
- Company
- Logistics
- Courier
- Shipping
- E-commerce
- Fulfillment
- Cash on Delivery
- Payments
- Fintech
- Pakistan
website: https://postex.pk
---

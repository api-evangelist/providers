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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 26.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Public REST API for eCommerce shipping and order management — courier rate calculation and serviceability, order create/update/cancel, AWB and label generation, pickup scheduling, shipment tracking, r
  name: Shiprocket API
  slug: shiprocket-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://shiprocket.in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shiprocket.in/developers
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.shiprocket.in/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.shiprocket.in/
- group: company
  title: ''
  type: Blog
  url: https://shiprocket.in/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://shiprocket.in/pricing
- group: start
  title: ''
  type: SignUp
  url: https://shiprocket.in/login
- group: operate
  title: ''
  type: Support
  url: https://shiprocket.in/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shiprocket.in/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shiprocket.in/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shiprocket.in/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bfrs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kartrocket-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kartrocket-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/kartrocket-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kartrocket-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kartrocket-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kartrocket-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kartrocket-packages.yml
- group: design
  title: ''
  type: Components
  url: components/kartrocket-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kartrocket-domain-security.yml
created: '2026-07-17'
description: KartRocket is the original brand of what is now Shiprocket, India's leading eCommerce enablement and shipping-logistics platform (operated by BigFoot Retail Solutions Pvt Ltd). Shiprocket helps D2C brands, SMEs, and enterprise sellers manage eCommerce shipping, last-mile delivery, reverse logistics, freight, hyperlocal delivery, cross-border shipping, warehouse fulfillment, and seller analytics from one platform — delivering to 19,000+ pin codes in India and 220+ countries. The public Shiprocket API (apiv2.shiprocket.in/v1/external) lets sellers rate-shop couriers, create and cancel orders, generate AWBs and labels, schedule pickups, and track shipments; an official MCP server and agentic UI component library extend it to AI agents. Backed by 500 Global.
image: https://sr-website.shiprocket.in/wp-content/uploads/2025/02/OG-Image-for-Shiprocket.png
layout: provider
mcp_servers:
- description: ''
  name: kartrocket-mcp.yml
  slug: kartrocket-mcpyml
modified: '2026-07-19'
name: KartRocket
nav: Providers
network: true
overview: 'KartRocket publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, eCommerce, and Fulfillment.


  KartRocket''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, support, authentication, and 15 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 32.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Kartrocket Authentication
  slug: kartrocket-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kartrocket Domain Security
  slug: kartrocket-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kartrocket
tags:
- Company
- Shipping
- Logistics
- eCommerce
- Fulfillment
- Last-Mile Delivery
- India
- Order Management
website: https://shiprocket.in
---

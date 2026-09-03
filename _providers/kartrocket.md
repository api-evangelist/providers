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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.9
  scored_at: '2026-09-03'
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
  name: Shiprocket
  slug: shiprocket
modified: '2026-07-19'
name: KartRocket
nav: Providers
network: true
overview: 'KartRocket publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, E-Commerce, and Fulfillment.


  KartRocket''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, support, authentication, and 15 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 26.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kartrocket/refs/heads/main/screenshots/kartrocket-2026-07-25T223516.png
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
- E-Commerce
- Fulfillment
- Last Mile Delivery
- India
- Order Management
website: https://shiprocket.in
---

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
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 28.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'Server-side order-management endpoints for the Tiptop Direct integration: request capture, void (full or partial), and refund (full or partial) of orders created through the tiptop.js checkout, addres'
  name: Tiptop Direct Order Management API
  slug: tiptop-direct-order-management-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiptop-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tiptop.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tiptop.com/direct/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tiptop.com/direct/order-management-apis/capture/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiptopxyz
- group: company
  title: ''
  type: Blog
  url: https://blog.tiptop.xyz/
- group: build
  title: ''
  type: Packages
  url: packages/tiptop-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tiptop-packages.yml
- group: design
  title: ''
  type: Components
  url: components/tiptop-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiptop-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tiptop-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tiptop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tiptop-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tiptop-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tiptop-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tiptop-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tiptop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tiptop-llms.txt
created: '2026-07-17'
description: 'Tiptop (Tiptop Labs) is the payments company founded by Postmates co-founder Bastian Lehmann that lets shoppers trade in items they already own for instant credit at checkout, alongside pay-over-time options. Merchants integrate through a Shopify payments app, a Salesforce Commerce Cloud cartridge, a Magento 2 module, or the Direct API — the tiptop.js browser library plus server-side order-management endpoints (capture, void, refund) authenticated with an api-key header. Backed by a16z ($23M Series A, 2022). Note: as of July 2026 tiptop.com redirects to mother.ai (Mother Computer Inc.) and its TLS certificate has expired, while docs.tiptop.com, api.tiptop.com, cdn.tiptop.com, and the first-party packages remain live.'
image: https://raw.githubusercontent.com/tiptopxyz/magento/master/view/adminhtml/web/images/tiptop-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: tiptop-mcp.yml
  slug: tiptop-mcpyml
modified: '2026-07-21'
name: Tiptop
nav: Providers
network: true
overview: 'Tiptop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, FinTech, Trade-In, and Checkout.


  Tiptop''s developer surface includes documentation, getting-started guide, API reference, engineering blog, authentication, sandbox, and 12 more developer resources.'
random_paper: 60
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Tiptop Authentication
  slug: tiptop-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Tiptop Domain Security
  slug: tiptop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiptop
tags:
- Company
- Payments
- FinTech
- Trade-In
- Checkout
- Commerce
- Pay Over Time
---

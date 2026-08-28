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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-26'
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
- description: No official Tiptop MCP server was found (none in the docs, the tiptopxyz GitHub org, npm, or the MCP registries). This is a candidate tool list derived from the three documented Direct Order Managemen
  name: Tiptop MCP Server
  slug: tiptop-mcp-server
modified: '2026-07-21'
name: Tiptop
nav: Providers
network: true
overview: 'Tiptop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Trade-In, and Checkout.


  Tiptop''s developer surface includes documentation, getting-started guide, API reference, engineering blog, authentication, sandbox, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 18.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- Fintech
- Trade-In
- Checkout
- Commerce
- Pay Over Time
---

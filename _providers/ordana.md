---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 3.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ordana-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ordana-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ordana-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://ordana.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://ordana.ai/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://ordana.ai/api-docs
- group: company
  title: ''
  type: Blog
  url: https://ordana.ai/news
- group: company
  title: ''
  type: About
  url: https://ordana.ai/about
- group: operate
  title: ''
  type: Support
  url: https://ordana.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://ordana.ai/contact
created: '2026-07-17'
description: 'Ordana provides AI agents that run wholesale order-desk operations for distributors, reading every order across email, fax, PDF, EDI, voice, SMS and chat, resolving exceptions, communicating with retailers, and closing orders directly into the customer''s ERP. Four agents cover the surface: Desk (end-to-end order automation), Voice (inbound/outbound phone ordering), Predict (cart prediction and AOV optimization), and Chat (text/SMS ordering). Ordana sits as an intelligence layer on top of existing ERP and commerce systems via pre-built connectors, and exposes its capabilities through a gated REST API, Webhooks, an MCP (Model Context Protocol) server over HTTP/SSE with OAuth 2.0, and the A2A agent-to-agent protocol. Surfaced as a Techstars portfolio company and enriched into the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ordana.png
layout: provider
mcp_servers:
- description: ''
  name: Ordana MCP Server
  slug: ordana-mcp-server
modified: '2026-07-20'
name: Ordana
nav: Providers
network: true
overview: 'Ordana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Order Management, and Wholesale Distribution.


  Ordana''s developer surface includes documentation, API reference, engineering blog, support, signup flow, and 5 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ordana/refs/heads/main/screenshots/ordana-2026-08-07T190902.png
security:
- kind: domain-security
  name: Ordana Domain Security
  slug: ordana-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ordana
tags:
- Company
- Artificial Intelligence
- AI Agents
- Order Management
- Wholesale Distribution
- ERP Integration
- Automation
- MCP
website: https://ordana.ai/
---

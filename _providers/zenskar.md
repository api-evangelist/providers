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
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Zenskar's REST API for billing, contracts, usage metering, invoicing, payments, credit notes, and accounting/revenue recognition (166+ documented operations).
  name: Zenskar API
  slug: zenskar-api
artifact_total: 5
asyncapis:
- description: ''
  name: Zenskar Webhooks
  slug: zenskar-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://zenskar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenskar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenskar.com/docs/introduction-to-zenskar
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenskar.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zenskar.com/docs/quickstart-guide
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenskar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zenskar-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zenskar-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zenskar-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zenskar-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zenskar-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zenskar-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenskar-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenskar-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.zenskar.com/
- group: company
  title: ''
  type: Blog
  url: https://zenskar.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zenskar.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.zenskar.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zenskar.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenskar.com/privacy
created: '2026-07-17'
description: Zenskar is an AI-native revenue automation and usage-based billing platform for SaaS and subscription businesses. Its order-to-cash suite covers contracts, flexible pricing models, usage metering, invoicing, payments, collections, credit notes, and revenue recognition/accounting, exposed through a REST API (api.zenskar.com), an official hosted Model Context Protocol (MCP) server with 103 tools, webhook alerts, and 100+ data, ERP, and CRM integrations including Stripe, Salesforce, NetSuite, QuickBooks, BigQuery, and Snowflake. It is built to replace finance spreadsheets and manual billing workarounds for finance teams.
image: https://zenskar.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Zenskar MCP Server
  slug: zenskar-mcp-server
modified: '2026-07-21'
name: Zenskar
nav: Providers
network: true
overview: 'Zenskar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Billing, Usage-Based Billing, and Revenue Automation.


  The Zenskar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zenskar''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 34.4
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenskar/refs/heads/main/screenshots/zenskar-2026-08-17T083046.png
security:
- kind: authentication
  name: Zenskar Authentication
  slug: zenskar-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Zenskar Domain Security
  slug: zenskar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenskar
tags:
- Company
- Cloud
- Billing
- Usage-Based Billing
- Revenue Automation
- Subscription Management
- Revenue Recognition
- Invoicing
- Fintech
- Order-to-Cash
- MCP
website: https://zenskar.com/
---

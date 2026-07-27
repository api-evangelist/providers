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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 35.6
  scored_at: '2026-07-27'
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
  name: zenskar-mcp.yml
  slug: zenskar-mcpyml
modified: '2026-07-21'
name: Zenskar
nav: Providers
network: true
overview: 'Zenskar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Billing, Usage-Based Billing, and Revenue Automation.


  The Zenskar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zenskar''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 22.6
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 37.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
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
- FinTech
- Order-to-Cash
- MCP
website: https://zenskar.com/
---

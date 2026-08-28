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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: gigstack API v2 — REST API for CFDI 4.0 invoicing, payments, collections, clients, services, receipts, retentions, webhooks and SAT catalogs in Mexico. Bearer JWT authentication; cursor pagination; st
  name: Gigstack API
  slug: gigstack-api
artifact_total: 5
asyncapis:
- description: ''
  name: Gigstack Webhooks
  slug: gigstack-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gigstack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gigstack.pro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.gigstack.pro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gigstack.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gigstack.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gigstack.io/welcome-to-gigstack-api-1385870m0
- group: company
  title: ''
  type: Blog
  url: https://blog.gigstack.pro/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.gigstack.pro/
- group: operate
  title: ''
  type: Support
  url: mailto:hola@gigstack.pro
- group: start
  title: ''
  type: SignUp
  url: https://app.gigstack.pro/register
- group: start
  title: ''
  type: Login
  url: https://app.gigstack.pro/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pro-gigstack.s3.us-east-2.amazonaws.com/legal/terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pro-gigstack.s3.us-east-2.amazonaws.com/legal/privacy.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/disruptive-learning
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gigstack-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/gigstack-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gigstack-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gigstack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gigstack-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gigstack-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gigstack-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/gigstack-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/gigstack-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gigstack-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/gigstack-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gigstack-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gigstack-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/gigstack-components.yml
created: '2026-07-17'
description: Gigstack (gigstack.pro) is a Mexican fintech and revenue-automation platform that automates electronic invoicing and tax compliance for businesses operating in Mexico. It generates CFDI 4.0 fiscal invoices through the SAT/PAC stamping pipeline, runs collections (cobranza) and accounts-receivable workflows, offers self-invoicing (autofactura) and customer portals, and performs automated SAT reconciliation and bulk SAT downloads (descarga masiva). Its REST API (v2, https://api.gigstack.io/v2) exposes clients, services, invoices (income/egress/draft/payment-complement), payments, receipts, retentions, teams, users, webhooks and SAT catalogs, with an official CLI and MCP server for terminal and agent workflows. Backed by 500 Global.
image: https://gigstack.pro/images/webclip.png
layout: provider
mcp_servers:
- description: Official gigstack MCP server exposing the gigstack API (Mexican invoice and payment automation - CFDI, payments, clients, receipts) to MCP-capable agents. Published to npm by a gigstack.io maintainer.
  name: Official gigstack MCP server
  slug: official-gigstack-mcp-server
modified: '2026-07-19'
name: Gigstack
nav: Providers
network: true
overview: 'Gigstack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Invoicing, CFDI, and SAT.


  The Gigstack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gigstack''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 21 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 40.1
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 40.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gigstack/refs/heads/main/screenshots/gigstack-2026-07-25T215817.png
security:
- kind: authentication
  name: Gigstack Authentication
  slug: gigstack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gigstack Domain Security
  slug: gigstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gigstack
tags:
- Company
- Fintech
- Invoicing
- CFDI
- SAT
- Tax Compliance
- Payments
- Billing
- Collection
- Mexico
- Accounts Receivable
website: https://gigstack.pro
---

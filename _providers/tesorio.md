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
  score: 11.2
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tesorio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tesorio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.tesorio.com/
- group: operate
  title: ''
  type: Support
  url: https://help.tesorio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tesorio.com/blog
- group: start
  title: ''
  type: Login
  url: https://dashboard.tesorio.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tesorio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tesorio.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tesorio
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tesorio-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tesorio-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tesorio-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.tesorio.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tesorio-llms.txt
created: '2026-07-17'
description: Tesorio is an AI-powered financial operations platform that automates accounts receivable, accelerates cash flow, and gives finance teams intelligent tools to manage collections, forecasting, and payment workflows. It connects to ERP, CRM, and payment systems (NetSuite, Sage Intacct, Workday, Zuora, Salesforce, Stripe and more), matches incoming payments to open invoices, drafts AI follow-up emails, extracts payment promises, and predicts pay dates so treasury, AR, and FP&A teams can reduce days sales outstanding. Tesorio exposes a hosted Model Context Protocol (MCP) server so AI tools like Claude, ChatGPT, and Cursor can query live Tesorio data. Founded via Y Combinator.
image: https://www.tesorio.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Tesorio MCP Server
  slug: tesorio-mcp-server
modified: '2026-07-21'
name: Tesorio
nav: Providers
network: true
overview: 'Tesorio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Operations, Accounts Receivable, Cash Flow, and Collection.


  Tesorio''s developer surface includes documentation, support, engineering blog, authentication, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 20.5
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tesorio/refs/heads/main/screenshots/tesorio-2026-09-02T163211.png
security:
- kind: authentication
  name: Tesorio Authentication
  slug: tesorio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tesorio Domain Security
  slug: tesorio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tesorio Trust Center
  slug: tesorio-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2
slug: tesorio
tags:
- Company
- Financial Operations
- Accounts Receivable
- Cash Flow
- Collection
- Treasury
- Fintech
- MCP
website: https://www.tesorio.com/
---

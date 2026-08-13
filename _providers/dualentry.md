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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for programmatic access to an organization's accounting data across setup (accounts, items, classifications), master data (companies, customers, vendors), transactions (invoices, bills, journ
  name: DualEntry Public API
  slug: dualentry-public-api
artifact_total: 6
asyncapis:
- description: ''
  name: Dualentry Webhooks
  slug: dualentry-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.dualentry.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dualentry.com/developers/guides/index
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dualentry.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dualentry.com/developers/api/resources-v2/invoices/list-invoicev2-records
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dualentry.com/developers/guides/quickstart-first-api-call
- group: company
  title: ''
  type: Blog
  url: https://www.dualentry.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dualentry.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.dualentry.com/
- group: start
  title: ''
  type: Login
  url: https://app.dualentry.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dualentry.com/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dualentry.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dualentry
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dualentry.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dualentry-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/dualentry-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/dualentry-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dualentry-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dualentry-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dualentry-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dualentry-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dualentry-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dualentry-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dualentry-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dualentry-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dualentry-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dualentry-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dualentry-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dualentry-llms.txt
created: '2026-07-17'
description: DualEntry is an AI-native ERP (enterprise resource planning) platform for finance and accounting teams, positioned as a modern replacement for NetSuite, QuickBooks, and Xero. It covers core financials (general ledger, accounts payable and receivable, cash management, bank and account reconciliation, tax, and month-end close), advanced accounting (ASC 606 revenue recognition, subscription billing, prepaid amortization, fixed-asset and multi-book depreciation), and enterprise scale (multi-entity consolidation, multi-currency, intercompany journal entries, budgeting, and reporting), layered with AI automation for categorization, anomaly detection, OCR document capture, and continuous close. Developers integrate through the DualEntry Public API (V1 and V2 REST), a hosted MCP server for AI assistants, a first-party Python CLI, and signed webhooks. The company raised a $90M Series A and is backed by GV, Khosla Ventures, and Lightspeed Venture Partners.
image: https://cdn.prod.website-files.com/66bf861737ab5a556a15c52b/671944f8d88d82c212724765_DualEntry.png
layout: provider
mcp_servers:
- description: ''
  name: dualentry-mcp.yml
  slug: dualentry-mcpyml
modified: '2026-07-18'
name: DualEntry
nav: Providers
network: true
overview: 'DualEntry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Accounting, ERP, and Finance.


  The DualEntry catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DualEntry''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 21 more developer resources.'
random_paper: 24
rate_limits:
- limit_count: 3
  name: Dualentry Rate Limits
  slug: dualentry-rate-limits
score:
  band: developing
  composite: 53.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 69.6
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 60.5
  previous_composite: 53.2
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dualentry/refs/heads/main/screenshots/dualentry-2026-07-25T212448.png
security:
- kind: authentication
  name: Dualentry Authentication
  slug: dualentry-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Dualentry Domain Security
  slug: dualentry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dualentry
tags:
- Company
- AI
- Accounting
- ERP
- Finance
- Financial Operations
- Bookkeeping
- Revenue Recognition
- Fintech
website: https://www.dualentry.com
---

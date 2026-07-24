---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Digits Com Agentic Access
  operation_count: 24
  slug: digits-com-agentic-access
  summary_line: 24 operations · 8 acting
api_count: 10
apis:
- description: Receive event notifications from Digits at a configured webhook endpoint; Digits POSTs a JSON event body and expects a 2xx acknowledgment (WebhookService.receiveWebhookEvent).
  name: Digits Webhooks API
  slug: digits-com-webhooks-api
- description: Model Context Protocol server that lets AI clients like ChatGPT and Claude connect directly to Digits to query the ledger in natural language. Discovery is published as an MCP Server Card at /.well-kn
  name: Digits MCP Server
  slug: digits-com-mcp-server
- description: Ledger categories and dimensional axes (departments, locations, projects).
  name: Digits Chart of Accounts API
  slug: digits-com-chart-of-accounts-api
- description: Connected data sources feeding the ledger.
  name: Digits Connections API
  slug: digits-com-connections-api
- description: Balance Sheet, P&L, Cash Flow, Trial Balance, aging reports, and summaries.
  name: Digits Financial Statements API
  slug: digits-com-financial-statements-api
- description: Accounting-firm organizations, clients, entities, and employees.
  name: Digits Organizations API
  slug: digits-com-organizations-api
- description: Vendors, suppliers, customers, and other business relationships.
  name: Digits Parties API
  slug: digits-com-parties-api
- description: Push raw source data into the AGL for enrichment and categorization.
  name: Digits Sources API
  slug: digits-com-sources-api
- description: Read AI-categorized ledger transactions and journal entries.
  name: Digits Transactions API
  slug: digits-com-transactions-api
- description: Event delivery to partner-configured endpoints.
  name: Digits Webhooks API
  slug: digits-com-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: Digits Connect API
  slug: open-digits-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/digits-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/digits-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/digits-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digits-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digits-com-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/digits-com-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digits
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digits-financial
- group: company
  title: ''
  type: Website
  url: https://digits.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.digits.com
- group: commercial
  title: ''
  type: Plans
  url: plans/digits-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/digits-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/digits-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://digits.com/blog/rss.xml
created: '2026-07-01'
description: Digits is an AI-native accounting and bookkeeping platform for startups and their accountants, built around the Autonomous General Ledger (AGL) that auto-books the majority of transactions in real time. The Digits Connect API opens the AGL programmatically over REST with OAuth 2.0, letting partners send raw transaction, party, and dimension data for AI categorization and vendor enrichment, and read back ledger entries and financial statements. Digits also publishes an MCP server for AI agents (ChatGPT, Claude) to query the ledger.
finops:
- name: Digits Com Finops
  service_category: Business Applications
  slug: digits-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digits-com.png
layout: provider
modified: '2026-07-01'
name: Digits
nav: Providers
network: true
overview: 'Digits publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Chart of Accounts API, Connections API, and 6 more. Tagged areas include Accounting, Bookkeeping, Finance, General Ledger, and AI.


  Digits'' developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Digits Com Plans Pricing
  plan_count: 2
  slug: digits-com-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 2
  name: Digits Com Rate Limits
  slug: digits-com-rate-limits
scopes:
- name: Digits Com Scopes
  scope_count: 2
  slug: digits-com-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 52.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Digits Com Authentication
  slug: digits-com-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Digits Com Domain Security
  slug: digits-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Digits Com Vulnerability Disclosure
  slug: digits-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Digits Com Trust Center
  slug: digits-com-trust-center
  summary_line: SOC 2
slug: digits-com
tags:
- Accounting
- Bookkeeping
- Finance
- General Ledger
- AI
- FinTech
website: https://digits.com
---

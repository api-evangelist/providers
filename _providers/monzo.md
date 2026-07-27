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
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The Monzo API is a REST interface over a user's Monzo account. It exposes accounts, balance, savings pots (with deposit/withdraw), transactions (list, retrieve, annotate with metadata, expand merchant
  name: Monzo API
  slug: monzo-api
artifact_total: 6
asyncapis:
- description: ''
  name: Monzo Webhooks
  slug: monzo-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/monzo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://monzo.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monzo-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/monzo-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monzo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monzo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monzo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/monzo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monzo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monzo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monzo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/monzo-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/monzo-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/monzo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monzo-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/monzo-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://monzo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.monzo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monzo.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.monzo.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.monzo.com/api/playground
- group: company
  title: ''
  type: Blog
  url: https://monzo.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://community.monzo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monzo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.monzo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monzo.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monzo.com/legal/privacy-policy/
created: '2026-07-17'
description: 'Monzo is a UK-based digital challenger bank (Monzo Bank Ltd, FCA-authorised) offering current accounts, savings pots, joint accounts, business banking and lending through a mobile-first app. For developers, Monzo publishes a public REST API at api.monzo.com that lets a user build personal applications against their own Monzo account: listing accounts, reading balances, managing savings pots, retrieving and annotating transactions, uploading receipts and attachments, posting custom feed items into the app, and registering webhooks for real-time transaction notifications. Access uses OAuth 2.0 with Strong Customer Authentication (SCA) approved via push notification in the Monzo app. The API is intended for personal use and small groups of authorised users rather than large public applications.'
image: https://monzo.com/static/images/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Monzo MCP (candidate)
  slug: monzo-mcp-candidate
modified: '2026-07-20'
name: Monzo
nav: Providers
network: true
overview: 'Monzo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, Financial Services, and Payments.


  The Monzo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Monzo''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, engineering blog, support, and 21 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 43.3
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Monzo Authentication
  slug: monzo-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Monzo Domain Security
  slug: monzo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Monzo Vulnerability Disclosure
  slug: monzo-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: monzo
tags:
- Company
- Banking
- Fintech
- Financial Services
- Payments
- Open Banking
- Accounts
- Transactions
- OAuth
website: https://monzo.com
---

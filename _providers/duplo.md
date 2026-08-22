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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Atlas is Duplo''s global payments API for African and emerging-market businesses: collect payments (checkout, payment links, virtual accounts), disburse funds (single and bulk bank payouts, internation'
  name: Atlas Payments API
  slug: atlas-payments-api
artifact_total: 5
asyncapis:
- description: ''
  name: Duplo Atlas Webhooks
  slug: duplo-atlas-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duplo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryduplo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryduplo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryduplo.com/en/atlas
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryduplo.com/en/atlas/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryduplo.com/en/atlas/guides
- group: company
  title: ''
  type: Blog
  url: https://tryduplo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://duplo.zohodesk.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryduplo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://tryduplo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.tryduplo.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.tryduplo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryduplo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryduplo.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tryduplo
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tryduplo.com/en/atlas/changelogs
- group: auth
  title: ''
  type: Compliance
  url: conformance/duplo-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duplo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/duplo-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/duplo-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/duplo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/duplo-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/duplo-atlas-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/duplo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/duplo-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/duplo-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/duplo-llms.txt
created: '2026-07-17'
description: 'Duplo is a fintech company building the financial operating system for African and emerging-market businesses, headquartered in Lagos, Nigeria with operations in South Africa. Its platform unifies B2B payments and spend management: automated expense tracking with approval workflows, local and international (cross-border) payments, multi-currency global business accounts, NRS-compliant e-invoicing, direct debit, tax management, auto reconciliation, bulk payments to up to 500 recipients, and real-time financial reporting. For developers, Duplo exposes Atlas, a global payments API (base host atlas.tryduplo.com) covering collections/checkout, disbursements and bulk payouts, virtual accounts, payment links, exchange rates and FX swaps, wallet management, and e-invoicing, authenticated with Bearer API keys and delivering event notifications via webhooks. Duplo maintains PCI DSS, ISO 27001 and ISO 22301 certifications, is NDPR compliant, and operates under Central Bank of Nigeria
  oversight as a licensed Payment Service Solution Provider (PSSP).'
image: https://tryduplo.com/wp-content/uploads/2026/04/Dashboard-1-01-scaled.webp
layout: provider
mcp_servers:
- description: ''
  name: duplo-mcp.yml
  slug: duplo-mcpyml
modified: '2026-07-18'
name: Duplo
nav: Providers
network: true
overview: 'Duplo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Payments, B2B Payments, and Cross-Border Payments.


  The Duplo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Duplo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 2
score:
  band: strong
  composite: 54.3
  delta: 4.1
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 50.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duplo/refs/heads/main/screenshots/duplo-2026-07-25T212511.png
security:
- kind: authentication
  name: Duplo Authentication
  slug: duplo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duplo Domain Security
  slug: duplo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: duplo
tags:
- Company
- FinTech
- Payments
- B2B Payments
- Cross-Border Payments
- Expense Management
- Virtual Accounts
- E-Invoicing
- Foreign Exchange
- Africa
- Nigeria
website: https://tryduplo.com
---

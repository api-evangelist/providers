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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Real-time consumer credit underwriting / risk-assessment API. Partners POST an underwriting request for a credit-card applicant and receive a Guard Score, risk band and credit-limit decision. The call
  name: GUARD API
  slug: guard-api
- description: Credit-card module integration API (private, partner B2B) for issuing and managing alt.bank white-label credit cards.
  name: CC Integration API
  slug: cc-integration-api
- description: Identity verification / KYC SDK and API for onboarding and verifying applicants as part of the alt.bank credit and card flows.
  name: SDK KYC API
  slug: sdk-kyc-api
artifact_total: 7
asyncapis:
- description: ''
  name: Alt Bank Guard Webhooks
  slug: alt-bank-guard-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alt-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altbank.ai/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.altbank.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.altbank.ai/docs/guard-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.altbank.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.altbank.ai/docs/guard
- group: operate
  title: ''
  type: Support
  url: https://altbank.ai/en/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alt-bank
- group: auth
  title: ''
  type: Authentication
  url: authentication/alt-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alt-bank-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alt-bank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/alt-bank-guard-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alt-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alt-bank-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alt-bank-well-known.yml
created: '2026-07-17'
description: alt.bank (Alt Bank) is a Brazilian fintech providing a fully integrated, turnkey credit-card and consumer-credit platform for partners who want to launch prepaid and postpaid cards without becoming a financial institution. Its flagship product, GUARD, is a machine-learning underwriting / credit-risk engine ("Brazil's most accurate credit model") that returns a Guard Score, risk band and credit-limit decision through a real-time partner API. The platform also bundles white-label credit cards (novücard), Visa BIN sponsorship, KYC, anti-fraud, dispute management and Pix/boleto payment processing. Partners integrate over a documented HTTPS API secured with a per-partner X-Partner-Auth token plus IP allow-listing, with a mirrored staging sandbox and asynchronous callback delivery of underwriting results. Backed by Anthemis, Union Square Ventures, Repeat Ventures and SquareOne Capital, alt.bank targets financial inclusion for underbanked consumers.
image: https://altbank.ai/wp-content/uploads/2020/08/cropped-alt.bank-logo-square-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: alt-bank-mcp.yml
  slug: alt-bank-mcpyml
modified: '2026-07-17'
name: Alt Bank
nav: Providers
network: true
overview: 'Alt Bank publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Credit, and Underwriting.


  The Alt Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Alt Bank''s developer surface includes documentation, getting-started guide, API reference, support, authentication, sandbox, and 9 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 31.6
  delta: 3.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 83.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alt-bank/refs/heads/main/screenshots/alt-bank-2026-07-25T195808.png
security:
- kind: authentication
  name: Alt Bank Authentication
  slug: alt-bank-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alt Bank Domain Security
  slug: alt-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alt-bank
tags:
- Company
- Fintech
- Banking
- Credit
- Underwriting
- Credit Cards
- Payments
- KYC
- Risk
- Brazil
- Financial Inclusion
- Banking as a Service
website: https://altbank.ai/en/
---

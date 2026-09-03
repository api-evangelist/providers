---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://banked.com/'', ''status'': 301, ''note'': ''declared website redirects to https://paybyb.com/ — a different registrable domain (banked.com -> paybyb.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Account-to-account payments over open banking — create payment sessions (checkout), payouts, refunds, and webhooks. The Partner API onboards businesses on behalf of platforms. OAuth 2.0 client-credent
  name: Banked Payments API
  slug: banked-payments-api
artifact_total: 6
asyncapis:
- description: ''
  name: Banked Webhooks
  slug: banked-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/banked-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/banked-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/banked-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://banked.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.banked.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.banked.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.banked.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.banked.com/docs
- group: operate
  title: ''
  type: Support
  url: https://support.paybybank.com
- group: start
  title: ''
  type: Login
  url: https://console.banked.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@banked
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://banked.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/banked
- group: build
  title: ''
  type: Postman
  url: https://github.com/banked/postman-collections-public
- group: operate
  title: ''
  type: StatusPage
  url: https://status.banked.com/
- group: build
  title: ''
  type: Packages
  url: packages/banked-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/banked-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/banked-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/banked-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/banked-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/banked-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/banked-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/banked-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/banked-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/banked-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/banked-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/banked-webhooks.yml
created: '2026-07-17'
description: Banked is a global account-to-account (A2A) payments network built on open banking that enables real-time pay-by-bank payments for consumers, businesses, and banks. Its API-first platform provides hosted Checkout, Payment Links and QR codes, Payouts, Refunds, Reporting, loyalty (Incentivize), and fraud protection, using bank-native biometric authentication and Strong Customer Authentication (SCA) to move money securely with minimal chargebacks. A single Payments API and Partner API integration gives merchants and platforms access across multiple markets, and Banked ships an official hosted MCP server so agents can create, search, and refund payments over OAuth 2.0.
image: https://images.prismic.io/banked/dc1e104e-b397-4f26-ba16-0b64aee7daea_page-og-2.png?auto=compress,format&w=1200&h=627
layout: provider
mcp_servers:
- description: ''
  name: Banked MCP Server
  slug: banked-mcp-server
modified: '2026-07-18'
name: Banked
nav: Providers
network: true
overview: 'Banked publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Open Banking, Account-to-Account, and Pay by Bank.


  The Banked catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Banked''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 38.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 34.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/banked/refs/heads/main/screenshots/banked-2026-07-25T202342.png
security:
- kind: authentication
  name: Banked Authentication
  slug: banked-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Banked Domain Security
  slug: banked-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Banked Vulnerability Disclosure
  slug: banked-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: banked
tags:
- Company
- Payments
- Open Banking
- Account-to-Account
- Pay by Bank
- Fintech
- Payment Processing
- Payouts
website: https://banked.com/
---

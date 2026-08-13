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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-08-12'
api_count: 16
apis:
- description: The 3D Secure API from TabaPay — 3 operation(s) for 3d secure.
  name: TabaPay 3D Secure API
  slug: tabapay-3d-secure-api
- description: This resource represents a Client's Account.
  name: TabaPay Account API
  slug: tabapay-account-api
- description: This resource represents a Bank.
  name: TabaPay Bank API
  slug: tabapay-bank-api
- description: This resource represents a Payment Card (Debit Card, PrePaid Card, or Credit Card).
  name: TabaPay Card API
  slug: tabapay-card-api
- description: This resource represents a Client.
  name: TabaPay Client API
  slug: tabapay-client-api
- description: This resource represents an FX Rate.
  name: TabaPay FXRate API
  slug: tabapay-fxrate-api
- description: The Health API from TabaPay — 2 operation(s) for health.
  name: TabaPay Health API
  slug: tabapay-health-api
- description: This resource represents an RSA Encryption Key.
  name: TabaPay Key API
  slug: tabapay-key-api
- description: This resource represents a Client's Ledger.
  name: TabaPay Ledger API
  slug: tabapay-ledger-api
- description: This resource represents a Name on the OFAC Sanctions List.
  name: TabaPay OFAC API
  slug: tabapay-ofac-api
- description: This resource represents a Client's SubClient.
  name: TabaPay SubClient API
  slug: tabapay-subclient-api
- description: The Tag API from TabaPay — 1 operation(s) for tag.
  name: TabaPay Tag API
  slug: tabapay-tag-api
- description: This resource represents a Client's Transaction.
  name: TabaPay Transaction API
  slug: tabapay-transaction-api
- description: This resource represents a TransactionRequest One-time Payment Portal (<<glossary:OTPP>>)
  name: TabaPay TransactionRequest API
  slug: tabapay-transactionrequest-api
- description: This resource represents a Client's User.
  name: TabaPay User API
  slug: tabapay-user-api
- description: This resource represents a Client's Verification.
  name: TabaPay Verification API
  slug: tabapay-verification-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tabapay-3ds-transaction.md
- group: other
  title: ''
  type: Overlay
  url: overlays/tabapay-openapi-overlay.yaml
- group: build
  title: ''
  type: SDKs
  url: https://developers.tabapay.com/reference/client
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tabapay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tabapay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tabapay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tabapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tabapay.com/docs/learn-more
- group: docs
  title: ''
  type: APIReference
  url: https://developers.tabapay.com/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tabapay.com/docs/starter-guide
- group: operate
  title: ''
  type: Support
  url: https://tabapay.zendesk.com/hc/en-us/requests/new
- group: company
  title: ''
  type: Blog
  url: https://tabapay.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tabapay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tabapay.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tabapay.com/privacy
- group: start
  title: ''
  type: Login
  url: https://clientcentral.tabapay.net/dashboard/authentication/
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/tabapaydevs/workspace/tabapay-developers
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tabapay-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tabapay-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tabapay-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tabapay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tabapay-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tabapay-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tabapay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://developers.tabapay.com/reference/pcisoc
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tabapay-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/tabapay-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tabapay-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tabapay-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tabapay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tabapay-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tabapay-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/tabapay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tabapay-data-model.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
created: '2026-07-17'
description: 'TabaPay is an instant money movement platform for fintechs, banks, and payment companies. One Unified API accepts payments (pull) and sends payouts (push) across debit and credit card networks (Visa, Mastercard, Discover, American Express, Accel, STAR), RTP by The Clearing House, and ACH, with cross-border push-to-card, 3D Secure, account verification (AVS, ANI, OFAC), tokenized card storage, KYB/KYC verifications, ledgers, and real-time transaction monitoring. TabaPay is a PCI DSS Level 1 service provider, SOC 1 and SOC 2 Type II certified, and backed by SoftBank Vision Fund. APIs are not publicly self-serve: clients board through TabaPay and receive a dedicated FQDN plus bearer credentials for sandbox and production.'
image: https://cdn.prod.website-files.com/69d506915e199fb590336928/69efd4e2e784c73028ca53f7_Website.svg
layout: provider
mcp_servers:
- description: Official hosted MCP server at https://developers.tabapay.com/mcp (Streamable HTTP) — list/search/get endpoints from the API reference and execute live requests.
  name: TabaPay Developers MCP Server
  slug: tabapay-developers-mcp-server
modified: '2026-07-21'
name: TabaPay
nav: Providers
network: true
overview: 'TabaPay publishes 16 APIs on the [APIs.io](https://apis.io/) network, including 3D Secure API, Account API, Bank API, and 13 more. Tagged areas include Company, Fintech, Payments, Instant Payments, and Money Movement.


  TabaPay''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 28 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 2
  name: Tabapay Rate Limits
  slug: tabapay-rate-limits
score:
  band: developing
  composite: 54.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 55.6
    developer_ergonomics: 79.9
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 54.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Tabapay Authentication
  slug: tabapay-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tabapay Domain Security
  slug: tabapay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tabapay
tags:
- Company
- Fintech
- Payments
- Instant Payments
- Money Movement
- Payouts
- Cards
- Real-Time Payments
- ACH
website: https://tabapay.com
---

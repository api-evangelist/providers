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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Aza Finance Agentic Access
  operation_count: 49
  slug: aza-finance-agentic-access
  summary_line: 49 operations · 22 acting
api_count: 16
apis:
- description: The Account Debits API from AZA Finance — 1 operation(s) for account debits.
  name: AZA Finance Account Debits API
  slug: aza-finance-account-debits-api
- description: The Account Validation API from AZA Finance — 1 operation(s) for account validation.
  name: AZA Finance Account Validation API
  slug: aza-finance-account-validation-api
- description: The Accounts API from AZA Finance — 2 operation(s) for accounts.
  name: AZA Finance Accounts API
  slug: aza-finance-accounts-api
- description: The API Logs API from AZA Finance — 2 operation(s) for api logs.
  name: AZA Finance API Logs API
  slug: aza-finance-api-logs-api
- description: The Currency Info API from AZA Finance — 3 operation(s) for currency info.
  name: AZA Finance Currency Info API
  slug: aza-finance-currency-info-api
- description: The dlocal balance API from AZA Finance — 1 operation(s) for dlocal balance.
  name: AZA Finance dlocal balance API
  slug: aza-finance-dlocal-balance-api
- description: The Documents API from AZA Finance — 2 operation(s) for documents.
  name: AZA Finance Documents API
  slug: aza-finance-documents-api
- description: The Logs API from AZA Finance — 2 operation(s) for logs.
  name: AZA Finance Logs API
  slug: aza-finance-logs-api
- description: The Mandates API from AZA Finance — 1 operation(s) for mandates.
  name: AZA Finance Mandates API
  slug: aza-finance-mandates-api
- description: The Payin Methods API from AZA Finance — 2 operation(s) for payin methods.
  name: AZA Finance Payin Methods API
  slug: aza-finance-payin-methods-api
- description: The Payment Methods API from AZA Finance — 2 operation(s) for payment methods.
  name: AZA Finance Payment Methods API
  slug: aza-finance-payment-methods-api
- description: The Payout Methods API from AZA Finance — 2 operation(s) for payout methods.
  name: AZA Finance Payout Methods API
  slug: aza-finance-payout-methods-api
- description: The Recipients API from AZA Finance — 3 operation(s) for recipients.
  name: AZA Finance Recipients API
  slug: aza-finance-recipients-api
- description: The Senders API from AZA Finance — 2 operation(s) for senders.
  name: AZA Finance Senders API
  slug: aza-finance-senders-api
- description: The Transactions API from AZA Finance — 7 operation(s) for transactions.
  name: AZA Finance Transactions API
  slug: aza-finance-transactions-api
- description: The Webhooks API from AZA Finance — 3 operation(s) for webhooks.
  name: AZA Finance Webhooks API
  slug: aza-finance-webhooks-api
arazzos:
- description: Quote FX, create a sender, create a transaction, fund it, and confirm settlement.
  name: AZA Finance — send a cross-border payout
  slug: aza-finance-send-payout
artifact_total: 39
asyncapis:
- description: ''
  name: Aza Finance Webhooks
  slug: aza-finance-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TransferZero Account Debits API
  slug: open-aza-finance-account-debits-api
- collection_type: open
  name: TransferZero Account Debits Account Validation API
  slug: open-aza-finance-account-validation-api
- collection_type: open
  name: TransferZero Account Debits Accounts API
  slug: open-aza-finance-accounts-api
- collection_type: open
  name: TransferZero Account Debits API Logs API
  slug: open-aza-finance-api-logs-api
- collection_type: open
  name: TransferZero Account Debits Currency Info API
  slug: open-aza-finance-currency-info-api
- collection_type: open
  name: TransferZero Account Debits dlocal balance API
  slug: open-aza-finance-dlocal-balance-api
- collection_type: open
  name: TransferZero Account Debits Documents API
  slug: open-aza-finance-documents-api
- collection_type: open
  name: TransferZero Account Debits Logs API
  slug: open-aza-finance-logs-api
- collection_type: open
  name: TransferZero Account Debits Mandates API
  slug: open-aza-finance-mandates-api
- collection_type: open
  name: TransferZero Account Debits Payin Methods API
  slug: open-aza-finance-payin-methods-api
- collection_type: open
  name: TransferZero Account Debits Payment Methods API
  slug: open-aza-finance-payment-methods-api
- collection_type: open
  name: TransferZero Account Debits Payout Methods API
  slug: open-aza-finance-payout-methods-api
- collection_type: open
  name: TransferZero Account Debits Recipients API
  slug: open-aza-finance-recipients-api
- collection_type: open
  name: TransferZero Account Debits Senders API
  slug: open-aza-finance-senders-api
- collection_type: open
  name: TransferZero Account Debits Transactions API
  slug: open-aza-finance-transactions-api
- collection_type: open
  name: TransferZero Account Debits Webhooks API
  slug: open-aza-finance-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/aza-finance-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.transferzero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.transferzero.com/docs/home/
- group: docs
  title: ''
  type: APIReference
  url: https://api.transferzero.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.transferzero.com/docs/home/
- group: auth
  title: ''
  type: Authentication
  url: authentication/aza-finance-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/aza-finance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aza-finance-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aza-finance-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aza-finance-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aza-finance-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aza-finance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aza-finance-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aza-finance-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aza-finance-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aza-finance-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aza-finance-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aza-finance-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aza-finance-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://azafinance.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transferzero
- group: operate
  title: ''
  type: Support
  url: https://azafinance.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azafinance.com/terms-and-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://azafinance.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://account.azafinance.com/signin
- group: company
  title: ''
  type: Website
  url: https://www.azafinance.com/
created: '2026-07-17'
description: AZA Finance is a regulated financial-infrastructure provider delivering foreign exchange (FX), collections, treasury and cross-border payout services across Africa and between Africa and the rest of the world. Its developer platform is the TransferZero API V1 — a REST API that lets businesses create senders, quote FX, send bulk and individual payouts to bank accounts and mobile-money wallets, validate accounts, attach KYC documents, and receive real-time webhook notifications. Authentication is HMAC request-signing; official SDKs are published for Ruby, JavaScript, PHP, .NET and Java. AZA Finance is licensed by the UK FCA (#673100), the Bank of Uganda (#MR 125/23) and the Central Bank of Nigeria.
image: https://www.azafinance.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: aza-finance-mcp.yml
  slug: aza-finance-mcpyml
modified: '2026-07-18'
name: AZA Finance
nav: Providers
network: true
overview: 'AZA Finance publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account Debits API, Account Validation API, Accounts API, and 13 more. Tagged areas include Company, Financial Services, Payments, Foreign Exchange, and Cross-Border Payments.


  The AZA Finance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AZA Finance''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 20 more developer resources.'
random_paper: 42
score:
  band: thin
  composite: 34.6
  delta: -12.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 67.7
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/aza-finance/refs/heads/main/screenshots/aza-finance-2026-07-25T202112.png
security:
- kind: authentication
  name: Aza Finance Authentication
  slug: aza-finance-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Aza Finance Domain Security
  slug: aza-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aza-finance
tags:
- Company
- Financial Services
- Payments
- Foreign Exchange
- Cross-Border Payments
- Africa
- Fintech
- API
website: https://www.azafinance.com/
---

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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: First-party hosted remote MCP server, launched with API 1.7.0 on 2026-06-05, exposing 16 read tools over wallets, balances, financial movements, payments, live FX rates, spot trades, fixed forwards an
  name: iBanFirst MCP Connector
  slug: ibanfirst-mcp-connector
- description: PSD2 access-to-account API for registered third-party providers, covering account information services (AIS), payment initiation services (PIS) and strong customer authentication. A sandbox is publish
  name: iBanFirst PSD2 XS2A API
  slug: ibanfirst-psd2-xs2a-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: Each of your accounts has its own specific currency and IBAN. The API allows you to get details and balances about each account in real time. **Note :** ***accounts*** are also labelled as ***wallets*
  name: iBanFirst Accounts API
  slug: ibanfirst-accounts-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: A beneficiary can be either your own account in another bank or a third party recipient account. Beneficiaries can be created or deleted through the API. **Note :** ***beneficiaries*** are also labell
  name: iBanFirst Beneficiaries API
  slug: ibanfirst-beneficiaries-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The API allows you to access your documents stored on the iBanFirst platform through a one-time access link. Documents must be generated on the platform before being available through the API.
  name: iBanFirst Documents API
  slug: ibanfirst-documents-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The API allows you to retrieve all financial movements from your accounts.
  name: iBanFirst Financial movements API
  slug: ibanfirst-financial-movements-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: 'Book a fixed forward payment contracts instantly on iBanFirst without manual intervention. - Available currency pairs: - **EUR/USD** - **EUR/GBP** - **GBP/USD** - Maturities: **up to 6 months**. - Tra'
  name: iBanFirst Fixed forward payment contract API
  slug: ibanfirst-fixed-forward-payment-contract-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The Logs API from iBanFirst — 2 operation(s) for logs.
  name: iBanFirst Logs API
  slug: ibanfirst-logs-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: 'Sending funds from one of your iBanFirst accounts to your own external bank account or a third-party recipient involves two steps: 1. Generate the payment object with the ''Create payment'' method. A un'
  name: iBanFirst Payments API
  slug: ibanfirst-payments-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The API provides a deliverable FX facility and deliverable FX liquidity. You will become counterparty to iBanFirst and can market and sell deliverable FX services to corporate and private clients as w
  name: iBanFirst Spot trades API
  slug: ibanfirst-spot-trades-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: '**1. WHAT IS A WEBHOOK ?** - Webhooks are events based real-time notifications providing updates on transactions and removing the need for periodic polling. - Webhook notifications are sent as HTTPS P'
  name: iBanFirst Webhook subscriptions API
  slug: ibanfirst-webhook-subscriptions-api
artifact_total: 19
asyncapis:
- description: ''
  name: Ibanfirst Webhooks
  slug: ibanfirst-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ibanfirst-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.ibanfirst.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ibanfirst.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ibanfirst.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ibanfirst.com/api/clientapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ibanfirst.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.ibanfirst.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.ibanfirst.com/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iBanFirst
- group: commercial
  title: ''
  type: Pricing
  url: https://ibanfirst.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://info.ibanfirst.com/en/request-an-account
- group: start
  title: ''
  type: Login
  url: https://platform.ibanfirst.com/login?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ibanfirst.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ibanfirst.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/productibf/ibanfirst-rest-api-workspace/collection/d24hl8d/ibanfirst-rest-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ibanfirst.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ibanfirst-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ibanfirst-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.ibanfirst.com/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ibanfirst-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ibanfirst-security.txt
- group: auth
  title: ''
  type: Security
  url: https://ibanfirst.com/security-policy.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibanfirst-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibanfirst-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ibanfirst-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ibanfirst-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ibanfirst-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ibanfirst.com/psd2-api
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ibanfirst-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ibanfirst-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ibanfirst-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ibanfirst-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ibanfirst-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/ibanfirst-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ibanfirst-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ibanfirst-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ibanfirst-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ibanfirst-clientapi-overlay.yaml
created: '2026-08-17'
description: iBanFirst is a Brussels-headquartered cross-border payment and foreign-exchange platform for businesses, licensed as a payment institution by the National Bank of Belgium (company number 0849.872.824) and operating across Belgium, France, the Netherlands, Germany, Spain, Romania, Bulgaria, Italy, Hungary and the United Kingdom. It provides multi-currency "augmented currency accounts" with dedicated IBANs, SWIFT and SEPA payments with payment tracking, spot FX in 30+ currencies, and fixed forward payment contracts for currency-risk hedging. Its developer surface is a public REST API (iBanFirst API 1.6.0, 38 operations over accounts, financial movements, beneficiaries, payments, spot trades, fixed forwards, documents and webhook subscriptions), X-WSSE token authentication, HMAC-SHA256-signed webhooks for payment and trade events, a separate eIDAS/QWAC-gated PSD2 XS2A API for AIS and PIS third-party providers, and a hosted first-party remote MCP server that gives agents read access
  to treasury data.
image: https://ibanfirst.com/_next/static/media/iban-og-image.1rlnmbejef6_m.jpg
layout: provider
mcp_servers:
- description: ''
  name: iBanFirst MCP
  slug: ibanfirst-mcp
- description: ''
  name: iBanFirst MCP Server
  slug: ibanfirst-mcp-server
modified: '2026-08-17'
name: iBanFirst
nav: Providers
network: true
overview: 'iBanFirst publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Beneficiaries API, Documents API, and 6 more. Tagged areas include Company, Fintech Insurtech, Cross-Border Payments, Foreign Exchange, and B2B Payments.


  The iBanFirst catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  iBanFirst''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Ibanfirst Plans Pricing
  plan_count: 1
  slug: ibanfirst-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Ibanfirst Rate Limits
  slug: ibanfirst-rate-limits
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 57.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 59.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/screenshots/ibanfirst-2026-09-02T145820.png
security:
- kind: authentication
  name: Ibanfirst Authentication
  slug: ibanfirst-authentication
  summary_line: apiKey/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Ibanfirst Domain Security
  slug: ibanfirst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibanfirst Vulnerability Disclosure
  slug: ibanfirst-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ibanfirst
tags:
- Company
- Fintech Insurtech
- Cross-Border Payments
- Foreign Exchange
- B2B Payments
- Treasury
- multi-currency-accounts
- Swift
- SEPA
- PSD2
- Open Banking
- currency-risk-management
- Webhook
- MCP
- Belgium
- Europe
website: https://www.ibanfirst.com/
---

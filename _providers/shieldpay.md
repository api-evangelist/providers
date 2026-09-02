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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API to manage payment workflows end to end — create projects, manage payers and payees, run KYC verification, and authorise payments to disburse funds securely. Secured with mTLS + API key + RSA-
  name: Shieldpay Partner API
  slug: shieldpay-partner-api
artifact_total: 6
asyncapis:
- description: ''
  name: Shieldpay Webhooks
  slug: shieldpay-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shieldpay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.shieldpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shieldpay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.shieldpay.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.shieldpay.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.shieldpay.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.shieldpay.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shieldpay
- group: start
  title: ''
  type: Login
  url: https://ent.shieldpay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shieldpay.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shieldpay.com/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shieldpay.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/shieldpay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shieldpay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shieldpay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shieldpay-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shieldpay-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shieldpay-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shieldpay-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shieldpay-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/shieldpay-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/shieldpay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/shieldpay-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shieldpay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.shieldpay.com/security/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/shieldpay-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shieldpay-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shieldpay-llms.txt
created: '2026-07-17'
description: Shieldpay is an FCA-authorised (firm reference 770210) payments platform built for the UK legal and professional-services sector, offering a regulated alternative to holding client money in traditional client accounts. It combines KYC/due-diligence verification of parties, safeguarding of funds with tier-1 banking partners (Citi and ClearBank), and audited disbursement of payments, supporting M&A holdbacks/earnouts and shareholder distributions, multi-claimant litigation settlements, escrow, conveyancing, and ongoing client-money management via its Third-Party Managed Account (TPMA) service. Shieldpay has processed over £18 billion and serves 40+ of the UK top-100 law firms. Its Partner API lets integrators programmatically create projects, manage payers and payees, run KYC, and authorise payments; the API secures every request with mutual TLS, an API key, an RSA-SHA256 request signature, a v4-UUID RequestID for idempotency, and IP whitelisting, and delivers real-time events
  over webhooks.
image: https://d24lr4zqs1tgqh.cloudfront.net/69dd90cd-7657-4b6d-8bb5-361a7e0d99d6.png
layout: provider
modified: '2026-07-21'
name: Shieldpay
nav: Providers
network: true
overview: 'Shieldpay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Escrow, Legal Technology, and Fintech.


  The Shieldpay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shieldpay''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 50.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shieldpay/refs/heads/main/screenshots/shieldpay-2026-08-17T081831.png
security:
- kind: authentication
  name: Shieldpay Authentication
  slug: shieldpay-authentication
  summary_line: mutualTLS/apiKey/requestSignature · 4 schemes
- kind: domain-security
  name: Shieldpay Domain Security
  slug: shieldpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shieldpay Vulnerability Disclosure
  slug: shieldpay-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Shieldpay Trust Center
  slug: shieldpay-trust-center
  summary_line: ISO 27001, Cyber Essentials, FIPS 140-2
slug: shieldpay
tags:
- Company
- Payments
- Escrow
- Legal Technology
- Fintech
- Compliance
- KYC
- Banking
website: https://shieldpay.com/
---

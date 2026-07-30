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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Falcon's RESTful embedded-finance API for card issuance, lending, and program management. All responses are JSON; authentication is a JWT bearer token obtained from a client-id/client-secret login, wi
  name: Falcon API
  slug: falcon-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://falconfs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.falconfs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.falconfs.com/docs/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://docs.falconfs.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.falconfs.com/docs/quick-start
- group: company
  title: ''
  type: Blog
  url: https://falconfs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://falconfs.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://falconfs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://falconfs.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://docs.falconfs.com/docs/certifications
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.falconfs.com/reference/versioning
- group: auth
  title: ''
  type: Authentication
  url: authentication/falcon-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/falcon-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/falcon-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/falcon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/falcon-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/falcon-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/falcon-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/falcon-llms.txt
created: '2026-07-17'
description: 'Falcon (Falcon Financial Services, falconfs.com) is a global embedded-finance and Banking-as-a-Service platform that lets fintechs, banks, and enterprises launch credit and payment products in days rather than months. Its developer-first REST APIs and no-code tooling cover the full issuance and lending lifecycle: issuer and program onboarding, enterprise and user KYC, credit-card issuance (virtual, physical, add-on, co-branded, corporate), accounts and credit limits, transactions, statements, repayments and auto-debit, EMI conversion and amortisation, disputes, rewards, interest, fees, funding, and reconciliations. Falcon holds its own lending and issuance licenses, is built on a modular multi-tenant architecture, and is certified against PCI DSS, ISO 27001:2022, and SOC 2. Product lines include Falcon CardFX (issuance), CreditFX (lending), WalletFX (prepaid/wallets), and SurgeFX (AI growth and portfolio tools).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/falcon.png
layout: provider
modified: '2026-07-19'
name: Falcon
nav: Providers
network: true
overview: 'Falcon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Financial Services, Banking, and Payments.


  Falcon''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 12 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 29.2
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 7.9
  previous_composite: 33.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/screenshots/falcon-2026-07-25T214200.png
security:
- kind: authentication
  name: Falcon Authentication
  slug: falcon-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Falcon Domain Security
  slug: falcon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: falcon
tags:
- Company
- Infrastructure
- Financial Services
- Banking
- Payments
- Credit Cards
- Embedded Finance
- Fintech
- Card Issuing
- Lending
- Banking as a Service
- India
website: https://falconfs.com/
---

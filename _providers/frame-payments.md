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
    agent_skills: true
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
  score: 29.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Frame REST API for payments, payouts, accounts, KYC/identity, disputes, subscriptions, invoices, and usage-based billing. Bearer secret-key auth over HTTPS; page-based pagination; HMAC-SHA256 sign
  name: Frame API
  slug: frame-api
artifact_total: 4
asyncapis:
- description: ''
  name: Frame Payments Webhooks
  slug: frame-payments-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://framepayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.framepayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.framepayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.framepayments.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.framepayments.com/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.framepayments.com
- group: commercial
  title: ''
  type: Pricing
  url: https://framepayments.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.framepayments.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://framepayments.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://framepayments.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Frame-Payments
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/frame-payments-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/frame-payments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/frame-payments-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/frame-payments-cli.yml
- group: design
  title: ''
  type: Components
  url: components/frame-payments-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/frame-payments-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/frame-payments-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/frame-payments-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/frame-payments-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/frame-payments-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/frame-payments-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/frame-payments-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/frame-payments-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/frame-payments-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frame-payments-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Frame Payments is a payments and compliance platform ("operating system") for high-compliance and high-risk merchants across regulated verticals including travel, crypto, telemedicine, gaming, gambling, the creator economy, and AI businesses. The frameOS platform unifies payments, payouts, KYC/KYB, identity verification, fraud detection (Sonar), geocompliance, disputes, subscriptions, and usage-based billing behind one REST API at api.framepayments.com/v1. Frame ships backend SDKs (Node, PHP, Ruby), mobile SDKs (iOS, Android, React Native), the Frame.js browser SDK with embeddable elements, a sandbox-only CLI, and HMAC-signed webhooks. Backed by Techstars.
image: https://framerusercontent.com/images/ZuP5qavgwprrdI5GSuMK3zq6P0.jpg
layout: provider
modified: '2026-07-19'
name: Frame Payments
nav: Providers
network: true
overview: 'Frame Payments publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Financial-Services, Fintech, and KYC.


  The Frame Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Frame Payments'' developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, CLI, and 20 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 51.7
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 60.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/frame-payments/refs/heads/main/screenshots/frame-payments-2026-07-25T215103.png
security:
- kind: authentication
  name: Frame Payments Authentication
  slug: frame-payments-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Frame Payments Domain Security
  slug: frame-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: frame-payments
tags:
- Company
- Payments
- Financial-Services
- Fintech
- KYC
- Compliance
- Fraud Detection
- Billing
- Payouts
- Identity Verification
website: https://framepayments.com/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'REST API for accepting bKash payments — token-based auth (Grant/Refresh Token), Checkout and Tokenized Checkout (create/execute/query payment, create/execute agreement), Refund, Instant Payout (B2C), '
  name: bKash Payment Gateway (PGW)
  slug: bkash-payment-gateway-pgw
artifact_total: 4
asyncapis:
- description: ''
  name: Bkash Webhooks
  slug: bkash-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bkash-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bka.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bka.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bka.sh/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bka.sh/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bKash-developer
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bkash-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bkash-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bkash-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bkash-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bkash-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bkash-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bkash-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bkash-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bkash-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bkash-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bkash-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/bkash-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/bkash-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bkash-mcp.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.bka.sh/usage-plan
- group: operate
  title: ''
  type: Support
  url: https://www.bkash.com/en/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bkash.com/en/page/tokenized_checkout
created: '2026-07-17'
description: bKash is Bangladesh's largest mobile financial services (MFS) provider, offering a Payment Gateway (PGW) that lets online and mobile merchants accept bKash wallet payments through secure REST APIs. The developer platform (developer.bka.sh, public beta "Inferno Dragon") documents Checkout (hosted iframe/URL), Tokenized Checkout (agreement-based PIN-only payments), Instant Payout (B2C disbursement), Add Wallet, Auth and Capture, Subscriptions, and real-time webhook Instant Payment Notifications. Integration follows a token-based flow — Grant Token, Create Payment, Execute Payment, Query, Refund — with a self-service sandbox (service-name.sandbox.bka.sh) and production (service-name.pay.bka.sh) environments. bKash is a portfolio company associated with the SoftBank Vision Fund and is majority owned by BRAC Bank, with investment from Ant Group, the Bill & Melinda Gates Foundation, and IFC.
image: https://developer.bka.sh/favicon.ico
layout: provider
modified: '2026-07-18'
name: bKash
nav: Providers
network: true
overview: 'bKash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payment Gateway, and Mobile Financial Services.


  The bKash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  bKash''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, sandbox, pricing, and 16 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 32.7
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bkash/refs/heads/main/screenshots/bkash-2026-07-25T203226.png
security:
- kind: authentication
  name: Bkash Authentication
  slug: bkash-authentication
  summary_line: token/apiKey · 2 schemes
- kind: domain-security
  name: Bkash Domain Security
  slug: bkash-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bkash
tags:
- Company
- Fintech
- Payments
- Payment Gateway
- Mobile Financial Services
- Digital Wallet
- Bangladesh
- Checkout
- Webhook
website: https://developer.bka.sh/
---

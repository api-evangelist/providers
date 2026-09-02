---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: The MoMo All-in-One (AIO v2) merchant payment gateway. One integration covers MoMo e-wallet, domestic ATM card, credit card, Apple Pay, Google Pay, Buy Now Pay Later, Quick Pay POS scanner, collection
  name: MoMo All-in-One Payment Gateway (AIO v2)
  slug: aio-payment-gateway
- description: 'Server-to-server API for operating a MoMo Business Page: list and read managed pages, update page detail, images, logo, opening times, utilities and ambiences, publish and read posts and their comment'
  name: MoMo Business Page OpenAPI
  slug: business-page-openapi
- description: API for creating and distributing promotion campaigns and voucher codes to MoMo users, and for reconciling redemption. Create and update campaigns, upload voucher codes by file, query campaign and vou
  name: MoMo Voucher Distribution API
  slug: voucher-distribution
- description: The M_Service Open Platform server-to-server API used by Mini Apps embedded in the MoMo app. Exchange a user authorisation code for a short-lived access token, read the user profile fields the user co
  name: MoMo Mini App Open API
  slug: mini-app-open-api
artifact_total: 10
asyncapis:
- description: ''
  name: Momo Webhooks
  slug: momo-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/momo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.momo.vn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.momo.vn/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.momo.vn/v3/docs/payment/guides/home/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.momo.vn/v3/docs/payment/api/wallet/onetime/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.momo.vn/v3/docs/payment/onboarding/integration-process/
- group: operate
  title: ''
  type: Support
  url: https://developers.momo.vn/v3/docs/app-center/technical-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.momo.vn/hoi-dap
- group: company
  title: ''
  type: Blog
  url: https://www.momo.vn/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/momo-wallet
- group: start
  title: ''
  type: SignUp
  url: https://business.momo.vn/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.momo.vn/dieu-khoan-dieu-le
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.momo.vn/chinh-sach-quyen-rieng-tu
- group: build
  title: ''
  type: Postman
  url: https://developers.momo.vn/v3/docs/payment/api/other/postman/
- group: build
  title: ''
  type: Packages
  url: packages/momo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/momo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/momo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/momo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/momo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/momo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/momo-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/momo-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/momo-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/momo-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/momo-cli.yml
- group: design
  title: ''
  type: Components
  url: components/momo-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/momo-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/momo-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/momo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/momo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/momo-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/momo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/momo-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/momo-llms.txt
created: '2026-08-26'
description: MoMo is Vietnam's largest mobile-money and e-wallet platform, operated by Online Mobile Services Joint Stock Company (Cong ty Co phan Dich vu Di dong Truc tuyen, "M_Service"), founded in 2007 and licensed by the State Bank of Vietnam for e-wallet, money transfer and collection/disbursement services. Alongside the consumer wallet it runs a merchant payments business whose public developer surface at developers.momo.vn documents the All-in-One (AIO v2) Payment Gateway for wallet, domestic ATM card, credit card, Apple Pay, Google Pay, Buy Now Pay Later, POS Quick Pay and static/dynamic QR acceptance, single and batch disbursement, collection links, and tokenised one-click and subscription payments. It also publishes a Business Page OpenAPI, a Voucher Distribution API and a Mini App Open Platform for third-party apps embedded inside the MoMo app. Integration is HMAC-SHA256 signed with RSA and AES payload encryption, uses requestId-based idempotency and server-to-server IPN callbacks,
  and is distributed as fourteen public Postman collections plus first-party PHP, Java and mobile SDKs.
image: https://homepage.momocdn.net/img/momo-amazone-s3-api-241029082636-638657871963540172.jpg
layout: provider
modified: '2026-08-26'
name: MoMo
nav: Providers
network: true
overview: 'MoMo publishes 1 API on the [APIs.io](https://apis.io/) network: All-in-One Payment Gateway (AIO v2). Tagged areas include Payments, Mobile Payments, Fintech, Digital Wallet, and Payment Gateway.


  The MoMo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MoMo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Momo Plans Pricing
  plan_count: 0
  slug: momo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Momo Rate Limits
  slug: momo-rate-limits
scopes:
- name: Momo Scopes
  scope_count: 0
  slug: momo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 83.3
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 50.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Momo Authentication
  slug: momo-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Momo Domain Security
  slug: momo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: momo
tags:
- Payments
- Mobile Payments
- Fintech
- Digital Wallet
- Payment Gateway
- QR Payments
- Disbursement
- Buy Now Pay Later
- E-Commerce
- Vietnam
website: https://www.momo.vn/
---

---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-09-24'
api_count: 2
apis:
- description: BANCOMAT Pay is a mobile payment service enabling Italian consumers to make e-commerce purchases and P2P transfers through a smartphone app linked to their bank account by phone number and IBAN. Merch
  name: BANCOMAT Pay
  slug: bancomat-pay
- baseURL: https://app.flowpay.it/api
  baseurl_source: declared
  description: Production REST API of FlowPay S.r.l., the Bank of Italy-authorised payment institution (AISP/PISP, ref. 36925) that BANCOMAT S.p.A. acquired on 2025-07-22. Tenant-scoped endpoints for account informa
  name: FlowPay API (v1)
  slug: flowpay-api-v1
- baseURL: https://api.flowpay.it/v2
  baseurl_source: declared
  description: 'Second-generation FlowPay API published as OpenAPI 3.1.0 (2.0.0-alpha.4) in the public FlowPay/client-openapi GitHub repository, with operationIds, page/size pagination, documented 100 req/min and 10 '
  name: FlowPay API (v2)
  slug: flowpay-api-v2
artifact_total: 31
asyncapis:
- description: ''
  name: Bancomat Flowpay Webhooks
  slug: bancomat-flowpay-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://flowpay.it/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlowPay
- group: company
  title: ''
  type: Blog
  url: https://blog.flowpay.it/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.flowpay.it/feed/
- group: operate
  title: ''
  type: Support
  url: https://youtrack.flowpay.it/
- group: operate
  title: ''
  type: Support
  url: https://bancomat.it/en/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://bancomat.it/en/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bancomat.it/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bancomat.it/en/terms-and-conditions
- group: operate
  title: ''
  type: PressReleases
  url: https://bancomat.it/en/press-releases
- group: start
  title: ''
  type: Login
  url: https://insight.bancomat.it/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/packages/bancomat-packages.yml
  title: ''
  type: Packages
  url: packages/bancomat-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/packages/bancomat-packages.yml
  title: ''
  type: SDKs
  url: packages/bancomat-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/cli/bancomat-cli.yml
  title: ''
  type: CLI
  url: cli/bancomat-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/well-known/bancomat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bancomat-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/authentication/bancomat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bancomat-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/scopes/bancomat-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bancomat-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/errors/bancomat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bancomat-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/conventions/bancomat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bancomat-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/lifecycle/bancomat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bancomat-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/conformance/bancomat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bancomat-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/conformance/bancomat-conformance.yml
  title: ''
  type: Compliance
  url: conformance/bancomat-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/data-model/bancomat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bancomat-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/llms/bancomat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bancomat-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/plans/bancomat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bancomat-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/rate-limits/bancomat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bancomat-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/security/bancomat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bancomat-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bancomatofficial
- group: company
  title: ''
  type: Website
  url: https://bancomat.it/en
- group: company
  title: ''
  type: Website
  url: https://bancomat.it/en/the-company
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/rules/bancomat-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/bancomat-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/vocabulary/bancomat-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/bancomat-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/json-ld/bancomat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bancomat-context.jsonld
created: '2024-01-15'
description: BANCOMAT S.p.A. is Italy's leading payment network operator managing the PagoBancomat debit card scheme, ATM network, and BANCOMAT Pay mobile payment service. Launched in 1983 for ATM withdrawals and expanded in 1986 with PagoBancomat for PIN-based POS payments, the network underpins Italian electronic payment infrastructure. BANCOMAT Pay, introduced in 2019, enables mobile e-commerce and P2P payments linked to bank accounts via phone number and IBAN. Since the 2025-07-22 acquisition of FlowPay S.r.l., a Bank of Italy-authorised payment institution (AISP/PISP), the group also publishes a public open-banking REST API — account information, payment initiation, invoicing, pagoPA notices and webhooks — with OpenAPI contracts on docs.flowpay.it and GitHub.
features:
- description: Italy's largest ATM cash withdrawal network operational since 1983.
  name: ATM Network
- description: PIN-based POS debit card payments accepted at millions of Italian merchants.
  name: PagoBancomat Debit
- description: Mobile app payment service for e-commerce and P2P transfers linked to bank accounts.
  name: BANCOMAT Pay Mobile
- description: QR code-based checkout integration for online and in-store merchants.
  name: QR Code Payments
- description: Deep integration with Italian banks enabling account-linked payment authorization.
  name: Bank Integration
- description: Person-to-person money transfers between Italian bank accounts via mobile app.
  name: P2P Transfers
finops:
- name: Bancomat Finops
  service_category: API
  slug: bancomat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bancomat.png
integrations:
- description: Integration via Nexi XPay Global payment gateway for merchant acceptance.
  name: Nexi
- description: Integration via Axerve/Fabrick for Italian e-commerce BANCOMAT Pay acceptance.
  name: Axerve (Fabrick)
- description: Integration via PPRO for international PSP access to BANCOMAT Pay.
  name: PPRO
- description: Integration via HiPay payment platform.
  name: HiPay
- description: Integration via Viva.com payment services.
  name: Viva.com
- description: Integration via PayPal Braintree payment gateway.
  name: PayPal Braintree
- description: Integration via Nuvei payment technology platform.
  name: Nuvei
jsonld:
- class_count: 0
  name: Bancomat Context
  property_count: 15
  slug: bancomat-context
layout: provider
mcp_servers:
- description: ''
  name: Derived candidate tool list (no server shipped)
  slug: derived-candidate-tool-list-no-server-shipped
modified: '2026-09-17'
name: Bancomat
nav: Providers
network: true
overview: 'Bancomat publishes 2 APIs on the [APIs.io](https://apis.io/) network: FlowPay API (v1) and FlowPay API (v2). Tagged areas include ATM, Banking, Financial Services, Italy, and Mobile Payments.


  The Bancomat catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bancomat''s developer surface includes engineering blog, support, FAQ, CLI, authentication, and 28 more developer resources.'
plans:
- name: Bancomat Plans Pricing
  plan_count: 0
  slug: bancomat-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Bancomat Rate Limits
  slug: bancomat-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: Bancomat API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: bancomat-spectral-rules
scopes:
- name: Bancomat Scopes
  scope_count: 55
  slug: bancomat-scopes
  summary_line: 55 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 66.0
    catalog_earned_first_party: 8.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 63.6
    contract_quality: 71.7
    developer_ergonomics: 58.9
    discoverability: 59.3
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 60.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/screenshots/bancomat-2026-06-20T172935.png
security:
- kind: authentication
  name: Bancomat Authentication
  slug: bancomat-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Bancomat Domain Security
  slug: bancomat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bancomat
tags:
- ATM
- Banking
- Financial Services
- Italy
- Mobile Payments
- Payments
- Debit Cards
- Open Banking
- PSD2
- Account Information
- Payment Initiation
- Invoicing
- pagoPA
use_cases:
- description: Debit card ATM withdrawals across Italy's national banking network.
  name: ATM Cash Withdrawals
- description: PIN-based debit card payments at retail point-of-sale terminals.
  name: POS Debit Payments
- description: Online checkout integration via BANCOMAT Pay mobile app.
  name: E-Commerce Payments
- description: Person-to-person payments between bank accounts via mobile app.
  name: P2P Money Transfer
- description: Enable BANCOMAT Pay as a local Italian payment method for online stores.
  name: Merchant Acceptance
website: https://flowpay.it/
---

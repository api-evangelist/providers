---
access_model:
  confidence: high
  label: Paid — €0.06 per transaction + €18/year; PREPROD sandbox on request (up to 2 weeks), production keys after contract
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.bancontact.com/en/professional/our-solutions/integrated-solution
  - https://docs.bancontactpro.com/guides/general/gettingstarted052025v4
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-09-25'
api_count: 3
apis:
- baseURL: https://merchant.api.bancontact.net
  baseurl_source: declared
  description: 'First-party OpenAPI 3.1 contract (v3.6.5) for the Bancontact Pro merchant acceptance service, formerly the Payconiq merchant API. Merchants create dynamic QR / deeplink / checkout payments, static-QR '
  name: Bancontact Pro Payment V3 API
  slug: payconiq-acceptance-api
- baseURL: https://merchant.api.bancontact.net
  baseurl_source: declared
  description: First-party OpenAPI 3.1 contract (v3.0.3) for creating and retrieving refunds against SUCCEEDED Bancontact Pro payments. Refund creation is idempotent on a required Idempotency-Key header, must be act
  name: Bancontact Pro Payment Refund Service API
  slug: payment-refund-service-api
- baseURL: https://merchant.api.bancontact.net
  baseurl_source: declared
  description: 'First-party OpenAPI 3.1 contract (v3.0.1) for reconciling Bancontact Pro payouts with the payments and refunds they settle: list payouts by date, list SUCCEEDED payments and refunds by payout id or 30'
  name: Bancontact Pro Merchant Reconciliation API
  slug: merchant-reconciliation-api
artifact_total: 23
asyncapis:
- description: ''
  name: Bancontact Callbacks Webhooks
  slug: bancontact-callbacks-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/authentication/bancontact-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bancontact-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/security/bancontact-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bancontact-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bancontactcompany/
- group: company
  title: ''
  type: Website
  url: https://www.bancontact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bancontactpro.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/rules/bancontact-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/bancontact-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/vocabulary/bancontact-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/bancontact-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/json-ld/bancontact-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bancontact-context.jsonld
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.bancontactpro.com/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bancontactpro.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bancontactpro.com/apis/merchant-payment.openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bancontactpro.com/guides/general/gettingstarted052025v4
- group: operate
  title: ''
  type: FAQ
  url: https://docs.bancontactpro.com/guides/general/faq
- group: operate
  title: ''
  type: Support
  url: https://www.bancontact.com/en/professional/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bancontact.com/en/faq?audience=professional
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bancontact.com/en/professional/our-solutions/integrated-solution
- group: start
  title: ''
  type: Login
  url: https://portal.bancontactpro.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.bancontact.com/en/professional/start/integrated-solution
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bancontact.com/en/privacy-statement-and-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bancontact.com/en/privacy-statement-and-terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://www.bancontact.com/en/news
- group: auth
  title: ''
  type: Compliance
  url: https://www.bancontact.com/en/professional/legal-and-administrative-specifications
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/llms/bancontact-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bancontact-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/packages/bancontact-packages.yml
  title: ''
  type: Packages
  url: packages/bancontact-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/well-known/bancontact-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bancontact-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/mcp/bancontact-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bancontact-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/conformance/bancontact-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bancontact-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/errors/bancontact-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bancontact-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/errors/bancontact-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/bancontact-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/lifecycle/bancontact-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bancontact-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/lifecycle/bancontact-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/bancontact-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/sandbox/bancontact-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bancontact-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/conventions/bancontact-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bancontact-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/conventions/bancontact-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bancontact-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/changelog/bancontact-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bancontact-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/data-model/bancontact-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bancontact-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/asyncapi/bancontact-callbacks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bancontact-callbacks-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/plans/bancontact-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bancontact-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/rate-limits/bancontact-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bancontact-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/finops/bancontact-finops.yml
  title: ''
  type: FinOps
  url: finops/bancontact-finops.yml
created: '2025-01-01'
description: 'Bancontact Company nv/sa (formerly Bancontact Payconiq Company) operates Belgium''s national debit card scheme and the Bancontact Pro merchant acceptance service (the rebranded Payconiq merchant platform). The Bancontact Pro developer portal publishes three OpenAPI 3.1 contracts on merchant.api.bancontact.net: the Payment V3 API (create, search, cancel and acknowledge QR/deeplink/checkout payments, with JWS-signed status callbacks), the Payment Refund Service API (idempotent refunds against SUCCEEDED payments) and the Merchant Reconciliation API (D+1 payouts, payments and refunds). Merchants authenticate with per-product API keys and ES256 detached JWS signatures verified against public JWKS endpoints, test end-to-end in a PREPROD environment with published test cards, and pay €0.06 per transaction plus €18 per year.'
features:
- description: Accept Bancontact debit card payments in e-commerce checkouts.
  name: Online Payments
- description: Generate QR codes for in-store and contactless payment acceptance.
  name: QR Code Payments
- description: Payconiq by Bancontact app integration for mobile checkout.
  name: Mobile App Payments
- description: Real-time payment status notifications via webhook callbacks.
  name: Webhooks
- description: Programmatic refund processing for completed transactions.
  name: Refunds
- description: EUR-denominated payments with Belgian bank account settlement.
  name: Multi-currency
- description: Mobile deep links to open the Payconiq app directly from merchant checkout.
  name: Deep Links
finops:
- name: Bancontact Finops
  service_category: API
  slug: bancontact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bancontact.png
jsonld:
- class_count: 0
  name: Bancontact Context
  property_count: 18
  slug: bancontact-context
layout: provider
modified: '2026-09-17'
name: Bancontact
nav: Providers
network: true
overview: 'Bancontact publishes 3 APIs on the [APIs.io](https://apis.io/) network: Pro Payment V3 API, Pro Payment Refund Service API, and Pro Merchant Reconciliation API. Tagged areas include Banking, Belgium, Debit Cards, E-Commerce, and Fintech.


  The Bancontact catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bancontact''s developer surface includes authentication, documentation, API reference, getting-started guide, FAQ, support, pricing, and 34 more developer resources.'
plans:
- name: Bancontact Plans Pricing
  plan_count: 1
  slug: bancontact-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bancontact Rate Limits
  slug: bancontact-rate-limits
rules:
- effective_rule_count: 12
  extends: []
  name: Bancontact API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 6
  slug: bancontact-spectral-rules
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 75.2
    catalog_earned_first_party: 8.0
    catalog_gap: 39.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 81.6
    contract_governance: 67.3
    contract_quality: 62.8
    developer_ergonomics: 66.1
    discoverability: 78.6
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 69.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/screenshots/bancontact-2026-06-20T172938.png
security:
- kind: authentication
  name: Bancontact Authentication
  slug: bancontact-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bancontact Domain Security
  slug: bancontact-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bancontact
tags:
- Banking
- Belgium
- Debit Cards
- E-Commerce
- Fintech
- Payments
- QR Codes
- Refunds
- Reconciliation
- Mobile Payments
use_cases:
- description: Accept Bancontact as a local Belgian payment method at checkout.
  name: E-Commerce Checkout
- description: In-store and restaurant QR code payment acceptance.
  name: QR Code POS
- description: Integrate Bancontact into iOS and Android apps.
  name: Mobile In-App Payments
- description: Payment links and QR codes for invoicing and B2C collections.
  name: Invoice Payments
- description: Recurring payment collection from Belgian consumers.
  name: Subscription Billing
website: https://www.bancontact.com/
---

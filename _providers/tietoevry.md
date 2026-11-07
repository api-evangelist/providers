---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
api_count: 24
apis:
- description: A credit platform used by banks and financial institutions in 20+ countries to manage virtually any type of credit, organised around loan origination, loan life cycle and collection. The developer por
  name: Tietoevry Credit Cloud
  slug: tietoevry-credit-cloud
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for establish and managing account information consent.
  name: TietoEVRY Account consent service API
  slug: tietoevry-account-consent-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for managing account information.
  name: TietoEVRY Account Information Service API
  slug: tietoevry-account-information-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations, which are executed for multiple destination providers.
  name: TietoEVRY Aggregated services API
  slug: tietoevry-aggregated-services-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for bulk payments.
  name: TietoEVRY Bulk Payment Initiation Service API
  slug: tietoevry-bulk-payment-initiation-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for managing card account information.
  name: TietoEVRY Card account information service API
  slug: tietoevry-card-account-information-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for managing card information.
  name: TietoEVRY Card information service API
  slug: tietoevry-card-information-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for receiving funds confirmation.
  name: TietoEVRY Confirmation of Funds Service API
  slug: tietoevry-confirmation-of-funds-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for establish and managing confirmation of funds consent.
  name: TietoEVRY Confirmation of Funds Service consent API
  slug: tietoevry-confirmation-of-funds-service-consent-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operation for creditors
  name: TietoEVRY Creditor API
  slug: tietoevry-creditor-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operation for debtors
  name: TietoEVRY Debtor API
  slug: tietoevry-debtor-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for managing anonymous End Users.
  name: TietoEVRY End User management API
  slug: tietoevry-end-user-management-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for payments.
  name: TietoEVRY Payment Initiation Service API
  slug: tietoevry-payment-initiation-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for recalling the payments.
  name: TietoEVRY Payment Recall Initiation Service API
  slug: tietoevry-payment-recall-initiation-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for periodic payments.
  name: TietoEVRY Periodic Payment Initiation Service API
  slug: tietoevry-periodic-payment-initiation-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for establishing Pre-step SCA
  name: TietoEVRY Pre-step SCA service API
  slug: tietoevry-pre-step-sca-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Retrieve information about providers.
  name: TietoEVRY Provider information API
  slug: tietoevry-provider-information-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations to request for payments.
  name: TietoEVRY Request to pay Initiation Service API
  slug: tietoevry-request-to-pay-initiation-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Signing Baskets Service
  name: TietoEVRY Signing Baskets Service API
  slug: tietoevry-signing-baskets-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations to create subscription.
  name: TietoEVRY Subscription Initiation Service API
  slug: tietoevry-subscription-initiation-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for managing user roles.
  name: TietoEVRY User Roles service API
  slug: tietoevry-user-roles-service-api
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: Operations for managing users.
  name: TietoEVRY Users service API
  slug: tietoevry-users-service-api
artifact_total: 32
asyncapis:
- description: ''
  name: Tietoevry Sepa Direct Debit Webhooks
  slug: tietoevry-sepa-direct-debit-webhooks
common:
- group: other
  href: https://artifacts.apis.io/tietoevry/overlays/tietoevry-tieto-xs2a-accounts-v1-3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tietoevry-tieto-xs2a-accounts-v1-3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tietoevry/overlays/tietoevry-tieto-xs2a-payments-v1-3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tietoevry-tieto-xs2a-payments-v1-3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tietoevry/overlays/tietoevry-openbanking-xs2a-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tietoevry-openbanking-xs2a-swagger-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tietoevry/overlays/tietoevry-financial-api-aggregation-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tietoevry-financial-api-aggregation-swagger-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tietoevry/overlays/tietoevry-sepa-direct-debit-api-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tietoevry-sepa-direct-debit-api-gateway-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/tietoevry/security/tietoevry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tietoevry-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tietoevry/authentication/tietoevry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tietoevry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tietoevry.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tietoevry.com/
- group: docs
  title: ''
  type: Documentation
  url: https://openbanking.api.tietoevry.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://openbanking.api.tietoevry.com/documentation/xs2a
- group: start
  title: ''
  type: GettingStarted
  url: https://openbanking.api.tietoevry.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://openbanking.api.tietoevry.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://openbanking.api.tietoevry.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://openbanking.api.tietoevry.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://openbanking.api.tietoevry.com/faq
- group: other
  title: ''
  type: Glossary
  url: https://openbanking.api.tietoevry.com/documentation/glossary
- group: company
  title: ''
  type: Blog
  url: https://www.tieto.com/en/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tietoevry
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tietoevry.com/en/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tietoevry.com/en/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tietoevry
- group: build
  href: https://artifacts.apis.io/tietoevry/packages/tietoevry-packages.yml
  title: ''
  type: Packages
  url: packages/tietoevry-packages.yml
- group: agent
  href: https://artifacts.apis.io/tietoevry/llms/tietoevry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tietoevry-llms.txt
- group: design
  href: https://artifacts.apis.io/tietoevry/conformance/tietoevry-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tietoevry-conformance.yml
- group: design
  href: https://artifacts.apis.io/tietoevry/errors/tietoevry-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tietoevry-problem-types.yml
- group: build
  href: https://artifacts.apis.io/tietoevry/errors/tietoevry-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/tietoevry-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/tietoevry/lifecycle/tietoevry-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tietoevry-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/tietoevry/sandbox/tietoevry-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tietoevry-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tietoevry/conventions/tietoevry-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tietoevry-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tietoevry/changelog/tietoevry-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tietoevry-changelog.yml
- group: design
  href: https://artifacts.apis.io/tietoevry/data-model/tietoevry-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tietoevry-data-model.yml
- group: agent
  href: https://artifacts.apis.io/tietoevry/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/tietoevry/plans/tietoevry-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tietoevry-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tietoevry/rate-limits/tietoevry-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tietoevry-rate-limits.yml
created: '2026-09-02'
description: 'TietoEVRY (Tietoevry Corporation, listed as TIETO on Nasdaq Helsinki and Stockholm, rebranded to "Tieto" in 2026) is a Nordic software and technology company of roughly 14,000 people operating in 20+ countries, serving banking, healthcare, public sector and industry. Its public API surface is published by the banking business (Tieto Banktech / Tietoevry Banking) through the Tietoevry Banking API Hub at api.tietoevry.com, which fronts three developer portals: an Open Banking PSD2/XS2A platform built on the Berlin Group NextGenPSD2 framework with a free self-service sandbox, a Financial API Aggregation service offering one integration to Nordic and Baltic banks, and a Credit Cloud platform for loan origination and loan life-cycle management. 24 machine-readable Swagger 2.0 / OpenAPI 3.0 contracts covering 211 operations are published unauthenticated from the Open Banking and Aggregation portals, including account information, payment initiation, confirmation of funds, bulk and
  periodic payments, payment recall, request-to-pay, signing baskets, virtual account management, card account information and a SEPA Direct Debits gateway with a webhook event-notification surface.'
finops:
- has_sources: true
  method: derived
  name: Tietoevry Finops
  primary_unit: ''
  service_category: ''
  slug: tietoevry-finops
  template: true
image: https://www.tieto.com/images/tieto-logo.svg
layout: provider
modified: '2026-09-02'
name: TietoEVRY
nav: Providers
network: true
overview: 'TietoEVRY publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account consent service API, Account Information Service API, Aggregated services API, and 19 more. Tagged areas include Company, Banking, Open Banking, PSD2, and XS2A.


  The TietoEVRY catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  TietoEVRY''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 28 more developer resources.'
plans:
- name: Tietoevry Plans Pricing
  plan_count: 0
  slug: tietoevry-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Tietoevry Rate Limits
  slug: tietoevry-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: TietoEVRY API Rules
  rule_count: 57
  severity_counts:
    error: 34
    hint: 0
    info: 7
    warn: 16
  slug: tietoevry-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.5
  facets:
    access_clarity: 27.6
    contract_governance: 31.8
    contract_quality: 54.8
    developer_ergonomics: 44.6
    discoverability: 69.6
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 41.1
  provenance:
    conformance: first-party
    contracts:
      callable: 90.5
      derived: 0
      marker_coverage: 19.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 28.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tietoevry/tietoevry-2026-10-11T130940.png
security:
- kind: authentication
  name: Tietoevry Authentication
  slug: tietoevry-authentication
  summary_line: apiKey/openIdConnect/mutualTLS · 7 schemes
- kind: domain-security
  name: Tietoevry Domain Security
  slug: tietoevry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: tietoevry-initiate-payment
  slug: tietoevry-initiate-payment
- name: tietoevry-read-account-data
  slug: tietoevry-read-account-data
- name: tietoevry-reverse-sepa-direct-debit
  slug: tietoevry-reverse-sepa-direct-debit
slug: tietoevry
tags:
- Company
- Banking
- Open Banking
- PSD2
- XS2A
- Berlin Group
- Payments
- SEPA
- Account Information
- Financial Services
- Aggregation
- Credit
- Fintech
- Nordic
- Finland
website: https://www.tietoevry.com/en/
---

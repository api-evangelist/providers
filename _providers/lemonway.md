---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 59
  human_in_the_loop: 15
  name: Lemonway Agentic Access
  operation_count: 87
  slug: lemonway-agentic-access
  summary_line: 87 operations · 59 acting · 15 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: REST API for online KYC/KYB onboarding flows, enabling marketplace operators to collect identity verification, document uploads, and account creation for both individual and legal entity account holde
  name: Lemonway Onboarding API
  slug: lemonway-onboarding-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The Accounts | Admin API from Lemonway — 9 operation(s) for accounts | admin.
  name: Lemonway Accounts | Admin API
  slug: lemonway-accounts-admin-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The accounts API from Lemonway — 9 operation(s) for accounts.
  name: Lemonway Accounts API
  slug: lemonway-accounts-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The Accounts | Create & KYC API from Lemonway — 7 operation(s) for accounts | create & kyc.
  name: Lemonway Accounts | Create & KYC API
  slug: lemonway-accounts-create-kyc-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The Accounts | Update API from Lemonway — 3 operation(s) for accounts | update.
  name: Lemonway Accounts | Update API
  slug: lemonway-accounts-update-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The Disputes API from Lemonway — 1 operation(s) for disputes.
  name: Lemonway Disputes API
  slug: lemonway-disputes-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The legal-entity-onboarding API from Lemonway — 1 operation(s) for legal-entity-onboarding.
  name: Lemonway Legal Entity Onboarding API
  slug: lemonway-legal-entity-onboarding-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | APM API from Lemonway — 1 operation(s) for moneyins | apm.
  name: Lemonway MoneyIns | APM API
  slug: lemonway-moneyins-apm-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | BNPL API from Lemonway — 2 operation(s) for moneyins | bnpl.
  name: Lemonway MoneyIns | BNPL API
  slug: lemonway-moneyins-bnpl-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Cards API from Lemonway — 11 operation(s) for moneyins | cards.
  name: Lemonway MoneyIns | Cards API
  slug: lemonway-moneyins-cards-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Cheque API from Lemonway — 2 operation(s) for moneyins | cheque.
  name: Lemonway MoneyIns | Cheque API
  slug: lemonway-moneyins-cheque-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Direct Debits API from Lemonway — 7 operation(s) for moneyins | direct debits.
  name: Lemonway MoneyIns | Direct Debits API
  slug: lemonway-moneyins-direct-debits-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Local Payments API from Lemonway — 7 operation(s) for moneyins | local payments.
  name: Lemonway MoneyIns | Local Payments API
  slug: lemonway-moneyins-local-payments-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Pay by Bank API from Lemonway — 2 operation(s) for moneyins | pay by bank.
  name: Lemonway MoneyIns | Pay by Bank API
  slug: lemonway-moneyins-pay-by-bank-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Pay by Link API from Lemonway — 3 operation(s) for moneyins | pay by link.
  name: Lemonway MoneyIns | Pay by Link API
  slug: lemonway-moneyins-pay-by-link-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | PayPal API from Lemonway — 2 operation(s) for moneyins | paypal.
  name: Lemonway MoneyIns | PayPal API
  slug: lemonway-moneyins-paypal-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Transfers In API from Lemonway — 1 operation(s) for moneyins | transfers in.
  name: Lemonway MoneyIns | Transfers In API
  slug: lemonway-moneyins-transfers-in-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyIns | Virtual IBAN API from Lemonway — 3 operation(s) for moneyins | virtual iban.
  name: Lemonway MoneyIns | Virtual IBAN API
  slug: lemonway-moneyins-virtual-iban-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The MoneyOuts API from Lemonway — 6 operation(s) for moneyouts.
  name: Lemonway Money Outs API
  slug: lemonway-moneyouts-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The onboarding API from Lemonway — 1 operation(s) for onboarding.
  name: Lemonway Onboarding API
  slug: lemonway-onboarding-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The onboardings API from Lemonway — 5 operation(s) for onboardings.
  name: Lemonway Onboardings API
  slug: lemonway-onboardings-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The P2Ps API from Lemonway — 1 operation(s) for p2ps.
  name: Lemonway P2Ps API
  slug: lemonway-p2ps-api
- baseURL: https://api.lemonway.com
  baseurl_source: declared
  description: The Refunds API from Lemonway — 2 operation(s) for refunds.
  name: Lemonway Refunds API
  slug: lemonway-refunds-api
artifact_total: 44
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/agentic-access/lemonway-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lemonway-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/rules/lemonway-rules.yml
  title: ''
  type: Spectral
  url: rules/lemonway-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/json-ld/lemonway-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lemonway-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/vocabulary/lemonway-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lemonway-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/data-model/lemonway-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lemonway-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/security/lemonway-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lemonway-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/errors/lemonway-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lemonway-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/conformance/lemonway-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lemonway-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/llms/lemonway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lemonway-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/well-known/lemonway-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lemonway-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/hosts/lemonway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lemonway-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/vendors/lemonway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lemonway-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lemonway.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.lemonway.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.lemonway.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/authentication/lemonway-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lemonway-authentication.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/security/lemonway-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lemonway-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/security/lemonway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lemonway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lemonway.com/en
- group: other
  title: ''
  type: Developers
  url: https://www.lemonway.com/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.lemonway.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lemonway.com/en/pricing
- group: operate
  title: ''
  type: Status
  url: https://documentation.lemonway.com/page/api-status
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.lemonway.com/page/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.lemonway.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.lemonway.com/en/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemonway
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lemonwaysas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lemonway.com/en/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lemonway.com/en/privacy-policy
created: '2026-06-13'
description: Lemonway is a European payment institution regulated by the French ACPR (registration 16568) since 2012, providing REST APIs for marketplace payments including IBAN wallet creation, bank transfers, card payments, KYC/KYB verification, P2P transfers, and crowdfunding platform payment flows. Trusted by over 1,400 marketplaces across Europe.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemonway.png
json_schemas:
- name: CreateAccountResponse
  property_count: 3
  slug: lemonway-create-account-response
- name: CreateBnplPaymentInput
  property_count: 14
  slug: lemonway-create-bnpl-payment-input
- name: CreateIndividualAccountRequest
  property_count: 4
  slug: lemonway-create-individual-account-request
- name: CreateLegalEntityAccountRequest
  property_count: 5
  slug: lemonway-create-legal-entity-account-request
- name: CreateOnboardingCompanyRequest
  property_count: 5
  slug: lemonway-create-onboarding-company-request
- name: CreatePaymentFormInput
  property_count: 16
  slug: lemonway-create-payment-form-input
- name: CreateProfileRequest
  property_count: 4
  slug: lemonway-create-profile-request
- name: GetAccountResponse
  property_count: 12
  slug: lemonway-get-account-response
- name: MoneyInWebInitInput
  property_count: 18
  slug: lemonway-money-in-web-init-input
- name: RegisterIndividualAccountInput
  property_count: 15
  slug: lemonway-register-individual-account-input
- name: RegisterLegalAccountInput
  property_count: 16
  slug: lemonway-register-legal-account-input
- name: UploadDocumentInput
  property_count: 4
  slug: lemonway-upload-document-input
jsonld:
- class_count: 0
  name: Lemonway Context
  property_count: 7
  slug: lemonway-context
layout: provider
modified: '2026-06-13'
name: Lemonway
nav: Providers
network: true
overview: 'Lemonway publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Onboarding API, Accounts | Admin API, Accounts API, and 20 more. Tagged areas include Payments, Marketplace, IBAN, KYC, and Wallets.


  The Lemonway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lemonway''s developer surface includes authentication, documentation, pricing, status page, changelog, support, engineering blog, and 26 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 18
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Lemonway API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 3
  slug: lemonway-rules
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.8
    catalog_earned_first_party: 0.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.1
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 41.7
    discoverability: 80.4
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 22
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/screenshots/lemonway-2026-06-20T184419.png
security:
- kind: authentication
  name: Lemonway Authentication
  slug: lemonway-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lemonway Domain Security
  slug: lemonway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lemonway Vulnerability Disclosure
  slug: lemonway-vulnerability-disclosure
  summary_line: no policy recorded
slug: lemonway
tags:
- Payments
- Marketplace
- IBAN
- KYC
- Wallets
- Bank Transfers
- Card Payments
- Crowdfunding
- European
- PSD2
website: https://www.lemonway.com/en
---

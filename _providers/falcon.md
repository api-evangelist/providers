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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 67
  human_in_the_loop: 1
  name: Falcon Agentic Access
  operation_count: 119
  slug: falcon-agentic-access
  summary_line: 119 operations · 67 acting · 1 human-in-the-loop
api_count: 93
apis:
- description: Falcon's RESTful embedded-finance API for card issuance, lending, and program management. All responses are JSON; authentication is a JWT bearer token obtained from a client-id/client-secret login, wi
  name: Falcon API
  slug: falcon-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Account API from Falcon — 18 operation(s) for account.
  name: Falcon Account API
  slug: falcon-account-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Aggregator API from Falcon — 2 operation(s) for aggregator.
  name: Falcon Aggregator API
  slug: falcon-aggregator-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Balance API from Falcon — 1 operation(s) for balance.
  name: Falcon Balance API
  slug: falcon-balance-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Banking API from Falcon — 2 operation(s) for banking.
  name: Falcon Banking API
  slug: falcon-banking-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Card API from Falcon — 9 operation(s) for card.
  name: Falcon Card API
  slug: falcon-card-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Card Cvv API from Falcon — 1 operation(s) for card cvv.
  name: Falcon Card Cvv API
  slug: falcon-card-cvv-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Cc Open Api API from Falcon — 4 operation(s) for cc open api.
  name: Falcon Cc Open API
  slug: falcon-cc-open-api-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Close API from Falcon — 1 operation(s) for close.
  name: Falcon Close API
  slug: falcon-close-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Convert Emi API from Falcon — 1 operation(s) for convert emi.
  name: Falcon Convert Emi API
  slug: falcon-convert-emi-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Dispute API from Falcon — 4 operation(s) for dispute.
  name: Falcon Dispute API
  slug: falcon-dispute-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Due Date API from Falcon — 1 operation(s) for due date.
  name: Falcon Due Date API
  slug: falcon-due-date-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Emi Details API from Falcon — 1 operation(s) for emi details.
  name: Falcon Emi Details API
  slug: falcon-emi-details-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Emi Plan API from Falcon — 1 operation(s) for emi plan.
  name: Falcon Emi Plan API
  slug: falcon-emi-plan-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Employee API from Falcon — 1 operation(s) for employee.
  name: Falcon Employee API
  slug: falcon-employee-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Enterprise API from Falcon — 3 operation(s) for enterprise.
  name: Falcon Enterprise API
  slug: falcon-enterprise-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Enterprise Details API from Falcon — 1 operation(s) for enterprise details.
  name: Falcon Enterprise Details API
  slug: falcon-enterprise-details-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Enterprise Summary API from Falcon — 1 operation(s) for enterprise summary.
  name: Falcon Enterprise Summary API
  slug: falcon-enterprise-summary-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The FD API from Falcon — 1 operation(s) for fd.
  name: Falcon FD API
  slug: falcon-fd-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Fee API from Falcon — 6 operation(s) for fee.
  name: Falcon Fee API
  slug: falcon-fee-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Foreclose API from Falcon — 1 operation(s) for foreclose.
  name: Falcon Foreclose API
  slug: falcon-foreclose-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Foreclose Quote API from Falcon — 1 operation(s) for foreclose quote.
  name: Falcon Foreclose Quote API
  slug: falcon-foreclose-quote-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Initiate Payment API from Falcon — 1 operation(s) for initiate payment.
  name: Falcon Initiate Payment API
  slug: falcon-initiate-payment-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Interest API from Falcon — 2 operation(s) for interest.
  name: Falcon Interest API
  slug: falcon-interest-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Issuer API from Falcon — 4 operation(s) for issuer.
  name: Falcon Issuer API
  slug: falcon-issuer-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The List Emi API from Falcon — 1 operation(s) for list emi.
  name: Falcon List Emi API
  slug: falcon-list-emi-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Non Pci Card API from Falcon — 1 operation(s) for non pci card.
  name: Falcon Non Pci Card API
  slug: falcon-non-pci-card-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Npa API from Falcon — 1 operation(s) for npa.
  name: Falcon Npa API
  slug: falcon-npa-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Pci Card API from Falcon — 1 operation(s) for pci card.
  name: Falcon Pci Card API
  slug: falcon-pci-card-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Product API from Falcon — 4 operation(s) for product.
  name: Falcon Product API
  slug: falcon-product-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Program API from Falcon — 5 operation(s) for program.
  name: Falcon Program API
  slug: falcon-program-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Programs API from Falcon — 2 operation(s) for programs.
  name: Falcon Programs API
  slug: falcon-programs-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Repayment API from Falcon — 1 operation(s) for repayment.
  name: Falcon Repayment API
  slug: falcon-repayment-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Reward API from Falcon — 3 operation(s) for reward.
  name: Falcon Reward API
  slug: falcon-reward-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Statement API from Falcon — 2 operation(s) for statement.
  name: Falcon Statement API
  slug: falcon-statement-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Statement Past API from Falcon — 1 operation(s) for statement past.
  name: Falcon Statement Past API
  slug: falcon-statement-past-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Statementlist API from Falcon — 4 operation(s) for statementlist.
  name: Falcon Statementlist API
  slug: falcon-statementlist-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Transaction Eligibility API from Falcon — 1 operation(s) for transaction eligibility.
  name: Falcon Transaction Eligibility API
  slug: falcon-transaction-eligibility-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The Update Status Emi Plan API from Falcon — 1 operation(s) for update status emi plan.
  name: Falcon Update Status Emi Plan API
  slug: falcon-update-status-emi-plan-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The User API from Falcon — 8 operation(s) for user.
  name: Falcon User API
  slug: falcon-user-api
- baseURL: https://credituat.falconfs.com
  baseurl_source: declared
  description: The View Amortisation Schedules API from Falcon — 1 operation(s) for view amortisation schedules.
  name: Falcon View Amortisation Schedules API
  slug: falcon-view-amortisation-schedules-api
artifact_total: 64
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/agentic-access/falcon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/falcon-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/rules/falcon-rules.yml
  title: ''
  type: Spectral
  url: rules/falcon-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/json-ld/falcon-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/falcon-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/vocabulary/falcon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/falcon-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/data-model/falcon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/falcon-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/errors/falcon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/falcon-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/well-known/falcon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/falcon-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/hosts/falcon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/falcon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/vendors/falcon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/falcon-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/authentication/falcon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/falcon-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/conventions/falcon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/falcon-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/lifecycle/falcon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/falcon-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/conformance/falcon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/falcon-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/errors/falcon-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/falcon-error-codes.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/sandbox/falcon-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/falcon-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/security/falcon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/falcon-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/falcon/refs/heads/main/llms/falcon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/falcon-llms.txt
created: '2026-07-17'
description: 'Falcon (Falcon Financial Services, falconfs.com) is a global embedded-finance and Banking-as-a-Service platform that lets fintechs, banks, and enterprises launch credit and payment products in days rather than months. Its developer-first REST APIs and no-code tooling cover the full issuance and lending lifecycle: issuer and program onboarding, enterprise and user KYC, credit-card issuance (virtual, physical, add-on, co-branded, corporate), accounts and credit limits, transactions, statements, repayments and auto-debit, EMI conversion and amortisation, disputes, rewards, interest, fees, funding, and reconciliations. Falcon holds its own lending and issuance licenses, is built on a modular multi-tenant architecture, and is certified against PCI DSS, ISO 27001:2022, and SOC 2. Product lines include Falcon CardFX (issuance), CreditFX (lending), WalletFX (prepaid/wallets), and SurgeFX (AI growth and portfolio tools).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/falcon.png
json_schemas:
- name: AddCorporateAdminRequest
  property_count: 5
  slug: falcon-add-corporate-admin-request
- name: AddCorporateAdminResponse
  property_count: 1
  slug: falcon-add-corporate-admin-response
- name: Address
  property_count: 6
  slug: falcon-address
- name: EmployeeResponse
  property_count: 4
  slug: falcon-employee-response
- name: EnterpriseCreditLimitRequest
  property_count: 3
  slug: falcon-enterprise-credit-limit-request
- name: EnterpriseProgramActionRequest
  property_count: 4
  slug: falcon-enterprise-program-action-request
- name: EnterpriseRequest
  property_count: 19
  slug: falcon-enterprise-request
- name: EnterpriseResponse
  property_count: 2
  slug: falcon-enterprise-response
- name: EnterpriseSummaryRequest
  property_count: 3
  slug: falcon-enterprise-summary-request
- name: EnterpriseSummaryResponse
  property_count: 23
  slug: falcon-enterprise-summary-response
- name: EnterpriseUpdateRequest
  property_count: 9
  slug: falcon-enterprise-update-request
- name: FeeWaiver
  property_count: 2
  slug: falcon-fee-waiver
- name: ProductRequest
  property_count: 17
  slug: falcon-product-request
- name: ProductResponse
  property_count: 6
  slug: falcon-product-response
- name: SpendLimits
  property_count: 5
  slug: falcon-spend-limits
- name: SuccessResponse
  property_count: 0
  slug: falcon-success-response
- name: TransactionCategory
  property_count: 8
  slug: falcon-transaction-category
- name: TransactionLimits
  property_count: 5
  slug: falcon-transaction-limits
jsonld:
- class_count: 28
  name: Falcon Context
  property_count: 131
  slug: falcon-context
layout: provider
modified: '2026-07-19'
name: Falcon
nav: Providers
network: true
overview: 'Falcon publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Aggregator API, Balance API, and 38 more. Tagged areas include Company, Infrastructure, Financial Services, Banking, and Payments.


  The Falcon catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Falcon''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 21 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Falcon API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 5
  slug: falcon-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.2
  facets:
    access_clarity: 3.9
    contract_governance: 35.6
    contract_quality: 61.0
    developer_ergonomics: 32.1
    discoverability: 78.6
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 18.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 40
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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

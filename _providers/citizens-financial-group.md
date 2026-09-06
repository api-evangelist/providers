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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-05'
api_count: 12
apis:
- description: Citizens Open Banking API is the FDX-aligned API surface launched in Q1 2025 that gives business, commercial, wealth, and private- banking customers a single endpoint to share account balances, transa
  name: Citizens Open Banking API
  slug: citizens-open-banking-api
- baseURL: https://api.citizensbank.com/fdx/v1.0
  baseurl_source: declared
  description: The Citizens Accounts API is the FDX-aligned account surface - account list, account detail, transactions, contact and payment networks - for authorized retrieval of Citizens Bank customer account inf
  name: Citizens Accounts API
  slug: citizens-accounts-api
- baseURL: https://api.citizensbank.com/fdx/v1.0
  baseurl_source: declared
  description: The Citizens Statements API enables authorized retrieval of Citizens Bank customer monthly statements for personal financial management and document workflows. Two operations - list an account's state
  name: Citizens Statements API
  slug: citizens-statements-api
- baseURL: https://apis.citizensbank.com/v3/payments
  baseurl_source: declared
  description: The Citizens Payments API initiates RTP and ACH payment instructions, retrieves payment status, and checks whether a counterparty routing number is reachable on The Clearing House RTP network before a
  name: Citizens Payments API
  slug: citizens-payments-api
- baseURL: https://apis.citizensbank.com/v1/account-validation
  baseurl_source: declared
  description: The Citizens Account Validation API verifies a payee's account number, routing number and beneficiary name before an irrevocable payment is sent, returning an account status (open, closed, unverified,
  name: Citizens Account Validation API
  slug: citizens-account-validation-api
- baseURL: https://apis.citizensbank.com/v1/account-transfer
  baseurl_source: declared
  description: The Citizens Account Transfer API moves funds near real-time between accounts a client already holds at Citizens. Single same-day transfers only - batch and future-dated transfers are not supported in
  name: Citizens Account Transfer API
  slug: citizens-account-transfer-api
- baseURL: https://apis.citizensbank.com/v1/information-reporting
  baseurl_source: declared
  description: The Citizens Information Reporting API lets an authenticated consumer retrieve the authorized account list, deposit account balances and transaction history for Citizens Bank checking and savings acco
  name: Citizens Information Reporting API
  slug: citizens-information-reporting-api
- baseURL: https://api.citizensbank.com/authorize/v1.0
  baseurl_source: declared
  description: The Citizens Authorize API is the Citizens identity provider that authenticates a partner and grants access to bank resources such as accounts and transactions. The published contract declares only th
  name: Citizens Authorize API
  slug: citizens-authorize-api
- baseURL: https://sandboxapi.citizensbank.com/v1/atm-locator
  baseurl_source: declared
  description: The Citizens ATM Locator API enables searching for Citizens Bank ATMs throughout the USA using zip code, street address, or geographical coordinates, returning location, hours of operation and whether
  name: Citizens ATM Locator API
  slug: citizens-atm-locator-api
- baseURL: https://sandboxapi.citizensbank.com/v1/branch-locator
  baseurl_source: declared
  description: The Citizens Branch Locator API enables searching for Citizens Bank branches throughout the USA using zip code, street address, geographical coordinates or routing number. Like the ATM Locator it is p
  name: Citizens Branch Locator API
  slug: citizens-branch-locator-api
- description: Citizens Pay is the buy-now-pay-later embedded financing platform offered by Citizens Bank. The Citizens Pay developer portal that previously exposed merchant integration, underwriting and installment
  name: Citizens Pay API
  slug: citizens-pay-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.citizensbank.com
- group: start
  title: ''
  type: Portal
  url: https://developer.citizensbank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.citizensbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.citizensbank.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.citizensbank.com/product
- group: start
  title: ''
  type: Sandbox
  url: https://sandboxdeveloper.citizensbank.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.citizensbank.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.citizensbank.com/customer-service/contact-us.aspx
- group: start
  title: ''
  type: Login
  url: https://developer.citizensbank.com/user/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rbs-citizens-financial-group
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.citizensbank.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://investor.citizensbank.com/about-us/newsroom/latest-news/2025/2025-03-27.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citizensbank.com/account-safeguards/privacy.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.citizensbank.com/account-safeguards/terms-of-use.aspx
- group: auth
  title: ''
  type: Authentication
  url: authentication/citizens-financial-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/citizens-financial-group-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/citizens-financial-group-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/citizens-financial-group-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/citizens-financial-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/citizens-financial-group-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/citizens-financial-group-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/citizens-financial-group-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/citizens-financial-group-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/citizens-financial-group-decline-codes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/citizens-financial-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/citizens-financial-group-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/citizens-financial-group-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citizens-financial-group-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/citizens-financial-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/citizens-financial-group-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/citizens-financial-group-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/citizens-financial-group-mcp.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/citizens-financial-group-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/citizens-financial-group-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/citizens-financial-group-rules.yml
created: '2026-03-23'
description: 'Citizens Financial Group is one of the oldest and largest financial institutions in the United States, serving individuals, small businesses, middle-market companies and large corporations through Citizens Bank and its subsidiaries. Citizens runs a public IBM API Connect developer portal at developer.citizensbank.com, with a matching sandbox at sandboxdeveloper.citizensbank.com, publishing twelve machine-readable contracts across four surfaces: an FDX-aligned account and statement surface, a commercial-banking surface (RTP and ACH payments, account validation, information reporting, internal transfer), an identity/authorize surface, and ATM and branch locators. The FDX Open Banking API launched in Q1 2025 gives business, commercial, wealth and private-banking customers one endpoint for sharing account and transaction data with authorized third parties. Access is partner-gated throughout, and sandbox testing is mandatory.'
finops:
- name: Citizens Financial Group Finops
  service_category: Banking
  slug: citizens-financial-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citizens-financial-group.png
jsonld:
- class_count: 18
  name: Citizens Financial Group Context
  property_count: 0
  slug: citizens-financial-group-context
layout: provider
modified: '2026-09-05'
name: Citizens Financial Group
nav: Providers
network: true
overview: 'Citizens Financial Group publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Citizens Accounts API, Citizens Statements API, Citizens Payments API, and 6 more. Tagged areas include Banking, Buy Now Pay Later, Financial-Services, FDX, and Locator.


  The Citizens Financial Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citizens Financial Group''s developer surface includes developer portal, documentation, API reference, sandbox, support, authentication, and 30 more developer resources.'
plans:
- name: Citizens Financial Group Plans Pricing
  plan_count: 11
  slug: citizens-financial-group-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 8
  name: Citizens Financial Group Rate Limits
  slug: citizens-financial-group-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Citizens Financial Group API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: citizens-financial-group-rules
scopes:
- name: Citizens Financial Group Scopes
  scope_count: 5
  slug: citizens-financial-group-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 65.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 85.0
    catalog_earned_first_party: 24.0
    catalog_gap: 30.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 41.2
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 63.6
    contract_quality: 52.0
    developer_ergonomics: 51.8
    discoverability: 64.8
    governance: 63.6
    operational_transparency: 42.1
  previous_composite: 23.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 88.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/citizens-financial-group/refs/heads/main/screenshots/citizens-financial-group-2026-06-20T174413.png
security:
- kind: authentication
  name: Citizens Financial Group Authentication
  slug: citizens-financial-group-authentication
  summary_line: oauth2/apiKey/mutualTLS · 5 schemes
- kind: domain-security
  name: Citizens Financial Group Domain Security
  slug: citizens-financial-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Citizens Financial Group Vulnerability Disclosure
  slug: citizens-financial-group-vulnerability-disclosure
  summary_line: disclosure policy published
slug: citizens-financial-group
tags:
- Banking
- Buy Now Pay Later
- Financial-Services
- FDX
- Locator
- Open Banking
- Payments
website: https://www.citizensbank.com
---

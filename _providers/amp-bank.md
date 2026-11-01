---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amp Bank Agentic Access
  operation_count: 19
  slug: amp-bank-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: AMP Bank Banking Account Balances API
  slug: amp-bank-banking-account-balances-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: AMP Bank Banking Account Direct Debits API
  slug: amp-bank-banking-account-direct-debits-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: AMP Bank Banking Account Scheduled Payments API
  slug: amp-bank-banking-account-scheduled-payments-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: AMP Bank Banking Account Transactions API
  slug: amp-bank-banking-account-transactions-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account endpoints
  name: AMP Bank Banking Accounts API
  slug: amp-bank-banking-accounts-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Payee endpoints
  name: AMP Bank Banking Payees API
  slug: amp-bank-banking-payees-api
- baseURL: https://pub.cdr-sme.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: 'Public Consumer Data Right Product Reference Data endpoints (GET /banking/products and /banking/products/{productId}) for the AMP Bank - Mobile banking (AMP Bank GO) brand, as published on AMP''s open '
  name: AMP Bank GO Banking Products API
  slug: amp-bank-go-banking-products-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: AMP Bank Banking Products API
  slug: amp-bank-banking-products-api
artifact_total: 43
collections:
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-amp-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-amp-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-amp-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-amp-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-amp-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-amp-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-amp-bank-banking-products-api
common:
- group: auth
  href: https://artifacts.apis.io/amp-bank/authentication/amp-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amp-bank-authentication.yml
- group: agent
  href: https://artifacts.apis.io/amp-bank/agentic-access/amp-bank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amp-bank-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/amp-bank/rate-limits/amp-bank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amp-bank-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/amp-bank/rules/amp-bank-rules.yml
  title: ''
  type: Spectral
  url: rules/amp-bank-rules.yml
- group: design
  href: https://artifacts.apis.io/amp-bank/json-ld/amp-bank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amp-bank-context.jsonld
- group: design
  href: https://artifacts.apis.io/amp-bank/vocabulary/amp-bank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amp-bank-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/amp-bank/overlays/amp-bank-banking-account-balances-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amp-bank-banking-account-balances-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/amp-bank/hosts/amp-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amp-bank-hosts.yml
- group: build
  href: https://artifacts.apis.io/amp-bank/integrations/amp-bank-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/amp-bank-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/amp-bank/vendors/amp-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amp-bank-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amp.com.au/investments/pricing-and-performance
- group: company
  title: ''
  type: Newsroom
  url: https://www.amp.com.au/about-amp/news
- group: company
  title: ''
  type: Blog
  url: https://www.amp.com.au/about-amp/news
- group: other
  href: https://artifacts.apis.io/amp-bank/capabilities/amp-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amp-bank-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/amp-bank/security/amp-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amp-bank-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amp-bank/security/amp-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amp-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amp.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.amp.com.au/personal-banking/open-banking/open-banking-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.amp.com.au/personal-banking/open-banking/open-banking-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.amp.com.au/personal-banking/open-banking/open-banking-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amp.com.au/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amp.com.au/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.amp.com.au/help-and-support
- group: start
  title: ''
  type: Login
  url: https://secure.amp.com.au/public/login
- group: auth
  title: ''
  type: Security
  url: https://www.amp.com.au/help-and-support/security
- group: other
  title: ''
  type: HackerOne
  url: https://hackerone.com/ampau
- group: auth
  href: https://artifacts.apis.io/amp-bank/scopes/amp-bank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/amp-bank-scopes.yml
- group: design
  href: https://artifacts.apis.io/amp-bank/conventions/amp-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amp-bank-conventions.yml
- group: design
  href: https://artifacts.apis.io/amp-bank/errors/amp-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amp-bank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amp-bank/lifecycle/amp-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amp-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  href: https://artifacts.apis.io/amp-bank/conformance/amp-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amp-bank-conformance.yml
- group: design
  href: https://artifacts.apis.io/amp-bank/data-model/amp-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amp-bank-data-model.yml
- group: agent
  href: https://artifacts.apis.io/amp-bank/mcp/amp-bank-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amp-bank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/amp-bank/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/amp-bank/well-known/amp-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amp-bank-well-known.yml
- group: auth
  href: https://artifacts.apis.io/amp-bank/well-known/amp-bank-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amp-bank-security.txt
created: '2026-07-20'
description: AMP Bank Limited is the retail and business banking arm of AMP Limited (ASX:AMP), a diversified Australian financial services group operating since 1849 and headquartered in Sydney. AMP Bank is a publicly listed (shareholder-owned, not a mutual) authorised deposit-taking institution (ADI) regulated by APRA, offering home loans, deposit and savings accounts, and the digital AMP Bank GO small-business and everyday banking brand. As an active ADI, AMP participates in Australia's Consumer Data Right (CDR / Open Banking) regime and exposes public, unauthenticated Product Reference Data (PRD) APIs conforming to the DSB Consumer Data Standards, alongside the accredited, FAPI-secured consumer data sharing surface used by authorised data recipients.
examples:
- key_count: 3
  name: Amp Bank Banking Products Live Response
  slug: amp-bank-banking-products-live-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amp-bank.png
json_schemas:
- name: ResponseBankingAccountByIdV5
  property_count: 3
  slug: amp-bank-response-banking-account-by-id-v5
- name: ResponseBankingAccountListV3
  property_count: 3
  slug: amp-bank-response-banking-account-list-v3
- name: ResponseBankingAccountsBalanceById
  property_count: 3
  slug: amp-bank-response-banking-accounts-balance-by-id
- name: ResponseBankingAccountsBalanceList
  property_count: 3
  slug: amp-bank-response-banking-accounts-balance-list
- name: ResponseBankingDirectDebitAuthorisationList
  property_count: 3
  slug: amp-bank-response-banking-direct-debit-authorisation-list
- name: ResponseBankingInstalmentPlanList
  property_count: 3
  slug: amp-bank-response-banking-instalment-plan-list
- name: ResponseBankingPayeeByIdV2
  property_count: 3
  slug: amp-bank-response-banking-payee-by-id-v2
- name: ResponseBankingPayeeListV2
  property_count: 3
  slug: amp-bank-response-banking-payee-list-v2
- name: ResponseBankingProductByIdV7
  property_count: 3
  slug: amp-bank-response-banking-product-by-id-v7
- name: ResponseBankingProductListV4
  property_count: 3
  slug: amp-bank-response-banking-product-list-v4
- name: ResponseBankingScheduledPaymentsListV2
  property_count: 3
  slug: amp-bank-response-banking-scheduled-payments-list-v2
- name: ResponseBankingTransactionByIdV3
  property_count: 3
  slug: amp-bank-response-banking-transaction-by-id-v3
- name: ResponseBankingTransactionListV2
  property_count: 3
  slug: amp-bank-response-banking-transaction-list-v2
jsonld:
- class_count: 95
  name: Amp Bank Context
  property_count: 280
  slug: amp-bank-context
layout: provider
modified: '2026-10-20'
name: AMP Bank
nav: Providers
network: true
overview: 'AMP Bank publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 5 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Banking.


  The AMP Bank catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AMP Bank''s developer surface includes authentication, pricing, engineering blog, documentation, getting-started guide, support, and 32 more developer resources.'
plans:
- name: Amp Bank Plans Pricing
  plan_count: 0
  slug: amp-bank-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 8
  name: Amp Bank Rate Limits
  slug: amp-bank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: AMP Bank API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: amp-bank-rules
scopes:
- name: Amp Bank Scopes
  scope_count: 5
  slug: amp-bank-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 61.6
    developer_ergonomics: 58.9
    discoverability: 67.9
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 37.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amp-bank/amp-bank-2026-07-21T114657.png
security:
- kind: authentication
  name: Amp Bank Authentication
  slug: amp-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Amp Bank Domain Security
  slug: amp-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Amp Bank Vulnerability Disclosure
  slug: amp-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: amp-bank-list-payees
  slug: amp-bank-list-payees
- name: amp-bank-lookup-products
  slug: amp-bank-lookup-products
- name: amp-bank-read-account-balances
  slug: amp-bank-read-account-balances
- name: amp-bank-review-regular-payments
  slug: amp-bank-review-regular-payments
- name: amp-bank-review-transactions
  slug: amp-bank-review-transactions
slug: amp-bank
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.amp.com.au/
---

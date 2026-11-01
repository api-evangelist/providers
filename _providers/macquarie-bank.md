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
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Macquarie Bank Agentic Access
  operation_count: 19
  slug: macquarie-bank-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- description: Macquarie's connectivity / data APIs for business, documented through the registered Macquarie developer portal, let approved businesses and software partners automate account information retrieval an
  name: Macquarie Connectivity & Data API
  slug: macquarie-connectivity-data-api
- description: Macquarie's DEFT payments platform, surfaced through the registered Macquarie developer portal, lets businesses build branded payment experiences with tokenised credit card, bank account and direct de
  name: Macquarie DEFT Payments API
  slug: macquarie-deft-payments-api
- baseURL: https://api.macquariebank.io/cds-au/v1
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Macquarie Bank Banking Account Balances API
  slug: macquarie-bank-banking-account-balances-api
- baseURL: https://api.macquariebank.io/cds-au/v1
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Macquarie Bank Banking Account Direct Debits API
  slug: macquarie-bank-banking-account-direct-debits-api
- baseURL: https://api.macquariebank.io/cds-au/v1
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Macquarie Bank Banking Account Scheduled Payments API
  slug: macquarie-bank-banking-account-scheduled-payments-api
- baseURL: https://api.macquariebank.io/cds-au/v1
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Macquarie Bank Banking Account Transactions API
  slug: macquarie-bank-banking-account-transactions-api
- baseURL: https://api.macquariebank.io/cds-au/v1
  baseurl_source: declared
  description: Banking Account endpoints
  name: Macquarie Bank Banking Accounts API
  slug: macquarie-bank-banking-accounts-api
- baseURL: https://api.macquariebank.io/cds-au/v1
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Macquarie Bank Banking Payees API
  slug: macquarie-bank-banking-payees-api
- baseURL: https://api.macquariebank.io/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: Macquarie Bank Banking Products API
  slug: macquarie-bank-banking-products-api
artifact_total: 43
collections:
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-macquarie-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-macquarie-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-macquarie-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-macquarie-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-macquarie-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-macquarie-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-macquarie-bank-banking-products-api
common:
- group: operate
  href: https://artifacts.apis.io/macquarie-bank/rate-limits/macquarie-bank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/macquarie-bank-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/macquarie-bank/rules/macquarie-bank-rules.yml
  title: ''
  type: Spectral
  url: rules/macquarie-bank-rules.yml
- group: design
  href: https://artifacts.apis.io/macquarie-bank/json-ld/macquarie-bank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/macquarie-bank-context.jsonld
- group: design
  href: https://artifacts.apis.io/macquarie-bank/vocabulary/macquarie-bank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/macquarie-bank-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/macquarie-bank/overlays/macquarie-bank-banking-account-balances-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/macquarie-bank-banking-account-balances-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/macquarie-bank/hosts/macquarie-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/macquarie-bank-hosts.yml
- group: build
  href: https://artifacts.apis.io/macquarie-bank/integrations/macquarie-bank-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/macquarie-bank-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/macquarie-bank/vendors/macquarie-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/macquarie-bank-vendors.yml
- group: other
  href: https://artifacts.apis.io/macquarie-bank/capabilities/macquarie-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/macquarie-bank-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/macquarie-bank/security/macquarie-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/macquarie-bank-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/macquarie-bank/agentic-access/macquarie-bank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/macquarie-bank-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/macquarie-bank/authentication/macquarie-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/macquarie-bank-authentication.yml
- group: auth
  href: https://artifacts.apis.io/macquarie-bank/scopes/macquarie-bank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/macquarie-bank-scopes.yml
- group: design
  href: https://artifacts.apis.io/macquarie-bank/conformance/macquarie-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/macquarie-bank-conformance.yml
- group: design
  href: https://artifacts.apis.io/macquarie-bank/errors/macquarie-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/macquarie-bank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/macquarie-bank/lifecycle/macquarie-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/macquarie-bank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.macquariebank.io/cds-au/v1/discovery/status
- group: operate
  href: https://artifacts.apis.io/macquarie-bank/lifecycle/macquarie-bank-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/macquarie-bank-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/macquarie-bank/conventions/macquarie-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/macquarie-bank-conventions.yml
- group: design
  href: https://artifacts.apis.io/macquarie-bank/data-model/macquarie-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/macquarie-bank-data-model.yml
- group: agent
  href: https://artifacts.apis.io/macquarie-bank/mcp/macquarie-bank-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/macquarie-bank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/macquarie-bank/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/macquarie-bank/sandbox/macquarie-bank-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/macquarie-bank-sandbox.yml
- group: company
  title: ''
  type: Website
  url: https://www.macquarie.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.macquariebank.io/devportal/
- group: docs
  title: ''
  type: Documentation
  url: https://www.macquarie.com.au/digital-banking/open-banking.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/macquariegroup/
- group: start
  title: ''
  type: CDRRegister
  url: https://www.cdr.gov.au/find-a-provider
- group: operate
  title: ''
  type: Support
  url: https://www.macquarie.com.au/help/personal.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.macquarie.com.au/newsroom.html
- group: operate
  title: ''
  type: Contact
  url: https://www.macquarie.com.au/contact-us.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.macquarie.com.au/privacy-and-cookies.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.macquarie.com.au/important-information.html
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-banking-api
- group: auth
  href: https://artifacts.apis.io/macquarie-bank/security/macquarie-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/macquarie-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.macquarie.com/us/en/disclosures/cybersecurity.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.macquarie.com/us/en/disclosures/cybersecurity.html
- group: start
  title: ''
  type: SignUp
  url: https://developer.macquariebank.io/devportal/
created: '2026-07-20'
description: Macquarie Bank Limited is an Australian authorised deposit-taking institution (ADI) and the retail and business banking arm of Macquarie Group Limited, the ASX-listed (ASX:MQG) global financial services group headquartered in Sydney. It is not a mutual or customer-owned bank; it is a wholly-owned, shareholder-owned subsidiary of a publicly listed parent. Its digital bank offers transaction and savings accounts, home loans, credit and charge cards, term deposits, overdrafts and business lending. As a designated data holder under Australia's Consumer Data Right (CDR / Open Banking), Macquarie Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards (CDS), alongside accredited-data-recipient data sharing and a registered developer portal that documents its DEFT payments platform.
examples:
- key_count: 3
  name: Macquarie Bank Banking Products List Response
  slug: macquarie-bank-banking-products-list-response
- key_count: 3
  name: Macquarie Bank Discovery Status Response
  slug: macquarie-bank-discovery-status-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/macquarie-bank.png
json_schemas:
- name: ResponseBankingAccountByIdV5
  property_count: 3
  slug: macquarie-bank-response-banking-account-by-id-v5
- name: ResponseBankingAccountListV3
  property_count: 3
  slug: macquarie-bank-response-banking-account-list-v3
- name: ResponseBankingAccountsBalanceById
  property_count: 3
  slug: macquarie-bank-response-banking-accounts-balance-by-id
- name: ResponseBankingAccountsBalanceList
  property_count: 3
  slug: macquarie-bank-response-banking-accounts-balance-list
- name: ResponseBankingDirectDebitAuthorisationList
  property_count: 3
  slug: macquarie-bank-response-banking-direct-debit-authorisation-list
- name: ResponseBankingInstalmentPlanList
  property_count: 3
  slug: macquarie-bank-response-banking-instalment-plan-list
- name: ResponseBankingPayeeByIdV2
  property_count: 3
  slug: macquarie-bank-response-banking-payee-by-id-v2
- name: ResponseBankingPayeeListV2
  property_count: 3
  slug: macquarie-bank-response-banking-payee-list-v2
- name: ResponseBankingProductByIdV7
  property_count: 3
  slug: macquarie-bank-response-banking-product-by-id-v7
- name: ResponseBankingProductListV4
  property_count: 3
  slug: macquarie-bank-response-banking-product-list-v4
- name: ResponseBankingScheduledPaymentsListV2
  property_count: 3
  slug: macquarie-bank-response-banking-scheduled-payments-list-v2
- name: ResponseBankingTransactionByIdV3
  property_count: 3
  slug: macquarie-bank-response-banking-transaction-by-id-v3
- name: ResponseBankingTransactionListV2
  property_count: 3
  slug: macquarie-bank-response-banking-transaction-list-v2
jsonld:
- class_count: 95
  name: Macquarie Bank Context
  property_count: 280
  slug: macquarie-bank-context
layout: provider
modified: '2026-10-20'
name: Macquarie Bank
nav: Providers
network: true
overview: 'Macquarie Bank publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 6 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Data Right.


  The Macquarie Bank catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Macquarie Bank''s developer surface includes authentication, sandbox, documentation, support, API reference, signup flow, and 32 more developer resources.'
plans:
- name: Macquarie Bank Plans Pricing
  plan_count: 0
  slug: macquarie-bank-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 13
  name: Macquarie Bank Rate Limits
  slug: macquarie-bank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Macquarie Bank API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: macquarie-bank-rules
scopes:
- name: Macquarie Bank Scopes
  scope_count: 10
  slug: macquarie-bank-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 58.3
    developer_ergonomics: 51.8
    discoverability: 58.9
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 54.4
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
    score: 46.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/macquarie-bank/macquarie-bank-2026-07-21T130910.png
security:
- kind: authentication
  name: Macquarie Bank Authentication
  slug: macquarie-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Macquarie Bank Domain Security
  slug: macquarie-bank-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Macquarie Bank Vulnerability Disclosure
  slug: macquarie-bank-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
skill_count: 3
skills:
- name: macquarie-bank-list-banking-products
  slug: macquarie-bank-list-banking-products
- name: macquarie-bank-review-payment-obligations
  slug: macquarie-bank-review-payment-obligations
- name: macquarie-bank-share-account-data
  slug: macquarie-bank-share-account-data
slug: macquarie-bank
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Product Reference Data
- Payments
website: https://www.macquarie.com.au/
---

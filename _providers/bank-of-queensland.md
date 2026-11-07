---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bank Of Queensland Agentic Access
  operation_count: 19
  slug: bank-of-queensland-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Balance endpoints
  name: Bank of Queensland Banking Account Balances API
  slug: bank-of-queensland-banking-account-balances-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Direct Debit endpoints
  name: Bank of Queensland Banking Account Direct Debits API
  slug: bank-of-queensland-banking-account-direct-debits-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Scheduled Payment endpoints
  name: Bank of Queensland Banking Account Scheduled Payments API
  slug: bank-of-queensland-banking-account-scheduled-payments-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Transaction endpoints
  name: Bank of Queensland Banking Account Transactions API
  slug: bank-of-queensland-banking-account-transactions-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account endpoints
  name: Bank of Queensland Banking Accounts API
  slug: bank-of-queensland-banking-accounts-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Payee endpoints
  name: Bank of Queensland Banking Payees API
  slug: bank-of-queensland-banking-payees-api
- baseURL: https://api.cds.boq.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: Bank of Queensland Banking Products API
  slug: bank-of-queensland-banking-products-api
artifact_total: 37
collections:
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-bank-of-queensland-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-bank-of-queensland-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-bank-of-queensland-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-bank-of-queensland-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-bank-of-queensland-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-bank-of-queensland-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-bank-of-queensland-banking-products-api
common:
- group: operate
  href: https://artifacts.apis.io/bank-of-queensland/rate-limits/bank-of-queensland-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bank-of-queensland-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/rules/bank-of-queensland-rules.yml
  title: ''
  type: Spectral
  url: rules/bank-of-queensland-rules.yml
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/json-ld/bank-of-queensland-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bank-of-queensland-context.jsonld
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/vocabulary/bank-of-queensland-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bank-of-queensland-vocabulary.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: other
  href: https://artifacts.apis.io/bank-of-queensland/overlays/bank-of-queensland-banking-account-balances-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bank-of-queensland-banking-account-balances-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/bank-of-queensland/hosts/bank-of-queensland-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bank-of-queensland-hosts.yml
- group: build
  href: https://artifacts.apis.io/bank-of-queensland/integrations/bank-of-queensland-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/bank-of-queensland-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/bank-of-queensland/vendors/bank-of-queensland-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bank-of-queensland-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://internetbanking.boq.com.au/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.boq.com.au/personal/help-and-support/business/getting-started-business
- group: company
  title: ''
  type: Blog
  url: https://www.boq.com.au/blog/
- group: other
  href: https://artifacts.apis.io/bank-of-queensland/capabilities/bank-of-queensland-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bank-of-queensland-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bank-of-queensland/agentic-access/bank-of-queensland-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-queensland-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bank-of-queensland/scopes/bank-of-queensland-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-queensland-scopes.yml
- group: auth
  href: https://artifacts.apis.io/bank-of-queensland/security/bank-of-queensland-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bank-of-queensland-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bank-of-queensland/authentication/bank-of-queensland-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bank-of-queensland-authentication.yml
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/conventions/bank-of-queensland-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bank-of-queensland-conventions.yml
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/errors/bank-of-queensland-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-queensland-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/conformance/bank-of-queensland-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bank-of-queensland-conformance.yml
- group: auth
  href: https://artifacts.apis.io/bank-of-queensland/conformance/bank-of-queensland-conformance.yml
  title: ''
  type: Compliance
  url: conformance/bank-of-queensland-conformance.yml
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/lifecycle/bank-of-queensland-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-queensland-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bank-of-queensland/data-model/bank-of-queensland-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bank-of-queensland-data-model.yml
- group: agent
  href: https://artifacts.apis.io/bank-of-queensland/mcp/bank-of-queensland-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bank-of-queensland-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bank-of-queensland/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.boq.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.boq.com.au/personal/help-and-support/forms-and-important-information/open-banking
- group: operate
  title: ''
  type: Support
  url: https://www.boq.com.au/personal/help-and-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boq.com.au/personal/help-and-support/forms-and-important-information/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boq.com.au/personal/help-and-support/forms-and-important-information/terms-and-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-queensland
created: '2026-07-20'
description: Bank of Queensland Limited (ASX code BOQ) is one of Australia's oldest banks, founded in Brisbane in 1874, and today an APRA-regulated authorised deposit-taking institution (ADI) and ASX-listed regional retail and commercial bank - a publicly listed company, not a customer-owned mutual. Its banking group includes the ME Bank, Virgin Money Australia and BOQ Specialist brands. As an accredited Consumer Data Right (CDR) data holder, BOQ exposes a public, unauthenticated Product Reference Data (PRD) API that conforms to the Australian Consumer Data Standards, while consumer data sharing runs through the regulated CDR / Accredited Data Recipient (ADR) model with OAuth2 / OIDC (FAPI) authorization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-queensland.png
json_schemas:
- name: ResponseBankingAccountByIdV5
  property_count: 3
  slug: bank-of-queensland-response-banking-account-by-id-v5
- name: ResponseBankingAccountListV3
  property_count: 3
  slug: bank-of-queensland-response-banking-account-list-v3
- name: ResponseBankingAccountsBalanceById
  property_count: 3
  slug: bank-of-queensland-response-banking-accounts-balance-by-id
- name: ResponseBankingAccountsBalanceList
  property_count: 3
  slug: bank-of-queensland-response-banking-accounts-balance-list
- name: ResponseBankingDirectDebitAuthorisationList
  property_count: 3
  slug: bank-of-queensland-response-banking-direct-debit-authorisation-list
- name: ResponseBankingInstalmentPlanList
  property_count: 3
  slug: bank-of-queensland-response-banking-instalment-plan-list
- name: ResponseBankingPayeeByIdV2
  property_count: 3
  slug: bank-of-queensland-response-banking-payee-by-id-v2
- name: ResponseBankingPayeeListV2
  property_count: 3
  slug: bank-of-queensland-response-banking-payee-list-v2
- name: ResponseBankingProductByIdV7
  property_count: 3
  slug: bank-of-queensland-response-banking-product-by-id-v7
- name: ResponseBankingProductListV4
  property_count: 3
  slug: bank-of-queensland-response-banking-product-list-v4
- name: ResponseBankingScheduledPaymentsListV2
  property_count: 3
  slug: bank-of-queensland-response-banking-scheduled-payments-list-v2
- name: ResponseBankingTransactionByIdV3
  property_count: 3
  slug: bank-of-queensland-response-banking-transaction-by-id-v3
- name: ResponseBankingTransactionListV2
  property_count: 3
  slug: bank-of-queensland-response-banking-transaction-list-v2
jsonld:
- class_count: 95
  name: Bank Of Queensland Context
  property_count: 280
  slug: bank-of-queensland-context
layout: provider
modified: '2026-10-20'
name: Bank of Queensland
nav: Providers
network: true
overview: 'Bank of Queensland publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Banking.


  The Bank of Queensland catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bank of Queensland''s developer surface includes getting-started guide, engineering blog, authentication, documentation, support, and 26 more developer resources.'
plans:
- name: Bank Of Queensland Plans Pricing
  plan_count: 0
  slug: bank-of-queensland-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Bank Of Queensland Rate Limits
  slug: bank-of-queensland-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Bank of Queensland API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: bank-of-queensland-rules
scopes:
- name: Bank Of Queensland Scopes
  scope_count: 9
  slug: bank-of-queensland-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 30.3
    contract_governance: 35.6
    contract_quality: 58.3
    developer_ergonomics: 36.3
    discoverability: 64.3
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
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
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bank-of-queensland/bank-of-queensland-2026-07-21T114702.png
security:
- kind: authentication
  name: Bank Of Queensland Authentication
  slug: bank-of-queensland-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Bank Of Queensland Domain Security
  slug: bank-of-queensland-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: bank-of-queensland-cdr-account-data
  slug: bank-of-queensland-cdr-account-data
- name: bank-of-queensland-product-reference
  slug: bank-of-queensland-product-reference
slug: bank-of-queensland
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.boq.com.au/
---

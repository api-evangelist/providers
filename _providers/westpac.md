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
    agentic_access: derived
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
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Westpac Agentic Access
  operation_count: 19
  slug: westpac-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- description: First-party Westpac payment API (beyond CDR). PayWay is Westpac's merchant payment platform; its public REST API v1 processes real-time credit-card and bank-account payments, refunds, pre-authorisatio
  name: Westpac PayWay REST API
  slug: westpac-payway-rest-api
- description: First-party Westpac payment API (beyond CDR). QuickStream is Westpac's online payment gateway; its public REST API v1 exposes Transactions, Customers, Accounts, Credit Cards, Recurring Payments, PayID
  name: Westpac QuickStream REST API
  slug: westpac-quickstream-rest-api
- baseURL: https://digital-api.westpac.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Westpac Banking Corporation Banking Account Balances API
  slug: westpac-banking-account-balances-api
- baseURL: https://digital-api.westpac.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Westpac Banking Corporation Banking Account Direct Debits API
  slug: westpac-banking-account-direct-debits-api
- baseURL: https://digital-api.westpac.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Westpac Banking Corporation Banking Account Scheduled Payments API
  slug: westpac-banking-account-scheduled-payments-api
- baseURL: https://digital-api.westpac.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Westpac Banking Corporation Banking Account Transactions API
  slug: westpac-banking-account-transactions-api
- baseURL: https://digital-api.westpac.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account endpoints
  name: Westpac Banking Corporation Banking Accounts API
  slug: westpac-banking-accounts-api
- baseURL: https://digital-api.westpac.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Westpac Banking Corporation Banking Payees API
  slug: westpac-banking-payees-api
- baseURL: https://digital-api.westpac.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: Westpac Banking Corporation Banking Products API
  slug: westpac-banking-products-api
artifact_total: 41
collections:
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-westpac-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-westpac-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-westpac-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-westpac-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-westpac-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-westpac-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-westpac-banking-products-api
common:
- group: agent
  href: https://artifacts.apis.io/westpac/agentic-access/westpac-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/westpac-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/westpac/rate-limits/westpac-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/westpac-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/westpac/rules/westpac-rules.yml
  title: ''
  type: Spectral
  url: rules/westpac-rules.yml
- group: design
  href: https://artifacts.apis.io/westpac/json-ld/westpac-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/westpac-context.jsonld
- group: design
  href: https://artifacts.apis.io/westpac/vocabulary/westpac-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/westpac-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/westpac/conventions/westpac-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/westpac-conventions.yml
- group: auth
  href: https://artifacts.apis.io/westpac/scopes/westpac-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/westpac-scopes.yml
- group: operate
  href: https://artifacts.apis.io/westpac/lifecycle/westpac-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/westpac-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://qvalent.statuspage.io/
- group: design
  href: https://artifacts.apis.io/westpac/errors/westpac-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/westpac-error-codes.yml
- group: other
  href: https://artifacts.apis.io/westpac/overlays/westpac-banking-account-balances-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/westpac-banking-account-balances-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/westpac/hosts/westpac-hosts.yml
  title: ''
  type: Hosts
  url: hosts/westpac-hosts.yml
- group: build
  href: https://artifacts.apis.io/westpac/integrations/westpac-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/westpac-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/westpac/vendors/westpac-vendors.yml
  title: ''
  type: Vendors
  url: vendors/westpac-vendors.yml
- group: build
  href: https://artifacts.apis.io/westpac/packages/westpac-packages.yml
  title: ''
  type: SDKs
  url: packages/westpac-packages.yml
- group: build
  href: https://artifacts.apis.io/westpac/packages/westpac-packages.yml
  title: ''
  type: Packages
  url: packages/westpac-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://www.westpac.com.au/news/
- group: other
  href: https://artifacts.apis.io/westpac/capabilities/westpac-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/westpac-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/westpac/security/westpac-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/westpac-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/westpac/security/westpac-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/westpac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.westpac.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.westpac.com.au/about-westpac/innovation/open-banking/
- group: docs
  title: ''
  type: Documentation
  url: https://www.westpac.com.au/about-westpac/innovation/open-banking/product-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/westpac
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/westpac
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westpac.com.au/privacy/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westpac.com.au/terms-and-conditions/
- group: other
  title: ''
  type: X-CDRPolicy
  url: https://www.westpac.com.au/content/dam/public/wbc/documents/pdf/aw/WBC_CDR_Policy.pdf
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.westpac.com.au/help/
- group: operate
  title: ''
  type: Support
  url: https://www.westpac.com.au/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://www.westpac.com.au/security/how-to-report/responsible-disclosure.html
- group: auth
  href: https://artifacts.apis.io/westpac/authentication/westpac-authentication.yml
  title: ''
  type: Authentication
  url: authentication/westpac-authentication.yml
- group: design
  href: https://artifacts.apis.io/westpac/conventions/westpac-conventions.yml
  title: ''
  type: Conventions
  url: conventions/westpac-conventions.yml
- group: design
  href: https://artifacts.apis.io/westpac/errors/westpac-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/westpac-problem-types.yml
- group: design
  href: https://artifacts.apis.io/westpac/lifecycle/westpac-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/westpac-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/westpac/conformance/westpac-conformance.yml
  title: ''
  type: Conformance
  url: conformance/westpac-conformance.yml
- group: design
  href: https://artifacts.apis.io/westpac/data-model/westpac-data-model.yml
  title: ''
  type: DataModel
  url: data-model/westpac-data-model.yml
- group: agent
  href: https://artifacts.apis.io/westpac/mcp/westpac-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/westpac-mcp.yml
- group: agent
  href: https://artifacts.apis.io/westpac/skills/westpac-browse-products.md
  title: ''
  type: AgentSkill
  url: skills/westpac-browse-products.md
- group: agent
  href: https://artifacts.apis.io/westpac/llms/westpac-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/westpac-llms.txt
- group: operate
  href: https://artifacts.apis.io/westpac/changelog/westpac-quickstream-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/westpac-quickstream-changelog.yml
- group: start
  href: https://artifacts.apis.io/westpac/sandbox/westpac-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/westpac-sandbox.yml
- group: design
  href: https://artifacts.apis.io/westpac/components/westpac-components.yml
  title: ''
  type: Components
  url: components/westpac-components.yml
- group: build
  href: https://artifacts.apis.io/westpac/errors/westpac-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/westpac-decline-codes.yml
- group: auth
  title: ''
  type: Compliance
  url: https://quickstream.westpac.com.au/docs/general/pci-compliance/
- group: start
  title: ''
  type: GettingStarted
  url: https://quickstream.westpac.com.au/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://quickstream.westpac.com.au/docs/quickstreamapi/v1/
created: '2026-07-20'
description: Westpac Banking Corporation is Australia's oldest bank and company, founded in 1817 as the Bank of New South Wales, and is one of the country's "Big Four" banks. Headquartered in Sydney, it is a publicly listed company on the Australian Securities Exchange (ASX:WBC), not a customer-owned mutual, and operates a multi-brand group that includes St.George, BankSA, Bank of Melbourne, and RAMS. As an authorised deposit-taking institution (ADI) regulated by APRA, Westpac is a designated data holder under Australia's Consumer Data Right (CDR / Open Banking) regime and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards. Consumer and account data sharing beyond product reference data is available only to accredited data recipients through the CDR's authenticated, consent-driven channels.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/westpac.png
json_schemas:
- name: ResponseBankingAccountByIdV5
  property_count: 3
  slug: westpac-response-banking-account-by-id-v5
- name: ResponseBankingAccountListV3
  property_count: 3
  slug: westpac-response-banking-account-list-v3
- name: ResponseBankingAccountsBalanceById
  property_count: 3
  slug: westpac-response-banking-accounts-balance-by-id
- name: ResponseBankingAccountsBalanceList
  property_count: 3
  slug: westpac-response-banking-accounts-balance-list
- name: ResponseBankingDirectDebitAuthorisationList
  property_count: 3
  slug: westpac-response-banking-direct-debit-authorisation-list
- name: ResponseBankingInstalmentPlanList
  property_count: 3
  slug: westpac-response-banking-instalment-plan-list
- name: ResponseBankingPayeeByIdV2
  property_count: 3
  slug: westpac-response-banking-payee-by-id-v2
- name: ResponseBankingPayeeListV2
  property_count: 3
  slug: westpac-response-banking-payee-list-v2
- name: ResponseBankingProductByIdV7
  property_count: 3
  slug: westpac-response-banking-product-by-id-v7
- name: ResponseBankingProductListV4
  property_count: 3
  slug: westpac-response-banking-product-list-v4
- name: ResponseBankingScheduledPaymentsListV2
  property_count: 3
  slug: westpac-response-banking-scheduled-payments-list-v2
- name: ResponseBankingTransactionByIdV3
  property_count: 3
  slug: westpac-response-banking-transaction-by-id-v3
- name: ResponseBankingTransactionListV2
  property_count: 3
  slug: westpac-response-banking-transaction-list-v2
jsonld:
- class_count: 95
  name: Westpac Context
  property_count: 280
  slug: westpac-context
layout: provider
modified: '2026-10-20'
name: Westpac
nav: Providers
network: true
overview: 'Westpac publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including QuickStream REST API, Banking Corporation Banking Account Balances API, Banking Corporation Banking Account Direct Debits API, and 6 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Banking.


  The Westpac catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Westpac''s developer surface includes engineering blog, documentation, support, authentication, changelog, sandbox, getting-started guide, and 40 more developer resources.'
plans:
- name: Westpac Plans Pricing
  plan_count: 0
  slug: westpac-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Westpac Rate Limits
  slug: westpac-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Westpac API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: westpac-rules
scopes:
- name: Westpac Scopes
  scope_count: 5
  slug: westpac-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 35
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 61.4
    developer_ergonomics: 75.6
    discoverability: 73.2
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
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
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/westpac/westpac-2026-07-21T114757.png
security:
- kind: authentication
  name: Westpac Authentication
  slug: westpac-authentication
  summary_line: http-basic · 1 scheme
- kind: domain-security
  name: Westpac Domain Security
  slug: westpac-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Westpac Vulnerability Disclosure
  slug: westpac-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 3
skills:
- name: westpac-browse-products
  slug: westpac-browse-products
- name: westpac-review-account-activity
  slug: westpac-review-account-activity
- name: westpac-review-payment-commitments
  slug: westpac-review-payment-commitments
slug: westpac
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.westpac.com.au/
---

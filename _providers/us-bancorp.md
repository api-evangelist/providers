---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Us Bancorp Agentic Access
  operation_count: 15
  slug: us-bancorp-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 4
apis:
- description: The Wire Transfers API enables domestic and international wire transfer origination from U.S. Bank corporate accounts for large-value, time-sensitive payments.
  name: US Bank Wire Transfers API
  slug: us-bank-wire-transfers
- description: The Data Toolbox API provides access to U.S. Bank retail banking consumer account data including checking, savings, credit card, mortgage, and brokerage account information. Used to build personalized
  name: US Bank Data Toolbox API
  slug: us-bank-data-toolbox
- description: The Voyager Fleet API suite provides fleet management capabilities for the Voyager network, enabling access to fleet transaction data, vehicle management, account information, and reporting for corpor
  name: US Bank Voyager Fleet API
  slug: us-bank-voyager
- description: The Freight Payment API suite provides freight audit and payment processing capabilities, enabling freight shippers to submit and receive transaction data through a single API and manage freight payme
  name: US Bank Freight Payment API
  slug: us-bank-freight-payment
- description: The Instant Payments API enables instant payment origination supporting FedNow and RTP payment rails for real-time settlement.
  name: US Bank Instant Payments API
  slug: us-bank-instant-payments
- description: The Bank Holidays API provides information about U.S. Bank processing holidays and Federal Reserve banking holidays, useful for payment scheduling and clearing house availability calculations.
  name: US Bank Holidays API
  slug: us-bank-bank-holidays
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Accounts API from US Bancorp — 1 operation(s) for accounts.
  name: US Bancorp Accounts API
  slug: us-bancorp-accounts-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Balances API from US Bancorp — 2 operation(s) for balances.
  name: US Bancorp Balances API
  slug: us-bancorp-balances-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Credit Transfers API from US Bancorp — 2 operation(s) for credit transfers.
  name: US Bancorp Credit Transfers API
  slug: us-bancorp-credit-transfers-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Exception History API from US Bancorp — 1 operation(s) for exception history.
  name: US Bancorp Exception History API
  slug: us-bancorp-exception-history-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Exceptions API from US Bancorp — 2 operation(s) for exceptions.
  name: US Bancorp Exceptions API
  slug: us-bancorp-exceptions-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Push to Card Payments API from US Bancorp — 2 operation(s) for push to card payments.
  name: US Bancorp Push to Card Payments API
  slug: us-bancorp-push-to-card-payments-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Request for Payment API from US Bancorp — 2 operation(s) for request for payment.
  name: US Bancorp Request for Payment API
  slug: us-bancorp-request-for-payment-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The RTP Eligibility API from US Bancorp — 1 operation(s) for rtp eligibility.
  name: US Bancorp RTP Eligibility API
  slug: us-bancorp-rtp-eligibility-api
- baseURL: https://api.usbank.com
  baseurl_source: declared
  description: The Transactions API from US Bancorp — 2 operation(s) for transactions.
  name: US Bancorp Transactions API
  slug: us-bancorp-transactions-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: US Bank Corporate Account Information Accounts API
  slug: open-us-bancorp-accounts-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts Balances API
  slug: open-us-bancorp-balances-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts Credit Transfers API
  slug: open-us-bancorp-credit-transfers-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts Exception History API
  slug: open-us-bancorp-exception-history-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts Exceptions API
  slug: open-us-bancorp-exceptions-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts Push to Card Payments API
  slug: open-us-bancorp-push-to-card-payments-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts Request for Payment API
  slug: open-us-bancorp-request-for-payment-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts RTP Eligibility API
  slug: open-us-bancorp-rtp-eligibility-api
- collection_type: open
  name: US Bank Corporate Account Information Accounts Transactions API
  slug: open-us-bancorp-transactions-api
- collection_type: open
  name: US Bank Corporate Account Information API
  slug: open-us-bank-corporate-account-information
- collection_type: open
  name: US Bank Positive Pay API
  slug: open-us-bank-positive-pay
- collection_type: open
  name: US Bank Push to Card API
  slug: open-us-bank-push-to-card
- collection_type: open
  name: US Bank RTP Real-Time Payments API
  slug: open-us-bank-rtp
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/us-bancorp-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-bancorp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-bancorp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-bancorp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/us-bancorp-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usbank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-bank
created: '2024-11-21'
description: U.S. Bancorp is the parent company of U.S. Bank National Association, one of the largest commercial banks in the United States. U.S. Bank provides a developer portal at developer.usbank.com offering APIs for corporate banking, payments, and treasury management including RTP, ACH, Positive Pay, corporate account information, data toolbox, fleet management (Voyager), freight payment, and push-to-card capabilities. Authentication uses OAuth MFA with SinglePoint credentials.
examples:
- key_count: 2
  name: Us Bank Corporate Account Information Get Current Day Balances Example
  slug: us-bank-corporate-account-information-get-current-day-balances-example
- key_count: 2
  name: Us Bank Rtp Initiate Credit Transfer Example
  slug: us-bank-rtp-initiate-credit-transfer-example
features:
- 'U.S. Bancorp: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- U.S. Bank APIs are sold to commercial treasury and embedded payment customers via account managers.
finops:
- name: Us Bancorp Finops
  service_category: Banking
  slug: us-bancorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-bancorp.png
json_schemas:
- name: US Bank Deposit Account
  property_count: 5
  slug: us-bank-account
- name: US Bank Account Transaction
  property_count: 10
  slug: us-bank-transaction
json_structures:
- name: Us Bank Transaction Structure
  property_count: 0
  slug: us-bank-transaction-structure
jsonld:
- class_count: 30
  name: Us Bancorp Context
  property_count: 5
  slug: us-bancorp-context
layout: provider
modified: '2026-05-19'
name: US Bancorp
nav: Providers
network: true
overview: 'US Bancorp publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Balances API, Credit Transfers API, and 6 more. Tagged areas include Banking, Finance, Fortune 500, Corporate Banking, and Payments.


  The US Bancorp catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Bancorp''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Us Bancorp Plans Pricing
  plan_count: 1
  slug: us-bancorp-plans-pricing
press:
- date: '2026-05-25'
  title: U.S. Bank Expands Collaboration with AWS to Accelerate ...
  url: https://press.aboutamazon.com/aws/2026/5/u-s-bank-expands-collaboration-with-aws-to-accelerate-progressive-technology-transformation-and-ai-driven-customer-experience-innovation
- date: '2026-05-25'
  title: 'US Bancorp''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/us-bancorp-ai-strategy-analysis-of-dominance-in-banking-financial-services-ai/
- date: '2026-05-25'
  title: U.S. Bancorp Announces Leadership Changes in Its ...
  url: https://finance.yahoo.com/news/u-bancorp-announces-leadership-changes-200000201.html
- date: '2026-05-25'
  title: U.S. Bank Partners With Microsoft to Accelerate the Future of ...
  url: https://ir.usbank.com/news-events/news/news-details/2022/U.S.-Bank-Partners-With-Microsoft-to-Accelerate-the-Future-of-Banking-With-Cloud-Computing-02-22-2022/default.aspx
- date: '2026-05-25'
  title: U.S. Bancorp Annual Report 2025
  url: https://s203.q4cdn.com/711684571/files/doc_financials/2025/ar/2025-Annual-Report_ADA_F.pdf
random_paper: 10
rate_limits:
- limit_count: 1
  name: Us Bancorp Rate Limits
  slug: us-bancorp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Bancorp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-bancorp-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: US Bancorp API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: us-bank-rules
scopes:
- name: Us Bancorp Scopes
  scope_count: 6
  slug: us-bancorp-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 68.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-bancorp/refs/heads/main/screenshots/us-bancorp-2026-06-20T200603.png
security:
- kind: authentication
  name: Us Bancorp Authentication
  slug: us-bancorp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Us Bancorp Domain Security
  slug: us-bancorp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: us-bancorp
tags:
- Banking
- Finance
- Fortune 500
- Corporate Banking
- Payments
- Open Banking
- Treasury Management
- Consumer Banking
---

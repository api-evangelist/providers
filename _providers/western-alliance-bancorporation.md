---
access_model:
  confidence: high
  label: Enterprise - Requires approval (Treasury Management enrollment; no license fee, transaction fees per bank fee schedule)
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://www.westernalliancebancorporation.com/sites/default/files/2025-05/api-services-terms-conditions.pdf
  - '{''url'': ''https://www.westernalliancebancorp.com'', ''status'': 301, ''note'': "declared website redirects to https://www.westernalliancebancorporation.com/ - the bank''s current corporate domain; the developer portal lives on the westernalliancebank.com brand domain (probed 2026-09-17)"}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-11-06'
api_count: 12
apis:
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Retrieves the image of a paid check by account, check date, check number, trace number and amount. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank Check Image API
  slug: western-alliance-bancorporation-check-image-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Places a stop-payment order on a check (or range) and looks up existing stop payments on an account. Family: Informational APIs on the WAB API Developer Portal; 4 operations captured.'
  name: Western Alliance Bank Stop Payments API
  slug: western-alliance-bancorporation-stop-payments-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Moves funds between two Western Alliance accounts held by the same client (book transfer). Family: Transactional APIs on the WAB API Developer Portal; 2 operations captured.'
  name: Western Alliance Bank Book Transfer API
  slug: western-alliance-bancorporation-book-transfer-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: Initiates an intra-bank transfer between two Western Alliance Bank accounts and searches intra-bank transfers as originator or beneficiary. The transfer returns a Payment Message Reference that is the
  name: Western Alliance Bank Intrabank Transfer API
  slug: western-alliance-bancorporation-intrabank-transfer-api
- description: Western Alliance Bank's commercial open-banking API lets approved business clients interact directly with WAB systems to access balance and transaction information, retrieve check images, initiate fun
  name: Western Alliance Bank API (Treasury Management)
  slug: wab-treasury-management-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The ACH Request API from Western Alliance Bancorporation — 1 operation(s) for ach request.
  name: Western Alliance Bancorporation ACH Request API
  slug: western-alliance-bancorporation-ach-request-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Balance API from Western Alliance Bancorporation — 1 operation(s) for balance.
  name: Western Alliance Bancorporation Balance API
  slug: western-alliance-bancorporation-balance-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Client Data API from Western Alliance Bancorporation — 1 operation(s) for client data.
  name: Western Alliance Bancorporation Client Data API
  slug: western-alliance-bancorporation-client-data-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Date Range Transaction History API from Western Alliance Bancorporation — 1 operation(s) for date range transaction history.
  name: Western Alliance Bancorporation Date Range Transaction History API
  slug: western-alliance-bancorporation-date-range-transaction-history-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Deposite API from Western Alliance Bancorporation — 2 operation(s) for deposite.
  name: Western Alliance Bancorporation Deposite API
  slug: western-alliance-bancorporation-deposite-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Get Balance API from Western Alliance Bancorporation — 2 operation(s) for get balance.
  name: Western Alliance Bancorporation Get Balance API
  slug: western-alliance-bancorporation-get-balance-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Get Bank Statement API API from Western Alliance Bancorporation — 1 operation(s) for get bank statement api.
  name: Western Alliance Bancorporation Get Bank Statement API
  slug: western-alliance-bancorporation-get-bank-statement-api-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Get Tassat Login Token API from Western Alliance Bancorporation — 1 operation(s) for get tassat login token.
  name: Western Alliance Bancorporation Get Tassat Login Token API
  slug: western-alliance-bancorporation-get-tassat-login-token-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Get Token API from Western Alliance Bancorporation — 1 operation(s) for get token.
  name: Western Alliance Bancorporation Get Token API
  slug: western-alliance-bancorporation-get-token-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Get User Token API from Western Alliance Bancorporation — 1 operation(s) for get user token.
  name: Western Alliance Bancorporation Get User Token API
  slug: western-alliance-bancorporation-get-user-token-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Get WAB Token API from Western Alliance Bancorporation — 1 operation(s) for get wab token.
  name: Western Alliance Bancorporation Get WAB Token API
  slug: western-alliance-bancorporation-get-wab-token-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Health Check API from Western Alliance Bancorporation — 12 operation(s) for health check.
  name: Western Alliance Bancorporation Health Check API
  slug: western-alliance-bancorporation-health-check-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: On-demand lookup of intra-bank transfers; a fallback when the webhook is missed, not a replacement for it.
  name: Western Alliance Bancorporation Intrabank Search API
  slug: western-alliance-bancorporation-intrabank-search-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Redeem API from Western Alliance Bancorporation — 2 operation(s) for redeem.
  name: Western Alliance Bancorporation Redeem API
  slug: western-alliance-bancorporation-redeem-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Send API from Western Alliance Bancorporation — 2 operation(s) for send.
  name: Western Alliance Bancorporation Send API
  slug: western-alliance-bancorporation-send-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Transaction History Intraday API from Western Alliance Bancorporation — 2 operation(s) for transaction history intraday.
  name: Western Alliance Bancorporation Transaction History Intraday API
  slug: western-alliance-bancorporation-transaction-history-intraday-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Transaction History Priorday API from Western Alliance Bancorporation — 2 operation(s) for transaction history priorday.
  name: Western Alliance Bancorporation Transaction History Priorday API
  slug: western-alliance-bancorporation-transaction-history-priorday-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Transactions API from Western Alliance Bancorporation — 1 operation(s) for transactions.
  name: Western Alliance Bancorporation Transactions API
  slug: western-alliance-bancorporation-transactions-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Wallet balance API from Western Alliance Bancorporation — 1 operation(s) for wallet balance.
  name: Western Alliance Bancorporation Wallet balance API
  slug: western-alliance-bancorporation-wallet-balance-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Wallet Names API from Western Alliance Bancorporation — 1 operation(s) for wallet names.
  name: Western Alliance Bancorporation Wallet Names API
  slug: western-alliance-bancorporation-wallet-names-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: The Wires Request API API from Western Alliance Bancorporation — 1 operation(s) for wires request api.
  name: Western Alliance Bancorporation Wires Request API
  slug: western-alliance-bancorporation-wires-request-api-api
artifact_total: 51
asyncapis:
- description: ''
  name: Western Alliance Bancorporation Webhooks
  slug: western-alliance-bancorporation-webhooks
collections:
- collection_type: postman
  name: ACH EAPI | Beta
  slug: postman-western-alliance-bancorporation-ach-eapi-beta
- collection_type: postman
  name: All Account Balance API
  slug: postman-western-alliance-bancorporation-all-account-balance-api
- collection_type: postman
  name: All Account Intraday API
  slug: postman-western-alliance-bancorporation-all-account-intraday-api
- collection_type: postman
  name: All Account Priorday API
  slug: postman-western-alliance-bancorporation-all-account-priorday-api
- collection_type: postman
  name: Bank Statement API
  slug: postman-western-alliance-bancorporation-bank-statement-api
- collection_type: postman
  name: Book Transfer API
  slug: postman-western-alliance-bancorporation-book-transfer-api
- collection_type: postman
  name: Check image API
  slug: postman-western-alliance-bancorporation-check-image-api
- collection_type: postman
  name: Date Range Transactions API
  slug: postman-western-alliance-bancorporation-date-range-transactions-api
- collection_type: postman
  name: Single Account Balance API
  slug: postman-western-alliance-bancorporation-single-account-balance-api
- collection_type: postman
  name: Single Account Intraday API
  slug: postman-western-alliance-bancorporation-single-account-intraday-api
- collection_type: postman
  name: Single Account Priorday API
  slug: postman-western-alliance-bancorporation-single-account-priorday-api
- collection_type: postman
  name: Stop Payments API
  slug: postman-western-alliance-bancorporation-stop-payments-api
- collection_type: postman
  name: TassatPay EAPI | Beta
  slug: postman-western-alliance-bancorporation-tassatpay-eapi-beta
- collection_type: postman
  name: Token API
  slug: postman-western-alliance-bancorporation-token-api
- collection_type: postman
  name: Wires Request API
  slug: postman-western-alliance-bancorporation-wires-request-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.westernalliancebancorporation.com/sites/default/files/2025-05/api-services-terms-conditions.pdf
- group: other
  title: ''
  type: Customers
  url: https://www.westernalliancebank.com
- group: other
  title: ''
  type: Resources
  url: https://www.westernalliancebancorporation.com/investor-relations
- group: start
  title: ''
  type: Signup
  url: https://developer.westernalliancebank.com/s/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/westernalliancebank
- group: company
  title: ''
  type: Website
  url: https://www.westernalliancebancorporation.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.westernalliancebank.com/s/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.westernalliancebank.com/s/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.westernalliancebank.com/s/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.westernalliancebank.com/s/get-token-tutorial
- group: docs
  title: ''
  type: Documentation
  url: https://developer.westernalliancebank.com/s/get-balance-tutorial
- group: build
  title: ''
  type: Postman
  url: https://developer.westernalliancebank.com/s/postman-collection
- group: build
  href: https://artifacts.apis.io/western-alliance-bancorporation/postman/western-alliance-bancorporation-postman.yml
  title: ''
  type: PostmanCollection
  url: postman/western-alliance-bancorporation-postman.yml
- group: operate
  title: ''
  type: FAQ
  url: https://developer.westernalliancebank.com/s/faq
- group: operate
  title: ''
  type: Support
  url: https://developer.westernalliancebank.com/s/forums
- group: company
  title: ''
  type: Blog
  url: https://developer.westernalliancebank.com/s/blog
- group: company
  title: ''
  type: News
  url: https://developer.westernalliancebank.com/s/news
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.westernalliancebank.com/s/incident
- group: start
  title: ''
  type: Login
  url: https://developer.westernalliancebank.com/s/login/
- group: start
  title: ''
  type: SignUp
  url: https://developer.westernalliancebank.com/s/login/SelfRegister
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westernalliancebancorporation.com/sites/default/files/2025-05/api-services-terms-conditions.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westernalliancebancorporation.com/privacy-legal-home/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/western-alliance-bank
- group: agent
  href: https://artifacts.apis.io/western-alliance-bancorporation/llms/western-alliance-bancorporation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/western-alliance-bancorporation-llms.txt
- group: agent
  href: https://artifacts.apis.io/western-alliance-bancorporation/well-known/western-alliance-bancorporation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/western-alliance-bancorporation-well-known.yml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/well-known/western-alliance-bancorporation-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/western-alliance-bancorporation-openid-configuration.json
- group: auth
  href: https://artifacts.apis.io/western-alliance-bancorporation/authentication/western-alliance-bancorporation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/western-alliance-bancorporation-authentication.yml
- group: design
  href: https://artifacts.apis.io/western-alliance-bancorporation/conventions/western-alliance-bancorporation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/western-alliance-bancorporation-conventions.yml
- group: design
  href: https://artifacts.apis.io/western-alliance-bancorporation/conventions/western-alliance-bancorporation-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/western-alliance-bancorporation-conventions.yml
- group: design
  href: https://artifacts.apis.io/western-alliance-bancorporation/errors/western-alliance-bancorporation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/western-alliance-bancorporation-problem-types.yml
- group: build
  href: https://artifacts.apis.io/western-alliance-bancorporation/errors/western-alliance-bancorporation-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/western-alliance-bancorporation-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/western-alliance-bancorporation/lifecycle/western-alliance-bancorporation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/western-alliance-bancorporation-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/western-alliance-bancorporation/conformance/western-alliance-bancorporation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/western-alliance-bancorporation-conformance.yml
- group: start
  href: https://artifacts.apis.io/western-alliance-bancorporation/sandbox/western-alliance-bancorporation-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/western-alliance-bancorporation-sandbox.yml
- group: design
  href: https://artifacts.apis.io/western-alliance-bancorporation/asyncapi/western-alliance-bancorporation-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/western-alliance-bancorporation-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/western-alliance-bancorporation/mcp/western-alliance-bancorporation-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/western-alliance-bancorporation-mcp.yml
- group: build
  href: https://artifacts.apis.io/western-alliance-bancorporation/mcp/western-alliance-bancorporation-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/western-alliance-bancorporation-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/western-alliance-bancorporation/data-model/western-alliance-bancorporation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/western-alliance-bancorporation-data-model.yml
- group: agent
  href: https://artifacts.apis.io/western-alliance-bancorporation/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/western-alliance-bancorporation/plans/western-alliance-bancorporation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/western-alliance-bancorporation-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/western-alliance-bancorporation/rate-limits/western-alliance-bancorporation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/western-alliance-bancorporation-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/western-alliance-bancorporation/security/western-alliance-bancorporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/western-alliance-bancorporation-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/western-alliance-bancorporation/finops/western-alliance-bancorporation-finops.yml
  title: ''
  type: FinOps
  url: finops/western-alliance-bancorporation-finops.yml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-ach-eapi-beta-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-ach-eapi-beta-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-all-account-balance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-all-account-balance-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-all-account-intraday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-all-account-intraday-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-all-account-priorday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-all-account-priorday-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-bank-statement-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-bank-statement-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-book-transfer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-book-transfer-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-check-image-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-check-image-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-date-range-transactions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-date-range-transactions-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-intrabank-transfer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-intrabank-transfer-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-single-account-balance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-single-account-balance-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-single-account-intraday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-single-account-intraday-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-single-account-priorday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-single-account-priorday-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-stop-payments-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-stop-payments-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-tassatpay-eapi-beta-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-tassatpay-eapi-beta-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-token-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-token-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/western-alliance-bancorporation/overlays/western-alliance-bancorporation-wires-request-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-wires-request-api-overlay.yaml
created: '2026-04-19'
description: 'Western Alliance Bancorporation (NYSE: WAL) is the parent of Western Alliance Bank, a top-performing US commercial bank. Its WAB API Developer Portal (developer.westernalliancebank.com, built on Salesforce Experience Cloud with MuleSoft Anypoint API Community Manager) publishes treasury-management APIs on the api-connect.westernalliancebank.com gateway in six families - Informational (balances, intraday, prior-day and date-range transactions, statements, check images, stop payments), Transactional (book transfer, wires, intrabank transfer, ACH beta), Utility (token), Embedded Finance, Digital Assets (TassatPay beta) and Corporate Trust. Access requires Treasury Management enrollment; the bank issues a Client ID / Client Secret exchanged for a time-limited bearer token, and the intrabank transfer surface pushes ISO 20022-coded status webhooks.'
finops:
- has_sources: true
  method: derived
  name: Western Alliance Bancorporation Finops
  primary_unit: ''
  service_category: ''
  slug: western-alliance-bancorporation-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western-alliance-bancorporation.png
layout: provider
modified: '2026-09-17'
name: Western Alliance Bancorporation
nav: Providers
network: true
overview: 'Western Alliance Bancorporation publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Western Alliance Bank Check Image API, Western Alliance Bank Stop Payments API, Western Alliance Bank Book Transfer API, and 23 more. Tagged areas include Banking, Financial Services, Treasury Management, Payments, and Account.


  The Western Alliance Bancorporation catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Western Alliance Bancorporation''s developer surface includes pricing, signup flow, API reference, getting-started guide, documentation, FAQ, support, and 52 more developer resources.'
plans:
- name: Western Alliance Bancorporation Plans Pricing
  plan_count: 1
  slug: western-alliance-bancorporation-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Western Alliance Bancorporation Rate Limits
  slug: western-alliance-bancorporation-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Western Alliance Bancorporation API Rules
  rule_count: 59
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 9
  slug: western-alliance-bancorporation-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 21.0
    developer_ergonomics: 70.8
    discoverability: 70.5
    operational_transparency: 26.3
  previous_composite: 47.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 25
      marker_coverage: 100.0
      total: 25
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/western-alliance-bancorporation/western-alliance-bancorporation-2026-06-20T201359.png
security:
- kind: authentication
  name: Western Alliance Bancorporation Authentication
  slug: western-alliance-bancorporation-authentication
  summary_line: apiKey/http/mutualTLS · 4 schemes
- kind: domain-security
  name: Western Alliance Bancorporation Domain Security
  slug: western-alliance-bancorporation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Check balances and pull transaction history
  slug: western-alliance-bancorporation-check-balances-and-transactions
- name: Initiate and reconcile an intrabank transfer
  slug: western-alliance-bancorporation-initiate-and-reconcile-intrabank-transfer
- name: Submit a wire transfer request
  slug: western-alliance-bancorporation-submit-wire-request
slug: western-alliance-bancorporation
tags:
- Banking
- Financial Services
- Treasury Management
- Payments
- Account
- Transaction
- Wires
- ACH
- Digital Assets
- Webhook
website: https://www.westernalliancebancorporation.com
---

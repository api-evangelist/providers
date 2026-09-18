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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.8
  scored_at: '2026-09-17'
api_count: 17
apis:
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Entitlements token service: exchanges the client id + client secret issued at enrollment for a scoped bearer token used by every other WAB API. Family: Utility APIs on the WAB API Developer Portal; 2 '
  name: Western Alliance Bank Token API
  slug: western-alliance-bancorporation-token-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Returns current balances for every account entitled to the calling client. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank All Account Balance API
  slug: western-alliance-bancorporation-all-account-balance-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Returns the current balance for one account. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank Single Account Balance API
  slug: western-alliance-bancorporation-single-account-balance-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Same-day (intraday) transaction history across all entitled accounts, with optional filters and page-key pagination. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank All Account Intraday API
  slug: western-alliance-bancorporation-all-account-intraday-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Same-day (intraday) transaction history for one account. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank Single Account Intraday API
  slug: western-alliance-bancorporation-single-account-intraday-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Prior-business-day posted transaction history across all entitled accounts. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank All Account Priorday API
  slug: western-alliance-bancorporation-all-account-priorday-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Prior-business-day posted transaction history for one account. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank Single Account Priorday API
  slug: western-alliance-bancorporation-single-account-priorday-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Posted transactions for one account over a BeginDate/EndDate window, with filters and page-key pagination. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank Date Range Transactions API
  slug: western-alliance-bancorporation-date-range-transactions-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: 'Retrieves a bank statement document for an account and statement period. Family: Informational APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank Bank Statement API
  slug: western-alliance-bancorporation-bank-statement-api
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
  description: 'Submits a wire transfer request (Fedwire or other method of payment) from a virtual account. Family: Transactional APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank Wires Request API
  slug: western-alliance-bancorporation-wires-request-api
- baseURL: https://api-connect.westernalliancebank.com
  baseurl_source: declared
  description: Initiates an intra-bank transfer between two Western Alliance Bank accounts and searches intra-bank transfers as originator or beneficiary. The transfer returns a Payment Message Reference that is the
  name: Western Alliance Bank Intrabank Transfer API
  slug: western-alliance-bancorporation-intrabank-transfer-api
- baseURL: https://api-connect.westernalliancebanktest.com
  baseurl_source: declared
  description: 'Beta. Originates an ACH batch (NACHA batch header + entry details) for credit or debit. Family: Transactional APIs on the WAB API Developer Portal; 3 operations captured.'
  name: Western Alliance Bank ACH API (Beta)
  slug: western-alliance-bancorporation-ach-eapi-beta
- baseURL: https://api-connect.westernalliancebanktest.com
  baseurl_source: declared
  description: 'Beta. Client gateway to the TassatPay blockchain-based real-time B2B payments network: wallet balances, deposits (wallet to DDA), redemptions, sends between wallets, transactions and wallet names. Fam'
  name: Western Alliance Bank TassatPay API (Beta)
  slug: western-alliance-bancorporation-tassatpay-eapi-beta
- description: Western Alliance Bank's commercial open-banking API lets approved business clients interact directly with WAB systems to access balance and transaction information, retrieve check images, initiate fun
  name: Western Alliance Bank API (Treasury Management)
  slug: wab-treasury-management-api
artifact_total: 38
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
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/postman/western-alliance-bancorporation-postman.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/llms/western-alliance-bancorporation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/western-alliance-bancorporation-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/well-known/western-alliance-bancorporation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/western-alliance-bancorporation-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/well-known/western-alliance-bancorporation-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/western-alliance-bancorporation-openid-configuration.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/authentication/western-alliance-bancorporation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/western-alliance-bancorporation-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/conventions/western-alliance-bancorporation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/western-alliance-bancorporation-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/conventions/western-alliance-bancorporation-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/western-alliance-bancorporation-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/errors/western-alliance-bancorporation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/western-alliance-bancorporation-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/errors/western-alliance-bancorporation-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/western-alliance-bancorporation-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/lifecycle/western-alliance-bancorporation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/western-alliance-bancorporation-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/conformance/western-alliance-bancorporation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/western-alliance-bancorporation-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/sandbox/western-alliance-bancorporation-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/western-alliance-bancorporation-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/asyncapi/western-alliance-bancorporation-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/western-alliance-bancorporation-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/mcp/western-alliance-bancorporation-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/western-alliance-bancorporation-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/mcp/western-alliance-bancorporation-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/western-alliance-bancorporation-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/data-model/western-alliance-bancorporation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/western-alliance-bancorporation-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/plans/western-alliance-bancorporation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/western-alliance-bancorporation-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/rate-limits/western-alliance-bancorporation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/western-alliance-bancorporation-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/security/western-alliance-bancorporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/western-alliance-bancorporation-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/finops/western-alliance-bancorporation-finops.yml
  title: ''
  type: FinOps
  url: finops/western-alliance-bancorporation-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-ach-eapi-beta-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-ach-eapi-beta-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-all-account-balance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-all-account-balance-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-all-account-intraday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-all-account-intraday-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-all-account-priorday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-all-account-priorday-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-bank-statement-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-bank-statement-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-book-transfer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-book-transfer-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-check-image-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-check-image-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-date-range-transactions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-date-range-transactions-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-intrabank-transfer-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-intrabank-transfer-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-single-account-balance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-single-account-balance-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-single-account-intraday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-single-account-intraday-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-single-account-priorday-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-single-account-priorday-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-stop-payments-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-stop-payments-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-tassatpay-eapi-beta-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-tassatpay-eapi-beta-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-token-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-token-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/overlays/western-alliance-bancorporation-wires-request-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/western-alliance-bancorporation-wires-request-api-overlay.yaml
created: '2026-04-19'
description: 'Western Alliance Bancorporation (NYSE: WAL) is the parent of Western Alliance Bank, a top-performing US commercial bank. Its WAB API Developer Portal (developer.westernalliancebank.com, built on Salesforce Experience Cloud with MuleSoft Anypoint API Community Manager) publishes treasury-management APIs on the api-connect.westernalliancebank.com gateway in six families - Informational (balances, intraday, prior-day and date-range transactions, statements, check images, stop payments), Transactional (book transfer, wires, intrabank transfer, ACH beta), Utility (token), Embedded Finance, Digital Assets (TassatPay beta) and Corporate Trust. Access requires Treasury Management enrollment; the bank issues a Client ID / Client Secret exchanged for a time-limited bearer token, and the intrabank transfer surface pushes ISO 20022-coded status webhooks.'
finops:
- name: Western Alliance Bancorporation Finops
  service_category: Banking
  slug: western-alliance-bancorporation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western-alliance-bancorporation.png
layout: provider
modified: '2026-09-17'
name: Western Alliance Bancorporation
nav: Providers
network: true
overview: 'Western Alliance Bancorporation publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Western Alliance Bank Token API, Western Alliance Bank All Account Balance API, Western Alliance Bank Single Account Balance API, and 13 more. Tagged areas include Banking, Financial-Services, Treasury Management, Payments, and Account.


  The Western Alliance Bancorporation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Western Alliance Bancorporation''s developer surface includes signup flow, API reference, getting-started guide, documentation, FAQ, support, engineering blog, and 51 more developer resources.'
plans:
- name: Western Alliance Bancorporation Plans Pricing
  plan_count: 1
  slug: western-alliance-bancorporation-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Western Alliance Bancorporation Rate Limits
  slug: western-alliance-bancorporation-rate-limits
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 39.1
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 21.1
    developer_ergonomics: 70.8
    discoverability: 66.7
    operational_transparency: 28.9
  previous_composite: 7.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 49.4
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/western-alliance-bancorporation/refs/heads/main/screenshots/western-alliance-bancorporation-2026-06-20T201359.png
security:
- kind: authentication
  name: Western Alliance Bancorporation Authentication
  slug: western-alliance-bancorporation-authentication
  summary_line: apiKey/http/mutualTLS · 4 schemes
- kind: domain-security
  name: Western Alliance Bancorporation Domain Security
  slug: western-alliance-bancorporation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: western-alliance-bancorporation
tags:
- Banking
- Financial-Services
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

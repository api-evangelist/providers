---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 263
  human_in_the_loop: 5
  name: Plaid Agentic Access
  operation_count: 265
  slug: plaid-agentic-access
  summary_line: 265 operations · 263 acting · 5 human-in-the-loop
api_count: 41
apis:
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: 'The Plaid REST API — the aggregator surface for bank-account, identity, transactions, income, assets, liabilities, investments, transfer, payment initiation, virtual accounts, signal, beacon, monitor '
  name: Plaid API
  phrasing_intents:
  - id: baseReportGet
    intent: Retrieve a consumer Base Report
    question: How do I pull the Base Report for a user in Plaid Check?
  - id: baseReportCreate
    intent: Create a consumer Base Report
    question: How do I generate a Base Report from a user's most recently linked bank?
  - id: craBankIncomeGet
    intent: Retrieve a CRA bank income report
    question: How do I read the bank income report for a user after income verification?
  - id: craBankIncomeCreate
    intent: Create a CRA bank income report
    question: How do I start a consumer report that verifies income from bank deposits?
  - id: craPartnerInsightsGet
    intent: Retrieve cash flow insights for a user
    question: How do I get cash flow insights from the accounts a user linked for income checks?
  - id: craLoansApplicationsRegister
    intent: Register loan applications and decisions
    question: How do I tell Plaid Check which loan applications I approved or declined?
  - id: craLoansRegister
    intent: Register loans to their applicants
    question: How do I link funded loans to the applicants they were issued to?
  - id: craLoansUpdate
    intent: Update registered loan status and payments
    question: How do I report payment history on a loan I already registered?
  phrasing_ops: 265
  slug: plaid-plaid-api
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: Search and view customer accounts
  name: Plaid Account Information API
  slug: plaid-account-information-api
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: Search and retrieve account statements
  name: Plaid Account Statements API
  slug: plaid-account-statements-api
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: Search and view account transactions
  name: Plaid Account Transactions API
  slug: plaid-account-transactions-api
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: Search and view asset transfer networks
  name: Plaid Asset Transfer Networks Information API
  slug: plaid-asset-transfer-networks-information-api
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: Search and view account payment networks
  name: Plaid Payment Networks Information API
  slug: plaid-payment-networks-information-api
- baseURL: https://production.plaid.com
  baseurl_source: declared
  description: Search and view customer or customers
  name: Plaid Personal Information API
  slug: plaid-personal-information-api
artifact_total: 117
asyncapis:
- description: AsyncAPI 2.6 specification for the Plaid webhook surface. Plaid delivers asynchronous notifications via HTTP POST to the URL registered on an Item (`webhook` parameter in `/link/token/create`) or conf
  name: Plaid Webhooks
  slug: plaid-webhooks--asyncapi-original
- description: ''
  name: Plaid Webhooks
  slug: plaid-webhooks
collections:
- collection_type: postman
  name: Plaid accounts/
  slug: postman-plaid-accounts-
- collection_type: postman
  name: Plaid asset report/
  slug: postman-plaid-asset-report-
- collection_type: postman
  name: Plaid auth/
  slug: postman-plaid-auth-
- collection_type: postman
  name: Plaid bank transfer/
  slug: postman-plaid-bank-transfer-
- collection_type: postman
  name: Plaid beacon/
  slug: postman-plaid-beacon-
- collection_type: postman
  name: Plaid categories/
  slug: postman-plaid-categories-
- collection_type: postman
  name: Plaid cra/
  slug: postman-plaid-cra-
- collection_type: postman
  name: Plaid credit/
  slug: postman-plaid-credit-
- collection_type: postman
  name: Plaid deposit switch/
  slug: postman-plaid-deposit-switch-
- collection_type: postman
  name: Plaid employers/
  slug: postman-plaid-employers-
- collection_type: postman
  name: Plaid fdx/
  slug: postman-plaid-fdx-
- collection_type: postman
  name: Plaid identity/
  slug: postman-plaid-identity-
- collection_type: postman
  name: Plaid identity verification/
  slug: postman-plaid-identity-verification-
- collection_type: postman
  name: Plaid income/
  slug: postman-plaid-income-
- collection_type: postman
  name: Plaid institutions/
  slug: postman-plaid-institutions-
- collection_type: postman
  name: Plaid investments/
  slug: postman-plaid-investments-
- collection_type: postman
  name: Plaid item/
  slug: postman-plaid-item-
- collection_type: postman
  name: Plaid liabilities/
  slug: postman-plaid-liabilities-
- collection_type: postman
  name: Plaid link/
  slug: postman-plaid-link-
- collection_type: postman
  name: Plaid link delivery/
  slug: postman-plaid-link-delivery-
- collection_type: postman
  name: Plaid partner/
  slug: postman-plaid-partner-
- collection_type: postman
  name: Plaid payment initiation/
  slug: postman-plaid-payment-initiation-
- collection_type: postman
  name: Plaid payment profile/
  slug: postman-plaid-payment-profile-
- collection_type: postman
  name: Plaid processor/
  slug: postman-plaid-processor-
- collection_type: postman
  name: Plaid sandbox/
  slug: postman-plaid-sandbox-
- collection_type: postman
  name: Plaid signal/
  slug: postman-plaid-signal-
- collection_type: postman
  name: Plaid statements/
  slug: postman-plaid-statements-
- collection_type: postman
  name: Plaid transactions/
  slug: postman-plaid-transactions-
- collection_type: postman
  name: Plaid transfer/
  slug: postman-plaid-transfer-
- collection_type: postman
  name: Plaid wallet/
  slug: postman-plaid-wallet-
- collection_type: postman
  name: Plaid watchlist screening/
  slug: postman-plaid-watchlist-screening-
- collection_type: open
  name: Plaid accounts/
  slug: open-plaid-accounts-
- collection_type: open
  name: Plaid asset report/
  slug: open-plaid-asset-report-
- collection_type: open
  name: Plaid auth/
  slug: open-plaid-auth-
- collection_type: open
  name: Plaid bank transfer/
  slug: open-plaid-bank-transfer-
- collection_type: open
  name: Plaid beacon/
  slug: open-plaid-beacon-
- collection_type: open
  name: Plaid categories/
  slug: open-plaid-categories-
- collection_type: open
  name: Plaid cra/
  slug: open-plaid-cra-
- collection_type: open
  name: Plaid credit/
  slug: open-plaid-credit-
- collection_type: open
  name: Plaid deposit switch/
  slug: open-plaid-deposit-switch-
- collection_type: open
  name: Plaid employers/
  slug: open-plaid-employers-
- collection_type: open
  name: Plaid fdx/
  slug: open-plaid-fdx-
- collection_type: open
  name: Plaid identity/
  slug: open-plaid-identity-
- collection_type: open
  name: Plaid identity verification/
  slug: open-plaid-identity-verification-
- collection_type: open
  name: Plaid income/
  slug: open-plaid-income-
- collection_type: open
  name: Plaid institutions/
  slug: open-plaid-institutions-
- collection_type: open
  name: Plaid investments/
  slug: open-plaid-investments-
- collection_type: open
  name: Plaid item/
  slug: open-plaid-item-
- collection_type: open
  name: Plaid liabilities/
  slug: open-plaid-liabilities-
- collection_type: open
  name: Plaid link/
  slug: open-plaid-link-
- collection_type: open
  name: Plaid link delivery/
  slug: open-plaid-link-delivery-
- collection_type: open
  name: Plaid partner/
  slug: open-plaid-partner-
- collection_type: open
  name: Plaid payment initiation/
  slug: open-plaid-payment-initiation-
- collection_type: open
  name: Plaid payment profile/
  slug: open-plaid-payment-profile-
- collection_type: open
  name: Plaid processor/
  slug: open-plaid-processor-
- collection_type: open
  name: Plaid sandbox/
  slug: open-plaid-sandbox-
- collection_type: open
  name: Plaid signal/
  slug: open-plaid-signal-
- collection_type: open
  name: Plaid statements/
  slug: open-plaid-statements-
- collection_type: open
  name: Plaid transactions/
  slug: open-plaid-transactions-
- collection_type: open
  name: Plaid transfer/
  slug: open-plaid-transfer-
- collection_type: open
  name: Plaid wallet/
  slug: open-plaid-wallet-
- collection_type: open
  name: Plaid watchlist screening/
  slug: open-plaid-watchlist-screening-
common:
- group: build
  href: https://artifacts.apis.io/plaid/integrations/plaid-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/plaid-integration-edges.yml
- group: design
  href: https://artifacts.apis.io/plaid/rules/plaid-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/plaid-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/plaid/rules/plaid-rules.yml
  title: ''
  type: Spectral
  url: rules/plaid-rules.yml
- group: design
  href: https://artifacts.apis.io/plaid/rules/plaid-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/plaid-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/plaid/json-ld/plaid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/plaid-context.jsonld
- group: design
  href: https://artifacts.apis.io/plaid/vocabulary/plaid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/plaid-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/plaid/asyncapi/plaid-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/plaid-webhooks.yml
- group: design
  href: https://artifacts.apis.io/plaid/asyncapi/plaid-webhooks--asyncapi-original.yml
  title: ''
  type: Webhooks
  url: asyncapi/plaid-webhooks--asyncapi-original.yml
- group: agent
  href: https://artifacts.apis.io/plaid/mcp/plaid-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/plaid-mcp.yml
- group: other
  href: https://artifacts.apis.io/plaid/hosts/plaid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plaid-hosts.yml
- group: other
  href: https://artifacts.apis.io/plaid/vendors/plaid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plaid-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://plaid.com/careers/openings/security/security-engineer-grc/
- group: company
  title: ''
  type: Newsroom
  url: https://plaid.com/press/
- group: start
  title: ''
  type: GettingStarted
  url: https://plaid.com/docs/payment-initiation/payment-initiation-one-time/user-onboarding-and-account-funding/index.html
- group: auth
  href: https://artifacts.apis.io/plaid/scopes/plaid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/plaid-scopes.yml
- group: auth
  href: https://artifacts.apis.io/plaid/security/plaid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/plaid-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/plaid/skills/plaid-authorize-and-create-transfer.md
  title: ''
  type: AgentSkill
  url: skills/plaid-authorize-and-create-transfer.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/plaid/overview
- group: company
  title: ''
  type: Website
  url: https://plaid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plaid.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://plaid.com/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://plaid.com/docs/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plaid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plaid-
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Plaid
- group: company
  title: ''
  type: Blog
  url: https://plaid.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://plaid.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://plaid.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plaid.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plaid.com/legal/#privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://plaid.com/docs/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plaid.com/
- group: start
  title: ''
  type: Quickstarts
  url: https://plaid.com/docs/quickstart/
- group: start
  title: ''
  type: Sandbox
  url: https://plaid.com/docs/sandbox/
- group: design
  title: ''
  type: ErrorCodes
  url: https://plaid.com/docs/errors/
- group: build
  title: ''
  type: Libraries
  url: https://plaid.com/docs/api/libraries/
- group: design
  title: ''
  type: Versions
  url: https://plaid.com/docs/api/versioning/
- group: build
  title: ''
  type: PostmanCollection
  url: https://plaid.com/docs/api/postman/
- group: design
  title: ''
  type: Webhooks
  url: https://plaid.com/docs/api/webhooks/
- group: docs
  title: ''
  type: OpenAPISource
  url: https://github.com/plaid/plaid-openapi
- group: other
  title: ''
  type: CoreExchangeFDX
  url: https://github.com/plaid/core-exchange
- group: start
  title: ''
  type: Login
  url: https://dashboard.plaid.com/signin
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.plaid.com/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://plaid.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/plaid/agentic-access/plaid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plaid-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/plaid/security/plaid-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/plaid-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/plaid/security/plaid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plaid-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/plaid/authentication/plaid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plaid-authentication.yml
- group: start
  href: https://artifacts.apis.io/plaid/sandbox/plaid-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/plaid-sandbox.yml
- group: design
  href: https://artifacts.apis.io/plaid/conventions/plaid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plaid-conventions.yml
- group: operate
  href: https://artifacts.apis.io/plaid/changelog/plaid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plaid-changelog.yml
- group: build
  href: https://artifacts.apis.io/plaid/cli/plaid-cli.yml
  title: ''
  type: CLI
  url: cli/plaid-cli.yml
- group: design
  href: https://artifacts.apis.io/plaid/components/plaid-components.yml
  title: ''
  type: Components
  url: components/plaid-components.yml
- group: design
  href: https://artifacts.apis.io/plaid/data-model/plaid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plaid-data-model.yml
- group: build
  href: https://artifacts.apis.io/plaid/errors/plaid-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/plaid-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/plaid/errors/plaid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plaid-problem-types.yml
- group: build
  href: https://artifacts.apis.io/plaid/packages/plaid-packages.yml
  title: ''
  type: Packages
  url: packages/plaid-packages.yml
- group: build
  href: https://artifacts.apis.io/plaid/packages/plaid-packages.yml
  title: ''
  type: SDKs
  url: packages/plaid-packages.yml
- group: agent
  href: https://artifacts.apis.io/plaid/well-known/plaid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plaid-well-known.yml
- group: design
  href: https://artifacts.apis.io/plaid/conformance/plaid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plaid-conformance.yml
- group: auth
  href: https://artifacts.apis.io/plaid/security/plaid-trust-center.yml
  title: ''
  type: Compliance
  url: security/plaid-trust-center.yml
- group: design
  href: https://artifacts.apis.io/plaid/lifecycle/plaid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plaid-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://plaid.com/docs/api/versioning/
- group: design
  href: https://artifacts.apis.io/plaid/conventions/plaid-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/plaid-conventions.yml
- group: docs
  href: https://artifacts.apis.io/plaid/asyncapi/plaid-webhooks--asyncapi-original.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/plaid-webhooks--asyncapi-original.yml
- group: agent
  href: https://artifacts.apis.io/plaid/mcp/plaid-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/plaid-mcp.yml
- group: build
  href: https://artifacts.apis.io/plaid/mcp/plaid-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/plaid-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/plaid/skills/_index.yml
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/plaid/overlays/plaid-transfer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/plaid-transfer-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/plaid/llms/plaid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plaid-llms.txt
- group: commercial
  href: https://artifacts.apis.io/plaid/plans/plaid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plaid-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/plaid/rate-limits/plaid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/plaid-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/plaid/finops/plaid-finops.yml
  title: ''
  type: FinOps
  url: finops/plaid-finops.yml
created: '2024-07-07T00:00:00.000Z'
description: Plaid is a US financial-technology company and data-network aggregator that provides an API platform for businesses to securely connect with their users' bank and financial accounts. Plaid acts as the interface between 12,000+ financial institutions and third-party applications, powering bank-account verification (Auth, Balance, Identity), transactions and enrichment, income and asset verification, lending data (Assets, Liabilities, Investments, Consumer Report/CRA), risk and fraud tooling (Signal, Beacon, Monitor watchlist screening, Identity Verification), and money movement (Transfer, Payment Initiation, Virtual Accounts). Developers integrate through Plaid Link, a self-serve dashboard, client credentials, per-Item access tokens, and a publicly published OpenAPI definition. In the US voluntary open-finance landscape Plaid is an aggregator, and it also operates Core Exchange, its FDX-aligned data-access API for data providers, positioning it for CFPB 1033 open-banking rules.
features:
- Auth API for ACH account/routing verification (~$1.50/linked account)
- Identity API for KYC name/address/phone match (~$0.30/call)
- Income API for income verification
- Transactions API with /sync cursor for incremental pulls (~$0.45/call)
- Balance API for real-time balance check (~$0.10/call)
- Investments, Liabilities, Assets, Statements products
- Plaid Link prebuilt UI for OAuth bank connection
- 12,000+ supported financial institutions
- Sandbox environment with synthetic data
- Default 100 req/day/Item rate limit
- Webhooks for transaction updates and item events
- Pay-as-you-go default; Growth tier with discounts and SSO
- Custom contracts $1k-$10k+/month with 30-50% volume discounts at scale
- Plaid Beacon for fraud network signals
- Plaid Transfer for ACH payment initiation
- Plaid Signal for ACH risk scoring
- 'Core Exchange: Plaid''s FDX-aligned data-access API for data providers'
finops:
- has_sources: true
  method: derived
  name: Plaid Finops
  primary_unit: ''
  service_category: ''
  slug: plaid-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plaid.png
json_schemas:
- name: Account Contact entity
  property_count: 4
  slug: plaid-account-contact
- name: Payment Networks entity
  property_count: 2
  slug: plaid-account-payment-network-list
- name: Account With Details entity
  property_count: 0
  slug: plaid-account-with-details
- name: Accounts entity
  property_count: 2
  slug: plaid-accounts
- name: BetaPartnerCustomerV1CreateRequest
  property_count: 17
  slug: plaid-beta-partner-customer-v1-create-request
- name: Customer entity
  property_count: 1
  slug: plaid-customer
- name: LinkTokenCreateRequest
  property_count: 47
  slug: plaid-link-token-create-request
- name: PartnerCustomerCreateRequest
  property_count: 18
  slug: plaid-partner-customer-create-request
- name: ProcessorSignalEvaluateRequest
  property_count: 12
  slug: plaid-processor-signal-evaluate-request
- name: SignalEvaluateRequest
  property_count: 14
  slug: plaid-signal-evaluate-request
- name: Transactions entity
  property_count: 2
  slug: plaid-transactions
- name: TransferAuthorizationCreateRequest
  property_count: 26
  slug: plaid-transfer-authorization-create-request
jsonld:
- class_count: 120
  name: Plaid Context
  property_count: 167
  slug: plaid-context
layout: provider
mcp_servers:
- description: Plaid publishes TWO official MCP servers. (1) The Dashboard MCP server is a remote, hosted MCP endpoint at https://api.dashboard.plaid.com/mcp/ that exposes production diagnostics and Link analytics t
  name: Plaid MCP Server
  slug: plaid-mcp-yml
modified: '2026-09-23'
name: Plaid
nav: Providers
network: true
overview: 'Plaid publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Information API, Account Statements API, and 5 more. Tagged areas include Finance, Fintech, Open Banking, Bank Accounts, and Data Aggregation.


  The Plaid catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Plaid''s developer surface includes getting-started guide, documentation, API reference, engineering blog, pricing, support, sandbox, and 66 more developer resources.'
plans:
- name: Plaid Plans Pricing
  plan_count: 3
  slug: plaid-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 37
  name: Plaid Rate Limits
  slug: plaid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Plaid — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: plaid-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Plaid API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: plaid-rules
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Plaid API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: plaid-spectral-rules
scopes:
- name: Plaid Scopes
  scope_count: 5
  slug: plaid-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 83.4
  coverage:
    artifact_dirs: 40
    catalog_earned: 91.8
    catalog_earned_first_party: 24.0
    catalog_gap: 23.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 85.5
    contract_governance: 41.7
    contract_quality: 69.2
    developer_ergonomics: 79.2
    discoverability: 80.8
    operational_transparency: 86.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 84.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 14.3
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    - jurisdiction: US
      standard: fdx
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 57.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/plaid/plaid-2026-06-20T161613.png
security:
- kind: authentication
  name: Plaid Authentication
  slug: plaid-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Plaid Domain Security
  slug: plaid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plaid Vulnerability Disclosure
  slug: plaid-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Plaid Trust Center
  slug: plaid-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 3
skills:
- name: plaid-authorize-and-create-transfer
  slug: plaid-authorize-and-create-transfer
- name: plaid-link-and-fetch-accounts
  slug: plaid-link-and-fetch-accounts
- name: plaid-sync-transactions
  slug: plaid-sync-transactions
slug: plaid
tags:
- Finance
- Fintech
- Open Banking
- Bank Accounts
- Data Aggregation
- Payments
- United States
website: https://plaid.com/
---

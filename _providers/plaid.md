---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 577
  human_in_the_loop: 12
  name: Plaid Agentic Access
  operation_count: 577
  slug: plaid-agentic-access
  summary_line: 577 operations · 577 acting · 12 human-in-the-loop
api_count: 71
apis:
- description: The Plaid API from Plaid — 256 operation(s) for plaid.
  name: Plaid Plaid API
  slug: plaid-plaid-api
artifact_total: 93
asyncapis:
- description: AsyncAPI 2.6 specification for the Plaid webhook surface. Plaid delivers asynchronous notifications via HTTP POST to the URL registered on an Item (`webhook` parameter in `/link/token/create`) or conf
  name: Plaid Webhooks
  slug: plaid-webhooks--asyncapi-original
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
  name: API Collection
  slug: open-.refine-report
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
- group: agent
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
- group: agent
  title: ''
  type: LlmsText
  url: https://plaid.com/llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plaid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/plaid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plaid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plaid-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/plaid-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plaid-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plaid-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/plaid-cli.yml
- group: design
  title: ''
  type: Components
  url: components/plaid-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plaid-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/plaid-decline-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plaid-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/plaid-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/plaid-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plaid-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plaid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/plaid-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plaid-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://plaid.com/docs/api/versioning/
- group: design
  title: ''
  type: Idempotency
  url: conventions/plaid-conventions.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/plaid-webhooks--asyncapi-original.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plaid-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/plaid-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/plaid-transfer-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plaid-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/plaid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plaid-rate-limits.yml
- group: commercial
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
- name: Plaid Finops
  service_category: Fintech APIs
  slug: plaid-finops
graphqls:
- description: Plaid does not offer a native public GraphQL API. All Plaid APIs are REST-based, accessed via POST requests to `https://production.plaid.com` with JSON request/response bodies and `client_id` / `secre
  name: Plaid GraphQL
  slug: plaid-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plaid.png
layout: provider
mcp_servers:
- description: 'Plaid does not publish an official hosted/remote MCP server as of this round (no server advertised in Plaid docs, the plaid GitHub org, or the public MCP registries). This is a CANDIDATE tool surface '
  name: Plaid MCP Server
  slug: plaid-mcp-server
modified: '2026-07-23'
name: Plaid
nav: Providers
network: true
overview: 'Plaid publishes 1 API on the [APIs.io](https://apis.io/) network: Plaid API. Tagged areas include Financial, Fintech, Open Banking, Bank Accounts, and Data Aggregation.


  The Plaid catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Plaid''s developer surface includes documentation, engineering blog, pricing, support, sandbox, authentication, changelog, and 47 more developer resources.'
plans:
- name: Plaid Plans Pricing
  plan_count: 3
  slug: plaid-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Plaid Rate Limits
  slug: plaid-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Plaid API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: plaid-asyncapi-spectral-rules
- effective_rule_count: 49
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
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 30
    catalog_gap: 62.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 29.5
    contract_quality: 69.8
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 29.5
    operational_transparency: 57.9
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
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
    score: 63.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plaid/refs/heads/main/screenshots/plaid-2026-06-20T161613.png
security:
- kind: authentication
  name: Plaid Authentication
  slug: plaid-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Plaid Domain Security
  slug: plaid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plaid Trust Center
  slug: plaid-trust-center
  summary_line: SOC 2, ISO 27001
slug: plaid
tags:
- Financial
- Fintech
- Open Banking
- Bank Accounts
- Data Aggregation
- Payments
- United States
website: https://plaid.com/
---

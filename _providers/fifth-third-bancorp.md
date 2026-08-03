---
access_model:
  confidence: high
  label: Sandbox available · Partner onboarding
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - developer-portal
  - openapi
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.7
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Fifth Third Bancorp Agentic Access
  operation_count: 53
  slug: fifth-third-bancorp-agentic-access
  summary_line: 53 operations · 19 acting
api_count: 13
apis:
- description: Authentication for the Newline by Fifth Third platform. A client exchanges a refresh token for an access token by POSTing a JWS whose payload carries the Program UID (sub) and current epoch time (iat)
  name: Newline Auth API
  slug: newline-auth-api
- description: Create, list, retrieve, update, and archive the Customers who hold accounts on a Newline program. Handles personally identifiable information (PII), Tax Identifier/SSN capture and validation, customer
  name: Newline Customers API
  slug: newline-customers-api
- description: Onboard Customers onto Newline banking Products and manage the resulting Customer Product records. Submitting a Customer Product confirms the Customer is ready for account opening, locks their PII, an
  name: Newline Customer Products API
  slug: newline-customer-products-api
- description: List and retrieve the banking Products configured for a Newline program, including each Product's configuration, availability, required Customer Profile fields, and associated metadata. Products defin
  name: Newline Products API
  slug: newline-products-api
- description: List and retrieve Pools, the constructs that group Synthetic and Custodial Accounts and report aggregate asset balances across the accounts associated with them. Pools give program operators a roll-up
  name: Newline Pools API
  slug: newline-pools-api
- description: Retrieve the FDIC-insured Custodial Accounts held by Fifth Third Bank on behalf of onboarded Customers, including active and archived accounts, their balances, and daily closing balances. Provides lis
  name: Newline Custodial Accounts API
  slug: newline-custodial-accounts-api
- description: Create and manage Synthetic Accounts, the ledger accounts that route money through Newline. Includes liability accounts in the general category and external accounts in the ach_external, wire_external
  name: Newline Synthetic Accounts API
  slug: newline-synthetic-accounts-api
- description: Initiate, list, retrieve, and cancel Transfers that move assets between Synthetic Accounts across payment rails — ACH, wire, Real-Time Payments (RTP), and internal book transfers. Balance and access c
  name: Newline Transfers API
  slug: newline-transfers-api
- description: Orchestrate Combined Transfers, which bundle multiple related money movements into a single coordinated operation across a program's Synthetic Accounts. Provides endpoints to create, list, and retriev
  name: Newline Combined Transfers API
  slug: newline-combined-transfers-api
- description: List and retrieve Transactions and their Transaction Events, and approve or deny pending Transactions before execution. Transaction Events expose the individual steps required to complete a Transactio
  name: Newline Transactions API
  slug: newline-transactions-api
- description: Create, list, and retrieve Returns — the reversal of settled payments such as ACH returns — on the Newline platform. Returns move funds back across the originating rail and update the associated Trans
  name: Newline Returns API
  slug: newline-returns-api
- description: Create and manage Virtual Reference Numbers (VRNs), the unique account and routing number pairs that let a program receive inbound ACH, wire, and Real-Time Payments and attribute them to a specific Sy
  name: Newline Virtual Reference Numbers API
  slug: newline-virtual-reference-numbers-api
- description: Simulation endpoints for the Newline sandbox environment that let developers mock transactions and transfers, exercise error scenarios, and clear sandbox state while building against the platform. The
  name: Newline Sandbox API
  slug: newline-sandbox-api
artifact_total: 18
asyncapis:
- description: ''
  name: Fifth Third Bancorp Newline Webhooks
  slug: fifth-third-bancorp-newline-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fifth-third-bancorp-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fifth-third-bancorp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.53.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.newline53.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.newline53.com/docs/welcome
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.newline53.com/openapi/newline-platform-api.json
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/newline53
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newline53
- group: operate
  title: ''
  type: StatusPage
  url: https://status.newline53.com
- group: operate
  title: ''
  type: Changelog
  url: https://developers.newline53.com/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.53.com/content/fifth-third/en/privacy-security.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fifth-third-bank
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.53.com/
- group: other
  title: ''
  type: TreasuryManagement
  url: https://www.53.com/content/fifth-third/en/commercial-banking/payments-and-treasury-management.html
- group: other
  title: ''
  type: EmbeddedFinance
  url: https://newline53.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fifth-third-bancorp-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fifth-third-bancorp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fifth-third-bancorp-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/fifth-third-bancorp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fifth-third-bancorp-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fifth-third-bancorp-newline-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fifth-third-bancorp-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/fifth-third-bancorp-newline-platform-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/fifth-third-bancorp-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fifth-third-bancorp-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/fifth-third-bancorp-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fifth-third-bancorp-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fifth-third-bancorp-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fifth-third-bancorp-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fifth-third-bancorp-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fifth-third-bancorp-data-model.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.newline53.com/docs/quickstart-guide-completing-a-transfer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.newline53.com/docs/terms-conditions
created: '2026-03-21'
description: 'Fifth Third Bancorp is a diversified super-regional financial services company providing commercial banking, branch banking, consumer lending, and wealth and asset management services across multiple U.S. states. Its embedded-finance arm, Newline by Fifth Third (built on the 2023 Rize Money acquisition), operates a documented, API-first Banking-as-a-Service platform: the Newline Platform API exposes payments (ACH, wire, Real-Time Payments/RTP, book transfers), FDIC-insured deposit and custodial accounts, synthetic accounts, virtual reference numbers, card issuing, customer/KYC onboarding, transactions, returns, and webhook/message-queue notifications so fintechs and enterprises can embed financial products directly with Fifth Third Bank.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fifth-third-bancorp.png
layout: provider
mcp_servers:
- description: ''
  name: fifth-third-bancorp-mcp.yml
  slug: fifth-third-bancorp-mcpyml
modified: '2026-07-23'
name: Fifth Third Bancorp
nav: Providers
network: true
overview: 'Fifth Third Bancorp publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Newline Auth API, Newline Customers API, Newline Customer Products API, and 10 more. Tagged areas include Banking, United States, Embedded Finance, Banking as a Service, and Payments.


  The Fifth Third Bancorp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fifth Third Bancorp''s developer surface includes authentication, documentation, changelog, sandbox, getting-started guide, and 29 more developer resources.'
press:
- date: '2026-05-25'
  title: Fifth Third Bancorp Investor Meetings
  url: http://s23.q4cdn.com/252949160/files/doc_presentation/2025/2025-European-Roadshow-Deck-vF.pdf
- date: '2026-05-25'
  title: Fifth Third and Brex Partner to Bring AI-Powered Finance ...
  url: https://www.53.com/content/fifth-third/en/media-center/press-releases/2025/press-release-2025-12-09.html
- date: '2026-05-25'
  title: Fifth Third Sees 'Pretty Remarkable' AI Ability to Lower Costs
  url: https://www.bloomberg.com/news/articles/2026-03-11/fifth-third-sees-pretty-remarkable-outcome-of-ai-to-lower-cost
- date: '2026-05-25'
  title: Financial Information - Quarterly and Annual Reports
  url: https://ir.53.com/financial-information/quarterly-and-annual-reports/default.aspx
- date: '2026-05-25'
  title: Fifth Third Bank Welcomes Back Art Weston
  url: https://ir.53.com/news/news-details/2022/Fifth-Third-Bank-Welcomes-Back-Art-Weston/default.aspx
random_paper: 94
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 62.4
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fifth-third-bancorp/refs/heads/main/screenshots/fifth-third-bancorp-2026-06-20T181156.png
security:
- kind: authentication
  name: Fifth Third Bancorp Authentication
  slug: fifth-third-bancorp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fifth Third Bancorp Domain Security
  slug: fifth-third-bancorp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fifth-third-bancorp
tags:
- Banking
- United States
- Embedded Finance
- Banking as a Service
- Payments
- ACH
- Real-Time Payments
- Deposits
- Card Issuing
- Commercial Banking
- Consumer Lending
- Wealth Management
- Treasury Management
- Super-Regional Bank
- Fortune 500
website: https://www.53.com/
---

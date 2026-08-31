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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Fifth Third Bancorp Agentic Access
  operation_count: 53
  slug: fifth-third-bancorp-agentic-access
  summary_line: 53 operations · 19 acting
api_count: 1
apis:
- description: The Authentication section explains how to securely interact with Newline's API using access tokens and static IP addresses. Learn how to generate and refresh tokens to access protected resources. **E
  name: Fifth Third Bancorp Auth API
  slug: fifth-third-bancorp-auth-api
- description: The Combined Transfers endpoint allows clients to create both a transfer and a counterparty in a single API call. This simplifies the process by eliminating the need to first create an external synthe
  name: Fifth Third Bancorp Combined Transfers API
  slug: fifth-third-bancorp-combined-transfers-api
- description: 'Fifth Third Bank holds Custodial Accounts and represents funds managed for Customers. Through these endpoints, you can manage balances and track account statuses. **Endpoints:** - GET [List Custodial '
  name: Fifth Third Bancorp Custodial Accounts API
  slug: fifth-third-bancorp-custodial-accounts-api
- description: Customer Products link Customers to financial products. This section outlines how to onboard customers, manage their product relationships, and track statuses. **Endpoints:** - GET [List Customer Prod
  name: Fifth Third Bancorp Customer Products API
  slug: fifth-third-bancorp-customer-products-api
- description: The Customers section provides details on managing end-user accounts. Learn how to create, update, and archive customer records and onboard them to financial products while meeting KYC/AML requirement
  name: Fifth Third Bancorp Customers API
  slug: fifth-third-bancorp-customers-api
- description: 'Pools group multiple Customers for asset sharing and distributed account ownership. Each Pool is unique to a Customer or program. **Endpoints:** - GET [List Pools: GET /pools](https://developers.newli'
  name: Fifth Third Bancorp Pools API
  slug: fifth-third-bancorp-pools-api
- description: 'Products represent financial services available in your program. Discover onboarding requirements, prerequisites, and detailed product configurations. **Endpoints:** - GET [List Products: GET /product'
  name: Fifth Third Bancorp Products API
  slug: fifth-third-bancorp-products-api
- description: 'The Returns endpoints help initiate, track, and manage returns of received and originated payments. These endpoints are accessible within the Sandbox and Production environments. **Endpoints:** - GET '
  name: Fifth Third Bancorp Returns API
  slug: fifth-third-bancorp-returns-api
- description: 'The Sandbox section provides tools to test and simulate interactions with the Newline API in a controlled environment. **Endpoints:** - POST [Simulate a Transaction: POST /sandbox/mock_transactions](h'
  name: Fifth Third Bancorp Sandbox API
  slug: fifth-third-bancorp-sandbox-api
- description: 'Synthetic Accounts serve as the foundation for asset tracking in Newline. They allow for flexible configurations tailored to your program. **Endpoints:** - GET [List Synthetic Account Types: GET /synt'
  name: Fifth Third Bancorp Synthetic Accounts API
  slug: fifth-third-bancorp-synthetic-accounts-api
- description: 'Transactions represent asset movements, such as ACH payments, wire transfers, or card purchases. Track transaction statuses and events through these endpoints. **Endpoints:** - GET [List Transactions:'
  name: Fifth Third Bancorp Transactions API
  slug: fifth-third-bancorp-transactions-api
- description: 'Transfers facilitate the movement of assets between accounts, enabling transactions such as payments and withdrawals. **Endpoints:** - GET [List Transfers: GET /transfers](https://developers.newline53'
  name: Fifth Third Bancorp Transfers API
  slug: fifth-third-bancorp-transfers-api
- description: 'VRNs act as aliases for accounts, enabling unique use cases like accounts receivable segmentation or reconciliation. **Endpoints:** - GET [List Virtual Reference Numbers: GET /virtual_reference_number'
  name: Fifth Third Bancorp Virtual Reference Numbers API
  slug: fifth-third-bancorp-virtual-reference-numbers-api
artifact_total: 19
asyncapis:
- description: ''
  name: Fifth Third Bancorp Newline Webhooks
  slug: fifth-third-bancorp-newline-webhooks
collections:
- collection_type: open
  name: Newline Platform API
  slug: open-newline-platform-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fifth-third-bancorp-capability-edges.yml
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
  type: AgentSkills
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
  name: Fifth Third Bancorp MCP Server
  slug: fifth-third-bancorp-mcp-server
modified: '2026-07-23'
name: Fifth Third Bancorp
nav: Providers
network: true
overview: 'Fifth Third Bancorp publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Combined Transfers API, Custodial Accounts API, and 10 more. Tagged areas include Banking, United States, Embedded Finance, Banking as a Service, and Payments.


  The Fifth Third Bancorp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fifth Third Bancorp''s developer surface includes authentication, documentation, changelog, sandbox, getting-started guide, and 30 more developer resources.'
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
random_paper: 9
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 86.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.4
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 61.9
    discoverability: 61.1
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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

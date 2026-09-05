---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 82
  human_in_the_loop: 5
  name: Lightspark Agentic Access
  operation_count: 132
  slug: lightspark-agentic-access
  summary_line: 132 operations · 82 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: 'Endpoints for creating and managing agents (experimental), called by the partner''s backend using platform credentials. Covers the full agent lifecycle: creation, policy configuration, pausing, deletio'
  name: Lightspark Agent Management API
  slug: lightspark-agent-management-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints called by the agent itself using its own credentials (obtained via device code redemption). Scoped to the agent's associated customer — all requests automatically operate on behalf of that c
  name: Lightspark Agent Operations API
  slug: lightspark-agent-operations-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints to programmatically manage API tokens
  name: Lightspark API Tokens API
  slug: lightspark-api-tokens-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: The Available UMA Providers API from Lightspark — 1 operation(s) for available uma providers.
  name: Lightspark Available UMA Providers API
  slug: lightspark-available-uma-providers-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Card management endpoints. Issue debit cards against an internal account, freeze / unfreeze, close, manage card funding sources, and list card transactions.
  name: Lightspark Cards API
  slug: lightspark-cards-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for verifying a customer's email and phone via one-time codes. Required only for customers whose payment provider mandates contact verification (e.g. EU customers); other providers return 40
  name: Lightspark Contact Verification API
  slug: lightspark-contact-verification-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for creating and confirming quotes for cross-currency transfers
  name: Lightspark Cross-Currency Transfers API
  slug: lightspark-cross-currency-transfers-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Customer management endpoints for creating and updating customer information
  name: Lightspark Customers API
  slug: lightspark-customers-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for discovering available payment rails, banks, and providers for a given country and currency corridor.
  name: Lightspark Discoveries API
  slug: lightspark-discoveries-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for uploading and managing verification documents for customers and beneficial owners. Supports KYC and KYB document requirements.
  name: Lightspark Documents API
  slug: lightspark-documents-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for registering and verifying end-user authentication credentials (email OTP, OAuth, passkey) used to sign Embedded Wallet actions.
  name: Lightspark Embedded Wallet Auth API
  slug: lightspark-embedded-wallet-auth-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for retrieving cached foreign exchange rates. Rates are cached for approximately 5 minutes and include platform-specific fees.
  name: Lightspark Exchange Rates API
  slug: lightspark-exchange-rates-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: External account management endpoints for creating and managing external bank accounts
  name: Lightspark External Accounts API
  slug: lightspark-external-accounts-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Internal account management endpoints for creating and managing internal accounts
  name: Lightspark Internal Accounts API
  slug: lightspark-internal-accounts-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for creating, claiming and managing UMA invitations
  name: Lightspark Invitations API
  slug: lightspark-invitations-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for Know Your Customer (KYC) and Know Your Business (KYB) verification, including managing beneficial owners and triggering verification for customers.
  name: Lightspark KYC/KYB Verifications API
  slug: lightspark-kyc-kyb-verifications-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Platform configuration endpoints for managing global settings. You can also configure these settings in the Grid dashboard.
  name: Lightspark Platform Configuration API
  slug: lightspark-platform-configuration-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for transferring funds between internal and external accounts with the same currency
  name: Lightspark Same-Currency Transfers API
  slug: lightspark-same-currency-transfers-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints to trigger test cases in sandbox
  name: Lightspark Sandbox API
  slug: lightspark-sandbox-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Stablecoin issuance endpoints. Link provider accounts, register provider-created stablecoins, create mint/burn quotes, execute them, and track the resulting operations.
  name: Lightspark Stablecoins API
  slug: lightspark-stablecoins-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for authorizing money-movement operations that require Strong Customer Authentication. Relevant only for customers in a region where SCA is required (e.g. EU); customers outside SCA-regulate
  name: Lightspark Strong Customer Authentication API
  slug: lightspark-strong-customer-authentication-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Endpoints for retrieving transaction information
  name: Lightspark Transactions API
  slug: lightspark-transactions-api
- baseURL: https://api.lightspark.com/grid/2025-10-13
  baseurl_source: declared
  description: Webhook endpoints and configuration for receiving notifications
  name: Lightspark Webhooks API
  slug: lightspark-webhooks-api
artifact_total: 76
asyncapis:
- description: ''
  name: Lightspark Grid Webhooks
  slug: lightspark-grid-webhooks
collections:
- collection_type: postman
  name: Grid Agent Management API
  slug: postman-lightspark-agent-management-api
- collection_type: postman
  name: Grid Agent Management Agent Operations API
  slug: postman-lightspark-agent-operations-api
- collection_type: postman
  name: Grid Agent Management API Tokens API
  slug: postman-lightspark-api-tokens-api
- collection_type: postman
  name: Grid Agent Management Available UMA Providers API
  slug: postman-lightspark-available-uma-providers-api
- collection_type: postman
  name: Grid Agent Management Cards API
  slug: postman-lightspark-cards-api
- collection_type: postman
  name: Grid Agent Management Contact Verification API
  slug: postman-lightspark-contact-verification-api
- collection_type: postman
  name: Grid Agent Management Cross-Currency Transfers API
  slug: postman-lightspark-cross-currency-transfers-api
- collection_type: postman
  name: Grid Agent Management Customers API
  slug: postman-lightspark-customers-api
- collection_type: postman
  name: Grid Agent Management Discoveries API
  slug: postman-lightspark-discoveries-api
- collection_type: postman
  name: Grid Agent Management Documents API
  slug: postman-lightspark-documents-api
- collection_type: postman
  name: Grid Agent Management Embedded Wallet Auth API
  slug: postman-lightspark-embedded-wallet-auth-api
- collection_type: postman
  name: Grid Agent Management Exchange Rates API
  slug: postman-lightspark-exchange-rates-api
- collection_type: postman
  name: Grid Agent Management External Accounts API
  slug: postman-lightspark-external-accounts-api
- collection_type: postman
  name: Grid Agent Management Internal Accounts API
  slug: postman-lightspark-internal-accounts-api
- collection_type: postman
  name: Grid Agent Management Invitations API
  slug: postman-lightspark-invitations-api
- collection_type: postman
  name: Grid Agent Management KYC/KYB Verifications API
  slug: postman-lightspark-kyc-kyb-verifications-api
- collection_type: postman
  name: Grid Agent Management Platform Configuration API
  slug: postman-lightspark-platform-configuration-api
- collection_type: postman
  name: Grid Agent Management Same-Currency Transfers API
  slug: postman-lightspark-same-currency-transfers-api
- collection_type: postman
  name: Grid Agent Management Sandbox API
  slug: postman-lightspark-sandbox-api
- collection_type: postman
  name: Grid Agent Management Stablecoins API
  slug: postman-lightspark-stablecoins-api
- collection_type: postman
  name: Grid Agent Management Strong Customer Authentication API
  slug: postman-lightspark-strong-customer-authentication-api
- collection_type: postman
  name: Grid Agent Management Transactions API
  slug: postman-lightspark-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grid Agent Management API
  slug: open-lightspark-agent-management-api
- collection_type: open
  name: Grid Agent Management Agent Operations API
  slug: open-lightspark-agent-operations-api
- collection_type: open
  name: Grid Agent Management API Tokens API
  slug: open-lightspark-api-tokens-api
- collection_type: open
  name: Grid Agent Management Available UMA Providers API
  slug: open-lightspark-available-uma-providers-api
- collection_type: open
  name: Grid Agent Management Cards API
  slug: open-lightspark-cards-api
- collection_type: open
  name: Grid Agent Management Contact Verification API
  slug: open-lightspark-contact-verification-api
- collection_type: open
  name: Grid Agent Management Cross-Currency Transfers API
  slug: open-lightspark-cross-currency-transfers-api
- collection_type: open
  name: Grid Agent Management Customers API
  slug: open-lightspark-customers-api
- collection_type: open
  name: Grid Agent Management Discoveries API
  slug: open-lightspark-discoveries-api
- collection_type: open
  name: Grid Agent Management Documents API
  slug: open-lightspark-documents-api
- collection_type: open
  name: Grid Agent Management Embedded Wallet Auth API
  slug: open-lightspark-embedded-wallet-auth-api
- collection_type: open
  name: Grid Agent Management Exchange Rates API
  slug: open-lightspark-exchange-rates-api
- collection_type: open
  name: Grid Agent Management External Accounts API
  slug: open-lightspark-external-accounts-api
- collection_type: open
  name: Grid Agent Management Internal Accounts API
  slug: open-lightspark-internal-accounts-api
- collection_type: open
  name: Grid Agent Management Invitations API
  slug: open-lightspark-invitations-api
- collection_type: open
  name: Grid Agent Management KYC/KYB Verifications API
  slug: open-lightspark-kyc-kyb-verifications-api
- collection_type: open
  name: Grid Agent Management Platform Configuration API
  slug: open-lightspark-platform-configuration-api
- collection_type: open
  name: Grid Agent Management Same-Currency Transfers API
  slug: open-lightspark-same-currency-transfers-api
- collection_type: open
  name: Grid Agent Management Sandbox API
  slug: open-lightspark-sandbox-api
- collection_type: open
  name: Grid Agent Management Stablecoins API
  slug: open-lightspark-stablecoins-api
- collection_type: open
  name: Grid Agent Management Strong Customer Authentication API
  slug: open-lightspark-strong-customer-authentication-api
- collection_type: open
  name: Grid Agent Management Transactions API
  slug: open-lightspark-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lightspark-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lightspark-grid-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/lightsparkdev/grid-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/lightsparkdev/grid-api/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lightspark/overview
- group: company
  title: ''
  type: Website
  url: https://lightspark.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lightspark.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lightspark.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lightspark.com/api-reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lightspark.com/global-p2p/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.lightspark.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lightspark.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.lightspark.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightsparkdev
- group: start
  title: ''
  type: SignUp
  url: https://app.lightspark.com
- group: start
  title: ''
  type: Login
  url: https://app.lightspark.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lightspark.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lightspark.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightspark.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lightspark.com/changelog
- group: operate
  title: ''
  type: ChangeLogArtifact
  url: changelog/lightspark-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.lightspark.com/api-reference/environments
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightspark-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lightspark.com/news/lightspark/expanding-our-bug-bounty-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lightspark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lightspark-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/lightspark-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightspark-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightspark-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightspark-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightspark-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightspark-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightspark-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lightspark-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightspark-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lightspark-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lightspark-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightspark-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lightspark-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightspark-error-codes.yml
- group: other
  title: ''
  type: ProblemTypes
  url: errors/lightspark-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightspark-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lightspark-grid-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightspark-well-known.yml
created: '2026-07-17'
description: 'Lightspark builds global money-movement infrastructure on open payment networks. Its developer product is the Grid API — a dated-version REST API (OpenAPI 3.1, 104 paths, 564 schemas, 12 webhooks) for cross-border payouts, on/off-ramps, stablecoins, embedded wallets, card issuing, KYC/KYB verification and payments to Universal Money Addresses ($user@domain). Grid is unusually agent-native: it ships a first-class agent surface with device-code credentials, per-agent policy and human-in-the-loop approvals, a hosted MCP server, a published Claude agent skill, an open-source CLI, and generated TypeScript and Kotlin SDKs. Lightspark also operates the Spark and UMA protocol stacks and is backed by a16z, Matrix Partners, Paradigm and Ribbit Capital.'
image: https://images.prismic.io/lightspark-web/ageHhqYofJOwHSa5_og-05-2026.png?auto=format,compress
layout: provider
mcp_servers:
- description: ''
  name: Lightspark MCP Server
  slug: lightspark-mcp-server
modified: '2026-07-19'
name: Lightspark
nav: Providers
network: true
overview: 'Lightspark publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Agent Management API, Agent Operations API, API Tokens API, and 20 more. Tagged areas include Company, Payments, Cross-Border Payments, Stablecoins, and Bitcoin.


  The Lightspark catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Lightspark''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 38 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Lightspark API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 4
  slug: lightspark-grid-spectral
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 72.7
    contract_quality: 67.4
    developer_ergonomics: 81.5
    discoverability: 75.9
    governance: 72.7
    operational_transparency: 60.5
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightspark/refs/heads/main/screenshots/lightspark-2026-07-25T225132.png
security:
- kind: authentication
  name: Lightspark Authentication
  slug: lightspark-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Lightspark Domain Security
  slug: lightspark-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lightspark Vulnerability Disclosure
  slug: lightspark-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Lightspark Trust Center
  slug: lightspark-trust-center
  summary_line: SOC 2 Type 1
slug: lightspark
tags:
- Company
- Payments
- Cross-Border Payments
- Stablecoins
- Bitcoin
- Lightning Network
- Embedded Finance
- Agentic Payments
- Cards
- KYC
- Financial-Services
- Foreign Exchange
website: https://lightspark.com
---

---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: The long-standing public Uphold API at api.uphold.com/v0 — tickers and exchange rates, supported currencies and assets, plus OAuth 2.0 authenticated access to a member's cards, transactions and accoun
  name: Uphold Public API (v0)
  slug: uphold-public-api-v0
- description: Anonymous, read-only Model Context Protocol server published by Uphold at developer.uphold.com/mcp over streamable HTTP. Exposes three tools (documentation search, a virtualized read-only docs filesys
  name: Uphold Documentation MCP Server
  slug: uphold-documentation-mcp-server
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Accounts.
  name: Uphold Accounts API
  slug: uphold-accounts-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Assets, networks and rails.
  name: Uphold Assets API
  slug: uphold-assets-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Authentication.
  name: Uphold Authentication API
  slug: uphold-authentication-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: User capabilities.
  name: Uphold Capabilities API
  slug: uphold-capabilities-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Countries.
  name: Uphold Countries API
  slug: uphold-countries-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: External accounts.
  name: Uphold External accounts API
  slug: uphold-external-accounts-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Files.
  name: Uphold Files API
  slug: uphold-files-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: General.
  name: Uphold General API
  slug: uphold-general-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: The Ingestions API from Uphold — 0 operation(s) for ingestions.
  name: Uphold Ingestions API
  slug: uphold-ingestions-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Business User's KYB.
  name: Uphold KYB API
  slug: uphold-kyb-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Individual User's KYC.
  name: Uphold KYC API
  slug: uphold-kyc-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: KYC sharing.
  name: Uphold KYC sharing API
  slug: uphold-kyc-sharing-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Metadata.
  name: Uphold Metadata API
  slug: uphold-metadata-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Payment.
  name: Uphold Payment API
  slug: uphold-payment-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Portfolio.
  name: Uphold Portfolio API
  slug: uphold-portfolio-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Statements.
  name: Uphold Statements API
  slug: uphold-statements-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Sumsub KYC Connector.
  name: Uphold Sumsub API
  slug: uphold-sumsub-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: User terms of service.
  name: Uphold Terms of service API
  slug: uphold-terms-of-service-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Transactions.
  name: Uphold Transactions API
  slug: uphold-transactions-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Travel rule.
  name: Uphold Travel rule API
  slug: uphold-travel-rule-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Users.
  name: Uphold Users API
  slug: uphold-users-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Veriff KYC Connector.
  name: Uphold Veriff API
  slug: uphold-veriff-api
- baseURL: https://api.enterprise.uphold.com
  baseurl_source: declared
  description: Webhooks.
  name: Uphold Webhooks API
  slug: uphold-webhooks-api
artifact_total: 56
asyncapis:
- description: ''
  name: Uphold Core Webhooks
  slug: uphold-core-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Core Accounts API
  slug: open-uphold-accounts-api
- collection_type: open
  name: Uphold Assets API
  slug: open-uphold-assets-api
- collection_type: open
  name: Core Authentication API
  slug: open-uphold-authentication-api
- collection_type: open
  name: Core Capabilities API
  slug: open-uphold-capabilities-api
- collection_type: open
  name: Core Countries API
  slug: open-uphold-countries-api
- collection_type: open
  name: Core External accounts API
  slug: open-uphold-external-accounts-api
- collection_type: open
  name: Core Files API
  slug: open-uphold-files-api
- collection_type: open
  name: Market Pulse General API
  slug: open-uphold-general-api
- collection_type: open
  name: KYC Connectors Ingestions API
  slug: open-uphold-ingestions-api
- collection_type: open
  name: Core KYB API
  slug: open-uphold-kyb-api
- collection_type: open
  name: Uphold KYC API
  slug: open-uphold-kyc-api
- collection_type: open
  name: Topper KYC sharing API
  slug: open-uphold-kyc-sharing-api
- collection_type: open
  name: Core Metadata API
  slug: open-uphold-metadata-api
- collection_type: open
  name: Widget Payment API
  slug: open-uphold-payment-api
- collection_type: open
  name: Core Portfolio API
  slug: open-uphold-portfolio-api
- collection_type: open
  name: Core Statements API
  slug: open-uphold-statements-api
- collection_type: open
  name: KYC Connectors Sumsub API
  slug: open-uphold-sumsub-api
- collection_type: open
  name: Core Terms of service API
  slug: open-uphold-terms-of-service-api
- collection_type: open
  name: Core Transactions API
  slug: open-uphold-transactions-api
- collection_type: open
  name: Widget Travel rule API
  slug: open-uphold-travel-rule-api
- collection_type: open
  name: Core Users API
  slug: open-uphold-users-api
- collection_type: open
  name: KYC Connectors Veriff API
  slug: open-uphold-veriff-api
- collection_type: open
  name: Core Webhooks API
  slug: open-uphold-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/uphold-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/uphold/docs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/uphold/docs/releases
- group: other
  title: ''
  type: Overlay
  url: overlays/uphold-core-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://uphold.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uphold.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uphold.com/rest-apis/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uphold.com/rest-apis/core-api/concepts
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uphold.com/get-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://developer.uphold.com/get-started/make-your-first-api-call
- group: operate
  title: ''
  type: Support
  url: https://support.uphold.com/
- group: company
  title: ''
  type: Blog
  url: https://uphold.com/en-us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uphold
- group: commercial
  title: ''
  type: Pricing
  url: https://uphold.com/en-us/get-started/service-fees
- group: start
  title: ''
  type: SignUp
  url: https://portal.enterprise.uphold.com/
- group: start
  title: ''
  type: Login
  url: https://portal.enterprise.uphold.com/
- group: commercial
  title: ''
  type: DeveloperAgreement
  url: https://uphold.com/en-us/legal/developer-agreement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uphold.com/en-us/legal/membership-agreement/usa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uphold.com/en-us/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/uphold/workspace/enterprise-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uphold.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.uphold.com/rest-apis/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uphold-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uphold-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://uphold.com/en-us/get-started/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uphold-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/uphold-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://uphold.com/en-us/get-started/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uphold-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/uphold-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uphold-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uphold-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/uphold-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uphold-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uphold-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uphold-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uphold-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uphold-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uphold-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/uphold-decline-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uphold-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/uphold-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uphold-packages.yml
- group: design
  title: ''
  type: Components
  url: components/uphold-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uphold-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uphold-core-webhooks.yml
created: '2026-08-05'
description: Uphold is a multi-asset digital money platform and regulated crypto exchange that lets consumers and businesses hold, trade, send and spend more than 300 cryptocurrencies, national currencies and precious metals from a single account. Its Enterprise API Suite ("Move on chain") is a modular set of OpenAPI 3.1 REST APIs — Core, Widgets, Topper, Market Pulse and KYC Connector — that partners embed to onboard and KYC/KYB-verify users, move value across bank rails (ACH, FedNow/RTP, Wire, FPS, SEPA), debit and credit cards, alternative payment methods (Apple Pay, PayPal) and 50+ blockchain networks, and to run buy/sell, trade, send, portfolio, statements and FATF Travel Rule flows. Uphold also runs a public legacy market-data and wallet API at api.uphold.com/v0, publishes embeddable Payment, KYC and Travel Rule widgets, a Svix-backed webhook event surface, a full Sandbox with test helpers, a public Postman workspace, an llms.txt, an A2A agent card and a documentation MCP server.
image: https://cdn.prod.website-files.com/65116a8935747aeda81c6865/65a8ffa13ea101b31a905d2f_UPHOLD%20LOGO-2.png
layout: provider
mcp_servers:
- description: ''
  name: Uphold
  slug: uphold
modified: '2026-08-05'
name: Uphold
nav: Providers
network: true
overview: 'Uphold publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Assets API, Authentication API, and 20 more. Tagged areas include Company, Cryptocurrency, Digital Assets, Payments, and Banking.


  The Uphold catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uphold''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 40 more developer resources.'
random_paper: 1
scopes:
- name: Uphold Scopes
  scope_count: 64
  slug: uphold-scopes
  summary_line: 64 scopes · clientCredentials
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 66.0
    developer_ergonomics: 81.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 68.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uphold/refs/heads/main/screenshots/uphold-2026-08-17T081941.png
security:
- kind: authentication
  name: Uphold Authentication
  slug: uphold-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Uphold Domain Security
  slug: uphold-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Uphold Vulnerability Disclosure
  slug: uphold-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Uphold Trust Center
  slug: uphold-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, PCI DSS
slug: uphold
tags:
- Company
- Cryptocurrency
- Digital Assets
- Payments
- Banking
- Fintech
- KYC
- Compliance
- Crypto Exchange
- Market Data
- Embedded Finance
- Travel Rule
- Webhook
- agent-native
website: https://uphold.com/
---

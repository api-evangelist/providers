---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Bvnk Agentic Access
  operation_count: 54
  slug: bvnk-agentic-access
  summary_line: 54 operations · 20 acting
api_count: 17
apis:
- description: The BVNK Cards API issues and manages virtual cards linked to BVNK wallets — card creation, renewal, cancellation, freeze/unfreeze, spend limits, eligibility checks, sensitive-card-detail tokens, card
  name: BVNK Cards API
  slug: bvnk-cards-api
- description: Create and manage addresses
  name: BVNK Address API
  slug: bvnk-address-api
- description: Create and manage asset pools
  name: BVNK Asset Pool API
  slug: bvnk-asset-pool-api
- description: The Channels API from BVNK — 4 operation(s) for channels.
  name: BVNK Channels API
  slug: bvnk-channels-api
- description: The Currencies API from BVNK — 3 operation(s) for currencies.
  name: BVNK Currencies API
  slug: bvnk-currencies-api
- description: Create and manage data exports
  name: BVNK Export API
  slug: bvnk-export-api
- description: Network fee estimation
  name: BVNK Fee API
  slug: bvnk-fee-api
- description: Create and manage key-pairs
  name: BVNK Key Pair API
  slug: bvnk-key-pair-api
- description: The Merchant IDs API from BVNK — 1 operation(s) for merchant ids.
  name: BVNK Merchant IDs API
  slug: bvnk-merchant-ids-api
- description: The Network API from BVNK — 1 operation(s) for network.
  name: BVNK Network API
  slug: bvnk-network-api
- description: The Payments API from BVNK — 3 operation(s) for payments.
  name: BVNK Payments API
  slug: bvnk-payments-api
- description: The Return API from BVNK — 1 operation(s) for return.
  name: BVNK Return API
  slug: bvnk-return-api
- description: Manage screening requests
  name: BVNK Screening API
  slug: bvnk-screening-api
- description: The Trading and Conversions API from BVNK — 4 operation(s) for trading and conversions.
  name: BVNK Trading and Conversions API
  slug: bvnk-trading-and-conversions-api
- description: Create and manage transactions
  name: BVNK Transaction API
  slug: bvnk-transaction-api
- description: The Transaction Request API from BVNK — 3 operation(s) for transaction request.
  name: BVNK Transaction Request API
  slug: bvnk-transaction-request-api
- description: The Wallets API from BVNK — 4 operation(s) for wallets.
  name: BVNK Wallets API
  slug: bvnk-wallets-api
artifact_total: 24
asyncapis:
- description: ''
  name: Bvnk Webhooks
  slug: bvnk-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bvnk-api-endpoints-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.bvnk.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/bvnk-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bvnk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bvnk.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bvnk.com/bvnk/api-explorer/endpoints/bvnk-api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bvnk.com/bvnk/get-started/get-started-w-bvnk
- group: operate
  title: ''
  type: Support
  url: https://help.bvnk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.bvnk.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bvnk
- group: start
  title: ''
  type: SignUp
  url: https://app.bvnk.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.bvnk.com/hc/en-us/articles/7662073461394-Website-Terms-of-Use-Cookies-Policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.bvnk.com/hc/en-us/articles/7662076884882-Privacy-Policy
- group: build
  title: ''
  type: Postman
  url: https://docs.bvnk.com/postman/bvnk-api-endpoints.postman_collection.json
- group: operate
  title: ''
  type: StatusPage
  url: https://bvnk.status.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bvnk.com/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.bvnk.com/compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bvnk-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/bvnk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bvnk-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bvnk-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bvnk-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bvnk-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bvnk-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bvnk-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bvnk-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bvnk-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bvnk-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bvnk-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bvnk-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bvnk-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bvnk-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bvnk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bvnk-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/bvnk-cli.yml
- group: design
  title: ''
  type: Components
  url: components/bvnk-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bvnk-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bvnk-agentic-access.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bvnk-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bvnk-problem-types.yml
created: '2026-08-08'
description: BVNK is a stablecoin payments infrastructure company that lets businesses move money between fiat and stablecoins over a single API. The platform covers merchant crypto payment collection through payment links and blockchain channels, embedded stablecoin wallets and named virtual accounts (vIBAN) in EUR, GBP and USD, fiat pay-ins and payouts over SWIFT, ACH, Fedwire and local rails, on-ramp and off-ramp conversion, card issuing, treasury and trading, plus customer onboarding, compliance and Travel Rule workflows. Developers integrate over a REST API authenticated with Hawk HMAC-SHA256 request signing, with webhooks for every payment, wallet, card and onboarding lifecycle event, a full sandbox with a payment simulator, and a Postman collection generated from the OpenAPI. BVNK operates as a regulated EMI in the UK (FCA) and Malta (MFSA), is ISO 27001:2022 and SOC 2 Type II certified, and also runs the Layer1 institutional digital-asset platform.
image: https://cdn.prod.website-files.com/66dacc76fb28939d860bf57c/66fc3ae406ca2e2c41d2ccff_og-image.png
layout: provider
mcp_servers:
- description: ''
  name: bvnk-mcp.yml
  slug: bvnk-mcpyml
modified: '2026-08-08'
name: BVNK
nav: Providers
network: true
overview: 'BVNK publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Address API, Asset Pool API, Channels API, and 13 more. Tagged areas include Company, Payments, Stablecoins, Cryptocurrency, and Wallets.


  The BVNK catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  BVNK''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 34 more developer resources.'
random_paper: 85
scopes:
- name: Bvnk Scopes
  scope_count: 156
  slug: bvnk-scopes
  summary_line: 156 scopes · clientCredentials
score:
  band: strong
  composite: 62.9
  delta: 0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.5
    developer_ergonomics: 86.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Bvnk Authentication
  slug: bvnk-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Bvnk Domain Security
  slug: bvnk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bvnk Trust Center
  slug: bvnk-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II
slug: bvnk
tags:
- Company
- Payments
- Stablecoins
- Cryptocurrency
- Wallets
- Virtual Accounts
- Cross-Border Payments
- Financial Services
- Cards
- Digital Assets
- Banking
- Compliance
website: https://www.bvnk.com/
---

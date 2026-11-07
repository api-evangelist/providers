---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.brale.xyz
  baseurl_source: declared
  description: The Accounts API from Brale — 4 operation(s) for accounts.
  name: Brale Accounts API
  slug: brale-accounts-api
- baseURL: https://api.brale.xyz
  baseurl_source: declared
  description: The Addresses API from Brale — 5 operation(s) for addresses.
  name: Brale Addresses API
  slug: brale-addresses-api
- baseURL: https://api.brale.xyz
  baseurl_source: declared
  description: The Automations API from Brale — 2 operation(s) for automations.
  name: Brale Automations API
  slug: brale-automations-api
- baseURL: https://api.brale.xyz
  baseurl_source: declared
  description: The Financial Institutions API from Brale — 10 operation(s) for financial institutions.
  name: Brale Financial Institutions API
  slug: brale-financial-institutions-api
- baseURL: https://api.brale.xyz
  baseurl_source: declared
  description: The Orders API from Brale — 8 operation(s) for orders.
  name: Brale Orders API
  slug: brale-orders-api
- baseURL: https://api.brale.xyz
  baseurl_source: declared
  description: Bank linking and ACH debit via Plaid.
  name: Brale Plaid API
  slug: brale-plaid-api
- baseURL: https://api.brale.xyz
  baseurl_source: declared
  description: Endpoints for creating and retrieving transfers (fiat to stablecoins, etc.)
  name: Brale Transfers API
  slug: brale-transfers-api
artifact_total: 33
asyncapis:
- description: ''
  name: Brale Webhooks
  slug: brale-webhooks
collections:
- collection_type: postman
  name: Brale Accounts API
  slug: postman-brale-accounts-api
- collection_type: postman
  name: Brale Accounts Addresses API
  slug: postman-brale-addresses-api
- collection_type: postman
  name: Brale Accounts Automations API
  slug: postman-brale-automations-api
- collection_type: postman
  name: Brale Accounts Financial Institutions API
  slug: postman-brale-financial-institutions-api
- collection_type: postman
  name: Brale Accounts Orders API
  slug: postman-brale-orders-api
- collection_type: postman
  name: Brale Accounts Webhooks API
  slug: postman-brale-webhooks-api
- collection_type: open
  name: Brale Accounts API
  slug: open-brale-accounts-api
- collection_type: open
  name: Brale Accounts Addresses API
  slug: open-brale-addresses-api
- collection_type: open
  name: Brale Accounts Automations API
  slug: open-brale-automations-api
- collection_type: open
  name: Brale Accounts Financial Institutions API
  slug: open-brale-financial-institutions-api
- collection_type: open
  name: Brale Accounts Orders API
  slug: open-brale-orders-api
- collection_type: open
  name: Brale Accounts Webhooks API
  slug: open-brale-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/brale/plans/brale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brale-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://brale.xyz/feed.xml
- group: company
  title: ''
  type: Website
  url: https://www.brale.xyz/
- group: other
  href: https://artifacts.apis.io/brale/capabilities/brale-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/brale-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/brale/overview
- group: other
  href: https://artifacts.apis.io/brale/a2a/brale-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/brale-a2a.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brale.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.brale.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.brale.xyz/api-reference/brale-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brale.xyz/documentation/introduction
- group: company
  title: ''
  type: Blog
  url: https://brale.xyz/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://brale.xyz/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.brale.xyz
- group: start
  title: ''
  type: Login
  url: https://app.brale.xyz
- group: operate
  title: ''
  type: Support
  url: https://brale.xyz/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brale.xyz/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brale.xyz/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brale-xyz
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/brale-xyz/brale-api/overview
- group: docs
  href: https://artifacts.apis.io/brale/openapi/_original/brale-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/brale-openapi-original.yml
- group: auth
  href: https://artifacts.apis.io/brale/authentication/brale-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brale-authentication.yml
- group: auth
  href: https://artifacts.apis.io/brale/scopes/brale-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/brale-scopes.yml
- group: auth
  href: https://artifacts.apis.io/brale/security/brale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brale-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/brale/well-known/brale-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brale-security.txt
- group: agent
  href: https://artifacts.apis.io/brale/well-known/brale-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brale-well-known.yml
- group: auth
  href: https://artifacts.apis.io/brale/security/brale-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://brale.xyz/security
- group: agent
  href: https://artifacts.apis.io/brale/mcp/brale-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brale-mcp.yml
- group: agent
  href: https://artifacts.apis.io/brale/llms/brale-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brale-llms.txt
- group: build
  href: https://artifacts.apis.io/brale/packages/brale-packages.yml
  title: ''
  type: Packages
  url: packages/brale-packages.yml
- group: build
  href: https://artifacts.apis.io/brale/cli/brale-cli.yml
  title: ''
  type: CLI
  url: cli/brale-cli.yml
- group: other
  href: https://artifacts.apis.io/brale/overlays/brale-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brale-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/brale/conformance/brale-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brale-conformance.yml
- group: design
  href: https://artifacts.apis.io/brale/errors/brale-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brale-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brale/lifecycle/brale-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brale-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brale.xyz
- group: operate
  href: https://artifacts.apis.io/brale/lifecycle/brale-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/brale-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/brale/conventions/brale-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brale-conventions.yml
- group: design
  href: https://artifacts.apis.io/brale/conventions/brale-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/brale-conventions.yml
- group: operate
  href: https://artifacts.apis.io/brale/changelog/brale-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brale-changelog.yml
- group: start
  href: https://artifacts.apis.io/brale/sandbox/brale-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/brale-sandbox.yml
- group: design
  href: https://artifacts.apis.io/brale/data-model/brale-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brale-data-model.yml
- group: design
  href: https://artifacts.apis.io/brale/asyncapi/brale-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/brale-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/brale/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Brale is a regulated stablecoin issuance and orchestration platform. Its Issuance and Orchestration API lets businesses create their own fiat-backed stablecoins and move value across fiat rails and blockchains — onramps, offramps, swaps, custody, and payouts — with mint/burn execution, reserves, custody, settlement, and reporting handled by Brale. Developers authenticate with OAuth2 client-credentials and manage customer accounts (KYB/KYC), on-chain and off-chain addresses, transfers, automations (virtual U.S. account/routing numbers that auto-mint stablecoins on fiat deposit), self-attested tokenization (mints, burns, transfers), and webhooks across Stellar, Solana, Base, Ethereum, Polygon, Avalanche, Celo, Optimism, Arbitrum, and Canton.
finops:
- has_sources: true
  method: derived
  name: Brale Finops
  primary_unit: account
  service_category: ''
  slug: brale-finops
  template: false
image: https://brale.xyz/assets/site/global-og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.brale.xyz over HTTP requiring OAuth; 4 tools listed.
  name: Brale MCP Server
  slug: brale
modified: '2026-10-06'
name: Brale
nav: Providers
network: true
overview: 'Brale publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Addresses API, Automations API, and 4 more. Tagged areas include Company, Stablecoins, Stablecoin Issuance, Payments, and Blockchain.


  The Brale catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Brale''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 37 more developer resources.'
plans:
- name: Brale Plans Pricing
  plan_count: 15
  slug: brale-plans-pricing
- name: Brale Price Estimates
  plan_count: 0
  slug: brale-price-estimates
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Brale API Rules
  rule_count: 66
  severity_counts:
    error: 48
    hint: 0
    info: 5
    warn: 13
  slug: brale-rules
scopes:
- name: Brale Scopes
  scope_count: 20
  slug: brale-scopes
  summary_line: 20 scopes · clientCredentials
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 57.9
    developer_ergonomics: 75.6
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 65.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 36.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/brale/brale-2026-07-25T203713.png
security:
- kind: authentication
  name: Brale Authentication
  slug: brale-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Brale Domain Security
  slug: brale-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Brale Vulnerability Disclosure
  slug: brale-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: Create a deposit automation (auto-mint on fiat deposit)
  slug: brale-create-automation
- name: Onramp fiat to a stablecoin
  slug: brale-onramp-fiat-to-stablecoin
- name: Send a stablecoin payout to an external wallet
  slug: brale-stablecoin-payout
- name: Subscribe to and debug Brale webhooks
  slug: brale-webhook-setup
slug: brale
tags:
- Company
- Stablecoins
- Stablecoin Issuance
- Payments
- Blockchain
- Cryptocurrency
- Fintech
- Financial Services
- Custody
- Tokenization
- On-Ramp
- Off-Ramp
- A2A
website: https://www.brale.xyz/
---

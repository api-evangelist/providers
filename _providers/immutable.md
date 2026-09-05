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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Passport is Immutable's authentication and embedded-wallet product. Its OpenID Connect provider publishes anonymous discovery documents at auth.immutable.com, exposing the authorization, token, device
  name: Immutable Passport Authentication
  slug: immutable-passport-auth
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Activities Endpoints
  name: Immutable Activities API
  slug: immutable-activities-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Chains Endpoints
  name: Immutable Chains API
  slug: immutable-chains-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Collections Endpoints
  name: Immutable Collections API
  slug: immutable-collections-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: The crafting API from Immutable — 1 operation(s) for crafting.
  name: Immutable Crafting API
  slug: immutable-crafting-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Data erasure endpoints
  name: Immutable Data API
  slug: immutable-data-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Audience event ingestion endpoints
  name: Immutable Ingest API
  slug: immutable-ingest-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: NFT Metadata Endpoints
  name: Immutable Metadata API
  slug: immutable-metadata-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: The metadata-search API from Immutable — 3 operation(s) for metadata-search.
  name: Immutable Metadata Search API
  slug: immutable-metadata-search-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: NFT Owner Endpoints
  name: Immutable nft owners API
  slug: immutable-nft-owners-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: NFTs Endpoints
  name: Immutable Nfts API
  slug: immutable-nfts-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: The orders API from Immutable — 14 operation(s) for orders.
  name: Immutable Orders API
  slug: immutable-orders-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Passport operations
  name: Immutable Passport API
  slug: immutable-passport-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Passport Profile endpoints
  name: Immutable passport profile API
  slug: immutable-passport-profile-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Pricing Endpoints
  name: Immutable Pricing API
  slug: immutable-pricing-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: ERC20 Token Endpoints
  name: Immutable Tokens API
  slug: immutable-tokens-api
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: Tracking consent management endpoints
  name: Immutable Tracking Consent API
  slug: immutable-tracking-consent-api
artifact_total: 26
asyncapis:
- description: ''
  name: Immutable Webhooks
  slug: immutable-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/immutable-zkevm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/immutable-audience-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.immutable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.immutable.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.immutable.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.immutable.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.immutable.com/docs/guides/build-a-game
- group: operate
  title: ''
  type: Support
  url: https://support.immutable.com
- group: company
  title: ''
  type: Blog
  url: https://www.immutable.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/immutable
- group: start
  title: ''
  type: SignUp
  url: https://hub.immutable.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.immutable.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.immutable.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.immutable.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.immutable.com/docs/products/immutable-chain/immutable-x-deprecation
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/immutable-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/immutable-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/immutable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/immutable-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/immutable-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/immutable-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/immutable-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/immutable-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/immutable-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/immutable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/immutable-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/immutable-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/immutable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/immutable-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/immutable-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/immutable-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/immutable-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/immutable-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/immutable-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/immutable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/immutable-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/immutable-components.yml
- group: auth
  title: ''
  type: Security
  url: security/immutable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/immutable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/immutable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/immutable-domain-security.yml
created: '2026-08-23'
description: 'Immutable is a games growth and blockchain infrastructure company whose platform spans two connected halves: Immutable Audience, a games-focused CDP, attribution and player-activation stack (ingestion, analytics, engage, conversion funnel, ad-network postbacks), and Immutable Chain, a gaming-optimised Ethereum zkEVM with Passport embedded wallets, pre-built ERC-721/ERC-1155/ERC-20 asset contracts, a gasless Minting API, a Seaport-based decentralised Orderbook, an NFT Indexer and Checkout flows. Developers work against a public REST surface on api.immutable.com described by two published OpenAPI 3.0.3 documents, configure projects and API keys in Immutable Hub, and integrate through first-party TypeScript, Unity and Unreal SDKs.'
image: https://www.immutable.com/images/og-image.jpg
layout: provider
mcp_servers:
- description: Immutable serves a remote, anonymous Model Context Protocol endpoint from its own documentation host. A JSON-RPC tools/list POST returns HTTP 200 with a text/event-stream body carrying three real tool
  name: Immutable Documentation MCP Server
  slug: immutable-documentation-mcp-server
modified: '2026-08-23'
name: Immutable
nav: Providers
network: true
overview: 'Immutable publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Chains API, Collections API, and 13 more. Tagged areas include Company, Gaming, Blockchain, NFT, and Web3.


  The Immutable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Immutable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 35 more developer resources.'
plans:
- name: Immutable Plans Pricing
  plan_count: 3
  slug: immutable-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Immutable Rate Limits
  slug: immutable-rate-limits
scopes:
- name: Immutable Scopes
  scope_count: 0
  slug: immutable-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 62.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 69.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/immutable/refs/heads/main/screenshots/immutable-2026-09-02T145838.png
security:
- kind: authentication
  name: Immutable Authentication
  slug: immutable-authentication
  summary_line: apiKey/http/openIdConnect · 4 schemes
- kind: domain-security
  name: Immutable Domain Security
  slug: immutable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Immutable Vulnerability Disclosure
  slug: immutable-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Immutable Trust Center
  slug: immutable-trust-center
  summary_line: named, note
slug: immutable
tags:
- Company
- Gaming
- Blockchain
- NFT
- Web3
- Wallets
- Marketplace
- Analytics
- Attribution
- Customer Data Platform
- Authentication
- Developer Platform
website: https://www.immutable.com
---

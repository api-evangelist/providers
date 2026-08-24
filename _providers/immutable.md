---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 63.9
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: The Immutable Multi Rollup API — the public REST surface for Immutable Chain. Covers activities, chains, collections, NFTs and NFT owners, ERC-20 tokens, metadata and metadata search, the Seaport-back
  name: Immutable zkEVM API
  slug: immutable-zkevm-api
- description: The Audience event tracking and identity resolution service. Ingests batched identify/track/page/screen messages from game servers and backends, reads and updates per-identity tracking consent, and ac
  name: Immutable Audience API
  slug: immutable-audience-api
- description: Passport is Immutable's authentication and embedded-wallet product. Its OpenID Connect provider publishes anonymous discovery documents at auth.immutable.com, exposing the authorization, token, device
  name: Immutable Passport Authentication
  slug: immutable-passport-auth
artifact_total: 12
asyncapis:
- description: ''
  name: Immutable Webhooks
  slug: immutable-webhooks
common:
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
overview: 'Immutable publishes 2 APIs on the [APIs.io](https://apis.io/) network: zkEVM API and Audience API. Tagged areas include Company, Gaming, Blockchain, NFT, and Web3.


  The Immutable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Immutable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 33 more developer resources.'
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
  composite: 72.7
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 30.3
    contract_quality: 61.7
    developer_ergonomics: 64.3
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 92.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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

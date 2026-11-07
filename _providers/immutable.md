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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Immutable Agentic Access
  operation_count: 63
  slug: immutable-agentic-access
  summary_line: 63 operations · 19 acting
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
- baseURL: https://api.immutable.com
  baseurl_source: declared
  description: NFTs Endpoints
  name: Immutable Nfts API
  slug: immutable-nfts-api
artifact_total: 83
asyncapis:
- description: ''
  name: Immutable Webhooks
  slug: immutable-webhooks
common:
- group: other
  href: https://artifacts.apis.io/immutable/capabilities/immutable-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/immutable-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/immutable/agentic-access/immutable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/immutable-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/immutable/rules/immutable-rules.yml
  title: ''
  type: Spectral
  url: rules/immutable-rules.yml
- group: design
  href: https://artifacts.apis.io/immutable/json-ld/immutable-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/immutable-context.jsonld
- group: design
  href: https://artifacts.apis.io/immutable/vocabulary/immutable-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/immutable-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/immutable/overlays/immutable-activities-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/immutable-activities-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/immutable/llms/immutable-www-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/immutable-www-llms.txt
- group: other
  href: https://artifacts.apis.io/immutable/hosts/immutable-hosts.yml
  title: ''
  type: Hosts
  url: hosts/immutable-hosts.yml
- group: build
  href: https://artifacts.apis.io/immutable/integrations/immutable-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/immutable-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/immutable/vendors/immutable-vendors.yml
  title: ''
  type: Vendors
  url: vendors/immutable-vendors.yml
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
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/immutable
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
  href: https://artifacts.apis.io/immutable/lifecycle/immutable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/immutable-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/immutable/changelog/immutable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/immutable-changelog.yml
- group: build
  href: https://artifacts.apis.io/immutable/packages/immutable-packages.yml
  title: ''
  type: Packages
  url: packages/immutable-packages.yml
- group: build
  href: https://artifacts.apis.io/immutable/packages/immutable-packages.yml
  title: ''
  type: SDKs
  url: packages/immutable-packages.yml
- group: agent
  href: https://artifacts.apis.io/immutable/mcp/immutable-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/immutable-mcp.yml
- group: build
  href: https://artifacts.apis.io/immutable/mcp/immutable-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/immutable-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/immutable/a2a/immutable-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/immutable-a2a.yml
- group: agent
  href: https://artifacts.apis.io/immutable/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/immutable/llms/immutable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/immutable-llms.txt
- group: agent
  href: https://artifacts.apis.io/immutable/well-known/immutable-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/immutable-well-known.yml
- group: auth
  href: https://artifacts.apis.io/immutable/authentication/immutable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/immutable-authentication.yml
- group: auth
  href: https://artifacts.apis.io/immutable/scopes/immutable-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/immutable-scopes.yml
- group: design
  href: https://artifacts.apis.io/immutable/conventions/immutable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/immutable-conventions.yml
- group: design
  href: https://artifacts.apis.io/immutable/conventions/immutable-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/immutable-conventions.yml
- group: design
  href: https://artifacts.apis.io/immutable/errors/immutable-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/immutable-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/immutable/rate-limits/immutable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/immutable-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/immutable/plans/immutable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/immutable-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/immutable/asyncapi/immutable-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/immutable-webhooks.yml
- group: start
  href: https://artifacts.apis.io/immutable/sandbox/immutable-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/immutable-sandbox.yml
- group: design
  href: https://artifacts.apis.io/immutable/data-model/immutable-data-model.yml
  title: ''
  type: DataModel
  url: data-model/immutable-data-model.yml
- group: design
  href: https://artifacts.apis.io/immutable/conformance/immutable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/immutable-conformance.yml
- group: auth
  href: https://artifacts.apis.io/immutable/conformance/immutable-conformance.yml
  title: ''
  type: Compliance
  url: conformance/immutable-conformance.yml
- group: design
  href: https://artifacts.apis.io/immutable/components/immutable-components.yml
  title: ''
  type: Components
  url: components/immutable-components.yml
- group: auth
  href: https://artifacts.apis.io/immutable/security/immutable-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/immutable-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/immutable/security/immutable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/immutable-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/immutable/security/immutable-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/immutable-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/immutable/security/immutable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/immutable-domain-security.yml
created: '2026-08-23'
description: 'Immutable is a games growth and blockchain infrastructure company whose platform spans two connected halves: Immutable Audience, a games-focused CDP, attribution and player-activation stack (ingestion, analytics, engage, conversion funnel, ad-network postbacks), and Immutable Chain, a gaming-optimised Ethereum zkEVM with Passport embedded wallets, pre-built ERC-721/ERC-1155/ERC-20 asset contracts, a gasless Minting API, a Seaport-based decentralised Orderbook, an NFT Indexer and Checkout flows. Developers work against a public REST surface on api.immutable.com described by two published OpenAPI 3.0.3 documents, configure projects and API keys in Immutable Hub, and integrate through first-party TypeScript, Unity and Unreal SDKs.'
finops:
- has_sources: true
  method: derived
  name: Immutable Finops
  primary_unit: cent of trade
  service_category: ''
  slug: immutable-finops
  template: false
image: https://www.immutable.com/images/og-image.jpg
json_schemas:
- name: CreateBidRequestBody
  property_count: 10
  slug: immutable-create-bid-request-body
- name: CreateCollectionBidRequestBody
  property_count: 10
  slug: immutable-create-collection-bid-request-body
- name: CreateListingRequestBody
  property_count: 10
  slug: immutable-create-listing-request-body
- name: CreateMetadataBidRequestBody
  property_count: 12
  slug: immutable-create-metadata-bid-request-body
- name: CreateMintRequestRequest
  property_count: 1
  slug: immutable-create-mint-request-request
- name: CreateMintRequestResult
  property_count: 4
  slug: immutable-create-mint-request-result
- name: CreateTraitBidRequestBody
  property_count: 11
  slug: immutable-create-trait-bid-request-body
- name: GetActivityResult
  property_count: 1
  slug: immutable-get-activity-result
- name: GetCollectionResult
  property_count: 1
  slug: immutable-get-collection-result
- name: GetLinkedAddressesRes
  property_count: 1
  slug: immutable-get-linked-addresses-res
- name: GetMetadataResult
  property_count: 1
  slug: immutable-get-metadata-result
- name: GetNFTResult
  property_count: 1
  slug: immutable-get-nftresult
- name: GetTokenResult
  property_count: 1
  slug: immutable-get-token-result
- name: LinkWalletV2Request
  property_count: 4
  slug: immutable-link-wallet-v2-request
- name: ListActivitiesResult
  property_count: 2
  slug: immutable-list-activities-result
- name: ListChainsResult
  property_count: 2
  slug: immutable-list-chains-result
- name: ListCollectionBidsResult
  property_count: 2
  slug: immutable-list-collection-bids-result
- name: ListCollectionOwnersResult
  property_count: 2
  slug: immutable-list-collection-owners-result
- name: ListCollectionsResult
  property_count: 2
  slug: immutable-list-collections-result
- name: ListFiltersResult
  property_count: 2
  slug: immutable-list-filters-result
- name: ListMetadataResult
  property_count: 2
  slug: immutable-list-metadata-result
- name: ListMintRequestsResult
  property_count: 2
  slug: immutable-list-mint-requests-result
- name: ListNFTOwnersResult
  property_count: 2
  slug: immutable-list-nftowners-result
- name: ListNFTsByOwnerResult
  property_count: 2
  slug: immutable-list-nfts-by-owner-result
- name: ListNFTsResult
  property_count: 2
  slug: immutable-list-nfts-result
- name: ListTokensResult
  property_count: 2
  slug: immutable-list-tokens-result
- name: MessagesRequest
  property_count: 1
  slug: immutable-messages-request
- name: MessagesResponse
  property_count: 4
  slug: immutable-messages-response
- name: MetadataRefreshRateLimitResult
  property_count: 4
  slug: immutable-metadata-refresh-rate-limit-result
- name: PhoneNumberOTPRequest
  property_count: 2
  slug: immutable-phone-number-otprequest
- name: PhoneNumberOTPVerificationRequest
  property_count: 2
  slug: immutable-phone-number-otpverification-request
- name: QuotesForNFTsResult
  property_count: 2
  slug: immutable-quotes-for-nfts-result
- name: QuotesForStacksResult
  property_count: 2
  slug: immutable-quotes-for-stacks-result
- name: RefreshCollectionMetadataRequest
  property_count: 1
  slug: immutable-refresh-collection-metadata-request
- name: RefreshCollectionMetadataResult
  property_count: 3
  slug: immutable-refresh-collection-metadata-result
- name: RefreshMetadataByIDRequest
  property_count: 1
  slug: immutable-refresh-metadata-by-idrequest
- name: RefreshNFTMetadataByTokenIDRequest
  property_count: 1
  slug: immutable-refresh-nftmetadata-by-token-idrequest
- name: SearchNFTsResult
  property_count: 2
  slug: immutable-search-nfts-result
- name: SearchStacksResult
  property_count: 2
  slug: immutable-search-stacks-result
- name: SignCraftingRequest
  property_count: 4
  slug: immutable-sign-crafting-request
- name: SignCraftingResult
  property_count: 2
  slug: immutable-sign-crafting-result
- name: StackBundle
  property_count: 5
  slug: immutable-stack-bundle
- name: TrackingConsentResponse
  property_count: 1
  slug: immutable-tracking-consent-response
- name: UpdateTrackingConsentRequest
  property_count: 3
  slug: immutable-update-tracking-consent-request
- name: UserInfo
  property_count: 4
  slug: immutable-user-info
- name: UsernameUpdateRequest
  property_count: 1
  slug: immutable-username-update-request
- name: Wallet
  property_count: 6
  slug: immutable-wallet
jsonld:
- class_count: 120
  name: Immutable Context
  property_count: 172
  slug: immutable-context
layout: provider
mcp_servers:
- description: Immutable serves a remote, anonymous Model Context Protocol endpoint from its own documentation host. A JSON-RPC tools/list POST returns HTTP 200 with a text/event-stream body carrying three real tool
  name: Immutable Documentation MCP Server
  slug: immutable-documentation-mcp-server
modified: '2026-10-21'
name: Immutable
nav: Providers
network: true
overview: 'Immutable publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Chains API, Collections API, and 14 more. Tagged areas include Company, Gaming, Blockchain, NFT, and Web3.


  The Immutable catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Immutable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 44 more developer resources.'
plans:
- name: Immutable Plans Pricing
  plan_count: 1
  slug: immutable-plans-pricing
- name: Immutable Price Estimates
  plan_count: 0
  slug: immutable-price-estimates
random_paper: 0
rate_limits:
- limit_count: 8
  name: Immutable Rate Limits
  slug: immutable-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Immutable API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 1
  slug: immutable-rules
scopes:
- name: Immutable Scopes
  scope_count: 14
  slug: immutable-scopes
  summary_line: 14 scopes
score:
  band: exemplar
  composite: 71.1
  coverage:
    artifact_dirs: 38
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 73.3
    developer_ergonomics: 66.7
    discoverability: 75.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 41.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/immutable/immutable-2026-09-02T145838.png
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
  summary_line: trust center published
skill_count: 5
skills:
- name: immutable-audience-events
  slug: immutable-audience-events
- name: immutable
  slug: immutable-immutable-skill
- name: immutable-mint-nfts
  slug: immutable-mint-nfts
- name: immutable-query-assets
  slug: immutable-query-assets
- name: immutable-trade-nfts
  slug: immutable-trade-nfts
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
- A2A
website: https://www.immutable.com
---

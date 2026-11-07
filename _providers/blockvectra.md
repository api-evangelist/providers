---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 3
  name: Blockvectra Agentic Access
  operation_count: 66
  slug: blockvectra-agentic-access
  summary_line: 66 operations · 24 acting · 3 human-in-the-loop
api_count: 5
apis:
- description: Provides blockchain data via REST endpoints as described in the documentation.
  name: BlockVectra Data API
  slug: blockvectra-data-api
- baseURL: https://api.blockvectra.com/v1
  baseurl_source: declared
  description: Read-only lookup of the caller's own API key's balance and limits by x-api-key; never billed (Section 1).
  name: BlockVectra Account API
  slug: blockvectra-account-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: Address-scoped transactions, transfers, and balances.
  name: BlockVectra Addresses API
  slug: blockvectra-addresses-api
- baseURL: https://console-api.blockvectra.com/v1
  baseurl_source: declared
  description: Login, sign-up, and sessions
  name: BlockVectra Auth API
  slug: blockvectra-auth-api
- baseURL: https://console-api.blockvectra.com/v1
  baseurl_source: declared
  description: Balances, charges, top-ups, and usage
  name: BlockVectra Billing API
  slug: blockvectra-billing-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: Blocks and transactions.
  name: BlockVectra Chain API
  slug: blockvectra-chain-api
- baseURL: https://api.blockvectra.com/v1
  baseurl_source: declared
  description: Public list of served chains and their static parameters (Section 12).
  name: BlockVectra Chains API
  slug: blockvectra-chains-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: DEX swaps and daily prices.
  name: BlockVectra DEX API
  slug: blockvectra-dex-api
- baseURL: https://api.blockvectra.com/v1
  baseurl_source: declared
  description: Claim test ETH on the Robinhood testnet; claims are free.
  name: BlockVectra Faucet API
  slug: blockvectra-faucet-api
- baseURL: https://api.blockvectra.com/v1
  baseurl_source: declared
  description: Ethereum-style JSON-RPC 2.0 calls to a chain node (Section 1).
  name: BlockVectra JSON RPC API
  slug: blockvectra-json-rpc-api
- baseURL: https://console-api.blockvectra.com/v1
  baseurl_source: declared
  description: API key creation, query, renaming, rotation, and revocation
  name: BlockVectra Keys API
  slug: blockvectra-keys-api
- baseURL: https://console-api.blockvectra.com/v1
  baseurl_source: declared
  description: Current user, username, and identity linking
  name: BlockVectra Me API
  slug: blockvectra-me-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: ERC-721/ERC-1155 ownership.
  name: BlockVectra NFTs API
  slug: blockvectra-nfts-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: Data freshness for each public dataset.
  name: BlockVectra Status API
  slug: blockvectra-status-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: Tokenized-stock daily activity.
  name: BlockVectra Stocks API
  slug: blockvectra-stocks-api
- baseURL: https://api.blockvectra.com/v1
  baseurl_source: declared
  description: Subscriptions, their addresses and actions.
  name: BlockVectra Subscriptions API
  slug: blockvectra-subscriptions-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: ERC-20/ERC-721/ERC-1155 transfers, holders, and metadata.
  name: BlockVectra Tokens API
  slug: blockvectra-tokens-api
- baseURL: https://api.blockvectra.com/v1/data
  baseurl_source: declared
  description: Historical callTracer call trees.
  name: BlockVectra Traces API
  slug: blockvectra-traces-api
- description: Provides blockchain data via REST endpoints as described in the documentation.
  name: BlockVectra Data API
  slug: blockvectra-data-api
- baseURL: https://api.blockvectra.com
  baseurl_source: declared
  description: The Top Up API from BlockVectra — 3 operation(s) for top up.
  name: BlockVectra Top Up API
  slug: blockvectra-top-up-api
artifact_total: 54
asyncapis:
- description: ''
  name: Blockvectra Webhooks
  slug: blockvectra-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/blockvectra/plans/blockvectra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blockvectra-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/blockvectra/agentic-access/blockvectra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blockvectra-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/blockvectra/rate-limits/blockvectra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blockvectra-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/blockvectra/rules/blockvectra-rules.yml
  title: ''
  type: Spectral
  url: rules/blockvectra-rules.yml
- group: design
  href: https://artifacts.apis.io/blockvectra/json-ld/blockvectra-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blockvectra-context.jsonld
- group: design
  href: https://artifacts.apis.io/blockvectra/vocabulary/blockvectra-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blockvectra-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blockvectra/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blockvectra/asyncapi/blockvectra-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/blockvectra-webhooks.yml
- group: design
  href: https://artifacts.apis.io/blockvectra/data-model/blockvectra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blockvectra-data-model.yml
- group: auth
  href: https://artifacts.apis.io/blockvectra/security/blockvectra-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blockvectra-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blockvectra/authentication/blockvectra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blockvectra-authentication.yml
- group: design
  href: https://artifacts.apis.io/blockvectra/lifecycle/blockvectra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blockvectra-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/blockvectra/errors/blockvectra-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blockvectra-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blockvectra/conformance/blockvectra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockvectra-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blockvectra/llms/blockvectra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockvectra-llms.txt
- group: build
  href: https://artifacts.apis.io/blockvectra/mcp/blockvectra-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/blockvectra-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/blockvectra/mcp/blockvectra-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blockvectra-mcp.yml
- group: auth
  href: https://artifacts.apis.io/blockvectra/well-known/blockvectra-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blockvectra-security.txt
- group: auth
  href: https://artifacts.apis.io/blockvectra/well-known/blockvectra-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blockvectra-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/blockvectra/well-known/blockvectra-console-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blockvectra-console-security.txt
- group: agent
  href: https://artifacts.apis.io/blockvectra/well-known/blockvectra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockvectra-well-known.yml
- group: other
  href: https://artifacts.apis.io/blockvectra/hosts/blockvectra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockvectra-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockvectra/vendors/blockvectra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockvectra-vendors.yml
- group: build
  href: https://artifacts.apis.io/blockvectra/packages/blockvectra-packages.yml
  title: ''
  type: SDKs
  url: packages/blockvectra-packages.yml
- group: build
  href: https://artifacts.apis.io/blockvectra/packages/blockvectra-packages.yml
  title: ''
  type: Packages
  url: packages/blockvectra-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://blockvectra.com/zh/webhooks/
- group: start
  title: ''
  type: Sandbox
  url: https://console.blockvectra.com/playground/
- group: start
  title: ''
  type: Login
  url: https://console.blockvectra.com/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blockvectra.com/en/quickstart/
- group: auth
  href: https://artifacts.apis.io/blockvectra/security/blockvectra-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blockvectra-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blockvectra/security/blockvectra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockvectra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blockvectra.com
- group: other
  title: ''
  type: Image
  url: https://blockvectra.com/favicon.ico
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockvectra.com/en/api/data/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blockvectra.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blockvectra.com/en/api/data/
- group: commercial
  title: ''
  type: Pricing
  url: https://blockvectra.com/en/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blockvectra.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blockvectra.com/en/privacy/
- group: operate
  title: ''
  type: Support
  url: https://blockvectra.com/en/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blockvectra
created: '2026-11-02'
description: BlockVectra provides multi‑chain RPC and blockchain data APIs, offering a single API key for JSON‑RPC on every supported chain and a Data API for indexed blocks, transactions, addresses, tokens, NFTs and DEX activity. The platform delivers real‑time and historical blockchain data with flexible metering via Compute Units, a free tier of 30 million CU, and pay‑as‑you‑go pricing. It serves developers building crypto applications, analytics, and DeFi services.
json_schemas:
- name: AddResult
  property_count: 4
  slug: blockvectra-add-result
- name: AddressTransferListEnvelope
  property_count: 3
  slug: blockvectra-address-transfer-list-envelope
- name: BalanceResponse
  property_count: 7
  slug: blockvectra-balance-response
- name: DexSwapListEnvelope
  property_count: 3
  slug: blockvectra-dex-swap-list-envelope
- name: EventHistoryPage
  property_count: 2
  slug: blockvectra-event-history-page
- name: FaucetClaimAccepted
  property_count: 6
  slug: blockvectra-faucet-claim-accepted
- name: FaucetClaimRequest
  property_count: 1
  slug: blockvectra-faucet-claim-request
- name: FreshnessEnvelope
  property_count: 2
  slug: blockvectra-freshness-envelope
- name: IdentityView
  property_count: 6
  slug: blockvectra-identity-view
- name: JsonRpcResponseBody
  property_count: 0
  slug: blockvectra-json-rpc-response-body
- name: KeyView
  property_count: 12
  slug: blockvectra-key-view
- name: PlansResponse
  property_count: 6
  slug: blockvectra-plans-response
- name: RemoveResult
  property_count: 4
  slug: blockvectra-remove-result
- name: ResetsResponse
  property_count: 4
  slug: blockvectra-resets-response
- name: SessionResponse
  property_count: 2
  slug: blockvectra-session-response
- name: SubscriptionCreate
  property_count: 3
  slug: blockvectra-subscription-create
- name: SubscriptionList
  property_count: 2
  slug: blockvectra-subscription-list
- name: SubscriptionPatch
  property_count: 4
  slug: blockvectra-subscription-patch
- name: TokenTransferListEnvelope
  property_count: 3
  slug: blockvectra-token-transfer-list-envelope
- name: TokensBatchEnvelope
  property_count: 2
  slug: blockvectra-tokens-batch-envelope
- name: TransactionListEnvelope
  property_count: 3
  slug: blockvectra-transaction-list-envelope
jsonld:
- class_count: 120
  name: Blockvectra Context
  property_count: 305
  slug: blockvectra-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.blockvectra.com.
  name: BlockVectra MCP Server
  slug: blockvectra-mcp-yml
modified: '2026-11-02'
name: BlockVectra
nav: Providers
network: true
overview: 'BlockVectra publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Addresses API, Auth API, and 17 more. Tagged areas include Blockchain, Data API, Multi-Chain, Cryptocurrency, and Developer Platform.


  The BlockVectra catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BlockVectra''s developer surface includes authentication, sandbox, getting-started guide, documentation, API reference, pricing, support, and 34 more developer resources.'
plans:
- name: Blockvectra Plans Pricing
  plan_count: 1
  slug: blockvectra-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 6
  name: Blockvectra Rate Limits
  slug: blockvectra-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: BlockVectra API Rules
  rule_count: 63
  severity_counts:
    error: 46
    hint: 0
    info: 5
    warn: 12
  slug: blockvectra-rules
scopes:
- name: Blockvectra Scopes
  scope_count: 0
  slug: blockvectra-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 83.8
    catalog_earned_first_party: 20.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 72.8
    developer_ergonomics: 50.5
    discoverability: 66.7
    operational_transparency: 48.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blockvectra Authentication
  slug: blockvectra-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blockvectra Domain Security
  slug: blockvectra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blockvectra Vulnerability Disclosure
  slug: blockvectra-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: get-status-skill
  slug: blockvectra-get-status-skill
- name: list-chains-skill
  slug: blockvectra-list-chains-skill
slug: blockvectra
tags:
- Blockchain
- Data API
- Multi-Chain
- Cryptocurrency
- Developer Platform
website: https://blockvectra.com
---

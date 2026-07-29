---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 3
  name: Euler Agentic Access
  operation_count: 91
  slug: euler-agentic-access
  summary_line: 91 operations · 19 acting · 3 human-in-the-loop
api_count: 24
apis:
- description: An unofficial REST endpoint for fetching USD-denominated asset prices for ERC-20 tokens across supported networks. Accepts chainId and comma-separated asset addresses. Returns prices with 18-decimal p
  name: Euler Off-Chain Prices API
  slug: euler-off-chain-prices-api
- description: GraphQL-based subgraph endpoints hosted on Goldsky for querying indexed Euler V2 protocol data including vault states, account positions, borrow/supply history, interest rates, collateral relationship
  name: Euler Subgraphs (GraphQL)
  slug: euler-subgraphs-graphql
- description: The recommended TypeScript entry point for applications, bots, scripts, and operational tooling built on Euler V2. Provides protocol data fetching, EVC batch composition, transaction simulation, appro
  name: Euler V2 TypeScript SDK
  slug: euler-v2-typescript-sdk
- description: Account activity, discovered positions, and sub-account relationships. Legacy nested account payloads are flattened into account-vault rows in v3.
  name: Euler Finance Accounts API
  slug: euler-accounts-api
- description: Base and intrinsic APY surfaces. In v3, APY families are split into dedicated endpoints instead of being embedded inconsistently across larger payloads.
  name: Euler Finance APYs API
  slug: euler-apys-api
- description: Authentication and authorization conventions used across the API, including API keys, admin secrets, and rate-limit behavior.
  name: Euler Finance Auth API
  slug: euler-auth-api
- description: Chain inventory and per-chain protocol summaries. These replace ad-hoc chain-level aggregates from legacy APIs with explicit, cacheable resources.
  name: Euler Finance Chains API
  slug: euler-chains-api
- description: Curator-managed metadata such as labels, descriptions, and visibility controls. This is the operator-owned customization surface in v3.
  name: Euler Finance Curator API
  slug: euler-curator-api
- description: Euler Earn vault resources and historical data. These endpoints are separate from EVK vaults and should be modeled independently in client code.
  name: Euler Finance Earn API
  slug: euler-earn-api
- description: Platform-admin managed KYBed organization profiles used as backend-owned label and control-plane resources.
  name: Euler Finance Entities API
  slug: euler-entities-api
- description: Ethereum Vault Connector account event resources. These are separate from account position snapshots and are intended for event-level inspection.
  name: Euler Finance EVC API
  slug: euler-evc-api
- description: Fee-flow event resources and fee-related historical activity.
  name: Euler Finance FeeFlow API
  slug: euler-feeflow-api
- description: Controlled GraphQL passthrough endpoints for indexer-backed data exploration and compatibility workflows.
  name: Euler Finance GraphQL API
  slug: euler-graphql-api
- description: Liveness, readiness, and dashboard-friendly platform status checks. Use these for operational monitoring, not for reconstructing full portfolio state.
  name: Euler Finance Health API
  slug: euler-health-api
- description: Liquidation events and related historical views used for risk analysis and monitoring.
  name: Euler Finance Liquidations API
  slug: euler-liquidations-api
- description: Oracle routing, adapter, and price-source inspection endpoints. These expose pricing/oracle internals that were previously harder to inspect externally.
  name: Euler Finance Oracles API
  slug: euler-oracles-api
- description: Current and historical token prices. Prices follow v3 source priority rules and return the canonical merged value rather than exposing raw provider-specific reads by default.
  name: Euler Finance Prices API
  slug: euler-prices-api
- description: 'Protocol-wide summary endpoints and aggregate metrics. In v3, these endpoints are explicitly summary-oriented and should be treated as lightweight rollups rather than replacements for full vault list '
  name: Euler Finance Protocol API
  slug: euler-protocol-api
- description: Public allocator event resources for allocator-level activity and history.
  name: Euler Finance PublicAllocator API
  slug: euler-publicallocator-api
- description: Reward campaign APRs and per-account reward breakdowns. Rewards APY is intentionally separate from base vault APY in v3; combine them client-side when you need a legacy-style total supply APY.
  name: Euler Finance Rewards API
  slug: euler-rewards-api
- description: Terms-of-use signature state and audit endpoints.
  name: Euler Finance TermsOfUse API
  slug: euler-termsofuse-api
- description: Token metadata, protocol classifications, and related static reference data used throughout the API.
  name: Euler Finance Tokens API
  slug: euler-tokens-api
- description: API usage and API key analytics. These endpoints are intended for operators and consumers tracking traffic, rate limits, and key-level activity.
  name: Euler Finance Usage API
  slug: euler-usage-api
- description: Canonical vault resources, vault history, holders, borrowers, and open-interest views. In v3, vault detail is decomposed into focused endpoints instead of one large legacy response.
  name: Euler Finance Vaults API
  slug: euler-vaults-api
artifact_total: 233
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/euler-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/euler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/euler-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/euler-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.euler.finance/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.euler.finance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.euler.finance/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.euler.finance
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/euler-xyz/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/CdG97VSYGk
- group: other
  title: ''
  type: X
  url: https://x.com/eulerfinance
- group: company
  title: ''
  type: Blog
  url: https://www.euler.finance/blog
- group: other
  title: ''
  type: Governance
  url: https://gov.euler.finance
- group: auth
  title: ''
  type: BugBounty
  url: https://docs.euler.finance/security/bug-bounty
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.euler.finance/llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.euler.finance/llms-full.txt
created: '2026-06-14'
description: Euler is a permissionless modular lending protocol that enables users to lend, borrow, and build custom lending markets without limits. The platform provides REST APIs for querying vaults, account positions, interest rates, liquidation thresholds, token prices, APYs, reward campaigns, and lending market analytics across multiple EVM-compatible networks.
examples:
- key_count: 8
  name: Completeplatformauthcallback
  slug: completeplatformauthcallback
- key_count: 7
  name: Createentity
  slug: createentity
- key_count: 8
  name: Createentityaddress
  slug: createentityaddress
- key_count: 8
  name: Createentitymember
  slug: createentitymember
- key_count: 7
  name: Createplatformadminaccess
  slug: createplatformadminaccess
- key_count: 8
  name: Deleteadminapikeysbyid
  slug: deleteadminapikeysbyid
- key_count: 8
  name: Deleteentity
  slug: deleteentity
- key_count: 8
  name: Deleteentityaddress
  slug: deleteentityaddress
- key_count: 8
  name: Getaccountsbyaddressactivity
  slug: getaccountsbyaddressactivity
- key_count: 8
  name: Getaccountsbyaddressportfolio
  slug: getaccountsbyaddressportfolio
- key_count: 8
  name: Getaccountsbyaddresspositions
  slug: getaccountsbyaddresspositions
- key_count: 8
  name: Getaccountsbyaddresssubaccounts
  slug: getaccountsbyaddresssubaccounts
- key_count: 7
  name: Getadminapikeys
  slug: getadminapikeys
- key_count: 8
  name: Getadminapikeysbyid
  slug: getadminapikeysbyid
- key_count: 8
  name: Getadminapikeysbyidusage
  slug: getadminapikeysbyidusage
- key_count: 8
  name: Getapysintrinsic
  slug: getapysintrinsic
- key_count: 8
  name: Getapysintrinsichistory
  slug: getapysintrinsichistory
- key_count: 8
  name: Getapysrewards
  slug: getapysrewards
- key_count: 8
  name: Getapysrewardshistory
  slug: getapysrewardshistory
- key_count: 7
  name: Getchains
  slug: getchains
- key_count: 8
  name: Getchainsbychainidborrowablevaults
  slug: getchainsbychainidborrowablevaults
- key_count: 8
  name: Getchainsbychainidstats
  slug: getchainsbychainidstats
- key_count: 8
  name: Getcuratorvaults
  slug: getcuratorvaults
- key_count: 7
  name: Getdocs
  slug: getdocs
- key_count: 8
  name: Getearnvaults
  slug: getearnvaults
- key_count: 8
  name: Getearnvaultsbychainidbyaddress
  slug: getearnvaultsbychainidbyaddress
- key_count: 8
  name: Getearnvaultsbychainidbyaddressevents
  slug: getearnvaultsbychainidbyaddressevents
- key_count: 8
  name: Getentity
  slug: getentity
- key_count: 8
  name: Getevcaccountsbyaddressevents
  slug: getevcaccountsbyaddressevents
- key_count: 8
  name: Getfeeflowevents
  slug: getfeeflowevents
- key_count: 8
  name: Getgraphql
  slug: getgraphql
- key_count: 7
  name: Gethealth
  slug: gethealth
- key_count: 7
  name: Gethealthdetailed
  slug: gethealthdetailed
- key_count: 7
  name: Gethealthlive
  slug: gethealthlive
- key_count: 7
  name: Gethealthready
  slug: gethealthready
- key_count: 8
  name: Getliquidations
  slug: getliquidations
- key_count: 7
  name: Getmetrics
  slug: getmetrics
- key_count: 7
  name: Getopenapijson
  slug: getopenapijson
- key_count: 8
  name: Getoracleshistoricaladapters
  slug: getoracleshistoricaladapters
- key_count: 8
  name: Getoraclesprices
  slug: getoraclesprices
- key_count: 8
  name: Getoraclesrouters
  slug: getoraclesrouters
- key_count: 7
  name: Getplatformauthsession
  slug: getplatformauthsession
- key_count: 8
  name: Getprices
  slug: getprices
- key_count: 8
  name: Getpriceshistory
  slug: getpriceshistory
- key_count: 8
  name: Getprotocolstats
  slug: getprotocolstats
- key_count: 8
  name: Getpublicallocatorevents
  slug: getpublicallocatorevents
- key_count: 8
  name: Getrewardsbreakdown
  slug: getrewardsbreakdown
- key_count: 7
  name: Getroot
  slug: getroot
- key_count: 8
  name: Gettermsofusecheckbyaddress
  slug: gettermsofusecheckbyaddress
- key_count: 8
  name: Gettermsofusesignatures
  slug: gettermsofusesignatures
- key_count: 8
  name: Gettokens
  slug: gettokens
- key_count: 8
  name: Gettokensbychainidbyaddressprice
  slug: gettokensbychainidbyaddressprice
- key_count: 7
  name: Gettoolboxadminapikeys
  slug: gettoolboxadminapikeys
- key_count: 7
  name: Getusagestats
  slug: getusagestats
- key_count: 8
  name: Getvaultresolve
  slug: getvaultresolve
- key_count: 8
  name: Getvaults
  slug: getvaults
- key_count: 8
  name: Getvaultsbaddebt
  slug: getvaultsbaddebt
- key_count: 8
  name: Getvaultsbychainidbyaddress
  slug: getvaultsbychainidbyaddress
- key_count: 8
  name: Getvaultsbychainidbyaddressapy
  slug: getvaultsbychainidbyaddressapy
- key_count: 8
  name: Getvaultsbychainidbyaddresscaphistory
  slug: getvaultsbychainidbyaddresscaphistory
- key_count: 8
  name: Getvaultsbychainidbyaddresscollaterals
  slug: getvaultsbychainidbyaddresscollaterals
- key_count: 8
  name: Getvaultsbychainidbyaddressconfighistory
  slug: getvaultsbychainidbyaddressconfighistory
- key_count: 8
  name: Getvaultsbychainidbyaddressdebtholders
  slug: getvaultsbychainidbyaddressdebtholders
- key_count: 8
  name: Getvaultsbychainidbyaddressevents
  slug: getvaultsbychainidbyaddressevents
- key_count: 8
  name: Getvaultsbychainidbyaddressholders
  slug: getvaultsbychainidbyaddressholders
- key_count: 8
  name: Getvaultsbychainidbyaddressirmhistory
  slug: getvaultsbychainidbyaddressirmhistory
- key_count: 8
  name: Getvaultsbychainidbyaddresslabels
  slug: getvaultsbychainidbyaddresslabels
- key_count: 8
  name: Getvaultsbychainidbyaddressltvhistory
  slug: getvaultsbychainidbyaddressltvhistory
- key_count: 8
  name: Getvaultsbychainidbyaddresspositions
  slug: getvaultsbychainidbyaddresspositions
- key_count: 8
  name: Getvaultsbychainidbyaddresstotals
  slug: getvaultsbychainidbyaddresstotals
- key_count: 8
  name: Getvaultsbychainidbyaddressvisibility
  slug: getvaultsbychainidbyaddressvisibility
- key_count: 8
  name: Getvaultshealthcaps
  slug: getvaultshealthcaps
- key_count: 8
  name: Getvaultshealthutilization
  slug: getvaultshealthutilization
- key_count: 8
  name: Getvaultsopeninterest
  slug: getvaultsopeninterest
- key_count: 8
  name: Getvaultsopeninterestbycollateral
  slug: getvaultsopeninterestbycollateral
- key_count: 8
  name: Listentities
  slug: listentities
- key_count: 8
  name: Listentityaddresses
  slug: listentityaddresses
- key_count: 8
  name: Listentitymembers
  slug: listentitymembers
- key_count: 7
  name: Logoutplatformauthsession
  slug: logoutplatformauthsession
- key_count: 8
  name: Patchadminapikeysbyid
  slug: patchadminapikeysbyid
- key_count: 7
  name: Postadminapikeys
  slug: postadminapikeys
- key_count: 7
  name: Postearnvaultbatch
  slug: postearnvaultbatch
- key_count: 7
  name: Postevkvaultbatch
  slug: postevkvaultbatch
- key_count: 7
  name: Postgraphql
  slug: postgraphql
- key_count: 7
  name: Postvaultresolve
  slug: postvaultresolve
- key_count: 8
  name: Putcuratorvaultsbychainidbyaddresslabels
  slug: putcuratorvaultsbychainidbyaddresslabels
- key_count: 8
  name: Revokeentitymember
  slug: revokeentitymember
- key_count: 7
  name: Revokeplatformadminaccess
  slug: revokeplatformadminaccess
- key_count: 7
  name: Startplatformauthlogin
  slug: startplatformauthlogin
- key_count: 8
  name: Updateentity
  slug: updateentity
- key_count: 8
  name: Updateentitymember
  slug: updateentitymember
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Euler Finance V2 exposes on-chain vault and account data through GraphQL subgraphs hosted on Goldsky. The subgraphs index factory-created EulerVault and EulerEarn contracts, tracking active accounts (
  name: Euler Finance GraphQL API
  slug: euler-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/euler.png
json_schemas:
- name: AccountActivity
  property_count: 8
  slug: account-activity
- name: AccountLiquidityValue
  property_count: 3
  slug: account-liquidity-value
- name: AccountPortfolioResponse
  property_count: 6
  slug: account-portfolio-response
- name: AccountPositionLiquidity
  property_count: 8
  slug: account-position-liquidity
- name: AccountPosition
  property_count: 16
  slug: account-position
- name: ApiKeyCreateRequest
  property_count: 7
  slug: api-key-create-request
- name: ApiKeyCreateResponse
  property_count: 10
  slug: api-key-create-response
- name: ApiKeyResponse
  property_count: 12
  slug: api-key-response
- name: ApiKeyUsageResponse
  property_count: 3
  slug: api-key-usage-response
- name: AssetRef
  property_count: 4
  slug: asset-ref
- name: CapHistoryItem
  property_count: 6
  slug: cap-history-item
- name: ChainStats
  property_count: 0
  slug: chain-stats
- name: Chain
  property_count: 3
  slug: chain
- name: CollateralConfigWithPrice
  property_count: 0
  slug: collateral-config-with-price
- name: CollateralConfig
  property_count: 12
  slug: collateral-config
- name: ConfigHistoryItem
  property_count: 6
  slug: config-history-item
- name: CuratorInfo
  property_count: 3
  slug: curator-info
- name: CuratorVaultLabel
  property_count: 9
  slug: curator-vault-label
- name: DataIssue
  property_count: 7
  slug: data-issue
- name: DetailedHealthResponse
  property_count: 0
  slug: detailed-health-response
- name: EarnIncludePrices
  property_count: 1
  slug: earn-include-prices
- name: EarnStrategyAllocationCap
  property_count: 3
  slug: earn-strategy-allocation-cap
- name: EarnStrategy
  property_count: 18
  slug: earn-strategy
- name: EarnVaultBatchItem
  property_count: 0
  slug: earn-vault-batch-item
- name: EarnVaultBatchMeta
  property_count: 5
  slug: earn-vault-batch-meta
- name: EarnVaultBatchRequest
  property_count: 3
  slug: earn-vault-batch-request
- name: EarnVaultBatchResponse
  property_count: 2
  slug: earn-vault-batch-response
- name: EarnVaultDetailsWithIncludes
  property_count: 0
  slug: earn-vault-details-with-includes
- name: EarnVaultDetails
  property_count: 0
  slug: earn-vault-details
- name: EarnVaultGovernance
  property_count: 10
  slug: earn-vault-governance
- name: EarnVaultManagement
  property_count: 6
  slug: earn-vault-management
- name: EarnVaultSummary
  property_count: 22
  slug: earn-vault-summary
- name: EntityAddressCreateRequest
  property_count: 3
  slug: entity-address-create-request
- name: EntityAddress
  property_count: 4
  slug: entity-address
- name: EntityCreateRequest
  property_count: 10
  slug: entity-create-request
- name: EntityMemberCreateRequest
  property_count: 3
  slug: entity-member-create-request
- name: EntityMemberUpdateRequest
  property_count: 2
  slug: entity-member-update-request
- name: EntityMember
  property_count: 7
  slug: entity-member
- name: EntityUpdateRequest
  property_count: 9
  slug: entity-update-request
- name: Entity
  property_count: 12
  slug: entity
- name: ErrorResponse
  property_count: 1
  slug: error-response
- name: EvkVaultBatchMeta
  property_count: 5
  slug: evk-vault-batch-meta
- name: EvkVaultBatchRequest
  property_count: 3
  slug: evk-vault-batch-request
- name: EvkVaultBatchResponse
  property_count: 2
  slug: evk-vault-batch-response
- name: HealthResponse
  property_count: 4
  slug: health-response
- name: IntrinsicApyHistoryMeta
  property_count: 7
  slug: intrinsic-apy-history-meta
- name: IntrinsicApyHistoryPoint
  property_count: 4
  slug: intrinsic-apy-history-point
- name: IntrinsicApy
  property_count: 7
  slug: intrinsic-apy
- name: IrmHistoryItem
  property_count: 5
  slug: irm-history-item
- name: LtvHistoryItem
  property_count: 13
  slug: ltv-history-item
- name: OracleAdapterChainlinkDetail
  property_count: 1
  slug: oracle-adapter-chainlink-detail
- name: OracleAdapterEntry
  property_count: 6
  slug: oracle-adapter-entry
- name: OracleAdapterPythDetail
  property_count: 6
  slug: oracle-adapter-pyth-detail
- name: OracleAdapter
  property_count: 8
  slug: oracle-adapter
- name: OracleDetailedInfo
  property_count: 3
  slug: oracle-detailed-info
- name: OracleInfo
  property_count: 5
  slug: oracle-info
- name: OraclePriceRaw
  property_count: 7
  slug: oracle-price-raw
- name: OracleResolvedVault
  property_count: 4
  slug: oracle-resolved-vault
- name: OracleRouterConfig
  property_count: 6
  slug: oracle-router-config
- name: OracleRouterState
  property_count: 6
  slug: oracle-router-state
- name: OracleRouterVault
  property_count: 5
  slug: oracle-router-vault
- name: PaginationMeta
  property_count: 6
  slug: pagination-meta
- name: PlatformAdminAccessRequest
  property_count: 1
  slug: platform-admin-access-request
- name: PlatformAdminAccess
  property_count: 4
  slug: platform-admin-access
- name: PlatformAdminCreateAccessResult
  property_count: 2
  slug: platform-admin-create-access-result
- name: PlatformAdminRevokeAccessResult
  property_count: 2
  slug: platform-admin-revoke-access-result
- name: PlatformAuthSession
  property_count: 5
  slug: platform-auth-session
- name: PortfolioBorrowPosition
  property_count: 29
  slug: portfolio-borrow-position
- name: PortfolioSavingsPosition
  property_count: 8
  slug: portfolio-savings-position
- name: Price
  property_count: 9
  slug: price
- name: ProtocolStats
  property_count: 6
  slug: protocol-stats
- name: PublicVaultLabel
  property_count: 8
  slug: public-vault-label
- name: RewardBreakdown
  property_count: 7
  slug: reward-breakdown
- name: RewardsApyHistoryPoint
  property_count: 4
  slug: rewards-apy-history-point
- name: RewardsApy
  property_count: 4
  slug: rewards-apy
- name: SerializedPortfolioAccountPosition
  property_count: 16
  slug: serialized-portfolio-account-position
- name: SerializedPortfolioVault
  property_count: 8
  slug: serialized-portfolio-vault
- name: SubAccount
  property_count: 5
  slug: sub-account
- name: SwapPool
  property_count: 5
  slug: swap-pool
- name: TokenMetadata
  property_count: 3
  slug: token-metadata
- name: Token
  property_count: 10
  slug: token
- name: UsageStatsResponse
  property_count: 4
  slug: usage-stats-response
- name: VaultApyMeta
  property_count: 6
  slug: vault-apy-meta
- name: VaultApyPoint
  property_count: 3
  slug: vault-apy-point
- name: VaultApy
  property_count: 2
  slug: vault-apy
- name: VaultCapHealthItem
  property_count: 10
  slug: vault-cap-health-item
- name: VaultCaps
  property_count: 2
  slug: vault-caps
- name: VaultCollateralDetail
  property_count: 0
  slug: vault-collateral-detail
- name: VaultDetailResponseWithIncludes
  property_count: 0
  slug: vault-detail-response-with-includes
- name: VaultDetailResponse
  property_count: 43
  slug: vault-detail-response
- name: VaultDetailsWithIncludes
  property_count: 0
  slug: vault-details-with-includes
- name: VaultDetails
  property_count: 0
  slug: vault-details
- name: VaultFees
  property_count: 6
  slug: vault-fees
- name: VaultHookedOperations
  property_count: 15
  slug: vault-hooked-operations
- name: VaultHooks
  property_count: 2
  slug: vault-hooks
- name: VaultIncludePrices
  property_count: 2
  slug: vault-include-prices
- name: VaultInterestRateModel
  property_count: 3
  slug: vault-interest-rate-model
- name: VaultInterestRates
  property_count: 3
  slug: vault-interest-rates
- name: VaultLiquidation
  property_count: 3
  slug: vault-liquidation
- name: VaultPosition
  property_count: 5
  slug: vault-position
- name: VaultResolveEntry
  property_count: 7
  slug: vault-resolve-entry
- name: VaultTotalsFreshness
  property_count: 10
  slug: vault-totals-freshness
- name: VaultTotalsMeta
  property_count: 0
  slug: vault-totals-meta
- name: VaultTotalsPoint
  property_count: 7
  slug: vault-totals-point
- name: VaultTotals
  property_count: 2
  slug: vault-totals
- name: VaultVisibility
  property_count: 6
  slug: vault-visibility
- name: Vault
  property_count: 16
  slug: vault
- name: YieldApyBreakdown
  property_count: 5
  slug: yield-apy-breakdown
jsonld:
- class_count: 2
  name: Euler Context
  property_count: 1
  slug: euler-context
layout: provider
modified: '2026-06-14'
name: Euler Finance
nav: Providers
network: true
overview: 'Euler Finance publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, APYs API, Auth API, and 18 more. Tagged areas include DeFi, Lending, Borrowing, Finance, and Ethereum.


  The Euler Finance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Euler Finance''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 67
rate_limits:
- limit_count: 0
  name: Euler V3 Api
  slug: euler-v3-api
rules:
- name: Euler Finance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: euler-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.2
  delta: -5.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/euler/refs/heads/main/screenshots/euler-2026-06-20T180844.png
security:
- kind: authentication
  name: Euler Authentication
  slug: euler-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Euler Domain Security
  slug: euler-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Euler Vulnerability Disclosure
  slug: euler-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: euler
tags:
- DeFi
- Lending
- Borrowing
- Finance
- Ethereum
- Blockchain
- Vaults
- Liquidation
- Interest Rates
- Permissionless
---

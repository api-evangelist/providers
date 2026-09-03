---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 4
  name: Pendle Agentic Access
  operation_count: 34
  slug: pendle-agentic-access
  summary_line: 34 operations · 4 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Assets API from Pendle — 3 operation(s) for assets.
  name: Pendle Assets API
  slug: pendle-assets-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Chains API from Pendle — 1 operation(s) for chains.
  name: Pendle Chains API
  slug: pendle-chains-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Dashboard API from Pendle — 2 operation(s) for dashboard.
  name: Pendle Dashboard API
  slug: pendle-dashboard-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Limit Orders API from Pendle — 7 operation(s) for limit orders.
  name: Pendle Limit Orders API
  slug: pendle-limit-orders-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Markets API from Pendle — 4 operation(s) for markets.
  name: Pendle Markets API
  slug: pendle-markets-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Pendle Emission API from Pendle — 1 operation(s) for pendle emission.
  name: Pendle Pendle Emission API
  slug: pendle-pendle-emission-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The SDK API from Pendle — 10 operation(s) for sdk.
  name: Pendle SDK API
  slug: pendle-sdk-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Statistics API from Pendle — 1 operation(s) for statistics.
  name: Pendle Statistics API
  slug: pendle-statistics-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Transactions API from Pendle — 2 operation(s) for transactions.
  name: Pendle Transactions API
  slug: pendle-transactions-api
- baseURL: https://api-v2.pendle.finance/core
  baseurl_source: declared
  description: The Ve Pendle API from Pendle — 2 operation(s) for ve pendle.
  name: Pendle Ve Pendle API
  slug: pendle-ve-pendle-api
artifact_total: 259
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pendle V2 API Docs Assets API
  slug: open-pendle-assets-api
- collection_type: open
  name: Pendle V2 API Docs Assets Chains API
  slug: open-pendle-chains-api
- collection_type: open
  name: Pendle V2 API Docs Assets Dashboard API
  slug: open-pendle-dashboard-api
- collection_type: open
  name: Pendle V2 API Docs Assets Limit Orders API
  slug: open-pendle-limit-orders-api
- collection_type: open
  name: Pendle V2 API Docs Assets Markets API
  slug: open-pendle-markets-api
- collection_type: open
  name: Pendle V2 API Docs Assets Pendle Emission API
  slug: open-pendle-pendle-emission-api
- collection_type: open
  name: Pendle V2 API Docs Assets SDK API
  slug: open-pendle-sdk-api
- collection_type: open
  name: Pendle V2 API Docs Assets Statistics API
  slug: open-pendle-statistics-api
- collection_type: open
  name: Pendle V2 API Docs Assets Transactions API
  slug: open-pendle-transactions-api
- collection_type: open
  name: Pendle V2 API Docs Assets Ve Pendle API
  slug: open-pendle-ve-pendle-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pendle-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pendle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pendle-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.pendle.finance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pendle.finance
- group: docs
  title: ''
  type: APIReference
  url: https://api-v2.pendle.finance/core/docs
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/pendle-finance/documentation/master/static/pendle-dev-docs/openapi/open-api.json
- group: build
  title: ''
  type: GitHub
  url: https://github.com/pendle-finance
- group: commercial
  title: ''
  type: Pricing
  url: https://api-v2.pendle.finance/dashboard
- group: other
  title: ''
  type: X
  url: https://x.com/pendle_fi
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/pendle
- group: commercial
  title: ''
  type: Plans
  url: plans/pendle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pendle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pendle-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/@pendle
created: '2026-06-14'
description: Pendle is a permissionless yield tokenization protocol that splits yield-bearing assets into Principal Tokens (PT) and Yield Tokens (YT), enabling fixed-yield strategies and yield trading on-chain. The Pendle V2 REST API provides endpoints for querying markets, assets, prices, limit orders, liquidity pool data, implied APY, and user positions across Ethereum, Arbitrum, BSC, Base, Mantle, Optimism, Sonic, Berachain, and other supported chains. A Hosted SDK converts API calls into ready-to-broadcast transaction payloads for swaps, minting, redeeming, and liquidity operations.
examples:
- key_count: 5
  name: Pricescontroller_Ohlcv_V4 Response 200
  slug: PricesController_ohlcv_v4-response-200
- key_count: 5
  name: Statisticscontroller_Getdistinctuserfromtoken Response 200
  slug: StatisticsController_getDistinctUserFromToken-response-200
finops:
- name: Pendle Finops
  service_category: DeFi Protocol API
  slug: pendle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pendle.png
json_schemas:
- name: AddLiquidityData
  property_count: 6
  slug: AddLiquidityData
- name: AddLiquidityDualData
  property_count: 5
  slug: AddLiquidityDualData
- name: AddLiquidityDualResponse
  property_count: 6
  slug: AddLiquidityDualResponse
- name: AddLiquidityResponse
  property_count: 6
  slug: AddLiquidityResponse
- name: AllMarketTotalFeesResponse
  property_count: 1
  slug: AllMarketTotalFeesResponse
- name: ApyBreakdownResponse
  property_count: 6
  slug: ApyBreakdownResponse
- name: AssetAmountResponse
  property_count: 3
  slug: AssetAmountResponse
- name: AssetBasicResponse
  property_count: 10
  slug: AssetBasicResponse
- name: AssetCSVResponse
  property_count: 1
  slug: AssetCSVResponse
- name: AssetData
  property_count: 7
  slug: AssetData
- name: AssetDataCrossChain
  property_count: 8
  slug: AssetDataCrossChain
- name: AssetPricesResponse
  property_count: 3
  slug: AssetPricesResponse
- name: AssetResponse
  property_count: 21
  slug: AssetResponse
- name: AssetsResponse
  property_count: 4
  slug: AssetsResponse
- name: BlockEntity
  property_count: 2
  slug: BlockEntity
- name: ChainIdSimplifiedData
  property_count: 6
  slug: ChainIdSimplifiedData
- name: ChainIdsResponse
  property_count: 1
  slug: ChainIdsResponse
- name: ClaimTokenAmount
  property_count: 2
  slug: ClaimTokenAmount
- name: ContractParamInfo
  property_count: 3
  slug: ContractParamInfo
- name: ConvertData
  property_count: 7
  slug: ConvertData
- name: ConvertResponse
  property_count: 4
  slug: ConvertResponse
- name: ConvertV3Dto
  property_count: 11
  slug: ConvertV3Dto
- name: CreateLimitOrderDto
  property_count: 14
  slug: CreateLimitOrderDto
- name: CrossChainPtData
  property_count: 3
  slug: CrossChainPtData
- name: CrossPtPosition
  property_count: 2
  slug: CrossPtPosition
- name: CurrenyAmountEntity
  property_count: 2
  slug: CurrenyAmountEntity
- name: EstimatedDailyPoolRewardResponse
  property_count: 2
  slug: EstimatedDailyPoolRewardResponse
- name: EulerUserResponse
  property_count: 3
  slug: EulerUserResponse
- name: ExitMarketData
  property_count: 4
  slug: ExitMarketData
- name: ExitMarketResponse
  property_count: 6
  slug: ExitMarketResponse
- name: FeaturedMarketEntity
  property_count: 8
  slug: FeaturedMarketEntity
- name: FeaturedMarketsResponseEntity
  property_count: 4
  slug: FeaturedMarketsResponseEntity
- name: FeeUsd
  property_count: 1
  slug: FeeUsd
- name: GenerateLimitOrderDataDto
  property_count: 8
  slug: GenerateLimitOrderDataDto
- name: GenerateLimitOrderDataResponse
  property_count: 13
  slug: GenerateLimitOrderDataResponse
- name: GenerateScaledOrderDataDto
  property_count: 11
  slug: GenerateScaledOrderDataDto
- name: GenerateScaledOrderResponse
  property_count: 1
  slug: GenerateScaledOrderResponse
- name: GetActiveMarketsResponse
  property_count: 1
  slug: GetActiveMarketsResponse
- name: GetAllAssetsCrossChainResponse
  property_count: 1
  slug: GetAllAssetsCrossChainResponse
- name: GetAllCrossPtsResponse
  property_count: 1
  slug: GetAllCrossPtsResponse
- name: GetAllMarketCategoriesResponse
  property_count: 1
  slug: GetAllMarketCategoriesResponse
- name: GetAllRelatedInfoFromLpAndWlpResponse
  property_count: 4
  slug: GetAllRelatedInfoFromLpAndWlpResponse
- name: GetAllUtilizedProtocolsResponse
  property_count: 1
  slug: GetAllUtilizedProtocolsResponse
- name: GetAssetPricesCrossChainResponse
  property_count: 4
  slug: GetAssetPricesCrossChainResponse
- name: GetAssetPricesResponse
  property_count: 4
  slug: GetAssetPricesResponse
- name: GetAssetsResponse
  property_count: 1
  slug: GetAssetsResponse
- name: GetDistinctUsersFromTokenEntity
  property_count: 1
  slug: GetDistinctUsersFromTokenEntity
- name: GetHistoricalVotesResponse
  property_count: 1
  slug: GetHistoricalVotesResponse
- name: GetInactiveMarketsResponse
  property_count: 1
  slug: GetInactiveMarketsResponse
- name: GetLiquidityTransferableMarketsResponse
  property_count: 1
  slug: GetLiquidityTransferableMarketsResponse
- name: GetMarketStatHistoryCSVResponse
  property_count: 4
  slug: GetMarketStatHistoryCSVResponse
- name: GetMarketsCrossChainResponse
  property_count: 1
  slug: GetMarketsCrossChainResponse
- name: GetMetadataByTemplateResponse
  property_count: 2
  slug: GetMetadataByTemplateResponse
- name: GetMonthlyRevenueResponse
  property_count: 3
  slug: GetMonthlyRevenueResponse
- name: GetOngoingVotesResponse
  property_count: 3
  slug: GetOngoingVotesResponse
- name: GetPendleEmissionResponse
  property_count: 1
  slug: GetPendleEmissionResponse
- name: GetPointsMarketsResponse
  property_count: 1
  slug: GetPointsMarketsResponse
- name: GetSafePendleAddressesResponse
  property_count: 3
  slug: GetSafePendleAddressesResponse
- name: GetSimplifiedDataResponse
  property_count: 1
  slug: GetSimplifiedDataResponse
- name: GetSpotSwappingPriceResponse
  property_count: 6
  slug: GetSpotSwappingPriceResponse
- name: GetVePendleCapResponse
  property_count: 3
  slug: GetVePendleCapResponse
- name: HttpErrorResponse
  property_count: 3
  slug: HttpErrorResponse
- name: ImpliedApy
  property_count: 2
  slug: ImpliedApy
- name: IntegrationAssetEntity
  property_count: 4
  slug: IntegrationAssetEntity
- name: IntegrationAssetResponse
  property_count: 1
  slug: IntegrationAssetResponse
- name: IntegrationEventResponse
  property_count: 1
  slug: IntegrationEventResponse
- name: IntegrationPairResponse
  property_count: 1
  slug: IntegrationPairResponse
- name: JoinExitEvent
  property_count: 10
  slug: JoinExitEvent
- name: LimitOrderResponse
  property_count: 33
  slug: LimitOrderResponse
- name: LimitOrderTakerResponse
  property_count: 4
  slug: LimitOrderTakerResponse
- name: LimitOrdersResponse
  property_count: 4
  slug: LimitOrdersResponse
- name: LimitOrdersTakerResponse
  property_count: 4
  slug: LimitOrdersTakerResponse
- name: LimitOrdersV2Response
  property_count: 4
  slug: LimitOrdersV2Response
- name: LiquidLockerPoolResponse
  property_count: 5
  slug: LiquidLockerPoolResponse
- name: LiquidLockerPoolsResponse
  property_count: 2
  slug: LiquidLockerPoolsResponse
- name: MakerResponse
  property_count: 3
  slug: MakerResponse
- name: MakersResponse
  property_count: 1
  slug: MakersResponse
- name: MarketApyHistoriesCSVResponse
  property_count: 4
  slug: MarketApyHistoriesCSVResponse
- name: MarketApyHistoriesResponse
  property_count: 5
  slug: MarketApyHistoriesResponse
- name: MarketApyHistoryResponse
  property_count: 3
  slug: MarketApyHistoryResponse
- name: MarketAssetsResponse
  property_count: 10
  slug: MarketAssetsResponse
- name: MarketBasicMetadataResponse
  property_count: 67
  slug: MarketBasicMetadataResponse
- name: MarketBasicResponse
  property_count: 6
  slug: MarketBasicResponse
- name: MarketCategoryResponse
  property_count: 2
  slug: MarketCategoryResponse
- name: MarketCrossChainData
  property_count: 15
  slug: MarketCrossChainData
- name: MarketData
  property_count: 13
  slug: MarketData
- name: MarketDataResponse
  property_count: 23
  slug: MarketDataResponse
- name: MarketDetails
  property_count: 7
  slug: MarketDetails
- name: MarketDetailsV2Entity
  property_count: 15
  slug: MarketDetailsV2Entity
- name: MarketEmission
  property_count: 7
  slug: MarketEmission
- name: MarketExtendedInfoResponse
  property_count: 12
  slug: MarketExtendedInfoResponse
- name: MarketHistoricalDataPoint
  property_count: 26
  slug: MarketHistoricalDataPoint
- name: MarketHistoricalDataResponse
  property_count: 4
  slug: MarketHistoricalDataResponse
- name: MarketHistoricalDataTableResponse
  property_count: 28
  slug: MarketHistoricalDataTableResponse
- name: MarketHistoriesResponse
  property_count: 5
  slug: MarketHistoriesResponse
- name: MarketHistoryResponse
  property_count: 19
  slug: MarketHistoryResponse
- name: MarketImpliedApyDataPoint
  property_count: 2
  slug: MarketImpliedApyDataPoint
- name: MarketImpliedApyResponseEntity
  property_count: 4
  slug: MarketImpliedApyResponseEntity
- name: MarketMetaData
  property_count: 1
  slug: MarketMetaData
- name: MarketPointsEntity
  property_count: 2
  slug: MarketPointsEntity
- name: MarketPosition
  property_count: 5
  slug: MarketPosition
- name: MarketResponse
  property_count: 86
  slug: MarketResponse
- name: MarketTokensResponse
  property_count: 4
  slug: MarketTokensResponse
- name: MarketTotalFeesData
  property_count: 2
  slug: MarketTotalFeesData
- name: MarketsResponse
  property_count: 4
  slug: MarketsResponse
- name: MerklDataResponse
  property_count: 3
  slug: MerklDataResponse
- name: MerklRewardResponse
  property_count: 6
  slug: MerklRewardResponse
- name: MerkleClaimableRewardsResponse
  property_count: 1
  slug: MerkleClaimableRewardsResponse
- name: MerkleClaimedRewardsResponse
  property_count: 1
  slug: MerkleClaimedRewardsResponse
- name: MerkleProofResponse
  property_count: 5
  slug: MerkleProofResponse
- name: MerkleProofV2Response
  property_count: 2
  slug: MerkleProofV2Response
- name: MerkleRewardsResponse
  property_count: 3
  slug: MerkleRewardsResponse
- name: MerkleUserCampaignResponse
  property_count: 8
  slug: MerkleUserCampaignResponse
- name: MetadataQueryDto
  property_count: 1
  slug: MetadataQueryDto
- name: MetadataResponse
  property_count: 2
  slug: MetadataResponse
- name: MetadataValuesResponse
  property_count: 1
  slug: MetadataValuesResponse
- name: MintData
  property_count: 3
  slug: MintData
- name: MintResponse
  property_count: 6
  slug: MintResponse
- name: MintSyData
  property_count: 3
  slug: MintSyData
- name: MintSyResponse
  property_count: 6
  slug: MintSyResponse
- name: MorphoConfigResponse
  property_count: 2
  slug: MorphoConfigResponse
- name: MorphoUserResponse
  property_count: 2
  slug: MorphoUserResponse
- name: MultiRouteConvertResponse
  property_count: 5
  slug: MultiRouteConvertResponse
- name: MultiTokenMerkleProofResponse
  property_count: 6
  slug: MultiTokenMerkleProofResponse
- name: NotFoundResponse
  property_count: 2
  slug: NotFoundResponse
- name: NotionalV5
  property_count: 1
  slug: NotionalV5
- name: NotionalVolumeResponse
  property_count: 4
  slug: NotionalVolumeResponse
- name: OHLCVDataPoint
  property_count: 6
  slug: OHLCVDataPoint
- name: OKXCustomParamsDto
  property_count: 4
  slug: OKXCustomParamsDto
- name: OrderBookV2EntryResponse
  property_count: 3
  slug: OrderBookV2EntryResponse
- name: OrderBookV2Response
  property_count: 2
  slug: OrderBookV2Response
- name: OrderFilledStatusResponse
  property_count: 4
  slug: OrderFilledStatusResponse
- name: OrderStateResponse
  property_count: 14
  slug: OrderStateResponse
- name: PairEntity
  property_count: 4
  slug: PairEntity
- name: ParamsBreakdown
  property_count: 3
  slug: ParamsBreakdown
- name: PendleAssetType
  property_count: 0
  slug: PendleAssetType
- name: PendleSwapData
  property_count: 3
  slug: PendleSwapData
- name: PendleSwapDtoV2
  property_count: 5
  slug: PendleSwapDtoV2
- name: PendleSwapInput
  property_count: 2
  slug: PendleSwapInput
- name: PendleSwapResponse
  property_count: 6
  slug: PendleSwapResponse
- name: PendleTokenSupplyResponse
  property_count: 4
  slug: PendleTokenSupplyResponse
- name: PnLTransactionEntity
  property_count: 17
  slug: PnLTransactionEntity
- name: PointMetadataEntity
  property_count: 6
  slug: PointMetadataEntity
- name: PoolResponse
  property_count: 14
  slug: PoolResponse
- name: PoolV2Response
  property_count: 12
  slug: PoolV2Response
- name: PoolVoterAprSwapFeeResponse
  property_count: 6
  slug: PoolVoterAprSwapFeeResponse
- name: PoolVoterAprsSwapFeesResponse
  property_count: 4
  slug: PoolVoterAprsSwapFeesResponse
- name: PoolVoterApyChart
  property_count: 2
  slug: PoolVoterApyChart
- name: PoolVoterApyResponse
  property_count: 2
  slug: PoolVoterApyResponse
- name: PoolVoterApysResponse
  property_count: 3
  slug: PoolVoterApysResponse
- name: Position
  property_count: 4
  slug: Position
- name: PriceAssetData
  property_count: 3
  slug: PriceAssetData
- name: PriceImpactBreakDownData
  property_count: 2
  slug: PriceImpactBreakDownData
- name: PriceOHLCVCSVResponse
  property_count: 6
  slug: PriceOHLCVCSVResponse
- name: PriceOHLCVResponse
  property_count: 7
  slug: PriceOHLCVResponse
- name: PtCrossChainData
  property_count: 3
  slug: PtCrossChainData
- name: PtCrossChainMetadataResponse
  property_count: 2
  slug: PtCrossChainMetadataResponse
- name: RedeemData
  property_count: 3
  slug: RedeemData
- name: RedeemInterestsAndRewardsResponse
  property_count: 5
  slug: RedeemInterestsAndRewardsResponse
- name: RedeemResponse
  property_count: 6
  slug: RedeemResponse
- name: RedeemSyData
  property_count: 3
  slug: RedeemSyData
- name: RedeemSyResponse
  property_count: 6
  slug: RedeemSyResponse
- name: RemoveLiquidityData
  property_count: 5
  slug: RemoveLiquidityData
- name: RemoveLiquidityDualData
  property_count: 4
  slug: RemoveLiquidityDualData
- name: RemoveLiquidityDualResponse
  property_count: 6
  slug: RemoveLiquidityDualResponse
- name: RemoveLiquidityResponse
  property_count: 6
  slug: RemoveLiquidityResponse
- name: Reserves
  property_count: 2
  slug: Reserves
- name: RollOverPtData
  property_count: 5
  slug: RollOverPtData
- name: RollOverPtResponse
  property_count: 7
  slug: RollOverPtResponse
- name: SdkResponse
  property_count: 5
  slug: SdkResponse
- name: SiloUserResponse
  property_count: 2
  slug: SiloUserResponse
- name: SolanaTokenFileResponse
  property_count: 2
  slug: SolanaTokenFileResponse
- name: SolanaTokenPropertiesResponse
  property_count: 1
  slug: SolanaTokenPropertiesResponse
- name: SolanaTokenResponse
  property_count: 6
  slug: SolanaTokenResponse
- name: SpendUnitData
  property_count: 2
  slug: SpendUnitData
- name: SpokePtData
  property_count: 2
  slug: SpokePtData
- name: SupportedAggregator
  property_count: 2
  slug: SupportedAggregator
- name: SupportedAggregatorsResponse
  property_count: 1
  slug: SupportedAggregatorsResponse
- name: SwapData
  property_count: 6
  slug: SwapData
- name: SwapEvent
  property_count: 13
  slug: SwapEvent
- name: SwapPtCrossChainData
  property_count: 2
  slug: SwapPtCrossChainData
- name: SwapPtCrossChainResponse
  property_count: 6
  slug: SwapPtCrossChainResponse
- name: SwapResponse
  property_count: 6
  slug: SwapResponse
- name: SwapWithFixedPricePtAmmData
  property_count: 1
  slug: SwapWithFixedPricePtAmmData
- name: SwapWithFixedPricePtAmmResponse
  property_count: 6
  slug: SwapWithFixedPricePtAmmResponse
- name: SyBasicResponse
  property_count: 27
  slug: SyBasicResponse
- name: SyPosition
  property_count: 3
  slug: SyPosition
- name: SyResponse
  property_count: 27
  slug: SyResponse
- name: SyTokenOutRouteListResponse
  property_count: 1
  slug: SyTokenOutRouteListResponse
- name: SyTokenOutRouteResponse
  property_count: 2
  slug: SyTokenOutRouteResponse
- name: TagDefinitionResponse
  property_count: 2
  slug: TagDefinitionResponse
- name: TokenAmountDto
  property_count: 2
  slug: TokenAmountDto
- name: TokenAmountResponse
  property_count: 2
  slug: TokenAmountResponse
- name: TokenInfoResponse
  property_count: 8
  slug: TokenInfoResponse
- name: TokenProof
  property_count: 4
  slug: TokenProof
- name: TotalFeesWithTimestamp
  property_count: 2
  slug: TotalFeesWithTimestamp
- name: TransactionAction
  property_count: 0
  slug: TransactionAction
- name: TransactionDto
  property_count: 4
  slug: TransactionDto
- name: TransactionResponse
  property_count: 17
  slug: TransactionResponse
- name: TransactionType
  property_count: 0
  slug: TransactionType
- name: TransactionV5Response
  property_count: 11
  slug: TransactionV5Response
- name: TransactionsResponse
  property_count: 4
  slug: TransactionsResponse
- name: TransactionsResponseEntity
  property_count: 2
  slug: TransactionsResponseEntity
- name: TransactionsV4Response
  property_count: 5
  slug: TransactionsV4Response
- name: TransactionsV5Response
  property_count: 5
  slug: TransactionsV5Response
- name: TransferLiquidityData
  property_count: 5
  slug: TransferLiquidityData
- name: TransferLiquidityResponse
  property_count: 7
  slug: TransferLiquidityResponse
- name: TvlAndTradingVolumeResponseEntity
  property_count: 2
  slug: TvlAndTradingVolumeResponseEntity
- name: UniswapTokenListResponse
  property_count: 8
  slug: UniswapTokenListResponse
- name: UserPositionsCrossChainResponse
  property_count: 1
  slug: UserPositionsCrossChainResponse
- name: UserPositionsResponse
  property_count: 9
  slug: UserPositionsResponse
- name: UtilizedProtocolResponse
  property_count: 4
  slug: UtilizedProtocolResponse
- name: ValuationEntity
  property_count: 3
  slug: ValuationEntity
- name: ValuationResponse
  property_count: 2
  slug: ValuationResponse
- name: VePendleApyChartDataPoint
  property_count: 3
  slug: VePendleApyChartDataPoint
- name: VePendleApyChartResponse
  property_count: 4
  slug: VePendleApyChartResponse
- name: VePendleDataResponse
  property_count: 6
  slug: VePendleDataResponse
- name: VePendleExtendedDataResponse
  property_count: 8
  slug: VePendleExtendedDataResponse
- name: VersionResponse
  property_count: 3
  slug: VersionResponse
- name: VoteData
  property_count: 7
  slug: VoteData
- name: VoteResponse
  property_count: 3
  slug: VoteResponse
- name: VoteSnapshotResponse
  property_count: 4
  slug: VoteSnapshotResponse
- name: VoteV2Response
  property_count: 2
  slug: VoteV2Response
- name: VoterApyChartDataPoint
  property_count: 2
  slug: VoterApyChartDataPoint
- name: VoterApyChartResponse
  property_count: 1
  slug: VoterApyChartResponse
- name: WhitelistedSysResponse
  property_count: 1
  slug: WhitelistedSysResponse
- name: WlpDistinctUsersResponse
  property_count: 10
  slug: WlpDistinctUsersResponse
- name: WlpHolderMappingResponse
  property_count: 3
  slug: WlpHolderMappingResponse
- name: YieldRangeResponse
  property_count: 2
  slug: YieldRangeResponse
layout: provider
modified: '2026-06-14'
name: Pendle
nav: Providers
network: true
overview: 'Pendle publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Chains API, Dashboard API, and 7 more. Tagged areas include Web3, DeFi, Yield Tokenization, Crypto, and Principal Tokens.


  The Pendle catalog on APIs.io includes 1 Spectral governance ruleset.


  Pendle''s developer surface includes developer portal, documentation, API reference, GitHub presence, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Pendle Plans Pricing
  plan_count: 4
  slug: pendle-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Pendle Rate Limits
  slug: pendle-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pendle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pendle-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 43.6
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pendle/refs/heads/main/screenshots/pendle-2026-06-20T191632.png
security:
- kind: domain-security
  name: Pendle Domain Security
  slug: pendle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pendle Vulnerability Disclosure
  slug: pendle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pendle
tags:
- Web3
- DeFi
- Yield Tokenization
- Crypto
- Principal Tokens
- Yield Tokens
- AMM
- Liquidity Pools
website: https://www.pendle.finance
---

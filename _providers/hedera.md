---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Hedera Agentic Access
  operation_count: 48
  slug: hedera-agentic-access
  summary_line: 48 operations · 2 acting
api_count: 10
apis:
- description: The accounts object represents the information associated with an account entity and returns a list of account information.The accounts list endpoint is cached and not updated as frequently as the acc
  name: Hedera accounts API
  slug: hedera-accounts-api
- description: The airdrops API from Hedera — 2 operation(s) for airdrops.
  name: Hedera airdrops API
  slug: hedera-airdrops-api
- description: The balance object represents the balance of accounts on the Hedera network.
  name: Hedera balances API
  slug: hedera-balances-api
- description: The blocks API from Hedera — 2 operation(s) for blocks.
  name: Hedera blocks API
  slug: hedera-blocks-api
- description: The contracts objects represents the information associated with contract entities.The contracts list endpoint is cached and not updated as frequently as the contract lookup by a specific ID endpoint.
  name: Hedera contracts API
  slug: hedera-contracts-api
- description: The network API from Hedera — 6 operation(s) for network.
  name: Hedera network API
  slug: hedera-network-api
- description: The schedules object represents the information associated with a schedule entity.The schedules list endpoints is cached and not updated as frequently as the schedule lookup by a specific ID endpoint.
  name: Hedera schedules API
  slug: hedera-schedules-api
- description: The tokens object represents the information associated with a token entity and returns a list of token information.The tokens list endpoint is cached and not updated as frequently as the token lookup
  name: Hedera tokens API
  slug: hedera-tokens-api
- description: The topics object represents the information associated with a topic entity and returns topic messages information.
  name: Hedera topics API
  slug: hedera-topics-api
- description: The transaction object represents the transactions processed on the Hedera network.
  name: Hedera transactions API
  slug: hedera-transactions-api
artifact_total: 220
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mirror Node REST accounts API
  slug: open-hedera-accounts-api
- collection_type: open
  name: Mirror Node REST accounts airdrops API
  slug: open-hedera-airdrops-api
- collection_type: open
  name: Mirror Node REST accounts balances API
  slug: open-hedera-balances-api
- collection_type: open
  name: Mirror Node REST accounts blocks API
  slug: open-hedera-blocks-api
- collection_type: open
  name: Mirror Node REST accounts contracts API
  slug: open-hedera-contracts-api
- collection_type: open
  name: Mirror Node REST accounts network API
  slug: open-hedera-network-api
- collection_type: open
  name: Mirror Node REST accounts schedules API
  slug: open-hedera-schedules-api
- collection_type: open
  name: Mirror Node REST accounts tokens API
  slug: open-hedera-tokens-api
- collection_type: open
  name: Mirror Node REST accounts topics API
  slug: open-hedera-topics-api
- collection_type: open
  name: Mirror Node REST accounts transactions API
  slug: open-hedera-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hedera-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hedera-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.hedera.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hedera.com/hedera
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hashgraph
- group: other
  title: ''
  type: MirrorNodeSource
  url: https://github.com/hiero-ledger/hiero-mirror-node
- group: company
  title: ''
  type: Blog
  url: https://hedera.com/blog
- group: other
  title: ''
  type: Fees
  url: https://hedera.com/fees
- group: operate
  title: ''
  type: Status
  url: https://status.hedera.com
- group: operate
  title: ''
  type: Discord
  url: https://hedera.com/discord
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hedera
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/hashgraph
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/hederahashgraph
- group: other
  title: ''
  type: Foundation
  url: https://hedera.foundation
- group: other
  title: ''
  type: Governance
  url: https://hederacouncil.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hedera.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hedera.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: https://agentic-testnet-mcp.hedera.com/mcp
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://docs.hedera.com/hedera/open-source-solutions/ai-studio-on-hedera/hosted-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/hedera-dev/hedera-skills
created: '2026-06-13'
description: Hedera is an enterprise-grade public distributed ledger platform built for the digital economy and governed by a council of leading global institutions. The Hedera Mirror Node REST API provides read-only access to historical network data including transactions, accounts, tokens, NFTs, smart contracts, consensus topics, blocks, schedules, and network-level information. The public API requires no authentication and supports mainnet, testnet, and previewnet environments.
examples:
- key_count: 8
  name: Contractcall
  slug: contractCall
- key_count: 8
  name: Estimatefees
  slug: estimateFees
- key_count: 8
  name: Getaccount
  slug: getAccount
- key_count: 8
  name: Getaccounts
  slug: getAccounts
- key_count: 8
  name: Getbalances
  slug: getBalances
- key_count: 8
  name: Getblock
  slug: getBlock
- key_count: 8
  name: Getblocks
  slug: getBlocks
- key_count: 8
  name: Getcontract
  slug: getContract
- key_count: 8
  name: Getcontractactions
  slug: getContractActions
- key_count: 8
  name: Getcontractlogsbycontractid
  slug: getContractLogsByContractId
- key_count: 8
  name: Getcontractopcodes
  slug: getContractOpcodes
- key_count: 8
  name: Getcontractresultbyidandtimestamp
  slug: getContractResultByIdAndTimestamp
- key_count: 8
  name: Getcontractresultbytransactionidorhash
  slug: getContractResultByTransactionIdOrHash
- key_count: 8
  name: Getcontractresultsbycontractid
  slug: getContractResultsByContractId
- key_count: 8
  name: Getcontractstate
  slug: getContractState
- key_count: 8
  name: Getcontracts
  slug: getContracts
- key_count: 8
  name: Getcontractslogs
  slug: getContractsLogs
- key_count: 8
  name: Getcontractsresults
  slug: getContractsResults
- key_count: 8
  name: Getcryptoallowances
  slug: getCryptoAllowances
- key_count: 8
  name: Gethookstorage
  slug: getHookStorage
- key_count: 8
  name: Gethooks
  slug: getHooks
- key_count: 8
  name: Getnetworkexchangerate
  slug: getNetworkExchangeRate
- key_count: 8
  name: Getnetworkfees
  slug: getNetworkFees
- key_count: 8
  name: Getnetworknodes
  slug: getNetworkNodes
- key_count: 8
  name: Getnetworkstake
  slug: getNetworkStake
- key_count: 8
  name: Getnetworksupply
  slug: getNetworkSupply
- key_count: 8
  name: Getnft
  slug: getNft
- key_count: 8
  name: Getnftallowances
  slug: getNftAllowances
- key_count: 8
  name: Getnfttransactions
  slug: getNftTransactions
- key_count: 8
  name: Getnfts
  slug: getNfts
- key_count: 8
  name: Getnftsbyaccountid
  slug: getNftsByAccountId
- key_count: 8
  name: Getoutstandingtokenairdrops
  slug: getOutstandingTokenAirdrops
- key_count: 8
  name: Getpendingtokenairdrops
  slug: getPendingTokenAirdrops
- key_count: 8
  name: Getregisterednodes
  slug: getRegisteredNodes
- key_count: 8
  name: Getschedule
  slug: getSchedule
- key_count: 8
  name: Getschedules
  slug: getSchedules
- key_count: 8
  name: Getstakingrewards
  slug: getStakingRewards
- key_count: 8
  name: Gettoken
  slug: getToken
- key_count: 8
  name: Gettokenallowances
  slug: getTokenAllowances
- key_count: 8
  name: Gettokenbalances
  slug: getTokenBalances
- key_count: 8
  name: Gettokens
  slug: getTokens
- key_count: 8
  name: Gettokensbyaccountid
  slug: getTokensByAccountId
- key_count: 8
  name: Gettopic
  slug: getTopic
- key_count: 8
  name: Gettopicmessagebyidandsequencenumber
  slug: getTopicMessageByIdAndSequenceNumber
- key_count: 8
  name: Gettopicmessagebytimestamp
  slug: getTopicMessageByTimestamp
- key_count: 8
  name: Gettopicmessages
  slug: getTopicMessages
- key_count: 8
  name: Gettransaction
  slug: getTransaction
- key_count: 8
  name: Gettransactions
  slug: getTransactions
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hedera.png
json_schemas:
- name: AccessList
  property_count: 2
  slug: AccessList
- name: AccountAlias
  property_count: 0
  slug: AccountAlias
- name: AccountBalance
  property_count: 3
  slug: AccountBalance
- name: AccountBalanceTransactions
  property_count: 0
  slug: AccountBalanceTransactions
- name: AccountInfo
  property_count: 18
  slug: AccountInfo
- name: Accounts
  property_count: 0
  slug: Accounts
- name: AccountsResponse
  property_count: 2
  slug: AccountsResponse
- name: Alias
  property_count: 0
  slug: Alias
- name: Allowance
  property_count: 5
  slug: Allowance
- name: AssessedCustomFee
  property_count: 4
  slug: AssessedCustomFee
- name: AuthorizationList
  property_count: 6
  slug: AuthorizationList
- name: Balance
  property_count: 3
  slug: Balance
- name: BalancesResponse
  property_count: 3
  slug: BalancesResponse
- name: Block
  property_count: 10
  slug: Block
- name: Blocks
  property_count: 0
  slug: Blocks
- name: BlocksResponse
  property_count: 2
  slug: BlocksResponse
- name: Bloom
  property_count: 0
  slug: Bloom
- name: ChunkInfo
  property_count: 3
  slug: ChunkInfo
- name: ConsensusCustomFees
  property_count: 2
  slug: ConsensusCustomFees
- name: Contract
  property_count: 16
  slug: Contract
- name: ContractAction
  property_count: 17
  slug: ContractAction
- name: ContractActions
  property_count: 0
  slug: ContractActions
- name: ContractActionsResponse
  property_count: 2
  slug: ContractActionsResponse
- name: ContractCallRequest
  property_count: 8
  slug: ContractCallRequest
- name: ContractCallResponse
  property_count: 1
  slug: ContractCallResponse
- name: ContractLog
  property_count: 0
  slug: ContractLog
- name: ContractLogTopics
  property_count: 0
  slug: ContractLogTopics
- name: ContractLogs
  property_count: 0
  slug: ContractLogs
- name: ContractLogsResponse
  property_count: 2
  slug: ContractLogsResponse
- name: ContractResponse
  property_count: 0
  slug: ContractResponse
- name: ContractResult
  property_count: 33
  slug: ContractResult
- name: ContractResultDetails
  property_count: 0
  slug: ContractResultDetails
- name: ContractResultLog
  property_count: 6
  slug: ContractResultLog
- name: ContractResultLogs
  property_count: 0
  slug: ContractResultLogs
- name: ContractResultStateChange
  property_count: 5
  slug: ContractResultStateChange
- name: ContractResultStateChanges
  property_count: 0
  slug: ContractResultStateChanges
- name: ContractResults
  property_count: 0
  slug: ContractResults
- name: ContractResultsResponse
  property_count: 2
  slug: ContractResultsResponse
- name: ContractState
  property_count: 5
  slug: ContractState
- name: ContractStateResponse
  property_count: 2
  slug: ContractStateResponse
- name: Contracts
  property_count: 0
  slug: Contracts
- name: ContractsResponse
  property_count: 2
  slug: ContractsResponse
- name: CryptoAllowance
  property_count: 0
  slug: CryptoAllowance
- name: CryptoAllowances
  property_count: 0
  slug: CryptoAllowances
- name: CryptoAllowancesResponse
  property_count: 2
  slug: CryptoAllowancesResponse
- name: CustomFeeLimit
  property_count: 3
  slug: CustomFeeLimit
- name: CustomFees
  property_count: 4
  slug: CustomFees
- name: EntityId
  property_count: 0
  slug: EntityId
- name: EntityIdQuery
  property_count: 0
  slug: EntityIdQuery
- name: Error
  property_count: 1
  slug: Error
- name: EthereumHash
  property_count: 0
  slug: EthereumHash
- name: EvmAddress
  property_count: 0
  slug: EvmAddress
- name: EvmAddressNullable
  property_count: 0
  slug: EvmAddressNullable
- name: EvmAddressWithShardRealm
  property_count: 0
  slug: EvmAddressWithShardRealm
- name: ExchangeRate
  property_count: 3
  slug: ExchangeRate
- name: FeeEstimate
  property_count: 2
  slug: FeeEstimate
- name: FeeEstimateMode
  property_count: 0
  slug: FeeEstimateMode
- name: FeeEstimateNetwork
  property_count: 2
  slug: FeeEstimateNetwork
- name: FeeEstimateResponse
  property_count: 5
  slug: FeeEstimateResponse
- name: FeeExtra
  property_count: 6
  slug: FeeExtra
- name: FixedCustomFee
  property_count: 3
  slug: FixedCustomFee
- name: FixedFee
  property_count: 4
  slug: FixedFee
- name: FractionalFee
  property_count: 7
  slug: FractionalFee
- name: HederaHash
  property_count: 0
  slug: HederaHash
- name: Hook
  property_count: 9
  slug: Hook
- name: HookStorage
  property_count: 3
  slug: HookStorage
- name: HooksResponse
  property_count: 2
  slug: HooksResponse
- name: HooksStorageResponse
  property_count: 4
  slug: HooksStorageResponse
- name: Key
  property_count: 2
  slug: Key
- name: Links
  property_count: 1
  slug: Links
- name: LogTopicQueryParam
  property_count: 0
  slug: LogTopicQueryParam
- name: NetworkExchangeRateSetResponse
  property_count: 3
  slug: NetworkExchangeRateSetResponse
- name: NetworkFee
  property_count: 2
  slug: NetworkFee
- name: NetworkFees
  property_count: 0
  slug: NetworkFees
- name: NetworkFeesResponse
  property_count: 2
  slug: NetworkFeesResponse
- name: NetworkNode
  property_count: 20
  slug: NetworkNode
- name: NetworkNodes
  property_count: 0
  slug: NetworkNodes
- name: NetworkNodesResponse
  property_count: 2
  slug: NetworkNodesResponse
- name: NetworkStakeResponse
  property_count: 14
  slug: NetworkStakeResponse
- name: NetworkSupplyResponse
  property_count: 3
  slug: NetworkSupplyResponse
- name: Nft
  property_count: 9
  slug: Nft
- name: NftAllowance
  property_count: 5
  slug: NftAllowance
- name: NftAllowances
  property_count: 0
  slug: NftAllowances
- name: NftAllowancesResponse
  property_count: 2
  slug: NftAllowancesResponse
- name: NftTransactionHistory
  property_count: 2
  slug: NftTransactionHistory
- name: NftTransactionTransfer
  property_count: 7
  slug: NftTransactionTransfer
- name: Nfts
  property_count: 2
  slug: Nfts
- name: Opcode
  property_count: 9
  slug: Opcode
- name: OpcodesResponse
  property_count: 6
  slug: OpcodesResponse
- name: PositiveNumber
  property_count: 0
  slug: PositiveNumber
- name: RegisteredBlockNodeApi
  property_count: 0
  slug: RegisteredBlockNodeApi
- name: RegisteredBlockNodeEndpoint
  property_count: 1
  slug: RegisteredBlockNodeEndpoint
- name: RegisteredGeneralServiceEndpoint
  property_count: 1
  slug: RegisteredGeneralServiceEndpoint
- name: RegisteredMirrorNodeEndpoint
  property_count: 0
  slug: RegisteredMirrorNodeEndpoint
- name: RegisteredNode
  property_count: 6
  slug: RegisteredNode
- name: RegisteredNodeType
  property_count: 0
  slug: RegisteredNodeType
- name: RegisteredNodes
  property_count: 0
  slug: RegisteredNodes
- name: RegisteredNodesResponse
  property_count: 2
  slug: RegisteredNodesResponse
- name: RegisteredRpcRelayEndpoint
  property_count: 0
  slug: RegisteredRpcRelayEndpoint
- name: RegisteredServiceEndpoint
  property_count: 9
  slug: RegisteredServiceEndpoint
- name: RegisteredServiceEndpoints
  property_count: 0
  slug: RegisteredServiceEndpoints
- name: RoyaltyFee
  property_count: 4
  slug: RoyaltyFee
- name: Schedule
  property_count: 12
  slug: Schedule
- name: ScheduleSignature
  property_count: 4
  slug: ScheduleSignature
- name: Schedules
  property_count: 0
  slug: Schedules
- name: SchedulesResponse
  property_count: 2
  slug: SchedulesResponse
- name: ServiceEndpoint
  property_count: 3
  slug: ServiceEndpoint
- name: ServiceEndpoints
  property_count: 0
  slug: ServiceEndpoints
- name: StakingReward
  property_count: 3
  slug: StakingReward
- name: StakingRewardTransfer
  property_count: 2
  slug: StakingRewardTransfer
- name: StakingRewardTransfers
  property_count: 0
  slug: StakingRewardTransfers
- name: StakingRewardsResponse
  property_count: 2
  slug: StakingRewardsResponse
- name: Timestamp
  property_count: 0
  slug: Timestamp
- name: TimestampNullable
  property_count: 0
  slug: TimestampNullable
- name: TimestampRange
  property_count: 2
  slug: TimestampRange
- name: TimestampRangeNullable
  property_count: 2
  slug: TimestampRangeNullable
- name: Token
  property_count: 7
  slug: Token
- name: TokenAirdrop
  property_count: 6
  slug: TokenAirdrop
- name: TokenAirdrops
  property_count: 0
  slug: TokenAirdrops
- name: TokenAirdropsResponse
  property_count: 2
  slug: TokenAirdropsResponse
- name: TokenAllowance
  property_count: 0
  slug: TokenAllowance
- name: TokenAllowances
  property_count: 0
  slug: TokenAllowances
- name: TokenAllowancesResponse
  property_count: 2
  slug: TokenAllowancesResponse
- name: TokenBalance
  property_count: 2
  slug: TokenBalance
- name: TokenBalancesResponse
  property_count: 3
  slug: TokenBalancesResponse
- name: TokenDistribution
  property_count: 0
  slug: TokenDistribution
- name: TokenInfo
  property_count: 29
  slug: TokenInfo
- name: TokenRelationship
  property_count: 7
  slug: TokenRelationship
- name: TokenRelationshipResponse
  property_count: 2
  slug: TokenRelationshipResponse
- name: Tokens
  property_count: 0
  slug: Tokens
- name: TokensResponse
  property_count: 2
  slug: TokensResponse
- name: Topic
  property_count: 12
  slug: Topic
- name: TopicMessage
  property_count: 8
  slug: TopicMessage
- name: TopicMessages
  property_count: 0
  slug: TopicMessages
- name: TopicMessagesResponse
  property_count: 2
  slug: TopicMessagesResponse
- name: Transaction
  property_count: 24
  slug: Transaction
- name: TransactionByIdResponse
  property_count: 1
  slug: TransactionByIdResponse
- name: TransactionDetail
  property_count: 0
  slug: TransactionDetail
- name: TransactionDetails
  property_count: 0
  slug: TransactionDetails
- name: TransactionId
  property_count: 4
  slug: TransactionId
- name: TransactionIdStr
  property_count: 0
  slug: TransactionIdStr
- name: TransactionTypes
  property_count: 0
  slug: TransactionTypes
- name: Transactions
  property_count: 0
  slug: Transactions
- name: TransactionsResponse
  property_count: 2
  slug: TransactionsResponse
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-07-12'
name: Hedera
nav: Providers
network: true
overview: 'Hedera publishes 10 APIs on the [APIs.io](https://apis.io/) network, including accounts API, airdrops API, balances API, and 7 more. Tagged areas include Distributed Ledger, Blockchain, DLT, Hashgraph, and Transactions.


  The Hedera catalog on APIs.io includes 1 Spectral governance ruleset.


  Hedera''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, status page, YouTube channel, and 14 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 21
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- name: Hedera API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hedera-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.9
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hedera/refs/heads/main/screenshots/hedera-2026-06-20T182613.png
security:
- kind: domain-security
  name: Hedera Domain Security
  slug: hedera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hedera
tags:
- Distributed Ledger
- Blockchain
- DLT
- Hashgraph
- Transactions
- Tokens
- NFTs
- Smart Contracts
- Enterprise
website: https://portal.hedera.com
---

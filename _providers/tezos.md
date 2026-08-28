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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tezos Agentic Access
  operation_count: 288
  slug: tezos-agentic-access
  summary_line: 288 operations · 3 acting
api_count: 34
apis:
- description: 'The Accounts API returns profile data for any Tezos address — user wallets, delegates (bakers), smart contracts, and ghost accounts. Endpoints expose balance, staked amounts, token holdings, contract '
  name: TzKT Accounts API
  slug: tzkt-accounts
- description: The Blocks API exposes Tezos block-level data including block hash, level, protocol, timestamp, baker, priority, number of operations, volume, fees, and reward metadata. Blocks can be fetched by hash,
  name: TzKT Blocks API
  slug: tzkt-blocks
- description: 'The Operations API is the broadest endpoint group in TzKT, covering all Tezos operation types: transactions, originations, delegations, reveals, endorsements, double-bake evidence, ballot and proposal'
  name: TzKT Operations API
  slug: tzkt-operations
- description: The Contracts API provides access to Tezos smart contract metadata, storage, entrypoints, views, and code. Storage can be retrieved as decoded JSON at the current state or at a historical block level.
  name: TzKT Contracts API
  slug: tzkt-contracts
- description: The Big Maps API indexes all Tezos big map allocations across smart contracts, exposing individual key-value entries with historical tracking. Keys and values are decoded from Micheline to JSON. Suppo
  name: TzKT Big Maps API
  slug: tzkt-bigmaps
- description: The Tokens API covers FA1.2, FA2, and NFT token standards on Tezos. Endpoints expose token metadata, holder balances, and transfer history. Token balances can be queried per account or per token contr
  name: TzKT Tokens API
  slug: tzkt-tokens
- description: The Delegations and Staking APIs expose baking (validation) economics on Tezos. Delegations endpoints return active and historical delegation assignments between addresses and bakers. Staking endpoint
  name: TzKT Delegations and Staking API
  slug: tzkt-delegations-staking
- description: The Governance API exposes Tezos on-chain governance data including voting periods, proposals, ballots, and quorum thresholds. Developers can query the history of all protocol upgrade votes, the curre
  name: TzKT Governance API
  slug: tzkt-governance
- description: 'The Protocols API returns metadata for each Tezos protocol version including hash, first and last cycle, constants (block time, gas limits, baking rewards), and amendment history. Useful for building '
  name: TzKT Protocols API
  slug: tzkt-protocols
- description: 'The TzKT WebSocket API uses SignalR to deliver real-time push notifications to subscribed clients. Channels cover new blocks, new and confirmed operations (filtered by sender, target, or entrypoint), '
  name: TzKT WebSocket API
  slug: tzkt-websocket
- description: The Accounts API from Tezos — 12 operation(s) for accounts.
  name: Tezos Accounts API
  slug: tezos-accounts-api
- description: The BigMaps API from Tezos — 12 operation(s) for bigmaps.
  name: Tezos BigMaps API
  slug: tezos-bigmaps-api
- description: The Blocks API from Tezos — 7 operation(s) for blocks.
  name: Tezos Blocks API
  slug: tezos-blocks-api
- description: The Commitments API from Tezos — 3 operation(s) for commitments.
  name: Tezos Commitments API
  slug: tezos-commitments-api
- description: The Constants API from Tezos — 3 operation(s) for constants.
  name: Tezos Constants API
  slug: tezos-constants-api
- description: The Contracts API from Tezos — 25 operation(s) for contracts.
  name: Tezos Contracts API
  slug: tezos-contracts-api
- description: The Cycles API from Tezos — 3 operation(s) for cycles.
  name: Tezos Cycles API
  slug: tezos-cycles-api
- description: The Delegates API from Tezos — 3 operation(s) for delegates.
  name: Tezos Delegates API
  slug: tezos-delegates-api
- description: The Domains API from Tezos — 3 operation(s) for domains.
  name: Tezos Domains API
  slug: tezos-domains-api
- description: The Events API from Tezos — 2 operation(s) for events.
  name: Tezos Events API
  slug: tezos-events-api
- description: The Head API from Tezos — 1 operation(s) for head.
  name: Tezos Head API
  slug: tezos-head-api
- description: The Helpers API from Tezos — 2 operation(s) for helpers.
  name: Tezos Helpers API
  slug: tezos-helpers-api
- description: The Operations API from Tezos — 142 operation(s) for operations.
  name: Tezos Operations API
  slug: tezos-operations-api
- description: The Protocols API from Tezos — 6 operation(s) for protocols.
  name: Tezos Protocols API
  slug: tezos-protocols-api
- description: The Quotes API from Tezos — 3 operation(s) for quotes.
  name: Tezos Quotes API
  slug: tezos-quotes-api
- description: The Rewards API from Tezos — 8 operation(s) for rewards.
  name: Tezos Rewards API
  slug: tezos-rewards-api
- description: The Rights API from Tezos — 2 operation(s) for rights.
  name: Tezos Rights API
  slug: tezos-rights-api
- description: The SmartRollups API from Tezos — 12 operation(s) for smartrollups.
  name: Tezos SmartRollups API
  slug: tezos-smartrollups-api
- description: The Software API from Tezos — 2 operation(s) for software.
  name: Tezos Software API
  slug: tezos-software-api
- description: The Staking API from Tezos — 4 operation(s) for staking.
  name: Tezos Staking API
  slug: tezos-staking-api
- description: The Statistics API from Tezos — 4 operation(s) for statistics.
  name: Tezos Statistics API
  slug: tezos-statistics-api
- description: The Tickets API from Tezos — 7 operation(s) for tickets.
  name: Tezos Tickets API
  slug: tezos-tickets-api
- description: The Tokens API from Tezos — 7 operation(s) for tokens.
  name: Tezos Tokens API
  slug: tezos-tokens-api
- description: The Voting API from Tezos — 14 operation(s) for voting.
  name: Tezos Voting API
  slug: tezos-voting-api
artifact_total: 285
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TzKT Accounts API
  slug: open-tezos-accounts-api
- collection_type: open
  name: TzKT Accounts BigMaps API
  slug: open-tezos-bigmaps-api
- collection_type: open
  name: TzKT Accounts Blocks API
  slug: open-tezos-blocks-api
- collection_type: open
  name: TzKT Accounts Commitments API
  slug: open-tezos-commitments-api
- collection_type: open
  name: TzKT Accounts Constants API
  slug: open-tezos-constants-api
- collection_type: open
  name: TzKT Accounts Contracts API
  slug: open-tezos-contracts-api
- collection_type: open
  name: TzKT Accounts Cycles API
  slug: open-tezos-cycles-api
- collection_type: open
  name: TzKT Accounts Delegates API
  slug: open-tezos-delegates-api
- collection_type: open
  name: TzKT Accounts Domains API
  slug: open-tezos-domains-api
- collection_type: open
  name: TzKT Accounts Events API
  slug: open-tezos-events-api
- collection_type: open
  name: TzKT Accounts Head API
  slug: open-tezos-head-api
- collection_type: open
  name: TzKT Accounts Helpers API
  slug: open-tezos-helpers-api
- collection_type: open
  name: TzKT Accounts Operations API
  slug: open-tezos-operations-api
- collection_type: open
  name: TzKT Accounts Protocols API
  slug: open-tezos-protocols-api
- collection_type: open
  name: TzKT Accounts Quotes API
  slug: open-tezos-quotes-api
- collection_type: open
  name: TzKT Accounts Rewards API
  slug: open-tezos-rewards-api
- collection_type: open
  name: TzKT Accounts Rights API
  slug: open-tezos-rights-api
- collection_type: open
  name: TzKT Accounts SmartRollups API
  slug: open-tezos-smartrollups-api
- collection_type: open
  name: TzKT Accounts Software API
  slug: open-tezos-software-api
- collection_type: open
  name: TzKT Accounts Staking API
  slug: open-tezos-staking-api
- collection_type: open
  name: TzKT Accounts Statistics API
  slug: open-tezos-statistics-api
- collection_type: open
  name: TzKT Accounts Tickets API
  slug: open-tezos-tickets-api
- collection_type: open
  name: TzKT Accounts Tokens API
  slug: open-tezos-tokens-api
- collection_type: open
  name: TzKT Accounts Voting API
  slug: open-tezos-voting-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tezos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tezos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tzkt.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tzkt.io
- group: docs
  title: ''
  type: Documentation
  url: https://api.tzkt.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baking-bad
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/baking-bad/tzkt
- group: other
  title: ''
  type: MainnetAPI
  url: https://api.tzkt.io/v1
- group: other
  title: ''
  type: GhostnetAPI
  url: https://api.ghostnet.tzkt.io/v1
- group: commercial
  title: ''
  type: License
  url: https://github.com/baking-bad/tzkt/blob/master/LICENSE
- group: operate
  title: ''
  type: Status
  url: https://tzkt.io
- group: company
  title: ''
  type: Blog
  url: https://baking-bad.org/blog/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/openapi.json
- group: commercial
  title: ''
  type: Plans
  url: plans/tezos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tezos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tezos-finops.yml
created: '2026-06-13'
description: Tezos is a self-amending blockchain platform that uses on-chain governance to upgrade its protocol without hard forks. The primary developer API surface is provided by TzKT, an open-source Tezos blockchain indexer built and maintained by the Baking Bad team. TzKT exposes a comprehensive REST API (https://api.tzkt.io) covering 100+ endpoints for querying blocks, accounts, operations, delegations, smart contracts, big maps, tokens (FA1.2/FA2/NFTs), staking data, baking rights, governance periods, and protocol metadata on the Tezos mainnet. The API supports deep filtering, deep selection, deep sorting, CSV exports, and historical data queries at specific block heights. A WebSocket API (SignalR) provides real-time subscription streams for new blocks and operations. The public TzKT API is freely available with no API key required; rate limits apply per IP via standard RateLimit headers and HTTP 429 responses. TzKT Pro is available for teams requiring elevated quotas and dedicated
  support. The indexer is MIT-licensed and can also be self-hosted against a Tezos node.
examples:
- key_count: 6
  name: Example Accounts
  slug: example-accounts
- key_count: 6
  name: Example Bigmaps
  slug: example-bigmaps
- key_count: 6
  name: Example Blocks
  slug: example-blocks
- key_count: 6
  name: Example Commitments
  slug: example-commitments
- key_count: 6
  name: Example Constants
  slug: example-constants
- key_count: 6
  name: Example Contracts
  slug: example-contracts
- key_count: 6
  name: Example Cycles
  slug: example-cycles
- key_count: 6
  name: Example Delegates
  slug: example-delegates
- key_count: 6
  name: Example Domains
  slug: example-domains
- key_count: 6
  name: Example Events
  slug: example-events
- key_count: 6
  name: Example Head
  slug: example-head
- key_count: 6
  name: Example Helpers
  slug: example-helpers
- key_count: 6
  name: Example Operations
  slug: example-operations
- key_count: 6
  name: Example Protocols
  slug: example-protocols
- key_count: 6
  name: Example Quotes
  slug: example-quotes
- key_count: 6
  name: Example Rewards
  slug: example-rewards
- key_count: 6
  name: Example Rights
  slug: example-rights
- key_count: 6
  name: Example Smartrollups
  slug: example-smartrollups
- key_count: 6
  name: Example Software
  slug: example-software
- key_count: 6
  name: Example Staking
  slug: example-staking
- key_count: 6
  name: Example Statistics
  slug: example-statistics
- key_count: 6
  name: Example Tickets
  slug: example-tickets
- key_count: 6
  name: Example Tokens
  slug: example-tokens
- key_count: 6
  name: Example Voting
  slug: example-voting
finops:
- name: Tezos Finops
  service_category: API
  slug: tezos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tezos.png
json_schemas:
- name: Account
  property_count: 2
  slug: account
- name: AccountParameter
  property_count: 9
  slug: accountparameter
- name: AccountTypeParameter
  property_count: 2
  slug: accounttypeparameter
- name: ActivationOperation
  property_count: 0
  slug: activationoperation
- name: Activity
  property_count: 2
  slug: activity
- name: AddressNullParameter
  property_count: 5
  slug: addressnullparameter
- name: AddressParameter
  property_count: 4
  slug: addressparameter
- name: Alias
  property_count: 2
  slug: alias
- name: AnnotationType
  property_count: 0
  slug: annotationtype
- name: AnyOfParameter
  property_count: 3
  slug: anyofparameter
- name: AttestationOperation
  property_count: 0
  slug: attestationoperation
- name: AttestationRewardOperation
  property_count: 0
  slug: attestationrewardoperation
- name: AutostakingOperation
  property_count: 0
  slug: autostakingoperation
- name: BakerRewards
  property_count: 80
  slug: bakerrewards
- name: BakingOperation
  property_count: 0
  slug: bakingoperation
- name: BakingRight
  property_count: 8
  slug: bakingright
- name: BakingRightStatusParameter
  property_count: 2
  slug: bakingrightstatusparameter
- name: BakingRightTypeParameter
  property_count: 2
  slug: bakingrighttypeparameter
- name: BalanceTooLowError
  property_count: 0
  slug: balancetoolowerror
- name: BallotOperation
  property_count: 0
  slug: ballotoperation
- name: BaseOperationError
  property_count: 0
  slug: baseoperationerror
- name: BigIntegerNullableParameter
  property_count: 9
  slug: bigintegernullableparameter
- name: BigMap
  property_count: 12
  slug: bigmap
- name: BigMapActionParameter
  property_count: 4
  slug: bigmapactionparameter
- name: BigMapDiff
  property_count: 4
  slug: bigmapdiff
- name: BigMapInterface
  property_count: 4
  slug: bigmapinterface
- name: BigMapKey
  property_count: 8
  slug: bigmapkey
- name: BigMapKeyFull
  property_count: 11
  slug: bigmapkeyfull
- name: BigMapKeyHistorical
  property_count: 5
  slug: bigmapkeyhistorical
- name: BigMapKeyShort
  property_count: 3
  slug: bigmapkeyshort
- name: BigMapKeyUpdate
  property_count: 5
  slug: bigmapkeyupdate
- name: BigMapTagsParameter
  property_count: 3
  slug: bigmaptagsparameter
- name: BigMapUpdate
  property_count: 8
  slug: bigmapupdate
- name: Block
  property_count: 78
  slug: block
- name: BoolParameter
  property_count: 2
  slug: boolparameter
- name: Commitment
  property_count: 6
  slug: commitment
- name: Constant
  property_count: 8
  slug: constant
- name: Contract
  property_count: 0
  slug: contract
- name: ContractEvent
  property_count: 10
  slug: contractevent
- name: ContractInterface
  property_count: 4
  slug: contractinterface
- name: ContractKindParameter
  property_count: 4
  slug: contractkindparameter
- name: ContractTagsParameter
  property_count: 3
  slug: contracttagsparameter
- name: ContractView
  property_count: 7
  slug: contractview
- name: Cycle
  property_count: 19
  slug: cycle
- name: DalAttestationRewardOperation
  property_count: 0
  slug: dalattestationrewardoperation
- name: DalEntrapmentEvidenceOperation
  property_count: 0
  slug: dalentrapmentevidenceoperation
- name: DalPublishCommitmentOperation
  property_count: 0
  slug: dalpublishcommitmentoperation
- name: DateTimeParameter
  property_count: 8
  slug: datetimeparameter
- name: Delegate
  property_count: 0
  slug: delegate
- name: DelegateInfo
  property_count: 3
  slug: delegateinfo
- name: DelegationOperation
  property_count: 0
  slug: delegationoperation
- name: Delegator
  property_count: 6
  slug: delegator
- name: DelegatorRewards
  property_count: 66
  slug: delegatorrewards
- name: Domain
  property_count: 12
  slug: domain
- name: DoubleBakingOperation
  property_count: 0
  slug: doublebakingoperation
- name: DoubleConsensusKindParameter
  property_count: 2
  slug: doubleconsensuskindparameter
- name: DoubleConsensusOperation
  property_count: 0
  slug: doubleconsensusoperation
- name: DrainDelegateOperation
  property_count: 0
  slug: draindelegateoperation
- name: EmptyAccount
  property_count: 0
  slug: emptyaccount
- name: Entrypoint
  property_count: 5
  slug: entrypoint
- name: EntrypointInterface
  property_count: 2
  slug: entrypointinterface
- name: EpochStatusParameter
  property_count: 4
  slug: epochstatusparameter
- name: EventInterface
  property_count: 2
  slug: eventinterface
- name: ExpressionAlreadyRegisteredError
  property_count: 0
  slug: expressionalreadyregisterederror
- name: ExpressionParameter
  property_count: 4
  slug: expressionparameter
- name: Ghost
  property_count: 0
  slug: ghost
- name: HistoricalBalance
  property_count: 4
  slug: historicalbalance
- name: IAnnotation
  property_count: 2
  slug: iannotation
- name: IMicheline
  property_count: 1
  slug: imicheline
- name: IncreasePaidStorageOperation
  property_count: 0
  slug: increasepaidstorageoperation
- name: Int32NullParameter
  property_count: 9
  slug: int32nullparameter
- name: Int32Parameter
  property_count: 8
  slug: int32parameter
- name: Int64NullParameter
  property_count: 9
  slug: int64nullparameter
- name: Int64Parameter
  property_count: 9
  slug: int64parameter
- name: JsonParameter
  property_count: 11
  slug: jsonparameter
- name: MichelineFormat
  property_count: 0
  slug: michelineformat
- name: MichelineParameter
  property_count: 4
  slug: michelineparameter
- name: MichelinePrim
  property_count: 3
  slug: michelineprim
- name: MichelineType
  property_count: 0
  slug: michelinetype
- name: MigrationKindParameter
  property_count: 4
  slug: migrationkindparameter
- name: MigrationOperation
  property_count: 0
  slug: migrationoperation
- name: NatParameter
  property_count: 8
  slug: natparameter
- name: NonceRevelationOperation
  property_count: 0
  slug: noncerevelationoperation
- name: NonExistingContractError
  property_count: 0
  slug: nonexistingcontracterror
- name: OffsetParameter
  property_count: 3
  slug: offsetparameter
- name: Operation
  property_count: 0
  slug: operation
- name: OperationError
  property_count: 1
  slug: operationerror
- name: OperationStatusParameter
  property_count: 2
  slug: operationstatusparameter
- name: OpHashParameter
  property_count: 4
  slug: ophashparameter
- name: OriginatedContract
  property_count: 6
  slug: originatedcontract
- name: OriginationOperation
  property_count: 0
  slug: originationoperation
- name: PeriodInfo
  property_count: 5
  slug: periodinfo
- name: PreattestationOperation
  property_count: 0
  slug: preattestationoperation
- name: PrimType
  property_count: 0
  slug: primtype
- name: Proposal
  property_count: 9
  slug: proposal
- name: ProposalAlias
  property_count: 2
  slug: proposalalias
- name: ProposalOperation
  property_count: 0
  slug: proposaloperation
- name: Protocol
  property_count: 9
  slug: protocol
- name: ProtocolConstants
  property_count: 43
  slug: protocolconstants
- name: ProtocolParameter
  property_count: 4
  slug: protocolparameter
- name: Quote
  property_count: 10
  slug: quote
- name: QuoteShort
  property_count: 8
  slug: quoteshort
- name: RefutationGameStatusParameter
  property_count: 4
  slug: refutationgamestatusparameter
- name: RefutationMoveParameter
  property_count: 4
  slug: refutationmoveparameter
- name: RegisterConstantOperation
  property_count: 0
  slug: registerconstantoperation
- name: RelatedContract
  property_count: 7
  slug: relatedcontract
- name: RevealOperation
  property_count: 0
  slug: revealoperation
- name: RevelationPenaltyOperation
  property_count: 0
  slug: revelationpenaltyoperation
- name: RewardSplit
  property_count: 0
  slug: rewardsplit
- name: Rollup
  property_count: 0
  slug: rollup
- name: SecondaryKeyTypeParameter
  property_count: 2
  slug: secondarykeytypeparameter
- name: SelectionParameter
  property_count: 2
  slug: selectionparameter
- name: SelectParameter
  property_count: 2
  slug: selectparameter
- name: SetDelegateParametersOperation
  property_count: 0
  slug: setdelegateparametersoperation
- name: SetDepositsLimitOperation
  property_count: 0
  slug: setdepositslimitoperation
- name: SmartRollup
  property_count: 0
  slug: smartrollup
- name: SmartRollupAddMessagesOperation
  property_count: 0
  slug: smartrollupaddmessagesoperation
- name: SmartRollupCementOperation
  property_count: 0
  slug: smartrollupcementoperation
- name: SmartRollupExecuteOperation
  property_count: 0
  slug: smartrollupexecuteoperation
- name: SmartRollupOriginateOperation
  property_count: 0
  slug: smartrolluporiginateoperation
- name: SmartRollupParameter
  property_count: 4
  slug: smartrollupparameter
- name: SmartRollupPublishOperation
  property_count: 0
  slug: smartrolluppublishoperation
- name: SmartRollupRecoverBondOperation
  property_count: 0
  slug: smartrolluprecoverbondoperation
- name: SmartRollupRefuteOperation
  property_count: 0
  slug: smartrolluprefuteoperation
- name: Software
  property_count: 7
  slug: software
- name: SoftwareAlias
  property_count: 2
  slug: softwarealias
- name: SortMode
  property_count: 0
  slug: sortmode
- name: SortParameter
  property_count: 2
  slug: sortparameter
- name: SourceOperation
  property_count: 5
  slug: sourceoperation
- name: SplitActualStaker
  property_count: 4
  slug: splitactualstaker
- name: SplitDelegator
  property_count: 3
  slug: splitdelegator
- name: SplitMember
  property_count: 5
  slug: splitmember
- name: SplitStaker
  property_count: 3
  slug: splitstaker
- name: SrBondStatusParameter
  property_count: 4
  slug: srbondstatusparameter
- name: Src1HashParameter
  property_count: 4
  slug: src1hashparameter
- name: SrCommitment
  property_count: 16
  slug: srcommitment
- name: SrCommitmentInfo
  property_count: 8
  slug: srcommitmentinfo
- name: SrCommitmentStatusParameter
  property_count: 4
  slug: srcommitmentstatusparameter
- name: SrGame
  property_count: 15
  slug: srgame
- name: SrGameInfo
  property_count: 9
  slug: srgameinfo
- name: SrGameMove
  property_count: 6
  slug: srgamemove
- name: SrMessage
  property_count: 14
  slug: srmessage
- name: SrMessageTypeParameter
  property_count: 4
  slug: srmessagetypeparameter
- name: SrStaker
  property_count: 0
  slug: srstaker
- name: StakerRewards
  property_count: 10
  slug: stakerrewards
- name: StakingActionParameter
  property_count: 4
  slug: stakingactionparameter
- name: StakingOperation
  property_count: 0
  slug: stakingoperation
- name: StakingUpdate
  property_count: 17
  slug: stakingupdate
- name: StakingUpdateTypeParameter
  property_count: 4
  slug: stakingupdatetypeparameter
- name: State
  property_count: 22
  slug: state
- name: Statistics
  property_count: 26
  slug: statistics
- name: StorageRecord
  property_count: 5
  slug: storagerecord
- name: StringParameter
  property_count: 7
  slug: stringparameter
- name: Symbols
  property_count: 0
  slug: symbols
- name: Ticket
  property_count: 18
  slug: ticket
- name: TicketBalance
  property_count: 9
  slug: ticketbalance
- name: TicketBalanceShort
  property_count: 4
  slug: ticketbalanceshort
- name: TicketInfo
  property_count: 8
  slug: ticketinfo
- name: TicketInfoShort
  property_count: 7
  slug: ticketinfoshort
- name: TicketTransfer
  property_count: 10
  slug: tickettransfer
- name: TicketTransferActivity
  property_count: 0
  slug: tickettransferactivity
- name: TimestampParameter
  property_count: 8
  slug: timestampparameter
- name: Token
  property_count: 16
  slug: token
- name: TokenBalance
  property_count: 10
  slug: tokenbalance
- name: TokenBalanceShort
  property_count: 3
  slug: tokenbalanceshort
- name: TokenGlobalIdParameter
  property_count: 2
  slug: tokenglobalidparameter
- name: TokenInfo
  property_count: 6
  slug: tokeninfo
- name: TokenInfoShort
  property_count: 5
  slug: tokeninfoshort
- name: TokenStandardParameter
  property_count: 2
  slug: tokenstandardparameter
- name: TokenTransfer
  property_count: 10
  slug: tokentransfer
- name: TokenTransferActivity
  property_count: 0
  slug: tokentransferactivity
- name: TransactionOperation
  property_count: 0
  slug: transactionoperation
- name: TransferTicketOperation
  property_count: 0
  slug: transferticketoperation
- name: TxParameter
  property_count: 2
  slug: txparameter
- name: TxRollupCommitOperation
  property_count: 0
  slug: txrollupcommitoperation
- name: TxRollupDispatchTicketsOperation
  property_count: 0
  slug: txrollupdispatchticketsoperation
- name: TxRollupFinalizeCommitmentOperation
  property_count: 0
  slug: txrollupfinalizecommitmentoperation
- name: TxRollupOriginationOperation
  property_count: 0
  slug: txrolluporiginationoperation
- name: TxRollupRejectionOperation
  property_count: 0
  slug: txrolluprejectionoperation
- name: TxRollupRemoveCommitmentOperation
  property_count: 0
  slug: txrollupremovecommitmentoperation
- name: TxRollupReturnBondOperation
  property_count: 0
  slug: txrollupreturnbondoperation
- name: TxRollupSubmitBatchOperation
  property_count: 0
  slug: txrollupsubmitbatchoperation
- name: UnregisteredDelegateError
  property_count: 0
  slug: unregistereddelegateerror
- name: UnstakeRequest
  property_count: 19
  slug: unstakerequest
- name: UnstakeRequestStatusParameter
  property_count: 2
  slug: unstakerequeststatusparameter
- name: UpdateSecondaryKeyOperation
  property_count: 0
  slug: updatesecondarykeyoperation
- name: User
  property_count: 0
  slug: user
- name: ValueTupleOfStringAndListOfInteger
  property_count: 0
  slug: valuetupleofstringandlistofinteger
- name: VdfRevelationOperation
  property_count: 0
  slug: vdfrevelationoperation
- name: VoteParameter
  property_count: 4
  slug: voteparameter
- name: VoterSnapshot
  property_count: 3
  slug: votersnapshot
- name: VoterStatusParameter
  property_count: 4
  slug: voterstatusparameter
- name: VotingEpoch
  property_count: 8
  slug: votingepoch
- name: VotingPeriod
  property_count: 23
  slug: votingperiod
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 17
  name: context Context
  property_count: 2
  slug: context
layout: provider
modified: '2026-06-13'
name: Tezos
nav: Providers
network: true
overview: 'Tezos publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, BigMaps API, Blocks API, and 21 more. Tagged areas include Tezos, Blockchain, TzKT, Baking Bad, and Cryptocurrency.


  The Tezos catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Tezos'' developer surface includes documentation, status page, engineering blog, and 13 more developer resources.'
plans:
- name: Tezos Plans Pricing
  plan_count: 3
  slug: tezos-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Tezos Rate Limits
  slug: tezos-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tezos API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tezos-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 55.4
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tezos/refs/heads/main/screenshots/tezos-2026-06-20T195210.png
security:
- kind: domain-security
  name: Tezos Domain Security
  slug: tezos-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tezos
tags:
- Tezos
- Blockchain
- TzKT
- Baking Bad
- Cryptocurrency
- Smart Contracts
- NFT
- Tokens
- Delegations
- Staking
- Governance
- FA1.2
- FA2
- WebSocket
website: https://tzkt.io
---

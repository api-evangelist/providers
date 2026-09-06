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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Wormhole Agentic Access
  operation_count: 74
  slug: wormhole-agentic-access
  summary_line: 74 operations · 2 acting
api_count: 1
apis:
- description: Testnet version of the Wormholescan REST API for development and testing against Wormhole-supported test networks. Mirrors the mainnet API surface for VAAs, operations, and token transfers in a non-pr
  name: Wormholescan Testnet API
  slug: wormholescan-testnet-api
- description: Unified TypeScript SDK for building cross-chain applications on Wormhole. Supports Native Token Transfers, Wrapped Token Transfers, CCTP, Settlement, and core messaging/VAA handling across EVM chains,
  name: Wormhole TypeScript SDK
  slug: wormhole-typescript-sdk
- description: Embeddable React widget that provides a full cross-chain token transfer UI powered by Wormhole. Supports 45+ chains and integrates Native Token Transfers, Wrapped Token Transfers, CCTP, and Settlement
  name: Wormhole Connect Widget
  slug: wormhole-connect-widget
- description: Command-line interface for interacting with Wormhole protocol operations including token transfers, NTT deployments, and cross-chain messaging tasks.
  name: Wormhole CLI
  slug: wormhole-cli
- baseURL: https://api.wormholescan.io/api/v1
  baseurl_source: declared
  description: The Guardian API from Wormhole — 8 operation(s) for guardian.
  name: Wormhole Guardian API
  slug: wormhole-guardian-api
- baseURL: https://api.wormholescan.io/api/v1
  baseurl_source: declared
  description: The wormhole API from Wormhole — 1 operation(s) for wormhole.
  name: Wormhole wormhole API
  slug: wormhole-wormhole-api
- baseURL: https://api.wormholescan.io/api/v1
  baseurl_source: declared
  description: The wormholescan API from Wormhole — 64 operation(s) for wormholescan.
  name: Wormhole wormholescan API
  slug: wormhole-wormholescan-api
artifact_total: 204
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wormholescan Guardian API
  slug: open-wormhole-guardian-api
- collection_type: open
  name: Wormholescan Guardian wormhole API
  slug: open-wormhole-wormhole-api
- collection_type: open
  name: Guardian wormholescan API
  slug: open-wormhole-wormholescan-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wormhole-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wormhole-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://wormhole.com/docs/
- group: build
  title: ''
  type: github
  url: https://github.com/wormhole-foundation
- group: other
  title: ''
  type: explorer
  url: https://wormholescan.io/
- group: company
  title: ''
  type: Blog
  url: https://wormhole.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://wormhole.com/contact
- group: operate
  title: ''
  type: Community
  url: https://wormhole.com/community/hub
- group: operate
  title: ''
  type: Forums
  url: https://forum.wormhole.com/
- group: auth
  title: ''
  type: Security
  url: https://immunefi.com/bug-bounty/wormhole/
- group: operate
  title: ''
  type: status
  url: https://wormholescan.io/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/wormhole
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/wormholecrypto
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wormhole.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wormhole.com/privacy
description: Wormhole is a decentralized cross-chain messaging and interoperability protocol connecting 45+ blockchain networks. It provides REST APIs for querying VAA (Verifiable Action Approval) status, native and wrapped token transfers, cross-chain operations, and Guardian Network data via the Wormholescan API. Developers can build multichain applications with the TypeScript SDK, CLI tooling, and the Connect bridging widget.
examples:
- key_count: 7
  name: Api V1 Native Token Transfer Activity
  slug: api-v1-native-token-transfer-activity
- key_count: 7
  name: Api V1 Native Token Transfer Summary
  slug: api-v1-native-token-transfer-summary
- key_count: 7
  name: Api V1 Native Token Transfer Token List
  slug: api-v1-native-token-transfer-token-list
- key_count: 7
  name: Api V1 Native Token Transfer Top Address
  slug: api-v1-native-token-transfer-top-address
- key_count: 7
  name: Api V1 Native Token Transfer Top Holder
  slug: api-v1-native-token-transfer-top-holder
- key_count: 7
  name: Api V1 Native Token Transfer Transfer By Time
  slug: api-v1-native-token-transfer-transfer-by-time
- key_count: 7
  name: Api V1 Top 100 Corridors
  slug: api-v1-top-100-corridors
- key_count: 7
  name: Application Activity
  slug: application-activity
- key_count: 7
  name: Circulating Supply
  slug: circulating-supply
- key_count: 7
  name: Find Address By Id
  slug: find-address-by-id
- key_count: 7
  name: Find All Vaas
  slug: find-all-vaas
- key_count: 7
  name: Find Delegate Observations By Chain
  slug: find-delegate-observations-by-chain
- key_count: 7
  name: Find Delegate Observations By Emitter
  slug: find-delegate-observations-by-emitter
- key_count: 7
  name: Find Delegate Observations By Guardian
  slug: find-delegate-observations-by-guardian
- key_count: 7
  name: Find Delegate Observations By Sequence
  slug: find-delegate-observations-by-sequence
- key_count: 7
  name: Find Duplicated Vaa By Id
  slug: find-duplicated-vaa-by-id
- key_count: 7
  name: Find Global Transaction By Id
  slug: find-global-transaction-by-id
- key_count: 7
  name: Find Observations By Chain
  slug: find-observations-by-chain
- key_count: 7
  name: Find Observations By Emitter
  slug: find-observations-by-emitter
- key_count: 7
  name: Find Observations By Id
  slug: find-observations-by-id
- key_count: 7
  name: Find Observations By Sequence
  slug: find-observations-by-sequence
- key_count: 7
  name: Find Observations
  slug: find-observations
- key_count: 7
  name: Find Relay By Vaa Id
  slug: find-relay-by-vaa-id
- key_count: 7
  name: Find Vaa By Id
  slug: find-vaa-by-id
- key_count: 7
  name: Find Vaas By Chain
  slug: find-vaas-by-chain
- key_count: 7
  name: Find Vaas By Emitter
  slug: find-vaas-by-emitter
- key_count: 7
  name: Get Guardian Set
  slug: get-guardian-set
- key_count: 7
  name: Get Last Transactions
  slug: get-last-transactions
- key_count: 7
  name: Get Operation By Id
  slug: get-operation-by-id
- key_count: 7
  name: Get Operations
  slug: get-operations
- key_count: 7
  name: Get Protocol Network Pairs
  slug: get-protocol-network-pairs
- key_count: 7
  name: Get Protocol Trending Tokens
  slug: get-protocol-trending-tokens
- key_count: 7
  name: Get Scorecards
  slug: get-scorecards
- key_count: 7
  name: Get Secured Tokens
  slug: get-secured-tokens
- key_count: 7
  name: Get Token By Chain And Address
  slug: get-token-by-chain-and-address
- key_count: 7
  name: Get Top Assets By Volume
  slug: get-top-assets-by-volume
- key_count: 7
  name: Get Top Chain Pairs By Num Transfers
  slug: get-top-chain-pairs-by-num-transfers
- key_count: 7
  name: Get Top Protocols Stats
  slug: get-top-protocols-stats
- key_count: 7
  name: Get Transaction By Id
  slug: get-transaction-by-id
- key_count: 7
  name: Get Vaa Counts
  slug: get-vaa-counts
- key_count: 7
  name: Get Version
  slug: get-version
- key_count: 7
  name: Governor Available Notional By Chain
  slug: governor-available-notional-by-chain
- key_count: 7
  name: Governor Config By Guardian Address
  slug: governor-config-by-guardian-address
- key_count: 7
  name: Governor Config
  slug: governor-config
- key_count: 7
  name: Governor Enqueued Vaas
  slug: governor-enqueued-vaas
- key_count: 7
  name: Governor Max Notional Available By Chain
  slug: governor-max-notional-available-by-chain
- key_count: 7
  name: Governor Notional Available By Chain
  slug: governor-notional-available-by-chain
- key_count: 7
  name: Governor Notional Available
  slug: governor-notional-available
- key_count: 7
  name: Governor Notional Limit Detail By Chain
  slug: governor-notional-limit-detail-by-chain
- key_count: 7
  name: Governor Notional Limit Detail
  slug: governor-notional-limit-detail
- key_count: 7
  name: Governor Notional Limit
  slug: governor-notional-limit
- key_count: 7
  name: Governor Status By Guardian Address
  slug: governor-status-by-guardian-address
- key_count: 7
  name: Governor Status
  slug: governor-status
- key_count: 7
  name: Governor Vaas
  slug: governor-vaas
- key_count: 7
  name: Guardian Set
  slug: guardian-set
- key_count: 7
  name: Guardians Enqueued Vaas By Chain
  slug: guardians-enqueued-vaas-by-chain
- key_count: 7
  name: Guardians Enqueued Vaas
  slug: guardians-enqueued-vaas
- key_count: 7
  name: Guardians Find Signed Batch Vaa
  slug: guardians-find-signed-batch-vaa
- key_count: 7
  name: Guardians Find Signed Vaa
  slug: guardians-find-signed-vaa
- key_count: 7
  name: Guardians Hearbeats
  slug: guardians-hearbeats
- key_count: 7
  name: Guardians Is Vaa Enqueued
  slug: guardians-is-vaa-enqueued
- key_count: 7
  name: Guardians Token List
  slug: guardians-token-list
- key_count: 7
  name: Health Check
  slug: health-check
- key_count: 7
  name: List Transactions
  slug: list-transactions
- key_count: 7
  name: Live Tracking Subscribe
  slug: live-tracking-subscribe
- key_count: 7
  name: Parse Vaa
  slug: parse-vaa
- key_count: 7
  name: Ready Check
  slug: ready-check
- key_count: 7
  name: Search Operations
  slug: search-operations
- key_count: 7
  name: Supply Info
  slug: supply-info
- key_count: 7
  name: Swagger
  slug: swagger
- key_count: 7
  name: Top Symbols By Volume
  slug: top-symbols-by-volume
- key_count: 7
  name: Total Supply
  slug: total-supply
- key_count: 7
  name: X Chain Activity Tops
  slug: x-chain-activity-tops
- key_count: 7
  name: X Chain Activity
  slug: x-chain-activity
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://wormhole.com/logo.png
json_schemas:
- name: address.AddressOverview
  property_count: 1
  slug: address-addressoverview
- name: github_com_wormhole-foundation_wormhole-explorer_api_routes_wormscan_operations.BalanceChanges
  property_count: 3
  slug: balancechanges
- name: delegate_observations.DelegateObservationDoc
  property_count: 18
  slug: delegate-observations-delegateobservationdoc
- name: governor.AvailableNotionalItemResponse
  property_count: 4
  slug: governor-availablenotionalitemresponse
- name: governor.AvailableNotionalResponse
  property_count: 1
  slug: governor-availablenotionalresponse
- name: governor.Emitter
  property_count: 3
  slug: governor-emitter
- name: governor.EnqueuedVaa
  property_count: 5
  slug: governor-enqueuedvaa
- name: governor.EnqueuedVaaDetail
  property_count: 6
  slug: governor-enqueuedvaadetail
- name: governor.EnqueuedVaaItemResponse
  property_count: 6
  slug: governor-enqueuedvaaitemresponse
- name: governor.EnqueuedVaaResponse
  property_count: 1
  slug: governor-enqueuedvaaresponse
- name: governor.EnqueuedVaas
  property_count: 2
  slug: governor-enqueuedvaas
- name: governor.GovConfig
  property_count: 7
  slug: governor-govconfig
- name: governor.GovConfigChains
  property_count: 3
  slug: governor-govconfigchains
- name: governor.GovConfigfTokens
  property_count: 3
  slug: governor-govconfigftokens
- name: governor.GovernorLimit
  property_count: 4
  slug: governor-governorlimit
- name: governor.GovernorVaasResponse
  property_count: 8
  slug: governor-governorvaasresponse
- name: governor.GovStatus
  property_count: 5
  slug: governor-govstatus
- name: governor.GovStatusChainEmitter
  property_count: 3
  slug: governor-govstatuschainemitter
- name: governor.GovStatusChains
  property_count: 3
  slug: governor-govstatuschains
- name: governor.MaxNotionalAvailableRecord
  property_count: 7
  slug: governor-maxnotionalavailablerecord
- name: governor.NotionalAvailable
  property_count: 2
  slug: governor-notionalavailable
- name: governor.NotionalAvailableDetail
  property_count: 6
  slug: governor-notionalavailabledetail
- name: governor.NotionalLimitDetail
  property_count: 7
  slug: governor-notionallimitdetail
- name: governor.TokenList
  property_count: 3
  slug: governor-tokenlist
- name: guardian.GuardianSetResponse
  property_count: 1
  slug: guardian-guardiansetresponse
- name: guardian_sets.GuardianAddress
  property_count: 2
  slug: guardian-sets-guardianaddress
- name: guardian_sets.GuardianSetDoc
  property_count: 2
  slug: guardian-sets-guardiansetdoc
- name: github_com_wormhole-foundation_wormhole-explorer_api_routes_guardian_guardian.GuardianSet
  property_count: 2
  slug: guardianset
- name: heartbeats.HeartbeatNetworkResponse
  property_count: 4
  slug: heartbeats-heartbeatnetworkresponse
- name: heartbeats.HeartbeatResponse
  property_count: 3
  slug: heartbeats-heartbeatresponse
- name: heartbeats.HeartbeatsResponse
  property_count: 1
  slug: heartbeats-heartbeatsresponse
- name: heartbeats.RawHeartbeat
  property_count: 8
  slug: heartbeats-rawheartbeat
- name: infrastructure.VersionResponse
  property_count: 3
  slug: infrastructure-versionresponse
- name: observations.ObservationDoc
  property_count: 10
  slug: observations-observationdoc
- name: operations.Content
  property_count: 3
  slug: operations-content
- name: operations.Data
  property_count: 2
  slug: operations-data
- name: operations.EmitterAddress
  property_count: 2
  slug: operations-emitteraddress
- name: operations.OperationResponse
  property_count: 9
  slug: operations-operationresponse
- name: operations.SourceChain
  property_count: 11
  slug: operations-sourcechain
- name: operations.StandardizedProperties
  property_count: 12
  slug: operations-standardizedproperties
- name: operations.TargetChain
  property_count: 10
  slug: operations-targetchain
- name: operations.Transaction
  property_count: 2
  slug: operations-transaction
- name: operations.Vaa
  property_count: 3
  slug: operations-vaa
- name: parser.ParseVaaWithStandarizedPropertiesdResponse
  property_count: 2
  slug: parser-parsevaawithstandarizedpropertiesdresponse
- name: parser.StandardizedProperties
  property_count: 12
  slug: parser-standardizedproperties
- name: protocols.ProtocolNetworkPairResponse
  property_count: 2
  slug: protocols-protocolnetworkpairresponse
- name: protocols.ProtocolNetworkPairResult
  property_count: 3
  slug: protocols-protocolnetworkpairresult
- name: protocols.ProtocolNetworkPairVolume
  property_count: 3
  slug: protocols-protocolnetworkpairvolume
- name: protocols.ProtocolTotalValuesDTO
  property_count: 10
  slug: protocols-protocoltotalvaluesdto
- name: protocols.ProtocolTrendingToken
  property_count: 7
  slug: protocols-protocoltrendingtoken
- name: protocols.ProtocolTrendingTokensResponse
  property_count: 2
  slug: protocols-protocoltrendingtokensresponse
- name: protocols.ProtocolTrendingTokensResult
  property_count: 3
  slug: protocols-protocoltrendingtokensresult
- name: relays.DeliveryReponse
  property_count: 5
  slug: relays-deliveryreponse
- name: relays.InstructionsResponse
  property_count: 11
  slug: relays-instructionsresponse
- name: relays.RelayDataResponse
  property_count: 5
  slug: relays-relaydataresponse
- name: relays.RelayResponse
  property_count: 7
  slug: relays-relayresponse
- name: relays.ResultExecutionResponse
  property_count: 6
  slug: relays-resultexecutionresponse
- name: response.APIError
  property_count: 3
  slug: response-apierror
- name: response.ErrorDetail
  property_count: 2
  slug: response-errordetail
- name: response.Response-address_AddressOverview
  property_count: 2
  slug: response-response-address-addressoverview
- name: response.Response-array_governor_EnqueuedVaaDetail
  property_count: 2
  slug: response-response-array-governor-enqueuedvaadetail
- name: response.Response-array_governor_EnqueuedVaas
  property_count: 2
  slug: response-response-array-governor-enqueuedvaas
- name: response.Response-array_governor_GovernorLimit
  property_count: 2
  slug: response-response-array-governor-governorlimit
- name: response.Response-array_governor_GovernorVaasResponse
  property_count: 2
  slug: response-response-array-governor-governorvaasresponse
- name: response.Response-array_governor_GovStatus
  property_count: 2
  slug: response-response-array-governor-govstatus
- name: response.Response-array_governor_NotionalAvailable
  property_count: 2
  slug: response-response-array-governor-notionalavailable
- name: response.Response-array_governor_NotionalAvailableDetail
  property_count: 2
  slug: response-response-array-governor-notionalavailabledetail
- name: response.Response-array_governor_NotionalLimitDetail
  property_count: 2
  slug: response-response-array-governor-notionallimitdetail
- name: response.Response-array_vaa_VaaDoc
  property_count: 2
  slug: response-response-array-vaa-vaadoc
- name: response.Response-array_vaa_VaaStats
  property_count: 2
  slug: response-response-array-vaa-vaastats
- name: response.Response-governor_GovConfig
  property_count: 2
  slug: response-response-governor-govconfig
- name: response.Response-governor_GovStatus
  property_count: 2
  slug: response-response-governor-govstatus
- name: response.Response-governor_MaxNotionalAvailableRecord
  property_count: 2
  slug: response-response-governor-maxnotionalavailablerecord
- name: response.Response-guardian_sets_GuardianSetDoc
  property_count: 2
  slug: response-response-guardian-sets-guardiansetdoc
- name: response.ResponsePagination
  property_count: 1
  slug: response-responsepagination
- name: stats.image
  property_count: 3
  slug: stats-image
- name: stats.NativeTokenTransferActivity
  property_count: 4
  slug: stats-nativetokentransferactivity
- name: stats.NativeTokenTransferByTime
  property_count: 3
  slug: stats-nativetokentransferbytime
- name: stats.NativeTokenTransferSummary
  property_count: 11
  slug: stats-nativetokentransfersummary
- name: stats.NativeTokenTransferTopAddress
  property_count: 2
  slug: stats-nativetokentransfertopaddress
- name: stats.NativeTokenTransferTopHolder
  property_count: 3
  slug: stats-nativetokentransfertopholder
- name: stats.Token
  property_count: 21
  slug: stats-token
- name: stats.TokenInfoDTO
  property_count: 18
  slug: stats-tokeninfodto
- name: stats.TokenResult
  property_count: 5
  slug: stats-tokenresult
- name: stats.TokenType
  property_count: 0
  slug: stats-tokentype
- name: stats.TopCorridor
  property_count: 5
  slug: stats-topcorridor
- name: stats.TopCorridorsResult
  property_count: 1
  slug: stats-topcorridorsresult
- name: stats.TopSymbolByVolumeResult
  property_count: 1
  slug: stats-topsymbolbyvolumeresult
- name: stats.TopSymbolResult
  property_count: 4
  slug: stats-topsymbolresult
- name: supply.SupplyInfoResponse
  property_count: 2
  slug: supply-supplyinforesponse
- name: transactions.AssetWithVolume
  property_count: 5
  slug: transactions-assetwithvolume
- name: transactions.AttributeDoc
  property_count: 2
  slug: transactions-attributedoc
- name: transactions.ChainActivity
  property_count: 1
  slug: transactions-chainactivity
- name: transactions.ChainActivityTopResult
  property_count: 6
  slug: transactions-chainactivitytopresult
- name: transactions.ChainPair
  property_count: 3
  slug: transactions-chainpair
- name: transactions.Destination
  property_count: 3
  slug: transactions-destination
- name: transactions.DestinationTx
  property_count: 9
  slug: transactions-destinationtx
- name: transactions.GlobalTransactionDoc
  property_count: 3
  slug: transactions-globaltransactiondoc
- name: transactions.ListTransactionsResponse
  property_count: 1
  slug: transactions-listtransactionsresponse
- name: transactions.OriginTx
  property_count: 4
  slug: transactions-origintx
- name: transactions.ScorecardsResponse
  property_count: 14
  slug: transactions-scorecardsresponse
- name: transactions.Token
  property_count: 3
  slug: transactions-token
- name: transactions.TopAssetsResponse
  property_count: 1
  slug: transactions-topassetsresponse
- name: transactions.TopChainPairsResponse
  property_count: 1
  slug: transactions-topchainpairsresponse
- name: transactions.TransactionCountResult
  property_count: 2
  slug: transactions-transactioncountresult
- name: transactions.TransactionDetail
  property_count: 12
  slug: transactions-transactiondetail
- name: transactions.Tx
  property_count: 4
  slug: transactions-tx
- name: vaa.ChainID
  property_count: 0
  slug: vaa-chainid
- name: vaa.VaaDoc
  property_count: 15
  slug: vaa-vaadoc
- name: vaa.VaaStats
  property_count: 2
  slug: vaa-vaastats
- name: workflow.Event
  property_count: 8
  slug: workflow-event
- name: workflow.EventStatus
  property_count: 0
  slug: workflow-eventstatus
- name: workflow.EventType
  property_count: 0
  slug: workflow-eventtype
layout: provider
modified: '2026-06-13'
name: Wormhole
nav: Providers
network: true
overview: 'Wormhole publishes 3 APIs on the [APIs.io](https://apis.io/) network: Guardian API, wormhole API, and wormholescan API. Tagged areas include Cross-Chain, Blockchain, Interoperability, DeFi, and Token Transfers.


  The Wormhole catalog on APIs.io includes 1 Spectral governance ruleset.


  Wormhole''s developer surface includes developer portal, GitHub presence, engineering blog, status page, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 16
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wormhole API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wormhole-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 45.4
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wormhole/refs/heads/main/screenshots/wormhole-2026-06-20T201625.png
security:
- kind: domain-security
  name: Wormhole Domain Security
  slug: wormhole-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wormhole
tags:
- Cross-Chain
- Blockchain
- Interoperability
- DeFi
- Token Transfers
- Messaging
- Web3
website: https://wormhole.com/docs/
---

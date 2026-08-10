---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 45
  human_in_the_loop: 2
  name: Stellar Agentic Access
  operation_count: 127
  slug: stellar-agentic-access
  summary_line: 127 operations · 45 acting · 2 human-in-the-loop
api_count: 33
apis:
- description: The Stellar RPC API (formerly Soroban RPC) is a JSON-RPC interface for interacting with Soroban smart contracts deployed on the Stellar network. It supports simulating and submitting contract invocati
  name: Stellar RPC API
  slug: stellar-rpc-api
- description: Users interact with the Stellar network through accounts. Everything else in the ledger—assets, offers, trustlines, etc. are owned by accounts, and accounts must authorize all changes to the ledger th
  name: Stellar Accounts API
  slug: stellar-accounts-api
- description: The Admin API oversees the management of tenants within the system, facilitating tasks such as provisioning new tenants, updating their information, and retrieving tenant data.
  name: Stellar Admin API
  slug: stellar-admin-api
- description: API Keys functionality allows to create access key with granular permissions and resource management.
  name: Stellar API Keys API
  slug: stellar-api-keys-api
- description: Assets are representations of value issued on the Stellar network. An asset consists of a type, code, and issuer.
  name: Stellar Assets API
  slug: stellar-assets-api
- description: Authentication controls the log in/log out process for all SDP users, as well as the token refresh process. Authentication uses a JWT approach signed with an ES256 private key.
  name: Stellar Authentication API
  slug: stellar-authentication-api
- description: Endpoints related to balances. A balance is an amount of a particular asset held by an organization, tenant, or account.
  name: Stellar Balances API
  slug: stellar-balances-api
- description: Bridge integration endpoints for connecting organizations with Bridge services. **Integration Flow:** 1. Organization opts into Bridge (OPTED_IN status) 2. Complete KYC verification process via Bridge
  name: Stellar Bridge Integration API
  slug: stellar-bridge-integration-api
- description: A Claimable Balance represents the transfer of ownership of some amount of an asset. Claimable balances provide a mechanism for setting up a payment which can be claimed in the future. This allows you
  name: Stellar Claimable Balances API
  slug: stellar-claimable-balances-api
- description: '[SEP-12](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0012.md) requests made from client applications.'
  name: Stellar Customers API
  slug: stellar-customers-api
- description: Endpoints related to disbursements. A disbursement is a group of payments sent to multiple individuals at once. An SDP user with the appropriate role triggers a new disbursement through the SDP dashbo
  name: Stellar Disbursements API
  slug: stellar-disbursements-api
- description: Effects represent specific changes that occur in the ledger as a result of successful operations, but are not necessarily directly reflected in the ledger or history, as transactions and operations ar
  name: Stellar Effects API
  slug: stellar-effects-api
- description: The Events API from Stellar — 1 operation(s) for events.
  name: Stellar Events API
  slug: stellar-events-api
- description: The Exports API from Stellar — 3 operation(s) for exports.
  name: Stellar Exports API
  slug: stellar-exports-api
- description: Fee stats are used to predict what fee to set for a transaction before submitting it to the network.
  name: Stellar Fee Stats API
  slug: stellar-fee-stats-api
- description: Each ledger stores the state of the network at a point in time and contains all the changes - transactions, operations, effects, etc. - to that state.
  name: Stellar Ledgers API
  slug: stellar-ledgers-api
- description: Liquidity Pools provide a simple, non-interactive way to trade large amounts of capital and enable high volumes of trading.
  name: Stellar Liquidity Pools API
  slug: stellar-liquidity-pools-api
- description: Offers are statements about how much of an asset an account wants to buy or sell.
  name: Stellar Offers API
  slug: stellar-offers-api
- description: 'Operations are objects that represent a desired change to the ledger: payments, offers to exchange currency, changes made to account options, etc. Operations are submitted to the Stellar network group'
  name: Stellar Operations API
  slug: stellar-operations-api
- description: An order book is a collections of offers for a specific pair of assets.
  name: Stellar Order Books API
  slug: stellar-order-books-api
- description: Organization endpoints manage the process of getting and updating organizational profile information. The organization's profile has basic information set at the time of SDP deployment. It can be modi
  name: Stellar Organization API
  slug: stellar-organization-api
- description: Paths provide information about potential path payments. A path can be used to populate the necessary fields for a path payment operation.
  name: Stellar Paths API
  slug: stellar-paths-api
- description: Endpoints related to payments. An SDP payment is an individual payment from an organization to a receiver. Each payment is part of a disbursement and occurs on the Stellar network. Granular payment st
  name: Stellar Payments API
  slug: stellar-payments-api
- description: Profiles endpoints manage the process of getting and updating individual profile information. Profile information is set when the account is created and can be updated by the user on the SDP dashboard
  name: Stellar Profile API
  slug: stellar-profile-api
- description: Requests containing data that can be used to provide exchange rates between on & off-chain assets.
  name: Stellar Rates API
  slug: stellar-rates-api
- description: Endpoints related to receivers. A receiver is an individual receiving a payment in a disbursement. The receiver is tracked by phone number to reduce the need for personally identifiable information. E
  name: Stellar Receivers API
  slug: stellar-receivers-api
- description: The registration endpoints guide the process for a receiver to verify their identity and link their wallet address to an SDP. The registration process only needs to happen once per receiver to link th
  name: Stellar Registration API
  slug: stellar-registration-api
- description: Statistics endpoints return general aggregated data per organization, as well as disbursement-specific metrics. SDP users can use this data to monitor their disbursements over time.
  name: Stellar Statistics API
  slug: stellar-statistics-api
- description: A trade aggregation represents aggregated statistics on an asset pair (base and counter) for a specific time period. Trade aggregations are useful to developers of trading clients and provide historic
  name: Stellar Trade Aggregations API
  slug: stellar-trade-aggregations-api
- description: When an offer is fully or partially fulfilled, a trade happens. Trades can also be caused by successful path payments, because path payments involve fulfilling offers. A trade occurs between two parti
  name: Stellar Trades API
  slug: stellar-trades-api
- description: Transactions initiated by client applications via SEP APIs
  name: Stellar Transactions API
  slug: stellar-transactions-api
- description: The users endpoints facilitate the creation of new SDP users - including setting the appropriate role, sending an email invitation, and activating a user - and managing roles.
  name: Stellar Users API
  slug: stellar-users-api
- description: The Wallets API from Stellar — 2 operation(s) for wallets.
  name: Stellar Wallets API
  slug: stellar-wallets-api
artifact_total: 215
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stellar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stellar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stellar-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.stellar.org/docs
- group: company
  title: ''
  type: Blog
  url: https://stellar.org/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stellar.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stellar
- group: build
  title: ''
  type: SDKs
  url: https://developers.stellar.org/docs/tools/sdks/client-sdks
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/stellar/js-stellar-sdk
- group: build
  title: ''
  type: GoSDK
  url: https://github.com/stellar/go-stellar-sdk
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/StellarCN/py-stellar-base
- group: build
  title: ''
  type: iOSSDK
  url: https://github.com/Soneso/stellar-ios-mac-sdk
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/stellardev
- group: company
  title: ''
  type: About
  url: https://stellar.org/foundation
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/stellar-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stellar-vocabulary.yml
created: '2026-06-14'
description: Stellar is an open-source, decentralized blockchain network designed for fast, low-cost cross-border payments and asset issuance. The Stellar Development Foundation (SDF) maintains the core protocol and the Horizon REST API, which provides HTTP access to ledger data including accounts, transactions, operations, effects, offers, trades, claimable balances, and liquidity pools. Horizon is the primary data gateway for the Stellar network, re-serving ledger data in a developer-friendly format. The network supports native XLM transfers, custom asset issuance, a built-in decentralized exchange (DEX), Soroban smart contracts, and anchor integrations for fiat on/off-ramps. Authentication is not required for read queries; transaction submission requires signing with a Stellar keypair.
examples:
- key_count: 5
  name: Stellar Horizon Cbretrieverelatedoperations 200
  slug: stellar-horizon-cbretrieverelatedoperations-200
- key_count: 5
  name: Stellar Horizon Cbretrieverelatedtransactions 200
  slug: stellar-horizon-cbretrieverelatedtransactions-200
- key_count: 5
  name: Stellar Horizon Getalloffers 200
  slug: stellar-horizon-getalloffers-200
- key_count: 5
  name: Stellar Horizon Getalltrades 200
  slug: stellar-horizon-getalltrades-200
- key_count: 5
  name: Stellar Horizon Getdatabyaccountid 200
  slug: stellar-horizon-getdatabyaccountid-200
- key_count: 5
  name: Stellar Horizon Geteffectsbyaccountid 200
  slug: stellar-horizon-geteffectsbyaccountid-200
- key_count: 5
  name: Stellar Horizon Getofferbyofferid 200
  slug: stellar-horizon-getofferbyofferid-200
- key_count: 5
  name: Stellar Horizon Getoffersbyaccountid 200
  slug: stellar-horizon-getoffersbyaccountid-200
- key_count: 5
  name: Stellar Horizon Getoperationsbyaccountid 200
  slug: stellar-horizon-getoperationsbyaccountid-200
- key_count: 5
  name: Stellar Horizon Getpaymentsbyaccountid 200
  slug: stellar-horizon-getpaymentsbyaccountid-200
- key_count: 5
  name: Stellar Horizon Gettradesbyaccountid 200
  slug: stellar-horizon-gettradesbyaccountid-200
- key_count: 5
  name: Stellar Horizon Gettradesbyofferid 200
  slug: stellar-horizon-gettradesbyofferid-200
- key_count: 5
  name: Stellar Horizon Gettransactionsbyaccountid 200
  slug: stellar-horizon-gettransactionsbyaccountid-200
- key_count: 5
  name: Stellar Horizon Listallaccounts 200
  slug: stellar-horizon-listallaccounts-200
- key_count: 5
  name: Stellar Horizon Listallassets 200
  slug: stellar-horizon-listallassets-200
- key_count: 5
  name: Stellar Horizon Listallclaimablebalances 200
  slug: stellar-horizon-listallclaimablebalances-200
- key_count: 5
  name: Stellar Horizon Listalleffects 200
  slug: stellar-horizon-listalleffects-200
- key_count: 5
  name: Stellar Horizon Listallledgers 200
  slug: stellar-horizon-listallledgers-200
- key_count: 5
  name: Stellar Horizon Listalloperations 200
  slug: stellar-horizon-listalloperations-200
- key_count: 5
  name: Stellar Horizon Listallpayments 200
  slug: stellar-horizon-listallpayments-200
- key_count: 5
  name: Stellar Horizon Listalltransactions 200
  slug: stellar-horizon-listalltransactions-200
- key_count: 5
  name: Stellar Horizon Listliquiditypools 200
  slug: stellar-horizon-listliquiditypools-200
- key_count: 5
  name: Stellar Horizon Liststrictreceivepaymentpaths 200
  slug: stellar-horizon-liststrictreceivepaymentpaths-200
- key_count: 5
  name: Stellar Horizon Liststrictsendpaymentpaths 200
  slug: stellar-horizon-liststrictsendpaymentpaths-200
- key_count: 5
  name: Stellar Horizon Listtradeaggregations 200
  slug: stellar-horizon-listtradeaggregations-200
- key_count: 5
  name: Stellar Horizon Lpretrieverelatedoperations 200
  slug: stellar-horizon-lpretrieverelatedoperations-200
- key_count: 5
  name: Stellar Horizon Lpretrieverelatedtransactions 200
  slug: stellar-horizon-lpretrieverelatedtransactions-200
- key_count: 5
  name: Stellar Horizon Retrieveaclaimablebalance 200
  slug: stellar-horizon-retrieveaclaimablebalance-200
- key_count: 5
  name: Stellar Horizon Retrievealedger 200
  slug: stellar-horizon-retrievealedger-200
- key_count: 5
  name: Stellar Horizon Retrievealedgerseffects 200
  slug: stellar-horizon-retrievealedgerseffects-200
- key_count: 5
  name: Stellar Horizon Retrievealedgersoperations 200
  slug: stellar-horizon-retrievealedgersoperations-200
- key_count: 5
  name: Stellar Horizon Retrievealedgerspayments 200
  slug: stellar-horizon-retrievealedgerspayments-200
- key_count: 5
  name: Stellar Horizon Retrievealedgerstransactions 200
  slug: stellar-horizon-retrievealedgerstransactions-200
- key_count: 5
  name: Stellar Horizon Retrievealiquiditypool 200
  slug: stellar-horizon-retrievealiquiditypool-200
- key_count: 5
  name: Stellar Horizon Retrieveanaccount 200
  slug: stellar-horizon-retrieveanaccount-200
- key_count: 5
  name: Stellar Horizon Retrieveanoperation 200
  slug: stellar-horizon-retrieveanoperation-200
- key_count: 5
  name: Stellar Horizon Retrieveanoperationseffects 200
  slug: stellar-horizon-retrieveanoperationseffects-200
- key_count: 5
  name: Stellar Horizon Retrieveanorderbook 200
  slug: stellar-horizon-retrieveanorderbook-200
- key_count: 5
  name: Stellar Horizon Retrieveatransaction 200
  slug: stellar-horizon-retrieveatransaction-200
- key_count: 5
  name: Stellar Horizon Retrieveatransactionseffects 200
  slug: stellar-horizon-retrieveatransactionseffects-200
- key_count: 5
  name: Stellar Horizon Retrieveatransactionsoperations 200
  slug: stellar-horizon-retrieveatransactionsoperations-200
- key_count: 5
  name: Stellar Horizon Retrieveatransactionspayments 200
  slug: stellar-horizon-retrieveatransactionspayments-200
- key_count: 5
  name: Stellar Horizon Retrievefeestats 200
  slug: stellar-horizon-retrievefeestats-200
- key_count: 5
  name: Stellar Horizon Retrieverelatedeffects 200
  slug: stellar-horizon-retrieverelatedeffects-200
- key_count: 5
  name: Stellar Horizon Retrieverelatedtrades 200
  slug: stellar-horizon-retrieverelatedtrades-200
- key_count: 5
  name: Stellar Horizon Submitasynctransaction 201
  slug: stellar-horizon-submitasynctransaction-201
- key_count: 5
  name: Stellar Horizon Submitasynctransaction 400
  slug: stellar-horizon-submitasynctransaction-400
- key_count: 5
  name: Stellar Horizon Submitasynctransaction 403
  slug: stellar-horizon-submitasynctransaction-403
- key_count: 5
  name: Stellar Horizon Submitasynctransaction 409
  slug: stellar-horizon-submitasynctransaction-409
- key_count: 5
  name: Stellar Horizon Submitasynctransaction 500
  slug: stellar-horizon-submitasynctransaction-500
- key_count: 5
  name: Stellar Horizon Submitasynctransaction 503
  slug: stellar-horizon-submitasynctransaction-503
- key_count: 5
  name: Stellar Horizon Submitatransaction 200
  slug: stellar-horizon-submitatransaction-200
finops:
- name: Stellar Finops
  service_category: Blockchain Infrastructure
  slug: stellar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stellar.png
json_schemas:
- name: Account
  property_count: 1
  slug: stellar-horizon-account
- name: AccountMerge
  property_count: 11
  slug: stellar-horizon-accountmerge
- name: address
  property_count: 0
  slug: stellar-horizon-address
- name: Asset
  property_count: 1
  slug: stellar-horizon-asset
- name: asset_balance_change
  property_count: 7
  slug: stellar-horizon-asset_balance_change
- name: AsyncTransactionSubmissionResponse
  property_count: 3
  slug: stellar-horizon-asynctransactionsubmissionresponse
- name: BalanceLineAsset
  property_count: 12
  slug: stellar-horizon-balancelineasset
- name: BalanceLineLiquidityPool
  property_count: 9
  slug: stellar-horizon-balancelineliquiditypool
- name: BalanceLineNative
  property_count: 11
  slug: stellar-horizon-balancelinenative
- name: BaseAsset
  property_count: 3
  slug: stellar-horizon-baseasset
- name: BaseFeeDistribution
  property_count: 14
  slug: stellar-horizon-basefeedistribution
- name: ChargedFeeDistribution
  property_count: 0
  slug: stellar-horizon-chargedfeedistribution
- name: ClaimableBalance
  property_count: 10
  slug: stellar-horizon-claimablebalance
- name: ClaimableBalances
  property_count: 1
  slug: stellar-horizon-claimablebalances
- name: CreateAccount
  property_count: 12
  slug: stellar-horizon-createaccount
- name: currency
  property_count: 0
  slug: stellar-horizon-currency
- name: Effect
  property_count: 1
  slug: stellar-horizon-effect
- name: FeeBumpTransaction
  property_count: 2
  slug: stellar-horizon-feebumptransaction
- name: FeeStats
  property_count: 5
  slug: stellar-horizon-feestats
- name: flags
  property_count: 4
  slug: stellar-horizon-flags
- name: hash
  property_count: 0
  slug: stellar-horizon-hash
- name: host_function_parameter
  property_count: 2
  slug: stellar-horizon-host_function_parameter
- name: id
  property_count: 0
  slug: stellar-horizon-id
- name: InnerTransaction
  property_count: 3
  slug: stellar-horizon-innertransaction
- name: InvokeHostFunction
  property_count: 14
  slug: stellar-horizon-invokehostfunction
- name: last_modified_ledger
  property_count: 0
  slug: stellar-horizon-last_modified_ledger
- name: Ledger
  property_count: 1
  slug: stellar-horizon-ledger
- name: link
  property_count: 2
  slug: stellar-horizon-link
- name: Links
  property_count: 1
  slug: stellar-horizon-links
- name: LiquidityPool
  property_count: 10
  slug: stellar-horizon-liquiditypool
- name: LiquidityPools
  property_count: 1
  slug: stellar-horizon-liquiditypools
- name: MaxFeeDistribution
  property_count: 0
  slug: stellar-horizon-maxfeedistribution
- name: Offer
  property_count: 1
  slug: stellar-horizon-offer
- name: Operation
  property_count: 5
  slug: stellar-horizon-operation
- name: OrderBook
  property_count: 4
  slug: stellar-horizon-orderbook
- name: paging_token
  property_count: 0
  slug: stellar-horizon-paging_token
- name: Path
  property_count: 1
  slug: stellar-horizon-path
- name: PathPaymentStrictReceive
  property_count: 21
  slug: stellar-horizon-pathpaymentstrictreceive
- name: PathPaymentStrictSend
  property_count: 21
  slug: stellar-horizon-pathpaymentstrictsend
- name: Payment
  property_count: 1
  slug: stellar-horizon-payment
- name: Price
  property_count: 2
  slug: stellar-horizon-price
- name: Problem
  property_count: 5
  slug: stellar-horizon-problem
- name: schemas-Asset
  property_count: 3
  slug: stellar-horizon-schemas-asset
- name: schemas-Transaction
  property_count: 23
  slug: stellar-horizon-schemas-transaction
- name: sequence
  property_count: 0
  slug: stellar-horizon-sequence
- name: sequence_ledger
  property_count: 0
  slug: stellar-horizon-sequence_ledger
- name: signatures
  property_count: 0
  slug: stellar-horizon-signatures
- name: signers
  property_count: 4
  slug: stellar-horizon-signers
- name: subentry_count
  property_count: 0
  slug: stellar-horizon-subentry_count
- name: SubmitTransaction
  property_count: 1
  slug: stellar-horizon-submittransaction
- name: thresholds
  property_count: 3
  slug: stellar-horizon-thresholds
- name: Trade
  property_count: 1
  slug: stellar-horizon-trade
- name: TradeAggregation
  property_count: 1
  slug: stellar-horizon-tradeaggregation
- name: tradePrice
  property_count: 2
  slug: stellar-horizon-tradeprice
- name: Transaction
  property_count: 1
  slug: stellar-horizon-transaction
- name: TransactionPreconditions
  property_count: 6
  slug: stellar-horizon-transactionpreconditions
- name: TransactionPreconditionsLedgerbounds
  property_count: 2
  slug: stellar-horizon-transactionpreconditionsledgerbounds
- name: TransactionPreconditionsTimebounds
  property_count: 2
  slug: stellar-horizon-transactionpreconditionstimebounds
- name: Amount
  property_count: 3
  slug: stellar-sdp-amount
- name: APIKey
  property_count: 10
  slug: stellar-sdp-apikey
- name: Asset
  property_count: 6
  slug: stellar-sdp-asset
- name: Balance
  property_count: 3
  slug: stellar-sdp-balance
- name: BridgeIntegrationInfo
  property_count: 8
  slug: stellar-sdp-bridgeintegrationinfo
- name: BridgeIntegrationPatchRequest
  property_count: 4
  slug: stellar-sdp-bridgeintegrationpatchrequest
- name: BridgeIntegrationStatus
  property_count: 0
  slug: stellar-sdp-bridgeintegrationstatus
- name: CreateAPIKeyRequest
  property_count: 4
  slug: stellar-sdp-createapikeyrequest
- name: CreateAPIKeyResponse
  property_count: 11
  slug: stellar-sdp-createapikeyresponse
- name: CreateDirectPaymentRequest
  property_count: 5
  slug: stellar-sdp-createdirectpaymentrequest
- name: CreateReceiverRequest
  property_count: 0
  slug: stellar-sdp-createreceiverrequest
- name: CreateWalletRequest
  property_count: 7
  slug: stellar-sdp-createwalletrequest
- name: DirectPayment
  property_count: 9
  slug: stellar-sdp-directpayment
- name: Disbursement
  property_count: 19
  slug: stellar-sdp-disbursement
- name: DisbursementLite
  property_count: 10
  slug: stellar-sdp-disbursementlite
- name: DisbursementPagination
  property_count: 2
  slug: stellar-sdp-disbursementpagination
- name: DisbursementReceiver
  property_count: 8
  slug: stellar-sdp-disbursementreceiver
- name: DisbursementReceiverPagination
  property_count: 2
  slug: stellar-sdp-disbursementreceiverpagination
- name: DisbursementsStatistics
  property_count: 4
  slug: stellar-sdp-disbursementsstatistics
- name: DisbursementStatus
  property_count: 0
  slug: stellar-sdp-disbursementstatus
- name: DisbursementStatusHistory
  property_count: 0
  slug: stellar-sdp-disbursementstatushistory
- name: DisbursementStatusHistoryEntry
  property_count: 3
  slug: stellar-sdp-disbursementstatushistoryentry
- name: DistributionAccount
  property_count: 4
  slug: stellar-sdp-distributionaccount
- name: GeneralStatistics
  property_count: 5
  slug: stellar-sdp-generalstatistics
- name: KYCLinkInfo
  property_count: 11
  slug: stellar-sdp-kyclinkinfo
- name: KYCStatus
  property_count: 0
  slug: stellar-sdp-kycstatus
- name: KYCType
  property_count: 0
  slug: stellar-sdp-kyctype
- name: MessageResponse
  property_count: 1
  slug: stellar-sdp-messageresponse
- name: Organization
  property_count: 11
  slug: stellar-sdp-organization
- name: Pagination
  property_count: 4
  slug: stellar-sdp-pagination
- name: PatchReceiverRequest
  property_count: 6
  slug: stellar-sdp-patchreceiverrequest
- name: Payment
  property_count: 14
  slug: stellar-sdp-payment
- name: PaymentAmounts
  property_count: 8
  slug: stellar-sdp-paymentamounts
- name: PaymentAmountsByAsset
  property_count: 2
  slug: stellar-sdp-paymentamountsbyasset
- name: PaymentCounters
  property_count: 7
  slug: stellar-sdp-paymentcounters
- name: PaymentPagination
  property_count: 2
  slug: stellar-sdp-paymentpagination
- name: PaymentStatus
  property_count: 0
  slug: stellar-sdp-paymentstatus
- name: PaymentStatusHistory
  property_count: 0
  slug: stellar-sdp-paymentstatushistory
- name: PaymentStatusHistoryEntry
  property_count: 3
  slug: stellar-sdp-paymentstatushistoryentry
- name: Profile
  property_count: 5
  slug: stellar-sdp-profile
- name: Receiver
  property_count: 12
  slug: stellar-sdp-receiver
- name: ReceiverLite
  property_count: 1
  slug: stellar-sdp-receiverlite
- name: ReceiverPagination
  property_count: 2
  slug: stellar-sdp-receiverpagination
- name: ReceiverRegistrationRequest
  property_count: 6
  slug: stellar-sdp-receiverregistrationrequest
- name: ReceiversWalletStatus
  property_count: 0
  slug: stellar-sdp-receiverswalletstatus
- name: ReceiversWalletStatusHistoryEntry
  property_count: 2
  slug: stellar-sdp-receiverswalletstatushistoryentry
- name: ReceiverWallet
  property_count: 17
  slug: stellar-sdp-receiverwallet
- name: ReceiverWalletLite
  property_count: 14
  slug: stellar-sdp-receiverwalletlite
- name: ReceiverWalletsCounters
  property_count: 5
  slug: stellar-sdp-receiverwalletscounters
- name: RegistrationContactType
  property_count: 0
  slug: stellar-sdp-registrationcontacttype
- name: Tenant
  property_count: 12
  slug: stellar-sdp-tenant
- name: Tenants
  property_count: 0
  slug: stellar-sdp-tenants
- name: TOSStatus
  property_count: 0
  slug: stellar-sdp-tosstatus
- name: UpdateAPIKeyRequest
  property_count: 2
  slug: stellar-sdp-updateapikeyrequest
- name: UpdateWalletRequest
  property_count: 6
  slug: stellar-sdp-updatewalletrequest
- name: User
  property_count: 6
  slug: stellar-sdp-user
- name: Users
  property_count: 0
  slug: stellar-sdp-users
- name: VerificationField
  property_count: 0
  slug: stellar-sdp-verificationfield
- name: VirtualAccountDepositInstructions
  property_count: 7
  slug: stellar-sdp-virtualaccountdepositinstructions
- name: VirtualAccountDestination
  property_count: 4
  slug: stellar-sdp-virtualaccountdestination
- name: VirtualAccountInfo
  property_count: 6
  slug: stellar-sdp-virtualaccountinfo
- name: VirtualAccountStatus
  property_count: 0
  slug: stellar-sdp-virtualaccountstatus
- name: Wallet
  property_count: 7
  slug: stellar-sdp-wallet
- name: WalletLite
  property_count: 7
  slug: stellar-sdp-walletlite
jsonld:
- class_count: 8
  name: Stellar Context
  property_count: 30
  slug: stellar-context
layout: provider
modified: '2026-06-14'
name: Stellar
nav: Providers
network: true
overview: 'Stellar publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Admin API, API Keys API, and 29 more. Tagged areas include Blockchain, Cryptocurrency, Decentralized Exchange, Ledger, and Payments.


  The Stellar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stellar''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Stellar Plans Pricing
  plan_count: 3
  slug: stellar-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 2
  name: Stellar Rate Limits
  slug: stellar-rate-limits
rules:
- name: Stellar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stellar-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.2
    developer_ergonomics: 28.3
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stellar/refs/heads/main/screenshots/stellar-2026-06-20T194539.png
security:
- kind: authentication
  name: Stellar Authentication
  slug: stellar-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Stellar Domain Security
  slug: stellar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stellar
tags:
- Blockchain
- Cryptocurrency
- Decentralized Exchange
- Ledger
- Payments
- Smart Contracts
- Web3
---

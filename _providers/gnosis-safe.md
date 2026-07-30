---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Gnosis Safe Agentic Access
  operation_count: 59
  slug: gnosis-safe-agentic-access
  summary_line: 59 operations · 16 acting
api_count: 16
apis:
- description: Endpoints for managing delegate relationships on a Safe. Delegates are addresses authorized by Safe owners to propose transactions without being full owners. Supports creating, listing, and deleting d
  name: Safe Delegates API
  slug: delegates
- description: Endpoints for off-chain message signing via Safe smart accounts. Allows creating signed messages for a Safe, retrieving existing messages by their hash, and listing all messages associated with a Safe
  name: Safe Messages API
  slug: messages
- description: Endpoints supporting ERC-4337 account abstraction user operations for Safe smart accounts. Allows listing, retrieving, and managing ERC-4337 user operations associated with a Safe, enabling gas-abstra
  name: Safe 4337 User Operations API
  slug: '4337'
- description: 'Official TypeScript client SDK for the Safe Transaction Service API. Wraps all Transaction Service endpoints with typed methods for proposing transactions, confirming signatures, fetching pending and '
  name: Safe API Kit (TypeScript SDK)
  slug: api-kit
- description: The 4337 API from Safe (Gnosis Safe) — 5 operation(s) for 4337.
  name: Safe (Gnosis Safe) 4337 API
  slug: gnosis-safe-4337-api
- description: The about API from Safe (Gnosis Safe) — 6 operation(s) for about.
  name: Safe (Gnosis Safe) about API
  slug: gnosis-safe-about-api
- description: The analytics API from Safe (Gnosis Safe) — 1 operation(s) for analytics.
  name: Safe (Gnosis Safe) analytics API
  slug: gnosis-safe-analytics-api
- description: The contracts API from Safe (Gnosis Safe) — 2 operation(s) for contracts.
  name: Safe (Gnosis Safe) contracts API
  slug: gnosis-safe-contracts-api
- description: The data-decoder API from Safe (Gnosis Safe) — 1 operation(s) for data-decoder.
  name: Safe (Gnosis Safe) data-decoder API
  slug: gnosis-safe-data-decoder-api
- description: The delegates API from Safe (Gnosis Safe) — 5 operation(s) for delegates.
  name: Safe (Gnosis Safe) delegates API
  slug: gnosis-safe-delegates-api
- description: The messages API from Safe (Gnosis Safe) — 3 operation(s) for messages.
  name: Safe (Gnosis Safe) messages API
  slug: gnosis-safe-messages-api
- description: The modules API from Safe (Gnosis Safe) — 2 operation(s) for modules.
  name: Safe (Gnosis Safe) modules API
  slug: gnosis-safe-modules-api
- description: The owners API from Safe (Gnosis Safe) — 2 operation(s) for owners.
  name: Safe (Gnosis Safe) owners API
  slug: gnosis-safe-owners-api
- description: The safes API from Safe (Gnosis Safe) — 6 operation(s) for safes.
  name: Safe (Gnosis Safe) safes API
  slug: gnosis-safe-safes-api
- description: The tokens API from Safe (Gnosis Safe) — 3 operation(s) for tokens.
  name: Safe (Gnosis Safe) tokens API
  slug: gnosis-safe-tokens-api
- description: The transactions API from Safe (Gnosis Safe) — 13 operation(s) for transactions.
  name: Safe (Gnosis Safe) transactions API
  slug: gnosis-safe-transactions-api
artifact_total: 150
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gnosis-safe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gnosis-safe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gnosis-safe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://safe.global/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.safe.global/
- group: start
  title: ''
  type: Portal
  url: https://developer.safe.global/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/safe-global
- group: commercial
  title: ''
  type: Plans
  url: plans/gnosis-safe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gnosis-safe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gnosis-safe-finops.yml
- group: operate
  title: ''
  type: Status
  url: https://status.safe.global/
- group: company
  title: ''
  type: Blog
  url: https://safe.mirror.xyz/
- group: other
  title: ''
  type: X
  url: https://x.com/safe
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/safe
created: '2026-06-13'
description: Safe (formerly Gnosis Safe) provides multi-signature smart contract wallets for managing digital assets on EVM-compatible blockchains. The Safe Transaction Service is a REST API that tracks transactions submitted to Safe smart contracts, enabling off-chain collection of signatures, owner notification of pending transactions, delegate management, on-chain message signing, and token/NFT balance retrieval across 40+ supported networks including Mainnet, Arbitrum, Optimism, Polygon, Base, Gnosis Chain, zkSync, and testnets. The Safe{Core} SDK (API Kit) provides a TypeScript client for the Transaction Service. Authentication uses JWT API keys with tiered plans ranging from a free Builder tier to high-throughput Scale plans.
examples:
- key_count: 8
  name: About_Deployments_List
  slug: about_deployments_list
- key_count: 8
  name: About_Ethereum_Rpc_Retrieve
  slug: about_ethereum_rpc_retrieve
- key_count: 8
  name: About_Ethereum_Tracing_Rpc_Retrieve
  slug: about_ethereum_tracing_rpc_retrieve
- key_count: 8
  name: About_Indexing_Retrieve
  slug: about_indexing_retrieve
- key_count: 8
  name: About_Retrieve
  slug: about_retrieve
- key_count: 8
  name: About_Singletons_List
  slug: about_singletons_list
- key_count: 8
  name: Analytics_Multisig_Transactions_By_Origin_Retrieve
  slug: analytics_multisig_transactions_by_origin_retrieve
- key_count: 8
  name: Contracts_List
  slug: contracts_list
- key_count: 8
  name: Contracts_Retrieve
  slug: contracts_retrieve
- key_count: 9
  name: Data_Decoder_Create
  slug: data_decoder_create
- key_count: 9
  name: Delegates_Create
  slug: delegates_create
- key_count: 9
  name: Delegates_Create_2
  slug: delegates_create_2
- key_count: 8
  name: Delegates_Destroy
  slug: delegates_destroy
- key_count: 8
  name: Delegates_Destroy_2
  slug: delegates_destroy_2
- key_count: 8
  name: Delegates_List
  slug: delegates_list
- key_count: 8
  name: Delegates_List_2
  slug: delegates_list_2
- key_count: 8
  name: Messages_Retrieve
  slug: messages_retrieve
- key_count: 9
  name: Messages_Signatures_Create
  slug: messages_signatures_create
- key_count: 8
  name: Module_Transaction_Retrieve
  slug: module_transaction_retrieve
- key_count: 8
  name: Modules_Safes_List
  slug: modules_safes_list
- key_count: 8
  name: Modules_Safes_Retrieve
  slug: modules_safes_retrieve
- key_count: 9
  name: Multisig_Transactions_Confirmations_Create
  slug: multisig_transactions_confirmations_create
- key_count: 8
  name: Multisig_Transactions_Confirmations_List
  slug: multisig_transactions_confirmations_list
- key_count: 8
  name: Multisig_Transactions_Destroy
  slug: multisig_transactions_destroy
- key_count: 8
  name: Multisig_Transactions_Destroy_2
  slug: multisig_transactions_destroy_2
- key_count: 8
  name: Multisig_Transactions_Retrieve
  slug: multisig_transactions_retrieve
- key_count: 8
  name: Multisig_Transactions_Retrieve_2
  slug: multisig_transactions_retrieve_2
- key_count: 2
  name: Operations Index
  slug: operations-index
- key_count: 8
  name: Owners_Safes_List
  slug: owners_safes_list
- key_count: 8
  name: Owners_Safes_Retrieve
  slug: owners_safes_retrieve
- key_count: 9
  name: Safe_Operations_Confirmations_Create
  slug: safe_operations_confirmations_create
- key_count: 8
  name: Safe_Operations_Confirmations_List
  slug: safe_operations_confirmations_list
- key_count: 8
  name: Safe_Operations_Retrieve
  slug: safe_operations_retrieve
- key_count: 8
  name: Safes_All_Transactions_List
  slug: safes_all_transactions_list
- key_count: 8
  name: Safes_All_Transactions_List_2
  slug: safes_all_transactions_list_2
- key_count: 8
  name: Safes_Balances_Retrieve
  slug: safes_balances_retrieve
- key_count: 8
  name: Safes_Balances_Retrieve_2
  slug: safes_balances_retrieve_2
- key_count: 8
  name: Safes_Collectibles_Retrieve
  slug: safes_collectibles_retrieve
- key_count: 8
  name: Safes_Creation_Retrieve
  slug: safes_creation_retrieve
- key_count: 8
  name: Safes_Delegates_Destroy
  slug: safes_delegates_destroy
- key_count: 8
  name: Safes_Export_Retrieve
  slug: safes_export_retrieve
- key_count: 8
  name: Safes_Incoming_Transfers_List
  slug: safes_incoming_transfers_list
- key_count: 9
  name: Safes_Messages_Create
  slug: safes_messages_create
- key_count: 8
  name: Safes_Messages_List
  slug: safes_messages_list
- key_count: 8
  name: Safes_Module_Transactions_List
  slug: safes_module_transactions_list
- key_count: 9
  name: Safes_Multisig_Transactions_Create
  slug: safes_multisig_transactions_create
- key_count: 9
  name: Safes_Multisig_Transactions_Create_2
  slug: safes_multisig_transactions_create_2
- key_count: 9
  name: Safes_Multisig_Transactions_Estimations_Create
  slug: safes_multisig_transactions_estimations_create
- key_count: 8
  name: Safes_Multisig_Transactions_List
  slug: safes_multisig_transactions_list
- key_count: 8
  name: Safes_Multisig_Transactions_List_2
  slug: safes_multisig_transactions_list_2
- key_count: 8
  name: Safes_Retrieve
  slug: safes_retrieve
- key_count: 9
  name: Safes_Safe_Operations_Create
  slug: safes_safe_operations_create
- key_count: 8
  name: Safes_Safe_Operations_List
  slug: safes_safe_operations_list
- key_count: 8
  name: Safes_Transfers_List
  slug: safes_transfers_list
- key_count: 8
  name: Safes_User_Operations_List
  slug: safes_user_operations_list
- key_count: 8
  name: Tokens_List
  slug: tokens_list
- key_count: 8
  name: Tokens_Lists_List
  slug: tokens_lists_list
- key_count: 8
  name: Tokens_Retrieve
  slug: tokens_retrieve
- key_count: 8
  name: Transfer_Retrieve
  slug: transfer_retrieve
- key_count: 8
  name: User_Operations_Retrieve
  slug: user_operations_retrieve
finops:
- name: Gnosis Safe Finops
  service_category: Blockchain Infrastructure
  slug: gnosis-safe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gnosis-safe.png
json_schemas:
- name: AllTransactionsSchema
  property_count: 3
  slug: AllTransactionsSchema
- name: AllTransactionsSchemaSerializerV2
  property_count: 3
  slug: AllTransactionsSchemaSerializerV2
- name: CodeErrorResponse
  property_count: 3
  slug: CodeErrorResponse
- name: Contract
  property_count: 6
  slug: Contract
- name: ContractAbi
  property_count: 3
  slug: ContractAbi
- name: DataDecoder
  property_count: 2
  slug: DataDecoder
- name: Delegate
  property_count: 5
  slug: Delegate
- name: DelegateSerializerV2
  property_count: 6
  slug: DelegateSerializerV2
- name: Erc20Info
  property_count: 4
  slug: Erc20Info
- name: EthereumTxWithTransfersResponse
  property_count: 8
  slug: EthereumTxWithTransfersResponse
- name: IndexingStatus
  property_count: 9
  slug: IndexingStatus
- name: MasterCopyResponse
  property_count: 6
  slug: MasterCopyResponse
- name: ModulesResponse
  property_count: 1
  slug: ModulesResponse
- name: OwnerResponse
  property_count: 1
  slug: OwnerResponse
- name: PaginatedAllTransactionsSchemaList
  property_count: 4
  slug: PaginatedAllTransactionsSchemaList
- name: PaginatedAllTransactionsSchemaSerializerV2List
  property_count: 4
  slug: PaginatedAllTransactionsSchemaSerializerV2List
- name: PaginatedContractList
  property_count: 4
  slug: PaginatedContractList
- name: PaginatedSafeCollectibleResponseList
  property_count: 4
  slug: PaginatedSafeCollectibleResponseList
- name: PaginatedSafeDelegateResponseList
  property_count: 4
  slug: PaginatedSafeDelegateResponseList
- name: PaginatedSafeExportTransactionList
  property_count: 4
  slug: PaginatedSafeExportTransactionList
- name: PaginatedSafeLastStatusList
  property_count: 4
  slug: PaginatedSafeLastStatusList
- name: PaginatedSafeMessageResponseList
  property_count: 4
  slug: PaginatedSafeMessageResponseList
- name: PaginatedSafeModuleTransactionResponseList
  property_count: 4
  slug: PaginatedSafeModuleTransactionResponseList
- name: PaginatedSafeMultisigConfirmationResponseList
  property_count: 4
  slug: PaginatedSafeMultisigConfirmationResponseList
- name: PaginatedSafeMultisigTransactionResponseList
  property_count: 4
  slug: PaginatedSafeMultisigTransactionResponseList
- name: PaginatedSafeMultisigTransactionResponseSerializerV2List
  property_count: 4
  slug: PaginatedSafeMultisigTransactionResponseSerializerV2List
- name: PaginatedSafeOperationConfirmationResponseList
  property_count: 4
  slug: PaginatedSafeOperationConfirmationResponseList
- name: PaginatedSafeOperationWithUserOperationResponseList
  property_count: 4
  slug: PaginatedSafeOperationWithUserOperationResponseList
- name: PaginatedTokenInfoResponseList
  property_count: 4
  slug: PaginatedTokenInfoResponseList
- name: PaginatedTokenListList
  property_count: 4
  slug: PaginatedTokenListList
- name: PaginatedTransferWithTokenInfoResponseList
  property_count: 4
  slug: PaginatedTransferWithTokenInfoResponseList
- name: PaginatedUserOperationWithSafeOperationResponseList
  property_count: 4
  slug: PaginatedUserOperationWithSafeOperationResponseList
- name: SafeBalanceResponse
  property_count: 3
  slug: SafeBalanceResponse
- name: SafeCollectibleResponse
  property_count: 10
  slug: SafeCollectibleResponse
- name: SafeCreationInfoResponse
  property_count: 9
  slug: SafeCreationInfoResponse
- name: SafeDelegateResponse
  property_count: 5
  slug: SafeDelegateResponse
- name: SafeDeployment
  property_count: 2
  slug: SafeDeployment
- name: SafeDeploymentContract
  property_count: 2
  slug: SafeDeploymentContract
- name: SafeExportTransaction
  property_count: 16
  slug: SafeExportTransaction
- name: SafeInfoResponse
  property_count: 10
  slug: SafeInfoResponse
- name: SafeLastStatus
  property_count: 9
  slug: SafeLastStatus
- name: SafeMessage
  property_count: 4
  slug: SafeMessage
- name: SafeMessageResponse
  property_count: 10
  slug: SafeMessageResponse
- name: SafeMessageSignature
  property_count: 1
  slug: SafeMessageSignature
- name: SafeModuleTransactionResponse
  property_count: 13
  slug: SafeModuleTransactionResponse
- name: SafeModuleTransactionWithTransfersResponse
  property_count: 15
  slug: SafeModuleTransactionWithTransfersResponse
- name: SafeMultisigConfirmation
  property_count: 1
  slug: SafeMultisigConfirmation
- name: SafeMultisigConfirmationResponse
  property_count: 5
  slug: SafeMultisigConfirmationResponse
- name: SafeMultisigTransaction
  property_count: 15
  slug: SafeMultisigTransaction
- name: SafeMultisigTransactionEstimate
  property_count: 4
  slug: SafeMultisigTransactionEstimate
- name: SafeMultisigTransactionEstimateResponse
  property_count: 1
  slug: SafeMultisigTransactionEstimateResponse
- name: SafeMultisigTransactionResponse
  property_count: 34
  slug: SafeMultisigTransactionResponse
- name: SafeMultisigTransactionResponseSerializerV2
  property_count: 34
  slug: SafeMultisigTransactionResponseSerializerV2
- name: SafeMultisigTransactionWithTransfersResponse
  property_count: 36
  slug: SafeMultisigTransactionWithTransfersResponse
- name: SafeMultisigTransactionWithTransfersResponseSerializerV2
  property_count: 36
  slug: SafeMultisigTransactionWithTransfersResponseSerializerV2
- name: SafeOperation
  property_count: 14
  slug: SafeOperation
- name: SafeOperationConfirmation
  property_count: 1
  slug: SafeOperationConfirmation
- name: SafeOperationConfirmationResponse
  property_count: 5
  slug: SafeOperationConfirmationResponse
- name: SafeOperationResponse
  property_count: 8
  slug: SafeOperationResponse
- name: SafeOperationWithUserOperationResponse
  property_count: 9
  slug: SafeOperationWithUserOperationResponse
- name: TokenInfoResponse
  property_count: 7
  slug: TokenInfoResponse
- name: TokenList
  property_count: 2
  slug: TokenList
- name: TransferWithTokenInfoResponse
  property_count: 11
  slug: TransferWithTokenInfoResponse
- name: UserOperationResponse
  property_count: 15
  slug: UserOperationResponse
- name: UserOperationWithSafeOperationResponse
  property_count: 16
  slug: UserOperationWithSafeOperationResponse
jsonld:
- class_count: 0
  name: Gnosis Safe Api Context
  property_count: 0
  slug: gnosis-safe-api
- class_count: 49
  name: Gnosis Safe Context
  property_count: 6
  slug: gnosis-safe-context
layout: provider
modified: '2026-06-13'
name: Safe (Gnosis Safe)
nav: Providers
network: true
overview: 'Safe (Gnosis Safe) publishes 12 APIs on the [APIs.io](https://apis.io/) network, including 4337 API, about API, analytics API, and 9 more. Tagged areas include Multisig, Smart Contract, Ethereum, Web3, and Blockchain.


  The Safe (Gnosis Safe) catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Safe (Gnosis Safe)''s developer surface includes authentication, documentation, developer portal, GitHub presence, status page, engineering blog, and 8 more developer resources.'
plans:
- name: Gnosis Safe Plans Pricing
  plan_count: 4
  slug: gnosis-safe-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 8
  name: Gnosis Safe Rate Limits
  slug: gnosis-safe-rate-limits
rules:
- name: Safe (Gnosis Safe) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gnosis-safe-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.9
  delta: -6.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.3
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/gnosis-safe/refs/heads/main/screenshots/gnosis-safe-2026-06-20T181937.png
security:
- kind: authentication
  name: Gnosis Safe Authentication
  slug: gnosis-safe-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Gnosis Safe Domain Security
  slug: gnosis-safe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gnosis-safe
tags:
- Multisig
- Smart Contract
- Ethereum
- Web3
- Blockchain
- DeFi
- Safe
- Gnosis
- Wallet
website: https://safe.global/
---

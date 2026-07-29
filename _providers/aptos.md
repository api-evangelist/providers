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
    asyncapi_events: false
    auth_clarity: false
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
  score: 28.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Aptos Agentic Access
  operation_count: 29
  slug: aptos-agentic-access
  summary_line: 29 operations · 7 acting
api_count: 10
apis:
- description: 'High-level GraphQL API backed by the Aptos Indexer, providing opinionated access to processed blockchain data. Optimized for querying NFTs, Aptos Objects, token balances, fungible assets, custom Move '
  name: Aptos Indexer GraphQL API
  slug: indexer-graphql-api
- description: 'gRPC streaming API that delivers historical and real-time transaction data from the Aptos blockchain. Used to power the Aptos Core Indexer and to build custom app-specific real-time event processors. '
  name: Aptos Transaction Stream API
  slug: transaction-stream-api
- description: Testnet and devnet faucet that distributes APT test tokens for development and testing. Available programmatically on devnet; testnet faucet is accessible via the mint page. Not available on mainnet.
  name: Aptos Faucet API
  slug: faucet-api
- description: Access to accounts, resources, and modules
  name: Aptos Accounts API
  slug: aptos-accounts-api
- description: Access to blocks
  name: Aptos Blocks API
  slug: aptos-blocks-api
- description: Access to events
  name: Aptos Events API
  slug: aptos-events-api
- description: General information
  name: Aptos General API
  slug: aptos-general-api
- description: Access to tables
  name: Aptos Tables API
  slug: aptos-tables-api
- description: Access to transactions
  name: Aptos Transactions API
  slug: aptos-transactions-api
- description: View functions,
  name: Aptos View API
  slug: aptos-view-api
artifact_total: 253
collections:
- collection_type: postman
  name: Aptos Node Accounts API
  slug: postman-aptos-accounts-api
- collection_type: postman
  name: Aptos Node Accounts Blocks API
  slug: postman-aptos-blocks-api
- collection_type: postman
  name: Aptos Node Accounts Events API
  slug: postman-aptos-events-api
- collection_type: postman
  name: Aptos Node Accounts General API
  slug: postman-aptos-general-api
- collection_type: postman
  name: Aptos Node Accounts Tables API
  slug: postman-aptos-tables-api
- collection_type: postman
  name: Aptos Node Accounts Transactions API
  slug: postman-aptos-transactions-api
- collection_type: postman
  name: Aptos Node Accounts View API
  slug: postman-aptos-view-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aptos/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aptos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptos-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aptos.dev
- group: docs
  title: ''
  type: Documentation
  url: https://aptos.dev/en/build/apis
- group: docs
  title: ''
  type: APIReference
  url: https://api.mainnet.aptoslabs.com/v1/spec
- group: start
  title: ''
  type: GettingStarted
  url: https://aptos.dev/en/build/get-started
- group: start
  title: ''
  type: Signup
  url: https://geomi.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://geomi.dev/pricing
- group: operate
  title: ''
  type: RateLimiting
  url: https://geomi.dev/docs/admin/billing
- group: other
  title: ''
  type: Networks
  url: https://aptos.dev/en/network/nodes/networks
- group: company
  title: ''
  type: Blog
  url: https://aptoslabs.medium.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aptoslabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aptoslabs.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aptos-labs
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/aptos-labs/aptos-core/main/api/doc/spec.yaml
- group: build
  title: TypeScript / JavaScript SDK
  type: SDKs
  url: https://github.com/aptos-labs/aptos-ts-sdk
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/aptos-labs/aptos-python-sdk
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/aptos-labs/aptos-go-sdk
- group: build
  title: Rust SDK
  type: SDKs
  url: https://github.com/aptos-labs/aptos-core/tree/main/sdk
- group: commercial
  title: ''
  type: Plans
  url: plans/aptos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aptos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aptos-finops.yml
created: '2026-06-13'
description: Aptos is a Move-based Layer 1 blockchain platform that exposes a REST API for reading on-chain state and submitting transactions, a GraphQL Indexer API for high-level queries over processed blockchain data (NFTs, objects, custom Move contracts), and a gRPC Transaction Stream for real-time and historical event feeds. Public endpoints are provided by Aptos Labs for mainnet, testnet, and devnet; enhanced rate limits are available through Geomi (formerly Aptos Labs Developer Portal).
examples:
- key_count: 9
  name: Encode_Submission
  slug: encode_submission
- key_count: 9
  name: Estimate_Gas_Price
  slug: estimate_gas_price
- key_count: 9
  name: Get_Account
  slug: get_account
- key_count: 9
  name: Get_Account_Balance
  slug: get_account_balance
- key_count: 9
  name: Get_Account_Module
  slug: get_account_module
- key_count: 9
  name: Get_Account_Modules
  slug: get_account_modules
- key_count: 9
  name: Get_Account_Resource
  slug: get_account_resource
- key_count: 9
  name: Get_Account_Resources
  slug: get_account_resources
- key_count: 9
  name: Get_Account_Transaction_Summaries
  slug: get_account_transaction_summaries
- key_count: 9
  name: Get_Account_Transactions
  slug: get_account_transactions
- key_count: 9
  name: Get_Block_By_Height
  slug: get_block_by_height
- key_count: 9
  name: Get_Block_By_Version
  slug: get_block_by_version
- key_count: 9
  name: Get_Events_By_Creation_Number
  slug: get_events_by_creation_number
- key_count: 9
  name: Get_Events_By_Event_Handle
  slug: get_events_by_event_handle
- key_count: 9
  name: Get_Ledger_Info
  slug: get_ledger_info
- key_count: 9
  name: Get_Raw_Table_Item
  slug: get_raw_table_item
- key_count: 9
  name: Get_Table_Item
  slug: get_table_item
- key_count: 9
  name: Get_Transaction_By_Hash
  slug: get_transaction_by_hash
- key_count: 9
  name: Get_Transaction_By_Version
  slug: get_transaction_by_version
- key_count: 9
  name: Get_Transactions
  slug: get_transactions
- key_count: 9
  name: Get_Transactions_Auxiliary_Info
  slug: get_transactions_auxiliary_info
- key_count: 9
  name: Healthy
  slug: healthy
- key_count: 9
  name: Info
  slug: info
- key_count: 9
  name: Simulate_Transaction
  slug: simulate_transaction
- key_count: 9
  name: Spec
  slug: spec
- key_count: 9
  name: Submit_Batch_Transactions
  slug: submit_batch_transactions
- key_count: 9
  name: Submit_Transaction
  slug: submit_transaction
- key_count: 9
  name: View
  slug: view
- key_count: 9
  name: Wait_Transaction_By_Hash
  slug: wait_transaction_by_hash
features:
- description: Aptos uses the Move language for safe, resource-oriented smart contracts and on-chain modules.
  name: Move-based smart contracts
- description: Dual API surface — low-level REST for nodes and high-level GraphQL for indexed blockchain data.
  name: REST and GraphQL APIs
- description: Real-time and historical transaction event feeds via gRPC for custom indexers and processors.
  name: gRPC transaction streaming
- description: Public mainnet, testnet, and devnet endpoints with consistent API surfaces across all three.
  name: Multi-network support
- description: Compute-unit metered access with $10-$100/month free credit; no locked tiers.
  name: Usage-based API access via Geomi
finops:
- name: Aptos Finops
  service_category: Blockchain
  slug: aptos-finops
graphqls:
- description: The Aptos Indexer GraphQL API provides high-level access to processed Aptos blockchain data. Backed by a Hasura GraphQL engine over the Aptos Indexer database, it exposes queryable tables covering tok
  name: Aptos GraphQL API
  slug: aptos-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aptos.png
json_schemas:
- name: AbstractSignature
  property_count: 2
  slug: AbstractSignature
- name: AccountData
  property_count: 2
  slug: AccountData
- name: AccountSignature
  property_count: 0
  slug: AccountSignature
- name: AccountSignature_AbstractSignature
  property_count: 0
  slug: AccountSignature_AbstractSignature
- name: AccountSignature_Ed25519Signature
  property_count: 0
  slug: AccountSignature_Ed25519Signature
- name: AccountSignature_MultiEd25519Signature
  property_count: 0
  slug: AccountSignature_MultiEd25519Signature
- name: AccountSignature_MultiKeySignature
  property_count: 0
  slug: AccountSignature_MultiKeySignature
- name: AccountSignature_NoAccountSignature
  property_count: 0
  slug: AccountSignature_NoAccountSignature
- name: AccountSignature_SingleKeySignature
  property_count: 0
  slug: AccountSignature_SingleKeySignature
- name: Address
  property_count: 0
  slug: Address
- name: AptosError
  property_count: 3
  slug: AptosError
- name: AptosErrorCode
  property_count: 0
  slug: AptosErrorCode
- name: AssetType
  property_count: 0
  slug: AssetType
- name: Block
  property_count: 6
  slug: Block
- name: BlockEndInfo
  property_count: 4
  slug: BlockEndInfo
- name: BlockEpilogueTransaction
  property_count: 12
  slug: BlockEpilogueTransaction
- name: BlockMetadataExtension
  property_count: 0
  slug: BlockMetadataExtension
- name: BlockMetadataExtensionEmpty
  property_count: 0
  slug: BlockMetadataExtensionEmpty
- name: BlockMetadataExtensionRandomness
  property_count: 1
  slug: BlockMetadataExtensionRandomness
- name: BlockMetadataExtensionRandomnessAndDecKey
  property_count: 2
  slug: BlockMetadataExtensionRandomnessAndDecKey
- name: BlockMetadataExtension_BlockMetadataExtensionEmpty
  property_count: 0
  slug: BlockMetadataExtension_BlockMetadataExtensionEmpty
- name: BlockMetadataExtension_BlockMetadataExtensionRandomness
  property_count: 0
  slug: BlockMetadataExtension_BlockMetadataExtensionRandomness
- name: BlockMetadataExtension_BlockMetadataExtensionRandomnessAndDecKey
  property_count: 0
  slug: BlockMetadataExtension_BlockMetadataExtensionRandomnessAndDecKey
- name: BlockMetadataTransaction
  property_count: 19
  slug: BlockMetadataTransaction
- name: ChunkyDKGResultTransaction
  property_count: 14
  slug: ChunkyDKGResultTransaction
- name: ClaimedEntryFunction
  property_count: 2
  slug: ClaimedEntryFunction
- name: DKGResultTransaction
  property_count: 13
  slug: DKGResultTransaction
- name: DecodedTableData
  property_count: 4
  slug: DecodedTableData
- name: DecryptedPayload
  property_count: 6
  slug: DecryptedPayload
- name: DelegatedVoterLimitsRequest
  property_count: 2
  slug: DelegatedVoterLimitsRequest
- name: DelegationPoolDelegatorLimitsRequest
  property_count: 2
  slug: DelegationPoolDelegatorLimitsRequest
- name: DeleteModule
  property_count: 3
  slug: DeleteModule
- name: DeleteResource
  property_count: 3
  slug: DeleteResource
- name: DeleteTableItem
  property_count: 4
  slug: DeleteTableItem
- name: DeletedTableData
  property_count: 2
  slug: DeletedTableData
- name: DeprecatedModuleBundlePayload
  property_count: 0
  slug: DeprecatedModuleBundlePayload
- name: DirectWriteSet
  property_count: 2
  slug: DirectWriteSet
- name: Ed25519
  property_count: 1
  slug: Ed25519
- name: Ed25519Signature
  property_count: 2
  slug: Ed25519Signature
- name: EncodeSubmissionRequest
  property_count: 8
  slug: EncodeSubmissionRequest
- name: EncryptedPayload
  property_count: 4
  slug: EncryptedPayload
- name: EncryptedTransactionInnerPayload
  property_count: 0
  slug: EncryptedTransactionInnerPayload
- name: EncryptedTransactionInnerPayload_EntryFunctionPayload
  property_count: 0
  slug: EncryptedTransactionInnerPayload_EntryFunctionPayload
- name: EncryptedTransactionInnerPayload_MultisigPayload
  property_count: 0
  slug: EncryptedTransactionInnerPayload_MultisigPayload
- name: EncryptedTransactionInnerPayload_ScriptPayload
  property_count: 0
  slug: EncryptedTransactionInnerPayload_ScriptPayload
- name: EncryptedTransactionPayload
  property_count: 0
  slug: EncryptedTransactionPayload
- name: EncryptedTransactionPayload_DecryptedPayload
  property_count: 0
  slug: EncryptedTransactionPayload_DecryptedPayload
- name: EncryptedTransactionPayload_EncryptedPayload
  property_count: 0
  slug: EncryptedTransactionPayload_EncryptedPayload
- name: EncryptedTransactionPayload_FailedDecryptionPayload
  property_count: 0
  slug: EncryptedTransactionPayload_FailedDecryptionPayload
- name: EntryFunctionId
  property_count: 0
  slug: EntryFunctionId
- name: EntryFunctionPayload
  property_count: 3
  slug: EntryFunctionPayload
- name: Event
  property_count: 4
  slug: Event
- name: EventGuid
  property_count: 2
  slug: EventGuid
- name: ExportedAggregateSignature
  property_count: 2
  slug: ExportedAggregateSignature
- name: ExportedCertifiedAggregatedChunkySubtranscript
  property_count: 4
  slug: ExportedCertifiedAggregatedChunkySubtranscript
- name: ExportedDKGTranscript
  property_count: 3
  slug: ExportedDKGTranscript
- name: ExportedProviderJWKs
  property_count: 3
  slug: ExportedProviderJWKs
- name: ExportedQuorumCertifiedUpdate
  property_count: 2
  slug: ExportedQuorumCertifiedUpdate
- name: FailedDecryptionPayload
  property_count: 4
  slug: FailedDecryptionPayload
- name: FederatedKeyless
  property_count: 1
  slug: FederatedKeyless
- name: FeePayerSignature
  property_count: 5
  slug: FeePayerSignature
- name: GasEstimation
  property_count: 3
  slug: GasEstimation
- name: GenesisPayload
  property_count: 0
  slug: GenesisPayload
- name: GenesisPayload_WriteSetPayload
  property_count: 0
  slug: GenesisPayload_WriteSetPayload
- name: GenesisTransaction
  property_count: 12
  slug: GenesisTransaction
- name: HashValue
  property_count: 0
  slug: HashValue
- name: HealthCheckSuccess
  property_count: 1
  slug: HealthCheckSuccess
- name: HexEncodedBytes
  property_count: 0
  slug: HexEncodedBytes
- name: I128
  property_count: 0
  slug: I128
- name: I256
  property_count: 0
  slug: I256
- name: I64
  property_count: 0
  slug: I64
- name: IdentifierWrapper
  property_count: 0
  slug: IdentifierWrapper
- name: IndexResponse
  property_count: 10
  slug: IndexResponse
- name: IndexedSignature
  property_count: 2
  slug: IndexedSignature
- name: JWK
  property_count: 0
  slug: JWK
- name: JWKUpdateTransaction
  property_count: 13
  slug: JWKUpdateTransaction
- name: Keyless
  property_count: 1
  slug: Keyless
- name: MoveAbility
  property_count: 0
  slug: MoveAbility
- name: MoveFunction
  property_count: 7
  slug: MoveFunction
- name: MoveFunctionGenericTypeParam
  property_count: 1
  slug: MoveFunctionGenericTypeParam
- name: MoveFunctionVisibility
  property_count: 0
  slug: MoveFunctionVisibility
- name: MoveModule
  property_count: 5
  slug: MoveModule
- name: MoveModuleBytecode
  property_count: 2
  slug: MoveModuleBytecode
- name: MoveModuleId
  property_count: 0
  slug: MoveModuleId
- name: MoveResource
  property_count: 2
  slug: MoveResource
- name: MoveScriptBytecode
  property_count: 2
  slug: MoveScriptBytecode
- name: MoveStruct
  property_count: 8
  slug: MoveStruct
- name: MoveStructField
  property_count: 2
  slug: MoveStructField
- name: MoveStructGenericTypeParam
  property_count: 1
  slug: MoveStructGenericTypeParam
- name: MoveStructTag
  property_count: 0
  slug: MoveStructTag
- name: MoveStructValue
  property_count: 0
  slug: MoveStructValue
- name: MoveStructVariant
  property_count: 2
  slug: MoveStructVariant
- name: MoveType
  property_count: 0
  slug: MoveType
- name: MoveValue
  property_count: 0
  slug: MoveValue
- name: MultiAgentSignature
  property_count: 3
  slug: MultiAgentSignature
- name: MultiEd25519Signature
  property_count: 4
  slug: MultiEd25519Signature
- name: MultiKeySignature
  property_count: 3
  slug: MultiKeySignature
- name: MultisigPayload
  property_count: 2
  slug: MultisigPayload
- name: MultisigTransactionPayload
  property_count: 0
  slug: MultisigTransactionPayload
- name: MultisigTransactionPayload_EntryFunctionPayload
  property_count: 0
  slug: MultisigTransactionPayload_EntryFunctionPayload
- name: MultisigTransactionPayload_ScriptPayload
  property_count: 0
  slug: MultisigTransactionPayload_ScriptPayload
- name: NoAccountSignature
  property_count: 0
  slug: NoAccountSignature
- name: PendingTransaction
  property_count: 10
  slug: PendingTransaction
- name: PersistedAuxiliaryInfo
  property_count: 1
  slug: PersistedAuxiliaryInfo
- name: PublicKey
  property_count: 0
  slug: PublicKey
- name: PublicKey_Ed25519
  property_count: 0
  slug: PublicKey_Ed25519
- name: PublicKey_FederatedKeyless
  property_count: 0
  slug: PublicKey_FederatedKeyless
- name: PublicKey_Keyless
  property_count: 0
  slug: PublicKey_Keyless
- name: PublicKey_Secp256k1Ecdsa
  property_count: 0
  slug: PublicKey_Secp256k1Ecdsa
- name: PublicKey_Secp256r1Ecdsa
  property_count: 0
  slug: PublicKey_Secp256r1Ecdsa
- name: PublicKey_SlhDsa_Sha2_128s
  property_count: 0
  slug: PublicKey_SlhDsa_Sha2_128s
- name: RSA_JWK
  property_count: 5
  slug: RSA_JWK
- name: RawTableItemRequest
  property_count: 1
  slug: RawTableItemRequest
- name: ReplayProtector
  property_count: 0
  slug: ReplayProtector
- name: ReplayProtector_string(U64)
  property_count: 0
  slug: ReplayProtector_string(U64)
- name: RequestedMultipliers
  property_count: 2
  slug: RequestedMultipliers
- name: RoleType
  property_count: 0
  slug: RoleType
- name: ScriptPayload
  property_count: 3
  slug: ScriptPayload
- name: ScriptWriteSet
  property_count: 2
  slug: ScriptWriteSet
- name: Secp256k1Ecdsa
  property_count: 1
  slug: Secp256k1Ecdsa
- name: Secp256r1Ecdsa
  property_count: 1
  slug: Secp256r1Ecdsa
- name: Signature
  property_count: 0
  slug: Signature
- name: Signature_Ed25519
  property_count: 0
  slug: Signature_Ed25519
- name: Signature_Keyless
  property_count: 0
  slug: Signature_Keyless
- name: Signature_Secp256k1Ecdsa
  property_count: 0
  slug: Signature_Secp256k1Ecdsa
- name: Signature_SlhDsa_Sha2_128s
  property_count: 0
  slug: Signature_SlhDsa_Sha2_128s
- name: Signature_WebAuthn
  property_count: 0
  slug: Signature_WebAuthn
- name: SingleKeySignature
  property_count: 2
  slug: SingleKeySignature
- name: SlhDsa_Sha2_128s
  property_count: 1
  slug: SlhDsa_Sha2_128s
- name: StakePoolOwnerLimitsRequest
  property_count: 1
  slug: StakePoolOwnerLimitsRequest
- name: StateCheckpointTransaction
  property_count: 11
  slug: StateCheckpointTransaction
- name: StateKeyWrapper
  property_count: 0
  slug: StateKeyWrapper
- name: SubmitTransactionRequest
  property_count: 8
  slug: SubmitTransactionRequest
- name: TableItemRequest
  property_count: 3
  slug: TableItemRequest
- name: Transaction
  property_count: 0
  slug: Transaction
- name: TransactionPayload
  property_count: 0
  slug: TransactionPayload
- name: TransactionPayload_DeprecatedModuleBundlePayload
  property_count: 0
  slug: TransactionPayload_DeprecatedModuleBundlePayload
- name: TransactionPayload_EncryptedTransactionPayload
  property_count: 0
  slug: TransactionPayload_EncryptedTransactionPayload
- name: TransactionPayload_EntryFunctionPayload
  property_count: 0
  slug: TransactionPayload_EntryFunctionPayload
- name: TransactionPayload_MultisigPayload
  property_count: 0
  slug: TransactionPayload_MultisigPayload
- name: TransactionPayload_ScriptPayload
  property_count: 0
  slug: TransactionPayload_ScriptPayload
- name: TransactionSignature
  property_count: 0
  slug: TransactionSignature
- name: TransactionSignature_AccountSignature
  property_count: 0
  slug: TransactionSignature_AccountSignature
- name: TransactionSignature_Ed25519Signature
  property_count: 0
  slug: TransactionSignature_Ed25519Signature
- name: TransactionSignature_FeePayerSignature
  property_count: 0
  slug: TransactionSignature_FeePayerSignature
- name: TransactionSignature_MultiAgentSignature
  property_count: 0
  slug: TransactionSignature_MultiAgentSignature
- name: TransactionSignature_MultiEd25519Signature
  property_count: 0
  slug: TransactionSignature_MultiEd25519Signature
- name: TransactionSignature_NoAccountSignature
  property_count: 0
  slug: TransactionSignature_NoAccountSignature
- name: TransactionSummary
  property_count: 4
  slug: TransactionSummary
- name: Transaction_BlockEpilogueTransaction
  property_count: 0
  slug: Transaction_BlockEpilogueTransaction
- name: Transaction_BlockMetadataTransaction
  property_count: 0
  slug: Transaction_BlockMetadataTransaction
- name: Transaction_GenesisTransaction
  property_count: 0
  slug: Transaction_GenesisTransaction
- name: Transaction_PendingTransaction
  property_count: 0
  slug: Transaction_PendingTransaction
- name: Transaction_StateCheckpointTransaction
  property_count: 0
  slug: Transaction_StateCheckpointTransaction
- name: Transaction_UserTransaction
  property_count: 0
  slug: Transaction_UserTransaction
- name: Transaction_ValidatorTransaction
  property_count: 0
  slug: Transaction_ValidatorTransaction
- name: TransactionsBatchSingleSubmissionFailure
  property_count: 2
  slug: TransactionsBatchSingleSubmissionFailure
- name: TransactionsBatchSubmissionResult
  property_count: 1
  slug: TransactionsBatchSubmissionResult
- name: U128
  property_count: 0
  slug: U128
- name: U256
  property_count: 0
  slug: U256
- name: U64
  property_count: 0
  slug: U64
- name: UnsupportedJWK
  property_count: 2
  slug: UnsupportedJWK
- name: UserTransaction
  property_count: 21
  slug: UserTransaction
- name: UserTxnLimitsRequest
  property_count: 0
  slug: UserTxnLimitsRequest
- name: UserTxnLimitsRequest_DelegatedVoterLimitsRequest
  property_count: 0
  slug: UserTxnLimitsRequest_DelegatedVoterLimitsRequest
- name: UserTxnLimitsRequest_DelegationPoolDelegatorLimitsRequest
  property_count: 0
  slug: UserTxnLimitsRequest_DelegationPoolDelegatorLimitsRequest
- name: UserTxnLimitsRequest_StakePoolOwnerLimitsRequest
  property_count: 0
  slug: UserTxnLimitsRequest_StakePoolOwnerLimitsRequest
- name: ValidatorTransaction
  property_count: 0
  slug: ValidatorTransaction
- name: ValidatorTransaction_ChunkyDKGResultTransaction
  property_count: 0
  slug: ValidatorTransaction_ChunkyDKGResultTransaction
- name: ValidatorTransaction_DKGResultTransaction
  property_count: 0
  slug: ValidatorTransaction_DKGResultTransaction
- name: ValidatorTransaction_JWKUpdateTransaction
  property_count: 0
  slug: ValidatorTransaction_JWKUpdateTransaction
- name: VersionedEvent
  property_count: 5
  slug: VersionedEvent
- name: ViewRequest
  property_count: 3
  slug: ViewRequest
- name: WebAuthn
  property_count: 1
  slug: WebAuthn
- name: WriteModule
  property_count: 3
  slug: WriteModule
- name: WriteResource
  property_count: 3
  slug: WriteResource
- name: WriteSet
  property_count: 0
  slug: WriteSet
- name: WriteSetChange
  property_count: 0
  slug: WriteSetChange
- name: WriteSetChange_DeleteModule
  property_count: 0
  slug: WriteSetChange_DeleteModule
- name: WriteSetChange_DeleteResource
  property_count: 0
  slug: WriteSetChange_DeleteResource
- name: WriteSetChange_DeleteTableItem
  property_count: 0
  slug: WriteSetChange_DeleteTableItem
- name: WriteSetChange_WriteModule
  property_count: 0
  slug: WriteSetChange_WriteModule
- name: WriteSetChange_WriteResource
  property_count: 0
  slug: WriteSetChange_WriteResource
- name: WriteSetChange_WriteTableItem
  property_count: 0
  slug: WriteSetChange_WriteTableItem
- name: WriteSetPayload
  property_count: 1
  slug: WriteSetPayload
- name: WriteSet_DirectWriteSet
  property_count: 0
  slug: WriteSet_DirectWriteSet
- name: WriteSet_ScriptWriteSet
  property_count: 0
  slug: WriteSet_ScriptWriteSet
- name: WriteTableItem
  property_count: 5
  slug: WriteTableItem
jsonld:
- class_count: 30
  name: Aptos Context
  property_count: 22
  slug: aptos-context
- class_count: 0
  name: Aptos Schema Context
  property_count: 0
  slug: aptos-schema
layout: provider
modified: '2026-06-13'
name: Aptos
nav: Providers
network: true
overview: 'Aptos publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Events API, and 4 more. Tagged areas include Blockchain, Web3, Move, Layer 1, and Cryptocurrency.


  The Aptos catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Aptos'' developer surface includes developer portal, documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Aptos Plans Pricing
  plan_count: 3
  slug: aptos-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Aptos Rate Limits
  slug: aptos-rate-limits
rules:
- name: Aptos API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aptos-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.4
  delta: -3.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 58.9
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 63.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aptos/refs/heads/main/screenshots/aptos-2026-06-20T172345.png
security:
- kind: domain-security
  name: Aptos Domain Security
  slug: aptos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aptos
tags:
- Blockchain
- Web3
- Move
- Layer 1
- Cryptocurrency
- NFT
- Smart Contracts
- DeFi
- Transactions
- Accounts
- GraphQL
- gRPC
use_cases:
- description: Query account balances, fungible asset positions, and submit swap/liquidity transactions on-chain.
  name: DeFi protocol development
- description: Use the Indexer GraphQL API to surface token collections, ownership history, and transfer events.
  name: NFT marketplace integration
- description: Subscribe to the Transaction Stream gRPC feed to build application-specific event processors.
  name: Custom blockchain indexers
- description: Fetch account resources, module states, and transaction history via the Fullnode REST API.
  name: Wallet and portfolio apps
- description: Use testnet and devnet endpoints with faucet funding before deploying to mainnet.
  name: Testing and prototyping
website: https://aptos.dev
---

---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cardano Agentic Access
  operation_count: 127
  slug: cardano-agentic-access
  summary_line: 127 operations · 6 acting
api_count: 21
apis:
- description: Blockfrost also operates as an IPFS provider, enabling developers building on Cardano to pin and retrieve content-addressed files via the InterPlanetary File System. The IPFS API base URL is https://i
  name: Blockfrost IPFS API
  slug: blockfrost-ipfs-api
- description: The Cardano » Accounts API from Cardano — 12 operation(s) for cardano » accounts.
  name: Cardano Cardano » Accounts API
  slug: cardano-cardano-accounts-api
- description: The Cardano » Addresses API from Cardano — 7 operation(s) for cardano » addresses.
  name: Cardano Cardano » Addresses API
  slug: cardano-cardano-addresses-api
- description: The Cardano » Assets API from Cardano — 7 operation(s) for cardano » assets.
  name: Cardano Cardano » Assets API
  slug: cardano-cardano-assets-api
- description: The Cardano » Blocks API from Cardano — 11 operation(s) for cardano » blocks.
  name: Cardano Cardano » Blocks API
  slug: cardano-cardano-blocks-api
- description: The Cardano » Epochs API from Cardano — 10 operation(s) for cardano » epochs.
  name: Cardano Cardano » Epochs API
  slug: cardano-cardano-epochs-api
- description: The Cardano » Governance API from Cardano — 20 operation(s) for cardano » governance.
  name: Cardano Cardano » Governance API
  slug: cardano-cardano-governance-api
- description: The Cardano » Ledger API from Cardano — 1 operation(s) for cardano » ledger.
  name: Cardano Cardano » Ledger API
  slug: cardano-cardano-ledger-api
- description: The Cardano » Mempool API from Cardano — 3 operation(s) for cardano » mempool.
  name: Cardano Cardano » Mempool API
  slug: cardano-cardano-mempool-api
- description: The Cardano » Metadata API from Cardano — 3 operation(s) for cardano » metadata.
  name: Cardano Cardano » Metadata API
  slug: cardano-cardano-metadata-api
- description: The Cardano » Network API from Cardano — 2 operation(s) for cardano » network.
  name: Cardano Cardano » Network API
  slug: cardano-cardano-network-api
- description: The Cardano » Pools API from Cardano — 12 operation(s) for cardano » pools.
  name: Cardano Cardano » Pools API
  slug: cardano-cardano-pools-api
- description: The Cardano » Scripts API from Cardano — 7 operation(s) for cardano » scripts.
  name: Cardano Cardano » Scripts API
  slug: cardano-cardano-scripts-api
- description: The Cardano » Transactions API from Cardano — 14 operation(s) for cardano » transactions.
  name: Cardano Cardano » Transactions API
  slug: cardano-cardano-transactions-api
- description: The Cardano » Utilities API from Cardano — 3 operation(s) for cardano » utilities.
  name: Cardano Cardano » Utilities API
  slug: cardano-cardano-utilities-api
- description: The Health API from Cardano — 3 operation(s) for health.
  name: Cardano Health API
  slug: cardano-health-api
- description: The IPFS » Add API from Cardano — 1 operation(s) for ipfs » add.
  name: Cardano IPFS » Add API
  slug: cardano-ipfs-add-api
- description: The IPFS » Gateway API from Cardano — 1 operation(s) for ipfs » gateway.
  name: Cardano IPFS » Gateway API
  slug: cardano-ipfs-gateway-api
- description: The IPFS » Pins API from Cardano — 4 operation(s) for ipfs » pins.
  name: Cardano IPFS » Pins API
  slug: cardano-ipfs-pins-api
- description: The Metrics API from Cardano — 2 operation(s) for metrics.
  name: Cardano Metrics API
  slug: cardano-metrics-api
- description: The Nut.link API from Cardano — 4 operation(s) for nut.link.
  name: Cardano Nut.link API
  slug: cardano-nut-link-api
artifact_total: 240
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cardano-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardano-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cardano-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://cardano.org/news/
created: '2026-06-13'
description: Cardano is a proof-of-stake blockchain platform designed for secure and scalable decentralized applications and smart contracts. Developer API access to the Cardano network is provided primarily through Blockfrost, a hosted REST API service that exposes over 100 endpoints covering transactions, addresses, assets, blocks, epochs, stake pools, governance, scripts, metadata, and mempool data. Authentication uses project-scoped API keys passed as HTTP headers. Blockfrost operates on Cardano Mainnet, Preview, and Pre-Production testnets, and also supports IPFS storage and the Milkomeda sidechain. SDKs are available for 15+ programming languages.
examples:
- key_count: 3
  name: Aggregatorfeaturesmessage Example
  slug: AggregatorFeaturesMessage-example
- key_count: 3
  name: Cardanodbbeacon Example
  slug: CardanoDbBeacon-example
- key_count: 4
  name: Cardanotransactionproofmessage Example
  slug: CardanoTransactionProofMessage-example
- key_count: 6
  name: Cardanotransactionsnapshotmessage Example
  slug: CardanoTransactionSnapshotMessage-example
- key_count: 9
  name: Certificatelistitemmessage Example
  slug: CertificateListItemMessage-example
- key_count: 6
  name: Certificatelistitemmessagemetadata Example
  slug: CertificateListItemMessageMetadata-example
- key_count: 11
  name: Certificatemessage Example
  slug: CertificateMessage-example
- key_count: 6
  name: Certificatemetadata Example
  slug: CertificateMetadata-example
- key_count: 7
  name: Certificatependingmessage Example
  slug: CertificatePendingMessage-example
- key_count: 3
  name: Epochsettingsmessage Example
  slug: EpochSettingsMessage-example
- key_count: 2
  name: Error Example
  slug: Error-example
- key_count: 6
  name: Mithrilstakedistributionmessage Example
  slug: MithrilStakeDistributionMessage-example
- key_count: 1
  name: Protocolmessage Example
  slug: ProtocolMessage-example
- key_count: 3
  name: Protocolmessageparts Example
  slug: ProtocolMessageParts-example
- key_count: 3
  name: Protocolparameters Example
  slug: ProtocolParameters-example
- key_count: 1
  name: Registersignermessage Example
  slug: RegisterSignerMessage-example
- key_count: 4
  name: Registersinglesignaturemessage Example
  slug: RegisterSingleSignatureMessage-example
- key_count: 0
  name: Signedentitytype Example
  slug: SignedEntityType-example
- key_count: 5
  name: Signer Example
  slug: Signer-example
- key_count: 1
  name: Signerregistrationslistitemmessage Example
  slug: SignerRegistrationsListItemMessage-example
- key_count: 3
  name: Signerregistrationsmessage Example
  slug: SignerRegistrationsMessage-example
- key_count: 3
  name: Signertickerlistitemmessage Example
  slug: SignerTickerListItemMessage-example
- key_count: 0
  name: Signerwithstake Example
  slug: SignerWithStake-example
- key_count: 2
  name: Signerstickersmessage Example
  slug: SignersTickersMessage-example
- key_count: 8
  name: Snapshot Example
  slug: Snapshot-example
- key_count: 6
  name: Snapshotdownloadmessage Example
  slug: SnapshotDownloadMessage-example
- key_count: 0
  name: Snapshotmessage Example
  slug: SnapshotMessage-example
- key_count: 1
  name: Stake Example
  slug: Stake-example
- key_count: 2
  name: Stakedistributionparty Example
  slug: StakeDistributionParty-example
- key_count: 4
  name: Account Addresses Total Example
  slug: account-addresses-total-example
- key_count: 12
  name: Account Content Example
  slug: account-content-example
- key_count: 5
  name: Address Content Example
  slug: address-content-example
- key_count: 5
  name: Address Content Extended Example
  slug: address-content-extended-example
- key_count: 4
  name: Address Content Total Example
  slug: address-content-total-example
- key_count: 11
  name: Asset Example
  slug: asset-example
- key_count: 5
  name: Asset Onchain Metadata Cip25 Example
  slug: asset-onchain-metadata-cip25-example
- key_count: 5
  name: Asset Onchain Metadata Cip68 Ft 333 Example
  slug: asset-onchain-metadata-cip68-ft-333-example
- key_count: 5
  name: Asset Onchain Metadata Cip68 Nft 222 Example
  slug: asset-onchain-metadata-cip68-nft-222-example
- key_count: 6
  name: Asset Onchain Metadata Cip68 Rft 444 Example
  slug: asset-onchain-metadata-cip68-rft-444-example
- key_count: 17
  name: Block Content Example
  slug: block-content-example
- key_count: 6
  name: Committee Example
  slug: committee-example
- key_count: 9
  name: Drep Example
  slug: drep-example
- key_count: 7
  name: Drep Metadata Example
  slug: drep-metadata-example
- key_count: 0
  name: Empty Object Example
  slug: empty-object-example
- key_count: 10
  name: Epoch Content Example
  slug: epoch-content-example
- key_count: 55
  name: Epoch Param Content Example
  slug: epoch-param-content-example
- key_count: 10
  name: Genesis Content Example
  slug: genesis-content-example
- key_count: 4
  name: Mempool Tx Content Example
  slug: mempool-tx-content-example
- key_count: 2
  name: Network Example
  slug: network-example
- key_count: 4
  name: Nutlink Address Example
  slug: nutlink-address-example
- key_count: 5
  name: Onchain Metadata Cip25 Example
  slug: onchain-metadata-cip25-example
- key_count: 5
  name: Onchain Metadata Cip68 Ft 333 Example
  slug: onchain-metadata-cip68-ft-333-example
- key_count: 5
  name: Onchain Metadata Cip68 Nft 222 Example
  slug: onchain-metadata-cip68-nft-222-example
- key_count: 6
  name: Onchain Metadata Cip68 Rft 444 Example
  slug: onchain-metadata-cip68-rft-444-example
- key_count: 20
  name: Pool Example
  slug: pool-example
- key_count: 9
  name: Pool Metadata Example
  slug: pool-metadata-example
- key_count: 12
  name: Proposal Example
  slug: proposal-example
- key_count: 7
  name: Proposal Metadata Example
  slug: proposal-metadata-example
- key_count: 8
  name: Proposal Metadata V2 Example
  slug: proposal-metadata-v2-example
- key_count: 4
  name: Proposal Parameters Example
  slug: proposal-parameters-example
- key_count: 1
  name: Script Cbor Example
  slug: script-cbor-example
- key_count: 1
  name: Script Datum Cbor Example
  slug: script-datum-cbor-example
- key_count: 1
  name: Script Datum Example
  slug: script-datum-example
- key_count: 3
  name: Script Example
  slug: script-example
- key_count: 1
  name: Script Json Example
  slug: script-json-example
- key_count: 1
  name: Tx Content Cbor Example
  slug: tx-content-cbor-example
- key_count: 22
  name: Tx Content Example
  slug: tx-content-example
- key_count: 3
  name: Tx Content Utxo Example
  slug: tx-content-utxo-example
- key_count: 4
  name: Utils Addresses Xpub Example
  slug: utils-addresses-xpub-example
finops:
- name: Cardano Finops
  service_category: Developer Tools
  slug: cardano-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardano.png
json_schemas:
- name: Aggregatorfeaturesmessage
  property_count: 3
  slug: AggregatorFeaturesMessage
- name: Cardanodbbeacon
  property_count: 3
  slug: CardanoDbBeacon
- name: Cardanotransactionproofmessage
  property_count: 4
  slug: CardanoTransactionProofMessage
- name: Cardanotransactionsnapshotlistmessage
  property_count: 0
  slug: CardanoTransactionSnapshotListMessage
- name: Cardanotransactionsnapshotmessage
  property_count: 6
  slug: CardanoTransactionSnapshotMessage
- name: Certificatelistitemmessage
  property_count: 9
  slug: CertificateListItemMessage
- name: Certificatelistitemmessagemetadata
  property_count: 6
  slug: CertificateListItemMessageMetadata
- name: Certificatelistmessage
  property_count: 0
  slug: CertificateListMessage
- name: Certificatemessage
  property_count: 11
  slug: CertificateMessage
- name: Certificatemetadata
  property_count: 6
  slug: CertificateMetadata
- name: Certificatependingmessage
  property_count: 7
  slug: CertificatePendingMessage
- name: Epoch
  property_count: 0
  slug: Epoch
- name: Epochsettingsmessage
  property_count: 3
  slug: EpochSettingsMessage
- name: Error
  property_count: 2
  slug: Error
- name: Mithrilstakedistributionlistmessage
  property_count: 0
  slug: MithrilStakeDistributionListMessage
- name: Mithrilstakedistributionmessage
  property_count: 6
  slug: MithrilStakeDistributionMessage
- name: Protocolmessage
  property_count: 1
  slug: ProtocolMessage
- name: Protocolmessageparts
  property_count: 3
  slug: ProtocolMessageParts
- name: Protocolparameters
  property_count: 3
  slug: ProtocolParameters
- name: Registersignermessage
  property_count: 1
  slug: RegisterSignerMessage
- name: Registersinglesignaturemessage
  property_count: 4
  slug: RegisterSingleSignatureMessage
- name: Signedentitytype
  property_count: 0
  slug: SignedEntityType
- name: Signer
  property_count: 5
  slug: Signer
- name: Signerregistrationslistitemmessage
  property_count: 1
  slug: SignerRegistrationsListItemMessage
- name: Signerregistrationsmessage
  property_count: 3
  slug: SignerRegistrationsMessage
- name: Signertickerlistitemmessage
  property_count: 3
  slug: SignerTickerListItemMessage
- name: Signerwithstake
  property_count: 0
  slug: SignerWithStake
- name: Signerstickersmessage
  property_count: 2
  slug: SignersTickersMessage
- name: Snapshot
  property_count: 8
  slug: Snapshot
- name: Snapshotdownloadmessage
  property_count: 6
  slug: SnapshotDownloadMessage
- name: Snapshotlistmessage
  property_count: 0
  slug: SnapshotListMessage
- name: Snapshotmessage
  property_count: 0
  slug: SnapshotMessage
- name: Stake
  property_count: 1
  slug: Stake
- name: Stakedistributionparty
  property_count: 2
  slug: StakeDistributionParty
- name: Account Addresses Assets
  property_count: 0
  slug: account-addresses-assets
- name: Account Addresses Content
  property_count: 0
  slug: account-addresses-content
- name: Account Addresses Total
  property_count: 4
  slug: account-addresses-total
- name: Account Content
  property_count: 12
  slug: account-content
- name: Account Delegation Content
  property_count: 0
  slug: account-delegation-content
- name: Account History Content
  property_count: 0
  slug: account-history-content
- name: Account Mir Content
  property_count: 0
  slug: account-mir-content
- name: Account Registration Content
  property_count: 0
  slug: account-registration-content
- name: Account Reward Content
  property_count: 0
  slug: account-reward-content
- name: Account Transactions Content
  property_count: 0
  slug: account-transactions-content
- name: Account Utxo Content
  property_count: 0
  slug: account-utxo-content
- name: Account Withdrawal Content
  property_count: 0
  slug: account-withdrawal-content
- name: Address Content Extended
  property_count: 5
  slug: address-content-extended
- name: Address Content Total
  property_count: 4
  slug: address-content-total
- name: Address Content
  property_count: 5
  slug: address-content
- name: Address Transactions Content
  property_count: 0
  slug: address-transactions-content
- name: Address Txs Content
  property_count: 0
  slug: address-txs-content
- name: Address Utxo Content
  property_count: 0
  slug: address-utxo-content
- name: Asset Addresses
  property_count: 0
  slug: asset-addresses
- name: Asset History
  property_count: 0
  slug: asset-history
- name: Asset Onchain Metadata Cip25
  property_count: 5
  slug: asset-onchain-metadata-cip25
- name: Asset Onchain Metadata Cip68 Ft 333
  property_count: 5
  slug: asset-onchain-metadata-cip68-ft-333
- name: Asset Onchain Metadata Cip68 Nft 222
  property_count: 5
  slug: asset-onchain-metadata-cip68-nft-222
- name: Asset Onchain Metadata Cip68 Rft 444
  property_count: 6
  slug: asset-onchain-metadata-cip68-rft-444
- name: Asset Policy
  property_count: 0
  slug: asset-policy
- name: Asset Transactions
  property_count: 0
  slug: asset-transactions
- name: Asset Txs
  property_count: 0
  slug: asset-txs
- name: Asset
  property_count: 11
  slug: asset
- name: Assets
  property_count: 0
  slug: assets
- name: Block Content Addresses
  property_count: 0
  slug: block-content-addresses
- name: Block Content Array
  property_count: 0
  slug: block-content-array
- name: Block Content Txs Cbor
  property_count: 0
  slug: block-content-txs-cbor
- name: Block Content Txs
  property_count: 0
  slug: block-content-txs
- name: Block Content
  property_count: 17
  slug: block-content
- name: Committee Votes
  property_count: 0
  slug: committee-votes
- name: Committee
  property_count: 6
  slug: committee
- name: Drep Delegators
  property_count: 0
  slug: drep-delegators
- name: Drep Metadata
  property_count: 7
  slug: drep-metadata
- name: Drep Updates
  property_count: 0
  slug: drep-updates
- name: Drep Votes
  property_count: 0
  slug: drep-votes
- name: Drep
  property_count: 9
  slug: drep
- name: Dreps
  property_count: 0
  slug: dreps
- name: Empty Object
  property_count: 0
  slug: empty-object
- name: Epoch Block Content
  property_count: 0
  slug: epoch-block-content
- name: Epoch Content Array
  property_count: 0
  slug: epoch-content-array
- name: Epoch Content
  property_count: 10
  slug: epoch-content
- name: Epoch Param Content
  property_count: 56
  slug: epoch-param-content
- name: Epoch Stake Content
  property_count: 0
  slug: epoch-stake-content
- name: Epoch Stake Pool Content
  property_count: 0
  slug: epoch-stake-pool-content
- name: Genesis Content
  property_count: 10
  slug: genesis-content
- name: Mempool Addresses Content
  property_count: 0
  slug: mempool-addresses-content
- name: Mempool Content
  property_count: 0
  slug: mempool-content
- name: Mempool Tx Content
  property_count: 4
  slug: mempool-tx-content
- name: Metrics Endpoints
  property_count: 0
  slug: metrics-endpoints
- name: Metrics
  property_count: 0
  slug: metrics
- name: Network-Eras
  property_count: 0
  slug: network-eras
- name: Network
  property_count: 2
  slug: network
- name: Nutlink Address Ticker
  property_count: 0
  slug: nutlink-address-ticker
- name: Nutlink Address Tickers
  property_count: 0
  slug: nutlink-address-tickers
- name: Nutlink Address
  property_count: 4
  slug: nutlink-address
- name: Nutlink Tickers Ticker
  property_count: 0
  slug: nutlink-tickers-ticker
- name: Onchain Metadata Cip25
  property_count: 0
  slug: onchain-metadata-cip25
- name: Onchain Metadata Cip68 Ft 333
  property_count: 0
  slug: onchain-metadata-cip68-ft-333
- name: Onchain Metadata Cip68 Nft 222
  property_count: 0
  slug: onchain-metadata-cip68-nft-222
- name: Onchain Metadata Cip68 Rft 444
  property_count: 0
  slug: onchain-metadata-cip68-rft-444
- name: Pool Blocks
  property_count: 0
  slug: pool-blocks
- name: Pool Delegators
  property_count: 0
  slug: pool-delegators
- name: Pool History
  property_count: 0
  slug: pool-history
- name: Pool List Extended
  property_count: 0
  slug: pool-list-extended
- name: Pool List Retire
  property_count: 0
  slug: pool-list-retire
- name: Pool List
  property_count: 0
  slug: pool-list
- name: Pool Metadata
  property_count: 9
  slug: pool-metadata
- name: Pool Relays
  property_count: 0
  slug: pool-relays
- name: Pool Updates
  property_count: 0
  slug: pool-updates
- name: Pool Votes
  property_count: 0
  slug: pool-votes
- name: Pool
  property_count: 20
  slug: pool
- name: Proposal Metadata V2
  property_count: 8
  slug: proposal-metadata-v2
- name: Proposal Metadata
  property_count: 7
  slug: proposal-metadata
- name: Proposal Parameters
  property_count: 4
  slug: proposal-parameters
- name: Proposal Votes
  property_count: 0
  slug: proposal-votes
- name: Proposal Withdrawals
  property_count: 0
  slug: proposal-withdrawals
- name: Proposal
  property_count: 12
  slug: proposal
- name: Proposals
  property_count: 0
  slug: proposals
- name: Script Cbor
  property_count: 1
  slug: script-cbor
- name: Script Datum Cbor
  property_count: 1
  slug: script-datum-cbor
- name: Script Datum
  property_count: 1
  slug: script-datum
- name: Script Json
  property_count: 1
  slug: script-json
- name: Script Redeemers
  property_count: 0
  slug: script-redeemers
- name: Script
  property_count: 3
  slug: script
- name: Scripts
  property_count: 0
  slug: scripts
- name: Tx Content Cbor
  property_count: 1
  slug: tx-content-cbor
- name: Tx Content Delegations
  property_count: 0
  slug: tx-content-delegations
- name: Tx Content Metadata Cbor
  property_count: 0
  slug: tx-content-metadata-cbor
- name: Tx Content Metadata
  property_count: 0
  slug: tx-content-metadata
- name: Tx Content Mirs
  property_count: 0
  slug: tx-content-mirs
- name: Tx Content Pool Certs
  property_count: 0
  slug: tx-content-pool-certs
- name: Tx Content Pool Retires
  property_count: 0
  slug: tx-content-pool-retires
- name: Tx Content Redeemers
  property_count: 0
  slug: tx-content-redeemers
- name: Tx Content Required Signers
  property_count: 0
  slug: tx-content-required-signers
- name: Tx Content Stake Addr
  property_count: 0
  slug: tx-content-stake-addr
- name: Tx Content Utxo
  property_count: 3
  slug: tx-content-utxo
- name: Tx Content Withdrawals
  property_count: 0
  slug: tx-content-withdrawals
- name: Tx Content
  property_count: 23
  slug: tx-content
- name: Tx Metadata Label Cbor
  property_count: 0
  slug: tx-metadata-label-cbor
- name: Tx Metadata Label Json
  property_count: 0
  slug: tx-metadata-label-json
- name: Tx Metadata Labels
  property_count: 0
  slug: tx-metadata-labels
- name: Utils Addresses Xpub
  property_count: 4
  slug: utils-addresses-xpub
jsonld:
- class_count: 0
  name: Blockfrost Cardano Api Context
  property_count: 0
  slug: blockfrost-cardano-api
- class_count: 145
  name: Blockfrost Cardano Context
  property_count: 113
  slug: blockfrost-cardano-context
layout: provider
modified: '2026-06-13'
name: Cardano
nav: Providers
network: true
overview: 'Cardano publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Cardano » Accounts API, Cardano » Addresses API, Cardano » Assets API, and 17 more. Tagged areas include Blockchain, Cryptocurrency, Proof-of-Stake, Smart Contracts, and Web3.


  The Cardano catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Cardano''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Cardano Plans Pricing
  plan_count: 4
  slug: cardano-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 6
  name: Cardano Rate Limits
  slug: cardano-rate-limits
rules:
- name: Cardano API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cardano-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.1
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.4
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardano/refs/heads/main/screenshots/cardano-2026-06-20T173952.png
security:
- kind: authentication
  name: Cardano Authentication
  slug: cardano-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cardano Domain Security
  slug: cardano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cardano
tags:
- Blockchain
- Cryptocurrency
- Proof-of-Stake
- Smart Contracts
- Web3
---

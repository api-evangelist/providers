---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 459
  human_in_the_loop: 0
  name: Chainstack Agentic Access
  operation_count: 757
  slug: chainstack-agentic-access
  summary_line: 757 operations · 459 acting
api_count: 26
apis:
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: Public Chainstack-operated testnet faucet for Hoodi, Sepolia, BNB Testnet, zkSync Testnet, Scroll Sepolia, and Polygon Amoy. JWT-authenticated POST /v1/faucet/{chain} request endpoint plus a transacti
  name: Chainstack Faucet API
  slug: chainstack-faucet-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Account Info API from Chainstack — 6 operation(s) for account info.
  name: Chainstack Account Info API
  slug: chainstack-account-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Accounts Info API from Chainstack — 6 operation(s) for accounts info.
  name: Chainstack Accounts Info API
  slug: chainstack-accounts-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Blocks Info API from Chainstack — 13 operation(s) for blocks info.
  name: Chainstack Blocks Info API
  slug: chainstack-blocks-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Chain Info API from Chainstack — 5 operation(s) for chain info.
  name: Chainstack Chain Info API
  slug: chainstack-chain-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Client Info API from Chainstack — 5 operation(s) for client info.
  name: Chainstack Client Info API
  slug: chainstack-client-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Configuration Info API from Chainstack — 5 operation(s) for configuration info.
  name: Chainstack Configuration Info API
  slug: chainstack-configuration-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Debug And Trace API from Chainstack — 37 operation(s) for debug and trace.
  name: Chainstack Debug And Trace API
  slug: chainstack-debug-and-trace-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Debug API from Chainstack — 3 operation(s) for debug.
  name: Chainstack Debug API
  slug: chainstack-debug-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Deployment Options API from Chainstack — 1 operation(s) for deployment options.
  name: Chainstack Deployment Options API
  slug: chainstack-deployment-options-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Events API from Chainstack — 1 operation(s) for events.
  name: Chainstack Events API
  slug: chainstack-events-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Execute Transactions API from Chainstack — 6 operation(s) for execute transactions.
  name: Chainstack Execute Transactions API
  slug: chainstack-execute-transactions-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Filter Handling API from Chainstack — 5 operation(s) for filter handling.
  name: Chainstack Filter Handling API
  slug: chainstack-filter-handling-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Gas Data API from Chainstack — 5 operation(s) for gas data.
  name: Chainstack Gas Data API
  slug: chainstack-gas-data-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The General API from Chainstack — 520 operation(s) for general.
  name: Chainstack General API
  slug: chainstack-general-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Logs And Events API from Chainstack — 3 operation(s) for logs and events.
  name: Chainstack Logs And Events API
  slug: chainstack-logs-and-events-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Network API from Chainstack — 2 operation(s) for network.
  name: Chainstack Network API
  slug: chainstack-network-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Node API from Chainstack — 2 operation(s) for node.
  name: Chainstack Node API
  slug: chainstack-node-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Node V2 API from Chainstack — 2 operation(s) for node v2.
  name: Chainstack Node V2 API
  slug: chainstack-node-v2-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Organization API from Chainstack — 1 operation(s) for organization.
  name: Chainstack Organization API
  slug: chainstack-organization-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Project API from Chainstack — 3 operation(s) for project.
  name: Chainstack Project API
  slug: chainstack-project-api
- baseURL: https://api.chainstack.com
  baseurl_source: spec
  description: The Project V2 API from Chainstack — 2 operation(s) for project v2.
  name: Chainstack Project V2 API
  slug: chainstack-project-v2-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The State API from Chainstack — 10 operation(s) for state.
  name: Chainstack State API
  slug: chainstack-state-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Tempo Specific API from Chainstack — 2 operation(s) for tempo specific.
  name: Chainstack Tempo Specific API
  slug: chainstack-tempo-specific-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Transaction Info API from Chainstack — 14 operation(s) for transaction info.
  name: Chainstack Transaction Info API
  slug: chainstack-transaction-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Txpool API from Chainstack — 2 operation(s) for txpool.
  name: Chainstack Txpool API
  slug: chainstack-txpool-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Validatiors Info API from Chainstack — 12 operation(s) for validatiors info.
  name: Chainstack Validatiors Info API
  slug: chainstack-validatiors-info-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Zkevm Methods API from Chainstack — 8 operation(s) for zkevm methods.
  name: Chainstack Zkevm Methods API
  slug: chainstack-zkevm-methods-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The DetectAddress API from Chainstack — 1 operation(s) for detectaddress.
  name: Chainstack Detect Address API
  slug: chainstack-detectaddress-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The EstimateFee API from Chainstack — 1 operation(s) for estimatefee.
  name: Chainstack Estimate Fee API
  slug: chainstack-estimatefee-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetAccountInfo API from Chainstack — 1 operation(s) for getaccountinfo.
  name: Chainstack Get Account Info API
  slug: chainstack-getaccountinfo-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetAccountStates API from Chainstack — 1 operation(s) for getaccountstates.
  name: Chainstack Get Account States API
  slug: chainstack-getaccountstates-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetActions API from Chainstack — 1 operation(s) for getactions.
  name: Chainstack Get Actions API
  slug: chainstack-getactions-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetAddressBalance API from Chainstack — 1 operation(s) for getaddressbalance.
  name: Chainstack Get Address Balance API
  slug: chainstack-getaddressbalance-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetAddressBookInfo API from Chainstack — 1 operation(s) for getaddressbookinfo.
  name: Chainstack Get Address Book Info API
  slug: chainstack-getaddressbookinfo-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetAddressInformation API from Chainstack — 1 operation(s) for getaddressinformation.
  name: Chainstack Get Address Information API
  slug: chainstack-getaddressinformation-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetAddressState API from Chainstack — 1 operation(s) for getaddressstate.
  name: Chainstack Get Address State API
  slug: chainstack-getaddressstate-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetAdjacentTransactions API from Chainstack — 1 operation(s) for getadjacenttransactions.
  name: Chainstack Get Adjacent Transactions API
  slug: chainstack-getadjacenttransactions-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetBlockHeader API from Chainstack — 1 operation(s) for getblockheader.
  name: Chainstack Get Block Header API
  slug: chainstack-getblockheader-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetBlocks API from Chainstack — 1 operation(s) for getblocks.
  name: Chainstack Get Blocks API
  slug: chainstack-getblocks-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetBlockTransactions API from Chainstack — 1 operation(s) for getblocktransactions.
  name: Chainstack Get Block Transactions API
  slug: chainstack-getblocktransactions-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetBlockTransactionsExt API from Chainstack — 1 operation(s) for getblocktransactionsext.
  name: Chainstack Get Block Transactions Ext API
  slug: chainstack-getblocktransactionsext-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetConfigParam API from Chainstack — 1 operation(s) for getconfigparam.
  name: Chainstack Get Config Param API
  slug: chainstack-getconfigparam-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetConsensusBlock API from Chainstack — 1 operation(s) for getconsensusblock.
  name: Chainstack Get Consensus Block API
  slug: chainstack-getconsensusblock-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetEvents API from Chainstack — 1 operation(s) for getevents.
  name: Chainstack Get Events API
  slug: chainstack-getevents-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetExtendedAddressInformation API from Chainstack — 1 operation(s) for getextendedaddressinformation.
  name: Chainstack Get Extended Address Information API
  slug: chainstack-getextendedaddressinformation-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetJettonBurns API from Chainstack — 1 operation(s) for getjettonburns.
  name: Chainstack Get Jetton Burns API
  slug: chainstack-getjettonburns-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetJettonMasters API from Chainstack — 1 operation(s) for getjettonmasters.
  name: Chainstack Get Jetton Masters API
  slug: chainstack-getjettonmasters-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetJettonTransfers API from Chainstack — 1 operation(s) for getjettontransfers.
  name: Chainstack Get Jetton Transfers API
  slug: chainstack-getjettontransfers-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetJettonWallets API from Chainstack — 1 operation(s) for getjettonwallets.
  name: Chainstack Get Jetton Wallets API
  slug: chainstack-getjettonwallets-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMasterchainBlockShards API from Chainstack — 1 operation(s) for getmasterchainblockshards.
  name: Chainstack Get Masterchain Block Shards API
  slug: chainstack-getmasterchainblockshards-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMasterchainBlockShardState API from Chainstack — 1 operation(s) for getmasterchainblockshardstate.
  name: Chainstack Get Masterchain Block Shard State API
  slug: chainstack-getmasterchainblockshardstate-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMasterchainBlockSignatures API from Chainstack — 1 operation(s) for getmasterchainblocksignatures.
  name: Chainstack Get Masterchain Block Signatures API
  slug: chainstack-getmasterchainblocksignatures-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMasterchainInfo API from Chainstack — 1 operation(s) for getmasterchaininfo.
  name: Chainstack Get Masterchain Info API
  slug: chainstack-getmasterchaininfo-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMessages API from Chainstack — 1 operation(s) for getmessages.
  name: Chainstack Get Messages API
  slug: chainstack-getmessages-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMetadata API from Chainstack — 1 operation(s) for getmetadata.
  name: Chainstack Get Metadata API
  slug: chainstack-getmetadata-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMultisigOrders API from Chainstack — 1 operation(s) for getmultisigorders.
  name: Chainstack Get Multisig Orders API
  slug: chainstack-getmultisigorders-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetMultisigWallets API from Chainstack — 1 operation(s) for getmultisigwallets.
  name: Chainstack Get Multisig Wallets API
  slug: chainstack-getmultisigwallets-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetNFTCollections API from Chainstack — 1 operation(s) for getnftcollections.
  name: Chainstack Get NFT Collections API
  slug: chainstack-getnftcollections-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetNFTItems API from Chainstack — 1 operation(s) for getnftitems.
  name: Chainstack Get NFT Items API
  slug: chainstack-getnftitems-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetNFTTransfers API from Chainstack — 1 operation(s) for getnfttransfers.
  name: Chainstack Get NFT Transfers API
  slug: chainstack-getnfttransfers-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetPendingTraces API from Chainstack — 1 operation(s) for getpendingtraces.
  name: Chainstack Get Pending Traces API
  slug: chainstack-getpendingtraces-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetPendingTransactions API from Chainstack — 1 operation(s) for getpendingtransactions.
  name: Chainstack Get Pending Transactions API
  slug: chainstack-getpendingtransactions-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetShardBlockProof API from Chainstack — 1 operation(s) for getshardblockproof.
  name: Chainstack Get Shard Block Proof API
  slug: chainstack-getshardblockproof-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetTokenData API from Chainstack — 1 operation(s) for gettokendata.
  name: Chainstack Get Token Data API
  slug: chainstack-gettokendata-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetTopAccountsByBalance API from Chainstack — 1 operation(s) for gettopaccountsbybalance.
  name: Chainstack Get Top Accounts By Balance API
  slug: chainstack-gettopaccountsbybalance-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetTraces API from Chainstack — 1 operation(s) for gettraces.
  name: Chainstack Get Traces API
  slug: chainstack-gettraces-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetTransactions API from Chainstack — 1 operation(s) for gettransactions.
  name: Chainstack Get Transactions API
  slug: chainstack-gettransactions-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetTransactionsByMasterchainBlock API from Chainstack — 1 operation(s) for gettransactionsbymasterchainblock.
  name: Chainstack Get Transactions By Masterchain Block API
  slug: chainstack-gettransactionsbymasterchainblock-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetTransactionsByMessage API from Chainstack — 1 operation(s) for gettransactionsbymessage.
  name: Chainstack Get Transactions By Message API
  slug: chainstack-gettransactionsbymessage-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetWalletInfo API from Chainstack — 1 operation(s) for getwalletinfo.
  name: Chainstack Get Wallet Info API
  slug: chainstack-getwalletinfo-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetWalletInformation API from Chainstack — 1 operation(s) for getwalletinformation.
  name: Chainstack Get Wallet Information API
  slug: chainstack-getwalletinformation-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The GetWalletStates API from Chainstack — 1 operation(s) for getwalletstates.
  name: Chainstack Get Wallet States API
  slug: chainstack-getwalletstates-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The JsonRPC API from Chainstack — 1 operation(s) for jsonrpc.
  name: Chainstack JSON RPC API
  slug: chainstack-jsonrpc-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The LookupBlock API from Chainstack — 1 operation(s) for lookupblock.
  name: Chainstack Lookup Block API
  slug: chainstack-lookupblock-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The PackAddress API from Chainstack — 1 operation(s) for packaddress.
  name: Chainstack Pack Address API
  slug: chainstack-packaddress-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The RunGetMethod API from Chainstack — 1 operation(s) for rungetmethod.
  name: Chainstack Run Get Method API
  slug: chainstack-rungetmethod-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The SendBoc API from Chainstack — 1 operation(s) for sendboc.
  name: Chainstack Send Boc API
  slug: chainstack-sendboc-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The SendBocReturnHash API from Chainstack — 1 operation(s) for sendbocreturnhash.
  name: Chainstack Send Boc Return Hash API
  slug: chainstack-sendbocreturnhash-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The SendMessage API from Chainstack — 1 operation(s) for sendmessage.
  name: Chainstack Send Message API
  slug: chainstack-sendmessage-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The SendQuery API from Chainstack — 1 operation(s) for sendquery.
  name: Chainstack Send Query API
  slug: chainstack-sendquery-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Shards API from Chainstack — 1 operation(s) for shards.
  name: Chainstack Shards API
  slug: chainstack-shards-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The TryLocateResultTx API from Chainstack — 1 operation(s) for trylocateresulttx.
  name: Chainstack Try Locate Result Tx API
  slug: chainstack-trylocateresulttx-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The TryLocateSourceTx API from Chainstack — 1 operation(s) for trylocatesourcetx.
  name: Chainstack Try Locate Source Tx API
  slug: chainstack-trylocatesourcetx-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The TryLocateTx API from Chainstack — 1 operation(s) for trylocatetx.
  name: Chainstack Try Locate Tx API
  slug: chainstack-trylocatetx-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The UnpackAddress API from Chainstack — 1 operation(s) for unpackaddress.
  name: Chainstack Unpack Address API
  slug: chainstack-unpackaddress-api
- baseURL_template: https://{node_id}.p2pify.com/{api_key}
  baseurl_source: spec_template
  description: The Vesting API from Chainstack — 1 operation(s) for vesting.
  name: Chainstack Vesting API
  slug: chainstack-vesting-api
- baseURL: https://api.chainstack.com
  baseurl_source: declared
  description: The Marketplace API from Chainstack — 1 operation(s) for marketplace.
  name: Chainstack Marketplace API
  slug: chainstack-marketplace-api
artifact_total: 192
asyncapis:
- description: AsyncAPI 2.6 specification for Chainstack's JSON-RPC WebSocket (WSS) subscription APIs. Chainstack-managed nodes expose a persistent WebSocket endpoint per node that accepts JSON-RPC 2.0 messages. Cli
  name: Chainstack RPC WebSocket APIs
  slug: chainstack-asyncapi
collections:
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info API
  slug: postman-chainstack-account-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Accounts Info API
  slug: postman-chainstack-accounts-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Blocks Info API
  slug: postman-chainstack-blocks-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Chain Info API
  slug: postman-chainstack-chain-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Client Info API
  slug: postman-chainstack-client-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Configuration Info API
  slug: postman-chainstack-configuration-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Debug And Trace API
  slug: postman-chainstack-debug-and-trace-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Debug API
  slug: postman-chainstack-debug-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Deployment Options API
  slug: postman-chainstack-deployment-options-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Events API
  slug: postman-chainstack-events-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Execute Transactions API
  slug: postman-chainstack-execute-transactions-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info faucet API
  slug: postman-chainstack-faucet-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Filter Handling API
  slug: postman-chainstack-filter-handling-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Gas Data API
  slug: postman-chainstack-gas-data-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info General API
  slug: postman-chainstack-general-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info History API
  slug: postman-chainstack-history-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Logs And Events API
  slug: postman-chainstack-logs-and-events-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Network API
  slug: postman-chainstack-network-api
- collection_type: postman
  name: Chainstack Arbitrum Account Info Node API
  slug: postman-chainstack-node-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Node V2 API
  slug: postman-chainstack-node-v2-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Organization API
  slug: postman-chainstack-organization-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Project API
  slug: postman-chainstack-project-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Project V2 API
  slug: postman-chainstack-project-v2-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info State API
  slug: postman-chainstack-state-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Tempo Specific API
  slug: postman-chainstack-tempo-specific-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Transaction Info API
  slug: postman-chainstack-transaction-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Transactions Info API
  slug: postman-chainstack-transactions-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Txpool API
  slug: postman-chainstack-txpool-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info V2 API
  slug: postman-chainstack-v2-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info V3 API
  slug: postman-chainstack-v3-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Validatiors Info API
  slug: postman-chainstack-validatiors-info-api
- collection_type: postman
  name: Chainstack Arbitrum Node Account Info Zkevm Methods API
  slug: postman-chainstack-zkevm-methods-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info API
  slug: open-chainstack-account-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Accounts Info API
  slug: open-chainstack-accounts-info-api
- collection_type: open
  name: Chainstack Arbitrum Node API
  slug: open-chainstack-arbitrum-node-api
- collection_type: open
  name: Chainstack Aurora Node API
  slug: open-chainstack-aurora-node-api
- collection_type: open
  name: Chainstack Avalanche Node API
  slug: open-chainstack-avalanche-node-api
- collection_type: open
  name: Chainstack Base Node API
  slug: open-chainstack-base-node-api
- collection_type: open
  name: Chainstack Bitcoin Node API
  slug: open-chainstack-bitcoin-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Blocks Info API
  slug: open-chainstack-blocks-info-api
- collection_type: open
  name: Chainstack BNB Smart Chain Node API
  slug: open-chainstack-bnb-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Chain Info API
  slug: open-chainstack-chain-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Client Info API
  slug: open-chainstack-client-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Configuration Info API
  slug: open-chainstack-configuration-info-api
- collection_type: open
  name: Chainstack Cronos Node API
  slug: open-chainstack-cronos-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Debug And Trace API
  slug: open-chainstack-debug-and-trace-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Debug API
  slug: open-chainstack-debug-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Deployment Options API
  slug: open-chainstack-deployment-options-api
- collection_type: open
  name: Chainstack Ethereum Beacon Chain API
  slug: open-chainstack-ethereum-beacon-chain-api
- collection_type: open
  name: Chainstack Ethereum Node API
  slug: open-chainstack-ethereum-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Events API
  slug: open-chainstack-events-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Execute Transactions API
  slug: open-chainstack-execute-transactions-api
- collection_type: open
  name: Chainstack Fantom Node API
  slug: open-chainstack-fantom-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info faucet API
  slug: open-chainstack-faucet-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Filter Handling API
  slug: open-chainstack-filter-handling-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Gas Data API
  slug: open-chainstack-gas-data-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info General API
  slug: open-chainstack-general-api
- collection_type: open
  name: Chainstack Gnosis Node API
  slug: open-chainstack-gnosis-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info History API
  slug: open-chainstack-history-api
- collection_type: open
  name: Chainstack Hyperliquid Node API
  slug: open-chainstack-hyperliquid-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Logs And Events API
  slug: open-chainstack-logs-and-events-api
- collection_type: open
  name: Chainstack Monad Node API
  slug: open-chainstack-monad-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Network API
  slug: open-chainstack-network-api
- collection_type: open
  name: Chainstack Arbitrum Account Info Node API
  slug: open-chainstack-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Node V2 API
  slug: open-chainstack-node-v2-api
- collection_type: open
  name: Chainstack Optimism Node API
  slug: open-chainstack-optimism-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Organization API
  slug: open-chainstack-organization-api
- collection_type: open
  name: Chainstack Plasma Node API
  slug: open-chainstack-plasma-node-api
- collection_type: open
  name: 💙 CHAINSTACK PLATFORM API
  slug: open-chainstack-platform-api
- collection_type: open
  name: Chainstack Polygon Node API
  slug: open-chainstack-polygon-node-api
- collection_type: open
  name: Chainstack Polygon zkEVM Node API
  slug: open-chainstack-polygon-zkevm-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Project API
  slug: open-chainstack-project-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Project V2 API
  slug: open-chainstack-project-v2-api
- collection_type: open
  name: Chainstack Ronin Node API
  slug: open-chainstack-ronin-node-api
- collection_type: open
  name: Chainstack Solana Node API
  slug: open-chainstack-solana-node-api
- collection_type: open
  name: Chainstack Starknet Node API
  slug: open-chainstack-starknet-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info State API
  slug: open-chainstack-state-api
- collection_type: open
  name: Chainstack Tempo Node API
  slug: open-chainstack-tempo-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Tempo Specific API
  slug: open-chainstack-tempo-specific-api
- collection_type: open
  name: Chainstack TON Node API
  slug: open-chainstack-ton-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Transaction Info API
  slug: open-chainstack-transaction-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Transactions Info API
  slug: open-chainstack-transactions-info-api
- collection_type: open
  name: Chainstack TRON Node API
  slug: open-chainstack-tron-node-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Txpool API
  slug: open-chainstack-txpool-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info V2 API
  slug: open-chainstack-v2-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info V3 API
  slug: open-chainstack-v3-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Validatiors Info API
  slug: open-chainstack-validatiors-info-api
- collection_type: open
  name: Chainstack Arbitrum Node Account Info Zkevm Methods API
  slug: open-chainstack-zkevm-methods-api
- collection_type: open
  name: Chainstack zkSync Era Node API
  slug: open-chainstack-zksync-node-api
common:
- group: commercial
  href: https://artifacts.apis.io/chainstack/plans/chainstack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chainstack-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/chainstack/capabilities/chainstack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/chainstack-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/chainstack/overview
- group: agent
  href: https://artifacts.apis.io/chainstack/agentic-access/chainstack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chainstack-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chainstack/security/chainstack-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chainstack-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chainstack/security/chainstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainstack-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chainstack/authentication/chainstack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chainstack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chainstack/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/chainstackhq
- group: build
  title: ''
  type: Github
  url: https://github.com/chainstack
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/Cymtg2f7pX
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Chainstack
- group: company
  title: ''
  type: Website
  url: https://chainstack.com
- group: start
  title: ''
  type: Portal
  url: https://docs.chainstack.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/reference/platform-api-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/reference/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.chainstack.com/docs/about-limits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/docs/about-billing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainstack.com/docs/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://chainstack.com/pricing/
- group: other
  title: ''
  type: Faucet
  url: https://faucet.chainstack.com/
- group: operate
  title: ''
  type: Support
  url: https://support.chainstack.com
- group: other
  title: ''
  type: Feedback
  url: https://ideas.chainstack.com/
- group: company
  title: ''
  type: Blog
  url: https://chainstack.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://chainstack.com/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://chainstack.status.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chainstack.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chainstack.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://chainstack.com/security/
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/dev-portal
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/erigon
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/bsc-erigon
- group: other
  title: ''
  type: Source
  url: https://github.com/chainstack/op-erigon
- group: build
  title: ''
  type: Tools
  url: https://github.com/chainstack/solana-exporter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/solana-rpc-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/multichaincli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/bitcoincli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chainstack/web3quorum
- group: build
  title: ''
  type: Tools
  url: https://github.com/chainstack/terraform-openstack-rke2
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/global-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/dedicated-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/unlimited-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/trader-nodes/
- group: other
  title: ''
  type: Product
  url: https://chainstack.com/products/yellowstone-grpc/
- group: docs
  title: ''
  type: Documentation
  url: https://chainstack.com/build-better/
- group: design
  href: https://artifacts.apis.io/chainstack/vocabulary/chainstack-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chainstack-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chainstack/rules/chainstack-rules.yml
  title: ''
  type: SpectralRules
  url: rules/chainstack-rules.yml
- group: commercial
  href: https://artifacts.apis.io/chainstack/finops/chainstack-finops.yml
  title: ''
  type: FinOps
  url: finops/chainstack-finops.yml
description: Chainstack is a managed multi-chain RPC and node infrastructure platform supporting 70+ blockchain protocols including Ethereum, Solana, Bitcoin, BNB Smart Chain, Polygon, Arbitrum, Optimism, Base, Avalanche, TON, TRON, Starknet, zkSync Era, Hyperliquid, Monad, and many more. The platform exposes a REST Platform API for organization, project, network, and node lifecycle management, JSON-RPC endpoints for every supported chain, a Faucet API for testnet funding, real- time Solana streaming via Yellowstone gRPC, low-latency Trader Nodes via bloXroute, archive data with debug and trace namespaces, MEV protection, Flashblocks preconfirmations, and a Chainstack MCP server for AI agents.
finops:
- has_sources: true
  method: derived
  name: Chainstack Finops
  primary_unit: support plan
  service_category: ''
  slug: chainstack-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chainstack.png
json_schemas:
- name: ChainstackJsonRpcEnvelope
  property_count: 0
  slug: chainstack-jsonrpc-envelope
- name: ChainstackNode
  property_count: 11
  slug: chainstack-node
jsonld:
- class_count: 0
  name: Chainstack Context
  property_count: 8
  slug: chainstack-context
layout: provider
modified: 2026-05-29 00:00:00+00:00
name: Chainstack
nav: Providers
network: true
overview: 'Chainstack publishes 88 API contracts indexed on the [APIs.io](https://apis.io/) network, including Faucet API, Account Info API, Accounts Info API, and 85 more. Tagged areas include Blockchain, Multi-Chain, RPC, Node Infrastructure, and Web3.


  The Chainstack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Chainstack''s developer surface includes authentication, GitHub presence, YouTube channel, developer portal, documentation, pricing, support, and 41 more developer resources.'
plans:
- name: Chainstack Plans Pricing
  plan_count: 15
  slug: chainstack-plans-pricing
- name: Chainstack Price Estimates
  plan_count: 0
  slug: chainstack-price-estimates
random_paper: 17
rate_limits:
- limit_count: 10
  name: Chainstack Rate Limits
  slug: chainstack-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Chainstack — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: chainstack-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Chainstack — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: chainstack-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Chainstack API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: chainstack-rules
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 73.0
    catalog_earned_first_party: 12.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 27.3
    contract_quality: 60.6
    developer_ergonomics: 56.0
    discoverability: 57.1
    operational_transparency: 50.0
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 98
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chainstack/chainstack-2026-06-20T174203.png
security:
- kind: authentication
  name: Chainstack Authentication
  slug: chainstack-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Chainstack Domain Security
  slug: chainstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chainstack Vulnerability Disclosure
  slug: chainstack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chainstack
tags:
- Blockchain
- Multi-Chain
- RPC
- Node Infrastructure
- Web3
- Cryptocurrency
- Ethereum
- Solana
- Bitcoin
- DeFi
- MEV
- Trader Node
- Archive Data
- MCP
- AI Agents
- Real-Time
website: https://chainstack.com
---

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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cosmos Agentic Access
  operation_count: 109
  slug: cosmos-agentic-access
  summary_line: 109 operations · 6 acting
api_count: 2
apis:
- description: The Query API from Cosmos — 89 operation(s) for query.
  name: Cosmos Query API
  slug: cosmos-query-api
- description: The Service API from Cosmos — 19 operation(s) for service.
  name: Cosmos Service API
  slug: cosmos-service-api
artifact_total: 85
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cosmos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cosmos-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cosmos
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cosmos/cosmos-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cosmos.network
- group: docs
  title: ''
  type: OpenAPI
  url: https://cosmos.github.io/cosmos-sdk/openapi.html
- group: docs
  title: ''
  type: SwaggerUI
  url: https://localhost:1317/swagger
- group: operate
  title: ''
  type: Forums
  url: https://forum.cosmos.network
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/interchain
- group: company
  title: ''
  type: Blog
  url: https://blog.cosmos.network
- group: other
  title: ''
  type: X
  url: https://x.com/cosmosecosystem
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cosmos.network/privacy
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/cosmos/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/cosmos/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/cosmos/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Cosmos is an interoperable blockchain ecosystem providing a modular framework (Cosmos SDK) for building sovereign, high-performance application-specific blockchains. The Cosmos SDK exposes LCD (Light Client Daemon) REST APIs on port 1317, generated automatically via gRPC-gateway from Protobuf definitions. These endpoints cover accounts, balances, transactions, governance proposals, staking delegations, IBC transfers, minting, distribution, and ABCI app data. The Cosmos Hub (cosmoshub-4) is the flagship chain; the same API surface is shared by 150+ chains in the ecosystem.
examples:
- key_count: 3
  name: Cosmos Auth V1Beta1
  slug: cosmos-auth-v1beta1
- key_count: 3
  name: Cosmos Authz V1Beta1
  slug: cosmos-authz-v1beta1
- key_count: 3
  name: Cosmos Bank V1Beta1
  slug: cosmos-bank-v1beta1
- key_count: 3
  name: Cosmos Base Node
  slug: cosmos-base-node
- key_count: 3
  name: Cosmos Base Tendermint
  slug: cosmos-base-tendermint
- key_count: 3
  name: Cosmos Consensus V1
  slug: cosmos-consensus-v1
- key_count: 3
  name: Cosmos Distribution V1Beta1
  slug: cosmos-distribution-v1beta1
- key_count: 3
  name: Cosmos Epochs V1Beta1
  slug: cosmos-epochs-v1beta1
- key_count: 3
  name: Cosmos Evidence V1Beta1
  slug: cosmos-evidence-v1beta1
- key_count: 3
  name: Cosmos Feegrant V1Beta1
  slug: cosmos-feegrant-v1beta1
- key_count: 3
  name: Cosmos Gov V1
  slug: cosmos-gov-v1
- key_count: 3
  name: Cosmos Gov V1Beta1
  slug: cosmos-gov-v1beta1
- key_count: 3
  name: Cosmos Mint V1Beta1
  slug: cosmos-mint-v1beta1
- key_count: 3
  name: Cosmos Slashing V1Beta1
  slug: cosmos-slashing-v1beta1
- key_count: 3
  name: Cosmos Staking V1Beta1
  slug: cosmos-staking-v1beta1
- key_count: 3
  name: Cosmos Tx V1Beta1
  slug: cosmos-tx-v1beta1
- key_count: 3
  name: Cosmos Upgrade V1Beta1
  slug: cosmos-upgrade-v1beta1
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cosmos.png
json_schemas:
- name: Cosmos SDK cosmos.auth.v1beta1 Schemas
  property_count: 0
  slug: cosmos-auth-v1beta1
- name: Cosmos SDK cosmos.authz.v1beta1 Schemas
  property_count: 0
  slug: cosmos-authz-v1beta1
- name: Cosmos SDK cosmos.bank.v1beta1 Schemas
  property_count: 0
  slug: cosmos-bank-v1beta1
- name: Cosmos SDK cosmos.base.abci Schemas
  property_count: 0
  slug: cosmos-base-abci
- name: Cosmos SDK cosmos.base.node Schemas
  property_count: 0
  slug: cosmos-base-node
- name: Cosmos SDK cosmos.base.query Schemas
  property_count: 0
  slug: cosmos-base-query
- name: Cosmos SDK cosmos.base.tendermint Schemas
  property_count: 0
  slug: cosmos-base-tendermint
- name: Cosmos SDK cosmos.base.v1beta1 Schemas
  property_count: 0
  slug: cosmos-base-v1beta1
- name: Cosmos SDK cosmos.consensus.v1 Schemas
  property_count: 0
  slug: cosmos-consensus-v1
- name: Cosmos SDK cosmos.crypto.multisig Schemas
  property_count: 0
  slug: cosmos-crypto-multisig
- name: Cosmos SDK cosmos.distribution.v1beta1 Schemas
  property_count: 0
  slug: cosmos-distribution-v1beta1
- name: Cosmos SDK cosmos.epochs.v1beta1 Schemas
  property_count: 0
  slug: cosmos-epochs-v1beta1
- name: Cosmos SDK cosmos.evidence.v1beta1 Schemas
  property_count: 0
  slug: cosmos-evidence-v1beta1
- name: Cosmos SDK cosmos.feegrant.v1beta1 Schemas
  property_count: 0
  slug: cosmos-feegrant-v1beta1
- name: Cosmos SDK cosmos.gov.v1 Schemas
  property_count: 0
  slug: cosmos-gov-v1
- name: Cosmos SDK cosmos.gov.v1beta1 Schemas
  property_count: 0
  slug: cosmos-gov-v1beta1
- name: Cosmos SDK cosmos.mint.v1beta1 Schemas
  property_count: 0
  slug: cosmos-mint-v1beta1
- name: Cosmos SDK cosmos.slashing.v1beta1 Schemas
  property_count: 0
  slug: cosmos-slashing-v1beta1
- name: Cosmos SDK cosmos.staking.v1beta1 Schemas
  property_count: 0
  slug: cosmos-staking-v1beta1
- name: Cosmos SDK cosmos.tx.signing Schemas
  property_count: 0
  slug: cosmos-tx-signing
- name: Cosmos SDK cosmos.tx.v1beta1 Schemas
  property_count: 0
  slug: cosmos-tx-v1beta1
- name: Cosmos SDK cosmos.upgrade.v1beta1 Schemas
  property_count: 0
  slug: cosmos-upgrade-v1beta1
- name: Cosmos SDK google.protobuf.Any Schemas
  property_count: 0
  slug: google-protobuf-Any
- name: Cosmos SDK google.rpc.Status Schemas
  property_count: 0
  slug: google-rpc-Status
- name: Cosmos SDK tendermint.abci.Event Schemas
  property_count: 0
  slug: tendermint-abci-Event
- name: Cosmos SDK tendermint.abci.EventAttribute Schemas
  property_count: 0
  slug: tendermint-abci-EventAttribute
- name: Cosmos SDK tendermint.abci.ExecTxResult Schemas
  property_count: 0
  slug: tendermint-abci-ExecTxResult
- name: Cosmos SDK tendermint.abci.ValidatorUpdate Schemas
  property_count: 0
  slug: tendermint-abci-ValidatorUpdate
- name: Cosmos SDK tendermint.crypto.PublicKey Schemas
  property_count: 0
  slug: tendermint-crypto-PublicKey
- name: Cosmos SDK tendermint.p2p.DefaultNodeInfo Schemas
  property_count: 0
  slug: tendermint-p2p-DefaultNodeInfo
- name: Cosmos SDK tendermint.p2p.DefaultNodeInfoOther Schemas
  property_count: 0
  slug: tendermint-p2p-DefaultNodeInfoOther
- name: Cosmos SDK tendermint.p2p.ProtocolVersion Schemas
  property_count: 0
  slug: tendermint-p2p-ProtocolVersion
- name: Cosmos SDK tendermint.types.ABCIParams Schemas
  property_count: 0
  slug: tendermint-types-ABCIParams
- name: Cosmos SDK tendermint.types.AuthorityParams Schemas
  property_count: 0
  slug: tendermint-types-AuthorityParams
- name: Cosmos SDK tendermint.types.Block Schemas
  property_count: 0
  slug: tendermint-types-Block
- name: Cosmos SDK tendermint.types.BlockID Schemas
  property_count: 0
  slug: tendermint-types-BlockID
- name: Cosmos SDK tendermint.types.BlockIDFlag Schemas
  property_count: 0
  slug: tendermint-types-BlockIDFlag
- name: Cosmos SDK tendermint.types.BlockParams Schemas
  property_count: 0
  slug: tendermint-types-BlockParams
- name: Cosmos SDK tendermint.types.Commit Schemas
  property_count: 0
  slug: tendermint-types-Commit
- name: Cosmos SDK tendermint.types.CommitSig Schemas
  property_count: 0
  slug: tendermint-types-CommitSig
- name: Cosmos SDK tendermint.types.ConsensusParams Schemas
  property_count: 0
  slug: tendermint-types-ConsensusParams
- name: Cosmos SDK tendermint.types.Data Schemas
  property_count: 0
  slug: tendermint-types-Data
- name: Cosmos SDK tendermint.types.DuplicateVoteEvidence Schemas
  property_count: 0
  slug: tendermint-types-DuplicateVoteEvidence
- name: Cosmos SDK tendermint.types.Evidence Schemas
  property_count: 0
  slug: tendermint-types-Evidence
- name: Cosmos SDK tendermint.types.EvidenceList Schemas
  property_count: 0
  slug: tendermint-types-EvidenceList
- name: Cosmos SDK tendermint.types.EvidenceParams Schemas
  property_count: 0
  slug: tendermint-types-EvidenceParams
- name: Cosmos SDK tendermint.types.Header Schemas
  property_count: 0
  slug: tendermint-types-Header
- name: Cosmos SDK tendermint.types.LightBlock Schemas
  property_count: 0
  slug: tendermint-types-LightBlock
- name: Cosmos SDK tendermint.types.LightClientAttackEvidence Schemas
  property_count: 0
  slug: tendermint-types-LightClientAttackEvidence
- name: Cosmos SDK tendermint.types.PartSetHeader Schemas
  property_count: 0
  slug: tendermint-types-PartSetHeader
- name: Cosmos SDK tendermint.types.SignedHeader Schemas
  property_count: 0
  slug: tendermint-types-SignedHeader
- name: Cosmos SDK tendermint.types.SignedMsgType Schemas
  property_count: 0
  slug: tendermint-types-SignedMsgType
- name: Cosmos SDK tendermint.types.Validator Schemas
  property_count: 0
  slug: tendermint-types-Validator
- name: Cosmos SDK tendermint.types.ValidatorParams Schemas
  property_count: 0
  slug: tendermint-types-ValidatorParams
- name: Cosmos SDK tendermint.types.ValidatorSet Schemas
  property_count: 0
  slug: tendermint-types-ValidatorSet
- name: Cosmos SDK tendermint.types.VersionParams Schemas
  property_count: 0
  slug: tendermint-types-VersionParams
- name: Cosmos SDK tendermint.types.Vote Schemas
  property_count: 0
  slug: tendermint-types-Vote
- name: Cosmos SDK tendermint.version.Consensus Schemas
  property_count: 0
  slug: tendermint-version-Consensus
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 11
  name: context Context
  property_count: 17
  slug: context
layout: provider
modified: '2026-06-13'
name: Cosmos
nav: Providers
network: true
overview: 'Cosmos publishes 2 APIs on the [APIs.io](https://apis.io/) network: Query API and Service API. Tagged areas include Blockchain, Cosmos, IBC, Staking, and Governance.


  The Cosmos catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Cosmos'' developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Cosmos API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cosmos-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.2
  delta: -6.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cosmos/refs/heads/main/screenshots/cosmos-2026-06-20T175049.png
security:
- kind: domain-security
  name: Cosmos Domain Security
  slug: cosmos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosmos
tags:
- Blockchain
- Cosmos
- IBC
- Staking
- Governance
- DeFi
- Web3
---

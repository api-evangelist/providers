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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Uniblock Agentic Access
  operation_count: 27
  slug: uniblock-agentic-access
  summary_line: 27 operations · 3 acting
api_count: 2
apis:
- description: The Uniblock JSON-RPC API provides a single endpoint for standard JSON-RPC calls across hundreds of blockchain networks. Rather than managing individual node provider connections for each chain, devel
  name: Uniblock JSON-RPC API
  slug: json-rpc-api
- description: Pass-through endpoints that proxy requests directly to upstream blockchain data providers such as Alchemy, SimpleHash, TonAPI, Moralis, Covalent, Helius, Solscan, and others.
  name: Uniblock Direct Pass-Through API
  slug: uniblock-direct-pass-through-api
- description: Endpoints for real-time and historical market data including token prices, market capitalization, trading volume, trending tokens, and charting data from multiple exchanges.
  name: Uniblock Market Data API
  slug: uniblock-market-data-api
- description: Endpoints for retrieving non-fungible token data including balances, metadata, transfers, and collection information.
  name: Uniblock NFTs API
  slug: uniblock-nfts-api
- description: Endpoints for scanning blockchain networks for transactions, transfers, native supply, and block-level data similar to block explorers.
  name: Uniblock Scan API
  slug: uniblock-scan-api
- description: Endpoints for retrieving fungible token data including metadata, balances, prices, transfers, and allowances across multiple blockchain networks.
  name: Uniblock Tokens API
  slug: uniblock-tokens-api
- description: Endpoints for looking up transaction data by address or transaction hash, including detailed transaction information.
  name: Uniblock Transactions API
  slug: uniblock-transactions-api
artifact_total: 34
asyncapis:
- description: Uniblock webhooks enable real-time notifications for blockchain events without the need to poll endpoints. By configuring webhooks through the Uniblock dashboard or API, developers can receive HTTP ca
  name: Uniblock Webhook Events
  slug: uniblock-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uniblock Direct API
  slug: open-uniblock-direct-api
- collection_type: open
  name: Uniblock Direct Direct Pass-Through API
  slug: open-uniblock-direct-pass-through-api
- collection_type: open
  name: Uniblock Direct Direct Pass-Through JSON-RPC API
  slug: open-uniblock-json-rpc-api
- collection_type: open
  name: Uniblock Direct Direct Pass-Through Market Data API
  slug: open-uniblock-market-data-api
- collection_type: open
  name: Uniblock Direct Direct Pass-Through NFTs API
  slug: open-uniblock-nfts-api
- collection_type: open
  name: Uniblock Direct Direct Pass-Through Scan API
  slug: open-uniblock-scan-api
- collection_type: open
  name: Uniblock Direct Direct Pass-Through Tokens API
  slug: open-uniblock-tokens-api
- collection_type: open
  name: Uniblock Direct Direct Pass-Through Transactions API
  slug: open-uniblock-transactions-api
- collection_type: open
  name: Uniblock Unified API
  slug: open-uniblock-unified-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uniblock-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uniblock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uniblock-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uniblock-dapp
- group: design
  title: ''
  type: JSONLD
  url: json-ld/uniblock-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uniblock-token-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uniblock-nft-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uniblock-transaction-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uniblock-webhook-event-schema.json
- group: company
  title: ''
  type: Website
  url: https://uniblock.dev/
- group: start
  title: ''
  type: Portal
  url: https://docs.uniblock.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uniblock.dev/docs/welcome-to-uniblock
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.uniblock.dev/docs/uniblock-quickstart-guide
- group: company
  title: ''
  type: Blog
  url: https://www.uniblock.dev/blog
- group: other
  title: ''
  type: Chains
  url: https://www.uniblock.dev/chains
- group: start
  title: ''
  type: Login
  url: https://app.uniblock.dev/
- group: design
  title: ''
  type: SpectralRules
  url: rules/uniblock-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uniblock-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.uniblock.dev/llms.txt
created: '2025-02-08'
description: Uniblock is a Web3 infrastructure platform that provides a standardized API aggregating data from hundreds of DEXs and cross-chain bridges, abstracting the complexity of multi-chain development into a single endpoint. The platform completed $5.2 million in financing with $7.5 million in total funding.
examples:
- key_count: 3
  name: Uniblock Get Token Metadata Example
  slug: uniblock-get-token-metadata-example
finops:
- name: Uniblock Finops
  service_category: Web3 Infrastructure
  slug: uniblock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uniblock.png
json_schemas:
- name: Uniblock NFT
  property_count: 9
  slug: uniblock-nft
- name: Uniblock Token
  property_count: 7
  slug: uniblock-token
- name: Uniblock Transaction
  property_count: 12
  slug: uniblock-transaction
- name: Uniblock Webhook Event
  property_count: 2
  slug: uniblock-webhook-event
json_structures:
- name: Uniblock Token Structure
  property_count: 0
  slug: uniblock-token-structure
jsonld:
- class_count: 0
  name: Uniblock Context
  property_count: 7
  slug: uniblock-context
layout: provider
modified: '2026-05-19'
name: Uniblock
nav: Providers
network: true
overview: 'Uniblock publishes 7 APIs on the [APIs.io](https://apis.io/) network, including JSON-RPC API, Direct Pass-Through API, Market Data API, and 4 more. Tagged areas include Blockchain and Web3.


  The Uniblock catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Uniblock''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Uniblock Plans Pricing
  plan_count: 5
  slug: uniblock-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Uniblock Rate Limits
  slug: uniblock-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Uniblock API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: uniblock-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Uniblock API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: uniblock-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Uniblock API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: uniblock-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 28.8
    contract_quality: 70.3
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uniblock/refs/heads/main/screenshots/uniblock-2026-06-20T200030.png
security:
- kind: authentication
  name: Uniblock Authentication
  slug: uniblock-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uniblock Domain Security
  slug: uniblock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uniblock
tags:
- Blockchain
- Web3
website: https://uniblock.dev/
---

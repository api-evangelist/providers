---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Axelar Agentic Access
  operation_count: 9
  slug: axelar-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- description: Retrieves information about the Axelar network and the AXL token. Provides access to metrics such as circulating supply, total supply, inflation, total value locked (TVL) across 80+ chains and 30+ ass
  name: Axelarscan API
  slug: axelarscan
- description: Exposes metrics for validators operating on the Axelar network, including heartbeat status, uptime percentages, proposed block counts, voting participation, and quadratic voting scores. Useful for del
  name: Axelar Validator API
  slug: validator
- description: Provides insights into cross-chain token transfers executed through the Axelar network. Returns transfer status, source and destination chain details, asset denomination, amounts, confirmation counts,
  name: Axelar Token Transfer API
  slug: token-transfer
- description: Returns information about General Message Passing (GMP) calls routed through the Axelar network. Provides transaction status, source and destination chain data, contract call payloads, gas payment sta
  name: Axelar GMP API
  slug: gmp
- description: JavaScript/TypeScript SDK wrapping common cross-chain operations on the Axelar network. Key classes include AxelarAssetTransfer (generates deposit addresses for token transfers), AxelarQueryAPI (fee e
  name: AxelarJS SDK
  slug: axelarjs-sdk
- baseURL: https://api.axelarscan.io/api
  baseurl_source: declared
  description: The Chains API from Axelar — 3 operation(s) for chains.
  name: Axelar Chains API
  slug: axelar-chains-api
- baseURL: https://api.axelarscan.io/api
  baseurl_source: declared
  description: The Contracts API from Axelar — 3 operation(s) for contracts.
  name: Axelar Contracts API
  slug: axelar-contracts-api
- baseURL: https://api.axelarscan.io/api
  baseurl_source: declared
  description: The Health API from Axelar — 1 operation(s) for health.
  name: Axelar Health API
  slug: axelar-health-api
- baseURL: https://api.axelarscan.io/api
  baseurl_source: declared
  description: The Payloads API from Axelar — 2 operation(s) for payloads.
  name: Axelar Payloads API
  slug: axelar-payloads-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amplifier GMP Chains API
  slug: open-axelar-chains-api
- collection_type: open
  name: Amplifier GMP Chains Contracts API
  slug: open-axelar-contracts-api
- collection_type: open
  name: Amplifier GMP Chains Health API
  slug: open-axelar-health-api
- collection_type: open
  name: Amplifier GMP Chains Payloads API
  slug: open-axelar-payloads-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/axelarnetwork/axelarjs-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/axelarnetwork/axelarjs-sdk/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/axelarnetwork/axelarjs-sdk/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/axelar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axelar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axelar.network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axelar.dev/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/axelarnetwork
- group: other
  title: ''
  type: Explorer
  url: https://axelarscan.io/
- group: docs
  title: ''
  type: APIDocumentation
  url: https://docs.axelarscan.io/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/aRZ3Ra6f7D
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/axelar
- group: company
  title: ''
  type: Blog
  url: https://axelar.network/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/axelar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/axelar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/axelar-finops.yml
created: '2026-06-13'
description: Axelar is a decentralized cross-chain communication network that enables secure interoperability across 80+ blockchains including EVM chains, Cosmos, Solana, Sui, Stellar, and XRPL. The network provides General Message Passing (GMP) for arbitrary cross-chain contract calls, the Interchain Token Service (ITS) for deploying and bridging tokens across chains, and the Axelarscan API suite for querying network state, validator metrics, token transfer status, and GMP transaction data. Developer tooling includes the AxelarJS SDK, the Mobius Development Stack (MDS), and Axelar Virtual Machine (AVM).
examples:
- key_count: 3
  name: Broadcast Contract Request
  slug: broadcast-contract-request
- key_count: 3
  name: Get Tasks Response
  slug: get-tasks-response
- key_count: 3
  name: Publish Events Request
  slug: publish-events-request
finops:
- name: Axelar Finops
  service_category: Blockchain Infrastructure
  slug: axelar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axelar.png
json_schemas:
- name: Amplifier GMP API Schemas
  property_count: 0
  slug: amplifier-gmp-api
layout: provider
modified: '2026-06-13'
name: Axelar
nav: Providers
network: true
overview: 'Axelar publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chains API, Contracts API, Health API, and 1 more. Tagged areas include Blockchain, Cross-Chain, Interoperability, Web3, and General Message Passing.


  The Axelar catalog on APIs.io includes 1 Spectral governance ruleset.


  Axelar''s developer surface includes documentation, GitHub presence, engineering blog, and 13 more developer resources.'
plans:
- name: Axelar Plans Pricing
  plan_count: 2
  slug: axelar-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Axelar Rate Limits
  slug: axelar-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Axelar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: axelar-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 44.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 25.0
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axelar/refs/heads/main/screenshots/axelar-2026-06-20T172905.png
security:
- kind: domain-security
  name: Axelar Domain Security
  slug: axelar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: axelar
tags:
- Blockchain
- Cross-Chain
- Interoperability
- Web3
- General Message Passing
- Token Bridge
- Cosmos
- EVM
website: https://axelar.network/
---

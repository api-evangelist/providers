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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 69
  human_in_the_loop: 0
  name: Pokt Agentic Access
  operation_count: 123
  slug: pokt-agentic-access
  summary_line: 123 operations · 69 acting
api_count: 3
apis:
- description: Cosmos SDK-based REST and gRPC API for interacting with the Pocket Network Shannon protocol chain. Provides endpoints for querying applications, suppliers, sessions, gateways, proofs, and tokenomics p
  name: Pocket Network Shannon Chain API
  slug: pocket-network-shannon-chain-api
- description: PATH (Pocket API and Toolkit Harness) is an open-source framework for deploying permissionless gateways on top of Pocket Network. Exposes health, readiness, and Prometheus metrics endpoints for gatewa
  name: Pocket Network PATH Gateway API
  slug: pocket-network-path-gateway-api
- description: PATH API endpoints
  name: Pocket Network API API
  slug: pokt-api-api
- description: The Msg API from Pocket Network — 34 operation(s) for msg.
  name: Pocket Network Msg API
  slug: pokt-msg-api
- description: The Query API from Pocket Network — 26 operation(s) for query.
  name: Pocket Network Query API
  slug: pokt-query-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PATH - Path & Toolkit Harness API API
  slug: open-pokt-api-api
- collection_type: open
  name: PATH - Path & Toolkit Harness API Msg API
  slug: open-pokt-msg-api
- collection_type: open
  name: PATH - Path & Toolkit Harness API Query API
  slug: open-pokt-query-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pokt-network/poktroll/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/pokt-network/poktroll/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/pokt-network/poktroll/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pokt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pokt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pocket.network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pocket.network/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pokt-network/
- group: operate
  title: ''
  type: Forums
  url: https://forum.pokt.network/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/pokt
- group: company
  title: ''
  type: Blog
  url: https://pocket.network/blog/
- group: other
  title: ''
  type: Explorer
  url: https://explorer.pokt.network/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pocket.network/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pocket.network/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://pocketnetwork.statuspage.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://pocket.network/save-on-rpc-path/
- group: commercial
  title: ''
  type: Plans
  url: https://github.com/api-evangelist/pokt/blob/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://github.com/api-evangelist/pokt/blob/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://github.com/api-evangelist/pokt/blob/main/finops/finops.yml
created: '2026-06-13'
description: Pocket Network is a decentralized, permissionless RPC infrastructure network providing free public API access to 60+ blockchain chains including Ethereum, Avalanche, Polygon, Solana, and other EVM-compatible and non-EVM networks. The Shannon upgrade (June 2025) made Pocket the first open, permissionless API network where anyone can stake POKT tokens to deploy gateways and supply nodes without centralized approval.
examples:
- key_count: 4
  name: Eth_Blocknumber
  slug: eth_blockNumber
- key_count: 4
  name: Eth_Call
  slug: eth_call
- key_count: 4
  name: Path_Healthz
  slug: path_healthz
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://pocket.network/wp-content/uploads/2024/03/pocket-logo.png
json_schemas:
- name: Application represents the onchain definition and state of an application
  property_count: 7
  slug: pocket_application_Application
- name: pocket.gateway.Gateway
  property_count: 3
  slug: pocket_gateway_Gateway
- name: pocket.proof.Proof
  property_count: 3
  slug: pocket_proof_Proof
- name: pocket.session.Session
  property_count: 6
  slug: pocket_session_Session
- name: Service message to encapsulate unique and semantic identifiers for a service on the network
  property_count: 5
  slug: pocket_shared_Service
- name: Supplier represents an actor in Pocket Network that provides RPC services
  property_count: 6
  slug: pocket_shared_Supplier
- name: SupplierEndpoint message to hold service configuration details
  property_count: 3
  slug: pocket_shared_SupplierEndpoint
- name: SupplierServiceConfig holds the service configuration the supplier stakes for
  property_count: 3
  slug: pocket_shared_SupplierServiceConfig
- name: pocket.tokenomics.Params
  property_count: 4
  slug: pocket_tokenomics_Params
- name: ServiceID
  property_count: 0
  slug: serviceid
jsonld:
- class_count: 4
  name: context Context
  property_count: 19
  slug: context
layout: provider
modified: '2026-06-13'
name: Pocket Network
nav: Providers
network: true
overview: 'Pocket Network publishes 3 APIs on the [APIs.io](https://apis.io/) network: API API, Msg API, and Query API. Tagged areas include Blockchain, RPC, Decentralized, Web3, and Ethereum.


  The Pocket Network catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pocket Network''s developer surface includes documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pocket Network API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pokt-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 49.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 55.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pokt/refs/heads/main/screenshots/pokt-2026-06-20T191847.png
security:
- kind: domain-security
  name: Pokt Domain Security
  slug: pokt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pokt
tags:
- Blockchain
- RPC
- Decentralized
- Web3
- Ethereum
- EVM
- Infrastructure
website: https://pocket.network/
---

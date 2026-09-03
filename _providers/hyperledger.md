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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hyperledger Agentic Access
  operation_count: 1
  slug: hyperledger-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Hyperledger Fabric is a permissioned distributed ledger platform. Programmatic access is provided via the Fabric Gateway, peer gRPC APIs, and SDKs for chaincode invocation, ledger queries, and channel
  name: Hyperledger Fabric API
  slug: hyperledger-fabric-api
- description: Hyperledger FireFly is a multiparty system orchestration framework providing REST APIs for tokens, messages, identities, contracts, and events across multiple blockchain protocols.
  name: Hyperledger FireFly API
  slug: hyperledger-firefly-api
- description: Hyperledger Indy provides tools, libraries, and reusable components for decentralized identities rooted on blockchains. APIs are exposed via the Indy SDK and Indy Node REST endpoints.
  name: Hyperledger Indy API
  slug: hyperledger-indy-api
- description: Hyperledger Cacti (formerly Cactus) is a pluggable enterprise-grade framework for cross-chain transactions, providing connector plugins and REST APIs for interoperability across DLTs.
  name: Hyperledger Cacti API
  slug: hyperledger-cacti-api
- baseURL: https://besu.example.com
  baseurl_source: declared
  description: Standard Ethereum JSON-RPC methods.
  name: Hyperledger Eth API
  slug: hyperledger-eth-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hyperledger Besu JSON-RPC Eth API
  slug: open-hyperledger-eth-api
- collection_type: open
  name: Hyperledger Besu JSON-RPC API
  slug: open-hyperledger
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperledger-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperledger-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperledger-project
- group: docs
  title: ''
  type: Documentation
  url: https://www.hyperledger.org/use
- group: auth
  title: ''
  type: LFDecentralizedTrust
  url: https://lfdecentralizedtrust.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/hyperledger
- group: build
  title: ''
  type: LFDTGitHub
  url: https://github.com/LF-Decentralized-Trust
- group: other
  title: ''
  type: Wiki
  url: https://wiki.lfdecentralizedtrust.org/
- group: company
  title: ''
  type: Blog
  url: https://www.lfdecentralizedtrust.org/blog/rss.xml
created: '2026-03-16'
description: Hyperledger is an open source collaborative effort created to advance cross-industry blockchain technologies, originally hosted under the Linux Foundation and now stewarded by LF Decentralized Trust. It hosts enterprise-grade blockchain frameworks including Fabric, Besu, Indy, Iroha, and Cacti, along with tools like Firefly and Caliper for blockchain development, identity, and operations.
finops:
- name: Hyperledger Finops
  service_category: Blockchain & Distributed Ledger
  slug: hyperledger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperledger.png
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: hyperledger-jsonrpcrequest
- name: JsonRpcResponse
  property_count: 4
  slug: hyperledger-jsonrpcresponse
json_structures:
- name: Hyperledger Structure
  property_count: 0
  slug: hyperledger-structure
layout: provider
modified: '2026-05-19'
name: Hyperledger
nav: Providers
network: true
overview: 'Hyperledger publishes 1 API on the [APIs.io](https://apis.io/) network: Eth API. Tagged areas include Blockchain, Distributed Ledger, Enterprise, Linux Foundation, and Smart Contracts.


  The Hyperledger catalog on APIs.io includes 1 Spectral governance ruleset.


  Hyperledger''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Hyperledger Plans Pricing
  plan_count: 3
  slug: hyperledger-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Hyperledger Rate Limits
  slug: hyperledger-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Hyperledger API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hyperledger-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 70.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 46.3
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 25.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperledger/refs/heads/main/screenshots/hyperledger-2026-06-20T183044.png
security:
- kind: domain-security
  name: Hyperledger Domain Security
  slug: hyperledger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperledger
tags:
- Blockchain
- Distributed Ledger
- Enterprise
- Linux Foundation
- Smart Contracts
---

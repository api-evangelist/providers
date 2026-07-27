---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 152
  human_in_the_loop: 1
  name: Ipfs Agentic Access
  operation_count: 154
  slug: ipfs-agentic-access
  summary_line: 154 operations · 152 acting · 1 human-in-the-loop
api_count: 40
apis:
- description: The IPFS HTTP Gateway API is an implementation-agnostic interface for retrieving content-addressed data from IPFS over standard HTTP. Path gateways expose /ipfs/{cid} and /ipns/{name} namespaces, supp
  name: IPFS HTTP Gateway API
  slug: ipfs-http-gateway-api
- description: The Delegated Routing V1 HTTP API allows IPFS clients to offload content routing, peer routing, and IPNS resolution to a remote server without running a full DHT node. Endpoints include provider looku
  name: IPFS Delegated Routing V1 HTTP API
  slug: ipfs-delegated-routing-v1-http-api
- description: The Add API from IPFS — 1 operation(s) for add.
  name: IPFS Add API
  slug: ipfs-add-api
- description: The Bitswap API from IPFS — 4 operation(s) for bitswap.
  name: IPFS Bitswap API
  slug: ipfs-bitswap-api
- description: The Block API from IPFS — 4 operation(s) for block.
  name: IPFS Block API
  slug: ipfs-block-api
- description: The Bootstrap API from IPFS — 6 operation(s) for bootstrap.
  name: IPFS Bootstrap API
  slug: ipfs-bootstrap-api
- description: The Cat API from IPFS — 1 operation(s) for cat.
  name: IPFS Cat API
  slug: ipfs-cat-api
- description: The Cid API from IPFS — 5 operation(s) for cid.
  name: IPFS Cid API
  slug: ipfs-cid-api
- description: The Commands API from IPFS — 1 operation(s) for commands.
  name: IPFS Commands API
  slug: ipfs-commands-api
- description: The Config API from IPFS — 4 operation(s) for config.
  name: IPFS Config API
  slug: ipfs-config-api
- description: The Dag API from IPFS — 6 operation(s) for dag.
  name: IPFS Dag API
  slug: ipfs-dag-api
- description: The Dht API from IPFS — 6 operation(s) for dht.
  name: IPFS Dht API
  slug: ipfs-dht-api
- description: The Diag API from IPFS — 5 operation(s) for diag.
  name: IPFS Diag API
  slug: ipfs-diag-api
- description: The Dns API from IPFS — 1 operation(s) for dns.
  name: IPFS Dns API
  slug: ipfs-dns-api
- description: The File API from IPFS — 1 operation(s) for file.
  name: IPFS File API
  slug: ipfs-file-api
- description: The Files API from IPFS — 10 operation(s) for files.
  name: IPFS Files API
  slug: ipfs-files-api
- description: The Filestore API from IPFS — 3 operation(s) for filestore.
  name: IPFS Filestore API
  slug: ipfs-filestore-api
- description: The Get API from IPFS — 1 operation(s) for get.
  name: IPFS Get API
  slug: ipfs-get-api
- description: The Id API from IPFS — 1 operation(s) for id.
  name: IPFS Id API
  slug: ipfs-id-api
- description: The Key API from IPFS — 5 operation(s) for key.
  name: IPFS Key API
  slug: ipfs-key-api
- description: The Log API from IPFS — 3 operation(s) for log.
  name: IPFS Log API
  slug: ipfs-log-api
- description: The Ls API from IPFS — 1 operation(s) for ls.
  name: IPFS Ls API
  slug: ipfs-ls-api
- description: The Mount API from IPFS — 1 operation(s) for mount.
  name: IPFS Mount API
  slug: ipfs-mount-api
- description: The Multibase API from IPFS — 4 operation(s) for multibase.
  name: IPFS Multibase API
  slug: ipfs-multibase-api
- description: The Name API from IPFS — 6 operation(s) for name.
  name: IPFS Name API
  slug: ipfs-name-api
- description: The Object API from IPFS — 11 operation(s) for object.
  name: IPFS Object API
  slug: ipfs-object-api
- description: The P2p API from IPFS — 6 operation(s) for p2p.
  name: IPFS P2p API
  slug: ipfs-p2p-api
- description: The Pin API from IPFS — 11 operation(s) for pin.
  name: IPFS Pin API
  slug: ipfs-pin-api
- description: The Ping API from IPFS — 1 operation(s) for ping.
  name: IPFS Ping API
  slug: ipfs-ping-api
- description: The pins API from IPFS — 2 operation(s) for pins.
  name: IPFS pins API
  slug: ipfs-pins-api
- description: The Pubsub API from IPFS — 4 operation(s) for pubsub.
  name: IPFS Pubsub API
  slug: ipfs-pubsub-api
- description: The Refs API from IPFS — 2 operation(s) for refs.
  name: IPFS Refs API
  slug: ipfs-refs-api
- description: The Repo API from IPFS — 5 operation(s) for repo.
  name: IPFS Repo API
  slug: ipfs-repo-api
- description: The Resolve API from IPFS — 1 operation(s) for resolve.
  name: IPFS Resolve API
  slug: ipfs-resolve-api
- description: The Routing API from IPFS — 5 operation(s) for routing.
  name: IPFS Routing API
  slug: ipfs-routing-api
- description: The Shutdown API from IPFS — 1 operation(s) for shutdown.
  name: IPFS Shutdown API
  slug: ipfs-shutdown-api
- description: The Stats API from IPFS — 5 operation(s) for stats.
  name: IPFS Stats API
  slug: ipfs-stats-api
- description: The Swarm API from IPFS — 13 operation(s) for swarm.
  name: IPFS Swarm API
  slug: ipfs-swarm-api
- description: The Tar API from IPFS — 2 operation(s) for tar.
  name: IPFS Tar API
  slug: ipfs-tar-api
- description: The Version API from IPFS — 2 operation(s) for version.
  name: IPFS Version API
  slug: ipfs-version-api
artifact_total: 62
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ipfs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipfs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ipfs-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.ipfs.tech/index.xml
created: '2026-06-13'
description: InterPlanetary File System (IPFS) is a peer-to-peer hypermedia protocol and distributed content-addressed storage system. The Kubo implementation exposes an HTTP RPC API (/api/v0/) for adding, pinning, and retrieving content-addressed files, managing DAG (Directed Acyclic Graph) nodes, key management, and network peer operations. The HTTP Gateway API provides read-only access to IPFS and IPNS content over standard HTTP. The Delegated Routing V1 HTTP API enables clients to discover content providers and resolve peer records without running a full DHT node.
examples:
- key_count: 117
  name: Ipfs Kubo Rpc Examples
  slug: ipfs-kubo-rpc-examples
- key_count: 4
  name: Ipfs Pinning Service Schema Examples
  slug: ipfs-pinning-service-schema-examples
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://ipfs.tech/images/ipfs-logo.svg
json_schemas:
- name: Delegates
  property_count: 0
  slug: delegates
- name: Failure
  property_count: 1
  slug: failure
- name: Kubo Rpc Responses
  property_count: 0
  slug: kubo-rpc-responses
- name: Origins
  property_count: 0
  slug: origins
- name: Pin
  property_count: 4
  slug: pin
- name: PinMeta
  property_count: 0
  slug: pinmeta
- name: PinResults
  property_count: 2
  slug: pinresults
- name: PinStatus
  property_count: 6
  slug: pinstatus
- name: Status
  property_count: 0
  slug: status
- name: StatusInfo
  property_count: 0
  slug: statusinfo
- name: TextMatchingStrategy
  property_count: 0
  slug: textmatchingstrategy
jsonld:
- class_count: 30
  name: Ipfs Context
  property_count: 2
  slug: ipfs-context
- class_count: 0
  name: Ipfs Provider Context
  property_count: 0
  slug: ipfs-provider
layout: provider
modified: '2026-06-13'
name: IPFS
nav: Providers
network: true
overview: 'IPFS publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Add API, Bitswap API, Block API, and 35 more. Tagged areas include IPFS, Distributed Storage, Content-Addressed, Decentralized, and Peer-to-Peer.


  The IPFS catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  IPFS''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 26
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: IPFS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ipfs-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.7
    developer_ergonomics: 13.0
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 40.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ipfs/refs/heads/main/screenshots/ipfs-2026-06-20T183549.png
security:
- kind: authentication
  name: Ipfs Authentication
  slug: ipfs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ipfs Domain Security
  slug: ipfs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ipfs
tags:
- IPFS
- Distributed Storage
- Content-Addressed
- Decentralized
- Peer-to-Peer
- File Storage
- DAG
- Pinning
- Gateway
---

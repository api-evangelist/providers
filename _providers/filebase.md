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
  band: agent-aware
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Filebase Agentic Access
  operation_count: 34
  slug: filebase-agentic-access
  summary_line: 34 operations · 23 acting
api_count: 4
apis:
- description: The Filebase S3-Compatible API provides standard AWS S3 protocol support for bucket and object management. Developers can use any existing S3 SDK, CLI tool, or framework with endpoint s3.filebase.io a
  name: Filebase S3-Compatible API
  slug: filebase-s3-api
- description: The Filebase Platform API provides account-level operations that complement the S3 API. Using HTTP Basic authentication with base64-encoded access key and secret key pairs as a Bearer token, developer
  name: Filebase Platform API
  slug: filebase-platform-api
- description: The Filebase IPFS Pinning Service API implements the vendor-neutral IPFS Pinning Service specification. Per-bucket Bearer tokens authenticate requests to list, add, retrieve, replace, and delete pinne
  name: Filebase IPFS Pinning Service API
  slug: filebase-ipfs-pinning-service-api
- description: The Filebase IPFS RPC API exposes core IPFS daemon functionality through an HTTP interface. Bucket-specific Bearer tokens authenticate all POST requests to the rpc.filebase.io endpoint. Capabilities s
  name: Filebase IPFS RPC API
  slug: filebase-ipfs-rpc-api
- description: Per-bucket storage consumption
  name: Filebase Buckets API
  slug: filebase-buckets-api
- description: Add, retrieve, and import IPFS data
  name: Filebase Data Management API
  slug: filebase-data-management-api
- description: IPNS name publishing and resolution
  name: Filebase IPNS API
  slug: filebase-ipns-api
- description: IPNS keypair management
  name: Filebase Keypairs API
  slug: filebase-keypairs-api
- description: Mutable File System operations
  name: Filebase MFS API
  slug: filebase-mfs-api
- description: Large file multipart upload operations
  name: Filebase Multipart Upload API
  slug: filebase-multipart-upload-api
- description: IPFS node information
  name: Filebase Node API
  slug: filebase-node-api
- description: Object upload, download, copy, delete, and metadata
  name: Filebase Objects API
  slug: filebase-objects-api
- description: Pin and unpin IPFS objects
  name: Filebase Pinning API
  slug: filebase-pinning-api
- description: IPFS pin management operations
  name: Filebase Pins API
  slug: filebase-pins-api
- description: Account-level usage and bandwidth metrics
  name: Filebase Usage API
  slug: filebase-usage-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets API
  slug: open-filebase-buckets-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets Data Management API
  slug: open-filebase-data-management-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets IPNS API
  slug: open-filebase-ipns-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets Keypairs API
  slug: open-filebase-keypairs-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets MFS API
  slug: open-filebase-mfs-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets Multipart Upload API
  slug: open-filebase-multipart-upload-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets Node API
  slug: open-filebase-node-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets Objects API
  slug: open-filebase-objects-api
- collection_type: open
  name: Filebase IPFS Service Buckets Pinning API
  slug: open-filebase-pinning-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets Pins API
  slug: open-filebase-pins-api
- collection_type: open
  name: Filebase IPFS Pinning Service Buckets Usage API
  slug: open-filebase-usage-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/filebase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/filebase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/filebase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://filebase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://filebase.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/filebase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/filebase
- group: other
  title: ''
  type: X
  url: https://twitter.com/Filebase
- group: company
  title: ''
  type: Blog
  url: https://filebase.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://filebase.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.filebase.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/filebase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/filebase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/filebase-finops.yml
created: '2026-06-13'
description: Filebase is an S3-compatible object storage and IPFS pinning platform that combines familiar cloud storage APIs with decentralized, blockchain-backed infrastructure. Developers can store, manage, and pin files to IPFS using standard S3 tooling, a dedicated IPFS Pinning Service API, and an IPFS RPC API — all without changing existing workflows. Filebase delivers geo-redundant 3x replication, free egress for object storage, a global CDN, and predictable pricing, making it straightforward to build Web3 applications on top of decentralized networks through a Web2-style developer experience.
examples:
- key_count: 3
  name: Filebase Add Ipfs Response Example
  slug: filebase-add-ipfs-response-example
- key_count: 4
  name: Filebase Pin Example
  slug: filebase-pin-example
- key_count: 6
  name: Filebase Pin Status Example
  slug: filebase-pin-status-example
- key_count: 3
  name: Filebase Usage Example
  slug: filebase-usage-example
finops:
- name: Filebase Finops
  service_category: ''
  slug: filebase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/filebase.png
json_schemas:
- name: Filebase Pin
  property_count: 4
  slug: filebase-pin
- name: Filebase Pin Status
  property_count: 6
  slug: filebase-pin-status
- name: Filebase Usage Metrics
  property_count: 2
  slug: filebase-usage
jsonld:
- class_count: 15
  name: Filebase Context
  property_count: 32
  slug: filebase-context
layout: provider
modified: '2026-06-13'
name: Filebase
nav: Providers
network: true
overview: 'Filebase publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Buckets API, Data Management API, IPNS API, and 8 more. Tagged areas include Object Storage, IPFS, S3 Compatible, Decentralized Storage, and Pinning.


  The Filebase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Filebase''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Filebase Plans Pricing
  plan_count: 3
  slug: filebase-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Filebase Rate Limits
  slug: filebase-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Filebase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: filebase-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 45.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 64.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/filebase/refs/heads/main/screenshots/filebase-2026-06-20T181207.png
security:
- kind: authentication
  name: Filebase Authentication
  slug: filebase-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Filebase Domain Security
  slug: filebase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: filebase
tags:
- Object Storage
- IPFS
- S3 Compatible
- Decentralized Storage
- Pinning
- Web3
- Cloud Storage
- Blockchain
website: https://filebase.com/
---

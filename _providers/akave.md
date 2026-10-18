---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: S3-compatible object storage API for Akave decentralized storage; works with AWS SDKs, AWS CLI and Terraform. Credentials and a per-credential endpoint URL are issued in Akave Cloud; the documented co
  name: Akave O3 S3-Compatible API
  slug: akave-o3
- description: gRPC services IPCNodeAPI and IPCArchivalAPI (package ipcnodeapi) used by the Akave Go SDK and CLI to talk to Akave nodes; published as a .proto in the akavesdk repository.
  name: Akave IPC Node gRPC API
  slug: ipc-node-api
- baseURL: https://o3-rc2.akave.xyz
  baseurl_source: declared
  description: The Buckets API from Akave — 5 operation(s) for buckets.
  name: Akave Buckets API
  slug: akave-buckets-api
artifact_total: 13
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/rules/akave-rules.yml
  title: ''
  type: Spectral
  url: rules/akave-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/json-ld/akave-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/akave-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/vocabulary/akave-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/akave-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/data-model/akave-data-model.yml
  title: ''
  type: DataModel
  url: data-model/akave-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/conformance/akave-conformance.yml
  title: ''
  type: Conformance
  url: conformance/akave-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/llms/akave-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/akave-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/mcp/akave-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/akave-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/hosts/akave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akave-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/integrations/akave-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/akave-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/vendors/akave-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akave-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.akave.xyz/
- group: company
  title: ''
  type: Website
  url: https://akave.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akave/refs/heads/main/security/akave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akave-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akave.xyz/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.akave.xyz/akave-o3/introduction/setup/
- group: company
  title: ''
  type: Blog
  url: https://akave.com/blog
- group: start
  title: ''
  type: Login
  url: https://console.akave.com
- group: commercial
  title: ''
  type: Pricing
  url: https://akave.com/akave-cloud-pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://akave.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://akave.com/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akave-ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://akave.ai
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Akave is a decentralized, S3-compatible object storage company. Akave Cloud and the Akave O3 gateway expose an S3-compatible API usable with AWS SDKs and CLI tools, backed by the Akave (Oasis) protocol with encryption, erasure coding and on-chain data integrity. Akave also publishes Akavelink, a self-hostable REST API for buckets and files, the Akave CLI and Go/Python SDKs over a gRPC node API, and an MCP server (akave-mcp-js) for AI agents.
image: https://cdn.prod.website-files.com/6830156febbdf1222a7d2e9a/6a8679cda0f58c0878e05b3a_Akave%20Cloud%20-%20Home%20Page%20-%20Page%20Preview.png
json_schemas:
- name: DeleteBucketsMybucketResponse
  property_count: 2
  slug: akave-delete-buckets-mybucket-response
- name: GetBucketsMybucketFilesMyfileTxtDownloadResponse
  property_count: 2
  slug: akave-get-buckets-mybucket-files-myfile-txt-download-response
- name: GetBucketsMybucketFilesMyfileTxtResponse
  property_count: 2
  slug: akave-get-buckets-mybucket-files-myfile-txt-response
- name: GetBucketsMybucketFilesResponse
  property_count: 2
  slug: akave-get-buckets-mybucket-files-response
- name: GetBucketsMybucketResponse
  property_count: 2
  slug: akave-get-buckets-mybucket-response
- name: GetBucketsResponse
  property_count: 2
  slug: akave-get-buckets-response
jsonld:
- class_count: 10
  name: Akave Context
  property_count: 4
  slug: akave-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 12 tools listed.
  name: Akave MCP Server
  slug: akave-mcp-js
modified: '2026-10-13'
name: Akave
nav: Providers
network: true
overview: 'Akave is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Buckets API, and 2 more. Tagged areas include Company, Object Storage, S3 Compatible, Decentralized Storage, and Cloud Storage.


  The Akave catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Akave''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 17 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Akave API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: akave-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 19.7
    contract_quality: 22.6
    developer_ergonomics: 33.3
    discoverability: 76.7
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Akave Domain Security
  slug: akave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: akave
tags:
- Company
- Object Storage
- S3 Compatible
- Decentralized Storage
- Cloud Storage
- gRPC
- MCP
website: https://akave.com
---

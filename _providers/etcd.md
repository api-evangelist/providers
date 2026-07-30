---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 38
  human_in_the_loop: 4
  name: Etcd Agentic Access
  operation_count: 38
  slug: etcd-agentic-access
  summary_line: 38 operations · 38 acting · 4 human-in-the-loop
api_count: 10
apis:
- description: The etcd v3 API is a gRPC-based interface providing key-value operations (put, get, delete, range), watch streams for change notifications, lease management for TTL-based keys, cluster membership mana
  name: etcd gRPC API
  slug: etcd-grpc-api
- description: The etcd concurrency API provides distributed primitives built on top of the core key-value store, including distributed mutexes (locks), leader election, and software transactional memory (STM). Thes
  name: etcd Concurrency API
  slug: etcd-concurrency-api
- description: etcd exposes a Prometheus-compatible metrics endpoint that provides operational insights into the etcd cluster, including request rates, latency histograms, disk I/O statistics, Raft state, and cluste
  name: etcd Metrics API
  slug: etcd-metrics-api
- description: The original etcd v2 API exposed a RESTful HTTP interface for key-value operations using a hierarchical directory structure. This API has been deprecated in favor of the v3 gRPC API and was removed fr
  name: etcd v2 HTTP API
  slug: etcd-v2-api
- description: Authentication and authorization management for users and roles
  name: Etcd Auth API
  slug: etcd-auth-api
- description: Cluster membership management including member add, remove, and list
  name: Etcd Cluster API
  slug: etcd-cluster-api
- description: Key-value store operations including put, get, delete, and range queries
  name: Etcd KV API
  slug: etcd-kv-api
- description: Lease management for TTL-based key expiration
  name: Etcd Lease API
  slug: etcd-lease-api
- description: Maintenance operations including snapshots, defragmentation, and status
  name: Etcd Maintenance API
  slug: etcd-maintenance-api
- description: Watch operations for streaming key change notifications
  name: Etcd Watch API
  slug: etcd-watch-api
artifact_total: 96
collections:
- collection_type: open
  name: etcd HTTP Gateway API
  slug: open-etcd-http-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/etcd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/etcd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/etcd-authentication.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/etcd-key-value-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/etcd-context.jsonld
- group: company
  title: ''
  type: Website
  url: https://etcd.io
- group: docs
  title: ''
  type: Documentation
  url: https://etcd.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://etcd.io/docs/v3.5/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etcd-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/etcd-io/etcd
- group: company
  title: ''
  type: Blog
  url: https://etcd.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://etcd.io/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/etcd-io/etcd/blob/main/CHANGELOG/
- group: auth
  title: ''
  type: Security
  url: https://github.com/etcd-io/etcd/blob/main/security/SECURITY.md
- group: operate
  title: ''
  type: Support
  url: https://etcd.io/community/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/etcd
created: '2026-03-16'
description: etcd is a CNCF graduated distributed, reliable key-value store used as the backing store for all Kubernetes cluster data. It provides strong consistency guarantees using the Raft consensus algorithm, supporting watch operations, lease-based TTLs, and atomic compare-and-swap transactions. etcd is designed for high availability and stores critical configuration data for distributed systems.
finops:
- name: Etcd Finops
  service_category: Distributed Systems / Key-Value Store
  slug: etcd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/etcd.png
json_schemas:
- name: AlarmMember
  property_count: 2
  slug: etcd-alarmmember
- name: AlarmRequest
  property_count: 3
  slug: etcd-alarmrequest
- name: AlarmResponse
  property_count: 2
  slug: etcd-alarmresponse
- name: AuthDisableResponse
  property_count: 1
  slug: etcd-authdisableresponse
- name: AuthEnableResponse
  property_count: 1
  slug: etcd-authenableresponse
- name: AuthenticateRequest
  property_count: 2
  slug: etcd-authenticaterequest
- name: AuthenticateResponse
  property_count: 2
  slug: etcd-authenticateresponse
- name: AuthRoleAddRequest
  property_count: 1
  slug: etcd-authroleaddrequest
- name: AuthRoleAddResponse
  property_count: 1
  slug: etcd-authroleaddresponse
- name: AuthRoleDeleteRequest
  property_count: 1
  slug: etcd-authroledeleterequest
- name: AuthRoleDeleteResponse
  property_count: 1
  slug: etcd-authroledeleteresponse
- name: AuthRoleGetRequest
  property_count: 1
  slug: etcd-authrolegetrequest
- name: AuthRoleGetResponse
  property_count: 2
  slug: etcd-authrolegetresponse
- name: AuthRoleGrantPermissionRequest
  property_count: 2
  slug: etcd-authrolegrantpermissionrequest
- name: AuthRoleGrantPermissionResponse
  property_count: 1
  slug: etcd-authrolegrantpermissionresponse
- name: AuthRoleListResponse
  property_count: 2
  slug: etcd-authrolelistresponse
- name: AuthRoleRevokePermissionRequest
  property_count: 3
  slug: etcd-authrolerevokepermissionrequest
- name: AuthRoleRevokePermissionResponse
  property_count: 1
  slug: etcd-authrolerevokepermissionresponse
- name: AuthUserAddRequest
  property_count: 4
  slug: etcd-authuseraddrequest
- name: AuthUserAddResponse
  property_count: 1
  slug: etcd-authuseraddresponse
- name: AuthUserChangePasswordRequest
  property_count: 3
  slug: etcd-authuserchangepasswordrequest
- name: AuthUserChangePasswordResponse
  property_count: 1
  slug: etcd-authuserchangepasswordresponse
- name: AuthUserDeleteRequest
  property_count: 1
  slug: etcd-authuserdeleterequest
- name: AuthUserDeleteResponse
  property_count: 1
  slug: etcd-authuserdeleteresponse
- name: AuthUserGetRequest
  property_count: 1
  slug: etcd-authusergetrequest
- name: AuthUserGetResponse
  property_count: 2
  slug: etcd-authusergetresponse
- name: AuthUserGrantRoleRequest
  property_count: 2
  slug: etcd-authusergrantrolerequest
- name: AuthUserGrantRoleResponse
  property_count: 1
  slug: etcd-authusergrantroleresponse
- name: AuthUserListResponse
  property_count: 2
  slug: etcd-authuserlistresponse
- name: AuthUserRevokeRoleRequest
  property_count: 2
  slug: etcd-authuserrevokerolerequest
- name: AuthUserRevokeRoleResponse
  property_count: 1
  slug: etcd-authuserrevokeroleresponse
- name: CompactionRequest
  property_count: 2
  slug: etcd-compactionrequest
- name: CompactionResponse
  property_count: 1
  slug: etcd-compactionresponse
- name: Compare
  property_count: 9
  slug: etcd-compare
- name: DefragmentResponse
  property_count: 1
  slug: etcd-defragmentresponse
- name: DeleteRangeRequest
  property_count: 3
  slug: etcd-deleterangerequest
- name: DeleteRangeResponse
  property_count: 3
  slug: etcd-deleterangeresponse
- name: Error
  property_count: 3
  slug: etcd-error
- name: HashResponse
  property_count: 2
  slug: etcd-hashresponse
- name: etcd Key-Value Store
  property_count: 0
  slug: etcd-key-value
- name: KeyValue
  property_count: 6
  slug: etcd-keyvalue
- name: LeaseGrantRequest
  property_count: 2
  slug: etcd-leasegrantrequest
- name: LeaseGrantResponse
  property_count: 4
  slug: etcd-leasegrantresponse
- name: LeaseKeepAliveRequest
  property_count: 1
  slug: etcd-leasekeepaliverequest
- name: LeaseKeepAliveResponse
  property_count: 3
  slug: etcd-leasekeepaliveresponse
- name: LeaseLeasesResponse
  property_count: 2
  slug: etcd-leaseleasesresponse
- name: LeaseRevokeRequest
  property_count: 1
  slug: etcd-leaserevokerequest
- name: LeaseRevokeResponse
  property_count: 1
  slug: etcd-leaserevokeresponse
- name: LeaseTimeToLiveRequest
  property_count: 2
  slug: etcd-leasetimetoliverequest
- name: LeaseTimeToLiveResponse
  property_count: 5
  slug: etcd-leasetimetoliveresponse
- name: Member
  property_count: 5
  slug: etcd-member
- name: MemberAddRequest
  property_count: 2
  slug: etcd-memberaddrequest
- name: MemberAddResponse
  property_count: 3
  slug: etcd-memberaddresponse
- name: MemberListResponse
  property_count: 2
  slug: etcd-memberlistresponse
- name: MemberPromoteRequest
  property_count: 1
  slug: etcd-memberpromoterequest
- name: MemberPromoteResponse
  property_count: 2
  slug: etcd-memberpromoteresponse
- name: MemberRemoveRequest
  property_count: 1
  slug: etcd-memberremoverequest
- name: MemberRemoveResponse
  property_count: 2
  slug: etcd-memberremoveresponse
- name: MemberUpdateRequest
  property_count: 2
  slug: etcd-memberupdaterequest
- name: MemberUpdateResponse
  property_count: 2
  slug: etcd-memberupdateresponse
- name: MoveLeaderRequest
  property_count: 1
  slug: etcd-moveleaderrequest
- name: MoveLeaderResponse
  property_count: 1
  slug: etcd-moveleaderresponse
- name: Permission
  property_count: 3
  slug: etcd-permission
- name: PutRequest
  property_count: 6
  slug: etcd-putrequest
- name: PutResponse
  property_count: 2
  slug: etcd-putresponse
- name: RangeRequest
  property_count: 13
  slug: etcd-rangerequest
- name: RangeResponse
  property_count: 4
  slug: etcd-rangeresponse
- name: RequestOp
  property_count: 4
  slug: etcd-requestop
- name: ResponseHeader
  property_count: 4
  slug: etcd-responseheader
- name: StatusResponse
  property_count: 10
  slug: etcd-statusresponse
- name: TxnRequest
  property_count: 3
  slug: etcd-txnrequest
- name: TxnResponse
  property_count: 3
  slug: etcd-txnresponse
- name: WatchCreateRequest
  property_count: 8
  slug: etcd-watchcreaterequest
- name: WatchEvent
  property_count: 3
  slug: etcd-watchevent
- name: WatchRequest
  property_count: 2
  slug: etcd-watchrequest
- name: WatchResponse
  property_count: 8
  slug: etcd-watchresponse
json_structures:
- name: Etcd Structure
  property_count: 0
  slug: etcd-structure
jsonld:
- class_count: 0
  name: Etcd Context
  property_count: 9
  slug: etcd-context
layout: provider
modified: '2026-05-19'
name: Etcd
nav: Providers
network: true
overview: 'Etcd publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Cluster API, KV API, and 3 more. Tagged areas include Cloud Native, Consensus, Distributed Systems, Graduated, and Key-Value Store.


  The Etcd catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Etcd''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, support, Stack Overflow tag, and 9 more developer resources.'
plans:
- name: Etcd Plans Pricing
  plan_count: 1
  slug: etcd-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Etcd Rate Limits
  slug: etcd-rate-limits
rules:
- name: Etcd API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: etcd-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: -4.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.9
    developer_ergonomics: 37.0
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/etcd/refs/heads/main/screenshots/etcd-2026-06-20T180830.png
security:
- kind: authentication
  name: Etcd Authentication
  slug: etcd-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Etcd Domain Security
  slug: etcd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: etcd
tags:
- Cloud Native
- Consensus
- Distributed Systems
- Graduated
- Key-Value Store
- Kubernetes
website: https://etcd.io
---

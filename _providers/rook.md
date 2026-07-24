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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Rook Agentic Access
  operation_count: 11
  slug: rook-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 6
apis:
- description: Rook extends Kubernetes through Custom Resource Definitions (CRDs) to declaratively manage Ceph storage clusters. The CRD API includes resources for CephCluster, CephBlockPool, CephFilesystem, CephObj
  name: Rook Ceph Custom Resource API
  slug: rook-ceph-crd-api
- description: Rook provides Ceph block storage (RBD) through Kubernetes StorageClasses and PersistentVolumeClaims. The CephBlockPool CRD and associated StorageClass allow applications to dynamically provision block
  name: Rook Ceph Block Storage API
  slug: rook-ceph-block-storage-api
- description: Rook manages CephFilesystem resources to provision shared POSIX-compliant file storage backed by CephFS. Multiple pods can simultaneously read and write to shared filesystem volumes, making it suitabl
  name: Rook Ceph Shared Filesystem API
  slug: rook-ceph-filesystem-api
- description: S3-compatible bucket creation, listing, deletion, and configuration operations on Ceph Object Storage provisioned by Rook
  name: Rook Buckets API
  slug: rook-buckets-api
- description: S3-compatible multipart upload operations for large objects, including initiation, part upload, completion, and abort
  name: Rook Multipart Uploads API
  slug: rook-multipart-uploads-api
- description: S3-compatible object upload, download, listing, deletion, and metadata operations within Ceph Object Storage buckets
  name: Rook Objects API
  slug: rook-objects-api
artifact_total: 27
collections:
- collection_type: open
  name: Rook Ceph Object Storage API
  slug: open-rook-ceph-object-storage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rook-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rook-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rook-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rook-security
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rook-ceph-cluster-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rook-ceph-block-pool-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rook-ceph-filesystem-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rook-ceph-object-store-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/rook-ceph-cluster-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/rook-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rook-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/rook-spectral-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/storage-orchestration.yaml
- group: company
  title: ''
  type: Website
  url: https://rook.io
- group: docs
  title: ''
  type: Documentation
  url: https://rook.io/docs/rook/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://rook.io/docs/rook/latest/Getting-Started/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rook
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/rook/rook
- group: company
  title: ''
  type: Blog
  url: https://blog.rook.io/
- group: operate
  title: ''
  type: Community
  url: https://rook.io/community/
- group: operate
  title: ''
  type: Slack
  url: https://slack.rook.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/rook/rook/blob/master/CHANGELOG.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/rook/rook/blob/master/SECURITY.md
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/rook
- group: other
  title: ''
  type: X
  url: https://twitter.com/rook_io
created: '2025-01-01'
description: Rook is a CNCF graduated cloud-native storage orchestrator for Kubernetes, providing the platform, framework, and support for Ceph distributed storage systems to natively integrate with cloud-native environments. It automates the deployment, configuration, provisioning, scaling, upgrading, and monitoring of storage systems through Kubernetes operators and Custom Resource Definitions (CRDs), with primary support for Ceph block storage, shared filesystems, and S3-compatible object storage.
examples:
- key_count: 2
  name: Rook List Buckets Example
  slug: rook-list-buckets-example
- key_count: 2
  name: Rook List Objects Example
  slug: rook-list-objects-example
- key_count: 2
  name: Rook Put Object Example
  slug: rook-put-object-example
finops:
- name: Rook Finops
  service_category: Cloud Native Storage Orchestration
  slug: rook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rook.png
json_schemas:
- name: Rook CephBlockPool
  property_count: 5
  slug: rook-ceph-block-pool
- name: Rook Ceph CRD Resources
  property_count: 0
  slug: rook-ceph-cluster
- name: Rook CephFilesystem
  property_count: 5
  slug: rook-ceph-filesystem
- name: Rook CephObjectStore
  property_count: 5
  slug: rook-ceph-object-store
json_structures:
- name: Rook Ceph Block Pool Structure
  property_count: 0
  slug: rook-ceph-block-pool-structure
- name: Rook Ceph Cluster Structure
  property_count: 0
  slug: rook-ceph-cluster-structure
- name: Rook Ceph Filesystem Structure
  property_count: 0
  slug: rook-ceph-filesystem-structure
- name: Rook Ceph Object Store Structure
  property_count: 0
  slug: rook-ceph-object-store-structure
jsonld:
- class_count: 0
  name: Rook Context
  property_count: 6
  slug: rook-context
layout: provider
modified: '2026-05-19'
name: Rook
nav: Providers
network: true
overview: 'Rook publishes 3 APIs on the [APIs.io](https://apis.io/) network: Buckets API, Multipart Uploads API, and Objects API. Tagged areas include Block Storage, CNCF, Ceph, Cloud Native, and File Storage.


  The Rook catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rook''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, Stack Overflow tag, and 19 more developer resources.'
plans:
- name: Rook Plans Pricing
  plan_count: 2
  slug: rook-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 2
  name: Rook Rate Limits
  slug: rook-rate-limits
rules:
- name: Rook API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: rook-jsonschema-spectral-rules
- name: Rook API Rules
  rule_count: 17
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 13
  slug: rook-spectral-rules
score:
  band: developing
  composite: 53.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.6
    developer_ergonomics: 37.0
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 53.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rook/refs/heads/main/screenshots/rook-2026-06-20T193212.png
security:
- kind: authentication
  name: Rook Authentication
  slug: rook-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rook Domain Security
  slug: rook-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rook
tags:
- Block Storage
- CNCF
- Ceph
- Cloud Native
- File Storage
- Graduated
- Kubernetes
- Object Storage
- Orchestration
- Storage
website: https://rook.io
---

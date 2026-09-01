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
- acting_count: 11
  human_in_the_loop: 0
  name: Cubefs Agentic Access
  operation_count: 39
  slug: cubefs-agentic-access
  summary_line: 39 operations · 11 acting
api_count: 2
apis:
- description: Access control list operations for buckets and objects. Supports getting and setting ACLs to control access at the bucket and object level.
  name: CubeFS ACLs API
  slug: cubefs-acls-api
- description: Bucket-level operations including creating, listing, and deleting buckets. In CubeFS, each S3 bucket corresponds to a CubeFS volume. Bucket names must be unique within the cluster.
  name: CubeFS Buckets API
  slug: cubefs-buckets-api
- description: Cluster-level operations including retrieving cluster status, topology, and freezing/unfreezing the cluster to control automatic partition creation.
  name: CubeFS Cluster API
  slug: cubefs-cluster-api
- description: Data node management operations including listing nodes, querying node status, decommissioning nodes, and managing data partitions on nodes.
  name: CubeFS DataNodes API
  slug: cubefs-datanodes-api
- description: Data partition management including creating, loading, decommissioning, and diagnosing data partitions within volumes.
  name: CubeFS DataPartitions API
  slug: cubefs-datapartitions-api
- description: Metadata node management operations including listing nodes, querying node status, decommissioning nodes, and managing metadata partitions.
  name: CubeFS MetaNodes API
  slug: cubefs-metanodes-api
- description: Metadata partition management including creating, loading, and decommissioning metadata partitions within volumes.
  name: CubeFS MetaPartitions API
  slug: cubefs-metapartitions-api
- description: Multipart upload operations for uploading large objects in parts. Supports initiating, uploading parts, listing parts, completing, and aborting multipart uploads.
  name: CubeFS Multipart API
  slug: cubefs-multipart-api
- description: Object CRUD operations including uploading, downloading, copying, listing, and deleting objects. Supports both standard single-part uploads and multipart uploads for large objects.
  name: CubeFS Objects API
  slug: cubefs-objects-api
- description: User and access control management for CubeFS multi-tenancy. Users own volumes and are assigned access keys and secret keys for S3-compatible object storage operations.
  name: CubeFS Users API
  slug: cubefs-users-api
- description: Volume lifecycle management operations including creating, updating, expanding, shrinking, and deleting volumes. Volumes are the top-level storage namespaces in CubeFS.
  name: CubeFS Volumes API
  slug: cubefs-volumes-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CubeFS Master ACLs API
  slug: open-cubefs-acls-api
- collection_type: open
  name: CubeFS Master ACLs Buckets API
  slug: open-cubefs-buckets-api
- collection_type: open
  name: CubeFS Master ACLs Cluster API
  slug: open-cubefs-cluster-api
- collection_type: open
  name: CubeFS Master ACLs DataNodes API
  slug: open-cubefs-datanodes-api
- collection_type: open
  name: CubeFS Master ACLs DataPartitions API
  slug: open-cubefs-datapartitions-api
- collection_type: open
  name: CubeFS Master API
  slug: open-cubefs-master-api
- collection_type: open
  name: CubeFS Master ACLs MetaNodes API
  slug: open-cubefs-metanodes-api
- collection_type: open
  name: CubeFS Master ACLs MetaPartitions API
  slug: open-cubefs-metapartitions-api
- collection_type: open
  name: CubeFS Master ACLs Multipart API
  slug: open-cubefs-multipart-api
- collection_type: open
  name: CubeFS Master ACLs Objects API
  slug: open-cubefs-objects-api
- collection_type: open
  name: CubeFS S3-Compatible API
  slug: open-cubefs-s3-api
- collection_type: open
  name: CubeFS Master ACLs Users API
  slug: open-cubefs-users-api
- collection_type: open
  name: CubeFS Master ACLs Volumes API
  slug: open-cubefs-volumes-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cubefs/cubefs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cubefs/cubefs/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cubefs/cubefs/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cubefs/cubefs/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cubefs/cubefs/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cubefs/cubefs/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cubefs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cubefs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cubefs-authentication.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cubefs-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cubefs-volume-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cubefs-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/cubefs-master-rules.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/cubefs-s3-rules.yml
- group: company
  title: ''
  type: Website
  url: https://cubefs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://cubefs.io/docs/master/overview/introduction.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cubefs.io/docs/master/quickstart/single-deploy.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/cubefs/cubefs/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cubefs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cubefs/cubefs
- group: agent
  title: ''
  type: LlmsText
  url: https://cubefs.io/llms.txt
created: '2026-03-16'
description: CubeFS is a CNCF graduated cloud-native distributed file system supporting POSIX, HDFS, and S3-compatible object storage protocols. It provides multi-tenancy, multi-AZ deployment, cross-region replication, and erasure coding for both hot and cold data tiers, and is widely used to back cloud-native AI training, big-data analytics, and container storage workloads.
finops:
- name: Cubefs Finops
  service_category: API
  slug: cubefs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cubefs.png
json_schemas:
- name: CubeFS Volume
  property_count: 17
  slug: cubefs-volume
jsonld:
- class_count: 3
  name: Cubefs Context
  property_count: 9
  slug: cubefs-context
layout: provider
modified: '2026-05-19'
name: CubeFS
nav: Providers
network: true
overview: 'CubeFS publishes 11 APIs on the [APIs.io](https://apis.io/) network, including ACLs API, Buckets API, Cluster API, and 8 more. Tagged areas include Cloud-Native, CNCF Graduated, Distributed File System, Kubernetes, and Object Storage.


  The CubeFS catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  CubeFS''s developer surface includes authentication, documentation, getting-started guide, changelog, and 17 more developer resources.'
plans:
- name: Cubefs Plans Pricing
  plan_count: 3
  slug: cubefs-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Cubefs Rate Limits
  slug: cubefs-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: CubeFS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cubefs-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: CubeFS API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: cubefs-master-rules
- effective_rule_count: 44
  extends:
  - spectral:oas
  name: CubeFS API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: cubefs-s3-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 59.5
    developer_ergonomics: 33.3
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/screenshots/cubefs-2026-06-20T175330.png
security:
- kind: authentication
  name: Cubefs Authentication
  slug: cubefs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cubefs Domain Security
  slug: cubefs-domain-security
  summary_line: TLSv1.3
slug: cubefs
tags:
- Cloud-Native
- CNCF Graduated
- Distributed File System
- Kubernetes
- Object Storage
- POSIX
- S3 Compatible
- Storage
website: https://cubefs.io/
---

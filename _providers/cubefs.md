---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Cubefs Agentic Access
  operation_count: 39
  slug: cubefs-agentic-access
  summary_line: 39 operations · 11 acting
api_count: 2
apis:
- baseURL_template: http://{objectNodeHost}:{objectNodePort}
  baseurl_source: spec_template
  description: Bucket-level operations including creating, listing, and deleting buckets. In CubeFS, each S3 bucket corresponds to a CubeFS volume. Bucket names must be unique within the cluster.
  name: CubeFS Buckets API
  slug: cubefs-buckets-api
- baseURL_template: http://{masterHost}:{masterPort}
  baseurl_source: spec_template
  description: Cluster-level operations including retrieving cluster status, topology, and freezing/unfreezing the cluster to control automatic partition creation.
  name: CubeFS Cluster API
  slug: cubefs-cluster-api
- baseURL_template: http://{masterHost}:{masterPort}
  baseurl_source: spec_template
  description: Data partition management including creating, loading, decommissioning, and diagnosing data partitions within volumes.
  name: CubeFS DataPartitions API
  slug: cubefs-datapartitions-api
- baseURL_template: http://{masterHost}:{masterPort}
  baseurl_source: spec_template
  description: Metadata node management operations including listing nodes, querying node status, decommissioning nodes, and managing metadata partitions.
  name: CubeFS MetaNodes API
  slug: cubefs-metanodes-api
- baseURL_template: http://{masterHost}:{masterPort}
  baseurl_source: spec_template
  description: Metadata partition management including creating, loading, and decommissioning metadata partitions within volumes.
  name: CubeFS MetaPartitions API
  slug: cubefs-metapartitions-api
- baseURL_template: http://{objectNodeHost}:{objectNodePort}
  baseurl_source: spec_template
  description: Multipart upload operations for uploading large objects in parts. Supports initiating, uploading parts, listing parts, completing, and aborting multipart uploads.
  name: CubeFS Multipart API
  slug: cubefs-multipart-api
- baseURL_template: http://{objectNodeHost}:{objectNodePort}
  baseurl_source: spec_template
  description: Object CRUD operations including uploading, downloading, copying, listing, and deleting objects. Supports both standard single-part uploads and multipart uploads for large objects.
  name: CubeFS Objects API
  slug: cubefs-objects-api
- baseURL_template: http://{masterHost}:{masterPort}
  baseurl_source: spec_template
  description: User and access control management for CubeFS multi-tenancy. Users own volumes and are assigned access keys and secret keys for S3-compatible object storage operations.
  name: CubeFS Users API
  slug: cubefs-users-api
- baseURL_template: http://{masterHost}:{masterPort}
  baseurl_source: spec_template
  description: Volume lifecycle management operations including creating, updating, expanding, shrinking, and deleting volumes. Volumes are the top-level storage namespaces in CubeFS.
  name: CubeFS Volumes API
  slug: cubefs-volumes-api
- baseURL_template: http://{objectNodeHost}:{objectNodePort}
  baseurl_source: spec_template
  description: Access control list operations for buckets and objects. Supports getting and setting ACLs to control access at the bucket and object level.
  name: CubeFS AC Ls API
  slug: cubefs-acls-api
- baseURL_template: http://{masterHost}:{masterPort}
  baseurl_source: spec_template
  description: Data node management operations including listing nodes, querying node status, decommissioning nodes, and managing data partitions on nodes.
  name: CubeFS Data Nodes API
  slug: cubefs-data-nodes-api
artifact_total: 35
collections:
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
- group: commercial
  href: https://artifacts.apis.io/cubefs/plans/cubefs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cubefs-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cubefs/rate-limits/cubefs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cubefs-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cubefs/finops/cubefs-finops.yml
  title: ''
  type: FinOps
  url: finops/cubefs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://cubefs.io/blog/
- group: other
  href: https://artifacts.apis.io/cubefs/capabilities/cubefs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cubefs-capability-edges.yml
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
  href: https://artifacts.apis.io/cubefs/agentic-access/cubefs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cubefs-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cubefs/security/cubefs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cubefs-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cubefs/authentication/cubefs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cubefs-authentication.yml
- group: design
  href: https://artifacts.apis.io/cubefs/json-ld/cubefs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cubefs-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cubefs/json-schema/cubefs-volume-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cubefs-volume-schema.json
- group: design
  href: https://artifacts.apis.io/cubefs/vocabulary/cubefs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cubefs-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cubefs/rules/cubefs-master-rules.yml
  title: ''
  type: SpectralRules
  url: rules/cubefs-master-rules.yml
- group: design
  href: https://artifacts.apis.io/cubefs/rules/cubefs-s3-rules.yml
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
- has_sources: false
  method: generated
  name: Cubefs Finops
  primary_unit: request
  service_category: API
  slug: cubefs-finops
  template: true
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
modified: '2026-10-06'
name: CubeFS
nav: Providers
network: true
overview: 'CubeFS publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buckets API, Cluster API, DataPartitions API, and 8 more. Tagged areas include Cloud-Native, CNCF Graduated, Distributed File System, Kubernetes, and Object Storage.


  The CubeFS catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  CubeFS''s developer surface includes engineering blog, authentication, documentation, getting-started guide, changelog, and 21 more developer resources.'
plans:
- name: Cubefs Plans Pricing
  plan_count: 3
  slug: cubefs-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Cubefs Rate Limits
  slug: cubefs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: CubeFS — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cubefs-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: CubeFS — master rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: cubefs-master-rules
- authorship: unmarked
  effective_rule_count: 44
  extends:
  - spectral:oas
  name: CubeFS — s3 rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: cubefs-s3-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.4
    catalog_earned_first_party: 0.0
    catalog_gap: 57.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 27.3
    contract_quality: 53.9
    developer_ergonomics: 35.7
    discoverability: 64.3
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cubefs/cubefs-2026-06-20T175330.png
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

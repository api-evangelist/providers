---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 65
  human_in_the_loop: 3
  name: Weaviate Agentic Access
  operation_count: 111
  slug: weaviate-agentic-access
  summary_line: 111 operations · 65 acting · 3 human-in-the-loop
api_count: 22
apis:
- description: The authz API from Weaviate — 16 operation(s) for authz.
  name: Weaviate authz API
  slug: weaviate-authz-api
- description: The backups API from Weaviate — 3 operation(s) for backups.
  name: Weaviate backups API
  slug: weaviate-backups-api
- description: The batch API from Weaviate — 2 operation(s) for batch.
  name: Weaviate batch API
  slug: weaviate-batch-api
- description: The classifications API from Weaviate — 2 operation(s) for classifications.
  name: Weaviate classifications API
  slug: weaviate-classifications-api
- description: The cluster API from Weaviate — 1 operation(s) for cluster.
  name: Weaviate cluster API
  slug: weaviate-cluster-api
- description: The discovery API from Weaviate — 1 operation(s) for discovery.
  name: Weaviate discovery API
  slug: weaviate-discovery-api
- description: The distributedTasks API from Weaviate — 1 operation(s) for distributedtasks.
  name: Weaviate distributedTasks API
  slug: weaviate-distributedtasks-api
- description: The export API from Weaviate — 2 operation(s) for export.
  name: Weaviate export API
  slug: weaviate-export-api
- description: The graphql API from Weaviate — 2 operation(s) for graphql.
  name: Weaviate graphql API
  slug: weaviate-graphql-api
- description: The mcp API from Weaviate — 1 operation(s) for mcp.
  name: Weaviate mcp API
  slug: weaviate-mcp-api
- description: The meta API from Weaviate — 1 operation(s) for meta.
  name: Weaviate meta API
  slug: weaviate-meta-api
- description: The namespaces API from Weaviate — 2 operation(s) for namespaces.
  name: Weaviate namespaces API
  slug: weaviate-namespaces-api
- description: The nodes API from Weaviate — 2 operation(s) for nodes.
  name: Weaviate nodes API
  slug: weaviate-nodes-api
- description: The objects API from Weaviate — 7 operation(s) for objects.
  name: Weaviate objects API
  slug: weaviate-objects-api
- description: The oidc API from Weaviate — 1 operation(s) for oidc.
  name: Weaviate oidc API
  slug: weaviate-oidc-api
- description: The references API from Weaviate — 1 operation(s) for references.
  name: Weaviate references API
  slug: weaviate-references-api
- description: The replication API from Weaviate — 7 operation(s) for replication.
  name: Weaviate replication API
  slug: weaviate-replication-api
- description: The schema API from Weaviate — 12 operation(s) for schema.
  name: Weaviate schema API
  slug: weaviate-schema-api
- description: The tokenize API from Weaviate — 1 operation(s) for tokenize.
  name: Weaviate tokenize API
  slug: weaviate-tokenize-api
- description: The users API from Weaviate — 6 operation(s) for users.
  name: Weaviate users API
  slug: weaviate-users-api
- description: The Weaviate REST API API from Weaviate — 1 operation(s) for weaviate rest api.
  name: Weaviate Weaviate REST API API
  slug: weaviate-weaviate-rest-api-api
- description: The .well Known API from Weaviate — 3 operation(s) for .well known.
  name: Weaviate .well Known API
  slug: weaviate-well-known-api
artifact_total: 505
collections:
- collection_type: postman
  name: Weaviate REST authz API
  slug: postman-weaviate-authz-api
- collection_type: postman
  name: Weaviate REST authz backups API
  slug: postman-weaviate-backups-api
- collection_type: postman
  name: Weaviate REST authz batch API
  slug: postman-weaviate-batch-api
- collection_type: postman
  name: Weaviate REST authz classifications API
  slug: postman-weaviate-classifications-api
- collection_type: postman
  name: Weaviate REST authz cluster API
  slug: postman-weaviate-cluster-api
- collection_type: postman
  name: Weaviate REST authz discovery API
  slug: postman-weaviate-discovery-api
- collection_type: postman
  name: Weaviate REST authz distributedTasks API
  slug: postman-weaviate-distributedtasks-api
- collection_type: postman
  name: Weaviate REST authz export API
  slug: postman-weaviate-export-api
- collection_type: postman
  name: Weaviate REST authz graphql API
  slug: postman-weaviate-graphql-api
- collection_type: postman
  name: Weaviate REST authz mcp API
  slug: postman-weaviate-mcp-api
- collection_type: postman
  name: Weaviate REST authz meta API
  slug: postman-weaviate-meta-api
- collection_type: postman
  name: Weaviate REST authz namespaces API
  slug: postman-weaviate-namespaces-api
- collection_type: postman
  name: Weaviate REST authz nodes API
  slug: postman-weaviate-nodes-api
- collection_type: postman
  name: Weaviate REST authz objects API
  slug: postman-weaviate-objects-api
- collection_type: postman
  name: Weaviate REST authz oidc API
  slug: postman-weaviate-oidc-api
- collection_type: postman
  name: Weaviate REST authz references API
  slug: postman-weaviate-references-api
- collection_type: postman
  name: Weaviate REST authz replication API
  slug: postman-weaviate-replication-api
- collection_type: postman
  name: Weaviate REST authz schema API
  slug: postman-weaviate-schema-api
- collection_type: postman
  name: Weaviate REST authz tokenize API
  slug: postman-weaviate-tokenize-api
- collection_type: postman
  name: Weaviate REST authz users API
  slug: postman-weaviate-users-api
- collection_type: postman
  name: Weaviate REST authz Weaviate REST API API
  slug: postman-weaviate-weaviate-rest-api-api
- collection_type: postman
  name: Weaviate REST authz .well Known API
  slug: postman-weaviate-well-known-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Weaviate REST authz API
  slug: open-weaviate-authz-api
- collection_type: open
  name: Weaviate REST authz backups API
  slug: open-weaviate-backups-api
- collection_type: open
  name: Weaviate REST authz batch API
  slug: open-weaviate-batch-api
- collection_type: open
  name: Weaviate REST authz classifications API
  slug: open-weaviate-classifications-api
- collection_type: open
  name: Weaviate REST authz cluster API
  slug: open-weaviate-cluster-api
- collection_type: open
  name: Weaviate REST authz discovery API
  slug: open-weaviate-discovery-api
- collection_type: open
  name: Weaviate REST authz distributedTasks API
  slug: open-weaviate-distributedtasks-api
- collection_type: open
  name: Weaviate REST authz export API
  slug: open-weaviate-export-api
- collection_type: open
  name: Weaviate REST authz graphql API
  slug: open-weaviate-graphql-api
- collection_type: open
  name: Weaviate REST authz mcp API
  slug: open-weaviate-mcp-api
- collection_type: open
  name: Weaviate REST authz meta API
  slug: open-weaviate-meta-api
- collection_type: open
  name: Weaviate REST authz namespaces API
  slug: open-weaviate-namespaces-api
- collection_type: open
  name: Weaviate REST authz nodes API
  slug: open-weaviate-nodes-api
- collection_type: open
  name: Weaviate REST authz objects API
  slug: open-weaviate-objects-api
- collection_type: open
  name: Weaviate REST authz oidc API
  slug: open-weaviate-oidc-api
- collection_type: open
  name: Weaviate REST authz references API
  slug: open-weaviate-references-api
- collection_type: open
  name: Weaviate REST authz replication API
  slug: open-weaviate-replication-api
- collection_type: open
  name: Weaviate REST authz schema API
  slug: open-weaviate-schema-api
- collection_type: open
  name: Weaviate REST authz tokenize API
  slug: open-weaviate-tokenize-api
- collection_type: open
  name: Weaviate REST authz users API
  slug: open-weaviate-users-api
- collection_type: open
  name: Weaviate REST authz Weaviate REST API API
  slug: open-weaviate-weaviate-rest-api-api
- collection_type: open
  name: Weaviate REST authz .well Known API
  slug: open-weaviate-well-known-api
- collection_type: open
  name: Weaviate REST API
  slug: open-weaviate
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/weaviate/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weaviate-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/weaviate-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weaviate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weaviate-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weaviate-io
- group: docs
  title: ''
  type: Documentation
  url: https://weaviate.io/developers/weaviate/api/rest
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/weaviate/weaviate
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weaviate
- group: start
  title: ''
  type: GettingStarted
  url: https://weaviate.io/developers/weaviate/quickstart
- group: learn
  title: ''
  type: Learn
  url: https://weaviate.io/developers/academy
- group: company
  title: ''
  type: Blog
  url: https://weaviate.io/blog
- group: operate
  title: ''
  type: Community
  url: https://weaviate.io/community
- group: operate
  title: ''
  type: Forums
  url: https://forum.weaviate.io/
- group: operate
  title: ''
  type: Slack
  url: https://weaviate.io/slack
- group: commercial
  title: ''
  type: Pricing
  url: https://weaviate.io/pricing
- group: other
  title: ''
  type: Podcast
  url: https://weaviate.io/podcast
- group: company
  title: ''
  type: Newsletter
  url: https://newsletter.weaviate.io/
- group: other
  title: ''
  type: Events
  url: https://weaviate.io/community/events
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/weaviate/weaviate/blob/master/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://weaviate.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/weaviate/weaviate/blob/master/CHANGELOG.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/weaviate/weaviate/issues
- group: design
  title: ''
  type: SpectralRules
  url: rules/weaviate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/weaviate-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/weaviate/mcp-server-weaviate
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/weaviate/agent-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://weaviate.io/llms.txt
created: '2024-06-18'
description: Weaviate is an open-source, AI-native vector database that enables developers to build semantic search and AI-powered applications. It stores data as vector embeddings alongside structured properties, enabling lightning-fast similarity search using HNSW or flat indexes. Weaviate supports multi-tenancy, automatic vectorization via configurable modules, GraphQL and REST APIs, and enterprise features including authentication, authorization, backups, and replication.
examples:
- key_count: 1
  name: Weaviate Additional Properties Example
  slug: weaviate-additional-properties-example
- key_count: 2
  name: Weaviate Alias Example
  slug: weaviate-alias-example
- key_count: 1
  name: Weaviate Alias Response Example
  slug: weaviate-alias-response-example
- key_count: 3
  name: Weaviate Async Replication Status Example
  slug: weaviate-async-replication-status-example
- key_count: 6
  name: Weaviate Backup Config Example
  slug: weaviate-backup-config-example
- key_count: 5
  name: Weaviate Backup Create Request Example
  slug: weaviate-backup-create-request-example
- key_count: 7
  name: Weaviate Backup Create Response Example
  slug: weaviate-backup-create-response-example
- key_count: 8
  name: Weaviate Backup Create Status Response Example
  slug: weaviate-backup-create-status-response-example
- key_count: 5
  name: Weaviate Backup Restore Request Example
  slug: weaviate-backup-restore-request-example
- key_count: 6
  name: Weaviate Backup Restore Response Example
  slug: weaviate-backup-restore-response-example
- key_count: 5
  name: Weaviate Backup Restore Status Response Example
  slug: weaviate-backup-restore-status-response-example
- key_count: 4
  name: Weaviate Batch Delete Example
  slug: weaviate-batch-delete-example
- key_count: 5
  name: Weaviate Batch Delete Response Example
  slug: weaviate-batch-delete-response-example
- key_count: 3
  name: Weaviate Batch Reference Example
  slug: weaviate-batch-reference-example
- key_count: 2
  name: Weaviate Batch Reference Response Example
  slug: weaviate-batch-reference-response-example
- key_count: 2
  name: Weaviate Batch Stats Example
  slug: weaviate-batch-stats-example
- key_count: 2
  name: Weaviate Bm25 Config Example
  slug: weaviate-bm25-config-example
- key_count: 3
  name: Weaviate C11Y Extension Example
  slug: weaviate-c11y-extension-example
- key_count: 2
  name: Weaviate C11Y Words Response Example
  slug: weaviate-c11y-words-response-example
- key_count: 13
  name: Weaviate Class Example
  slug: weaviate-class-example
- key_count: 10
  name: Weaviate Classification Example
  slug: weaviate-classification-example
- key_count: 5
  name: Weaviate Classification Meta Example
  slug: weaviate-classification-meta-example
- key_count: 2
  name: Weaviate Cluster Statistics Response Example
  slug: weaviate-cluster-statistics-response-example
- key_count: 8
  name: Weaviate Dbuser Info Example
  slug: weaviate-dbuser-info-example
- key_count: 11
  name: Weaviate Deprecation Example
  slug: weaviate-deprecation-example
- key_count: 9
  name: Weaviate Distributed Task Example
  slug: weaviate-distributed-task-example
- key_count: 7
  name: Weaviate Distributed Task Unit Example
  slug: weaviate-distributed-task-unit-example
- key_count: 1
  name: Weaviate Distributed Tasks Example
  slug: weaviate-distributed-tasks-example
- key_count: 1
  name: Weaviate Error Response Example
  slug: weaviate-error-response-example
- key_count: 4
  name: Weaviate Export Create Request Example
  slug: weaviate-export-create-request-example
- key_count: 6
  name: Weaviate Export Create Response Example
  slug: weaviate-export-create-response-example
- key_count: 10
  name: Weaviate Export Status Response Example
  slug: weaviate-export-status-response-example
- key_count: 2
  name: Weaviate Geo Coordinates Example
  slug: weaviate-geo-coordinates-example
- key_count: 3
  name: Weaviate Graph Qlerror Example
  slug: weaviate-graph-qlerror-example
- key_count: 3
  name: Weaviate Graph Qlquery Example
  slug: weaviate-graph-qlquery-example
- key_count: 2
  name: Weaviate Graph Qlresponse Example
  slug: weaviate-graph-qlresponse-example
- key_count: 9
  name: Weaviate Inverted Index Config Example
  slug: weaviate-inverted-index-config-example
- key_count: 0
  name: Weaviate Json Object Example
  slug: weaviate-json-object-example
- key_count: 4
  name: Weaviate Link Example
  slug: weaviate-link-example
- key_count: 4
  name: Weaviate Meta Example
  slug: weaviate-meta-example
- key_count: 3
  name: Weaviate Multi Tenancy Config Example
  slug: weaviate-multi-tenancy-config-example
- key_count: 1
  name: Weaviate Namespace Example
  slug: weaviate-namespace-example
- key_count: 9
  name: Weaviate Nested Property Example
  slug: weaviate-nested-property-example
- key_count: 10
  name: Weaviate Node Shard Status Example
  slug: weaviate-node-shard-status-example
- key_count: 2
  name: Weaviate Node Stats Example
  slug: weaviate-node-stats-example
- key_count: 8
  name: Weaviate Node Status Example
  slug: weaviate-node-status-example
- key_count: 1
  name: Weaviate Nodes Status Response Example
  slug: weaviate-nodes-status-response-example
- key_count: 10
  name: Weaviate Object Example
  slug: weaviate-object-example
- key_count: 4
  name: Weaviate Object Ttl Config Example
  slug: weaviate-object-ttl-config-example
- key_count: 3
  name: Weaviate Objects Get Response Example
  slug: weaviate-objects-get-response-example
- key_count: 3
  name: Weaviate Objects List Response Example
  slug: weaviate-objects-list-response-example
- key_count: 4
  name: Weaviate Peer Update Example
  slug: weaviate-peer-update-example
- key_count: 12
  name: Weaviate Permission Example
  slug: weaviate-permission-example
- key_count: 7
  name: Weaviate Phone Number Example
  slug: weaviate-phone-number-example
- key_count: 5
  name: Weaviate Principal Example
  slug: weaviate-principal-example
- key_count: 12
  name: Weaviate Property Example
  slug: weaviate-property-example
- key_count: 0
  name: Weaviate Property Schema Example
  slug: weaviate-property-schema-example
- key_count: 1
  name: Weaviate Property Tokenize Request Example
  slug: weaviate-property-tokenize-request-example
- key_count: 18
  name: Weaviate Raft Statistics Example
  slug: weaviate-raft-statistics-example
- key_count: 10
  name: Weaviate Reference Meta Classification Example
  slug: weaviate-reference-meta-classification-example
- key_count: 14
  name: Weaviate Replication Async Config Example
  slug: weaviate-replication-async-config-example
- key_count: 4
  name: Weaviate Replication Config Example
  slug: weaviate-replication-config-example
- key_count: 12
  name: Weaviate Replication Replicate Details Replica Response Example
  slug: weaviate-replication-replicate-details-replica-response-example
- key_count: 2
  name: Weaviate Replication Replicate Details Replica Status Error Example
  slug: weaviate-replication-replicate-details-replica-status-error-example
- key_count: 3
  name: Weaviate Replication Replicate Details Replica Status Example
  slug: weaviate-replication-replicate-details-replica-status-example
- key_count: 5
  name: Weaviate Replication Replicate Force Delete Request Example
  slug: weaviate-replication-replicate-force-delete-request-example
- key_count: 2
  name: Weaviate Replication Replicate Force Delete Response Example
  slug: weaviate-replication-replicate-force-delete-response-example
- key_count: 5
  name: Weaviate Replication Replicate Replica Request Example
  slug: weaviate-replication-replicate-replica-request-example
- key_count: 1
  name: Weaviate Replication Replicate Replica Response Example
  slug: weaviate-replication-replicate-replica-response-example
- key_count: 3
  name: Weaviate Replication Scale Apply Response Example
  slug: weaviate-replication-scale-apply-response-example
- key_count: 3
  name: Weaviate Replication Scale Plan Example
  slug: weaviate-replication-scale-plan-example
- key_count: 2
  name: Weaviate Replication Shard Replicas Example
  slug: weaviate-replication-shard-replicas-example
- key_count: 2
  name: Weaviate Replication Sharding State Example
  slug: weaviate-replication-sharding-state-example
- key_count: 1
  name: Weaviate Replication Sharding State Response Example
  slug: weaviate-replication-sharding-state-response-example
- key_count: 6
  name: Weaviate Restore Config Example
  slug: weaviate-restore-config-example
- key_count: 2
  name: Weaviate Role Example
  slug: weaviate-role-example
- key_count: 3
  name: Weaviate Schema Example
  slug: weaviate-schema-example
- key_count: 4
  name: Weaviate Shard Progress Example
  slug: weaviate-shard-progress-example
- key_count: 1
  name: Weaviate Shard Status Example
  slug: weaviate-shard-status-example
- key_count: 3
  name: Weaviate Shard Status Get Response Example
  slug: weaviate-shard-status-get-response-example
- key_count: 5
  name: Weaviate Single Ref Example
  slug: weaviate-single-ref-example
- key_count: 13
  name: Weaviate Statistics Example
  slug: weaviate-statistics-example
- key_count: 3
  name: Weaviate Stopword Config Example
  slug: weaviate-stopword-config-example
- key_count: 2
  name: Weaviate Tenant Example
  slug: weaviate-tenant-example
- key_count: 3
  name: Weaviate Text Analyzer Config Example
  slug: weaviate-text-analyzer-config-example
- key_count: 5
  name: Weaviate Tokenize Request Example
  slug: weaviate-tokenize-request-example
- key_count: 2
  name: Weaviate Tokenize Response Example
  slug: weaviate-tokenize-response-example
- key_count: 2
  name: Weaviate Tokenizer User Dict Config Example
  slug: weaviate-tokenizer-user-dict-config-example
- key_count: 1
  name: Weaviate User Api Key Example
  slug: weaviate-user-api-key-example
- key_count: 3
  name: Weaviate User Own Info Example
  slug: weaviate-user-own-info-example
- key_count: 3
  name: Weaviate Vector Config Example
  slug: weaviate-vector-config-example
- key_count: 0
  name: Weaviate Vector Example
  slug: weaviate-vector-example
- key_count: 0
  name: Weaviate Vector Weights Example
  slug: weaviate-vector-weights-example
- key_count: 1
  name: Weaviate Vectors Example
  slug: weaviate-vectors-example
- key_count: 16
  name: Weaviate Where Filter Example
  slug: weaviate-where-filter-example
- key_count: 2
  name: Weaviate Where Filter Geo Range Example
  slug: weaviate-where-filter-geo-range-example
features:
- Free Trial 14 days then pay-as-you-go
- 'Flex from $45/mo: $0.255/GiB storage, $0.0264/GiB backup'
- 'Premium from $400/mo: $0.31875/GiB storage, $0.033/GiB backup'
- Hybrid search (vector + BM25)
- Dynamic index, compression, multi-tenancy
- REST, GraphQL, and gRPC APIs
- Throughput scales with cluster size
- Batch import recommended at 100 objects/request
- Built-in modules for OpenAI, Cohere, HuggingFace embeddings
- Generative search modules (RAG-style)
- Multi-tenancy with strict isolation
- Bring Your Own Vectors (BYOV)
- RBAC baseline security
- 99.5% SLA Flex, up to 99.95% Premium
- Available on AWS, GCP, Azure
- Open-source self-hosted alternative
finops:
- name: Weaviate Finops
  service_category: Vector Database
  slug: weaviate-finops
graphqls:
- description: The Weaviate REST API provides full programmatic access to vector database operations including object CRUD, schema management, GraphQL vector search, multi-tenancy, backups, authentication, authoriza
  name: Weaviate GraphQL API
  slug: weaviate-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weaviate.png
json_schemas:
- name: AdditionalProperties
  property_count: 0
  slug: weaviate-additional-properties
- name: AdditionalProperties
  property_count: 0
  slug: weaviate-additionalproperties
- name: AliasResponse
  property_count: 1
  slug: weaviate-alias-response
- name: Alias
  property_count: 2
  slug: weaviate-alias
- name: AliasResponse
  property_count: 1
  slug: weaviate-aliasresponse
- name: AsyncReplicationStatus
  property_count: 3
  slug: weaviate-async-replication-status
- name: AsyncReplicationStatus
  property_count: 3
  slug: weaviate-asyncreplicationstatus
- name: BackupConfig
  property_count: 6
  slug: weaviate-backup-config
- name: BackupCreateRequest
  property_count: 5
  slug: weaviate-backup-create-request
- name: BackupCreateResponse
  property_count: 7
  slug: weaviate-backup-create-response
- name: BackupCreateStatusResponse
  property_count: 8
  slug: weaviate-backup-create-status-response
- name: BackupListResponse
  property_count: 0
  slug: weaviate-backup-list-response
- name: BackupRestoreRequest
  property_count: 5
  slug: weaviate-backup-restore-request
- name: BackupRestoreResponse
  property_count: 6
  slug: weaviate-backup-restore-response
- name: BackupRestoreStatusResponse
  property_count: 5
  slug: weaviate-backup-restore-status-response
- name: BackupConfig
  property_count: 6
  slug: weaviate-backupconfig
- name: BackupCreateRequest
  property_count: 5
  slug: weaviate-backupcreaterequest
- name: BackupCreateResponse
  property_count: 7
  slug: weaviate-backupcreateresponse
- name: BackupCreateStatusResponse
  property_count: 8
  slug: weaviate-backupcreatestatusresponse
- name: BackupListResponse
  property_count: 0
  slug: weaviate-backuplistresponse
- name: BackupRestoreRequest
  property_count: 5
  slug: weaviate-backuprestorerequest
- name: BackupRestoreResponse
  property_count: 6
  slug: weaviate-backuprestoreresponse
- name: BackupRestoreStatusResponse
  property_count: 5
  slug: weaviate-backuprestorestatusresponse
- name: BatchDeleteResponse
  property_count: 5
  slug: weaviate-batch-delete-response
- name: BatchDelete
  property_count: 4
  slug: weaviate-batch-delete
- name: BatchReferenceResponse
  property_count: 0
  slug: weaviate-batch-reference-response
- name: BatchReference
  property_count: 3
  slug: weaviate-batch-reference
- name: BatchStats
  property_count: 2
  slug: weaviate-batch-stats
- name: BatchDelete
  property_count: 4
  slug: weaviate-batchdelete
- name: BatchDeleteResponse
  property_count: 5
  slug: weaviate-batchdeleteresponse
- name: BatchReference
  property_count: 3
  slug: weaviate-batchreference
- name: BatchReferenceResponse
  property_count: 0
  slug: weaviate-batchreferenceresponse
- name: BatchStats
  property_count: 2
  slug: weaviate-batchstats
- name: BM25Config
  property_count: 2
  slug: weaviate-bm25-config
- name: BM25Config
  property_count: 2
  slug: weaviate-bm25config
- name: C11yExtension
  property_count: 3
  slug: weaviate-c11y-extension
- name: C11yNearestNeighbors
  property_count: 0
  slug: weaviate-c11y-nearest-neighbors
- name: C11yVector
  property_count: 0
  slug: weaviate-c11y-vector
- name: C11yWordsResponse
  property_count: 2
  slug: weaviate-c11y-words-response
- name: C11yExtension
  property_count: 3
  slug: weaviate-c11yextension
- name: C11yNearestNeighbors
  property_count: 0
  slug: weaviate-c11ynearestneighbors
- name: C11yVector
  property_count: 0
  slug: weaviate-c11yvector
- name: C11yWordsResponse
  property_count: 2
  slug: weaviate-c11ywordsresponse
- name: Class
  property_count: 13
  slug: weaviate-class
- name: ClassificationMeta
  property_count: 5
  slug: weaviate-classification-meta
- name: Classification
  property_count: 10
  slug: weaviate-classification
- name: ClassificationMeta
  property_count: 5
  slug: weaviate-classificationmeta
- name: ClusterStatisticsResponse
  property_count: 2
  slug: weaviate-cluster-statistics-response
- name: ClusterStatisticsResponse
  property_count: 2
  slug: weaviate-clusterstatisticsresponse
- name: DBUserInfo
  property_count: 8
  slug: weaviate-dbuser-info
- name: DBUserInfo
  property_count: 8
  slug: weaviate-dbuserinfo
- name: Deprecation
  property_count: 11
  slug: weaviate-deprecation
- name: DistributedTask
  property_count: 9
  slug: weaviate-distributed-task
- name: DistributedTaskUnit
  property_count: 7
  slug: weaviate-distributed-task-unit
- name: DistributedTasks
  property_count: 0
  slug: weaviate-distributed-tasks
- name: DistributedTask
  property_count: 9
  slug: weaviate-distributedtask
- name: DistributedTasks
  property_count: 0
  slug: weaviate-distributedtasks
- name: DistributedTaskUnit
  property_count: 7
  slug: weaviate-distributedtaskunit
- name: ErrorResponse
  property_count: 1
  slug: weaviate-error-response
- name: ErrorResponse
  property_count: 1
  slug: weaviate-errorresponse
- name: ExportCreateRequest
  property_count: 4
  slug: weaviate-export-create-request
- name: ExportCreateResponse
  property_count: 6
  slug: weaviate-export-create-response
- name: ExportStatusResponse
  property_count: 10
  slug: weaviate-export-status-response
- name: ExportCreateRequest
  property_count: 4
  slug: weaviate-exportcreaterequest
- name: ExportCreateResponse
  property_count: 6
  slug: weaviate-exportcreateresponse
- name: ExportStatusResponse
  property_count: 10
  slug: weaviate-exportstatusresponse
- name: GeoCoordinates
  property_count: 2
  slug: weaviate-geo-coordinates
- name: GeoCoordinates
  property_count: 2
  slug: weaviate-geocoordinates
- name: GraphQLError
  property_count: 3
  slug: weaviate-graph-qlerror
- name: GraphQLQueries
  property_count: 0
  slug: weaviate-graph-qlqueries
- name: GraphQLQuery
  property_count: 3
  slug: weaviate-graph-qlquery
- name: GraphQLResponse
  property_count: 2
  slug: weaviate-graph-qlresponse
- name: GraphQLResponses
  property_count: 0
  slug: weaviate-graph-qlresponses
- name: GraphQLError
  property_count: 3
  slug: weaviate-graphqlerror
- name: GraphQLQueries
  property_count: 0
  slug: weaviate-graphqlqueries
- name: GraphQLQuery
  property_count: 3
  slug: weaviate-graphqlquery
- name: GraphQLResponse
  property_count: 2
  slug: weaviate-graphqlresponse
- name: GraphQLResponses
  property_count: 0
  slug: weaviate-graphqlresponses
- name: GroupType
  property_count: 0
  slug: weaviate-group-type
- name: GroupType
  property_count: 0
  slug: weaviate-grouptype
- name: InvertedIndexConfig
  property_count: 9
  slug: weaviate-inverted-index-config
- name: InvertedIndexConfig
  property_count: 9
  slug: weaviate-invertedindexconfig
- name: JsonObject
  property_count: 0
  slug: weaviate-json-object
- name: JsonObject
  property_count: 0
  slug: weaviate-jsonobject
- name: Link
  property_count: 4
  slug: weaviate-link
- name: Meta
  property_count: 4
  slug: weaviate-meta
- name: MultiTenancyConfig
  property_count: 3
  slug: weaviate-multi-tenancy-config
- name: MultipleRef
  property_count: 0
  slug: weaviate-multiple-ref
- name: MultipleRef
  property_count: 0
  slug: weaviate-multipleref
- name: MultiTenancyConfig
  property_count: 3
  slug: weaviate-multitenancyconfig
- name: NamespaceListResponse
  property_count: 0
  slug: weaviate-namespace-list-response
- name: Namespace
  property_count: 1
  slug: weaviate-namespace
- name: NamespaceListResponse
  property_count: 0
  slug: weaviate-namespacelistresponse
- name: NestedProperty
  property_count: 9
  slug: weaviate-nested-property
- name: NestedProperty
  property_count: 9
  slug: weaviate-nestedproperty
- name: NodeShardStatus
  property_count: 10
  slug: weaviate-node-shard-status
- name: NodeStats
  property_count: 2
  slug: weaviate-node-stats
- name: NodeStatus
  property_count: 8
  slug: weaviate-node-status
- name: NodesStatusResponse
  property_count: 1
  slug: weaviate-nodes-status-response
- name: NodeShardStatus
  property_count: 10
  slug: weaviate-nodeshardstatus
- name: NodesStatusResponse
  property_count: 1
  slug: weaviate-nodesstatusresponse
- name: NodeStats
  property_count: 2
  slug: weaviate-nodestats
- name: NodeStatus
  property_count: 8
  slug: weaviate-nodestatus
- name: Object
  property_count: 10
  slug: weaviate-object
- name: ObjectTtlConfig
  property_count: 4
  slug: weaviate-object-ttl-config
- name: ObjectsGetResponse
  property_count: 0
  slug: weaviate-objects-get-response
- name: ObjectsListResponse
  property_count: 3
  slug: weaviate-objects-list-response
- name: ObjectsGetResponse
  property_count: 0
  slug: weaviate-objectsgetresponse
- name: ObjectsListResponse
  property_count: 3
  slug: weaviate-objectslistresponse
- name: ObjectTtlConfig
  property_count: 4
  slug: weaviate-objectttlconfig
- name: PeerUpdate
  property_count: 4
  slug: weaviate-peer-update
- name: PeerUpdate
  property_count: 4
  slug: weaviate-peerupdate
- name: Permission
  property_count: 12
  slug: weaviate-permission
- name: PhoneNumber
  property_count: 7
  slug: weaviate-phone-number
- name: PhoneNumber
  property_count: 7
  slug: weaviate-phonenumber
- name: Principal
  property_count: 5
  slug: weaviate-principal
- name: PropertySchema
  property_count: 0
  slug: weaviate-property-schema
- name: Property
  property_count: 12
  slug: weaviate-property
- name: PropertyTokenizeRequest
  property_count: 1
  slug: weaviate-property-tokenize-request
- name: PropertySchema
  property_count: 0
  slug: weaviate-propertyschema
- name: PropertyTokenizeRequest
  property_count: 1
  slug: weaviate-propertytokenizerequest
- name: RaftStatistics
  property_count: 18
  slug: weaviate-raft-statistics
- name: RaftStatistics
  property_count: 18
  slug: weaviate-raftstatistics
- name: ReferenceMetaClassification
  property_count: 10
  slug: weaviate-reference-meta-classification
- name: ReferenceMetaClassification
  property_count: 10
  slug: weaviate-referencemetaclassification
- name: ReplicationAsyncConfig
  property_count: 14
  slug: weaviate-replication-async-config
- name: ReplicationConfig
  property_count: 4
  slug: weaviate-replication-config
- name: ReplicationReplicateDetailsReplicaResponse
  property_count: 12
  slug: weaviate-replication-replicate-details-replica-response
- name: ReplicationReplicateDetailsReplicaStatusError
  property_count: 2
  slug: weaviate-replication-replicate-details-replica-status-error
- name: ReplicationReplicateDetailsReplicaStatus
  property_count: 3
  slug: weaviate-replication-replicate-details-replica-status
- name: ReplicationReplicateForceDeleteRequest
  property_count: 5
  slug: weaviate-replication-replicate-force-delete-request
- name: ReplicationReplicateForceDeleteResponse
  property_count: 2
  slug: weaviate-replication-replicate-force-delete-response
- name: ReplicationReplicateReplicaRequest
  property_count: 5
  slug: weaviate-replication-replicate-replica-request
- name: ReplicationReplicateReplicaResponse
  property_count: 1
  slug: weaviate-replication-replicate-replica-response
- name: ReplicationScaleApplyResponse
  property_count: 3
  slug: weaviate-replication-scale-apply-response
- name: ReplicationScalePlan
  property_count: 3
  slug: weaviate-replication-scale-plan
- name: ReplicationShardReplicas
  property_count: 2
  slug: weaviate-replication-shard-replicas
- name: ReplicationShardingStateResponse
  property_count: 1
  slug: weaviate-replication-sharding-state-response
- name: ReplicationShardingState
  property_count: 2
  slug: weaviate-replication-sharding-state
- name: ReplicationAsyncConfig
  property_count: 14
  slug: weaviate-replicationasyncconfig
- name: ReplicationConfig
  property_count: 4
  slug: weaviate-replicationconfig
- name: ReplicationReplicateDetailsReplicaResponse
  property_count: 12
  slug: weaviate-replicationreplicatedetailsreplicaresponse
- name: ReplicationReplicateDetailsReplicaStatus
  property_count: 3
  slug: weaviate-replicationreplicatedetailsreplicastatus
- name: ReplicationReplicateDetailsReplicaStatusError
  property_count: 2
  slug: weaviate-replicationreplicatedetailsreplicastatuserror
- name: ReplicationReplicateForceDeleteRequest
  property_count: 5
  slug: weaviate-replicationreplicateforcedeleterequest
- name: ReplicationReplicateForceDeleteResponse
  property_count: 2
  slug: weaviate-replicationreplicateforcedeleteresponse
- name: ReplicationReplicateReplicaRequest
  property_count: 5
  slug: weaviate-replicationreplicatereplicarequest
- name: ReplicationReplicateReplicaResponse
  property_count: 1
  slug: weaviate-replicationreplicatereplicaresponse
- name: ReplicationScaleApplyResponse
  property_count: 3
  slug: weaviate-replicationscaleapplyresponse
- name: ReplicationScalePlan
  property_count: 3
  slug: weaviate-replicationscaleplan
- name: ReplicationShardingState
  property_count: 2
  slug: weaviate-replicationshardingstate
- name: ReplicationShardingStateResponse
  property_count: 1
  slug: weaviate-replicationshardingstateresponse
- name: ReplicationShardReplicas
  property_count: 2
  slug: weaviate-replicationshardreplicas
- name: RestoreConfig
  property_count: 6
  slug: weaviate-restore-config
- name: RestoreConfig
  property_count: 6
  slug: weaviate-restoreconfig
- name: Role
  property_count: 2
  slug: weaviate-role
- name: RolesListResponse
  property_count: 0
  slug: weaviate-roles-list-response
- name: RolesListResponse
  property_count: 0
  slug: weaviate-roleslistresponse
- name: Schema
  property_count: 3
  slug: weaviate-schema
- name: ShardProgress
  property_count: 4
  slug: weaviate-shard-progress
- name: ShardStatusGetResponse
  property_count: 3
  slug: weaviate-shard-status-get-response
- name: ShardStatusList
  property_count: 0
  slug: weaviate-shard-status-list
- name: ShardStatus
  property_count: 1
  slug: weaviate-shard-status
- name: ShardProgress
  property_count: 4
  slug: weaviate-shardprogress
- name: ShardStatus
  property_count: 1
  slug: weaviate-shardstatus
- name: ShardStatusGetResponse
  property_count: 3
  slug: weaviate-shardstatusgetresponse
- name: ShardStatusList
  property_count: 0
  slug: weaviate-shardstatuslist
- name: SingleRef
  property_count: 5
  slug: weaviate-single-ref
- name: SingleRef
  property_count: 5
  slug: weaviate-singleref
- name: Statistics
  property_count: 13
  slug: weaviate-statistics
- name: StopwordConfig
  property_count: 3
  slug: weaviate-stopword-config
- name: StopwordConfig
  property_count: 3
  slug: weaviate-stopwordconfig
- name: Tenant
  property_count: 2
  slug: weaviate-tenant
- name: TextAnalyzerConfig
  property_count: 3
  slug: weaviate-text-analyzer-config
- name: TextAnalyzerConfig
  property_count: 3
  slug: weaviate-textanalyzerconfig
- name: TokenizeRequest
  property_count: 5
  slug: weaviate-tokenize-request
- name: TokenizeResponse
  property_count: 2
  slug: weaviate-tokenize-response
- name: TokenizerUserDictConfig
  property_count: 2
  slug: weaviate-tokenizer-user-dict-config
- name: TokenizeRequest
  property_count: 5
  slug: weaviate-tokenizerequest
- name: TokenizeResponse
  property_count: 2
  slug: weaviate-tokenizeresponse
- name: TokenizerUserDictConfig
  property_count: 2
  slug: weaviate-tokenizeruserdictconfig
- name: UserApiKey
  property_count: 1
  slug: weaviate-user-api-key
- name: UserOwnInfo
  property_count: 3
  slug: weaviate-user-own-info
- name: UserTypeInput
  property_count: 0
  slug: weaviate-user-type-input
- name: UserTypeOutput
  property_count: 0
  slug: weaviate-user-type-output
- name: UserApiKey
  property_count: 1
  slug: weaviate-userapikey
- name: UserOwnInfo
  property_count: 3
  slug: weaviate-userowninfo
- name: UserTypeInput
  property_count: 0
  slug: weaviate-usertypeinput
- name: UserTypeOutput
  property_count: 0
  slug: weaviate-usertypeoutput
- name: VectorConfig
  property_count: 3
  slug: weaviate-vector-config
- name: Vector
  property_count: 0
  slug: weaviate-vector
- name: VectorWeights
  property_count: 0
  slug: weaviate-vector-weights
- name: VectorConfig
  property_count: 3
  slug: weaviate-vectorconfig
- name: Vectors
  property_count: 0
  slug: weaviate-vectors
- name: VectorWeights
  property_count: 0
  slug: weaviate-vectorweights
- name: WhereFilterGeoRange
  property_count: 2
  slug: weaviate-where-filter-geo-range
- name: WhereFilter
  property_count: 16
  slug: weaviate-where-filter
- name: WhereFilter
  property_count: 16
  slug: weaviate-wherefilter
- name: WhereFilterGeoRange
  property_count: 2
  slug: weaviate-wherefiltergeorange
json_structures:
- name: Weaviate Additional Properties Structure
  property_count: 0
  slug: weaviate-additional-properties-structure
- name: Weaviate Alias Response Structure
  property_count: 1
  slug: weaviate-alias-response-structure
- name: Weaviate Alias Structure
  property_count: 2
  slug: weaviate-alias-structure
- name: Weaviate Async Replication Status Structure
  property_count: 3
  slug: weaviate-async-replication-status-structure
- name: Weaviate Backup Config Structure
  property_count: 6
  slug: weaviate-backup-config-structure
- name: Weaviate Backup Create Request Structure
  property_count: 5
  slug: weaviate-backup-create-request-structure
- name: Weaviate Backup Create Response Structure
  property_count: 7
  slug: weaviate-backup-create-response-structure
- name: Weaviate Backup Create Status Response Structure
  property_count: 8
  slug: weaviate-backup-create-status-response-structure
- name: Weaviate Backup List Response Structure
  property_count: 0
  slug: weaviate-backup-list-response-structure
- name: Weaviate Backup Restore Request Structure
  property_count: 5
  slug: weaviate-backup-restore-request-structure
- name: Weaviate Backup Restore Response Structure
  property_count: 6
  slug: weaviate-backup-restore-response-structure
- name: Weaviate Backup Restore Status Response Structure
  property_count: 5
  slug: weaviate-backup-restore-status-response-structure
- name: Weaviate Batch Delete Response Structure
  property_count: 5
  slug: weaviate-batch-delete-response-structure
- name: Weaviate Batch Delete Structure
  property_count: 4
  slug: weaviate-batch-delete-structure
- name: Weaviate Batch Reference Response Structure
  property_count: 0
  slug: weaviate-batch-reference-response-structure
- name: Weaviate Batch Reference Structure
  property_count: 3
  slug: weaviate-batch-reference-structure
- name: Weaviate Batch Stats Structure
  property_count: 2
  slug: weaviate-batch-stats-structure
- name: Weaviate Bm25 Config Structure
  property_count: 2
  slug: weaviate-bm25-config-structure
- name: Weaviate C11Y Extension Structure
  property_count: 3
  slug: weaviate-c11y-extension-structure
- name: Weaviate C11Y Nearest Neighbors Structure
  property_count: 0
  slug: weaviate-c11y-nearest-neighbors-structure
- name: Weaviate C11Y Vector Structure
  property_count: 0
  slug: weaviate-c11y-vector-structure
- name: Weaviate C11Y Words Response Structure
  property_count: 2
  slug: weaviate-c11y-words-response-structure
- name: Weaviate Class Structure
  property_count: 13
  slug: weaviate-class-structure
- name: Weaviate Classification Meta Structure
  property_count: 5
  slug: weaviate-classification-meta-structure
- name: Weaviate Classification Structure
  property_count: 10
  slug: weaviate-classification-structure
- name: Weaviate Cluster Statistics Response Structure
  property_count: 2
  slug: weaviate-cluster-statistics-response-structure
- name: Weaviate Dbuser Info Structure
  property_count: 8
  slug: weaviate-dbuser-info-structure
- name: Weaviate Deprecation Structure
  property_count: 11
  slug: weaviate-deprecation-structure
- name: Weaviate Distributed Task Structure
  property_count: 9
  slug: weaviate-distributed-task-structure
- name: Weaviate Distributed Task Unit Structure
  property_count: 7
  slug: weaviate-distributed-task-unit-structure
- name: Weaviate Distributed Tasks Structure
  property_count: 0
  slug: weaviate-distributed-tasks-structure
- name: Weaviate Error Response Structure
  property_count: 1
  slug: weaviate-error-response-structure
- name: Weaviate Export Create Request Structure
  property_count: 4
  slug: weaviate-export-create-request-structure
- name: Weaviate Export Create Response Structure
  property_count: 6
  slug: weaviate-export-create-response-structure
- name: Weaviate Export Status Response Structure
  property_count: 10
  slug: weaviate-export-status-response-structure
- name: Weaviate Geo Coordinates Structure
  property_count: 2
  slug: weaviate-geo-coordinates-structure
- name: Weaviate Graph Qlerror Structure
  property_count: 3
  slug: weaviate-graph-qlerror-structure
- name: Weaviate Graph Qlqueries Structure
  property_count: 0
  slug: weaviate-graph-qlqueries-structure
- name: Weaviate Graph Qlquery Structure
  property_count: 3
  slug: weaviate-graph-qlquery-structure
- name: Weaviate Graph Qlresponse Structure
  property_count: 2
  slug: weaviate-graph-qlresponse-structure
- name: Weaviate Graph Qlresponses Structure
  property_count: 0
  slug: weaviate-graph-qlresponses-structure
- name: Weaviate Group Type Structure
  property_count: 0
  slug: weaviate-group-type-structure
- name: Weaviate Inverted Index Config Structure
  property_count: 9
  slug: weaviate-inverted-index-config-structure
- name: Weaviate Json Object Structure
  property_count: 0
  slug: weaviate-json-object-structure
- name: Weaviate Link Structure
  property_count: 4
  slug: weaviate-link-structure
- name: Weaviate Meta Structure
  property_count: 4
  slug: weaviate-meta-structure
- name: Weaviate Multi Tenancy Config Structure
  property_count: 3
  slug: weaviate-multi-tenancy-config-structure
- name: Weaviate Multiple Ref Structure
  property_count: 0
  slug: weaviate-multiple-ref-structure
- name: Weaviate Namespace List Response Structure
  property_count: 0
  slug: weaviate-namespace-list-response-structure
- name: Weaviate Namespace Structure
  property_count: 1
  slug: weaviate-namespace-structure
- name: Weaviate Nested Property Structure
  property_count: 9
  slug: weaviate-nested-property-structure
- name: Weaviate Node Shard Status Structure
  property_count: 10
  slug: weaviate-node-shard-status-structure
- name: Weaviate Node Stats Structure
  property_count: 2
  slug: weaviate-node-stats-structure
- name: Weaviate Node Status Structure
  property_count: 8
  slug: weaviate-node-status-structure
- name: Weaviate Nodes Status Response Structure
  property_count: 1
  slug: weaviate-nodes-status-response-structure
- name: Weaviate Object Structure
  property_count: 10
  slug: weaviate-object-structure
- name: Weaviate Object Ttl Config Structure
  property_count: 4
  slug: weaviate-object-ttl-config-structure
- name: Weaviate Objects Get Response Structure
  property_count: 0
  slug: weaviate-objects-get-response-structure
- name: Weaviate Objects List Response Structure
  property_count: 3
  slug: weaviate-objects-list-response-structure
- name: Weaviate Peer Update Structure
  property_count: 4
  slug: weaviate-peer-update-structure
- name: Weaviate Permission Structure
  property_count: 12
  slug: weaviate-permission-structure
- name: Weaviate Phone Number Structure
  property_count: 7
  slug: weaviate-phone-number-structure
- name: Weaviate Principal Structure
  property_count: 5
  slug: weaviate-principal-structure
- name: Weaviate Property Schema Structure
  property_count: 0
  slug: weaviate-property-schema-structure
- name: Weaviate Property Structure
  property_count: 12
  slug: weaviate-property-structure
- name: Weaviate Property Tokenize Request Structure
  property_count: 1
  slug: weaviate-property-tokenize-request-structure
- name: Weaviate Raft Statistics Structure
  property_count: 18
  slug: weaviate-raft-statistics-structure
- name: Weaviate Reference Meta Classification Structure
  property_count: 10
  slug: weaviate-reference-meta-classification-structure
- name: Weaviate Replication Async Config Structure
  property_count: 14
  slug: weaviate-replication-async-config-structure
- name: Weaviate Replication Config Structure
  property_count: 4
  slug: weaviate-replication-config-structure
- name: Weaviate Replication Replicate Details Replica Response Structure
  property_count: 12
  slug: weaviate-replication-replicate-details-replica-response-structure
- name: Weaviate Replication Replicate Details Replica Status Error Structure
  property_count: 2
  slug: weaviate-replication-replicate-details-replica-status-error-structure
- name: Weaviate Replication Replicate Details Replica Status Structure
  property_count: 3
  slug: weaviate-replication-replicate-details-replica-status-structure
- name: Weaviate Replication Replicate Force Delete Request Structure
  property_count: 5
  slug: weaviate-replication-replicate-force-delete-request-structure
- name: Weaviate Replication Replicate Force Delete Response Structure
  property_count: 2
  slug: weaviate-replication-replicate-force-delete-response-structure
- name: Weaviate Replication Replicate Replica Request Structure
  property_count: 5
  slug: weaviate-replication-replicate-replica-request-structure
- name: Weaviate Replication Replicate Replica Response Structure
  property_count: 1
  slug: weaviate-replication-replicate-replica-response-structure
- name: Weaviate Replication Scale Apply Response Structure
  property_count: 3
  slug: weaviate-replication-scale-apply-response-structure
- name: Weaviate Replication Scale Plan Structure
  property_count: 3
  slug: weaviate-replication-scale-plan-structure
- name: Weaviate Replication Shard Replicas Structure
  property_count: 2
  slug: weaviate-replication-shard-replicas-structure
- name: Weaviate Replication Sharding State Response Structure
  property_count: 1
  slug: weaviate-replication-sharding-state-response-structure
- name: Weaviate Replication Sharding State Structure
  property_count: 2
  slug: weaviate-replication-sharding-state-structure
- name: Weaviate Restore Config Structure
  property_count: 6
  slug: weaviate-restore-config-structure
- name: Weaviate Role Structure
  property_count: 2
  slug: weaviate-role-structure
- name: Weaviate Roles List Response Structure
  property_count: 0
  slug: weaviate-roles-list-response-structure
- name: Weaviate Schema Structure
  property_count: 3
  slug: weaviate-schema-structure
- name: Weaviate Shard Progress Structure
  property_count: 4
  slug: weaviate-shard-progress-structure
- name: Weaviate Shard Status Get Response Structure
  property_count: 3
  slug: weaviate-shard-status-get-response-structure
- name: Weaviate Shard Status List Structure
  property_count: 0
  slug: weaviate-shard-status-list-structure
- name: Weaviate Shard Status Structure
  property_count: 1
  slug: weaviate-shard-status-structure
- name: Weaviate Single Ref Structure
  property_count: 5
  slug: weaviate-single-ref-structure
- name: Weaviate Statistics Structure
  property_count: 13
  slug: weaviate-statistics-structure
- name: Weaviate Stopword Config Structure
  property_count: 3
  slug: weaviate-stopword-config-structure
- name: Weaviate Tenant Structure
  property_count: 2
  slug: weaviate-tenant-structure
- name: Weaviate Text Analyzer Config Structure
  property_count: 3
  slug: weaviate-text-analyzer-config-structure
- name: Weaviate Tokenize Request Structure
  property_count: 5
  slug: weaviate-tokenize-request-structure
- name: Weaviate Tokenize Response Structure
  property_count: 2
  slug: weaviate-tokenize-response-structure
- name: Weaviate Tokenizer User Dict Config Structure
  property_count: 2
  slug: weaviate-tokenizer-user-dict-config-structure
- name: Weaviate User Api Key Structure
  property_count: 1
  slug: weaviate-user-api-key-structure
- name: Weaviate User Own Info Structure
  property_count: 3
  slug: weaviate-user-own-info-structure
- name: Weaviate User Type Input Structure
  property_count: 0
  slug: weaviate-user-type-input-structure
- name: Weaviate User Type Output Structure
  property_count: 0
  slug: weaviate-user-type-output-structure
- name: Weaviate Vector Config Structure
  property_count: 3
  slug: weaviate-vector-config-structure
- name: Weaviate Vector Structure
  property_count: 0
  slug: weaviate-vector-structure
- name: Weaviate Vector Weights Structure
  property_count: 0
  slug: weaviate-vector-weights-structure
- name: Weaviate Vectors Structure
  property_count: 0
  slug: weaviate-vectors-structure
- name: Weaviate Where Filter Geo Range Structure
  property_count: 2
  slug: weaviate-where-filter-geo-range-structure
- name: Weaviate Where Filter Structure
  property_count: 16
  slug: weaviate-where-filter-structure
jsonld:
- class_count: 0
  name: Weaviate Context
  property_count: 402
  slug: weaviate-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Weaviate
nav: Providers
network: true
overview: 'Weaviate publishes 22 APIs on the [APIs.io](https://apis.io/) network, including authz API, backups API, batch API, and 19 more. Tagged areas include Vector Database, AI, Machine Learning, Semantic Search, and Open Source.


  The Weaviate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Weaviate''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, changelog, support, and 21 more developer resources.'
plans:
- name: Weaviate Plans Pricing
  plan_count: 3
  slug: weaviate-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 4
  name: Weaviate Rate Limits
  slug: weaviate-rate-limits
rules:
- name: Weaviate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: weaviate-jsonschema-spectral-rules
- name: Weaviate API Rules
  rule_count: 31
  severity_counts:
    error: 8
    hint: 0
    info: 10
    warn: 13
  slug: weaviate-spectral-rules
score:
  band: developing
  composite: 55.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.2
    developer_ergonomics: 56.5
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weaviate/refs/heads/main/screenshots/weaviate-2026-06-20T201320.png
security:
- kind: authentication
  name: Weaviate Authentication
  slug: weaviate-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Weaviate Domain Security
  slug: weaviate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Weaviate Trust Center
  slug: weaviate-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 2
skills:
- name: weaviate-cookbooks
  slug: weaviate-cookbooks
- name: weaviate
  slug: weaviate
slug: weaviate
tags:
- Vector Database
- AI
- Machine Learning
- Semantic Search
- Open Source
- GraphQL
- Kubernetes
use_cases:
- description: Build semantic and hybrid search applications using vector similarity and BM25 keyword search combined.
  name: Semantic Search
- description: Power Retrieval Augmented Generation (RAG) pipelines by storing and retrieving relevant context for large language model prompts.
  name: RAG Applications
- description: Search across text, images, and other modalities using unified vector representations.
  name: Multi-Modal Search
- description: Build recommendation engines using object similarity search to find related items based on vector proximity.
  name: AI-Powered Recommendations
---

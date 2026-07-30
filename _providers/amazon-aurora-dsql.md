---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Aurora Dsql Agentic Access
  operation_count: 11
  slug: amazon-aurora-dsql-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 2
apis:
- description: Operations for creating and managing Aurora DSQL clusters
  name: Amazon Aurora DSQL Clusters API
  slug: amazon-aurora-dsql-clusters-api
- description: Operations for managing multi-region cluster configurations
  name: Amazon Aurora DSQL Multi-Region Clusters API
  slug: amazon-aurora-dsql-multi-region-clusters-api
artifact_total: 92
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-aurora-dsql-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-aurora-dsql-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-aurora-dsql-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-aurora-dsql-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/well-known/amazon-aurora-dsql-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/well-known/amazon-aurora-dsql-security.txt
created: '2026-03-16'
description: Amazon Aurora DSQL is a distributed SQL database service optimized for transactional workloads. It provides a serverless, fully managed PostgreSQL-compatible database with built-in high availability, scalability, and global distribution capabilities.
examples:
- key_count: 3
  name: Aurora Dsql Cluster Status Example
  slug: aurora-dsql-cluster-status-example
- key_count: 3
  name: Aurora Dsql Cluster Summary Example
  slug: aurora-dsql-cluster-summary-example
- key_count: 3
  name: Aurora Dsql Create Cluster Input Example
  slug: aurora-dsql-create-cluster-input-example
- key_count: 3
  name: Aurora Dsql Create Cluster Output Example
  slug: aurora-dsql-create-cluster-output-example
- key_count: 3
  name: Aurora Dsql Create Multi Region Clusters Input Example
  slug: aurora-dsql-create-multi-region-clusters-input-example
- key_count: 3
  name: Aurora Dsql Create Multi Region Clusters Output Example
  slug: aurora-dsql-create-multi-region-clusters-output-example
- key_count: 3
  name: Aurora Dsql Delete Cluster Output Example
  slug: aurora-dsql-delete-cluster-output-example
- key_count: 3
  name: Aurora Dsql Delete Multi Region Clusters Input Example
  slug: aurora-dsql-delete-multi-region-clusters-input-example
- key_count: 3
  name: Aurora Dsql Delete Multi Region Clusters Output Example
  slug: aurora-dsql-delete-multi-region-clusters-output-example
- key_count: 3
  name: Aurora Dsql Get Cluster Endpoint Output Example
  slug: aurora-dsql-get-cluster-endpoint-output-example
- key_count: 3
  name: Aurora Dsql Get Cluster Output Example
  slug: aurora-dsql-get-cluster-output-example
- key_count: 3
  name: Aurora Dsql Linked Cluster Properties Example
  slug: aurora-dsql-linked-cluster-properties-example
- key_count: 3
  name: Aurora Dsql List Clusters Output Example
  slug: aurora-dsql-list-clusters-output-example
- key_count: 3
  name: Aurora Dsql List Tags For Resource Output Example
  slug: aurora-dsql-list-tags-for-resource-output-example
- key_count: 3
  name: Aurora Dsql Tag Resource Input Example
  slug: aurora-dsql-tag-resource-input-example
- key_count: 3
  name: Aurora Dsql Tag Resource Output Example
  slug: aurora-dsql-tag-resource-output-example
- key_count: 3
  name: Aurora Dsql Untag Resource Output Example
  slug: aurora-dsql-untag-resource-output-example
- key_count: 3
  name: Aurora Dsql Update Cluster Input Example
  slug: aurora-dsql-update-cluster-input-example
- key_count: 3
  name: Aurora Dsql Update Cluster Output Example
  slug: aurora-dsql-update-cluster-output-example
features:
- Serverless PostgreSQL-compatible distributed SQL database
- Automatic scaling with no database instances to manage
- Multi-region active-active replication for global distribution
- Built-in high availability with automatic failover
- Pay-per-use pricing based on I/O and storage
- Standard PostgreSQL client compatibility
- Transactional consistency across distributed nodes
- Integrated with AWS IAM for authentication
- Automatic software patching and maintenance
- Point-in-time recovery with continuous backups
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-aurora-dsql.png
integrations:
- Amazon VPC
- AWS IAM
- Amazon CloudWatch
- AWS CloudTrail
- Amazon RDS
- AWS KMS
- Amazon Route 53
- AWS PrivateLink
- Amazon S3
- AWS Secrets Manager
json_schemas:
- name: ClusterStatus
  property_count: 0
  slug: aurora-dsql-cluster-status
- name: ClusterSummary
  property_count: 0
  slug: aurora-dsql-cluster-summary
- name: CreateClusterInput
  property_count: 0
  slug: aurora-dsql-create-cluster-input
- name: CreateClusterOutput
  property_count: 0
  slug: aurora-dsql-create-cluster-output
- name: CreateMultiRegionClustersInput
  property_count: 0
  slug: aurora-dsql-create-multi-region-clusters-input
- name: CreateMultiRegionClustersOutput
  property_count: 0
  slug: aurora-dsql-create-multi-region-clusters-output
- name: DeleteClusterOutput
  property_count: 0
  slug: aurora-dsql-delete-cluster-output
- name: DeleteMultiRegionClustersInput
  property_count: 0
  slug: aurora-dsql-delete-multi-region-clusters-input
- name: DeleteMultiRegionClustersOutput
  property_count: 0
  slug: aurora-dsql-delete-multi-region-clusters-output
- name: GetClusterEndpointOutput
  property_count: 0
  slug: aurora-dsql-get-cluster-endpoint-output
- name: GetClusterOutput
  property_count: 0
  slug: aurora-dsql-get-cluster-output
- name: LinkedClusterProperties
  property_count: 0
  slug: aurora-dsql-linked-cluster-properties
- name: ListClustersOutput
  property_count: 0
  slug: aurora-dsql-list-clusters-output
- name: ListTagsForResourceOutput
  property_count: 0
  slug: aurora-dsql-list-tags-for-resource-output
- name: TagResourceInput
  property_count: 0
  slug: aurora-dsql-tag-resource-input
- name: TagResourceOutput
  property_count: 0
  slug: aurora-dsql-tag-resource-output
- name: UntagResourceOutput
  property_count: 0
  slug: aurora-dsql-untag-resource-output
- name: UpdateClusterInput
  property_count: 0
  slug: aurora-dsql-update-cluster-input
- name: UpdateClusterOutput
  property_count: 0
  slug: aurora-dsql-update-cluster-output
json_structures:
- name: Aurora Dsql Cluster Status Structure
  property_count: 0
  slug: aurora-dsql-cluster-status-structure
- name: Aurora Dsql Cluster Summary Structure
  property_count: 0
  slug: aurora-dsql-cluster-summary-structure
- name: Aurora Dsql Create Cluster Input Structure
  property_count: 0
  slug: aurora-dsql-create-cluster-input-structure
- name: Aurora Dsql Create Cluster Output Structure
  property_count: 0
  slug: aurora-dsql-create-cluster-output-structure
- name: Aurora Dsql Create Multi Region Clusters Input Structure
  property_count: 0
  slug: aurora-dsql-create-multi-region-clusters-input-structure
- name: Aurora Dsql Create Multi Region Clusters Output Structure
  property_count: 0
  slug: aurora-dsql-create-multi-region-clusters-output-structure
- name: Aurora Dsql Delete Cluster Output Structure
  property_count: 0
  slug: aurora-dsql-delete-cluster-output-structure
- name: Aurora Dsql Delete Multi Region Clusters Input Structure
  property_count: 0
  slug: aurora-dsql-delete-multi-region-clusters-input-structure
- name: Aurora Dsql Delete Multi Region Clusters Output Structure
  property_count: 0
  slug: aurora-dsql-delete-multi-region-clusters-output-structure
- name: Aurora Dsql Get Cluster Endpoint Output Structure
  property_count: 0
  slug: aurora-dsql-get-cluster-endpoint-output-structure
- name: Aurora Dsql Get Cluster Output Structure
  property_count: 0
  slug: aurora-dsql-get-cluster-output-structure
- name: Aurora Dsql Linked Cluster Properties Structure
  property_count: 0
  slug: aurora-dsql-linked-cluster-properties-structure
- name: Aurora Dsql List Clusters Output Structure
  property_count: 0
  slug: aurora-dsql-list-clusters-output-structure
- name: Aurora Dsql List Tags For Resource Output Structure
  property_count: 0
  slug: aurora-dsql-list-tags-for-resource-output-structure
- name: Aurora Dsql Tag Resource Input Structure
  property_count: 0
  slug: aurora-dsql-tag-resource-input-structure
- name: Aurora Dsql Tag Resource Output Structure
  property_count: 0
  slug: aurora-dsql-tag-resource-output-structure
- name: Aurora Dsql Untag Resource Output Structure
  property_count: 0
  slug: aurora-dsql-untag-resource-output-structure
- name: Aurora Dsql Update Cluster Input Structure
  property_count: 0
  slug: aurora-dsql-update-cluster-input-structure
- name: Aurora Dsql Update Cluster Output Structure
  property_count: 0
  slug: aurora-dsql-update-cluster-output-structure
jsonld:
- class_count: 4
  name: Amazon Aurora Dsql Context
  property_count: 0
  slug: amazon-aurora-dsql-context
layout: provider
modified: '2026-06-20'
name: Amazon Aurora DSQL
nav: Providers
network: true
overview: 'Amazon Aurora DSQL publishes 2 APIs on the [APIs.io](https://apis.io/) network: Clusters API and Multi-Region Clusters API. Tagged areas include Amazon Aurora DSQL, Distributed SQL, PostgreSQL, and Serverless.


  The Amazon Aurora DSQL catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Aurora DSQL''s developer surface includes authentication and 5 more developer resources.'
random_paper: 18
rules:
- name: Amazon Aurora DSQL API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-aurora-dsql-jsonschema-spectral-rules
- name: Amazon Aurora DSQL API Rules
  rule_count: 17
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 9
  slug: amazon-aurora-dsql-spectral-rules
score:
  band: thin
  composite: 37.0
  delta: -0.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 74.6
    developer_ergonomics: 10.9
    discoverability: 77.8
    governance: 69.8
    operational_transparency: 0.0
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/screenshots/amazon-aurora-dsql-2026-07-25T195931.png
security:
- kind: authentication
  name: Amazon Aurora Dsql Authentication
  slug: amazon-aurora-dsql-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Aurora Dsql Domain Security
  slug: amazon-aurora-dsql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Aurora Dsql Vulnerability Disclosure
  slug: amazon-aurora-dsql-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-aurora-dsql
tags:
- Amazon Aurora DSQL
- Distributed SQL
- PostgreSQL
- Serverless
use_cases:
- Build globally distributed transactional applications
- Run PostgreSQL workloads without managing instances
- Deploy active-active multi-region database architectures
- Migrate PostgreSQL applications to serverless infrastructure
- Build applications requiring strong consistency at global scale
- Implement high-throughput transactional microservices
---

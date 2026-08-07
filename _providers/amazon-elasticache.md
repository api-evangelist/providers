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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Elasticache Agentic Access
  operation_count: 5
  slug: amazon-elasticache-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
apis:
- description: The Amazon ElastiCache API API from Amazon ElastiCache — 1 operation(s) for amazon elasticache api.
  name: Amazon ElastiCache Amazon ElastiCache API API
  slug: amazon-elasticache-amazon-elasticache-api-api
- description: 'The #CreateReplicationGroup API from Amazon ElastiCache — 1 operation(s) for #createreplicationgroup.'
  name: 'Amazon ElastiCache #CreateReplicationGroup API'
  slug: amazon-elasticache-createreplicationgroup-api
- description: 'The #DeleteCacheCluster API from Amazon ElastiCache — 1 operation(s) for #deletecachecluster.'
  name: 'Amazon ElastiCache #DeleteCacheCluster API'
  slug: amazon-elasticache-deletecachecluster-api
- description: 'The #DescribeReplicationGroups API from Amazon ElastiCache — 1 operation(s) for #describereplicationgroups.'
  name: 'Amazon ElastiCache #DescribeReplicationGroups API'
  slug: amazon-elasticache-describereplicationgroups-api
arazzos:
- description: Describe a cluster, branch on its status, and confirm its replication group.
  name: Amazon ElastiCache Audit Cluster Readiness
  slug: amazon-elasticache-audit-cluster-readiness-workflow
- description: Create a cache cluster, confirm it, then delete it with a final snapshot.
  name: Amazon ElastiCache Cache Cluster Lifecycle
  slug: amazon-elasticache-cache-cluster-lifecycle-workflow
- description: Read a source cluster's config, create a matching cluster, and poll it.
  name: Amazon ElastiCache Clone Cluster Config
  slug: amazon-elasticache-clone-cluster-config-workflow
- description: Snapshot and delete a cache cluster, then poll until it is fully removed.
  name: Amazon ElastiCache Decommission Cache Cluster
  slug: amazon-elasticache-decommission-cache-cluster-workflow
- description: Create a cache cluster and poll until it reports an available status.
  name: Amazon ElastiCache Provision Cache Cluster
  slug: amazon-elasticache-provision-cache-cluster-workflow
- description: Create a Redis replication group and poll until it becomes available.
  name: Amazon ElastiCache Provision Replication Group
  slug: amazon-elasticache-provision-replication-group-workflow
- description: Verify an existing cluster, then build a replication group around it and poll.
  name: Amazon ElastiCache Replicate Existing Cluster
  slug: amazon-elasticache-replicate-existing-cluster-workflow
artifact_total: 45
collections:
- collection_type: postman
  name: Amazon ElastiCache API
  slug: postman-amazon-elasticache
- collection_type: open
  name: Amazon ElastiCache API
  slug: open-amazon-elasticache
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-elasticache-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-elasticache-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-elasticache-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-elasticache-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-elasticache-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-elasticache/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-audit-cluster-readiness-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-cache-cluster-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-clone-cluster-config-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-decommission-cache-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-provision-cache-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-provision-replication-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-replicate-existing-cluster-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/elasticache/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elasticache/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/elasticache/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/elasticache/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/elasticache
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-elasticache-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-elasticache-vocabulary.yaml
created: '2024-01-15'
description: Amazon ElastiCache is a fully managed in-memory caching service supporting Redis and Memcached. ElastiCache makes it easy to deploy, operate, and scale popular open-source compatible in-memory data stores, improving the performance of web applications.
examples:
- key_count: 10
  name: Amazon Elasticache Cache Cluster Example
  slug: amazon-elasticache-cache-cluster-example
- key_count: 10
  name: Amazon Elasticache Cachecluster Example
  slug: amazon-elasticache-cachecluster-example
- key_count: 1
  name: Amazon Elasticache Create Cache Cluster Result Example
  slug: amazon-elasticache-create-cache-cluster-result-example
- key_count: 2
  name: Amazon Elasticache Describe Cache Clusters Result Example
  slug: amazon-elasticache-describe-cache-clusters-result-example
features:
- description: Fully managed Redis with replication, clustering, and persistence
  name: Redis Support
- description: Fully managed Memcached for simple distributed caching
  name: Memcached Support
- description: Automatic failover with Multi-AZ replication groups
  name: Multi-AZ Replication
- description: Encryption at-rest and in-transit for compliance requirements
  name: Encryption
- description: Scheduled automatic backups with point-in-time recovery
  name: Automatic Backups
finops:
- name: Amazon Elasticache Finops
  service_category: API
  slug: amazon-elasticache-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: CacheCluster
  property_count: 16
  slug: amazon-elasticache-cache-cluster
- name: Amazon ElastiCache CacheCluster
  property_count: 23
  slug: amazon-elasticache-cachecluster
- name: CreateCacheClusterResult
  property_count: 1
  slug: amazon-elasticache-create-cache-cluster-result
- name: DescribeCacheClustersResult
  property_count: 2
  slug: amazon-elasticache-describe-cache-clusters-result
json_structures:
- name: Amazon Elasticache Cache Cluster Structure
  property_count: 16
  slug: amazon-elasticache-cache-cluster-structure
- name: Amazon Elasticache Cachecluster Structure
  property_count: 23
  slug: amazon-elasticache-cachecluster-structure
- name: Amazon Elasticache Create Cache Cluster Result Structure
  property_count: 1
  slug: amazon-elasticache-create-cache-cluster-result-structure
- name: Amazon Elasticache Describe Cache Clusters Result Structure
  property_count: 2
  slug: amazon-elasticache-describe-cache-clusters-result-structure
jsonld:
- class_count: 0
  name: Amazon Elasticache Context
  property_count: 3
  slug: amazon-elasticache-context
layout: provider
modified: '2026-05-19'
name: Amazon ElastiCache
nav: Providers
network: true
overview: 'Amazon ElastiCache publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Amazon ElastiCache API API, #CreateReplicationGroup API, #DeleteCacheCluster API, and 1 more. Tagged areas include Amazon Web Services, Caching, Database, ElastiCache, and In-Memory.


  The Amazon ElastiCache catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon ElastiCache''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 27 more developer resources.'
plans:
- name: Amazon Elasticache Plans Pricing
  plan_count: 3
  slug: amazon-elasticache-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Amazon Elasticache Rate Limits
  slug: amazon-elasticache-rate-limits
rules:
- name: Amazon ElastiCache API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-elasticache-jsonschema-spectral-rules
- name: Amazon ElastiCache API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: amazon-elasticache-spectral-rules
score:
  band: exemplar
  composite: 70.8
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 76.7
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 63.2
  previous_composite: 70.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-elasticache/refs/heads/main/screenshots/amazon-elasticache-2026-06-20T171652.png
security:
- kind: authentication
  name: Amazon Elasticache Authentication
  slug: amazon-elasticache-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Elasticache Domain Security
  slug: amazon-elasticache-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Elasticache Vulnerability Disclosure
  slug: amazon-elasticache-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Elasticache Trust Center
  slug: amazon-elasticache-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-elasticache
tags:
- Amazon Web Services
- Caching
- Database
- ElastiCache
- In-Memory
- Memcached
- Redis
use_cases:
- description: Store and manage user session data for web applications
  name: Session Management
- description: Cache expensive database queries to reduce latency
  name: Database Query Caching
- description: Process and cache real-time data streams for analytics dashboards
  name: Real-Time Analytics
- description: Build real-time leaderboards and gaming backends with Redis sorted sets
  name: Leaderboards and Gaming
website: https://aws.amazon.com/elasticache/
---

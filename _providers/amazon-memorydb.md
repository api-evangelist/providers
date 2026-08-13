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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Amazon Memorydb Agentic Access
  operation_count: 34
  slug: amazon-memorydb-agentic-access
  summary_line: 34 operations · 22 acting
api_count: 12
apis:
- description: The ACLs API from Amazon MemoryDB — 1 operation(s) for acls.
  name: Amazon MemoryDB ACLs API
  slug: amazon-memorydb-acls-api
- description: The Clusters API from Amazon MemoryDB — 1 operation(s) for clusters.
  name: Amazon MemoryDB Clusters API
  slug: amazon-memorydb-clusters-api
- description: The EngineVersions API from Amazon MemoryDB — 1 operation(s) for engineversions.
  name: Amazon MemoryDB EngineVersions API
  slug: amazon-memorydb-engineversions-api
- description: The Events API from Amazon MemoryDB — 1 operation(s) for events.
  name: Amazon MemoryDB Events API
  slug: amazon-memorydb-events-api
- description: The NodeTypes API from Amazon MemoryDB — 1 operation(s) for nodetypes.
  name: Amazon MemoryDB NodeTypes API
  slug: amazon-memorydb-nodetypes-api
- description: The ParameterGroups API from Amazon MemoryDB — 1 operation(s) for parametergroups.
  name: Amazon MemoryDB ParameterGroups API
  slug: amazon-memorydb-parametergroups-api
- description: The ReservedNodes API from Amazon MemoryDB — 2 operation(s) for reservednodes.
  name: Amazon MemoryDB ReservedNodes API
  slug: amazon-memorydb-reservednodes-api
- description: The Shards API from Amazon MemoryDB — 1 operation(s) for shards.
  name: Amazon MemoryDB Shards API
  slug: amazon-memorydb-shards-api
- description: The Snapshots API from Amazon MemoryDB — 2 operation(s) for snapshots.
  name: Amazon MemoryDB Snapshots API
  slug: amazon-memorydb-snapshots-api
- description: The SubnetGroups API from Amazon MemoryDB — 1 operation(s) for subnetgroups.
  name: Amazon MemoryDB SubnetGroups API
  slug: amazon-memorydb-subnetgroups-api
- description: The Tags API from Amazon MemoryDB — 1 operation(s) for tags.
  name: Amazon MemoryDB Tags API
  slug: amazon-memorydb-tags-api
- description: The Users API from Amazon MemoryDB — 1 operation(s) for users.
  name: Amazon MemoryDB Users API
  slug: amazon-memorydb-users-api
artifact_total: 74
collections:
- collection_type: postman
  name: Amazon MemoryDB ACLs API
  slug: postman-amazon-memorydb-acls-api
- collection_type: postman
  name: Amazon MemoryDB ACLs Clusters API
  slug: postman-amazon-memorydb-clusters-api
- collection_type: postman
  name: Amazon MemoryDB ACLs EngineVersions API
  slug: postman-amazon-memorydb-engineversions-api
- collection_type: postman
  name: Amazon MemoryDB ACLs Events API
  slug: postman-amazon-memorydb-events-api
- collection_type: postman
  name: Amazon MemoryDB ACLs NodeTypes API
  slug: postman-amazon-memorydb-nodetypes-api
- collection_type: postman
  name: Amazon MemoryDB ACLs ParameterGroups API
  slug: postman-amazon-memorydb-parametergroups-api
- collection_type: postman
  name: Amazon MemoryDB ACLs ReservedNodes API
  slug: postman-amazon-memorydb-reservednodes-api
- collection_type: postman
  name: Amazon MemoryDB ACLs Shards API
  slug: postman-amazon-memorydb-shards-api
- collection_type: postman
  name: Amazon MemoryDB ACLs Snapshots API
  slug: postman-amazon-memorydb-snapshots-api
- collection_type: postman
  name: Amazon MemoryDB ACLs SubnetGroups API
  slug: postman-amazon-memorydb-subnetgroups-api
- collection_type: postman
  name: Amazon MemoryDB ACLs Tags API
  slug: postman-amazon-memorydb-tags-api
- collection_type: postman
  name: Amazon MemoryDB ACLs Users API
  slug: postman-amazon-memorydb-users-api
- collection_type: open
  name: Amazon MemoryDB API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-memorydb/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-memorydb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-memorydb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-memorydb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-memorydb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-memorydb-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/memorydb/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/memorydb/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/memorydb/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-memorydb-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-memorydb-vocabulary.yaml
created: '2026-03-16'
description: Amazon MemoryDB for Redis is a durable, in-memory database service that delivers ultra-fast performance. It is Redis-compatible and provides microsecond reads, low single-digit millisecond writes, and enterprise-grade security.
examples:
- key_count: 4
  name: Memorydb Api Acl Example
  slug: memorydb-api-acl-example
- key_count: 9
  name: Memorydb Api Cluster Example
  slug: memorydb-api-cluster-example
- key_count: 8
  name: Memorydb Api Create Cluster Request Example
  slug: memorydb-api-create-cluster-request-example
- key_count: 2
  name: Memorydb Api Describe Clusters Response Example
  slug: memorydb-api-describe-clusters-response-example
- key_count: 4
  name: Memorydb Api Parameter Group Example
  slug: memorydb-api-parameter-group-example
- key_count: 5
  name: Memorydb Api Snapshot Example
  slug: memorydb-api-snapshot-example
- key_count: 4
  name: Memorydb Api Subnet Group Example
  slug: memorydb-api-subnet-group-example
- key_count: 2
  name: Memorydb Api Tag Example
  slug: memorydb-api-tag-example
- key_count: 4
  name: Memorydb Api User Example
  slug: memorydb-api-user-example
features:
- description: Fully compatible with Redis and Memcached data structures, APIs, and commands.
  name: Redis Compatibility
- description: Multi-AZ transactional log ensures data durability without sacrificing performance.
  name: Durable In-Memory Storage
- description: Microsecond read and low single-digit millisecond write latency at scale.
  name: Ultra-Fast Performance
- description: Create and manage MemoryDB clusters, shards, and replicas with ease.
  name: Cluster Management
- description: Create point-in-time snapshots for backup and restore operations.
  name: Snapshot and Restore
- description: Fine-grained access control with user-based ACLs for security.
  name: Access Control Lists
- description: Deploy clusters across multiple AWS regions for global low-latency access.
  name: Multi-Region Clusters
finops:
- name: Amazon Memorydb Finops
  service_category: API
  slug: amazon-memorydb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-memorydb.png
json_schemas:
- name: ACL
  property_count: 4
  slug: memorydb-api-acl
- name: Cluster
  property_count: 9
  slug: memorydb-api-cluster
- name: CreateClusterRequest
  property_count: 8
  slug: memorydb-api-create-cluster-request
- name: DescribeClustersResponse
  property_count: 2
  slug: memorydb-api-describe-clusters-response
- name: ParameterGroup
  property_count: 4
  slug: memorydb-api-parameter-group
- name: Snapshot
  property_count: 5
  slug: memorydb-api-snapshot
- name: SubnetGroup
  property_count: 4
  slug: memorydb-api-subnet-group
- name: Tag
  property_count: 2
  slug: memorydb-api-tag
- name: User
  property_count: 4
  slug: memorydb-api-user
json_structures:
- name: Memorydb Api Acl Structure
  property_count: 4
  slug: memorydb-api-acl-structure
- name: Memorydb Api Cluster Structure
  property_count: 9
  slug: memorydb-api-cluster-structure
- name: Memorydb Api Create Cluster Request Structure
  property_count: 8
  slug: memorydb-api-create-cluster-request-structure
- name: Memorydb Api Describe Clusters Response Structure
  property_count: 2
  slug: memorydb-api-describe-clusters-response-structure
- name: Memorydb Api Parameter Group Structure
  property_count: 4
  slug: memorydb-api-parameter-group-structure
- name: Memorydb Api Snapshot Structure
  property_count: 5
  slug: memorydb-api-snapshot-structure
- name: Memorydb Api Subnet Group Structure
  property_count: 4
  slug: memorydb-api-subnet-group-structure
- name: Memorydb Api Tag Structure
  property_count: 2
  slug: memorydb-api-tag-structure
- name: Memorydb Api User Structure
  property_count: 4
  slug: memorydb-api-user-structure
jsonld:
- class_count: 11
  name: Amazon Memorydb Memorydb Api Context
  property_count: 21
  slug: amazon-memorydb-memorydb-api-context
layout: provider
modified: '2026-05-19'
name: Amazon MemoryDB
nav: Providers
network: true
overview: 'Amazon MemoryDB publishes 12 APIs on the [APIs.io](https://apis.io/) network, including ACLs API, Clusters API, EngineVersions API, and 9 more. Tagged areas include Broadcasting, Media Processing, and Media.


  The Amazon MemoryDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MemoryDB''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 12 more developer resources.'
plans:
- name: Amazon Memorydb Plans Pricing
  plan_count: 3
  slug: amazon-memorydb-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 5
  name: Amazon Memorydb Rate Limits
  slug: amazon-memorydb-rate-limits
rules:
- name: Amazon MemoryDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-memorydb-jsonschema-spectral-rules
- name: Amazon MemoryDB API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 12
  slug: amazon-memorydb-spectral-rules
score:
  band: developing
  composite: 45.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 23.5
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-memorydb/refs/heads/main/screenshots/amazon-memorydb-2026-06-20T171744.png
security:
- kind: authentication
  name: Amazon Memorydb Authentication
  slug: amazon-memorydb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Memorydb Domain Security
  slug: amazon-memorydb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Memorydb Vulnerability Disclosure
  slug: amazon-memorydb-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Memorydb Trust Center
  slug: amazon-memorydb-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-memorydb
tags:
- Broadcasting
- Media Processing
- Media
use_cases:
- description: Store session data with ultra-low latency for modern microservices applications.
  name: Microservices Session Management
- description: Maintain sorted sets for gaming leaderboards and ranking systems.
  name: Real-Time Leaderboards
- description: Use as a durable caching layer to reduce database load and improve response times.
  name: Caching Layer
- description: Build real-time messaging and event streaming with Redis pub/sub patterns.
  name: Pub/Sub Messaging
website: https://aws.amazon.com/memorydb/
---

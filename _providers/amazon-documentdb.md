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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Documentdb Agentic Access
  operation_count: 5
  slug: amazon-documentdb-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The Amazon DocumentDB API API from Amazon DocumentDB — 1 operation(s) for amazon documentdb api.
  name: Amazon DocumentDB Amazon DocumentDB API API
  slug: amazon-documentdb-amazon-documentdb-api-api
- description: 'The #CreateDBInstance API from Amazon DocumentDB — 1 operation(s) for #createdbinstance.'
  name: 'Amazon DocumentDB #CreateDBInstance API'
  slug: amazon-documentdb-createdbinstance-api
- description: 'The #DeleteDBCluster API from Amazon DocumentDB — 1 operation(s) for #deletedbcluster.'
  name: 'Amazon DocumentDB #DeleteDBCluster API'
  slug: amazon-documentdb-deletedbcluster-api
- description: 'The #DescribeDBInstances API from Amazon DocumentDB — 1 operation(s) for #describedbinstances.'
  name: 'Amazon DocumentDB #DescribeDBInstances API'
  slug: amazon-documentdb-describedbinstances-api
arazzos:
- description: Add an instance to an existing cluster and poll until the instance is available.
  name: Amazon DocumentDB Add Instance and Await Available
  slug: amazon-documentdb-add-instance-await-available-workflow
- description: Create a cluster, wait until available, then add and await a primary instance.
  name: Amazon DocumentDB Bootstrap Cluster with Primary Instance
  slug: amazon-documentdb-bootstrap-cluster-with-instance-workflow
- description: Verify a cluster exists, delete it with a final snapshot, then poll until it is gone.
  name: Amazon DocumentDB Decommission Cluster with Final Snapshot
  slug: amazon-documentdb-decommission-cluster-with-final-snapshot-workflow
- description: Describe a cluster, then describe a member instance and the wider instance fleet.
  name: Amazon DocumentDB Inventory Cluster and Instances
  slug: amazon-documentdb-inventory-cluster-and-instances-workflow
- description: Create a DocumentDB cluster and poll until it reports the available status.
  name: Amazon DocumentDB Provision Cluster and Await Available
  slug: amazon-documentdb-provision-cluster-await-available-workflow
- description: Add a replica instance to a cluster, wait for it, then confirm cluster membership.
  name: Amazon DocumentDB Scale Out Read Replica
  slug: amazon-documentdb-scale-out-read-replica-workflow
artifact_total: 53
collections:
- collection_type: postman
  name: Amazon DocumentDB API
  slug: postman-amazon-documentdb
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon DocumentDB Amazon DocumentDB API API
  slug: open-amazon-documentdb-amazon-documentdb-api-api
- collection_type: open
  name: 'Amazon DocumentDB Amazon DocumentDB API #CreateDBInstance API'
  slug: open-amazon-documentdb-createdbinstance-api
- collection_type: open
  name: 'Amazon DocumentDB Amazon DocumentDB API #DeleteDBCluster API'
  slug: open-amazon-documentdb-deletedbcluster-api
- collection_type: open
  name: 'Amazon DocumentDB Amazon DocumentDB API #DescribeDBInstances API'
  slug: open-amazon-documentdb-describedbinstances-api
- collection_type: open
  name: Amazon DocumentDB API
  slug: open-amazon-documentdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-documentdb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-documentdb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-documentdb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-documentdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-documentdb-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-documentdb/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-documentdb-add-instance-await-available-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-documentdb-bootstrap-cluster-with-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-documentdb-decommission-cluster-with-final-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-documentdb-inventory-cluster-and-instances-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-documentdb-provision-cluster-await-available-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-documentdb-scale-out-read-replica-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/documentdb/
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
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/docdb/
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
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-documentdb
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-documentdb-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-documentdb-vocabulary.yaml
created: '2024-01-15'
description: Amazon DocumentDB is a fully managed, MongoDB-compatible document database service that makes it easy to set up, operate, and scale MongoDB-compatible databases in the cloud. DocumentDB is designed from the ground up to give you the performance, scalability, and availability you need when operating mission-critical MongoDB workloads at scale.
examples:
- key_count: 3
  name: Amazon Documentdb Dbcluster Example
  slug: amazon-documentdb-dbcluster-example
- key_count: 1
  name: Documentdb Openapi Create Db Cluster Result Example
  slug: documentdb-openapi-create-db-cluster-result-example
- key_count: 3
  name: Documentdb Openapi Db Cluster Example
  slug: documentdb-openapi-db-cluster-example
- key_count: 2
  name: Documentdb Openapi Describe Db Clusters Result Example
  slug: documentdb-openapi-describe-db-clusters-result-example
features:
- description: Automatically scales capacity up or down in fine-grained increments based on application demand, with up to 90% cost savings versus peak provisioning.
  name: Serverless Architecture
- description: Migrate applications typically without code changes or downtime using existing MongoDB drivers and tools.
  name: MongoDB Compatibility
- description: Automatically replicates data across up to 10 AWS Regions for low-latency reads and disaster recovery.
  name: Global Clusters
- description: Eliminates database patching, backups, and monitoring overhead so you can focus on application development.
  name: Fully Managed
- description: Provides up to 40% cost savings for I/O-intensive workloads with predictable pricing.
  name: I/O-Optimized Storage
- description: Offers memory-optimized instance types with up to 43% cost savings for large workloads.
  name: Memory-Optimized Instances
- description: Continuous backups to Amazon S3 and point-in-time recovery within the backup retention window.
  name: Automated Backups
- description: Data is encrypted using AES-256, with support for AWS KMS customer-managed keys.
  name: Encryption at Rest and in Transit
finops:
- name: Amazon Documentdb Finops
  service_category: API
  slug: amazon-documentdb-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon DocumentDB DBCluster
  property_count: 20
  slug: amazon-documentdb-dbcluster
- name: CreateDBClusterResult
  property_count: 1
  slug: documentdb-openapi-create-db-cluster-result
- name: DBCluster
  property_count: 14
  slug: documentdb-openapi-db-cluster
- name: DescribeDBClustersResult
  property_count: 2
  slug: documentdb-openapi-describe-db-clusters-result
json_structures:
- name: Amazon Documentdb Dbcluster Structure
  property_count: 20
  slug: amazon-documentdb-dbcluster-structure
- name: Documentdb Openapi Create Db Cluster Result Structure
  property_count: 1
  slug: documentdb-openapi-create-db-cluster-result-structure
- name: Documentdb Openapi Db Cluster Structure
  property_count: 14
  slug: documentdb-openapi-db-cluster-structure
- name: Documentdb Openapi Describe Db Clusters Result Structure
  property_count: 2
  slug: documentdb-openapi-describe-db-clusters-result-structure
jsonld:
- class_count: 3
  name: Amazon Documentdb Context
  property_count: 28
  slug: amazon-documentdb-context
layout: provider
modified: '2026-05-19'
name: Amazon DocumentDB
nav: Providers
network: true
overview: 'Amazon DocumentDB publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Amazon DocumentDB API API, #CreateDBInstance API, #DeleteDBCluster API, and 1 more. Tagged areas include Amazon Web Services, Database, Document Database, DocumentDB, and Managed Database.


  The Amazon DocumentDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon DocumentDB''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 25 more developer resources.'
plans:
- name: Amazon Documentdb Plans Pricing
  plan_count: 3
  slug: amazon-documentdb-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Amazon Documentdb Rate Limits
  slug: amazon-documentdb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon DocumentDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-documentdb-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: Amazon DocumentDB API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 18
  slug: amazon-documentdb-spectral-rules
score:
  band: strong
  composite: 60.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 28.8
    contract_quality: 70.1
    developer_ergonomics: 69.0
    discoverability: 70.4
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-documentdb/refs/heads/main/screenshots/amazon-documentdb-2026-06-20T171627.png
security:
- kind: authentication
  name: Amazon Documentdb Authentication
  slug: amazon-documentdb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Documentdb Domain Security
  slug: amazon-documentdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Documentdb Vulnerability Disclosure
  slug: amazon-documentdb-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Documentdb Trust Center
  slug: amazon-documentdb-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-documentdb
tags:
- Amazon Web Services
- Database
- Document Database
- DocumentDB
- Managed Database
- MongoDB
- NoSQL
use_cases:
- description: Store and retrieve flexible JSON-structured content with rich query capabilities for CMS platforms.
  name: Content Management Systems
- description: Manage product catalogs, user profiles, and order data with scalable document storage.
  name: E-Commerce Platforms
- description: Power real-time application backends with low-latency, scalable document storage.
  name: Mobile and Web Applications
- description: Store and retrieve context, embeddings, and conversational history for AI-powered agentic applications.
  name: Generative AI Applications
- description: Handle player profiles, leaderboards, and game state with flexible schema and high throughput.
  name: Gaming Applications
website: https://aws.amazon.com/developer/
---

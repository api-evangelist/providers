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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Elasticache Agentic Access
  operation_count: 5
  slug: amazon-elasticache-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Amazon ElastiCache API API from Amazon ElastiCache — 1 operation(s) for amazon elasticache api.
  name: Amazon ElastiCache Amazon ElastiCache API
  slug: amazon-elasticache-amazon-elasticache-api-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Cache Parameter Group API from Amazon ElastiCache — 5 operation(s) for elasticache cache parameter group.
  name: Amazon ElastiCache Elasticache Cache Parameter Group API
  slug: amazon-elasticache-cache-parameter-group-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Cache Security Group API from Amazon ElastiCache — 3 operation(s) for elasticache cache security group.
  name: Amazon ElastiCache Elasticache Cache Security Group API
  slug: amazon-elasticache-cache-security-group-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Cache Subnet Group API from Amazon ElastiCache — 4 operation(s) for elasticache cache subnet group.
  name: Amazon ElastiCache Elasticache Cache Subnet Group API
  slug: amazon-elasticache-cache-subnet-group-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Global Replication Group API from Amazon ElastiCache — 5 operation(s) for elasticache global replication group.
  name: Amazon ElastiCache Elasticache Global Replication Group API
  slug: amazon-elasticache-global-replication-group-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Migration API from Amazon ElastiCache — 3 operation(s) for elasticache migration.
  name: Amazon ElastiCache Elasticache Migration API
  slug: amazon-elasticache-migration-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Operations API from Amazon ElastiCache — 27 operation(s) for elasticache operations.
  name: Amazon ElastiCache Elasticache Operations API
  slug: amazon-elasticache-operations-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Serverless Cache API from Amazon ElastiCache — 4 operation(s) for elasticache serverless cache.
  name: Amazon ElastiCache Elasticache Serverless Cache API
  slug: amazon-elasticache-serverless-cache-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Serverless Cache Snapshot API from Amazon ElastiCache — 4 operation(s) for elasticache serverless cache snapshot.
  name: Amazon ElastiCache Elasticache Serverless Cache Snapshot API
  slug: amazon-elasticache-serverless-cache-snapshot-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Snapshot API from Amazon ElastiCache — 3 operation(s) for elasticache snapshot.
  name: Amazon ElastiCache Elasticache Snapshot API
  slug: amazon-elasticache-snapshot-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Tag API from Amazon ElastiCache — 3 operation(s) for elasticache tag.
  name: Amazon ElastiCache Elasticache Tag API
  slug: amazon-elasticache-tag-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache Update Action API from Amazon ElastiCache — 3 operation(s) for elasticache update action.
  name: Amazon ElastiCache Elasticache Update Action API
  slug: amazon-elasticache-update-action-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache User API from Amazon ElastiCache — 4 operation(s) for elasticache user.
  name: Amazon ElastiCache Elasticache User API
  slug: amazon-elasticache-user-api
- baseURL: https://elasticache.amazonaws.com
  baseurl_source: declared
  description: The Elasticache User Group API from Amazon ElastiCache — 4 operation(s) for elasticache user group.
  name: Amazon ElastiCache Elasticache User Group API
  slug: amazon-elasticache-user-group-api
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
artifact_total: 60
collections:
- collection_type: postman
  name: Amazon ElastiCache API
  slug: postman-amazon-elasticache
- collection_type: open
  name: Amazon ElastiCache Amazon ElastiCache API API
  slug: open-amazon-elasticache-amazon-elasticache-api-api
- collection_type: open
  name: 'Amazon ElastiCache Amazon ElastiCache API #CreateReplicationGroup API'
  slug: open-amazon-elasticache-createreplicationgroup-api
- collection_type: open
  name: 'Amazon ElastiCache Amazon ElastiCache API #DeleteCacheCluster API'
  slug: open-amazon-elasticache-deletecachecluster-api
- collection_type: open
  name: 'Amazon ElastiCache Amazon ElastiCache API #DescribeReplicationGroups API'
  slug: open-amazon-elasticache-describereplicationgroups-api
- collection_type: open
  name: Amazon ElastiCache API
  slug: open-amazon-elasticache
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-elasticache/plans/amazon-elasticache-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-elasticache-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-elasticache/rate-limits/amazon-elasticache-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-elasticache-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-elasticache/finops/amazon-elasticache-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-elasticache-finops.yml
- group: other
  href: https://artifacts.apis.io/amazon-elasticache/capabilities/amazon-elasticache-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-elasticache-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/elasticache/
- group: agent
  href: https://artifacts.apis.io/amazon-elasticache/agentic-access/amazon-elasticache-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-elasticache-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-elasticache/security/amazon-elasticache-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-elasticache-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-elasticache/security/amazon-elasticache-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-elasticache-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-elasticache/security/amazon-elasticache-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-elasticache-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-elasticache/authentication/amazon-elasticache-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-elasticache-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-elasticache/overview
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/arazzo/amazon-elasticache-audit-cluster-readiness-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-audit-cluster-readiness-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/arazzo/amazon-elasticache-cache-cluster-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-cache-cluster-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/arazzo/amazon-elasticache-clone-cluster-config-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-clone-cluster-config-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/arazzo/amazon-elasticache-decommission-cache-cluster-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-decommission-cache-cluster-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/arazzo/amazon-elasticache-provision-cache-cluster-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-provision-cache-cluster-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/arazzo/amazon-elasticache-provision-replication-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-elasticache-provision-replication-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/arazzo/amazon-elasticache-replicate-existing-cluster-workflow.yml
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
  href: https://artifacts.apis.io/amazon-elasticache/rules/amazon-elasticache-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-elasticache-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-elasticache/vocabulary/amazon-elasticache-vocabulary.yaml
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
- has_sources: true
  method: derived
  name: Amazon Elasticache Finops
  primary_unit: gb-hour
  service_category: ''
  slug: amazon-elasticache-finops
  template: false
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
modified: '2026-09-16'
name: Amazon ElastiCache
nav: Providers
network: true
overview: 'Amazon ElastiCache publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Amazon ElastiCache API, Elasticache Cache Parameter Group API, Elasticache Cache Security Group API, and 11 more. Tagged areas include Amazon Web Services, Caching, Database, ElastiCache, and In-Memory.


  The Amazon ElastiCache catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon ElastiCache''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 32 more developer resources.'
plans:
- name: Amazon Elasticache Plans Pricing
  plan_count: 9
  slug: amazon-elasticache-plans-pricing
- name: Amazon Elasticache Price Estimates
  plan_count: 0
  slug: amazon-elasticache-price-estimates
random_paper: 9
rate_limits:
- limit_count: 5
  name: Amazon Elasticache Rate Limits
  slug: amazon-elasticache-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon ElastiCache — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-elasticache-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon ElastiCache API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: amazon-elasticache-spectral-rules
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 78.0
    catalog_earned_first_party: 12.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 93.4
    contract_governance: 27.3
    contract_quality: 69.3
    developer_ergonomics: 65.5
    discoverability: 73.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 92.9
      total: 14
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-elasticache/amazon-elasticache-2026-06-20T171652.png
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

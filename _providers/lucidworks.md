---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Lucidworks Agentic Access
  operation_count: 33
  slug: lucidworks-agentic-access
  summary_line: 33 operations · 20 acting
api_count: 7
apis:
- description: Fusion REST APIs administer collections, indexing pipelines, query pipelines, connectors, and search apps inside the Lucidworks Fusion platform. The legacy Custom Rules API for Fusion 5.7 is part of t
  name: Lucidworks Fusion REST API
  slug: fusion
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Split content into chunks
  name: Lucidworks Chunking API
  slug: lucidworks-chunking-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Predict ranked labels
  name: Lucidworks Classification API
  slug: lucidworks-classification-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Manage model deployments
  name: Lucidworks Deployments API
  slug: lucidworks-deployments-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Generate vector encodings
  name: Lucidworks Embeddings API
  slug: lucidworks-embeddings-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Manage models
  name: Lucidworks Models API
  slug: lucidworks-models-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Submit prediction requests by use case
  name: Lucidworks Predictions API
  slug: lucidworks-predictions-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Manage query rewrite rules
  name: Lucidworks QueryRewrites API
  slug: lucidworks-queryrewrites-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Fetch prediction results
  name: Lucidworks Results API
  slug: lucidworks-results-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Manage custom business rules
  name: Lucidworks Rules API
  slug: lucidworks-rules-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Capture and retrieve user behavior signals
  name: Lucidworks Signals API
  slug: lucidworks-signals-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Tokenize text by model
  name: Lucidworks Tokenization API
  slug: lucidworks-tokenization-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Apps API manages your Fusion apps. To export or import an app, see the Objects API. You can also import an app using the Fusion UI.
  name: Lucidworks Apps API
  slug: lucidworks-apps-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Blob Store REST API allows storing binary objects in Solr. You can use it to store entity extraction models, lookup lists or exclusion lists for use in index pipelines. This may include the entity
  name: Lucidworks Blobs API
  slug: lucidworks-blobs-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Collections API manages Fusion collections. It provides endpoints for creating, updating, and deleting collection, as well as endpoints for getting a collection's status and usage statistics. Fusi
  name: Lucidworks Collections API
  slug: lucidworks-collections-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Configurations API allows setting global properties for Fusion. Some settings are not set by any configuration file but are reported as settings from the operating system. Those settings cannot be
  name: Lucidworks Configurations API
  slug: lucidworks-configurations-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Check the status of the CRUD Events service.
  name: Lucidworks CRUD events API
  slug: lucidworks-crud-events-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: These APIs manage data models. Data models simplify the process of getting started with Fusion by providing pre-configured objects to reduce the effort spent on basic starting tasks. This helps keep d
  name: Lucidworks Data models API
  slug: lucidworks-data-models-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Features API lets you observe the status of features across collections. To manipulate features for a specific collection, use the Collections API.
  name: Lucidworks Features API
  slug: lucidworks-features-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: These endpoints show you how your Fusion objects are grouped. For example, you can use this API to see the signals-related jobs and collections that are part of a primary collection's group.
  name: Lucidworks Groups API
  slug: lucidworks-groups-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The History API provides information about the services that are running. The list of these services is provided by the Introspect API.
  name: Lucidworks History API
  slug: lucidworks-history-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Fusion Introspect endpoint lists basic information about endpoints and parameters for all Fusion endpoints.
  name: Lucidworks Introspect API
  slug: lucidworks-introspect-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Jobs API allows you to define schedules for objects that perform work. You can schedule datasources, tasks, and Spark jobs.
  name: Lucidworks Jobs API
  slug: lucidworks-jobs-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The License API provides license management features.
  name: Lucidworks License API
  slug: lucidworks-license-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Links API manages the links that represent the relationships between Fusion objects. You can see these links in the Object Explorer in the Fusion UI. You can also export and import links using the
  name: Lucidworks Links API
  slug: lucidworks-links-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Nodes API lets you check the status of each node in the search cluster.
  name: Lucidworks Nodes API
  slug: lucidworks-nodes-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Objects API lets you import and export objects between Fusion instances. Fusion objects include all your searchable data, plus pipelines, aggregations, and other configurations on which your colle
  name: Lucidworks Objects API
  slug: lucidworks-objects-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Check the status of the Registration service.
  name: Lucidworks Registration API
  slug: lucidworks-registration-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: 'Use the Scheduler API to define a schedule for system activities and manage the jobs that result from the schedule. All of the Fusion services are available for scheduling, as are any Solr activities '
  name: Lucidworks Scheduler API
  slug: lucidworks-scheduler-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Search Cluster API lets you connect Fusion with existing Solr instances in a Zookeeper-managed cluster.
  name: Lucidworks Search cluster API
  slug: lucidworks-search-cluster-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Search Logs API lets you manage a `searchLogs` collection.
  name: Lucidworks Search logs API
  slug: lucidworks-search-logs-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Solr Admin API lets you send commands to Solr through Fusion's proxy service. This allows you to protect your Solr instances from outside connections, and apply roles and user permissions from Fus
  name: Lucidworks Solr admin API
  slug: lucidworks-solr-admin-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: 'The Solr API is used to manage collection-level configurations. Since this API proxies requests to Solr, each available method corresponds to the method in Solr. So, a `GET` request to Solr would use '
  name: Lucidworks Solr API
  slug: lucidworks-solr-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The Solr Configuration REST API lets you access and manage Solr configuration files stored in ZooKeeper.
  name: Lucidworks Solr Configuration API
  slug: lucidworks-solr-configuration-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: These endpoints give you details about Fusion's REST API schemas.
  name: Lucidworks Swagger API
  slug: lucidworks-swagger-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The System REST API allows you to monitor the system performance.
  name: Lucidworks System API
  slug: lucidworks-system-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: These endpoints let you manage tasks, a flexible job type that can be used to clean up old logs or run any REST call.
  name: Lucidworks Tasks API
  slug: lucidworks-tasks-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Consult Lucidworks before using these endpoints.
  name: Lucidworks Update API
  slug: lucidworks-update-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: Deprecated.
  name: Lucidworks Webapps API
  slug: lucidworks-webapps-api
- baseURL: https://api.lucidworks.ai
  baseurl_source: declared
  description: The ZooKeeper Import/Export API provides methods to upload or download information from Fusion's ZooKeeper service. This service provides an alternative to the ZooKeeper clients `zkCli.sh` and `zk-she
  name: Lucidworks Zoo Keeper API
  slug: lucidworks-zookeeper-api
artifact_total: 84
collections:
- collection_type: open
  name: Lucidworks AI Platform API
  slug: open-lucidworks-ai-platform
- collection_type: open
  name: Lucidworks AI Platform Chunking API
  slug: open-lucidworks-chunking-api
- collection_type: open
  name: Lucidworks Content Chunking API
  slug: open-lucidworks-chunking
- collection_type: open
  name: Lucidworks AI Platform Chunking Classification API
  slug: open-lucidworks-classification-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Deployments API
  slug: open-lucidworks-deployments-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Embeddings API
  slug: open-lucidworks-embeddings-api
- collection_type: open
  name: Lucidworks Embeddings and Classification API
  slug: open-lucidworks-embeddings
- collection_type: open
  name: Lucidworks AI Platform Chunking Models API
  slug: open-lucidworks-models-api
- collection_type: open
  name: Lucidworks Model Management API
  slug: open-lucidworks-models
- collection_type: open
  name: Lucidworks AI Platform Chunking Predictions API
  slug: open-lucidworks-predictions-api
- collection_type: open
  name: Lucidworks AI Platform Chunking QueryRewrites API
  slug: open-lucidworks-queryrewrites-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Results API
  slug: open-lucidworks-results-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Rules API
  slug: open-lucidworks-rules-api
- collection_type: open
  name: Lucidworks Rules and Query Rewrites API
  slug: open-lucidworks-rules
- collection_type: open
  name: Lucidworks AI Platform Chunking Signals API
  slug: open-lucidworks-signals-api
- collection_type: open
  name: Lucidworks Signals API
  slug: open-lucidworks-signals
- collection_type: open
  name: Lucidworks AI Platform Chunking Tokenization API
  slug: open-lucidworks-tokenization-api
common:
- group: commercial
  href: https://artifacts.apis.io/lucidworks/plans/lucidworks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lucidworks-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lucidworks/rate-limits/lucidworks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lucidworks-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lucidworks/finops/lucidworks-finops.yml
  title: ''
  type: FinOps
  url: finops/lucidworks-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://lucidworks.com/blog/feed
- group: other
  href: https://artifacts.apis.io/lucidworks/capabilities/lucidworks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lucidworks-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/lucidworks/agentic-access/lucidworks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lucidworks-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lucidworks/security/lucidworks-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lucidworks-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lucidworks/security/lucidworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lucidworks-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lucidworks/authentication/lucidworks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lucidworks-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lucidworks
- group: company
  title: ''
  type: Website
  url: https://lucidworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.lucidworks.com
- group: docs
  title: ''
  type: APIReference
  url: https://doc.lucidworks.com/api-reference
- group: auth
  title: ''
  type: Authentication
  url: https://doc.lucidworks.com/api-reference/request-access-token/request-access-token
- group: build
  title: ''
  type: SDKs
  url: https://doc.lucidworks.com/docs/5/fusion/dev-portal/connectors-sdk/overview
- group: company
  title: ''
  type: Blog
  url: https://lucidworks.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://lucidworks.ai/llms.txt
created: '2025-01-07'
description: Lucidworks builds AI-powered search, discovery, and agent platforms used by enterprise commerce, support, and workplace teams. The Lucidworks AI Platform, Fusion, Neural Hybrid Search, Agent Studio, Commerce Studio, and Analytics Studio expose REST APIs for prediction, embedding, classification, signals capture, query rewriting, custom rule management, content chunking, and model deployment.
finops:
- has_sources: true
  method: generated
  name: Lucidworks Finops
  primary_unit: ''
  service_category: Enterprise Search
  slug: lucidworks-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidworks.png
json_schemas:
- name: ChunkAck
  property_count: 2
  slug: lucidworks-chunkack
- name: ChunkRequest
  property_count: 4
  slug: lucidworks-chunkrequest
- name: ChunkResult
  property_count: 3
  slug: lucidworks-chunkresult
- name: ClassifyRequest
  property_count: 2
  slug: lucidworks-classifyrequest
- name: ClassifyResponse
  property_count: 1
  slug: lucidworks-classifyresponse
- name: Deployment
  property_count: 4
  slug: lucidworks-deployment
- name: Embedding
  property_count: 2
  slug: lucidworks-embedding
- name: EncodeRequest
  property_count: 1
  slug: lucidworks-encoderequest
- name: Model
  property_count: 5
  slug: lucidworks-model
- name: PredictionAck
  property_count: 2
  slug: lucidworks-predictionack
- name: PredictionRequest
  property_count: 2
  slug: lucidworks-predictionrequest
- name: PredictionResult
  property_count: 3
  slug: lucidworks-predictionresult
- name: QueryRewrite
  property_count: 5
  slug: lucidworks-queryrewrite
- name: Rule
  property_count: 6
  slug: lucidworks-rule
- name: Signal
  property_count: 5
  slug: lucidworks-signal
- name: SignalList
  property_count: 2
  slug: lucidworks-signallist
- name: TokenRequest
  property_count: 3
  slug: lucidworks-tokenrequest
- name: TokenResponse
  property_count: 3
  slug: lucidworks-tokenresponse
json_structures:
- name: Lucidworks Structure
  property_count: 0
  slug: lucidworks-structure
layout: provider
modified: '2026-10-06'
name: Lucidworks
nav: Providers
network: true
overview: 'Lucidworks publishes 40 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chunking API, Classification API, Deployments API, and 37 more. Tagged areas include Search, Artificial Intelligence, Enterprise Search, Vector Search, and RAG.


  The Lucidworks catalog on APIs.io includes 1 Spectral governance ruleset.


  Lucidworks'' developer surface includes authentication, documentation, API reference, engineering blog, and 14 more developer resources.'
plans:
- name: Lucidworks Plans Pricing
  plan_count: 1
  slug: lucidworks-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Lucidworks Rate Limits
  slug: lucidworks-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Lucidworks — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lucidworks-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 42.3
    catalog_earned_first_party: 0.0
    catalog_gap: 72.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 53.5
    developer_ergonomics: 38.1
    discoverability: 69.6
    operational_transparency: 7.9
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 71.8
      total: 39
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/lucidworks/lucidworks-2026-06-20T184745.png
security:
- kind: authentication
  name: Lucidworks Authentication
  slug: lucidworks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lucidworks Domain Security
  slug: lucidworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lucidworks Trust Center
  slug: lucidworks-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: lucidworks
tags:
- Search
- Artificial Intelligence
- Enterprise Search
- Vector Search
- RAG
- Commerce
website: https://lucidworks.com
---

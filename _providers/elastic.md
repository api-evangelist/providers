---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 428
  human_in_the_loop: 16
  name: Elastic Agentic Access
  operation_count: 834
  slug: elastic-agentic-access
  summary_line: 834 operations · 428 acting · 16 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Account-level information.
  name: Elastic Account API
  slug: elastic-account-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Cluster health, state, and statistics.
  name: Elastic Cluster API
  slug: elastic-cluster-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Manage Elasticsearch and Kibana deployments.
  name: Elastic Deployments API
  slug: elastic-deployments-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Index, update, retrieve, and delete documents.
  name: Elastic Documents API
  slug: elastic-documents-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Manage indices, mappings, and settings.
  name: Elastic Indices API
  slug: elastic-indices-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Search and query operations across indices.
  name: Elastic Search API
  slug: elastic-search-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Roles, users, API keys, and access control.
  name: Elastic Security API
  slug: elastic-security-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Manage Kibana Spaces.
  name: Elastic Spaces API
  slug: elastic-spaces-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Kibana server status.
  name: Elastic Status API
  slug: elastic-status-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: IP and VPC traffic filter rulesets for deployments.
  name: Elastic TrafficFilters API
  slug: elastic-trafficfilters-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: 'The behavioral analytics APIs let you create and manage analytics collections and view their data. Use them to analyze users'' search and click behavior, improve result relevance, and identify content '
  name: Elastic Analytics API
  slug: elastic-analytics-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The compact and aligned text (CAT) APIs aim are intended only for human consumption using the Kibana console or command line. They are not intended for use by applications. For application consumption
  name: Elastic Cat API
  slug: elastic-cat-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The cross-cluster replication (CCR) APIs let you run replication operations, such as creating and managing follower indices or auto-follow patterns. Use CCR to replicate indices across clusters to mai
  name: Elastic Ccr API
  slug: elastic-ccr-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The connector and sync jobs APIs provide a convenient way to create and manage Elastic connectors and sync jobs in an internal index. Connectors are Elasticsearch integrations for syncing content from
  name: Elastic Connector API
  slug: elastic-connector-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The data stream APIs enable you to create and manage data streams and data stream lifecycles. A data stream lets you store append-only time series data across multiple indices while giving you a singl
  name: Elastic data stream API
  slug: elastic-data-stream-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The document APIs enable you to create and manage documents in an Elasticsearch index.
  name: Elastic Document API
  slug: elastic-document-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The enrich APIs enable you to manage enrich policies. An enrich policy is a set of configuration options used to add the right enrich data to the right incoming documents.
  name: Elastic Enrich API
  slug: elastic-enrich-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Event Query Language (EQL) is a query language for event-based time series data, such as logs, metrics, and traces.
  name: Elastic Eql API
  slug: elastic-eql-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The Elasticsearch Query Language (ES|QL) provides a powerful way to filter, transform, and analyze data stored in Elasticsearch, and in the future in other runtimes.
  name: Elastic Esql API
  slug: elastic-esql-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The features APIs retrieve information about the features that are currently enabled and available on the node.
  name: Elastic Features API
  slug: elastic-features-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The Fleet APIs support Fleet's use of Elasticsearch as a data store for internal agent and action data.
  name: Elastic Fleet API
  slug: elastic-fleet-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The graph explore API enables you to extract and summarize information about the documents and terms in an Elasticsearch index.
  name: Elastic Graph API
  slug: elastic-graph-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The cluster - health API provides you a report with the health status of an Elasticsearch cluster.
  name: Elastic Health Report API
  slug: elastic-health-report-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: You can use the index lifecycle management (ILM) APIs to create and manage policies to automatically manage the lifecycle of your Elasticsearch indices.
  name: Elastic Ilm API
  slug: elastic-ilm-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Azure, Google AI Studio or Hugging Face. For bui
  name: Elastic Inference API
  slug: elastic-inference-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Get basic information about the cluster.
  name: Elastic Info API
  slug: elastic-info-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Ingest APIs enable you to manage tasks and resources related to ingest pipelines and processors.
  name: Elastic Ingest API
  slug: elastic-ingest-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Licensing APIs enable you to manage your licenses.
  name: Elastic License API
  slug: elastic-license-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Logstash APIs enable you to manage pipelines that are used by Logstash Central Management.
  name: Elastic Logstash API
  slug: elastic-logstash-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The migration APIs power Kibana's Upgrade Assistant feature.
  name: Elastic Migration API
  slug: elastic-migration-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The machine learning anomaly detection APIs enable you to perform anomaly detection activities.
  name: Elastic ml anomaly API
  slug: elastic-ml-anomaly-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Perform machine learning activities, such as anomaly detection, data frame analytics, and natural language processing tasks.
  name: Elastic Ml API
  slug: elastic-ml-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The machine learning data frame analytics APIs enable you to perform data frame analytics activities.
  name: Elastic ml data frame API
  slug: elastic-ml-data-frame-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The machine learning trained models APIs enable you to perform model management operations.
  name: Elastic ml trained model API
  slug: elastic-ml-trained-model-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Query rules enable you to configure per-query rules that are applied at query time to queries that match the specific rule. Query rules are organized into rulesets, collections of query rules that are
  name: Elastic Query Rules API
  slug: elastic-query-rules-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The rollup APIs enable you to create, manage, and retrieve information about rollup jobs.
  name: Elastic Rollup API
  slug: elastic-rollup-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Use the script support APIs to get a list of supported script contexts and languages. Use the stored script APIs to manage stored scripts and search templates.
  name: Elastic Script API
  slug: elastic-script-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The search application APIs provide a convenient way to leverage the power of Elasticsearch for your search applications.
  name: Elastic Search Application API
  slug: elastic-search-application-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The searchable snapshots APIs are used to mount snapshots as searchable indices.
  name: Elastic Searchable Snapshots API
  slug: elastic-searchable-snapshots-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Snapshot lifecycle management (SLM) enables you to automatically take snapshots and control how long they are kept.
  name: Elastic Slm API
  slug: elastic-slm-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The snapshot and restore APIs are used to take snapshots of running clusters. Snapshots are backups of individual indices or entire clusters.
  name: Elastic Snapshot API
  slug: elastic-snapshot-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Elasticsearch's SQL APIs enable you to run SQL queries on Elasticsearch indices and data streams.
  name: Elastic Sql API
  slug: elastic-sql-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The synonyms management API provides a convenient way to define and manage synonyms in an internal system index. Related synonyms can be grouped in a "synonyms set". Create as many synonym sets as you
  name: Elastic Synonyms API
  slug: elastic-synonyms-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The task management APIs enable you to get information about the tasks currently running on one or more nodes in the cluster.
  name: Elastic Tasks API
  slug: elastic-tasks-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The text structure APIs enable you to find the structure of a text field in an Elasticsearch index.
  name: Elastic Text Structure API
  slug: elastic-text-structure-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The transform APIs enable you to create and manage transforms.
  name: Elastic Transform API
  slug: elastic-transform-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: You can use Watcher to watch for changes or anomalies in your data and perform the necessary actions in response.
  name: Elastic Watcher API
  slug: elastic-watcher-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: The usage API provides usage information about the installed X-Pack features.
  name: Elastic Xpack API
  slug: elastic-xpack-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Manage data views (formerly index patterns).
  name: Elastic data views API
  slug: elastic-data-views-api
- baseURL: https://api.elastic-cloud.com
  baseurl_source: declared
  description: Manage Kibana saved objects (dashboards, visualizations, searches).
  name: Elastic saved objects API
  slug: elastic-saved-objects-api
artifact_total: 108
asyncapis:
- description: ''
  name: Elastic Webhooks
  slug: elastic-webhooks
collections:
- collection_type: open
  name: Elastic Cloud Account API
  slug: open-elastic-account-api
- collection_type: open
  name: Elastic Cloud API
  slug: open-elastic-cloud
- collection_type: open
  name: Elastic Cloud Account Cluster API
  slug: open-elastic-cluster-api
- collection_type: open
  name: Elastic Cloud Account DataViews API
  slug: open-elastic-dataviews-api
- collection_type: open
  name: Elastic Cloud Account Deployments API
  slug: open-elastic-deployments-api
- collection_type: open
  name: Elastic Cloud Account Documents API
  slug: open-elastic-documents-api
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elastic-elasticsearch
- collection_type: open
  name: Elastic Cloud Account Indices API
  slug: open-elastic-indices-api
- collection_type: open
  name: Kibana API
  slug: open-elastic-kibana
- collection_type: open
  name: Elastic Cloud Account SavedObjects API
  slug: open-elastic-savedobjects-api
- collection_type: open
  name: Elastic Cloud Account Search API
  slug: open-elastic-search-api
- collection_type: open
  name: Elastic Cloud Account Security API
  slug: open-elastic-security-api
- collection_type: open
  name: Elastic Cloud Account Spaces API
  slug: open-elastic-spaces-api
- collection_type: open
  name: Elastic Cloud Account Status API
  slug: open-elastic-status-api
- collection_type: open
  name: Elastic Cloud Account TrafficFilters API
  slug: open-elastic-trafficfilters-api
common:
- group: commercial
  href: https://artifacts.apis.io/elastic/finops/elastic-finops.yml
  title: ''
  type: FinOps
  url: finops/elastic-finops.yml
- group: operate
  href: https://artifacts.apis.io/elastic/rate-limits/elastic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elastic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/elastic/plans/elastic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elastic-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/elastic/rules/elastic-rules.yml
  title: ''
  type: Spectral
  url: rules/elastic-rules.yml
- group: design
  href: https://artifacts.apis.io/elastic/rules/elastic-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/elastic-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/elastic/json-ld/elastic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/elastic-context.jsonld
- group: design
  href: https://artifacts.apis.io/elastic/vocabulary/elastic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/elastic-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/elastic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/elastic/asyncapi/elastic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/elastic-webhooks.yml
- group: design
  href: https://artifacts.apis.io/elastic/data-model/elastic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elastic-data-model.yml
- group: operate
  href: https://artifacts.apis.io/elastic/changelog/elastic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elastic-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.elastic.co/trust
- group: design
  href: https://artifacts.apis.io/elastic/errors/elastic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elastic-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elastic/conformance/elastic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elastic-conformance.yml
- group: agent
  href: https://artifacts.apis.io/elastic/llms/elastic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elastic-llms.txt
- group: auth
  href: https://artifacts.apis.io/elastic/well-known/elastic-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elastic-status-security.txt
- group: auth
  href: https://artifacts.apis.io/elastic/well-known/elastic-cloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elastic-cloud-security.txt
- group: auth
  href: https://artifacts.apis.io/elastic/well-known/elastic-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elastic-api-security.txt
- group: agent
  href: https://artifacts.apis.io/elastic/well-known/elastic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elastic-well-known.yml
- group: other
  href: https://artifacts.apis.io/elastic/hosts/elastic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elastic-hosts.yml
- group: other
  href: https://artifacts.apis.io/elastic/vendors/elastic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elastic-vendors.yml
- group: build
  href: https://artifacts.apis.io/elastic/packages/elastic-packages.yml
  title: ''
  type: SDKs
  url: packages/elastic-packages.yml
- group: build
  href: https://artifacts.apis.io/elastic/packages/elastic-packages.yml
  title: ''
  type: Packages
  url: packages/elastic-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/legal/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elastic.co/
- group: start
  title: ''
  type: SignUp
  url: https://partners.elastic.co/English/register_email.aspx
- group: auth
  title: ''
  type: Security
  url: https://www.elastic.co/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.elastic.co/cloud/serverless/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elastic.co/legal/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://www.elastic.co/about/press
- group: other
  title: ''
  type: Leadership
  url: https://www.elastic.co/about/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.elastic.co/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elastic.co/docs/troubleshoot/elasticsearch/security/trb-security-setup
- group: agent
  href: https://artifacts.apis.io/elastic/agentic-access/elastic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/elastic/security/elastic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elastic-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/elastic/security/elastic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elastic-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/elastic/authentication/elastic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elastic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elastic-co
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/index.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/elastic
- group: start
  title: ''
  type: Console
  url: https://cloud.elastic.co
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing
- group: commercial
  title: ''
  type: License
  url: https://www.elastic.co/licensing/elastic-license
- group: agent
  title: ''
  type: LlmsText
  url: https://api.elastic-cloud.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/feed
- group: other
  href: https://artifacts.apis.io/elastic/capabilities/elastic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/elastic-capability-edges.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/elastic/apm-server/blob/c1dc5a1569eb2da398194bf64012c66387ddcae3/docs/spec/openapi/.spectral.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/elastic/docs-actions/blob/6424787358d5b21453778294bfc93f97e3a0ae2f/openapi/lint/ruleset.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/elastic/elasticsearch-specification/blob/108d535461e94dc3b74d8a246149359406fbb5b4/docs/linters/.spectral.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/elastic/kibana/blob/f38242ac0f935f780b9c2a937d0a088aebd7c71b/oas_docs/linters/.spectral.yaml
created: '2025-01-08'
description: Elastic is a software company that builds search-powered solutions for observability, security, and search use cases. The Elastic Stack (Elasticsearch, Kibana, and related tools) lets organizations ingest, search, analyze, and visualize structured and unstructured data in real time. Elastic Cloud delivers managed Elasticsearch and Kibana deployments with REST APIs for both data operations and deployment management.
features:
- 'Elastic Cloud Hosted: resource-based with Standard/Gold/Platinum/Enterprise tiers'
- 'Elastic Serverless: VCU + storage usage-based for Search/Observability/Security'
- 'Self-managed: license-based for on-prem deployment'
- 'Multi-cloud: AWS, GCP, Azure'
- REST API for Elasticsearch, Kibana, APM
- Bulk indexing API for high-throughput ingest
- Throughput scales with cluster hardware
- OAuth + API keys + JWT realm
- Watcher for alerting on rules
- ES|QL query language
- Vector search with kNN
- ELSER (Elastic Learned Sparse Encoder) for semantic search
- Cross-cluster search/replication
- Hot/Warm/Cold/Frozen data tiers
- Index Lifecycle Management (ILM)
- 'Compliance: SOC 2, HIPAA, FedRAMP (Enterprise)'
finops:
- has_sources: true
  method: derived
  name: Elastic Finops
  primary_unit: ''
  service_category: ''
  slug: elastic-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic.png
json_schemas:
- name: Deployment
  property_count: 4
  slug: elastic-deployment
- name: Document
  property_count: 4
  slug: elastic-document
- name: SavedObject
  property_count: 4
  slug: elastic-saved-object
- name: SavedObject
  property_count: 4
  slug: elastic-savedobject
- name: SearchResponse
  property_count: 3
  slug: elastic-searchresponse
- name: Space
  property_count: 4
  slug: elastic-space
json_structures:
- name: Elastic Structure
  property_count: 0
  slug: elastic-structure
jsonld:
- class_count: 120
  name: Elastic Context
  property_count: 383
  slug: elastic-context
layout: provider
modified: '2026-05-19'
name: Elastic
nav: Providers
network: true
overview: 'Elastic publishes 50 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Cluster API, Deployments API, and 47 more. Tagged areas include Search, Analytics, Observability, Security, and Visualization.


  The Elastic catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 6 Spectral governance rulesets.


  Elastic''s developer surface includes changelog, signup flow, getting-started guide, authentication, documentation, GitHub presence, developer console, and 44 more developer resources.'
plans:
- name: Elastic Plans Pricing
  plan_count: 0
  slug: elastic-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Elastic Rate Limits
  slug: elastic-rate-limits
rules:
- authorship: provider
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Elastic — apm server rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: elastic-apm-server-spectral-rules
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Elastic — docs actions rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: elastic-docs-actions-spectral-rules
- authorship: provider
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Elastic — elasticsearch specification rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: elastic-elasticsearch-specification-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Elastic — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: elastic-jsonschema-spectral-rules
- authorship: provider
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Elastic — kibana rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: elastic-kibana-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Elastic API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: elastic-rules
score:
  band: exemplar
  composite: 70.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 81.9
    catalog_earned_first_party: 18.0
    catalog_gap: 33.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 50.0
    contract_governance: 72.7
    contract_quality: 65.3
    developer_ergonomics: 45.8
    discoverability: 80.4
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 76.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 7.3
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/elastic/elastic-2026-06-20T180547.png
security:
- kind: authentication
  name: Elastic Authentication
  slug: elastic-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elastic Domain Security
  slug: elastic-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Elastic Trust Center
  slug: elastic-trust-center
  summary_line: GDPR
skill_count: 5
skills:
- name: elastic-create-get-delete-data-stream
  slug: elastic-create-get-delete-data-stream
- name: elastic-index-document
  slug: elastic-index-document
- name: elastic-indices-create-and-alias
  slug: elastic-indices-create-and-alias
- name: elastic-ingest-create-and-simulate-pipeline
  slug: elastic-ingest-create-and-simulate-pipeline
- name: elastic-search-async-flow
  slug: elastic-search-async-flow
slug: elastic
tags:
- Search
- Analytics
- Observability
- Security
- Visualization
- Cloud
- Monitoring
website: https://www.elastic.co
---

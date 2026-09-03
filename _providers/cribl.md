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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 67
  human_in_the_loop: 0
  name: Cribl Agentic Access
  operation_count: 133
  slug: cribl-agentic-access
  summary_line: 133 operations · 67 acting
api_count: 6
apis:
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage API credentials used for OAuth 2.0 client credentials authentication. Credentials consist of a client ID and client secret used to obtain bearer tokens for API access.
  name: Cribl API Credentials API
  slug: cribl-api-credentials-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Obtain and manage authentication tokens for API access.
  name: Cribl Authentication API
  slug: cribl-authentication-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage scheduled and on-demand data collection jobs from REST APIs, databases, scripts, and other sources.
  name: Cribl Collectors API
  slug: cribl-collectors-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Configure and manage database connections used by collectors and lookup functions.
  name: Cribl Database Connections API
  slug: cribl-database-connections-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage Cribl Lake datasets that define storage buckets for observability and security data in open formats.
  name: Cribl Datasets API
  slug: cribl-datasets-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage data output destinations where processed events are sent, including Splunk, S3, Elasticsearch, and webhook endpoints.
  name: Cribl Destinations API
  slug: cribl-destinations-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage data output destinations for edge nodes including forwarding to Stream workers, cloud storage, and analytics platforms.
  name: Cribl Edge Destinations API
  slug: cribl-edge-destinations-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage edge fleets that organize groups of edge nodes deployed on endpoints for local data collection and processing.
  name: Cribl Edge Fleets API
  slug: cribl-edge-fleets-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Monitor and manage individual edge nodes deployed on endpoints including their status, version, and resource utilization.
  name: Cribl Edge Nodes API
  slug: cribl-edge-nodes-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage processing pipelines running on edge nodes for local data transformation and filtering before forwarding.
  name: Cribl Edge Pipelines API
  slug: cribl-edge-pipelines-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage routes on edge nodes for directing collected data to appropriate pipelines and destinations.
  name: Cribl Edge Routes API
  slug: cribl-edge-routes-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage data input sources on edge nodes including file monitors, Windows Event Log, system metrics, AppScope, and other local collection methods.
  name: Cribl Edge Sources API
  slug: cribl-edge-sources-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Retrieve available processing functions that can be used within pipelines for data transformation.
  name: Cribl Functions API
  slug: cribl-functions-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage Worker Groups and Edge Fleets, which organize and deploy configurations to sets of worker nodes or edge agents.
  name: Cribl Groups API
  slug: cribl-groups-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Check the health and availability of the Cribl Cloud management plane services.
  name: Cribl Health API
  slug: cribl-health-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Monitor and manage running and completed collection and processing jobs.
  name: Cribl Jobs API
  slug: cribl-jobs-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage Cribl Lake datasets for storing and organizing observability data in open formats.
  name: Cribl Lake Datasets API
  slug: cribl-lake-datasets-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage lookup files and tables used for data enrichment in pipelines.
  name: Cribl Lookups API
  slug: cribl-lookups-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Monitor and manage individual worker nodes and edge nodes within groups and fleets.
  name: Cribl Nodes API
  slug: cribl-nodes-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Configure notification rules and targets for alerting on data flow anomalies and system events.
  name: Cribl Notifications API
  slug: cribl-notifications-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Install, manage, and distribute reusable configuration packs containing pipelines, routes, and other resources.
  name: Cribl Packs API
  slug: cribl-packs-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage processing pipelines that contain ordered sequences of functions for transforming, filtering, and enriching events.
  name: Cribl Pipelines API
  slug: cribl-pipelines-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Configure data retention policies that control how long data is stored in Lake datasets before automatic cleanup.
  name: Cribl Retention API
  slug: cribl-retention-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage routes that filter and direct incoming data across pipelines and destinations using filter expressions.
  name: Cribl Routes API
  slug: cribl-routes-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Create and manage saved search queries for reuse and sharing across teams and workflows.
  name: Cribl Saved Searches API
  slug: cribl-saved-searches-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Execute and manage search queries across live and stored observability data with support for federated search across multiple data sources.
  name: Cribl Search Jobs API
  slug: cribl-search-jobs-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Configure notification rules that trigger alerts based on search results using webhook and other notification targets.
  name: Cribl Search Notifications API
  slug: cribl-search-notifications-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage data input sources that collect events from various systems including Syslog, HTTP, Kafka, Splunk, and other protocols.
  name: Cribl Sources API
  slug: cribl-sources-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Access system-level settings including Git configuration, licensing, and global preferences.
  name: Cribl System API
  slug: cribl-system-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage configuration versions, commits, and deployment history.
  name: Cribl Versioning API
  slug: cribl-versioning-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage Stream worker groups that organize worker nodes and deploy shared pipeline configurations across clusters.
  name: Cribl Worker Groups API
  slug: cribl-worker-groups-api
- baseURL: https://api.cribl.cloud
  baseurl_source: declared
  description: Manage Cribl Cloud workspaces which are unique VPC containers each isolating an instance of the Cribl Product Suite including Stream, Edge, Search, and Lake.
  name: Cribl Workspaces API
  slug: cribl-workspaces-api
artifact_total: 126
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cribl As Code API Credentials API
  slug: open-cribl-api-credentials-api
- collection_type: open
  name: Cribl As Code API
  slug: open-cribl-as-code-api
- collection_type: open
  name: Cribl As Code API Credentials Authentication API
  slug: open-cribl-authentication-api
- collection_type: open
  name: Cribl Cloud API
  slug: open-cribl-cloud-api
- collection_type: open
  name: Cribl As Code API Credentials Collectors API
  slug: open-cribl-collectors-api
- collection_type: open
  name: Cribl As Code API Credentials Database Connections API
  slug: open-cribl-database-connections-api
- collection_type: open
  name: Cribl As Code API Credentials Datasets API
  slug: open-cribl-datasets-api
- collection_type: open
  name: Cribl As Code API Credentials Destinations API
  slug: open-cribl-destinations-api
- collection_type: open
  name: Cribl Edge API
  slug: open-cribl-edge-api
- collection_type: open
  name: Cribl As Code API Credentials Edge Destinations API
  slug: open-cribl-edge-destinations-api
- collection_type: open
  name: Cribl As Code API Credentials Edge Fleets API
  slug: open-cribl-edge-fleets-api
- collection_type: open
  name: Cribl As Code API Credentials Edge Nodes API
  slug: open-cribl-edge-nodes-api
- collection_type: open
  name: Cribl As Code API Credentials Edge Pipelines API
  slug: open-cribl-edge-pipelines-api
- collection_type: open
  name: Cribl As Code API Credentials Edge Routes API
  slug: open-cribl-edge-routes-api
- collection_type: open
  name: Cribl As Code API Credentials Edge Sources API
  slug: open-cribl-edge-sources-api
- collection_type: open
  name: Cribl As Code API Credentials Functions API
  slug: open-cribl-functions-api
- collection_type: open
  name: Cribl As Code API Credentials Groups API
  slug: open-cribl-groups-api
- collection_type: open
  name: Cribl As Code API Credentials Health API
  slug: open-cribl-health-api
- collection_type: open
  name: Cribl As Code API Credentials Jobs API
  slug: open-cribl-jobs-api
- collection_type: open
  name: Cribl Lake API
  slug: open-cribl-lake-api
- collection_type: open
  name: Cribl As Code API Credentials Lake Datasets API
  slug: open-cribl-lake-datasets-api
- collection_type: open
  name: Cribl As Code API Credentials Lookups API
  slug: open-cribl-lookups-api
- collection_type: open
  name: Cribl As Code API Credentials Nodes API
  slug: open-cribl-nodes-api
- collection_type: open
  name: Cribl As Code API Credentials Notifications API
  slug: open-cribl-notifications-api
- collection_type: open
  name: Cribl As Code API Credentials Packs API
  slug: open-cribl-packs-api
- collection_type: open
  name: Cribl As Code API Credentials Pipelines API
  slug: open-cribl-pipelines-api
- collection_type: open
  name: Cribl As Code API Credentials Retention API
  slug: open-cribl-retention-api
- collection_type: open
  name: Cribl As Code API Credentials Routes API
  slug: open-cribl-routes-api
- collection_type: open
  name: Cribl As Code API Credentials Saved Searches API
  slug: open-cribl-saved-searches-api
- collection_type: open
  name: Cribl Search API
  slug: open-cribl-search-api
- collection_type: open
  name: Cribl As Code API Credentials Search Jobs API
  slug: open-cribl-search-jobs-api
- collection_type: open
  name: Cribl As Code API Credentials Search Notifications API
  slug: open-cribl-search-notifications-api
- collection_type: open
  name: Cribl As Code API Credentials Sources API
  slug: open-cribl-sources-api
- collection_type: open
  name: Cribl Stream API
  slug: open-cribl-stream-api
- collection_type: open
  name: Cribl As Code API Credentials System API
  slug: open-cribl-system-api
- collection_type: open
  name: Cribl As Code API Credentials Versioning API
  slug: open-cribl-versioning-api
- collection_type: open
  name: Cribl As Code API Credentials Worker Groups API
  slug: open-cribl-worker-groups-api
- collection_type: open
  name: Cribl As Code API Credentials Workspaces API
  slug: open-cribl-workspaces-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cribl-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cribl-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cribl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cribl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cribl-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cribl-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/criblio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cribl
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cribl-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cribl-pipeline-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cribl-route-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cribl-source-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cribl-destination-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cribl-worker-group-schema.json
- group: company
  title: ''
  type: Website
  url: https://cribl.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cribl.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.cribl.io/
- group: start
  title: ''
  type: Login
  url: https://login.cribl.cloud/
- group: company
  title: ''
  type: Blog
  url: https://cribl.io/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cribl.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cribl.io/terms-of-service/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cribl.io/llms.txt
created: '2025-03-05'
description: Cribl is an observability pipeline company providing a suite of products for collecting, processing, routing, searching, and storing telemetry data at scale. Cribl's developer platform offers REST APIs across Stream, Edge, Search, Lake, and the As Code product line, exposing programmatic control over data pipelines, edge agents, federated search jobs, lake datasets, and infrastructure-as-code configuration management. The Cribl Cloud API acts as a centrally managed control plane across all deployments and authenticates with OAuth 2.0 client credentials.
finops:
- name: Cribl Finops
  service_category: Observability Pipeline
  slug: cribl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cribl.png
json_schemas:
- name: ApiCredential
  property_count: 6
  slug: cribl-apicredential
- name: ApiCredentialCreate
  property_count: 1
  slug: cribl-apicredentialcreate
- name: ApiCredentialUpdate
  property_count: 1
  slug: cribl-apicredentialupdate
- name: ApiCredentialWithSecret
  property_count: 6
  slug: cribl-apicredentialwithsecret
- name: Collector
  property_count: 5
  slug: cribl-collector
- name: DatabaseConnection
  property_count: 4
  slug: cribl-databaseconnection
- name: Cribl Destination
  property_count: 12
  slug: cribl-destination
- name: DestinationStatus
  property_count: 4
  slug: cribl-destinationstatus
- name: EdgeDestination
  property_count: 6
  slug: cribl-edgedestination
- name: EdgeFleet
  property_count: 7
  slug: cribl-edgefleet
- name: EdgeNode
  property_count: 9
  slug: cribl-edgenode
- name: EdgePipeline
  property_count: 2
  slug: cribl-edgepipeline
- name: EdgeRoute
  property_count: 8
  slug: cribl-edgeroute
- name: EdgeSource
  property_count: 6
  slug: cribl-edgesource
- name: Function
  property_count: 4
  slug: cribl-function
- name: GitSettings
  property_count: 5
  slug: cribl-gitsettings
- name: Group
  property_count: 7
  slug: cribl-group
- name: HealthStatus
  property_count: 3
  slug: cribl-healthstatus
- name: Job
  property_count: 6
  slug: cribl-job
- name: LakeDataset
  property_count: 5
  slug: cribl-lakedataset
- name: Lookup
  property_count: 4
  slug: cribl-lookup
- name: Node
  property_count: 8
  slug: cribl-node
- name: Notification
  property_count: 4
  slug: cribl-notification
- name: Pack
  property_count: 6
  slug: cribl-pack
- name: Cribl Pipeline
  property_count: 2
  slug: cribl-pipeline
- name: PipelineFunction
  property_count: 5
  slug: cribl-pipelinefunction
- name: RetentionPolicy
  property_count: 3
  slug: cribl-retentionpolicy
- name: Cribl Route
  property_count: 10
  slug: cribl-route
- name: SavedSearch
  property_count: 8
  slug: cribl-savedsearch
- name: SearchDataset
  property_count: 5
  slug: cribl-searchdataset
- name: SearchJob
  property_count: 9
  slug: cribl-searchjob
- name: SearchJobRequest
  property_count: 5
  slug: cribl-searchjobrequest
- name: Cribl Source
  property_count: 14
  slug: cribl-source
- name: Cribl Worker Group
  property_count: 9
  slug: cribl-worker-group
- name: WorkerGroup
  property_count: 6
  slug: cribl-workergroup
- name: Workspace
  property_count: 9
  slug: cribl-workspace
- name: WorkspaceCreate
  property_count: 3
  slug: cribl-workspacecreate
- name: WorkspaceUpdate
  property_count: 2
  slug: cribl-workspaceupdate
json_structures:
- name: Cribl Structure
  property_count: 0
  slug: cribl-structure
jsonld:
- class_count: 0
  name: Cribl Context
  property_count: 11
  slug: cribl-context
layout: provider
modified: '2026-05-19'
name: Cribl
nav: Providers
network: true
overview: 'Cribl publishes 32 APIs on the [APIs.io](https://apis.io/) network, including API Credentials API, Authentication API, Collectors API, and 29 more. Tagged areas include Configuration, Data Lake, Data Pipeline, Data Routing, and Edge Computing.


  The Cribl catalog on APIs.io includes 1 JSON-LD context and 7 Spectral governance rulesets.


  Cribl''s developer surface includes authentication, documentation, developer portal, engineering blog, and 18 more developer resources.'
plans:
- name: Cribl Plans Pricing
  plan_count: 3
  slug: cribl-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Cribl Rate Limits
  slug: cribl-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Cribl API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 1
  slug: cribl-as-code-api-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Cribl API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 1
  slug: cribl-cloud-api-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Cribl API Rules
  rule_count: 5
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 0
  slug: cribl-edge-api-rules
- effective_rule_count: 6
  extends: []
  name: Cribl API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cribl-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Cribl API Rules
  rule_count: 5
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 0
  slug: cribl-lake-api-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Cribl API Rules
  rule_count: 5
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 0
  slug: cribl-search-api-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Cribl API Rules
  rule_count: 5
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 0
  slug: cribl-stream-api-rules
scopes:
- name: Cribl Scopes
  scope_count: 6
  slug: cribl-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 54.5
    contract_quality: 64.2
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 54.5
    operational_transparency: 10.5
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cribl/refs/heads/main/screenshots/cribl-2026-06-20T175228.png
security:
- kind: authentication
  name: Cribl Authentication
  slug: cribl-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cribl Domain Security
  slug: cribl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cribl Vulnerability Disclosure
  slug: cribl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cribl
tags:
- Configuration
- Data Lake
- Data Pipeline
- Data Routing
- Edge Computing
- Infrastructure as Code
- Observability
- Search
- Security Data
- Stream Processing
- Telemetry
website: https://cribl.io/
---

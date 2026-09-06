---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Appdynamics Agentic Access
  operation_count: 65
  slug: appdynamics-agentic-access
  summary_line: 65 operations · 33 acting
api_count: 9
apis:
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Manage automated response actions triggered by policies including email notifications, HTTP requests, and custom scripts.
  name: AppDynamics Actions API
  slug: appdynamics-actions-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Export and import action configurations for alerting workflows.
  name: AppDynamics Actions Export/Import API
  slug: appdynamics-actions-export-import-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve business application names, IDs, and related metadata from the Controller.
  name: AppDynamics Applications API
  slug: appdynamics-applications-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve registered backend components detected by the Controller including their properties and exit point types.
  name: AppDynamics Backends API
  slug: appdynamics-backends-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve business transaction information including names, IDs, entry points, and detection status.
  name: AppDynamics Business Transactions API
  slug: appdynamics-business-transactions-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Configure data collection settings for cloud connections including service selection, region filtering, and resource group scoping.
  name: AppDynamics Configurations API
  slug: appdynamics-configurations-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Manage cloud provider connections for AWS, Azure, and GCP to enable automated cloud monitoring at scale.
  name: AppDynamics Connections API
  slug: appdynamics-connections-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Export and import custom dashboard configurations.
  name: AppDynamics Custom Dashboards Export/Import API
  slug: appdynamics-custom-dashboards-export-import-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Upload custom metrics to the AppDynamics Controller through the Machine Agent HTTP listener. Metrics must be uploaded at least once every 300 seconds to remain active.
  name: AppDynamics Custom Metrics API
  slug: appdynamics-custom-metrics-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Manage database collectors that monitor performance and availability of database instances including creation, retrieval, update, and deletion.
  name: AppDynamics Database Collectors API
  slug: appdynamics-database-collectors-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Publish custom analytics events to the Events Service for storage and analysis.
  name: AppDynamics Events API
  slug: appdynamics-events-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Manage health rules that define performance thresholds and violation conditions for monitored applications.
  name: AppDynamics Health Rules API
  slug: appdynamics-health-rules-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Export and import health rule configurations for backup, migration, and provisioning across Controller instances.
  name: AppDynamics Health Rules Export/Import API
  slug: appdynamics-health-rules-export-import-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve metric hierarchy and metric data for monitored applications with configurable time ranges and aggregation.
  name: AppDynamics Metrics API
  slug: appdynamics-metrics-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve node information for monitored applications including node names, IDs, machine details, and agent versions.
  name: AppDynamics Nodes API
  slug: appdynamics-nodes-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Generate and manage OAuth 2.0 access tokens for authenticating against AppDynamics APIs using the Client Credentials Grant flow.
  name: AppDynamics OAuth Tokens API
  slug: appdynamics-oauth-tokens-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Manage alerting policies that connect health rule violations to automated response actions.
  name: AppDynamics Policies API
  slug: appdynamics-policies-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Query stored events using the AppDynamics Analytics Query Language (ADQL) for custom analytics and reporting.
  name: AppDynamics Queries API
  slug: appdynamics-queries-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Query MELT observation data using the Cisco AppDynamics domain-specific query language.
  name: AppDynamics Query Service API
  slug: appdynamics-query-service-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve lists of supported cloud regions and services for connection configuration.
  name: AppDynamics Reference Data API
  slug: appdynamics-reference-data-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Manage custom event schemas that define the structure and data types for custom analytics events.
  name: AppDynamics Schemas API
  slug: appdynamics-schemas-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Check the status of the AppDynamics Controller server.
  name: AppDynamics Server Status API
  slug: appdynamics-server-status-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve transaction request snapshots for detailed performance analysis of individual requests.
  name: AppDynamics Snapshots API
  slug: appdynamics-snapshots-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Retrieve tier information for monitored applications including tier names and IDs.
  name: AppDynamics Tiers API
  slug: appdynamics-tiers-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Export and import business transaction detection rule configurations.
  name: AppDynamics Transaction Detection Export/Import API
  slug: appdynamics-transaction-detection-export-import-api
artifact_total: 124
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AppDynamics Alert and Respond Actions API
  slug: open-appdynamics-actions-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Actions Export/Import API
  slug: open-appdynamics-actions-export-import-api
- collection_type: open
  name: AppDynamics Alert and Respond API
  slug: open-appdynamics-alert-and-respond-api
- collection_type: open
  name: AppDynamics Analytics Events API
  slug: open-appdynamics-analytics-events-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Applications API
  slug: open-appdynamics-applications-api
- collection_type: open
  name: AppDynamics OAuth Authentication API
  slug: open-appdynamics-authentication-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Backends API
  slug: open-appdynamics-backends-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Business Transactions API
  slug: open-appdynamics-business-transactions-api
- collection_type: open
  name: Cisco Cloud Observability API
  slug: open-appdynamics-cloud-observability-api
- collection_type: open
  name: AppDynamics Configuration API
  slug: open-appdynamics-configuration-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Configurations API
  slug: open-appdynamics-configurations-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Connections API
  slug: open-appdynamics-connections-api
- collection_type: open
  name: AppDynamics Controller REST API
  slug: open-appdynamics-controller-rest-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Custom Dashboards Export/Import API
  slug: open-appdynamics-custom-dashboards-export-import-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Custom Metrics API
  slug: open-appdynamics-custom-metrics-api
- collection_type: open
  name: AppDynamics Database Agent API
  slug: open-appdynamics-database-agent-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Database Collectors API
  slug: open-appdynamics-database-collectors-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Events API
  slug: open-appdynamics-events-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Health Rules API
  slug: open-appdynamics-health-rules-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Health Rules Export/Import API
  slug: open-appdynamics-health-rules-export-import-api
- collection_type: open
  name: AppDynamics Machine Agent API
  slug: open-appdynamics-machine-agent-api
- collection_type: open
  name: AppDynamics Metric and Snapshot API
  slug: open-appdynamics-metric-and-snapshot-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Metrics API
  slug: open-appdynamics-metrics-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Nodes API
  slug: open-appdynamics-nodes-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions OAuth Tokens API
  slug: open-appdynamics-oauth-tokens-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Policies API
  slug: open-appdynamics-policies-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Queries API
  slug: open-appdynamics-queries-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Query Service API
  slug: open-appdynamics-query-service-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Reference Data API
  slug: open-appdynamics-reference-data-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Schemas API
  slug: open-appdynamics-schemas-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Server Status API
  slug: open-appdynamics-server-status-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Snapshots API
  slug: open-appdynamics-snapshots-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Tiers API
  slug: open-appdynamics-tiers-api
- collection_type: open
  name: AppDynamics Alert and Respond Actions Transaction Detection Export/Import API
  slug: open-appdynamics-transaction-detection-export-import-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appdynamics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appdynamics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appdynamics-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appdynamics
- group: design
  title: ''
  type: JSONLD
  url: json-ld/appdynamics-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/appdynamics-application-model-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/appdynamics-health-rule-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/appdynamics-database-collector-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/appdynamics-analytics-event-schema.json
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appdynamics.com/appd/24.x/24.3/en/extend-cisco-appdynamics/cisco-appdynamics-apis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/site/appdynamics/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/appdynamics/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Appdynamics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appdynamics.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.cisco.com/c/en/us/support/index.html
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/appdynamics-application-model-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/appdynamics-health-rule-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/appdynamics-database-collector-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/appdynamics-analytics-event-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/appdynamics-application-model-example.json
- group: build
  title: ''
  type: Examples
  url: examples/appdynamics-health-rule-example.json
- group: build
  title: ''
  type: Examples
  url: examples/appdynamics-database-collector-example.json
- group: build
  title: ''
  type: Examples
  url: examples/appdynamics-analytics-event-example.json
description: AppDynamics, now part of Cisco, is an application performance monitoring (APM) and observability platform that provides full-stack visibility into application, business, and infrastructure performance. The platform offers REST APIs for controller management, metrics, alerts, analytics events, database monitoring, and the next-generation Cisco Cloud Observability platform.
examples:
- key_count: 3
  name: Appdynamics Analytics Event Example
  slug: appdynamics-analytics-event-example
- key_count: 5
  name: Appdynamics Application Model Example
  slug: appdynamics-application-model-example
- key_count: 11
  name: Appdynamics Database Collector Example
  slug: appdynamics-database-collector-example
- key_count: 8
  name: Appdynamics Health Rule Example
  slug: appdynamics-health-rule-example
features:
- description: Full-stack APM with code-level visibility into Java, .NET, Node.js, PHP, Python, Go, and Ruby applications.
  name: Application Performance Monitoring
- description: End-to-end transaction tracing correlating application performance with business outcomes.
  name: Business Transaction Monitoring
- description: Automatic baselining and AI-driven anomaly detection to identify performance degradation.
  name: AI-Powered Anomaly Detection
- description: Server, container, and Kubernetes infrastructure monitoring via Machine Agent.
  name: Infrastructure Monitoring
- description: Database performance monitoring for PostgreSQL, MySQL, MongoDB, Oracle, and more.
  name: Database Monitoring
- description: Custom analytics events ingestion for correlating business data with application performance.
  name: Analytics Events API
- description: Next-generation Cisco Cloud Observability platform with OpenTelemetry support and cloud provider connections.
  name: Cloud Observability
- description: Configurable health rules and automated alerting with policy-based response actions.
  name: Health Rules and Alerting
- description: Import/export configuration for backup, restore, and migration between Controller instances.
  name: Configuration Management API
- description: Short-lived OAuth 2.0 access tokens for secure API authentication via Cisco platform.
  name: OAuth 2.0 Authentication
finops:
- name: Appdynamics Finops
  service_category: Observability / APM
  slug: appdynamics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appdynamics.png
integrations:
- description: Integration with Cisco FSO platform and Thousand Eyes for end-to-end observability.
  name: Cisco Full-Stack Observability
- description: Support for OpenTelemetry metrics ingestion via Cisco Cloud Observability common ingestion pipeline.
  name: OpenTelemetry
- description: Integration with Splunk for log correlation and SIEM.
  name: Splunk
- description: ITSM integration for automated incident and change management.
  name: ServiceNow
- description: Alerting integration for automated on-call notification and incident management.
  name: PagerDuty
- description: Amazon Web Services cloud connection for infrastructure and application monitoring.
  name: AWS
- description: Microsoft Azure cloud connection for cloud-native observability.
  name: Azure
- description: Google Cloud Platform connection for multi-cloud observability.
  name: GCP
json_schemas:
- name: AccessTokenResponse
  property_count: 4
  slug: appdynamics-accesstokenresponse
- name: Action
  property_count: 7
  slug: appdynamics-action
- name: AppDynamics Analytics Event
  property_count: 3
  slug: appdynamics-analytics-event
- name: AppDynamics Application Model
  property_count: 5
  slug: appdynamics-application-model
- name: Application
  property_count: 3
  slug: appdynamics-application
- name: Backend
  property_count: 4
  slug: appdynamics-backend
- name: BusinessTransaction
  property_count: 7
  slug: appdynamics-businesstransaction
- name: CloudConnection
  property_count: 8
  slug: appdynamics-cloudconnection
- name: CloudHealthRule
  property_count: 9
  slug: appdynamics-cloudhealthrule
- name: ConnectionConfiguration
  property_count: 6
  slug: appdynamics-connectionconfiguration
- name: CustomMetric
  property_count: 3
  slug: appdynamics-custommetric
- name: AppDynamics Database Collector
  property_count: 11
  slug: appdynamics-database-collector
- name: DatabaseCollector
  property_count: 11
  slug: appdynamics-databasecollector
- name: EventSchema
  property_count: 1
  slug: appdynamics-eventschema
- name: AppDynamics Health Rule
  property_count: 8
  slug: appdynamics-health-rule
- name: HealthRule
  property_count: 8
  slug: appdynamics-healthrule
- name: MetricData
  property_count: 5
  slug: appdynamics-metricdata
- name: MetricFolder
  property_count: 2
  slug: appdynamics-metricfolder
- name: MetricValue
  property_count: 9
  slug: appdynamics-metricvalue
- name: Node
  property_count: 12
  slug: appdynamics-node
- name: Policy
  property_count: 7
  slug: appdynamics-policy
- name: QueryResult
  property_count: 4
  slug: appdynamics-queryresult
- name: RequestSnapshot
  property_count: 16
  slug: appdynamics-requestsnapshot
- name: Tier
  property_count: 5
  slug: appdynamics-tier
json_structures:
- name: Appdynamics Analytics Event Structure
  property_count: 3
  slug: appdynamics-analytics-event-structure
- name: Appdynamics Application Model Structure
  property_count: 5
  slug: appdynamics-application-model-structure
- name: Appdynamics Database Collector Structure
  property_count: 11
  slug: appdynamics-database-collector-structure
- name: Appdynamics Health Rule Structure
  property_count: 8
  slug: appdynamics-health-rule-structure
- name: Appdynamics Structure
  property_count: 0
  slug: appdynamics-structure
jsonld:
- class_count: 0
  name: Appdynamics Context
  property_count: 11
  slug: appdynamics-context
layout: provider
modified: '2026-08-19'
name: AppDynamics
nav: Providers
network: true
overview: 'AppDynamics publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Actions Export/Import API, Applications API, and 22 more. Tagged areas include APM, Application Performance Monitoring, Cisco, Cloud Observability, and DevOps.


  The AppDynamics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AppDynamics'' developer surface includes authentication, documentation, getting-started guide, pricing, support, code examples, and 18 more developer resources.'
plans:
- name: Appdynamics Plans Pricing
  plan_count: 7
  slug: appdynamics-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Appdynamics Rate Limits
  slug: appdynamics-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: AppDynamics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: appdynamics-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 67.4
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appdynamics/refs/heads/main/screenshots/appdynamics-2026-06-20T172314.png
security:
- kind: authentication
  name: Appdynamics Authentication
  slug: appdynamics-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Appdynamics Domain Security
  slug: appdynamics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appdynamics
tags:
- APM
- Application Performance Monitoring
- Cisco
- Cloud Observability
- DevOps
- Monitoring
- Observability
- OpenTelemetry
use_cases:
- description: Identify and resolve performance bottlenecks at the code level before they impact end users.
  name: Application Performance Optimization
- description: Integrate performance monitoring into CI/CD pipelines using the Controller REST API.
  name: DevOps Integration
- description: Monitor application performance during and after cloud migration using Cloud Observability.
  name: Cloud Migration Monitoring
- description: Correlate application performance data with business metrics using the Analytics Events API.
  name: Business Impact Analysis
- description: Automate incident response workflows by integrating AppDynamics alerting with ticketing systems.
  name: Automated Incident Response
website: https://developer.cisco.com/site/appdynamics/
---

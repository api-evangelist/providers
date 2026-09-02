---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Sap Hana Agentic Access
  operation_count: 14
  slug: sap-hana-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- description: SQL interface for querying and managing data in SAP HANA databases.
  name: SAP HANA SQL API
  slug: sap-hana-sql-api
- description: Extended Application Services (XS) for building applications directly on SAP HANA.
  name: SAP HANA XS Engine API
  slug: sap-hana-xs-engine-api
- description: RESTful API for SAP HANA Cockpit administration and monitoring.
  name: SAP HANA Cockpit API
  slug: sap-hana-cockpit-api
- description: APIs for data provisioning, replication, and integration.
  name: SAP HANA Smart Data Integration API
  slug: sap-hana-smart-data-integration-api
- description: REST API for accessing triggered alerts, database metrics, and metering data for SAP HANA Cloud instances.
  name: SAP HANA Cloud Alerts and Metrics REST API
  slug: sap-hana-cloud-alerts-and-metrics-rest-api
- description: REST API providing geocoding, routing, and mapping services through a unified interface supporting multiple back-end service providers.
  name: SAP HANA Spatial Services API
  slug: sap-hana-spatial-services-api
- description: REST API for managing, uploading, reading, deleting, and listing files in SAP HANA Cloud Data Lake file containers.
  name: SAP HANA Cloud Data Lake Files REST API
  slug: sap-hana-cloud-data-lake-files-rest-api
- description: API for managing HDI containers used to deploy database artifacts in isolated schemas with dependency management and lifecycle support.
  name: SAP HANA Deployment Infrastructure (HDI) API
  slug: sap-hana-deployment-infrastructure-hdi-api
- description: In-database machine learning and statistical algorithms library providing clustering, classification, regression, and time series analysis capabilities.
  name: SAP HANA Predictive Analysis Library (PAL) API
  slug: sap-hana-predictive-analysis-library-pal-api
- description: API for storing, querying, and managing semi-structured JSON documents within SAP HANA using a hybrid relational and document-oriented approach.
  name: SAP HANA JSON Document Store API
  slug: sap-hana-json-document-store-api
- description: Graph processing engine for network analysis with built-in algorithms for path finding, pattern matching, and knowledge graph capabilities using OpenCypher and SPARQL.
  name: SAP HANA Graph Engine API
  slug: sap-hana-graph-engine-api
- description: REST API for retrieving system information and metadata about SAP HANA Platform instances.
  name: SAP HANA REST Info API
  slug: sap-hana-rest-info-api
- description: Operations for accessing and managing triggered alerts for SAP HANA Cloud instances, including alert state queries, severity filtering, and alert rule configuration.
  name: SAP HANA Alerts API
  slug: sap-hana-alerts-api
- description: Operations for creating and managing instance mappings that associate SAP HANA Cloud instances across subaccounts and environments.
  name: SAP HANA Instance Mappings API
  slug: sap-hana-instance-mappings-api
- description: Operations for managing SAP HANA Cloud database instances including provisioning, configuration, lifecycle management, and status retrieval.
  name: SAP HANA Instances API
  slug: sap-hana-instances-api
- description: Operations for accessing consumption metering data used for billing and capacity planning for SAP HANA Cloud instances.
  name: SAP HANA Metering API
  slug: sap-hana-metering-api
- description: Operations for retrieving database performance metrics and resource utilization data for SAP HANA Cloud instances.
  name: SAP HANA Metrics API
  slug: sap-hana-metrics-api
artifact_total: 157
collections:
- collection_type: postman
  name: SAP HANA Cloud REST Alerts API
  slug: postman-sap-hana-alerts-api
- collection_type: postman
  name: SAP HANA Cloud REST Alerts Instance Mappings API
  slug: postman-sap-hana-instance-mappings-api
- collection_type: postman
  name: SAP HANA Cloud REST Alerts Instances API
  slug: postman-sap-hana-instances-api
- collection_type: postman
  name: SAP HANA Cloud REST Alerts Metering API
  slug: postman-sap-hana-metering-api
- collection_type: postman
  name: SAP HANA Cloud REST Alerts Metrics API
  slug: postman-sap-hana-metrics-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP HANA Cloud REST Alerts API
  slug: open-sap-hana-alerts-api
- collection_type: open
  name: SAP HANA Cloud REST API
  slug: open-sap-hana-cloud-rest-api
- collection_type: open
  name: SAP HANA Cloud REST Alerts Instance Mappings API
  slug: open-sap-hana-instance-mappings-api
- collection_type: open
  name: SAP HANA Cloud REST Alerts Instances API
  slug: open-sap-hana-instances-api
- collection_type: open
  name: SAP HANA Cloud REST Alerts Metering API
  slug: open-sap-hana-metering-api
- collection_type: open
  name: SAP HANA Cloud REST Alerts Metrics API
  slug: open-sap-hana-metrics-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sap-hana-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-hana/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-hana-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-hana-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-hana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-hana-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-hana-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/sap-hana
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sap.com/
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sap.com/products/technology-platform/hana/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/trust-center/agreements.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sap.com/products/data-cloud/hana/get-started.html
- group: learn
  title: ''
  type: Tutorials
  url: https://developers.sap.com/tutorial-navigator.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/SAP-samples
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sap-hana-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/sap-hana-spectral-rules.yml
created: '2024-01-01'
description: APIs for SAP HANA, an in-memory, column-oriented, relational database management system developed and marketed by SAP SE.
examples:
- key_count: 12
  name: Sap Hana Cloud Rest Alert Event Example
  slug: sap-hana-cloud-rest-alert-event-example
- key_count: 1
  name: Sap Hana Cloud Rest Alert Event List Example
  slug: sap-hana-cloud-rest-alert-event-list-example
- key_count: 10
  name: Sap Hana Cloud Rest Alert Rule Example
  slug: sap-hana-cloud-rest-alert-rule-example
- key_count: 1
  name: Sap Hana Cloud Rest Alert Rule List Example
  slug: sap-hana-cloud-rest-alert-rule-list-example
- key_count: 2
  name: Sap Hana Cloud Rest Create Instance Mapping Request Example
  slug: sap-hana-cloud-rest-create-instance-mapping-request-example
- key_count: 3
  name: Sap Hana Cloud Rest Create Service Instance Request Example
  slug: sap-hana-cloud-rest-create-service-instance-request-example
- key_count: 3
  name: Sap Hana Cloud Rest Error Example
  slug: sap-hana-cloud-rest-error-example
- key_count: 5
  name: Sap Hana Cloud Rest Instance Mapping Example
  slug: sap-hana-cloud-rest-instance-mapping-example
- key_count: 1
  name: Sap Hana Cloud Rest Instance Mapping List Example
  slug: sap-hana-cloud-rest-instance-mapping-list-example
- key_count: 1
  name: Sap Hana Cloud Rest Instance Parameters Example
  slug: sap-hana-cloud-rest-instance-parameters-example
- key_count: 10
  name: Sap Hana Cloud Rest Inventory Instance Example
  slug: sap-hana-cloud-rest-inventory-instance-example
- key_count: 2
  name: Sap Hana Cloud Rest Inventory Instance List Example
  slug: sap-hana-cloud-rest-inventory-instance-list-example
- key_count: 5
  name: Sap Hana Cloud Rest Last Operation Example
  slug: sap-hana-cloud-rest-last-operation-example
- key_count: 5
  name: Sap Hana Cloud Rest Metering Value Example
  slug: sap-hana-cloud-rest-metering-value-example
- key_count: 1
  name: Sap Hana Cloud Rest Metering Value List Example
  slug: sap-hana-cloud-rest-metering-value-list-example
- key_count: 5
  name: Sap Hana Cloud Rest Metric Data Point Example
  slug: sap-hana-cloud-rest-metric-data-point-example
- key_count: 3
  name: Sap Hana Cloud Rest Metric Series Example
  slug: sap-hana-cloud-rest-metric-series-example
- key_count: 1
  name: Sap Hana Cloud Rest Metric Value List Example
  slug: sap-hana-cloud-rest-metric-value-list-example
- key_count: 10
  name: Sap Hana Cloud Rest Service Instance Example
  slug: sap-hana-cloud-rest-service-instance-example
- key_count: 3
  name: Sap Hana Cloud Rest Service Instance List Example
  slug: sap-hana-cloud-rest-service-instance-list-example
- key_count: 1
  name: Sap Hana Cloud Rest Update Alert Rules Request Example
  slug: sap-hana-cloud-rest-update-alert-rules-request-example
- key_count: 3
  name: Sap Hana Cloud Rest Update Service Instance Request Example
  slug: sap-hana-cloud-rest-update-service-instance-request-example
- key_count: 6
  name: Sap Hana Createinstancemapping Example
  slug: sap-hana-createinstancemapping-example
- key_count: 6
  name: Sap Hana Createserviceinstance Example
  slug: sap-hana-createserviceinstance-example
- key_count: 6
  name: Sap Hana Getmeteringvalues Example
  slug: sap-hana-getmeteringvalues-example
- key_count: 6
  name: Sap Hana Getmetricvalues Example
  slug: sap-hana-getmetricvalues-example
- key_count: 6
  name: Sap Hana Getserviceinstance Example
  slug: sap-hana-getserviceinstance-example
- key_count: 6
  name: Sap Hana Listalertevents Example
  slug: sap-hana-listalertevents-example
- key_count: 6
  name: Sap Hana Listalertrules Example
  slug: sap-hana-listalertrules-example
- key_count: 6
  name: Sap Hana Listinstancemappings Example
  slug: sap-hana-listinstancemappings-example
- key_count: 6
  name: Sap Hana Listinventoryinstances Example
  slug: sap-hana-listinventoryinstances-example
- key_count: 6
  name: Sap Hana Listserviceinstances Example
  slug: sap-hana-listserviceinstances-example
- key_count: 6
  name: Sap Hana Updatealertrules Example
  slug: sap-hana-updatealertrules-example
- key_count: 6
  name: Sap Hana Updateserviceinstance Example
  slug: sap-hana-updateserviceinstance-example
features:
- description: Process massive datasets in real-time using columnar in-memory storage for analytics and transactions.
  name: In-Memory Computing
- description: Support for relational, graph, spatial, JSON document, and time series data in a single database.
  name: Multi-Model Processing
- description: Fully managed cloud database service with elastic scaling, automated backups, and multi-region deployment.
  name: Cloud Native
- description: Built-in machine learning algorithms through the Predictive Analysis Library for in-database analytics.
  name: Predictive Analytics
- description: Seamlessly extend storage with SAP HANA Cloud Data Lake for cost-effective warm and cold data management.
  name: Data Lake Integration
- description: Real-time and batch data replication from heterogeneous sources with built-in data quality.
  name: Smart Data Integration
finops:
- name: Sap Hana Finops
  service_category: Database
  slug: sap-hana-finops
image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
integrations:
- description: Native integration with SAP Business Technology Platform for enterprise application development.
  name: SAP BTP
- description: Serve as the underlying database for SAP S/4HANA ERP suite.
  name: SAP S/4HANA
- description: Direct live connections for real-time business intelligence dashboards and planning.
  name: SAP Analytics Cloud
- description: Deploy SAP HANA Cloud instances on Azure infrastructure with cross-cloud governance.
  name: Microsoft Azure
json_schemas:
- name: AlertEvent
  property_count: 12
  slug: sap-hana-alertevent
- name: AlertEventList
  property_count: 1
  slug: sap-hana-alerteventlist
- name: AlertRule
  property_count: 10
  slug: sap-hana-alertrule
- name: AlertRuleList
  property_count: 1
  slug: sap-hana-alertrulelist
- name: AlertEventList
  property_count: 1
  slug: sap-hana-cloud-rest-alert-event-list
- name: AlertEvent
  property_count: 12
  slug: sap-hana-cloud-rest-alert-event
- name: AlertRuleList
  property_count: 1
  slug: sap-hana-cloud-rest-alert-rule-list
- name: AlertRule
  property_count: 10
  slug: sap-hana-cloud-rest-alert-rule
- name: CreateInstanceMappingRequest
  property_count: 2
  slug: sap-hana-cloud-rest-create-instance-mapping-request
- name: CreateServiceInstanceRequest
  property_count: 3
  slug: sap-hana-cloud-rest-create-service-instance-request
- name: Error
  property_count: 3
  slug: sap-hana-cloud-rest-error
- name: InstanceMappingList
  property_count: 1
  slug: sap-hana-cloud-rest-instance-mapping-list
- name: InstanceMapping
  property_count: 5
  slug: sap-hana-cloud-rest-instance-mapping
- name: InstanceParameters
  property_count: 1
  slug: sap-hana-cloud-rest-instance-parameters
- name: InventoryInstanceList
  property_count: 2
  slug: sap-hana-cloud-rest-inventory-instance-list
- name: InventoryInstance
  property_count: 10
  slug: sap-hana-cloud-rest-inventory-instance
- name: LastOperation
  property_count: 5
  slug: sap-hana-cloud-rest-last-operation
- name: MeteringValueList
  property_count: 1
  slug: sap-hana-cloud-rest-metering-value-list
- name: MeteringValue
  property_count: 5
  slug: sap-hana-cloud-rest-metering-value
- name: MetricDataPoint
  property_count: 5
  slug: sap-hana-cloud-rest-metric-data-point
- name: MetricSeries
  property_count: 3
  slug: sap-hana-cloud-rest-metric-series
- name: MetricValueList
  property_count: 1
  slug: sap-hana-cloud-rest-metric-value-list
- name: ServiceInstanceList
  property_count: 3
  slug: sap-hana-cloud-rest-service-instance-list
- name: ServiceInstance
  property_count: 10
  slug: sap-hana-cloud-rest-service-instance
- name: UpdateAlertRulesRequest
  property_count: 1
  slug: sap-hana-cloud-rest-update-alert-rules-request
- name: UpdateServiceInstanceRequest
  property_count: 3
  slug: sap-hana-cloud-rest-update-service-instance-request
- name: CreateInstanceMappingRequest
  property_count: 2
  slug: sap-hana-createinstancemappingrequest
- name: CreateServiceInstanceRequest
  property_count: 4
  slug: sap-hana-createserviceinstancerequest
- name: SAP HANA Cloud Database Instance
  property_count: 18
  slug: sap-hana-database
- name: Error
  property_count: 3
  slug: sap-hana-error
- name: InstanceMapping
  property_count: 5
  slug: sap-hana-instancemapping
- name: InstanceMappingList
  property_count: 1
  slug: sap-hana-instancemappinglist
- name: InstanceParameters
  property_count: 1
  slug: sap-hana-instanceparameters
- name: InventoryInstance
  property_count: 10
  slug: sap-hana-inventoryinstance
- name: InventoryInstanceList
  property_count: 2
  slug: sap-hana-inventoryinstancelist
- name: LastOperation
  property_count: 5
  slug: sap-hana-lastoperation
- name: MeteringValue
  property_count: 5
  slug: sap-hana-meteringvalue
- name: MeteringValueList
  property_count: 1
  slug: sap-hana-meteringvaluelist
- name: MetricDataPoint
  property_count: 5
  slug: sap-hana-metricdatapoint
- name: MetricSeries
  property_count: 3
  slug: sap-hana-metricseries
- name: MetricValueList
  property_count: 1
  slug: sap-hana-metricvaluelist
- name: ServiceInstance
  property_count: 12
  slug: sap-hana-serviceinstance
- name: ServiceInstanceList
  property_count: 3
  slug: sap-hana-serviceinstancelist
- name: UpdateAlertRulesRequest
  property_count: 1
  slug: sap-hana-updatealertrulesrequest
- name: UpdateServiceInstanceRequest
  property_count: 4
  slug: sap-hana-updateserviceinstancerequest
json_structures:
- name: Sap Hana Cloud Rest Alert Event List Structure
  property_count: 1
  slug: sap-hana-cloud-rest-alert-event-list-structure
- name: Sap Hana Cloud Rest Alert Event Structure
  property_count: 12
  slug: sap-hana-cloud-rest-alert-event-structure
- name: Sap Hana Cloud Rest Alert Rule List Structure
  property_count: 1
  slug: sap-hana-cloud-rest-alert-rule-list-structure
- name: Sap Hana Cloud Rest Alert Rule Structure
  property_count: 10
  slug: sap-hana-cloud-rest-alert-rule-structure
- name: Sap Hana Cloud Rest Create Instance Mapping Request Structure
  property_count: 2
  slug: sap-hana-cloud-rest-create-instance-mapping-request-structure
- name: Sap Hana Cloud Rest Create Service Instance Request Structure
  property_count: 3
  slug: sap-hana-cloud-rest-create-service-instance-request-structure
- name: Sap Hana Cloud Rest Error Structure
  property_count: 3
  slug: sap-hana-cloud-rest-error-structure
- name: Sap Hana Cloud Rest Instance Mapping List Structure
  property_count: 1
  slug: sap-hana-cloud-rest-instance-mapping-list-structure
- name: Sap Hana Cloud Rest Instance Mapping Structure
  property_count: 5
  slug: sap-hana-cloud-rest-instance-mapping-structure
- name: Sap Hana Cloud Rest Instance Parameters Structure
  property_count: 1
  slug: sap-hana-cloud-rest-instance-parameters-structure
- name: Sap Hana Cloud Rest Inventory Instance List Structure
  property_count: 2
  slug: sap-hana-cloud-rest-inventory-instance-list-structure
- name: Sap Hana Cloud Rest Inventory Instance Structure
  property_count: 10
  slug: sap-hana-cloud-rest-inventory-instance-structure
- name: Sap Hana Cloud Rest Last Operation Structure
  property_count: 5
  slug: sap-hana-cloud-rest-last-operation-structure
- name: Sap Hana Cloud Rest Metering Value List Structure
  property_count: 1
  slug: sap-hana-cloud-rest-metering-value-list-structure
- name: Sap Hana Cloud Rest Metering Value Structure
  property_count: 5
  slug: sap-hana-cloud-rest-metering-value-structure
- name: Sap Hana Cloud Rest Metric Data Point Structure
  property_count: 5
  slug: sap-hana-cloud-rest-metric-data-point-structure
- name: Sap Hana Cloud Rest Metric Series Structure
  property_count: 3
  slug: sap-hana-cloud-rest-metric-series-structure
- name: Sap Hana Cloud Rest Metric Value List Structure
  property_count: 1
  slug: sap-hana-cloud-rest-metric-value-list-structure
- name: Sap Hana Cloud Rest Service Instance List Structure
  property_count: 3
  slug: sap-hana-cloud-rest-service-instance-list-structure
- name: Sap Hana Cloud Rest Service Instance Structure
  property_count: 10
  slug: sap-hana-cloud-rest-service-instance-structure
- name: Sap Hana Cloud Rest Update Alert Rules Request Structure
  property_count: 1
  slug: sap-hana-cloud-rest-update-alert-rules-request-structure
- name: Sap Hana Cloud Rest Update Service Instance Request Structure
  property_count: 3
  slug: sap-hana-cloud-rest-update-service-instance-request-structure
- name: Sap Hana Structure
  property_count: 0
  slug: sap-hana-structure
jsonld:
- class_count: 0
  name: Sap Hana Cloud Rest Context
  property_count: 0
  slug: sap-hana-cloud-rest-context
- class_count: 0
  name: Sap Hana Context
  property_count: 14
  slug: sap-hana-context
layout: provider
modified: '2026-05-19'
name: SAP HANA
nav: Providers
network: true
overview: 'SAP HANA publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Instance Mappings API, Instances API, and 2 more. Tagged areas include Analytics, Cloud, Database, Enterprise, and In-Memory.


  The SAP HANA catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  SAP HANA''s developer surface includes authentication, support, pricing, getting-started guide, and 15 more developer resources.'
plans:
- name: Sap Hana Plans Pricing
  plan_count: 1
  slug: sap-hana-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Sap Hana Rate Limits
  slug: sap-hana-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SAP HANA API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: sap-hana-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: SAP HANA API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 11
  slug: sap-hana-spectral-rules
scopes:
- name: Sap Hana Scopes
  scope_count: 0
  slug: sap-hana-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 13.6
    contract_quality: 76.2
    developer_ergonomics: 42.9
    discoverability: 61.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-hana/refs/heads/main/screenshots/sap-hana-2026-06-20T193427.png
security:
- kind: authentication
  name: Sap Hana Authentication
  slug: sap-hana-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sap Hana Domain Security
  slug: sap-hana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Hana Vulnerability Disclosure
  slug: sap-hana-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-hana
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
use_cases:
- description: Run complex analytical queries on live transactional data without ETL delays.
  name: Real-Time Analytics
- description: Build high-performance applications directly on the database using XS Engine and HDI containers.
  name: Application Development
- description: Ingest and analyze high-volume sensor and device data with time series and spatial capabilities.
  name: IoT Data Processing
- description: Consolidate enterprise data for reporting and business intelligence with columnar compression.
  name: Enterprise Data Warehousing
website: https://api.sap.com/
---

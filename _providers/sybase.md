---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Sybase Agentic Access
  operation_count: 16
  slug: sybase-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 12
apis:
- description: APIs for Sybase mobile application development and management.
  name: SAP Mobile Platform API
  slug: sap-mobile-platform-api
- description: SAP SQL Anywhere includes a built-in HTTP web server that exposes database objects as OData and REST web services. Developers can create SERVICE objects that transform SQL query results into XML, HTML
  name: SAP SQL Anywhere HTTP Web Services
  slug: sap-sql-anywhere-http-web-services
- description: The SDK for SAP Adaptive Server Enterprise is a set of libraries and utilities for developing client applications. It includes SAP Open Client for C-language applications, Embedded SQL precompilers fo
  name: SDK for SAP ASE
  slug: sdk-for-sap-ase
- description: SAP Replication Server provides real-time data replication between SAP ASE databases and heterogeneous data sources. It uses Replication Command Language (RCL) to manage replication definitions, publi
  name: SAP Replication Server
  slug: sap-replication-server
- description: SAP ASE Cockpit is a web-based administration and management console for SAP Adaptive Server Enterprise. It provides monitoring, configuration, and management capabilities for ASE servers through a br
  name: SAP ASE Cockpit
  slug: sap-ase-cockpit
- description: Operations for managing database backup and recovery operations including scheduling and status monitoring.
  name: Sybase Backups API
  slug: sybase-backups-api
- description: Operations for viewing and modifying SAP ASE server configuration parameters via sp_configure equivalents.
  name: Sybase Configuration API
  slug: sybase-configuration-api
- description: Operations for managing databases within an SAP ASE server including creation, configuration, and status monitoring.
  name: Sybase Databases API
  slug: sybase-databases-api
- description: Operations for managing database devices and disk storage resources used by SAP ASE.
  name: Sybase Devices API
  slug: sybase-devices-api
- description: Operations for monitoring server performance metrics including cache statistics, lock activity, and resource utilization.
  name: Sybase Performance API
  slug: sybase-performance-api
- description: Operations for retrieving server information, status, and configuration details for SAP ASE instances.
  name: Sybase Servers API
  slug: sybase-servers-api
- description: Operations for managing server logins and database users including role assignments and permission management.
  name: Sybase Users API
  slug: sybase-users-api
artifact_total: 58
collections:
- collection_type: postman
  name: Sybase ASE REST Backups API
  slug: postman-sybase-backups-api
- collection_type: postman
  name: Sybase ASE REST Backups Configuration API
  slug: postman-sybase-configuration-api
- collection_type: postman
  name: Sybase ASE REST Backups Databases API
  slug: postman-sybase-databases-api
- collection_type: postman
  name: Sybase ASE REST Backups Devices API
  slug: postman-sybase-devices-api
- collection_type: postman
  name: Sybase ASE REST Backups Performance API
  slug: postman-sybase-performance-api
- collection_type: postman
  name: Sybase ASE REST Backups Servers API
  slug: postman-sybase-servers-api
- collection_type: postman
  name: Sybase ASE REST Backups Users API
  slug: postman-sybase-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sybase ASE REST API
  slug: open-sybase-ase-rest-api
- collection_type: open
  name: Sybase ASE REST Backups API
  slug: open-sybase-backups-api
- collection_type: open
  name: Sybase ASE REST Backups Configuration API
  slug: open-sybase-configuration-api
- collection_type: open
  name: Sybase ASE REST Backups Databases API
  slug: open-sybase-databases-api
- collection_type: open
  name: Sybase ASE REST Backups Devices API
  slug: open-sybase-devices-api
- collection_type: open
  name: Sybase ASE REST Backups Performance API
  slug: open-sybase-performance-api
- collection_type: open
  name: Sybase ASE REST Backups Servers API
  slug: open-sybase-servers-api
- collection_type: open
  name: Sybase ASE REST Backups Users API
  slug: open-sybase-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sybase/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sybase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sybase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sybase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sybase-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sybase-software
- group: start
  title: ''
  type: Portal
  url: https://support.sap.com/sybase
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com/en/product/database.html
- group: operate
  title: ''
  type: Community
  url: https://pages.community.sap.com/topics/applications-on-ase
- group: other
  title: ''
  type: Downloads
  url: https://support.sap.com/swdc
- group: company
  title: ''
  type: Blog
  url: https://blogs.sap.com/tags/products-sybase/
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/data-cloud/sybase-ase.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_ASE
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/SAP_ASE/9623e59098a24dc6b9013ba5d709309e/13ec24bd751e1014bf789ad719f1de31.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.sap.com/docs/SAP_ASE/791c41982ee345a19c4ec4b774222c4f/5db753f3a9c24ddcabc2581a98b99585.html
- group: start
  title: ''
  type: Login
  url: https://accounts.sap.com
- group: start
  title: ''
  type: Signup
  url: https://www.sap.com/products/technology-platform/sybase-ase/trial.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sqlanywhere
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/sybase
- group: build
  title: ''
  type: SDKs
  url: https://help.sap.com/docs/SAP_ASE_SDK
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sap.com/products/data-cloud/sybase-ase.html
created: '2024'
description: A collection of APIs and resources for Sybase database systems.
examples:
- key_count: 4
  name: Sybase Get Performance Metrics Example
  slug: sybase-get-performance-metrics-example
- key_count: 4
  name: Sybase List Databases Example
  slug: sybase-list-databases-example
finops:
- name: Sybase Finops
  service_category: Enterprise Database
  slug: sybase-finops
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
json_schemas:
- name: Backup
  property_count: 8
  slug: sybase-backup
- name: BackupCreateRequest
  property_count: 4
  slug: sybase-backupcreaterequest
- name: CacheMetrics
  property_count: 5
  slug: sybase-cachemetrics
- name: ConfigParameter
  property_count: 7
  slug: sybase-configparameter
- name: Configuration
  property_count: 1
  slug: sybase-configuration
- name: ConfigurationUpdateRequest
  property_count: 1
  slug: sybase-configurationupdaterequest
- name: Sybase ASE Database
  property_count: 8
  slug: sybase-database
- name: DatabaseCreateRequest
  property_count: 5
  slug: sybase-databasecreaterequest
- name: Device
  property_count: 6
  slug: sybase-device
- name: Error
  property_count: 3
  slug: sybase-error
- name: LockMetrics
  property_count: 7
  slug: sybase-lockmetrics
- name: Login
  property_count: 6
  slug: sybase-login
- name: LoginCreateRequest
  property_count: 4
  slug: sybase-logincreaterequest
- name: PerformanceMetrics
  property_count: 10
  slug: sybase-performancemetrics
- name: Sybase ASE Server
  property_count: 9
  slug: sybase-server
- name: ServerStatus
  property_count: 9
  slug: sybase-serverstatus
json_structures:
- name: Sybase Server Structure
  property_count: 0
  slug: sybase-server-structure
- name: Sybase Structure
  property_count: 0
  slug: sybase-structure
jsonld:
- class_count: 18
  name: Sybase Context
  property_count: 6
  slug: sybase-context
layout: provider
modified: '2026-05-19'
name: Sybase
nav: Providers
network: true
overview: 'Sybase publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Backups API, Configuration API, Databases API, and 4 more. Tagged areas include Database, Enterprise, SAP, and SQL.


  The Sybase catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sybase''s developer surface includes authentication, developer portal, support, engineering blog, documentation, getting-started guide, changelog, and 17 more developer resources.'
plans:
- name: Sybase Plans Pricing
  plan_count: 1
  slug: sybase-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Sybase Rate Limits
  slug: sybase-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sybase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sybase-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Sybase API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 6
  slug: sybase-rules
score:
  band: developing
  composite: 43.6
  delta: -14.3
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 9.8
    contract_quality: 60.8
    developer_ergonomics: 38.1
    discoverability: 63.0
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sybase/refs/heads/main/screenshots/sybase-2026-06-20T194816.png
security:
- kind: authentication
  name: Sybase Authentication
  slug: sybase-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Sybase Domain Security
  slug: sybase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sybase Vulnerability Disclosure
  slug: sybase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sybase
tags:
- Database
- Enterprise
- SAP
- SQL
website: https://www.sap.com/products/data-cloud/sybase-ase.html
---

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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Dreamfactory Agentic Access
  operation_count: 51
  slug: dreamfactory-agentic-access
  summary_line: 51 operations · 27 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: The DreamFactory System API provides administrative management capabilities for DreamFactory instances. It allows managing services, apps, roles, users, CORS configurations, email templates, environme
  name: DreamFactory System API
  slug: system-api
- description: System administrator management
  name: DreamFactory Admin API
  slug: dreamfactory-admin-api
- description: Application and API key management
  name: DreamFactory App API
  slug: dreamfactory-app-api
- description: Application group management
  name: DreamFactory AppGroup API
  slug: dreamfactory-appgroup-api
- description: Cross-Origin Resource Sharing configuration
  name: DreamFactory CORS API
  slug: dreamfactory-cors-api
- description: Custom settings management
  name: DreamFactory Custom API
  slug: dreamfactory-custom-api
- description: Email template management
  name: DreamFactory EmailTemplate API
  slug: dreamfactory-emailtemplate-api
- description: Environment information
  name: DreamFactory Environment API
  slug: dreamfactory-environment-api
- description: Event management
  name: DreamFactory Event API
  slug: dreamfactory-event-api
- description: API rate limiting management
  name: DreamFactory Limit API
  slug: dreamfactory-limit-api
- description: Lookup key management
  name: DreamFactory Lookup API
  slug: dreamfactory-lookup-api
- description: Package import and export
  name: DreamFactory Package API
  slug: dreamfactory-package-api
- description: Role-based access control management
  name: DreamFactory Role API
  slug: dreamfactory-role-api
- description: Script type discovery
  name: DreamFactory ScriptType API
  slug: dreamfactory-scripttype-api
- description: Service type discovery
  name: DreamFactory ServiceType API
  slug: dreamfactory-servicetype-api
- description: User management
  name: DreamFactory User API
  slug: dreamfactory-user-api
artifact_total: 93
asyncapis:
- description: Asynchronous event model for the DreamFactory System API. DreamFactory provides a comprehensive event scripting system that fires events before and after every API call, allowing server-side scripts (
  name: DreamFactory System API Events
  slug: dreamfactory-system-api-asyncapi
collections:
- collection_type: open
  name: DreamFactory System API
  slug: open-dreamfactory-system-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dreamfactory-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dreamfactory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dreamfactory-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dreamfactory-software
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dreamfactorysoftware
- group: company
  title: ''
  type: Website
  url: https://www.dreamfactory.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dreamfactory.com/?_gl=1*yrriox*_gcl_au*MTgxMzQyMDU4OC4xNzQ5MTM5NjA0
- group: other
  title: ''
  type: CaseStudies
  url: https://www.dreamfactory.com/stories
- group: other
  title: ''
  type: WhitePapers
  url: https://www.dreamfactory.com/resources/whitepapers
- group: company
  title: ''
  type: Blog
  url: https://blog.dreamfactory.com/
- group: docs
  title: ''
  type: Guide
  url: https://guide.dreamfactory.com/docs/
- group: company
  title: ''
  type: Partners
  url: https://www.dreamfactory.com/partners
- group: operate
  title: ''
  type: Support
  url: https://www.dreamfactory.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dreamfactory.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamfactory.com/privacy-policy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dreamfactory.com/llms.txt
created: '2025-06-05'
description: Automate the building, securing, and documenting of REST APIs for data products with built-in enterprise security on bare-metal, VMs, or containers.
features:
- name: Customer Hosted
- name: Application Migration
- name: API Publishing
- name: Admin Console
- name: Database API Generation
- name: Network API Generation
- name: Expert SQL Support
- name: Unlimited API Creation
- name: Unlimited API Volume
- name: Live API Docs
- name: Security
- name: Logging
- name: Reporting
- name: Role-Based Access Control (Rbac)
- name: API Key Management
- name: Service Side Scripting
- name: SOAP to REST
finops:
- name: Dreamfactory Finops
  service_category: API
  slug: dreamfactory-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dreamfactory.png
integrations:
- name: Alloydb
- name: Apache Hive
- name: AWS S3
- name: Azure Documentdb
- name: Azure Table Storage
- name: Azureblob
- name: Cassandra
- name: Cosmosdb
- name: Couchdb
- name: Databricks
- name: Dremio
- name: Dynamodb
- name: Firebird
- name: Ftp/Sftp
- name: Gridfs
- name: IBM DB2
- name: IBM Informix
- name: Local Storage
- name: Mariadb
- name: Mongodb
- name: Mysql
- name: Oracle
- name: Postgresql
- name: Rackspace Cloud Files
- name: Redshift
- name: Salesforce
- name: Sap SQL Anywhere
- name: Singlestore
- name: Snowflake
- name: SQL Server
- name: Sqlite
json_schemas:
- name: DreamFactory Admin
  property_count: 8
  slug: dreamfactory-admin
- name: DreamFactory App
  property_count: 9
  slug: dreamfactory-app
- name: DreamFactory Role
  property_count: 7
  slug: dreamfactory-role
- name: DreamFactory Service
  property_count: 9
  slug: dreamfactory-service
- name: DreamFactory User
  property_count: 9
  slug: dreamfactory-user
jsonld:
- class_count: 0
  name: Dreamfactory Context
  property_count: 5
  slug: dreamfactory-context
layout: provider
modified: '2026-05-19'
name: DreamFactory
nav: Providers
network: true
overview: 'DreamFactory publishes 16 APIs on the [APIs.io](https://apis.io/) network, including System API, Admin API, App API, and 13 more. Tagged areas include Automation, Deployment, Documentation, Generation, and Security.


  The DreamFactory catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  DreamFactory''s developer surface includes authentication, documentation, engineering blog, support, and 12 more developer resources.'
plans:
- name: Dreamfactory Plans Pricing
  plan_count: 3
  slug: dreamfactory-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Dreamfactory Rate Limits
  slug: dreamfactory-rate-limits
rules:
- name: DreamFactory API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: dreamfactory-asyncapi-spectral-rules
- name: DreamFactory API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dreamfactory-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.0
  delta: -4.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 80.5
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 36.8
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dreamfactory/refs/heads/main/screenshots/dreamfactory-2026-06-20T180322.png
security:
- kind: authentication
  name: Dreamfactory Authentication
  slug: dreamfactory-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Dreamfactory Domain Security
  slug: dreamfactory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dreamfactory
tags:
- Automation
- Deployment
- Documentation
- Generation
- Security
use_cases:
- name: API Generation
- name: API Management
- name: Api-First Development and Microservices
- name: Data Centralization
- name: Data Ingestion
- name: Data Integration and Migration
- name: Data Security
- name: Iot and Device Management
- name: Legacy System Modernization
- name: Microservices Architecture
- name: Mobile and Web App Development
- name: Restful API Access
- name: Secure Data Exchange
website: https://www.dreamfactory.com/
---

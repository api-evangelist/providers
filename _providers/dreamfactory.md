---
access_model:
  confidence: medium
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-04'
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
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: System administrator management
  name: DreamFactory Admin API
  slug: dreamfactory-admin-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Application and API key management
  name: DreamFactory App API
  slug: dreamfactory-app-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Application group management
  name: DreamFactory AppGroup API
  slug: dreamfactory-appgroup-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Cross-Origin Resource Sharing configuration
  name: DreamFactory CORS API
  slug: dreamfactory-cors-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Custom settings management
  name: DreamFactory Custom API
  slug: dreamfactory-custom-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Email template management
  name: DreamFactory EmailTemplate API
  slug: dreamfactory-emailtemplate-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Environment information
  name: DreamFactory Environment API
  slug: dreamfactory-environment-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Event management
  name: DreamFactory Event API
  slug: dreamfactory-event-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: API rate limiting management
  name: DreamFactory Limit API
  slug: dreamfactory-limit-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Lookup key management
  name: DreamFactory Lookup API
  slug: dreamfactory-lookup-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Package import and export
  name: DreamFactory Package API
  slug: dreamfactory-package-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Role-based access control management
  name: DreamFactory Role API
  slug: dreamfactory-role-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Script type discovery
  name: DreamFactory ScriptType API
  slug: dreamfactory-scripttype-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: Service type discovery
  name: DreamFactory ServiceType API
  slug: dreamfactory-servicetype-api
- baseURL: https://{instance}/api/v2/system
  baseurl_source: declared
  description: User management
  name: DreamFactory User API
  slug: dreamfactory-user-api
artifact_total: 109
asyncapis:
- description: Asynchronous event model for the DreamFactory System API. DreamFactory provides a comprehensive event scripting system that fires events before and after every API call, allowing server-side scripts (
  name: DreamFactory System API Events
  slug: dreamfactory-system-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DreamFactory System Admin API
  slug: open-dreamfactory-admin-api
- collection_type: open
  name: DreamFactory System Admin App API
  slug: open-dreamfactory-app-api
- collection_type: open
  name: DreamFactory System Admin AppGroup API
  slug: open-dreamfactory-appgroup-api
- collection_type: open
  name: DreamFactory System Admin CORS API
  slug: open-dreamfactory-cors-api
- collection_type: open
  name: DreamFactory System Admin Custom API
  slug: open-dreamfactory-custom-api
- collection_type: open
  name: DreamFactory System Admin EmailTemplate API
  slug: open-dreamfactory-emailtemplate-api
- collection_type: open
  name: DreamFactory System Admin Environment API
  slug: open-dreamfactory-environment-api
- collection_type: open
  name: DreamFactory System Admin Event API
  slug: open-dreamfactory-event-api
- collection_type: open
  name: DreamFactory System Admin Limit API
  slug: open-dreamfactory-limit-api
- collection_type: open
  name: DreamFactory System Admin Lookup API
  slug: open-dreamfactory-lookup-api
- collection_type: open
  name: DreamFactory System Admin Package API
  slug: open-dreamfactory-package-api
- collection_type: open
  name: DreamFactory System Admin Role API
  slug: open-dreamfactory-role-api
- collection_type: open
  name: DreamFactory System Admin ScriptType API
  slug: open-dreamfactory-scripttype-api
- collection_type: open
  name: DreamFactory System Admin ServiceType API
  slug: open-dreamfactory-servicetype-api
- collection_type: open
  name: DreamFactory Admin System API
  slug: open-dreamfactory-system-api
- collection_type: open
  name: DreamFactory System Admin User API
  slug: open-dreamfactory-user-api
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
random_paper: 0
rate_limits:
- limit_count: 5
  name: Dreamfactory Rate Limits
  slug: dreamfactory-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: DreamFactory API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: dreamfactory-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: DreamFactory API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dreamfactory-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 75.4
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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

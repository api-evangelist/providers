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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Snaplogic Agentic Access
  operation_count: 16
  slug: snaplogic-agentic-access
  summary_line: 16 operations · 9 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: SnapLogic API Management enables organizations to create, manage, secure, and monitor APIs throughout their lifecycle. It supports exposing SnapLogic pipelines as APIs or creating APIs from an OpenAPI
  name: SnapLogic API Management
  slug: snaplogic-api-management
- description: The SnapLogic Snap Development SDK provides a Java-based framework for building custom Snaps for the SnapLogic Intelligent Integration Platform. Snaps are streaming data processors that consume and pr
  name: SnapLogic Snap Development SDK
  slug: snaplogic-snap-development
- description: Our AI-powered, all-in-one generative integration platform unifies your data and streamlines workflows to transform your business.
  name: SnapLogic
  slug: snaplogic
- baseURL_template: https://{org}.snaplogic.com/api/1
  baseurl_source: spec_template
  description: Control project access, permissions, and asset management including project creation, renaming, deletion, and ACL management.
  name: SnapLogic Asset Management API
  slug: snaplogic-asset-management-api
- baseURL_template: https://{org}.snaplogic.com/api/1
  baseurl_source: spec_template
  description: Monitor and control pipeline execution state, performance metrics, and concurrent execution statistics.
  name: SnapLogic Runtime API
  slug: snaplogic-runtime-api
- baseURL_template: https://{org}.snaplogic.com/api/1
  baseurl_source: spec_template
  description: Enable, disable, and manage task configuration for triggered and scheduled pipeline tasks.
  name: SnapLogic Tasks API
  slug: snaplogic-tasks-api
- baseURL_template: https://{org}.snaplogic.com/api/1
  baseurl_source: spec_template
  description: Manage user accounts, groups, and membership for SnapLogic organizations.
  name: SnapLogic Users and Groups API
  slug: snaplogic-users-and-groups-api
artifact_total: 122
collections:
- collection_type: postman
  name: SnapLogic Public APIs Asset Management API
  slug: postman-snaplogic-asset-management-api
- collection_type: postman
  name: SnapLogic Public APIs Asset Management Runtime API
  slug: postman-snaplogic-runtime-api
- collection_type: postman
  name: SnapLogic Public APIs Asset Management Tasks API
  slug: postman-snaplogic-tasks-api
- collection_type: postman
  name: SnapLogic Public APIs Asset Management Users and Groups API
  slug: postman-snaplogic-users-and-groups-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SnapLogic Public APIs Asset Management API
  slug: open-snaplogic-asset-management-api
- collection_type: open
  name: SnapLogic Public APIs
  slug: open-snaplogic-public-apis
- collection_type: open
  name: SnapLogic Public APIs Asset Management Runtime API
  slug: open-snaplogic-runtime-api
- collection_type: open
  name: SnapLogic Public APIs Asset Management Tasks API
  slug: open-snaplogic-tasks-api
- collection_type: open
  name: SnapLogic Public APIs Asset Management Users and Groups API
  slug: open-snaplogic-users-and-groups-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/snaplogic/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snaplogic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snaplogic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snaplogic-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs-snaplogic.atlassian.net/wiki/spaces/SD/overview
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snaplogic/
- group: company
  title: ''
  type: Website
  url: https://www.snaplogic.com/
- group: start
  title: ''
  type: RequestDemo
  url: https://www.snaplogic.com/request-demo
- group: company
  title: ''
  type: Partners
  url: https://www.snaplogic.com/partners
- group: other
  title: ''
  type: Customers
  url: https://www.snaplogic.com/customers
- group: company
  title: ''
  type: Blog
  url: https://www.snaplogic.com/blog
- group: other
  title: ''
  type: eBooks
  url: https://www.snaplogic.com/resources?_resource_type=ebook
- group: other
  title: ''
  type: Podcast
  url: https://www.snaplogic.com/resources/podcasts
- group: learn
  title: ''
  type: Webinars
  url: https://www.snaplogic.com/resources/events
- group: learn
  title: ''
  type: Training
  url: https://www.snaplogic.com/resources/events/customer-workshops
- group: start
  title: ''
  type: Login
  url: https://cdn.elastic.snaplogic.com/sl/login.html?referrer=https://www.snaplogic.com/
- group: start
  title: ''
  type: RequestDemo
  url: https://www.snaplogic.com/request-demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.snaplogic.com/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.snaplogic.com/security-standards
- group: other
  title: ''
  type: Glossary
  url: https://www.snaplogic.com/glossary
- group: operate
  title: ''
  type: Support
  url: https://www.snaplogic.com/getting-help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.snaplogic.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.snaplogic.com/terms-of-use
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snaplogic.com/public-apis/public-apis-about.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snaplogic.com/
- group: operate
  title: ''
  type: Forums
  url: https://community.snaplogic.com
- group: start
  title: ''
  type: GettingStarted
  url: https://community.snaplogic.com/t5/getting-started/bd-p/getting_started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.snaplogic.com/introduction/release-process.html
- group: learn
  title: ''
  type: Training
  url: https://learn.snaplogic.com/
- group: auth
  title: ''
  type: Certification
  url: https://www.snaplogic.com/resources/snaplogic-academy
- group: docs
  title: ''
  type: Documentation
  url: https://developer.snaplogic.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SnapLogic
- group: company
  title: ''
  type: About
  url: https://www.snaplogic.com/company
- group: company
  title: ''
  type: Careers
  url: https://www.snaplogic.com/company/careers
- group: company
  title: ''
  type: News
  url: https://www.snaplogic.com/company/newsroom
- group: operate
  title: ''
  type: PressReleases
  url: https://www.snaplogic.com/company/newsroom/press-releases
- group: operate
  title: ''
  type: Contact
  url: https://www.snaplogic.com/contact-us
- group: other
  title: ''
  type: X
  url: https://x.com/SnapLogic
- group: other
  title: ''
  type: APIManagement
  url: https://www.snaplogic.com/products/api-management-development
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snaplogic.com/manager/view-pipeline-apis.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snaplogic.com/cicd/git-integration/git-integration-about.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snaplogic.com/monitor/observe-api-metrics.html
created: '2025-06-06T00:00:00.000Z'
description: Our AI-powered, all-in-one generative integration platform unifies your data and streamlines workflows to transform your business.
examples:
- key_count: 4
  name: Snaplogic List Pipeline Executions Example
  slug: snaplogic-list-pipeline-executions-example
finops:
- name: Snaplogic Finops
  service_category: Integration Platform
  slug: snaplogic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snaplogic.png
json_schemas:
- name: SnapLogic Pipeline Execution
  property_count: 11
  slug: snaplogic-pipeline-execution
json_structures:
- name: Snaplogic Platform Structure
  property_count: 0
  slug: snaplogic-platform-structure
jsonld:
- class_count: 6
  name: Snaplogic Context
  property_count: 27
  slug: snaplogic-context
layout: provider
modified: '2026-05-19'
name: SnapLogic
nav: Providers
network: true
overview: 'SnapLogic publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Asset Management API, Runtime API, Tasks API, and 1 more. Tagged areas include Artificial Intelligence, API Management, Automation, Data Integration, and Integration.


  The SnapLogic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SnapLogic''s developer surface includes authentication, documentation, engineering blog, training material, pricing, support, getting-started guide, and 35 more developer resources.'
plans:
- name: Snaplogic Plans Pricing
  plan_count: 1
  slug: snaplogic-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Snaplogic Rate Limits
  slug: snaplogic-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SnapLogic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: snaplogic-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: SnapLogic API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: snaplogic-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 13.6
    contract_quality: 65.6
    developer_ergonomics: 41.7
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 36.8
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snaplogic/refs/heads/main/screenshots/snaplogic-2026-06-20T194106.png
security:
- kind: authentication
  name: Snaplogic Authentication
  slug: snaplogic-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Snaplogic Domain Security
  slug: snaplogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snaplogic
tags:
- Artificial Intelligence
- API Management
- Automation
- Data Integration
- Integration
- iPaaS
- Management
use_cases:
- name: Active Directory
- name: AlloyDB
- name: Amazon Athena
- name: Amazon DynamoDB
- name: Amazon Redshift
- name: Amazon S3
- name: Amazon SNS
- name: Amazon SQS
- name: Anaplan
- name: Apache Kafka
- name: API Suite
- name: Azure Active Directory
- name: Azure Service Bus
- name: Azure SQL
- name: Azure Synapse SQL
- name: Binary
- name: Box
- name: Cassandra
- name: Coupa
- name: Data Catalog
- name: Databricks
- name: Email
- name: Exact Online
- name: Expensify
- name: Flow
- name: Google Analytics 4
- name: Google BigQuery Snaps
- name: Google Cloud Pub/Sub
- name: Google Directory Snaps
- name: Google Sheets
- name: Hadoop
- name: Hive
- name: HubSpot
- name: Infor Birst
- name: JDBC
- name: JIRA Snap
- name: JMS
- name: JSON Web Token
- name: LDAP
- name: Marketo
- name: Metadata
- name: Microsoft Dynamics 365 Business Central
- name: Microsoft Dynamics 365 Finance and SCM
- name: Microsoft Dynamics 365 for Sales
- name: Microsoft Dynamics AX
- name: Microsoft Exchange Online
- name: Microsoft OneDrive
- name: Microsoft Power BI
- name: Microsoft SharePoint
- name: Microsoft Teams
- name: ML Analytics
- name: ML Data Preparation
- name: MongoDB
- name: MQTT
- name: MySQL Snap
- name: Natural Language Processing
- name: NetSuite OpenAir
- name: NetSuite
- name: OPC UA
- name: OpenAPI
- name: Oracle CDC
- name: Oracle Eloqua
- name: Oracle HCM
- name: Oracle
- name: PDF
- name: PLM TC
- name: PostgreSQL
- name: RabbitMQ
- name: Reltio
- name: REST
- name: Salesforce
- name: SAP S/4HANA Cloud
- name: SAP S/4HANA
- name: SAP Snap
- name: SAP SuccessFactors
- name: Script
- name: ServiceNow Snap
- name: Shopify
- name: Snowflake
- name: SOAP
- name: Splunk
- name: SQL Server
- name: Sumo Logic
- name: Syndigo
- name: Tableau
- name: Teradata
- name: Transform
- name: Twilio
- name: Vertica
- name: Workday Prism Snap
- name: Workday
- name: Xactly
- name: Zuora Snap
website: https://www.snaplogic.com/
---

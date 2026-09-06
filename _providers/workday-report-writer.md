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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Workday Report Writer Agentic Access
  operation_count: 19
  slug: workday-report-writer-agentic-access
  summary_line: 19 operations · 5 acting
api_count: 4
apis:
- description: SOAP web service API for creating, managing, and executing custom reports in Workday using Report Writer functionality. Provides programmatic access to report definitions, calculated fields, and repor
  name: Workday Report Writer API
  slug: workday-report-writer-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: To view and maintain Agent Definitions with the Agent System of Record.
  name: Workday Report Writer agentDefinition API
  slug: workday-report-writer-agentdefinition-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage file upload buckets for staging compressed data files before executing data change tasks against tables
  name: Workday Report Writer Buckets API
  slug: workday-report-writer-buckets-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Execute custom reports exposed as web service endpoints, returning data in multiple formats including JSON, CSV, and XML
  name: Workday Report Writer Custom Reports API
  slug: workday-report-writer-custom-reports-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Execute data change tasks to load, update, or delete data in Prism Analytics tables using files uploaded to buckets
  name: Workday Report Writer Data Change Tasks API
  slug: workday-report-writer-data-change-tasks-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Discover available data sources (tables) that can be queried using WQL, including their fields and filter definitions
  name: Workday Report Writer Data Sources API
  slug: workday-report-writer-data-sources-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Manage Prism Analytics datasets, which are read-only data collections used in Prism reports and dashboards
  name: Workday Report Writer Datasets API
  slug: workday-report-writer-datasets-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Execute WQL queries against Workday data sources and retrieve paginated results
  name: Workday Report Writer Query Execution API
  slug: workday-report-writer-query-execution-api
- baseURL: https://wd2-impl-services1.workday.com/ccx/service
  baseurl_source: declared
  description: Create and manage Prism Analytics tables that define the schema for external data loaded into Workday for reporting and analytics
  name: Workday Report Writer Tables API
  slug: workday-report-writer-tables-api
artifact_total: 60
collections:
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets agentDefinition API
  slug: postman-workday-report-writer-agentdefinition-api
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets API
  slug: postman-workday-report-writer-buckets-api
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets Custom Reports API
  slug: postman-workday-report-writer-custom-reports-api
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets Data Change Tasks API
  slug: postman-workday-report-writer-data-change-tasks-api
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets Data Sources API
  slug: postman-workday-report-writer-data-sources-api
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets Datasets API
  slug: postman-workday-report-writer-datasets-api
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets Query Execution API
  slug: postman-workday-report-writer-query-execution-api
- collection_type: postman
  name: Workday Report Writer Workday Prism Analytics Buckets Tables API
  slug: postman-workday-report-writer-tables-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets agentDefinition API
  slug: open-workday-report-writer-agentdefinition-api
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets API
  slug: open-workday-report-writer-buckets-api
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets Custom Reports API
  slug: open-workday-report-writer-custom-reports-api
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets Data Change Tasks API
  slug: open-workday-report-writer-data-change-tasks-api
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets Data Sources API
  slug: open-workday-report-writer-data-sources-api
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets Datasets API
  slug: open-workday-report-writer-datasets-api
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics API
  slug: open-workday-report-writer-prism-analytics
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets Query Execution API
  slug: open-workday-report-writer-query-execution-api
- collection_type: open
  name: Workday Report Writer Workday Report-as-a-Service (RaaS) REST API
  slug: open-workday-report-writer-raas
- collection_type: open
  name: Workday Report Writer Workday Prism Analytics Buckets Tables API
  slug: open-workday-report-writer-tables-api
- collection_type: open
  name: Workday Report Writer Workday WQL API
  slug: open-workday-report-writer-wql
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Workday/raas-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Workday/raas-python/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Workday/raas-python/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Workday/raas-python/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-report-writer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-report-writer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-report-writer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-report-writer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-report-writer-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.workday.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/KfHiRHLBJB0O63TxIyZCFA
- group: docs
  title: ''
  type: Documentation
  url: https://community.workday.com/api
- group: auth
  title: ''
  type: Authentication
  url: https://doc.workday.com/admin-guide/en-us/workday-api/authentication/index.html
- group: start
  title: ''
  type: Sandbox
  url: https://community.workday.com/articles/6394
- group: other
  title: ''
  type: Hub
  url: https://community.workday.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/a3a_TL5Tde61ZFJKLtycjg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://community.workday.com/trust/status
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/services/support.html
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/technology.html
- group: start
  title: ''
  type: Signup
  url: https://resourcecenter.workday.com/
- group: start
  title: ''
  type: Console
  url: https://developer.workday.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: docs
  title: ''
  type: APIReference
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
created: '2024-01-01'
description: APIs for Workday Report Writer - a tool for creating custom reports and data extracts from Workday HCM and Financial systems.
features:
- description: Build custom reports using Report Writer with calculated fields, subfilters, and grouping across HCM and Financial Management data.
  name: Custom Report Authoring
- description: Expose any advanced custom report as a REST or SOAP web service returning JSON, CSV, XML, or RSS for programmatic consumption.
  name: Report-as-a-Service Web Endpoints
- description: Query Workday data with SQL-like SELECT/FROM/WHERE/ORDER BY/LIMIT syntax against governed data sources for high-performance retrieval.
  name: SQL-Like Data Access via WQL
- description: Programmatically create tables, upload compressed files via buckets, and run data change tasks (insert, update, upsert, delete) in Prism.
  name: External Data Loading with Prism Analytics
- description: Secure access to REST endpoints using OAuth 2.0 client credentials, refresh tokens, and bearer tokens managed through API client setup.
  name: OAuth 2.0 Authentication
- description: Retrieve report data in JSON, CSV, XML, RSS, and other formats with query parameter control over filtering, prompts, and pagination.
  name: Multi-Format Output
finops:
- name: Workday Report Writer Finops
  service_category: Reporting / Analytics
  slug: workday-report-writer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-report-writer.png
integrations:
- description: Land Workday RaaS and WQL extracts into Snowflake stages for use in enterprise data warehouse pipelines.
  name: Snowflake
- description: Ingest Workday report data into Databricks for analytics, ML feature engineering, and lakehouse modeling.
  name: Databricks
- description: Connect Tableau to RaaS endpoints or downstream warehouses to build interactive dashboards on Workday HCM and financial data.
  name: Tableau
- description: Use RaaS JSON or CSV outputs as data sources for Microsoft Power BI reports and semantic models.
  name: Power BI
- description: Orchestrate Workday API calls in iPaaS workflows that move data between Workday and third-party SaaS applications.
  name: Workato
- description: Build integration pipelines using SnapLogic's Workday Snap Pack to read RaaS, WQL, and Prism endpoints.
  name: SnapLogic
- description: Connect Workday APIs to ERP, CRM, and HRIS systems through Boomi AtomSphere integration processes.
  name: Boomi
json_schemas:
- name: Workday Prism Analytics Table Schema
  property_count: 1
  slug: workday-report-writer-prism-table
layout: provider
modified: '2026-05-19'
name: Workday Report Writer
nav: Providers
network: true
overview: 'Workday Report Writer publishes 8 APIs on the [APIs.io](https://apis.io/) network, including agentDefinition API, Buckets API, Custom Reports API, and 5 more. Tagged areas include Analytics, Enterprise, ERP, Financials, and HRMS.


  The Workday Report Writer catalog on APIs.io includes 1 Spectral governance ruleset.


  Workday Report Writer''s developer surface includes authentication, developer portal, getting-started guide, documentation, sandbox, support, engineering blog, and 18 more developer resources.'
plans:
- name: Workday Report Writer Plans Pricing
  plan_count: 1
  slug: workday-report-writer-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Workday Report Writer Rate Limits
  slug: workday-report-writer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Workday Report Writer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-report-writer-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 9.8
    contract_quality: 60.0
    developer_ergonomics: 56.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 50.0
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-report-writer/refs/heads/main/screenshots/workday-report-writer-2026-06-20T201608.png
security:
- kind: authentication
  name: Workday Report Writer Authentication
  slug: workday-report-writer-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Workday Report Writer Domain Security
  slug: workday-report-writer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Report Writer Trust Center
  slug: workday-report-writer-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-report-writer
solutions:
- description: End-to-end workforce and people analytics built on Report Writer, RaaS, and WQL across the Workday HCM suite.
  name: HCM Reporting
- description: Custom financial reporting and extracts spanning ledgers, projects, procurement, and revenue across Workday Financial Management.
  name: Financial Management Reporting
- description: Bring external data into Workday and combine with native data sets to deliver advanced analytics and self-service reporting.
  name: Prism Analytics
tags:
- Analytics
- Enterprise
- ERP
- Financials
- HRMS
- Reporting
- Software-as-a-Service
use_cases:
- description: Extract headcount, compensation, and turnover metrics from Workday HCM for downstream analytics, dashboards, and board reporting.
  name: HR Analytics and Workforce Reporting
- description: Pull custom financial reports for general ledger, accounts payable, and budget variance analysis in support of period close processes.
  name: Financial Reporting and Close
- description: Schedule RaaS or WQL extracts to feed Snowflake, BigQuery, Redshift, Databricks, or other downstream systems with Workday data.
  name: Data Warehouse and Lake Hydration
- description: Load external CSV or Parquet datasets into Prism Analytics tables to combine with native Workday data for cross-source reporting.
  name: External Data Blending in Prism
- description: Drive payroll vendors, benefits providers, and identity systems with scheduled report extracts derived from Workday source-of-truth data.
  name: Operational Integrations
- description: Generate audit-ready extracts of personnel actions, journal entries, and security configurations for regulatory and SOX compliance.
  name: Compliance and Audit Reporting
website: https://developer.workday.com/about
---

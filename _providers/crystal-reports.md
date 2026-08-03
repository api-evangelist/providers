---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Crystal Reports Agentic Access
  operation_count: 20
  slug: crystal-reports-agentic-access
  summary_line: 20 operations · 3 acting
api_count: 9
apis:
- description: Software Development Kit for embedding Crystal Reports into applications.
  name: Crystal Reports SDK
  slug: sdk
- description: API for Crystal Reports Server administration and report management.
  name: Crystal Reports Server REST API
  slug: server-rest-api
- description: Logon and session management
  name: Crystal Reports Authentication API
  slug: crystal-reports-authentication-api
- description: Report export to various formats
  name: Crystal Reports Export API
  slug: crystal-reports-export-api
- description: Transient report instance management
  name: Crystal Reports Instances API
  slug: crystal-reports-instances-api
- description: Report structure and metadata
  name: Crystal Reports Metadata API
  slug: crystal-reports-metadata-api
- description: OData data service for report row and summary data
  name: Crystal Reports OData API
  slug: crystal-reports-odata-api
- description: Report summary and URI information
  name: Crystal Reports Reports API
  slug: crystal-reports-reports-api
- description: Infostore repository navigation and folder browsing
  name: Crystal Reports Repository API
  slug: crystal-reports-repository-api
artifact_total: 107
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crystal-reports-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crystal-reports-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crystal-reports-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crystal-reports-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://api.sap.com
- group: company
  title: ''
  type: Blog
  url: https://blogs.sap.com/tags/73554900100800000134/
- group: operate
  title: ''
  type: Community
  url: https://community.sap.com/topics/crystal-reports
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com/crystal-reports
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
created: '2024-01-01'
description: APIs and resources for Crystal Reports, a business intelligence application for designing and generating reports from various data sources.
examples:
- key_count: 4
  name: Crystal Reports Connection Info Example
  slug: crystal-reports-connection-info-example
- key_count: 3
  name: Crystal Reports Data Source Example
  slug: crystal-reports-data-source-example
- key_count: 2
  name: Crystal Reports Error Example
  slug: crystal-reports-error-example
- key_count: 2
  name: Crystal Reports File Format Version Example
  slug: crystal-reports-file-format-version-example
- key_count: 2
  name: Crystal Reports Formula Example
  slug: crystal-reports-formula-example
- key_count: 1
  name: Crystal Reports Grand Total Collection Example
  slug: crystal-reports-grand-total-collection-example
- key_count: 2
  name: Crystal Reports Group Condition Example
  slug: crystal-reports-group-condition-example
- key_count: 6
  name: Crystal Reports Infostore Entry Example
  slug: crystal-reports-infostore-entry-example
- key_count: 1
  name: Crystal Reports Infostore Entry List Example
  slug: crystal-reports-infostore-entry-list-example
- key_count: 2
  name: Crystal Reports Instance Form Example
  slug: crystal-reports-instance-form-example
- key_count: 3
  name: Crystal Reports Logon Request Example
  slug: crystal-reports-logon-request-example
- key_count: 1
  name: Crystal Reports Logon Response Example
  slug: crystal-reports-logon-response-example
- key_count: 2
  name: Crystal Reports O Data Field Value Example
  slug: crystal-reports-o-data-field-value-example
- key_count: 3
  name: Crystal Reports O Data Row Collection Example
  slug: crystal-reports-o-data-row-collection-example
- key_count: 1
  name: Crystal Reports O Data Service Document Example
  slug: crystal-reports-o-data-service-document-example
- key_count: 3
  name: Crystal Reports Report Instance Example
  slug: crystal-reports-report-instance-example
- key_count: 5
  name: Crystal Reports Report Parameter Example
  slug: crystal-reports-report-parameter-example
- key_count: 8
  name: Crystal Reports Report Structure Example
  slug: crystal-reports-report-structure-example
- key_count: 10
  name: Crystal Reports Report Summary Example
  slug: crystal-reports-report-summary-example
- key_count: 4
  name: Crystal Reports Running Total Example
  slug: crystal-reports-running-total-example
- key_count: 2
  name: Crystal Reports Subreport Example
  slug: crystal-reports-subreport-example
- key_count: 3
  name: Crystal Reports Summary Field Example
  slug: crystal-reports-summary-field-example
- key_count: 3
  name: Crystal Reports Used Field Example
  slug: crystal-reports-used-field-example
features:
- description: Generate formatted reports from relational databases, spreadsheets, and XML data sources.
  name: Report Generation
- description: Embed report viewers in web and desktop applications for interactive report consumption.
  name: Report Viewing
- description: Schedule automated report generation and delivery via email or file system.
  name: Report Scheduling
- description: Pass dynamic parameters to filter and customize report content at runtime.
  name: Parameter Prompts
- description: Export reports to PDF, Excel, Word, CSV, XML, and other formats programmatically.
  name: Export Formats
- description: Embed linked sub-reports within parent reports for drill-down capabilities.
  name: Sub-Reports
- description: Generate pivot-table style cross-tabulation reports from data.
  name: Cross-Tab Reports
- description: Create charts and graphs within reports for data visualization.
  name: Charting
- description: Connect to SQL Server, Oracle, SAP HANA, ODBC, JDBC, and other data sources.
  name: Data Source Connectivity
- description: Manage report server instances, folders, users, and security via REST API.
  name: Report Server Management
finops:
- name: Crystal Reports Finops
  service_category: Business Intelligence
  slug: crystal-reports-finops
image: /assets/icons/crystal-reports.png
json_schemas:
- name: ConnectionInfo
  property_count: 4
  slug: crystal-reports-connection-info
- name: DataSource
  property_count: 3
  slug: crystal-reports-data-source
- name: Error
  property_count: 2
  slug: crystal-reports-error
- name: FileFormatVersion
  property_count: 2
  slug: crystal-reports-file-format-version
- name: Formula
  property_count: 2
  slug: crystal-reports-formula
- name: GrandTotalCollection
  property_count: 1
  slug: crystal-reports-grand-total-collection
- name: GroupCondition
  property_count: 2
  slug: crystal-reports-group-condition
- name: InfostoreEntryList
  property_count: 1
  slug: crystal-reports-infostore-entry-list
- name: InfostoreEntry
  property_count: 6
  slug: crystal-reports-infostore-entry
- name: InstanceForm
  property_count: 2
  slug: crystal-reports-instance-form
- name: LogonRequest
  property_count: 3
  slug: crystal-reports-logon-request
- name: LogonResponse
  property_count: 1
  slug: crystal-reports-logon-response
- name: ODataFieldValue
  property_count: 2
  slug: crystal-reports-o-data-field-value
- name: ODataRowCollection
  property_count: 3
  slug: crystal-reports-o-data-row-collection
- name: ODataServiceDocument
  property_count: 1
  slug: crystal-reports-o-data-service-document
- name: ReportInstance
  property_count: 3
  slug: crystal-reports-report-instance
- name: ReportParameter
  property_count: 5
  slug: crystal-reports-report-parameter
- name: ReportStructure
  property_count: 8
  slug: crystal-reports-report-structure
- name: ReportSummary
  property_count: 11
  slug: crystal-reports-report-summary
- name: RunningTotal
  property_count: 4
  slug: crystal-reports-running-total
- name: Subreport
  property_count: 2
  slug: crystal-reports-subreport
- name: SummaryField
  property_count: 3
  slug: crystal-reports-summary-field
- name: UsedField
  property_count: 3
  slug: crystal-reports-used-field
json_structures:
- name: Crystal Reports Connection Info Structure
  property_count: 4
  slug: crystal-reports-connection-info-structure
- name: Crystal Reports Data Source Structure
  property_count: 3
  slug: crystal-reports-data-source-structure
- name: Crystal Reports Error Structure
  property_count: 2
  slug: crystal-reports-error-structure
- name: Crystal Reports File Format Version Structure
  property_count: 2
  slug: crystal-reports-file-format-version-structure
- name: Crystal Reports Formula Structure
  property_count: 2
  slug: crystal-reports-formula-structure
- name: Crystal Reports Grand Total Collection Structure
  property_count: 1
  slug: crystal-reports-grand-total-collection-structure
- name: Crystal Reports Group Condition Structure
  property_count: 2
  slug: crystal-reports-group-condition-structure
- name: Crystal Reports Infostore Entry List Structure
  property_count: 1
  slug: crystal-reports-infostore-entry-list-structure
- name: Crystal Reports Infostore Entry Structure
  property_count: 6
  slug: crystal-reports-infostore-entry-structure
- name: Crystal Reports Instance Form Structure
  property_count: 2
  slug: crystal-reports-instance-form-structure
- name: Crystal Reports Logon Request Structure
  property_count: 3
  slug: crystal-reports-logon-request-structure
- name: Crystal Reports Logon Response Structure
  property_count: 1
  slug: crystal-reports-logon-response-structure
- name: Crystal Reports O Data Field Value Structure
  property_count: 2
  slug: crystal-reports-o-data-field-value-structure
- name: Crystal Reports O Data Row Collection Structure
  property_count: 3
  slug: crystal-reports-o-data-row-collection-structure
- name: Crystal Reports O Data Service Document Structure
  property_count: 1
  slug: crystal-reports-o-data-service-document-structure
- name: Crystal Reports Report Instance Structure
  property_count: 3
  slug: crystal-reports-report-instance-structure
- name: Crystal Reports Report Parameter Structure
  property_count: 5
  slug: crystal-reports-report-parameter-structure
- name: Crystal Reports Report Structure Structure
  property_count: 8
  slug: crystal-reports-report-structure-structure
- name: Crystal Reports Report Summary Structure
  property_count: 11
  slug: crystal-reports-report-summary-structure
- name: Crystal Reports Running Total Structure
  property_count: 4
  slug: crystal-reports-running-total-structure
- name: Crystal Reports Subreport Structure
  property_count: 2
  slug: crystal-reports-subreport-structure
- name: Crystal Reports Summary Field Structure
  property_count: 3
  slug: crystal-reports-summary-field-structure
- name: Crystal Reports Used Field Structure
  property_count: 3
  slug: crystal-reports-used-field-structure
jsonld:
- class_count: 22
  name: Crystal Reports Context
  property_count: 54
  slug: crystal-reports-context
layout: provider
modified: '2026-05-19'
name: Crystal Reports
nav: Providers
network: true
overview: 'Crystal Reports publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Export API, Instances API, and 4 more. Tagged areas include Business Intelligence, Crystal Reports, Data Analytics, Enterprise Software, and Reporting.


  The Crystal Reports catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Crystal Reports'' developer surface includes authentication, developer portal, engineering blog, support, and 6 more developer resources.'
plans:
- name: Crystal Reports Plans Pricing
  plan_count: 2
  slug: crystal-reports-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 2
  name: Crystal Reports Rate Limits
  slug: crystal-reports-rate-limits
rules:
- name: Crystal Reports API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: crystal-reports-jsonschema-spectral-rules
- name: Crystal Reports API Rules
  rule_count: 22
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 6
  slug: crystal-reports-spectral-rules
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 23.7
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crystal-reports/refs/heads/main/screenshots/crystal-reports-2026-06-20T175319.png
security:
- kind: authentication
  name: Crystal Reports Authentication
  slug: crystal-reports-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Crystal Reports Domain Security
  slug: crystal-reports-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crystal Reports Vulnerability Disclosure
  slug: crystal-reports-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crystal-reports
solutions:
- description: Desktop report designer for creating and editing report templates.
  name: SAP Crystal Reports
- description: Server platform for scheduling, managing, and distributing reports.
  name: SAP Crystal Reports Server
- description: Enterprise BI platform with Crystal Reports integration.
  name: SAP BusinessObjects BI
tags:
- Business Intelligence
- Crystal Reports
- Data Analytics
- Enterprise Software
- Reporting
- SAP
use_cases:
- description: Generate financial statements, balance sheets, and P&L reports from ERP data.
  name: Financial Reporting
- description: Create operational reports for manufacturing, logistics, and supply chain.
  name: Operational Dashboards
- description: Generate regulatory compliance reports for auditing and governance.
  name: Compliance Reports
- description: Produce formatted invoices and statements from billing data.
  name: Customer Invoicing
- description: Generate employee reports, headcount analytics, and compensation summaries.
  name: HR Analytics
- description: Embed Crystal Reports viewer into custom applications for end-user reporting.
  name: Embedded Reporting
website: https://api.sap.com
---

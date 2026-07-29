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
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cdata Agentic Access
  operation_count: 7
  slug: cdata-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 11
apis:
- description: The CData Cloud SQL API provides HTTP-based access to execute SQL queries, batch operations, and stored procedures across all data sources configured in a CData Connect Cloud account. Real-time data a
  name: CData SQL API
  slug: sql-api
- description: The CData Cloud Metadata API exposes catalog information including schemas, tables, columns, keys, and stored procedures across every configured data source, enabling tools to introspect the connected
  name: CData Metadata API
  slug: metadata-api
- description: The CData Cloud Log API retrieves operational logs for queries, jobs, and connection events, enabling observability of the CData Connect Cloud service.
  name: CData Log API
  slug: log-api
- description: The CData Cloud Connection API manages data source connections programmatically, allowing administrators to create, update, test, and delete connections to databases and SaaS applications.
  name: CData Connection API
  slug: connection-api
- description: The CData Cloud Job API monitors background jobs such as replication, caching, and scheduled operations, exposing job state and history.
  name: CData Job API
  slug: job-api
- description: The CData Cloud Account API manages account settings, workspaces, and user-level configuration for the CData Connect Cloud tenant.
  name: CData Account API
  slug: account-api
- description: The CData Cloud Audit API tracks system activities and administrative events, supporting compliance and security monitoring requirements such as SOC 2 and GDPR.
  name: CData Audit API
  slug: audit-api
- description: CData Connect Cloud exposes an OData v4 compatible API that allows any OData client to browse metadata and query data from any configured source, including Excel, Power BI, and other BI tools.
  name: CData OData API
  slug: odata-api
- description: Catalog/metadata exploration
  name: CData Metadata API
  slug: cdata-metadata-api
- description: Execute stored procedures
  name: CData Procedures API
  slug: cdata-procedures-api
- description: Execute SQL queries and batch operations
  name: CData Query API
  slug: cdata-query-api
artifact_total: 310
collections:
- collection_type: open
  name: CData Connect Cloud SQL API
  slug: open-cdata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cdata-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cdata-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cdata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cdata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cdatasoftware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdatasoftware
- group: company
  title: ''
  type: About
  url: https://www.cdata.com/company/
- group: company
  title: ''
  type: Partners
  url: https://www.cdata.com/embedded/customers/
- group: other
  title: ''
  type: Testimonials
  url: https://www.cdata.com/company/testimonials.aspx
- group: other
  title: ''
  type: CaseStudies
  url: https://www.cdata.com/case-study/
- group: operate
  title: ''
  type: Support
  url: https://www.cdata.com/support/
- group: other
  title: ''
  type: Knowledgebase
  url: https://www.cdata.com/kb/
- group: company
  title: ''
  type: Blog
  url: https://www.cdata.com/blog/
- group: other
  title: ''
  type: WhitePapers
  url: https://www.cdata.com/resources/
- group: learn
  title: ''
  type: Webinars
  url: https://www.cdata.com/resources/
- group: other
  title: ''
  type: Events
  url: https://www.cdata.com/events/
- group: start
  title: ''
  type: Portal
  url: https://www.cdata.com/developers/
- group: other
  title: ''
  type: Glossary
  url: https://www.cdata.com/glossary/
- group: learn
  title: ''
  type: Videos
  url: https://www.cdata.com/kb/video/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.cdata.com/company/press.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cdata.com/company/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cdata.com/company/legal/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.cdata.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cdata.com/security/
- group: other
  title: ''
  type: AWSMarketplace
  url: https://aws.amazon.com/marketplace/pp/prodview-jizwvan7n7sn6
created: '2025-06-05'
description: CData Software is a leading provider of data access and connectivity solutions. Our standards-based connectors streamline data access and insulate customers from the complexities of integrating with on-premise or cloud databases, SaaS, APIs, NoSQL, and Big Data.
features:
- name: SQL
- name: ODBC
- name: JDBC
- name: ADO.NET
- name: Excel
- name: SSIS
- name: EDI
- name: FTP
- name: X12
- name: EDIFact
- name: HL7 FHIR
- name: CSV
- name: XML
- name: ETL
- name: ELT
- name: SOC
- name: SOC2
- name: GDPR
- name: Data Quality
- name: Data Security
- name: Data Compliance
- name: Data Transformation
- name: SQL Normalization
- name: Metadata Caching
- name: Data Modeling
- name: Data Governance
- name: Data Replication
- name: Data Backups
- name: API Server
- name: Embedded Integrations
- name: Streaming
- name: Kafka
- name: Data Lakehouse
- name: Data Warehouse
- name: Security
- name: Authentication
- name: Hybrid-Cloud
- name: Multi-Cloud
- name: Semantic Layer
- name: Analytical Queries
- name: Data Intensive Workloads
- name: No-Code
- name: Low-Code
- name: Virtual Datasets
- name: Dashboards
- name: Reports
- name: Insights
- name: Intelligence
- name: Automation
- name: Webhooks
finops:
- name: Cdata Finops
  service_category: API
  slug: cdata-finops
graphqls:
- description: ''
  name: CData GraphQL API
  slug: cdata-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdata.png
integrations:
- name: Access
- name: Act CRM
- name: Act-On
- name: Active Directory
- name: ActiveCampaign
- name: Acumatica
- name: Adobe Analytics
- name: Adobe Commerce
- name: ADP
- name: Airtable
- name: AlloyDB
- name: Amazon Athena
- name: Amazon DynamoDB
- name: Amazon Marketplace
- name: Amazon S3
- name: Asana
- name: Authorize.Net
- name: Avalara AvaTax
- name: Avro
- name: Azure Active Directory
- name: Azure Analysis Services
- name: Azure Data Catalog
- name: Azure Data Lake Storage
- name: Azure DevOps
- name: Azure Synapse
- name: Azure Table
- name: Basecamp
- name: BigCommerce
- name: BigQuery
- name: Bing Ads
- name: Bing Search
- name: Bitbucket
- name: Blackbaud FE NXT
- name: Box
- name: Bullhorn CRM
- name: Cassandra
- name: Certinia
- name: Cloudant
- name: CockroachDB
- name: Confluence
- name: Cosmos DB
- name: Couchbase
- name: CouchDB
- name: CSV
- name: Cvent
- name: Databricks
- name: DB2
- name: DocuSign
- name: Dropbox
- name: Dynamics 365
- name: Dynamics 365 Business Central
- name: Dynamics CRM
- name: Dynamics GP
- name: Dynamics NAV
- name: eBay
- name: eBay Analytics
- name: Elasticsearch
- name: Email
- name: EnterpriseDB
- name: Epicor Kinetic
- name: Exact Online
- name: Excel
- name: Excel Online
- name: Facebook
- name: Facebook Ads
- name: FHIR
- name: Freshdesk
- name: FTP
- name: GitHub
- name: Gmail
- name: Google Ad Manager
- name: Google Ads
- name: Google Analytics
- name: Google Calendar
- name: Google Campaign Manager 360
- name: Google Cloud Storage
- name: Google Contacts
- name: Google Data Catalog
- name: Google Directory
- name: Google Drive
- name: Google Search
- name: Google Sheets
- name: Google Spanner
- name: GraphQL
- name: Greenhouse
- name: Greenplum
- name: HarperDB
- name: HBase
- name: HCL Domino
- name: HDFS
- name: Highrise
- name: Hive
- name: HubDB
- name: HubSpot
- name: IBM Cloud Data Engine
- name: IBM Cloud Object Storage
- name: IBM Informix
- name: Impala
- name: Instagram
- name: JDBC-ODBC Bridge
- name: Jira
- name: Jira Assets
- name: Jira Service Management
- name: JSON
- name: Kafka
- name: Kintone
- name: LDAP
- name: LinkedIn
- name: LinkedIn Ads
- name: MailChimp
- name: MariaDB
- name: Marketo
- name: MarkLogic
- name: Microsoft Dataverse
- name: Microsoft Entra ID
- name: Microsoft Exchange
- name: Microsoft OneDrive
- name: Microsoft Planner
- name: Microsoft Project
- name: Microsoft Teams
- name: Monday.com
- name: MongoDB
- name: MYOB AccountRight
- name: MySQL
- name: nCino
- name: Neo4J
- name: NetSuite
- name: OData
- name: Odoo
- name: Office 365
- name: Okta
- name: OneNote
- name: Oracle
- name: Oracle Eloqua
- name: Oracle Financials Cloud
- name: Oracle HCM Cloud
- name: Oracle Sales
- name: Oracle SCM
- name: Oracle Service Cloud
- name: Outreach.io
- name: Parquet
- name: Paylocity
- name: PayPal
- name: Phoenix
- name: PingOne
- name: Pinterest
- name: Pipedrive
- name: PostgreSQL
- name: Power BI XMLA
- name: Presto
- name: Quickbase
- name: QuickBooks
- name: QuickBooks Online
- name: QuickBooks Time
- name: Raisers Edge NXT
- name: Reckon
- name: Reckon Accounts Hosted
- name: Redis
- name: Redshift
- name: REST
- name: RSS
- name: Sage 200
- name: Sage 300
- name: Sage 50 UK
- name: Sage Cloud Accounting
- name: Sage Intacct
- name: Salesforce
- name: Salesforce Data Cloud
- name: Salesforce Financial Service Cloud
- name: Salesforce Marketing
- name: Salesforce Marketing Cloud Account Engagement
- name: Salesforce Pardot
- name: Salesloft
- name: SAP
- name: SAP Ariba Procurement
- name: SAP Ariba Source
- name: SAP Business One
- name: SAP BusinessObjects BI
- name: SAP ByDesign
- name: SAP Concur
- name: SAP Fieldglass
- name: SAP HANA
- name: SAP HANA XS Advanced
- name: SAP Hybris C4C
- name: SAP Netweaver Gateway
- name: SAP SuccessFactors
- name: SAS Data Sets
- name: SAS xpt
- name: SendGrid
- name: ServiceNow
- name: SFTP
- name: SharePoint
- name: SharePoint Excel Services
- name: ShipStation
- name: Shopify
- name: SingleStore
- name: Slack
- name: Smartsheet
- name: Snapchat Ads
- name: Snowflake
- name: Spark
- name: Splunk
- name: SQL Analysis Services
- name: SQL Server
- name: SQLite
- name: Square
- name: Stripe
- name: Sugar CRM
- name: SuiteCRM
- name: SurveyMonkey
- name: Sybase
- name: Sybase IQ
- name: Tableau CRM Analytics
- name: Tally
- name: TaxJar
- name: Teradata
- name: Tier1
- name: TigerGraph
- name: Trello
- name: Trino
- name: Twilio
- name: Twitter
- name: Twitter Ads
- name: Veeva CRM
- name: Veeva Vault
- name: Wave Financial
- name: WooCommerce
- name: WordPress
- name: Workday
- name: xBase
- name: Xero
- name: XML
- name: YouTube Analytics
- name: Zendesk
- name: Zoho Books
- name: Zoho Creator
- name: Zoho CRM
- name: Zoho Inventory
- name: Zoho Projects
- name: Zuora
layout: provider
modified: '2026-04-23'
name: CData
nav: Providers
network: true
overview: 'CData publishes 3 APIs on the [APIs.io](https://apis.io/) network: Metadata API, Procedures API, and Query API. Tagged areas include Data, Data Access, Data Connectivity, Databases, and NoSQL.


  CData''s developer surface includes authentication, support, engineering blog, developer portal, and 21 more developer resources.'
plans:
- name: Cdata Plans Pricing
  plan_count: 3
  slug: cdata-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Cdata Rate Limits
  slug: cdata-rate-limits
score:
  band: developing
  composite: 46.7
  delta: -1.8
  facets:
    commercial_clarity: 76.3
    contract_quality: 54.5
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cdata/refs/heads/main/screenshots/cdata-2026-06-20T174101.png
security:
- kind: authentication
  name: Cdata Authentication
  slug: cdata-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Cdata Domain Security
  slug: cdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cdata Trust Center
  slug: cdata-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: cdata
tags:
- Data
- Data Access
- Data Connectivity
- Databases
- NoSQL
- SQL
website: https://www.cdata.com/developers/
---

---
aid: cdata
url: https://raw.githubusercontent.com/api-evangelist/cdata/refs/heads/main/apis.yml
apis:
  - aid: cdata:sql-api
    name: CData SQL API
    tags:
      - Data Access
      - Query
      - REST
      - SQL
    humanURL: https://cloud.cdata.com/docs/SQL-API.html
    properties:
      - url: https://cloud.cdata.com/docs/SQL-API.html
        type: Documentation
      - url: https://cloud.cdata.com/docs/API.html
        type: Overview
      - url: https://cloud.cdata.com/docs/Authentication.html
        type: Authentication
    description: The CData Cloud SQL API provides HTTP-based access to execute SQL queries, batch operations, and stored procedures across all data sources configured in a CData Connect Cloud account. Real-time data access across enterprise apps.
  - aid: cdata:metadata-api
    name: CData Metadata API
    tags:
      - Catalog
      - Data Access
      - Metadata
      - Schemas
    humanURL: https://cloud.cdata.com/docs/Metadata-API.html
    properties:
      - url: https://cloud.cdata.com/docs/Metadata-API.html
        type: Documentation
    description: The CData Cloud Metadata API exposes catalog information including schemas, tables, columns, keys, and stored procedures across every configured data source, enabling tools to introspect the connected sources before querying.
  - aid: cdata:log-api
    name: CData Log API
    tags:
      - Audit
      - Logs
      - Observability
    humanURL: https://cloud.cdata.com/docs/Log-API.html
    properties:
      - url: https://cloud.cdata.com/docs/Log-API.html
        type: Documentation
    description: The CData Cloud Log API retrieves operational logs for queries, jobs, and connection events, enabling observability of the CData Connect Cloud service.
  - aid: cdata:connection-api
    name: CData Connection API
    tags:
      - Administration
      - Connections
      - Data Sources
    humanURL: https://cloud.cdata.com/docs/Connection-API.html
    properties:
      - url: https://cloud.cdata.com/docs/Connection-API.html
        type: Documentation
    description: The CData Cloud Connection API manages data source connections programmatically, allowing administrators to create, update, test, and delete connections to databases and SaaS applications.
  - aid: cdata:job-api
    name: CData Job API
    tags:
      - Background Jobs
      - Monitoring
      - Replication
    humanURL: https://cloud.cdata.com/docs/Job-API.html
    properties:
      - url: https://cloud.cdata.com/docs/Job-API.html
        type: Documentation
    description: The CData Cloud Job API monitors background jobs such as replication, caching, and scheduled operations, exposing job state and history.
  - aid: cdata:account-api
    name: CData Account API
    tags:
      - Account Management
      - Administration
      - Users
    humanURL: https://cloud.cdata.com/docs/Account-API.html
    properties:
      - url: https://cloud.cdata.com/docs/Account-API.html
        type: Documentation
    description: The CData Cloud Account API manages account settings, workspaces, and user-level configuration for the CData Connect Cloud tenant.
  - aid: cdata:audit-api
    name: CData Audit API
    tags:
      - Audit
      - Compliance
      - Security
    humanURL: https://cloud.cdata.com/docs/Audit-API.html
    properties:
      - url: https://cloud.cdata.com/docs/Audit-API.html
        type: Documentation
    description: The CData Cloud Audit API tracks system activities and administrative events, supporting compliance and security monitoring requirements such as SOC 2 and GDPR.
  - aid: cdata:odata-api
    name: CData OData API
    tags:
      - Data Access
      - OData
      - REST
    humanURL: https://cloud.cdata.com/docs/OData.html
    properties:
      - url: https://cloud.cdata.com/docs/OData.html
        type: Documentation
      - url: https://www.odata.org/documentation/
        type: Specification
    description: CData Connect Cloud exposes an OData v4 compatible API that allows any OData client to browse metadata and query data from any configured source, including Excel, Power BI, and other BI tools.
name: CData
tags:
  - Data
  - Data Access
  - Data Connectivity
  - Databases
  - NoSQL
  - SQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.cdata.com/company/
    name: CData Software - About Us
    type: About
    description: 'null'
  - url: https://www.cdata.com/embedded/customers/
    name: CData Partnerships by Industry | Become One Today
    type: Partners
    description: 'null'
  - url: https://www.cdata.com/company/testimonials.aspx
    name: CData Software - Testimonials
    type: Testimonials
    description: 'null'
  - url: https://www.cdata.com/case-study/
    name: CData Success Stories & Case Studies
    type: CaseStudies
    description: 'null'
  - url: https://www.cdata.com/support/
    name: CData Software - Technical Support
    type: Support
    description: 'null'
  - url: https://www.cdata.com/kb/
    name: CData Software - Knowledge Base
    type: Knowledgebase
    description: 'null'
  - url: https://www.cdata.com/blog/
    name: CData Software - Blog
    type: Blog
    description: 'null'
  - url: https://www.cdata.com/resources/
    name: Learn from Our E-Books, Whitepapers, Webinars, and More
    type: WhitePapers
    description: 'null'
  - url: https://www.cdata.com/resources/
    name: Learn from Our E-Books, Whitepapers, Webinars, and More
    type: Webinars
    description: 'null'
  - url: https://www.cdata.com/events/
    name: Join Us at These Upcoming In-Person and Virtual CData Events
    type: Events
    description: 'null'
  - url: https://www.cdata.com/developers/
    name: CData Developer Center
    type: Portal
    description: 'null'
  - url: https://www.cdata.com/glossary/
    name: CData Glossary Archive
    type: Glossary
    description: 'null'
  - url: https://www.cdata.com/kb/video/
    name: CData Software - Video Gallery
    type: Videos
    description: 'null'
  - url: https://www.cdata.com/company/press.aspx
    name: Read the Latest News from CData
    type: PressReleases
    description: 'null'
  - url: https://www.cdata.com/company/legal/terms/
    name: CData Software - Terms of use
    type: TermsOfService
    description: 'null'
  - url: https://www.cdata.com/company/legal/privacy/
    name: CData Software - Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.cdata.com/security/
    name: Security & Privacy - CData Software Trust Center
    type: Security
    description: 'null'
  - url: https://www.cdata.com/security/
    name: Security & Privacy - CData Software Trust Center
    type: Compliance
    description: 'null'
  - url: https://aws.amazon.com/marketplace/pp/prodview-jizwvan7n7sn6
    name: AWS Marketplace
    type: AWSMarketplace
  - name: Features
    type: Features
    data:
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
  - name: Integrations
    type: Integrations
    data:
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
created: '2025-06-05'
modified: '2026-04-23'
position: Consumer
description: CData Software is a leading provider of data access and connectivity solutions. Our standards-based connectors streamline data access and insulate customers from the complexities of integrating with on-premise or cloud databases, SaaS, APIs, NoSQL, and Big Data.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---

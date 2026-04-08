---
aid: snaplogic
url: https://raw.githubusercontent.com/api-evangelist/snaplogic/refs/heads/main/apis.yml
apis:
- aid: snaplogic:snaplogic-public-apis
  name: SnapLogic Public APIs
  tags:
  - Automation
  - Integration
  - iPaaS
  humanURL: https://docs.snaplogic.com/public-apis/public-apis-about.html
  properties:
  - url: https://docs.snaplogic.com/public-apis/public-apis-about.html
    type: Documentation
  - url: https://docs.snaplogic.com/public-apis/apis-asset.html
    type: Documentation
  - url: https://docs.snaplogic.com/public-apis/apis-runtime.html
    type: Documentation
  - url: https://docs.snaplogic.com/public-apis/apis-project.html
    type: Documentation
  - url: https://docs.snaplogic.com/public-apis/apis-apim.html
    type: Documentation
  - url: https://docs.snaplogic.com/public-apis/apis-user-and-group.html
    type: Documentation
  - url: https://docs.snaplogic.com/public-apis/entra-id-configuration.html
    type: Authentication
  description: SnapLogic Public APIs provide programmatic management for your environment and project assets. The APIs cover activity tracking, asset management, asset catalog and lineage, log retrieval, runtime and pipeline execution control, task management, project and Git operations, Snaplex infrastructure management, Snap statistics, API Management lifecycle, and user and group administration. The platform authenticates API calls with basic authentication and JSON Web Token (JWT) over HTTPS.
- aid: snaplogic:snaplogic-api-management
  name: SnapLogic API Management
  tags:
  - API Gateway
  - API Lifecycle
  - API Management
  humanURL: https://www.snaplogic.com/products/api-management-development
  properties:
  - url: https://www.snaplogic.com/products/api-management-development
    type: Documentation
  - url: https://docs.snaplogic.com/public-apis/apis-apim.html
    type: Documentation
  - url: https://docs.snaplogic.com/api-m/reference/generic-oauth2.html
    type: Documentation
  - url: https://docs.snaplogic.com/monitor/observe-api-metrics.html
    type: Documentation
  description: SnapLogic API Management enables organizations to create, manage, secure, and monitor APIs throughout their lifecycle. It supports exposing SnapLogic pipelines as APIs or creating APIs from an OpenAPI specification, applying security policies, managing versions, publishing to a customizable developer portal, and monitoring API metrics and performance across on-premises, hybrid, and cloud environments.
- aid: snaplogic:snaplogic-snap-development
  name: SnapLogic Snap Development SDK
  tags:
  - Development
  - Integration
  - SDK
  humanURL: https://developer.snaplogic.com/
  properties:
  - url: https://developer.snaplogic.com/
    type: Documentation
  - url: https://github.com/SnapLogic/developer.snaplogic.com
    type: GitHubOrganization
  description: The SnapLogic Snap Development SDK provides a Java-based framework for building custom Snaps for the SnapLogic Intelligent Integration Platform. Snaps are streaming data processors that consume and produce Binary or Document data through input and output views. The SDK supports property configuration, expression language, binary and document data handling, input schema validation, error view handling, and unit testing.
- aid: snaplogic:snaplogic
  name: SnapLogic
  tags: []
  humanURL: ' https://www.snaplogic.com/'
  properties:
  - url: ' https://www.snaplogic.com/'
    type: Documentation
  description: Our AI-powered, all-in-one generative integration platform unifies your data and streamlines workflows to transform your business.
name: SnapLogic
tags:
- AI
- API Management
- Automation
- Data Integration
- Integrations
- iPaaS
- Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://docs-snaplogic.atlassian.net/wiki/spaces/SD/overview
  name: Documentation
  type: Documentation
- url: https://www.linkedin.com/company/snaplogic/
  name: LinkedIn
  type: LinkedIn
- url: https://www.snaplogic.com/
  name: iPaaS Solution for the Enterprise | SnapLogic
  type: Website
  description: 'null'
- url: https://www.snaplogic.com/products/snaps
  name: SnapLogic Snaps | Pre-built Intelligent Connectors
  type: Integrations
  description: 'null'
- url: https://www.snaplogic.com/use-cases
  data:
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
  name: Data and Application Integration Use Cases | SnapLogic
  type: UseCases
- url: https://www.snaplogic.com/request-demo
  name: Request a Customized Demo of SnapLogic
  type: RequestDemo
  description: 'null'
- url: https://www.snaplogic.com/partners
  name: Partner Ecosystem | SnapLogic
  type: Partners
  description: 'null'
- url: https://www.snaplogic.com/customers
  name: SnapLogic Customer Success Stories and Case Studies
  type: Customers
  description: 'null'
- url: https://www.snaplogic.com/blog
  name: The Generative Integration Blog by SnapLogic
  type: Blog
  description: 'null'
- url: https://www.snaplogic.com/resources?_resource_type=ebook
  name: SnapLogic Resource Library
  type: eBooks
  description: 'null'
- url: https://www.snaplogic.com/resources/podcasts
  name: Evolving the Enterprise Podcast | Hosted by SnapLogic
  type: Podcast
  description: 'null'
- url: https://www.snaplogic.com/resources/events
  name: SnapLogic Upcoming Events & Webinars
  type: Webinars
  description: 'null'
- url: https://www.snaplogic.com/resources/events/customer-workshops
  name: SnapLogic 101 Training Workshops | SnapLogic
  type: Training
  description: 'null'
- url: https://cdn.elastic.snaplogic.com/sl/login.html?referrer=https://www.snaplogic.com/
  name: SnapLogic User Login
  type: Login
  description: 'null'
- url: https://www.snaplogic.com/request-demo
  name: Request a Customized Demo of SnapLogic
  type: RequestDemo
  description: 'null'
- url: https://www.snaplogic.com/pricing
  name: SnapLogic Pricing Model for iPaaS, ETL, AI Agents
  type: Pricing
  description: 'null'
- url: https://www.snaplogic.com/security-standards
  name: Security Standards | SnapLogic
  type: Security
  description: 'null'
- url: https://www.snaplogic.com/glossary
  name: SnapLogic Glossary
  type: Glossary
  description: 'null'
- url: https://www.snaplogic.com/getting-help
  name: Get Help with the SnapLogic Platform for Generative Integration
  type: Support
  description: 'null'
- url: https://www.snaplogic.com/privacy-policy
  name: Privacy and Cookie Policy | SnapLogic
  type: PrivacyPolicy
  description: 'null'
- url: https://www.snaplogic.com/terms-of-use
  name: Terms of Use | SnapLogic
  type: TermsOfService
  description: 'null'
created: '2025-06-06T00:00:00.000Z'
modified: '2026-04-07'
position: Consumer
description: Our AI-powered, all-in-one generative integration platform unifies your data and streamlines workflows to transform your business.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


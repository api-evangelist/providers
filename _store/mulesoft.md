---
aid: mulesoft
url: https://raw.githubusercontent.com/api-evangelist/mulesoft/refs/heads/main/apis.yml
apis:
- aid: mulesoft:mulesoft
  name: MuleSoft Anypoint Platform
  description: MuleSoft Anypoint Platform unifies API management with integration, providing a complete solution to connect any application, data source, or device with reusable APIs and integrations.
  humanURL: https://www.mulesoft.com/platform/api
  tags:
  - API Gateway
  - API Management
  - Enterprise
  properties:
  - type: Documentation
    url: https://docs.mulesoft.com/
  - type: Getting Started
    url: https://docs.mulesoft.com/general/
- aid: mulesoft:mulesoft-anypoint-platform-api
  name: MuleSoft Anypoint Platform Management API
  description: The Anypoint Platform Management API provides programmatic access to manage organizations, business groups, environments, and users within the MuleSoft Anypoint Platform. It enables automation of platform administration tasks including configuring access management, managing connected applications, and controlling role-based access control across the platform.
  humanURL: https://docs.mulesoft.com/access-management/
  baseURL: https://anypoint.mulesoft.com
  tags:
  - Administration
  - API Management
  - Enterprise
  - REST
  properties:
  - type: Documentation
    url: https://docs.mulesoft.com/access-management/
  - type: Reference
    url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
  - type: Authentication
    url: https://docs.mulesoft.com/access-management/connected-apps-overview
  - type: OpenAPI
    url: openapi/mulesoft-anypoint-platform-openapi.yml
  - type: JSONSchema
    url: json-schema/mulesoft-application-schema.json
  - type: JSON-LD
    url: json-ld/mulesoft-context.jsonld
- aid: mulesoft:mulesoft-anypoint-exchange-api
  name: MuleSoft Anypoint Exchange API
  description: The Anypoint Exchange API provides programmatic access to MuleSoft's asset marketplace, enabling discovery, publishing, and management of reusable integration assets including APIs, connectors, templates, examples, and custom pages. It allows organizations to automate asset lifecycle management and promote API reuse across teams.
  humanURL: https://docs.mulesoft.com/exchange/
  baseURL: https://anypoint.mulesoft.com/exchange/api/v2
  tags:
  - API Catalog
  - Asset Management
  - Enterprise
  - Marketplace
  properties:
  - type: Documentation
    url: https://docs.mulesoft.com/exchange/
  - type: Reference
    url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/exchange-experience-api/
  - type: Getting Started
    url: https://docs.mulesoft.com/exchange/to-publish-assets-maven
- aid: mulesoft:mulesoft-anypoint-runtime-manager-api
  name: MuleSoft Anypoint Runtime Manager API
  description: The Anypoint Runtime Manager API provides programmatic control over Mule application deployments across CloudHub, Runtime Fabric, and hybrid deployment targets. It enables CI/CD automation for deploying, updating, starting, stopping, and monitoring Mule applications and their runtime environments.
  humanURL: https://docs.mulesoft.com/runtime-manager/
  baseURL: https://anypoint.mulesoft.com/cloudhub/api
  tags:
  - CI/CD
  - CloudHub
  - Deployment
  - Runtime Manager
  properties:
  - type: Documentation
    url: https://docs.mulesoft.com/runtime-manager/
  - type: Reference
    url: https://docs.mulesoft.com/runtime-manager/cloudhub-api
  - type: Getting Started
    url: https://docs.mulesoft.com/runtime-manager/deploying-to-cloudhub
- aid: mulesoft:mulesoft-anypoint-mq-api
  name: MuleSoft Anypoint MQ API
  description: The Anypoint MQ API provides a cloud messaging service built on the Anypoint Platform for asynchronous messaging between Mule applications and other systems. It supports queues, exchanges, and dead-letter queues for reliable message delivery and decoupled integration patterns.
  humanURL: https://docs.mulesoft.com/mq/
  baseURL: https://anypoint.mulesoft.com/mq/stats/api/v1
  tags:
  - Async
  - Cloud
  - Messaging
  - Queue
  properties:
  - type: Documentation
    url: https://docs.mulesoft.com/mq/
  - type: Reference
    url: https://docs.mulesoft.com/mq/mq-apis
  - type: Getting Started
    url: https://docs.mulesoft.com/mq/mq-tutorial
- aid: mulesoft:mulesoft-anypoint-design-center-api
  name: MuleSoft Anypoint Design Center API
  description: The Anypoint Design Center API provides access to the MuleSoft web-based API design environment for creating and editing API specifications in RAML and OAS formats. It supports project management, file operations, and publishing designed APIs to Anypoint Exchange for reuse across the organization.
  humanURL: https://docs.mulesoft.com/design-center/
  baseURL: https://anypoint.mulesoft.com/designcenter/api-designer
  tags:
  - API Design
  - Design Center
  - OpenAPI
  - RAML
  properties:
  - type: Documentation
    url: https://docs.mulesoft.com/design-center/
  - type: Getting Started
    url: https://docs.mulesoft.com/design-center/design-create-publish-api-specs
name: MuleSoft
tags:
- API Gateway
- API Management
- Enterprise
- Integration
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://trailheadacademy.salesforce.com/products/mulesoft
  name: Certifications
  type: Certifications
- url: https://www.mulesoft.com/
  name: MuleSoft | Integration And Automation For The AI Era
  type: Website
  description: 'null'
- url: https://www.mulesoft.com/integration-resources?type[0]=Webinar
  name: API, SaaS & SOA Integration | Resource Center | MuleSoft
  type: Webinars
  description: 'null'
- url: https://videos.mulesoft.com/?_gl=1*1yqvlbf*_gcl_au*MjAyNzM1NTg1NS4xNzQ5MTM5OTUx
  name: MuleSoft Videos
  type: Videos
  description: 'null'
- url: https://www.mulesoft.com/integration-resources
  name: API, SaaS & SOA Integration | Resource Center | MuleSoft
  type: eBooks
  description: 'null'
- url: https://www.mulesoft.com/integration-resources?type[0]=Whitepaper
  name: API, SaaS & SOA Integration | Resource Center | MuleSoft
  type: WhitePapers
  description: 'null'
- url: https://www.mulesoft.com/resources/articles
  name: Articles | API, SaaS, SOA integration resources | MuleSoft
  type: ' Articles'
  description: 'null'
- url: https://blogs.mulesoft.com/bloghome/
  name: MuleSoft Blog
  type: Blog
  description: 'null'
- url: https://developer.mulesoft.com/
  name: Simplify API Design, implementation, deployment, and operation | MuleSoft Developers | MuleSoft Developers
  type: GettingStarted
  description: 'null'
- url: https://docs.mulesoft.com/general/
  name: MuleSoft Documentation
  type: Documentation
  description: 'null'
- url: https://docs.mulesoft.com/release-notes/quick-refs/by-date-index
  name: Release Note Summary by Month | MuleSoft Documentation
  type: ChangeLog
  description: 'null'
- url: https://docs.mulesoft.com/general/glossary
  name: Anypoint Platform Glossary | MuleSoft Documentation
  type: Glossary
  description: 'null'
- url: https://docs.mulesoft.com/general/learning-map-api-management
  name: Getting Started with API Management on Anypoint Platform | MuleSoft Documentation
  type: GettingStarted
  description: 'null'
- url: https://docs.mulesoft.com/mule-sdk/latest/
  name: Mule SDKs | MuleSoft Documentation
  type: SDKs
  description: 'null'
- url: https://anypoint.mulesoft.com/login/signin?apintent=generic
  name: Anypoint Platform
  type: Login
  description: 'null'
- url: https://anypoint.mulesoft.com/login/signup?apintent=generic
  name: Anypoint Platform
  type: SignUp
  description: 'null'
- url: https://www.mulesoft.com/integration-partner/partnermax-retirement
  name: MuleSoft PartnerMax Retirement New Program
  type: Partners
  description: 'null'
- data:
  - name: B2B EDI integration
  - name: DevOps
  - name: eCommerce
  - name: Event-Driven Architecture
  - name: iPaaS
  - name: Legacy system modernization
  - name: Microservices
  - name: Move to the cloud
  - name: Omnichannel
  - name: SaaS integration
  - name: Single view of customer
  - name: Business automation
  - name: eCommerce
  - name: Legacy system modernization
  - name: Mobile
  - name: Move to the cloud
  - name: Omnichannel
  - name: SaaS
  - name: Single view of customer
  name: UseCases
  type: UseCases
- data:
  - name: AI Agents and Models
  - name: Amazon Sqs
  - name: Amqp
  - name: API Catalogs
  - name: API Governance
  - name: Apply Standards
  - name: Automate Deployments
  - name: Automatic Hardening
  - name: Code Reuse
  - name: Collaboration Across Teams
  - name: Common API Patterns
  - name: Common Integratin Patterns
  - name: Conformance Validation
  - name: Connect Data
  - name: Connect to SAAS Applications
  - name: Continuous Communication Between Mulesoft and Agentforce
  - name: Continuous Software Updates
  - name: Create Any API With Asyncapi
  - name: Create Any API With Graphql
  - name: Create Any API With Oas
  - name: Create Any API With Raml
  - name: Curated Set of API Topics
  - name: Custom Security Policies
  - name: Data Residency for Regional Compliance
  - name: Dead Letter Queue Availability
  - name: Decrease Mean-Time-To-Resolution
  - name: Deploy Runtimes on Amazon Web Services (AWS)
  - name: Deploy Runtimes on Google Cloud Platform
  - name: Deploy Runtimes on Microsoft Azure
  - name: Deploy Runtimes on Red Hat Openshift
  - name: Design Suggestions
  - name: Design Time Error Handling
  - name: Developer Portals
  - name: Edge Security
  - name: Edi
  - name: Expose Any API as an Mcp Server
  - name: Expose Data From Third Party Applications to Agentforce
  - name: Filter Data Formats
  - name: Flexible API Gateways
  - name: Globally Distributed Architecture
  - name: Governance and Access Controls
  - name: Guided Recommendations
  - name: Hyperscale Log Management
  - name: Invoke Agentforce
  - name: Jdbc
  - name: Jms
  - name: Join Data Formats
  - name: Map Data Formats
  - name: Mqtt
  - name: Multi-Tenancy for Applications
  - name: Multi-Tenancy for Workers
  - name: Natural Language Requirements
  - name: Next Generation Security
  - name: Normalize Data Formats
  - name: Odbc
  - name: Orchestrate Deployments
  - name: Persistent Data Storage
  - name: Pre-built Security Policies
  - name: Prebuilt API Fragments
  - name: Prebuilt Connectors
  - name: Prebuilt Examples
  - name: Prebuilt Templates
  - name: Process Data
  - name: Programmatically Control Runtimes
  - name: Programmatically Monitor Runtimes
  - name: Responsive Experiences
  - name: Reusable API Fragments
  - name: Scale API Portals
  - name: Secure
  - name: Sensitive Information Detection
  - name: Service Mesh
  - name: Shared Platform
  - name: Source of Truth
  - name: Standards Control Groups
  - name: Switch Environments
  - name: Tracing
  - name: Transform Data
  - name: Understand Health of Your Application Network
  - name: Unified View of Applications
  - name: Unified View of Runtime
  - name: Universal Visibility
  - name: Vscode Integration
  name: Features
  type: Features
- data:
  - name: A2a
  - name: Adobe Marketo
  - name: Agentforce
  - name: Aggregators Module
  - name: Amazon Dynamodb
  - name: Amazon EC2
  - name: Amazon Kinesis
  - name: Amazon Lambda
  - name: Amazon Rds
  - name: Amazon Redshift
  - name: Amazon S3
  - name: Amazon Secrets Manager Properties Provider
  - name: Amazon Sns
  - name: Amazon Sqs
  - name: Amqp
  - name: Anypoint Custom Metrics
  - name: Anypoint MQ
  - name: Apache Cassandra
  - name: Apache Kafka
  - name: AS2
  - name: Asana
  - name: Azure Cosmos Db
  - name: Azure Data Lake Storage
  - name: Azure Event Hubs
  - name: Azure Key Vault
  - name: Azure Key Vault Properties Provider
  - name: Azure Service Bus
  - name: Azure Service Bus Management
  - name: BMC Remedy
  - name: Box
  - name: Caqh
  - name: Cloudhub
  - name: Compression Module
  - name: Confluent Schema Registry
  - name: Cryptography Module
  - name: Database
  - name: Docusign
  - name: Dropbox
  - name: Edifact Edi
  - name: Einstein AI
  - name: Email
  - name: File
  - name: FTP
  - name: Ftps
  - name: Gmail
  - name: Google Bigquery
  - name: Google Calendar
  - name: Google Drive
  - name: Google Pub/Sub
  - name: Google Sheets
  - name: Hadoop (Hdfs)
  - name: HL7 Edi
  - name: HL7 Mllp
  - name: HTTP
  - name: IBM Ctg
  - name: IBM MQ
  - name: Java Module
  - name: Jira
  - name: Jms
  - name: Json Module
  - name: Ldap
  - name: Mailchimp Marketing
  - name: Mcp
  - name: Microsoft .Net
  - name: Microsoft Dynamics 365
  - name: Microsoft Dynamics 365 Business Central
  - name: Microsoft Dynamics 365 for Finance and Operations
  - name: Microsoft Dynamics AX 2012
  - name: Microsoft Dynamics CRM
  - name: Microsoft Dynamics GP
  - name: Microsoft Dynamics Nav
  - name: Microsoft Excel Online
  - name: Microsoft Msmq
  - name: Microsoft Onedrive
  - name: Microsoft Outlook 365
  - name: Microsoft Power Bi
  - name: Microsoft Service Bus
  - name: Microsoft Sharepoint
  - name: Microsoft Teams
  - name: Microsoft Windows Powershell
  - name: Mongodb
  - name: Mqtt
  - name: Mulesoft AI Chain
  - name: Neo4j
  - name: Netsuite
  - name: Netsuite Openair
  - name: Netsuite Restlet
  - name: Oauth Module
  - name: OAUTH2 Provider Module
  - name: Object Store
  - name: Oracle Ebs 12.1
  - name: Oracle Ebs 12.2
  - name: Oracle Peoplesoft
  - name: Oracle Siebel
  - name: Quickbooks Online
  - name: Redis
  - name: Roostify
  - name: Rosettanet
  - name: Salesforce
  - name: Salesforce Commerce Cloud B2C Data
  - name: Salesforce Commerce Cloud B2C Shop API
  - name: Salesforce Composite
  - name: Salesforce Data Cloud
  - name: Salesforce Einstein Analytics
  - name: Salesforce Marketing Cloud
  - name: Salesforce Marketing Cloud Rest
  - name: Salesforce Pub/Sub
  - name: Sap
  - name: Sap Concur
  - name: Sap S/4HANA Odata
  - name: Sap S/4HANA Soap
  - name: Sap Successfactors
  - name: Scripting Module
  - name: Servicenow
  - name: Sftp
  - name: Shopify
  - name: Slack
  - name: Smartsheet
  - name: Snowflake
  - name: Sockets
  - name: Spring Module
  - name: Stripe
  - name: Tableau
  - name: Tracing Module
  - name: Tradacoms Edi
  - name: Trello
  - name: Twilio
  - name: Validation Module
  - name: Veeva Vault
  - name: Vm
  - name: Web Service Consumer
  - name: Websockets
  - name: Workday
  - name: Wss Module
  - name: X12 Edi
  - name: Xero Accounting
  - name: Xml Module
  - name: Zendesk
  - name: Zoom
  - name: Zuora
  - name: Zuora Aqua
  name: Integrations
  type: Integrations
created: '2025-06-05T00:00:00.000Z'
modified: '2026-04-07'
position: Consumer
description: MuleSoft Anypoint Platform is an enterprise integration and API management platform offering an API gateway, design center, exchange marketplace, and monitoring for hybrid deployments connecting applications and data.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


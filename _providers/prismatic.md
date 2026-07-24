---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 52.9
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Prismatic Agentic Access
  operation_count: 4
  slug: prismatic-agentic-access
  summary_line: 4 operations · 3 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Prismatic provides a GraphQL-based API for you to build, deploy, and support your integrations programmatically. While Prismatic recommends that new users use the web app or Prismatic CLI tool (prism)
  name: Prismatics GraphQL API
  slug: prismatics-graphql-api
- description: Authentication endpoints for obtaining, refreshing, and revoking JWT tokens used to access the Prismatic API
  name: Prismatic Authentication API
  slug: prismatic-authentication-api
arazzos:
- description: Get a short-lived token from an active web session, then list components.
  name: Prismatic Browser Session List Components
  slug: prismatic-browser-session-list-components-workflow
- description: Refresh an access token then create a new customer tenant.
  name: Prismatic Create Customer with Refreshed Token
  slug: prismatic-create-customer-workflow
- description: List all integrations, then list the deployed instances that reference them.
  name: Prismatic List Integrations and Deployed Instances
  slug: prismatic-list-integrations-and-instances-workflow
- description: Create a customer, branch on GraphQL errors, then verify it appears in the customer list.
  name: Prismatic Onboard and Verify Customer
  slug: prismatic-onboard-and-verify-customer-workflow
- description: Exchange a refresh token for a fresh access token, then list all customers.
  name: Prismatic Refresh Token and List Customers
  slug: prismatic-refresh-and-list-customers-workflow
- description: Refresh an access token, use it, then revoke the old refresh token.
  name: Prismatic Rotate Refresh Token
  slug: prismatic-rotate-refresh-token-workflow
- description: Capture a full snapshot of customers, integrations, and instances in one pass.
  name: Prismatic Tenant Inventory Snapshot
  slug: prismatic-tenant-inventory-snapshot-workflow
artifact_total: 254
collections:
- collection_type: postman
  name: Prismatic GraphQL API
  slug: postman-prismatic-graphql-api
- collection_type: open
  name: Prismatic GraphQL API
  slug: open-prismatic-graphql-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prismatic-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prismatic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prismatic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prismatic-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/prismatic/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prismatic-browser-session-list-components-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prismatic-create-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prismatic-list-integrations-and-instances-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prismatic-onboard-and-verify-customer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prismatic-refresh-and-list-customers-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prismatic-rotate-refresh-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prismatic-tenant-inventory-snapshot-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://prismatic.io
- group: docs
  title: ''
  type: Documentation
  url: https://prismatic.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://prismatic.io/docs/integrations/low-code-integration-designer/get-started/first-integration/
- group: build
  title: ''
  type: CLI
  url: https://prismatic.io/docs/cli/
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@prismatic-io/prism
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@prismatic-io/spectral
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@prismatic-io/embedded
- group: build
  title: ''
  type: SDKs
  url: https://prismatic.io/docs/custom-connectors/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prismatic-io/spectral
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prismatic-io/embedded
- group: other
  title: ''
  type: IDE
  url: https://github.com/prismatic-io/vscode
- group: other
  title: ''
  type: Terraform
  url: https://github.com/prismatic-io/terraform-provider-prismatic
- group: agent
  title: ''
  type: MCP
  url: https://github.com/prismatic-io/prism-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/prismatic-io/prismatic-skills
- group: other
  title: ''
  type: CI/CD
  url: https://prismatic.io/docs/api/ci-cd-system/
- group: build
  title: ''
  type: GitHubActions
  url: https://prismatic.io/docs/api/github-actions/
- group: operate
  title: ''
  type: ChangeLog
  url: https://prismatic.io/docs/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.prismatic-status.io/
- group: other
  title: ''
  type: RSS
  url: https://www.prismatic-status.io/history.rss
- group: other
  title: ''
  type: Atom
  url: https://www.prismatic-status.io/history.atom
- group: company
  title: ''
  type: Blog
  url: https://prismatic.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://prismatic.io/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/prismatic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prismatic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prismatic-finops.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prismatic.io/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prismatic.io/legal/terms/
- group: auth
  title: ''
  type: Security
  url: https://prismatic.io/legal/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prismatic-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prismatic-io
- group: other
  title: ''
  type: Benefits
  url: ''
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/prismatic-io/prismatic-skills
- group: agent
  title: ''
  type: MCP
  url: https://github.com/prismatic-io/prism-mcp
- group: other
  title: ''
  type: AIAgent
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://prismatic.io/llms.txt
created: '2025-06-05'
description: The integration platform for B2B SaaS teams. Prismatic empowers everyone on your team with integration tools for devs and non-devs alike, combining a code-native TypeScript SDK with a low-code designer and an embedded marketplace for shipping customer-facing integrations.
examples:
- key_count: 4
  name: Create Customer Example
  slug: create-customer-example
- key_count: 4
  name: List Components Example
  slug: list-components-example
- key_count: 4
  name: List Customers Example
  slug: list-customers-example
- key_count: 4
  name: List Instances Example
  slug: list-instances-example
- key_count: 4
  name: List Integrations Example
  slug: list-integrations-example
- key_count: 4
  name: Refresh Token Example
  slug: refresh-token-example
features:
- name: Low-Code Integration Designer
- name: Code-Native Integrations
- name: Embedded Workflow Builder
- name: AI Copilot For Workflow Builder
- name: AI Coding Agent Support (MCP Server)
- name: Connectors
- name: Integration Marketplace
- name: Integration Configuration
- name: Integration Deployment
- name: Integration Support
- name: Integration Monitoring
- name: Integration Management
- name: Workflow Contexts
finops:
- name: Prismatic Finops
  service_category: Embedded iPaaS
  slug: prismatic-finops
graphqls:
- description: Prismatic provides a GraphQL-based API for you to build, deploy, and support your integrations programmatically. While Prismatic recommends that new users use the web app or Prismatic CLI tool (prism)
  name: Prismatic GraphQL API
  slug: prismatic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prismatic.png
integrations:
- name: Active Directory
  url: https://prismatic.io/connectors/ldap/
- name: Adobe Acrobat Sign
  url: https://prismatic.io/connectors/adobe-acrobat-sign/
- name: Adobe Analytics
  url: https://prismatic.io/connectors/adobe-analytics/
- name: Adobe Commerce Magento
  url: https://prismatic.io/connectors/adobe-commerce-magento/
- name: Adobe I/O Events
  url: https://prismatic.io/connectors/adobe-io-events/
- name: Adobe Marketo Engage
  url: https://prismatic.io/connectors/marketo/
- name: ADP Workforce Now
  url: https://prismatic.io/connectors/adp-workforce-now/
- name: Airtable
  url: https://prismatic.io/connectors/airtable/
- name: Algolia
  url: https://prismatic.io/connectors/algolia/
- name: Amazon DynamoDB
  url: https://prismatic.io/connectors/aws-dynamodb/
- name: Amazon S3
  url: https://prismatic.io/connectors/aws-s3/
- name: Amazon Seller Central
  url: https://prismatic.io/connectors/amazon-seller-central/
- name: Amazon SES
  url: https://prismatic.io/connectors/aws-ses/
- name: Amazon SNS
  url: https://prismatic.io/connectors/aws-sns/
- name: Amazon SQS
  url: https://prismatic.io/connectors/aws-sqs/
- name: AMQP
  url: https://prismatic.io/connectors/amqp/
- name: Anthropic
  url: https://prismatic.io/connectors/anthropic/
- name: ArcGIS
  url: https://prismatic.io/connectors/arcgis/
- name: Arena PLM
  url: https://prismatic.io/connectors/arena-plm/
- name: Asana
  url: https://prismatic.io/connectors/asana/
- name: Aspose
  url: https://prismatic.io/connectors/aspose/
- name: AWS Glue
  url: https://prismatic.io/connectors/aws-glue/
- name: AWS Lambda
  url: https://prismatic.io/connectors/aws-lambda/
- name: Azure Blob Storage
  url: https://prismatic.io/connectors/azure-blob/
- name: Azure Event Grid
  url: https://prismatic.io/connectors/azure-event-grid/
- name: Azure Files
  url: https://prismatic.io/connectors/azure-files/
- name: Azure OpenAI Service
  url: https://prismatic.io/connectors/azure-openai-service/
- name: Azure Service Bus
  url: https://prismatic.io/connectors/azureServiceBus/
- name: BambooHR
  url: https://prismatic.io/connectors/bamboohr/
- name: BigCommerce
  url: https://prismatic.io/connectors/bigcommerce/
- name: Bill
  url: https://prismatic.io/connectors/bill/
- name: Box
  url: https://prismatic.io/connectors/box/
- name: Branch
  url: https://prismatic.io/connectors/branch/
- name: Bynder
  url: https://prismatic.io/connectors/bynder/
- name: Calendly
  url: https://prismatic.io/connectors/calendly/
- name: Change Data Format
  url: https://prismatic.io/connectors/change-data-format/
- name: ClickUp
  url: https://prismatic.io/connectors/click-up/
- name: Code
  url: https://prismatic.io/connectors/code/
- name: Collection Tools
  url: https://prismatic.io/connectors/collection-tools/
- name: Confluence
  url: https://prismatic.io/connectors/confluence/
- name: Contentful
  url: https://prismatic.io/connectors/contentful/
- name: Cross Flow
  url: https://prismatic.io/connectors/cross-flow/
- name: CSV
  url: https://prismatic.io/connectors/csv/
- name: Customer.io
  url: https://prismatic.io/connectors/customer-io/
- name: Data Mapper
  url: https://prismatic.io/connectors/data-mapper/
- name: Databricks
  url: https://prismatic.io/connectors/databricks/
- name: Date/Time
  url: https://prismatic.io/connectors/datetime/
- name: DeepSeek
  url: https://prismatic.io/connectors/deepseek/
- name: DocuSign
  url: https://prismatic.io/connectors/docusign/
- name: Domo
  url: https://prismatic.io/connectors/domo/
- name: Dropbox
  url: https://prismatic.io/connectors/dropbox/
- name: Duro PLM
  url: https://prismatic.io/connectors/duro-plm/
- name: Expensify
  url: https://prismatic.io/connectors/Expensify/
- name: Firebase
  url: https://prismatic.io/connectors/firebase/
- name: Fluent Commerce
  url: https://prismatic.io/connectors/fluent-commerce/
- name: Freshservice
  url: https://prismatic.io/connectors/freshservice/
- name: Frontify
  url: https://prismatic.io/connectors/frontify/
- name: FTP
  url: https://prismatic.io/connectors/ftp/
- name: GitHub
  url: https://prismatic.io/connectors/github/
- name: Gmail
  url: https://prismatic.io/connectors/google-gmail/
- name: Gong
  url: https://prismatic.io/connectors/gong/
- name: Google Ads
  url: https://prismatic.io/connectors/google-ads/
- name: Google Analytics - GA4
  url: https://prismatic.io/connectors/google-analytics-ga4/
- name: Google Analytics - UA
  url: https://prismatic.io/connectors/google-analytics/
- name: Google Calendar
  url: https://prismatic.io/connectors/google-calendar/
- name: Google Cloud BigQuery
  url: https://prismatic.io/connectors/google-cloud-bigquery/
- name: Google Cloud Pub/Sub
  url: https://prismatic.io/connectors/google-cloud-pub-sub/
- name: Google Cloud Storage
  url: https://prismatic.io/connectors/google-cloud-storage/
- name: Google Docs
  url: https://prismatic.io/connectors/google-docs/
- name: Google Drive
  url: https://prismatic.io/connectors/google-drive/
- name: Google Gemini
  url: https://prismatic.io/connectors/google-gemini/
- name: Google Sheets
  url: https://prismatic.io/connectors/google-sheets/
- name: Google Shopping
  url: https://prismatic.io/connectors/google-content-shopping/
- name: Gorgias
  url: https://prismatic.io/connectors/gorgias/
- name: GoTo Webinar
  url: https://prismatic.io/connectors/gotowebinar/
- name: GraphQL
  url: https://prismatic.io/connectors/graphql/
- name: Greenhouse
  url: https://prismatic.io/connectors/greenhouse/
- name: Gusto
  url: https://prismatic.io/connectors/gusto/
- name: Hash
  url: https://prismatic.io/connectors/hash/
- name: HiBob
  url: https://prismatic.io/connectors/hibob/
- name: HTML Utils
  url: https://prismatic.io/connectors/html-utils/
- name: HTTP
  url: https://prismatic.io/connectors/http/
- name: HubSpot
  url: https://prismatic.io/connectors/hubspot/
- name: IMAP
  url: https://prismatic.io/connectors/imap/
- name: Intercom
  url: https://prismatic.io/connectors/intercom/
- name: Jira
  url: https://prismatic.io/connectors/atlassian-jira/
- name: JSON Forms
  url: https://prismatic.io/connectors/jsonforms/
- name: JSONata
  url: https://prismatic.io/connectors/jsonata/
- name: Kafka
  url: https://prismatic.io/connectors/kafka/
- name: Karbon
  url: https://prismatic.io/connectors/karbon/
- name: Klaviyo
  url: https://prismatic.io/connectors/klaviyo/
- name: Liquid Template
  url: https://prismatic.io/connectors/liquid-template/
- name: Log
  url: https://prismatic.io/connectors/log/
- name: Loop
  url: https://prismatic.io/connectors/loop/
- name: Mailchimp
  url: https://prismatic.io/connectors/mailchimp/
- name: Management Trigger
  url: https://prismatic.io/connectors/management-triggers/
- name: Math
  url: https://prismatic.io/connectors/math/
- name: MessagePack
  url: https://prismatic.io/connectors/messagepack/
- name: Meta Ads
  url: https://prismatic.io/connectors/facebook-marketing/
- name: Microsoft Bing Ads
  url: https://prismatic.io/connectors/ms-bing-ads/
- name: Microsoft Bot Framework
  url: https://prismatic.io/connectors/ms-bot-framework/
- name: Microsoft Dynamics 365
  url: https://prismatic.io/connectors/ms-dynamics/
- name: Microsoft Dynamics 365 Business Central
  url: https://prismatic.io/connectors/ms-business-central/
- name: Microsoft Entra ID
  url: https://prismatic.io/connectors/ms-entra-id/
- name: Microsoft Excel
  url: https://prismatic.io/connectors/ms-excel/
- name: Microsoft Graph API
  url: https://prismatic.io/connectors/ms-graph-api/
- name: Microsoft Intune
  url: https://prismatic.io/connectors/ms-intune/
- name: Microsoft OneDrive
  url: https://prismatic.io/connectors/ms-onedrive/
- name: Microsoft Outlook
  url: https://prismatic.io/connectors/ms-outlook/
- name: Microsoft Power BI
  url: https://prismatic.io/connectors/ms-power-bi/
- name: Microsoft Project
  url: https://prismatic.io/connectors/ms-project/
- name: Microsoft SharePoint
  url: https://prismatic.io/connectors/ms-sharepoint/
- name: Microsoft SQL Server
  url: https://prismatic.io/connectors/ms-sql-server/
- name: Microsoft Teams
  url: https://prismatic.io/connectors/ms-teams/
- name: Mixpanel
  url: https://prismatic.io/connectors/mixpanel/
- name: Monday
  url: https://prismatic.io/connectors/monday/
- name: MongoDB
  url: https://prismatic.io/connectors/mongo/
- name: MQTT
  url: https://prismatic.io/connectors/mqtt/
- name: MySQL
  url: https://prismatic.io/connectors/mysql/
- name: NetSuite
  url: https://prismatic.io/connectors/netsuite/
- name: New Relic
  url: https://prismatic.io/connectors/new-relic/
- name: Notion
  url: https://prismatic.io/connectors/notion/
- name: Odoo
  url: https://prismatic.io/connectors/odoo/
- name: OpenAI
  url: https://prismatic.io/connectors/openai/
- name: Oracle Database
  url: https://prismatic.io/connectors/oracledb/
- name: PagerDuty
  url: https://prismatic.io/connectors/pagerduty/
- name: Paylocity
  url: https://prismatic.io/connectors/paylocity/
- name: PDF
  url: https://prismatic.io/connectors/pdf/
- name: PDQ
  url: https://prismatic.io/connectors/pdq/
- name: Persist Data
  url: https://prismatic.io/connectors/persist-data/
- name: Pipedrive
  url: https://prismatic.io/connectors/pipedrive/
- name: Planisware Enterprise
  url: https://prismatic.io/connectors/planisware-enterprise/
- name: PostgreSQL
  url: https://prismatic.io/connectors/postgres/
- name: Postmark
  url: https://prismatic.io/connectors/postmark/
- name: Pretty Good Privacy
  url: https://prismatic.io/connectors/pgp/
- name: Prismatic
  url: https://prismatic.io/connectors/prismatic/
- name: Process Data
  url: https://prismatic.io/connectors/process-data/
- name: Qlik
  url: https://prismatic.io/connectors/qlik/
- name: QuickBooks
  url: https://prismatic.io/connectors/quickbooks/
- name: QuickBooks Time
  url: https://prismatic.io/connectors/quickbooks-time/
- name: Ramp
  url: https://prismatic.io/connectors/ramp/
- name: Recursive Flow
  url: https://prismatic.io/connectors/recursive-flow/
- name: Redis
  url: https://prismatic.io/connectors/redis/
- name: Result Placeholder
  url: https://prismatic.io/connectors/result-placeholder/
- name: Rippling
  url: https://prismatic.io/connectors/rippling/
- name: Sage 200
  url: https://prismatic.io/connectors/sage-200/
- name: Sage Accounting
  url: https://prismatic.io/connectors/sage/
- name: Sage HR
  url: https://prismatic.io/connectors/sage-hr/
- name: Sage Intacct
  url: https://prismatic.io/connectors/sage-intacct/
- name: Salesforce
  url: https://prismatic.io/connectors/salesforce/
- name: SAP Business One
  url: https://prismatic.io/connectors/sap-business-one/
- name: SAP S/4HANA Cloud
  url: https://prismatic.io/connectors/sapS4Hana/
- name: SAP SuccessFactors
  url: https://prismatic.io/connectors/sap-successfactors/
- name: Schedule Trigger
  url: https://prismatic.io/connectors/schedule-triggers/
- name: Segment
  url: https://prismatic.io/connectors/segment/
- name: SendGrid
  url: https://prismatic.io/connectors/sendgrid/
- name: ServiceDesk Plus
  url: https://prismatic.io/connectors/servicedesk-plus/
- name: ServiceNow
  url: https://prismatic.io/connectors/servicenow/
- name: ServiceTitan
  url: https://prismatic.io/connectors/servicetitan/
- name: SFTP
  url: https://prismatic.io/connectors/sftp/
- name: ShipBob
  url: https://prismatic.io/connectors/shipbob/
- name: ShipStation
  url: https://prismatic.io/connectors/shipstation/
- name: Shopify
  url: https://prismatic.io/connectors/shopify/
- name: Slack
  url: https://prismatic.io/connectors/slack/
- name: Sleep
  url: https://prismatic.io/connectors/sleep/
- name: Smartsheet
  url: https://prismatic.io/connectors/smartsheet/
- name: SMTP
  url: https://prismatic.io/connectors/smtp/
- name: Snowflake
  url: https://prismatic.io/connectors/snowflake/
- name: SOAP
  url: https://prismatic.io/connectors/soap/
- name: Square
  url: https://prismatic.io/connectors/square/
- name: Stop Execution
  url: https://prismatic.io/connectors/stop-execution/
- name: Stripe
  url: https://prismatic.io/connectors/stripe/
- name: Tableau
  url: https://prismatic.io/connectors/tableau/
- name: TeamViewer
  url: https://prismatic.io/connectors/teamviewer/
- name: Tenable Vulnerability Management
  url: https://prismatic.io/connectors/tenable-vulnerability-management/
- name: Text Manipulation
  url: https://prismatic.io/connectors/text-manipulation/
- name: Toast
  url: https://prismatic.io/connectors/toast/
- name: Twilio
  url: https://prismatic.io/connectors/twilio/
- name: Typeform
  url: https://prismatic.io/connectors/typeform/
- name: Universal Webhook
  url: https://prismatic.io/connectors/webhook-triggers/
- name: UUID
  url: https://prismatic.io/connectors/uuid/
- name: WhatsApp
  url: https://prismatic.io/connectors/whatsapp/
- name: WooCommerce
  url: https://prismatic.io/connectors/woo-commerce/
- name: Workday (Beta)
  url: https://prismatic.io/connectors/workday/
- name: Xero
  url: https://prismatic.io/connectors/xero/
- name: Yoti Sign
  url: https://prismatic.io/connectors/yoti-sign/
- name: Zendesk
  url: https://prismatic.io/connectors/zendesk/
- name: Zendesk Sell
  url: https://prismatic.io/connectors/zendesk-sell/
- name: Zip
  url: https://prismatic.io/connectors/zip/
- name: Zoho
  url: https://prismatic.io/connectors/zoho/
- name: Zoom
  url: https://prismatic.io/connectors/zoom/
json_schemas:
- name: Prismatic Alert Monitor
  property_count: 11
  slug: alert-monitor
- name: Prismatic Component
  property_count: 15
  slug: component
- name: Prismatic Config Variable
  property_count: 11
  slug: config-variable
- name: Prismatic Customer
  property_count: 9
  slug: customer
- name: Prismatic Execution
  property_count: 9
  slug: execution
- name: Prismatic Flow
  property_count: 12
  slug: flow
- name: Prismatic Instance
  property_count: 14
  slug: instance
- name: Prismatic Integration
  property_count: 14
  slug: integration
- name: Prismatic User
  property_count: 9
  slug: user
json_structures:
- name: Component
  property_count: 0
  slug: component
- name: Customer
  property_count: 0
  slug: customer
- name: Flow
  property_count: 0
  slug: flow
- name: Instance
  property_count: 0
  slug: instance
- name: Integration
  property_count: 0
  slug: integration
jsonld:
- class_count: 2
  name: Prismatic Context
  property_count: 11
  slug: prismatic-context
layout: provider
modified: '2026-05-22'
name: Prismatic
nav: Providers
network: true
overview: 'Prismatic publishes 2 APIs on the [APIs.io](https://apis.io/) network: Prismatics GraphQL API and Authentication API. Tagged areas include Embedded iPaaS, Integrations, Workflows, Connectors, and AI Agents.


  The Prismatic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Prismatic''s developer surface includes authentication, documentation, getting-started guide, CLI, changelog, engineering blog, pricing, and 38 more developer resources.'
plans:
- name: Prismatic Plans Pricing
  plan_count: 3
  slug: prismatic-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Prismatic Rate Limits
  slug: prismatic-rate-limits
rules:
- name: Prismatic API Rules
  rule_count: 16
  severity_counts:
    error: 6
    hint: 2
    info: 0
    warn: 8
  slug: prismatic-graphql-api-rules
- name: Prismatic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: prismatic-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.6
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.0
    developer_ergonomics: 58.7
    discoverability: 60.0
    governance: 26.3
    operational_transparency: 78.9
  previous_composite: 62.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prismatic/refs/heads/main/screenshots/prismatic-2026-06-20T192113.png
security:
- kind: authentication
  name: Prismatic Authentication
  slug: prismatic-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Prismatic Domain Security
  slug: prismatic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prismatic Vulnerability Disclosure
  slug: prismatic-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 8
skills:
- name: boomi-migration
  slug: boomi-migration
- name: component-patterns
  slug: component-patterns
- name: cyclr-migration
  slug: cyclr-migration
- name: embedded-patterns
  slug: embedded-patterns
- name: integration-patterns
  slug: integration-patterns
- name: migration-framework
  slug: migration-framework
- name: prismatic-api
  slug: prismatic-api
- name: prismatic-docs
  slug: prismatic-docs
slug: prismatic
tags:
- Embedded iPaaS
- Integrations
- Workflows
- Connectors
- AI Agents
- MCP
- Code-Native
- Low-Code
website: https://prismatic.io
---

---
aid: stackone
url: https://raw.githubusercontent.com/api-evangelist/stackone/refs/heads/main/apis.yml
apis:
  - aid: stackone:stackone
    name: StackOne
    tags:
      - Integrations
      - iPaaS
    humanURL: https://www.stackone.com/
    properties:
      - url: https://www.stackone.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/stackone/refs/heads/main/openapi/stackone-openapi.yml
        type: OpenAPI
    description: 'One integration platform, two powerful interfaces: Unified APIs for SaaS products, and AI Agent Actions. Ship hundreds of integrations in days.'
  - aid: stackone:hris-api
    name: StackOne Unified HRIS API
    tags:
      - Employees
      - HRIS
      - Human Resources
      - Unified API
    humanURL: https://docs.stackone.com/hris/introduction
    properties:
      - url: https://docs.stackone.com/hris/introduction
        type: Documentation
      - url: https://docs.stackone.com/hris/api-reference/employees/list-employees
        type: APIReference
    description: StackOne Unified HRIS API provides a single, standardized interface to interact with multiple HR information system providers, normalizing data models for employee data, shifts, time-off, documents, and benefits across platforms.
  - aid: stackone:ats-api
    name: StackOne Unified ATS API
    tags:
      - Applicant Tracking
      - ATS
      - Recruitment
      - Unified API
    humanURL: https://docs.stackone.com/ats/introduction
    properties:
      - url: https://docs.stackone.com/ats/introduction
        type: Documentation
      - url: https://docs.stackone.com/ats/api-reference/jobs/list-jobs
        type: APIReference
    description: StackOne Unified ATS API standardizes recruitment workflows across applicant tracking system providers, providing consistent data models for candidates, job postings, applications, and hiring pipeline management.
  - aid: stackone:crm-api
    name: StackOne Unified CRM API
    tags:
      - Contacts
      - CRM
      - Customer Relationship Management
      - Unified API
    humanURL: https://docs.stackone.com/crm/introduction
    properties:
      - url: https://docs.stackone.com/crm/introduction
        type: Documentation
      - url: https://docs.stackone.com/crm/api-reference/contacts/creates-a-new-contact
        type: APIReference
    description: StackOne Unified CRM API provides a standardized interface for managing customer contacts, accounts, and opportunities across multiple CRM platforms, ensuring a consistent view of customer data.
  - aid: stackone:lms-api
    name: StackOne Unified LMS API
    tags:
      - Courses
      - Learning Management
      - LMS
      - Unified API
    humanURL: https://docs.stackone.com/lms/introduction
    properties:
      - url: https://docs.stackone.com/lms/introduction
        type: Documentation
    description: StackOne Unified LMS API standardizes learning management across platforms, streamlining course delivery, user progress tracking, content management, and assignments with consistent data models across LMS and learning content providers.
  - aid: stackone:iam-api
    name: StackOne Unified IAM API
    tags:
      - Access Management
      - IAM
      - Identity
      - Unified API
    humanURL: https://docs.stackone.com/iam/introduction
    properties:
      - url: https://docs.stackone.com/iam/introduction
        type: Documentation
    description: StackOne Unified IAM API provides a standardized interface for identity and access management across providers, with comprehensive user management, role and permission mapping, group management, and resource access control.
  - aid: stackone:documents-api
    name: StackOne Unified Documents API
    tags:
      - Documents
      - Files
      - Knowledge Management
      - Unified API
    humanURL: https://docs.stackone.com/documents/introduction
    properties:
      - url: https://docs.stackone.com/documents/introduction
        type: Documentation
    description: StackOne Unified Documents API provides a standardized interface for file and knowledge management across platforms like Google Drive, SharePoint, Dropbox, and Box, with consistent data models for drives, folders, and documents.
  - aid: stackone:marketing-api
    name: StackOne Unified Marketing API
    tags:
      - Campaigns
      - Email
      - Marketing
      - SMS
      - Unified API
    humanURL: https://docs.stackone.com/marketing/introduction
    properties:
      - url: https://docs.stackone.com/marketing/introduction
        type: Documentation
    description: StackOne Unified Marketing API standardizes campaign management across platforms, streamlining messages (SMS, Email, Push), campaigns, templates, and more with consistent endpoints across marketing automation providers.
  - aid: stackone:ticketing-api
    name: StackOne Unified Ticketing API
    tags:
      - Helpdesk
      - Support
      - Ticketing
      - Unified API
    humanURL: https://docs.stackone.com/ticketing/introduction
    properties:
      - url: https://docs.stackone.com/ticketing/introduction
        type: Documentation
    description: StackOne Unified Ticketing API standardizes support workflows across helpdesk platforms, with consistent data models for ticket management, comments, and status tracking.
  - aid: stackone:messaging-api
    name: StackOne Unified Messaging API
    tags:
      - Chat
      - Communication
      - Messaging
      - Unified API
    humanURL: https://docs.stackone.com/messaging/introduction
    properties:
      - url: https://docs.stackone.com/messaging/introduction
        type: Documentation
    description: StackOne Unified Messaging API standardizes communication workflows across platforms, with consistent data models for conversations, message delivery, and participant management.
  - aid: stackone:screening-api
    name: StackOne Unified Screening API
    tags:
      - Assessments
      - Background Checks
      - Screening
      - Unified API
    humanURL: https://docs.stackone.com/screening/introduction
    properties:
      - url: https://docs.stackone.com/screening/introduction
        type: Documentation
    description: StackOne Unified Screening API standardizes candidate verification across platforms, streamlining background checks, assessments, and screening workflows with consistent data models.
  - aid: stackone:platform-api
    name: StackOne Platform API
    tags:
      - Accounts
      - Actions
      - Administration
      - Platform
    humanURL: https://docs.stackone.com/reference/getting-started-with-your-api
    properties:
      - url: https://docs.stackone.com/reference/getting-started-with-your-api
        type: Documentation
    description: StackOne Platform API serves as the control plane for managing accounts, executing actions, controlling integrations, discovering connectors, monitoring and debugging via logs, and proxy requests across StackOne projects and AI agents.
name: StackOne
tags:
  - Integrations
  - iPaaS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/StackOneHQ
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://www.stackone.com/
    name: StackOne | The Universal Integration Layer for Modern Products
    type: Website
    description: 'null'
  - url: https://www.stackone.com/case-studies
    name: Case Studies - Learn Why Product Teams Love Building with StackOne
    type: CaseStudies
    description: 'null'
  - url: https://www.stackone.com/blog
    name: Blog - The Knowledge Hub for Unified APIs & Integration Expertise
    type: Blog
    description: 'null'
  - url: https://www.stackone.com/changelog
    name: Changelog - Whats New?
    type: ChangeLog
    description: 'null'
  - url: https://www.stackone.com/events
    name: Events - Upcoming Events at StackOne
    type: Events
    description: 'null'
  - url: https://docs.stackone.com/guides/stackone-basics
    name: StackOne Basics - Stackone
    type: Documentation
    description: 'null'
  - url: https://docs.stackone.com/agents/guides/getting-started
    name: Getting Started - Stackone
    type: GettingStarted
    description: 'null'
  - url: https://www.stackone.com/company
    name: Company - We Fuel Innovation by Connecting Software
    type: About
    description: 'null'
  - url: https://www.stackone.com/pricing/
    name: Pricing & Plans
    type: Pricing
    description: 'null'
  - url: https://status.stackone.com/
    name: StackOne Status
    type: StatusPage
    description: 'null'
  - url: https://app.stackone.com/
    name: StackOne Dashboard
    type: Login
    description: 'null'
  - url: https://www.stackone.com/partners
    name: Partners
    type: Partners
    description: 'null'
  - url: https://www.stackone.com/integrations
    name: Integrations - 200+ Integrations Through One API
    type: IntegrationCatalog
    description: 'null'
  - url: https://www.linkedin.com/company/stackonehq/
    name: StackOne on LinkedIn
    type: LinkedIn
    description: 'null'
  - url: https://x.com/StackOneHQ
    name: StackOne on X
    type: X
    description: 'null'
  - url: https://docs.stackone.com/guides/stackone-api-sdks
    name: StackOne API SDKs
    type: SDKs
    description: 'null'
  - url: https://github.com/StackOneHQ/stackone-client-typescript
    name: StackOne TypeScript SDK
    type: SDKTypeScript
    description: 'null'
  - url: https://github.com/StackOneHQ/stackone-ai-python
    name: StackOne Python AI SDK
    type: SDKPython
    description: 'null'
  - url: https://github.com/StackOneHQ/stackone-ai-node
    name: StackOne Node.js AI SDK
    type: SDKNode
    description: 'null'
  - url: https://github.com/StackOneHQ/stackone-client-ruby
    name: StackOne Ruby SDK
    type: SDKRuby
    description: 'null'
  - url: https://github.com/StackOneHQ/stackone-client-java
    name: StackOne Java SDK
    type: SDKJava
    description: 'null'
  - url: https://github.com/stackoneHQ/stackone-client-php
    name: StackOne PHP SDK
    type: SDKPHP
    description: 'null'
  - url: https://github.com/StackOneHQ/stackone-client-csharp
    name: StackOne C# SDK
    type: SDKCSharp
    description: 'null'
  - url: https://www.npmjs.com/package/@stackone/stackone-client-ts
    name: StackOne TypeScript SDK on npm
    type: SDKPackage
    description: 'null'
  - url: https://rubygems.org/gems/stackone_client
    name: StackOne Ruby SDK on RubyGems
    type: SDKPackage
    description: 'null'
  - url: https://packagist.org/packages/stackone/client-sdk
    name: StackOne PHP SDK on Packagist
    type: SDKPackage
    description: 'null'
  - url: https://github.com/StackOneHQ/stackone-client-postman
    name: StackOne Postman Collection
    type: PostmanCollection
    description: 'null'
  - url: https://docs.stackone.com/mcp/quickstart
    name: StackOne MCP Server Quickstart
    type: MCPServers
    description: 'null'
  - url: https://docs.stackone.com/a2a/introduction
    name: StackOne A2A Protocol
    type: A2AProtocol
    description: 'null'
  - url: https://docs.stackone.com/agents/typescript/introduction
    name: StackOne TypeScript Toolset for AI Agents
    type: AIToolset
    description: 'null'
  - url: https://docs.stackone.com/agents/guides/openapi-tools
    name: StackOne OpenAPI Tools
    type: OpenAPI
    description: 'null'
  - url: https://hub.stackone.com/about
    name: StackOne Integration Hub
    type: IntegrationHub
    description: 'null'
  - url: https://docs.stackone.com/llms.txt
    name: StackOne llms.txt
    type: LLMsTxt
    description: 'null'
  - name: Features
    type: Features
    data:
      - name: Unified APIs
      - name: Platform APIs
      - name: Integration Hub
      - name: Authentication Links
      - name: API Keys
      - name: Request Logs
      - name: Webhooks
      - name: Manage Integrations
      - name: Manage Projects
      - name: Manage Organizations
      - name: Custom Unified Fields
      - name: Liberaries
      - name: SDKs
      - name: Advanced Parameters
      - name: Pagination
      - name: StackOne Identifiers
      - name: Rate Limiting
      - name: OpenAPI Tools
      - name: Tool Filtering
      - name: Artificial Intelligence
      - name: RAG
      - name: SLA Guaranteed Integrations
      - name: Native Webhooks
      - name: Synthetic Webhooks
      - name: Authentication UI
      - name: Multi-Region
      - name: Hybrid Deployment
      - name: No PII Stored
      - name: MCP Server
      - name: A2A Protocol
      - name: Actions API
      - name: Connector Builder
      - name: Proxy Requests
      - name: Sandbox Environments
  - name: Use Cases
    type: UseCases
    data:
      - name: AI Agents
      - name: People Tech
      - name: Recruitment
      - name: Learning
      - name: Assessment & Background Check
      - name: Global Employment
      - name: Benefits
      - name: Fintech
      - name: Security & Compliance
  - name: Integrations
    type: Integrations
    data:
      - name: 15five
      - name: IAM
      - name: 1Password
      - name: 360 Learning
      - name: Learning
      - name: ADP Workforce Now
      - name: HRIS
      - name: Aircall
      - name: Airship
      - name: Marketing
      - name: Ansible
      - name: Anthropic
      - name: Articulate
      - name: Asana
      - name: Ticketing
      - name: Ashby
      - name: ATS
      - name: Attio
      - name: CRM
      - name: Autodesk
      - name: Avature
      - name: BambooHR
      - name: Bitwarden
      - name: Box
      - name: Braze
      - name: Breathe
      - name: Breezy
      - name: Bullhorn
      - name: Canva
      - name: Cezanne HR
      - name: CharlieHR
      - name: CheckMK
      - name: ClearCompany Learning (fka Brainier)
      - name: Cloudways
      - name: Confluence
      - name: Documents
      - name: Contentful
      - name: Cornerstone
      - name: Coursera
      - name: DATEV
      - name: Databricks
      - name: Deel
      - name: Dialpad
      - name: Dixa
      - name: Docebo
      - name: Domo
      - name: Dropbox
      - name: Dropbox Sign
      - name: Duo
      - name: EasyLlama
      - name: Egnyte
      - name: Elastic
      - name: Employment Hero
      - name: Envoy
      - name: Eploy
      - name: Factorial
      - name: Fivetran
      - name: Freshsales
      - name: Freshteam
      - name: GitHub
      - name: Go1
      - name: Gong
      - name: Google Drive
      - name: Google Workspace
      - name: Greenhouse
      - name: Gusto
      - name: HR Cloud
      - name: HaileyHR
      - name: Harvest
      - name: Hibob
      - name: Hubspot CRM
      - name: Humaans
      - name: IRIS Cascade HR
      - name: Intercom
      - name: Ironclad
      - name: Iterable
      - name: JazzHR
      - name: JetBrains
      - name: Jira
      - name: Kameleoon
      - name: Klaviyo
      - name: Lacework
      - name: LastPass
      - name: Lattice
      - name: Leapsome
      - name: Lever
      - name: LinkedIn Learning
      - name: LogicMelon
      - name: Make
      - name: Matillion
      - name: MeisterTask
      - name: Mercury
      - name: Microsoft Dynamics 365
      - name: Mixpanel
      - name: MoEngage
      - name: NetSuite
      - name: Netlify
      - name: Notion
      - name: Okta
      - name: OneDrive
      - name: OneLogin
      - name: Oneflow
      - name: OpenAI
      - name: OpenVPN
      - name: Oracle Fusion
      - name: Oracle HCM
      - name: Oyster
      - name: Payfit
      - name: Personio
      - name: Pinpoint
      - name: Pipedrive
      - name: Planday
      - name: Qlik
      - name: Recruitee
      - name: Recruiterflow
      - name: Remote
      - name: Render
      - name: Retool
      - name: RingCentral
      - name: Rollbar
      - name: SAP SuccessFactors
      - name: Sage HR
      - name: Salesforce
      - name: Salesforce Marketing Cloud
      - name: Salesloft
      - name: Scaleway
      - name: Scoro
      - name: SendGrid
      - name: SharePoint
      - name: Slack
      - name: Messaging
      - name: SmartRecruiters
      - name: Smartsheet
      - name: SonarCloud
      - name: Sophos
      - name: Spendesk
      - name: SpotDraft
      - name: Staffology HR
      - name: Tableau
      - name: TalentLMS
      - name: TeamTailor
      - name: TeamViewer
      - name: Teamwork
      - name: Terraform
      - name: Thrive
      - name: Toggl
      - name: Twilio
      - name: UKG Pro
      - name: UKG Ready
      - name: Udemy
      - name: Vincere
      - name: WebEx
      - name: Webflow
      - name: Workable
      - name: Workday
      - name: Workday RAAS
      - name: Zelt
      - name: Azure DevOps
      - name: Early Access
      - name: GitHub Issues
      - name: Gmail
      - name: Google Calendar
      - name: HubSpot Ticketing
      - name: Teams
      - name: Trello
      - name: Zendesk
      - name: AFAS Software
      - name: Coming Soon
      - name: Abacus
      - name: Absorb
      - name: Accelo
      - name: Act
      - name: ActiveCampaign
      - name: Adobe
      - name: Adobe Marketo Engage
      - name: Affinity
      - name: Agile CRM
      - name: Amazon Redshift
      - name: DB
      - name: Apollo
      - name: Attensi
      - name: Attentive
      - name: Avada
      - name: Beekeeper
      - name: Blackbaud CRM
      - name: Bloomreach
      - name: Brevo
      - name: BrightHR
      - name: CATS
      - name: Capsule
      - name: ChartHop
      - name: CircleCI
      - name: Cisco Meraki
      - name: CleverTap
      - name: ClickUp
      - name: Clockwork Recruiting
      - name: Close
      - name: Collage
      - name: Comeet
      - name: Copper
      - name: Darwinbox
      - name: Datadog
      - name: Dayforce
      - name: Dotdigital
      - name: Drip
      - name: Elasticsearch
      - name: Emarsys
      - name: Encharge
      - name: EngageATS
      - name: EngageBay
      - name: Foundry Intent
      - name: Fountain
      - name: Gem
      - name: GetResponse
      - name: HR Duo
      - name: HR Partner
      - name: Hireology
      - name: Homerun
      - name: HubSpot Marketing
      - name: Humanforce
      - name: IFS
      - name: Infobip
      - name: Insider
      - name: Insightly
      - name: Insperity
      - name: Invision Community
      - name: JobAdder
      - name: JobDiva
      - name: JobDone
      - name: JobScore
      - name: Jobsoid
      - name: Jobvite
      - name: JustGiving
      - name: Justworks
      - name: Kallidus
      - name: Keap
      - name: Keka
      - name: LMS365
      - name: Linear
      - name: Listrak
      - name: Lucca
      - name: MHR
      - name: Mailchimp
      - name: Microsoft Dynamics 365
      - name: Accounting
      - name: Monday.com
      - name: MongoDB
      - name: MySQL
      - name: Namely
      - name: NeonCRM
      - name: Nimble
      - name: Nmbrs
      - name: Nutshell
      - name: Officient
      - name: Omnisend
      - name: OneSignal
      - name: Optimizely
      - name: Oracle Taleo
      - name: Outlook
      - name: Paychex
      - name: Paycom
      - name: Paycor
      - name: Paylocity
      - name: PeopleHR
      - name: Pinecone
      - name: Pipeliner
      - name: Polymer
      - name: PostgreSQL
      - name: Productboard
      - name: Proliant
      - name: Quickbooks Online
      - name: Recruitive
      - name: Rippling
      - name: Rydoo
      - name: SD Worx
      - name: Sage Intacct
      - name: Sales Impact Academy
      - name: Salesflare
      - name: Screenloop
      - name: Seismic
      - name: Sendinblue
      - name: ServiceNow
      - name: Sesame
      - name: SharpSpring
      - name: Shopify
      - name: Simployer
      - name: Skilljar
      - name: Snowflake
      - name: Splunk
      - name: Square Payroll
      - name: Stripe
      - name: SugarCRM
      - name: Supermetrics
      - name: SurveyMonkey
      - name: TalentLyft
      - name: Teamleader
      - name: Thryv
      - name: Travis CI
      - name: TriNet
      - name: Vendasta
      - name: Vibes
      - name: Vtiger
      - name: WebEngage
      - name: WhatsApp
      - name: Xero
      - name: Zendesk Sell
      - name: Zenefits
      - name: Zoho CRM
      - name: Zoho People
      - name: edrone
      - name: iCIMS
      - name: turbopuffer
created: '2025-06-05'
modified: '2026-03-16'
position: Consuming
segments:
  - iPaaS
description: StackOne is an AI-powered embedded integration platform as a service (iPaaS) designed to simplify and accelerate how SaaS vendors and AI agents connect with enterprise software. It combines a proprietary LLM-based agent with a real-time execution engine to automate and manage integrations no need for manual API wiring or data syncing.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---

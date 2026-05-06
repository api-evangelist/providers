---
aid: tray-ai
url: https://raw.githubusercontent.com/api-evangelist/tray-ai/refs/heads/main/apis.yml
apis:
  - aid: tray-ai:embedded-api
    name: Tray.ai Embedded API
    tags:
      - Automation
      - Embedded
      - GraphQL
      - Integration
    humanURL: https://developer.tray.ai/openapi/embeddedapi-introduction/
    baseURL: https://tray.io/graphql
    properties:
      - url: https://developer.tray.ai/openapi/embeddedapi-introduction/
        type: Documentation
      - url: openapi/tray-ai-embedded-api-openapi.yml
        type: OpenAPI
      - url: https://www.postman.com/tray-docs/tray-io-s-public-workspace/collection/uo51x8u/tray-embedded-apis-graphql
        type: PostmanCollection
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/solution.json
        type: JSONSchema
      - url: json-schema/solution-instance.json
        type: JSONSchema
      - url: json-schema/authentication.json
        type: JSONSchema
      - url: json-ld/tray-ai-context.jsonld
        type: JSONLD
      - url: json-structure/tray-ai-solution-instance-structure.json
        type: JSONStructure
      - url: examples/tray-ai-create-solution-instance-example.json
        type: Example
      - url: capabilities/shared/embedded-api.yaml
        type: NaftikoCapability
    description: The Tray.ai Embedded API is a GraphQL-based API that allows partners and customers to present in-app embedded integration experiences. It provides programmatic access to manage users, solutions, solution instances, authentications, workflows, and connector operations via HTTP POST to the GraphQL endpoint with Bearer token authentication.
  - aid: tray-ai:platform-api
    name: Tray.ai Platform API
    tags:
      - Automation
      - Connectors
      - Integration
      - iPaaS
    humanURL: https://developer.tray.ai/openapi/trayapi/overview/
    baseURL: https://api.tray.io/core/v1
    properties:
      - url: https://developer.tray.ai/openapi/trayapi/overview/
        type: Documentation
      - url: openapi/tray-ai-platform-api-openapi.yml
        type: OpenAPI
      - url: json-schema/connector.json
        type: JSONSchema
      - url: json-schema/authentication.json
        type: JSONSchema
      - url: json-schema/subscription.json
        type: JSONSchema
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/workspace.json
        type: JSONSchema
      - url: json-ld/tray-ai-context.jsonld
        type: JSONLD
      - url: json-structure/tray-ai-connector-structure.json
        type: JSONStructure
      - url: examples/tray-ai-list-connectors-example.json
        type: Example
      - url: examples/tray-ai-call-connector-example.json
        type: Example
      - url: examples/tray-ai-create-authentication-example.json
        type: Example
      - url: rules/tray-ai-rules.yml
        type: SpectralRuleset
      - url: capabilities/shared/platform-api.yaml
        type: NaftikoCapability
    description: The Tray.ai Platform API (also known as the Connectivity API) provides direct programmatic REST access to Tray's 700+ pre-built service connectors, authentication management, trigger subscriptions, user and workspace administration, and project/solution lifecycle operations. It enables developers to integrate third-party service operations into their own applications without using the Builder UI.
name: Tray.ai
tags:
  - Automation
  - Integration
  - iPaaS
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-06-05'
modified: '2026-05-03'
position: Consumer
description: Tray.ai is an AI-ready integration and automation platform that helps enterprises connect systems, teams, and data. It provides 700+ pre-built connectors, a visual workflow builder, embedded integration capabilities, and programmatic APIs for building and managing integrations at scale.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Tray.ai Integration Automation Capability
    url: capabilities/integration-automation.yaml
    type: NaftikoCapability
  - name: Tray.ai Vocabulary
    url: vocabulary/tray-ai-vocabulary.yml
    type: Vocabulary
  - name: Tray.ai Pricing | Compare AI agent & iPaaS plans
    description: 'null'
    url: https://tray.ai/packages
    type: Plans
  - name: Connector Hub
    description: 'null'
    url: https://tray.ai/connectors?sort=alphabetical
    type: Integrations
  - name: Tray.ai | Login
    data:
      - name: Acuity Scheduling
      - name: Adobe Experience Manager
      - name: Airtable
      - name: Alteryx
      - name: Anthropic
      - name: ArcGIS
      - name: Asana
      - name: Atlassian Confluence
      - name: Attentive Mobile
      - name: AWS Bedrock
      - name: AWS SageMaker
      - name: Basecamp 2
      - name: Box
      - name: Bynder
      - name: Calendly
      - name: Cisco Webex
      - name: ClickUp
      - name: Coda
      - name: Cohere
      - name: Contentsquare Metrics API
      - name: DocRaptor
      - name: DocuSign
      - name: Domo
      - name: Drift
      - name: Dropbox
      - name: FirstRain
      - name: Float
      - name: Formstack
      - name: Front
      - name: G Suite
      - name: Getty
      - name: Giphy
      - name: Gmail
      - name: Google Calendar
      - name: Google Chat
      - name: Google Contacts
      - name: Google Docs
      - name: Google Drive
      - name: Google Maps
      - name: Google Sheets
      - name: Google Slides
      - name: Google Tasks
      - name: Google Vision
      - name: GoTo Meeting
      - name: GoTo Webinar
      - name: Harvest
      - name: HelloSign
      - name: Hive
      - name: Huddle
      - name: Hunter
      - name: iContact
      - name: Intercom
      - name: iOffice
      - name: Jira
      - name: Jive
      - name: Jotform
      - name: Kapost
      - name: Keatext
      - name: Keen IO
      - name: Kickbox
      - name: LivePerson
      - name: Looker
      - name: MessageBird
      - name: Microsoft Calendar
      - name: Microsoft OneDrive
      - name: Microsoft Outlook
      - name: Microsoft Power BI
      - name: Microsoft Sharepoint
      - name: Microsoft Teams
      - name: Monday
      - name: MongoDB Cloud
      - name: NewsCred
      - name: Nexmo
      - name: Nimble
      - name: Notion
      - name: Ooma
      - name: OpenAI
      - name: OptimoRoute
      - name: Oracle Bronto
      - name: Oracle Responsys
      - name: Oxford Dictionaries
      - name: PandaDoc
      - name: Paymo
      - name: Pinecone
      - name: Plivo
      - name: Qlik
      - name: RingCentral
      - name: Ringover
      - name: ruum by SAP
      - name: Salesforce
      - name: Samsara
      - name: Scoop
      - name: SearchBlox
      - name: Sedna
      - name: Sitecore
      - name: Slack
      - name: Smartsheet
      - name: Sprinklr
      - name: Teamwork
      - name: Toggl
      - name: Trello
      - name: Twilio
      - name: Typeform
      - name: Uberflip
      - name: Unbounce
      - name: Vbrick
      - name: VideoAsk
      - name: Vonage
      - name: WordPress
      - name: Workfront
      - name: Workplace by Facebook
      - name: Workstack
      - name: Wrike
      - name: Wufoo
      - name: Wunderlist
      - name: Xverify
      - name: Yammer
      - name: Yodiz
      - name: Zendesk
      - name: Zoom
      - name: ZoomInfo
    url: https://app.tray.io/login
    type: Login
  - name: Blogs - All
    description: 'null'
    url: https://tray.ai/blog
    type: Blog
  - name: Customers
    description: 'null'
    url: https://tray.ai/customers
    type: CaseStudies
  - name: Privacy Policy
    description: 'null'
    url: https://tray.ai/privacy
    type: PrivacyPolicy
  - name: Master Subscription Agreement
    description: 'null'
    url: https://tray.ai/terms
    type: TermsOfService
  - name: Tray.ai Status
    description: 'null'
    url: https://status.tray.ai/
    type: Status
  - name: AI-ready integration & automation platform
    description: 'null'
    url: https://tray.ai/
    type: Website
  - name: Developer Portal
    description: 'null'
    url: https://developer.tray.ai/
    type: Portal
  - name: Use Cases
    type: UseCases
    data:
      - name: E-commerce
      - name: Embedded integrations
      - name: IT Onboarding
      - name: Lead lifecycle
      - name: Order-to-cash
  - name: Features
    type: Features
    data:
      - name: 600+ Connectors
      - name: Account Audit Log Streaming
      - name: Advanced On-Prem
      - name: All Packages Include
      - name: Auth API
      - name: Auth Collector
      - name: Composable Templates
      - name: Connectivity API
      - name: Connector Builder
      - name: Connector Development Kit (Sdk)
      - name: Customer Success Resources
      - name: Dedicated Slack Channel
      - name: Embedded Bundle
      - name: HIPAA
      - name: In-App Support
      - name: Insights
      - name: Intelligent Document Processing
      - name: Live Workshops
      - name: Log Retention
      - name: Log Streaming
      - name: Management API
      - name: Merlin Build
      - name: Multi-Factor Authentication
      - name: No Log Retention
      - name: Regional Hosting
      - name: Role-Based Access Control
      - name: SSO
      - name: Starter Task Credit
      - name: Static IP for On-Prem
      - name: Support
      - name: Tray Academy
      - name: Tray Advantage
      - name: Tray Advantage Plus
      - name: Tray Community
      - name: Trigger API
      - name: Usage
      - name: User Interfaces
      - name: Workflows
      - name: Workspaces
---

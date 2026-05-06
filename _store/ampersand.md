---
aid: ampersand
url: https://raw.githubusercontent.com/api-evangelist/ampersand/refs/heads/main/apis.yml
name: Ampersand
description: Ampersand is a developer-first platform for building native SaaS integrations. It provides an embeddable UI component and managed infrastructure that lets developers add product integrations quickly, handling OAuth, data sync, webhooks, and field mapping out of the box. The platform supports hundreds of SaaS connectors including Salesforce, HubSpot, Marketo, Microsoft Dynamics 365, Zendesk, and Gong with bi-directional sync and declarative configuration.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Tools
  - Integrations
  - Platform
  - SaaS
  - OAuth
  - Data Sync
  - Webhooks
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: ampersand:ampersand-api
    name: Ampersand API
    description: The Ampersand API enables developers to programmatically manage integrations, connections, installations, destinations, and data flows for SaaS-to-SaaS connectivity. It provides endpoints for managing installations, connections, destinations, API keys, projects, organizations, providers, and integration configurations within the Ampersand platform.
    humanURL: https://docs.withampersand.com/
    baseURL: https://api.withampersand.com
    tags:
      - Integrations
      - Platform
      - SaaS
      - OAuth
      - Data Sync
    properties:
      - type: Documentation
        url: https://docs.withampersand.com/
      - type: GettingStarted
        url: https://docs.withampersand.com/getting-started
      - type: Authentication
        url: https://docs.withampersand.com/reference/authentication
      - type: OpenAPI
        url: openapi/ampersand-api-openapi-original.yml
common:
  - type: Website
    url: https://www.withampersand.com/
  - type: Documentation
    url: https://docs.withampersand.com/
  - type: GitHubOrganization
    url: https://github.com/amp-labs
  - type: Blog
    url: https://www.withampersand.com/blog
  - type: SignUp
    url: https://dashboard.withampersand.com/sign-up
  - type: Login
    url: https://dashboard.withampersand.com/sign-in
  - type: SDK
    url: https://www.npmjs.com/package/@amp-labs/react
    title: React UI SDK
  - type: CLI
    url: https://github.com/amp-labs/cli
  - type: SpectralRules
    url: rules/ampersand-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/ampersand-api.yaml
  - type: NaftikoCapability
    url: capabilities/integration-management.yaml
  - type: JSONLD
    url: json-ld/ampersand-api-context.jsonld
  - type: Vocabulary
    url: vocabulary/ampersand-vocabulary.yaml
  - type: Features
    data:
      - name: Declarative Integration Framework
        description: Code-based, composable integration building that is version-controllable and CI/CD compatible for professional engineering workflows.
      - name: Managed OAuth Authentication
        description: Free auth token management with auto-refresh for all supported SaaS providers, eliminating OAuth complexity from product teams.
      - name: Bi-directional Data Sync
        description: On-demand read/write operations, scheduled reads, and bulk write capabilities for synchronizing data between SaaS applications.
      - name: Proxy API
        description: Authenticated passthrough requests to customer systems enabling direct API calls without managing OAuth tokens.
      - name: Backfill Support
        description: Historical data retrieval during customer onboarding to populate integrations with existing customer data.
      - name: DevOps Infrastructure
        description: Automated retries, error handling, quota management, detailed logging, and alerting for production-grade integration reliability.
      - name: Custom Objects and Fields
        description: Support for custom objects and fields allowing customers to configure integrations without being constrained by inflexible unified APIs.
      - name: Embeddable UI Components
        description: React UI library with pre-built integration setup flows enabling customers to configure their own SaaS connections within your product.
      - name: AI SDK
        description: Official AI SDK enabling AI agents to read from and write to SaaS applications through natural language via Ampersand integrations.
  - type: UseCases
    data:
      - name: CRM Integration
        description: Build native Salesforce, HubSpot, and Dynamics 365 integrations to sync customer data bidirectionally with your SaaS product.
      - name: Marketing Automation Integration
        description: Connect Marketo, HubSpot, and other marketing platforms to enable customer data flows for campaign automation and lead management.
      - name: Customer Support Integration
        description: Integrate Zendesk and other support platforms to sync tickets, contacts, and customer data with your application.
      - name: Conversation Intelligence Integration
        description: Connect Gong and other conversation platforms to access call recordings, transcripts, and insights within your application.
      - name: AI Agent Integration
        description: Enable AI agents to read from and write to customer SaaS systems through the Ampersand AI SDK for autonomous workflow automation.
      - name: Developer Portal Embedding
        description: Embed Ampersand's React UI components into your product so customers can self-service configure their own SaaS integrations.
  - type: Integrations
    data:
      - name: Salesforce
        description: Bi-directional CRM integration with Salesforce for contacts, accounts, opportunities, and custom objects.
      - name: HubSpot
        description: CRM and marketing automation integration with HubSpot for contacts, deals, companies, and email tracking.
      - name: Marketo
        description: Marketing automation integration with Marketo for lead management, campaigns, and activity data.
      - name: Microsoft Dynamics 365
        description: CRM integration with Microsoft Dynamics 365 for enterprise sales and customer service workflows.
      - name: Zendesk
        description: Customer support integration with Zendesk for tickets, users, organizations, and support metrics.
      - name: Gong
        description: Conversation intelligence integration with Gong for call recordings, transcripts, and revenue insights.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

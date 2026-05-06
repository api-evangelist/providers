---
aid: activepieces
name: Activepieces
description: Activepieces is an open-source, no-code automation platform that enables users to streamline workflows by connecting various applications and automating tasks. It supports over 400 MCP servers and integrations, allowing developers to build custom TypeScript-based pieces. The platform offers AI agents, MCPs, and workflow automation capabilities with both cloud and self-hosted deployment options.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - No-Code
  - Open Source
  - Workflow
  - AI Agents
  - MCP
url: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: activepieces:activepieces-api
    name: Activepieces API
    tags:
      - Automation
      - Workflow
      - No-Code
    humanURL: https://www.activepieces.com/docs/endpoints/overview
    baseURL: https://cloud.activepieces.com/api/v1
    properties:
      - url: https://www.activepieces.com/docs/endpoints/overview
        type: Documentation
      - url: https://www.activepieces.com/docs/endpoints/overview
        type: APIReference
      - url: openapi/activepieces.json
        type: OpenAPI
      - url: json-schema/activepieces-flow-schema.json
        type: JSONSchema
        title: Flow
      - url: json-schema/activepieces-flow-run-schema.json
        type: JSONSchema
        title: Flow Run
      - url: json-schema/activepieces-connection-schema.json
        type: JSONSchema
        title: Connection
      - url: json-schema/activepieces-project-schema.json
        type: JSONSchema
        title: Project
      - url: json-structure/activepieces-flow-structure.json
        type: JSONStructure
        title: Flow
      - url: json-structure/activepieces-flow-run-structure.json
        type: JSONStructure
        title: Flow Run
      - url: examples/activepieces-flow-example.json
        type: Example
        title: Flow Example
      - url: examples/activepieces-flow-run-example.json
        type: Example
        title: Flow Run Example
    description: The Activepieces API provides programmatic access to the automation platform, enabling management of flows, connections, projects, users, folders, pieces, templates, and execution monitoring. Uses Bearer token authentication.
common:
  - type: Portal
    url: https://www.activepieces.com/
  - type: Documentation
    url: https://www.activepieces.com/docs/
  - type: GettingStarted
    url: https://www.activepieces.com/docs/getting-started/introduction
  - type: Authentication
    url: https://www.activepieces.com/docs/endpoints/overview
  - type: Pricing
    url: https://www.activepieces.com/pricing
  - type: GitHubOrganization
    url: https://github.com/activepieces
  - type: GitHubRepository
    url: https://github.com/activepieces/activepieces
  - type: StatusPage
    url: https://status.activepieces.com/
  - type: SpectralRules
    url: rules/activepieces-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/activepieces-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/activepieces.yaml
    title: Activepieces API Shared Definition
  - type: NaftikoCapability
    url: capabilities/workflow-automation.yaml
    title: Workflow Automation Capability
  - type: JSON-LD
    url: json-ld/activepieces-context.jsonld
    title: Activepieces Context
  - type: Features
    data:
      - name: Visual Flow Builder
        description: No-code drag-and-drop interface for building automation workflows with triggers and actions.
      - name: 400+ Integration Pieces
        description: Over 400 pre-built integrations (pieces) written in TypeScript, available as MCP servers for AI agents.
      - name: AI Agents
        description: Native AI agent creation and orchestration within automation workflows.
      - name: MCP Servers
        description: Every piece automatically becomes an MCP server for use with AI agents and LLMs like Claude.
      - name: Custom Pieces
        description: Build custom TypeScript-based integration pieces and publish them to npm.
      - name: Flow Versioning
        description: Version control for flows with publish/draft states and rollback capabilities.
      - name: Human-in-the-Loop
        description: Add approval steps, delays, and human decision points in automation workflows.
      - name: Self-Hosting
        description: Deploy on Docker, Kubernetes, AWS, GCP, or any cloud provider with full data control.
      - name: Git Sync
        description: Synchronize flows with Git repositories for version control and CI/CD integration.
      - name: Webhook Triggers
        description: Trigger flows via webhooks from any external system or service.
      - name: REST API
        description: Full programmatic access to manage flows, connections, projects, and execution history.
      - name: Flow Templates
        description: Share and reuse flow templates across projects and teams.
  - type: UseCases
    data:
      - name: Marketing Automation
        description: Automate lead capture, email sequences, and CRM updates from marketing platforms.
      - name: Sales Operations
        description: Sync contacts, deals, and activities between CRM, email, and communication tools.
      - name: Data Synchronization
        description: Keep data in sync across databases, spreadsheets, and SaaS applications.
      - name: AI Agent Orchestration
        description: Use Activepieces as an MCP server to give AI agents access to 400+ integrations.
      - name: IT Automation
        description: Automate user provisioning, notifications, and system integrations.
      - name: E-Commerce Operations
        description: Automate order processing, inventory updates, and customer notifications.
      - name: Developer Integration Platform
        description: Embed Activepieces as a white-label automation platform in SaaS products.
  - type: Integrations
    data:
      - name: GitHub
        description: Trigger workflows on GitHub events and automate repository operations.
      - name: Gmail
        description: Send emails, parse inbound mail, and automate email workflows.
      - name: Slack
        description: Send notifications, create channels, and respond to Slack events.
      - name: OpenAI
        description: Integrate GPT models for AI-powered automation and content generation.
      - name: Google Sheets
        description: Read and write data to Google Sheets for data synchronization workflows.
      - name: Airtable
        description: Sync records and trigger workflows from Airtable database changes.
      - name: Salesforce
        description: Create and update Salesforce records from automation workflows.
      - name: Stripe
        description: Trigger flows on payment events and automate billing operations.
  - type: Solutions
    data:
      - name: Community Edition
        description: Free, open-source self-hosted deployment with unlimited flows and no task limits.
      - name: Plus
        description: Cloud plan at $25/mo with 10 active flows, AI agents, and 500 AI credits.
      - name: Business
        description: Cloud plan at $150/mo with 50 active flows, team collaboration, and 1,000 AI credits.
      - name: Enterprise
        description: Custom pricing with unlimited flows, SSO, audit logs, and custom AI model support.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

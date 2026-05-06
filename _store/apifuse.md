---
aid: apifuse
name: Apifuse
description: Apifuse is a native integration platform that enables SaaS companies to build and embed integrations directly into their products. It provides a white-label integration solution with pre-built connectors across 20+ categories, an embeddable UI, workflow automation, and analytics tools that help developers add native integrations without building from scratch.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Embedded Integrations
  - Integration Platform
  - Integrations
  - iPaaS
  - Marketplace
  - SaaS
  - Workflow Automation
url: https://raw.githubusercontent.com/api-evangelist/apifuse/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apifuse:apifuse-api
    name: Apifuse API
    description: The Apifuse API enables developers to programmatically manage embedded integrations, connectors, workflows, and user authentication within their SaaS applications. Build and monitor native integration marketplaces with full programmatic control over the integration lifecycle.
    humanURL: https://apifuse.io/
    baseURL: https://api.apifuse.io
    tags:
      - Analytics
      - Connectors
      - Embedded Integrations
      - Integrations
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.apifuse.io/
      - type: GettingStarted
        url: https://docs.apifuse.io/getting-started
      - type: OpenAPI
        url: openapi/apifuse-api.yaml
      - type: Pricing
        url: https://apifuse.io/pricing
      - type: JSONSchema
        url: json-schema/apifuse-integration-schema.json
      - type: JSONSchema
        url: json-schema/apifuse-workflow-schema.json
      - type: JSONSchema
        url: json-schema/apifuse-connector-schema.json
      - type: JSONSchema
        url: json-schema/apifuse-analytics-schema.json
      - type: JSON-LD
        url: json-ld/apifuse-context.jsonld
common:
  - type: Website
    url: https://apifuse.io/
  - type: Documentation
    url: https://docs.apifuse.io/
  - type: GettingStarted
    url: https://docs.apifuse.io/getting-started
  - type: Pricing
    url: https://apifuse.io/pricing
  - type: Blog
    url: https://apifuse.io/blog
  - type: SignUp
    url: https://app.apifuse.io/register
  - type: Login
    url: https://app.apifuse.io/login
  - type: GitHubOrganization
    url: https://github.com/apifuse
  - type: Features
    data:
      - name: Embedded Integration Marketplace
        description: Build a branded integration marketplace within your SaaS product, allowing customers to connect their preferred business tools.
      - name: Pre-Built Connectors
        description: 150+ pre-built connectors across 20+ categories including CRM, Accounting, Email, Project Management, and more.
      - name: Workflow Builder
        description: Visual workflow builder with triggers (polling, realtime, scheduled, webhook) and steps (actions, conditionals, loops, delays, scripts).
      - name: White-Label Solution
        description: Fully white-labeled integration UI that embeds seamlessly into your product's look and feel.
      - name: Custom Connector SDK
        description: Build custom connectors for proprietary or internal systems using the Apifuse SDK.
      - name: Analytics and Monitoring
        description: Track integration usage, task counts, active users, and monitor workflow health in real time.
      - name: User Authentication
        description: Manage user OAuth connections, API keys, and integration authentication within your platform.
  - type: UseCases
    data:
      - name: SaaS Integration Marketplace
        description: Embed a branded integration marketplace into your SaaS product to let customers connect Salesforce, Mailchimp, DocuSign, and 150+ other tools.
      - name: Workflow Automation
        description: Allow customers to build no-code automation workflows between their connected apps and your platform.
      - name: Platform Expansion
        description: Transform a product into a comprehensive platform by adding native integration capabilities without building each connector from scratch.
      - name: Customer Data Sync
        description: Keep customer data synchronized across CRM, marketing automation, and your platform in real time.
  - type: Integrations
    data:
      - name: Salesforce
        description: CRM integration for managing leads, contacts, and opportunities.
      - name: Mailchimp
        description: Email marketing integration for campaign management and audience sync.
      - name: DocuSign
        description: E-signature integration for document workflow automation.
      - name: Slack
        description: Communication integration for notifications and workflow triggers.
      - name: QuickBooks
        description: Accounting integration for financial data synchronization.
      - name: HubSpot
        description: CRM and marketing automation integration.
  - type: Solutions
    data:
      - name: Growth Plan
        description: Up to 500,000 tasks/month with 6 pre-built connectors for companies starting with embedded integrations.
      - name: Platform Plan
        description: Up to 5,000,000 tasks/month with unlimited pre-built connectors for established SaaS companies.
      - name: Enterprise Plan
        description: Custom task volume, fully managed integrations, and dedicated support for enterprise SaaS platforms.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

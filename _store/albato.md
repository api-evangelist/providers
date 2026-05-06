---
aid: albato
url: https://raw.githubusercontent.com/api-evangelist/albato/refs/heads/main/apis.yml
name: Albato
tags:
  - No-Code Automation
  - Workflow Automation
  - Embedded iPaaS
  - App Integration
  - Integrations
  - Webhooks
  - White-Label
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
description: Albato is a no-code automation platform and embedded iPaaS that enables businesses to automate workflows by connecting 1,000+ apps without writing code. Supports multi-step automations with triggers, actions, conditions, and delays. Albato Embedded allows SaaS companies to offer white-label native integrations to their customers.
created: '2025-06-06'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: albato:automations-api
    name: Albato Automations API
    tags:
      - Automation
      - Workflow
      - No-Code
      - Executions
    properties:
      - url: https://albato.com
        type: Documentation
      - url: openapi/albato-automations-openapi.yaml
        type: OpenAPI
      - url: json-schema/albato-albato-automations-automation-schema.json
        type: JSONSchema
      - url: json-schema/albato-albato-automations-automation-step-schema.json
        type: JSONSchema
      - url: json-schema/albato-albato-automations-execution-schema.json
        type: JSONSchema
      - url: json-structure/albato-albato-automations-automation-structure.json
        type: JSONStructure
      - url: json-structure/albato-albato-automations-automation-step-structure.json
        type: JSONStructure
      - url: json-structure/albato-albato-automations-execution-structure.json
        type: JSONStructure
      - url: examples/albato-albato-automations-automation-example.json
        type: Example
      - url: examples/albato-albato-automations-automation-step-example.json
        type: Example
      - url: examples/albato-albato-automations-execution-example.json
        type: Example
    humanURL: https://albato.com
    baseURL: https://albato.com/api/v1
    description: REST API for managing multi-step automation workflows in Albato. Supports creating, enabling, disabling, and monitoring automation executions across 1,000+ connected apps.
  - aid: albato:embedded-api
    name: Albato Embedded API
    tags:
      - Embedded iPaaS
      - White-Label
      - Teams
      - Connectors
      - Templates
    properties:
      - url: https://albato.com/embedded
        type: Documentation
      - url: openapi/albato-embedded-openapi.yaml
        type: OpenAPI
      - url: json-schema/albato-albato-embedded-team-schema.json
        type: JSONSchema
      - url: json-schema/albato-albato-embedded-user-schema.json
        type: JSONSchema
      - url: json-schema/albato-albato-embedded-connector-schema.json
        type: JSONSchema
      - url: json-schema/albato-albato-embedded-template-schema.json
        type: JSONSchema
      - url: json-structure/albato-albato-embedded-team-structure.json
        type: JSONStructure
      - url: json-structure/albato-albato-embedded-user-structure.json
        type: JSONStructure
      - url: json-structure/albato-albato-embedded-connector-structure.json
        type: JSONStructure
      - url: json-structure/albato-albato-embedded-template-structure.json
        type: JSONStructure
      - url: examples/albato-albato-embedded-team-example.json
        type: Example
      - url: examples/albato-albato-embedded-user-example.json
        type: Example
      - url: examples/albato-albato-embedded-connector-example.json
        type: Example
      - url: examples/albato-albato-embedded-template-example.json
        type: Example
    humanURL: https://albato.com/embedded
    baseURL: https://albato.com/api/v1/embedded
    description: REST API for Albato Embedded iPaaS enabling SaaS companies to manage customer teams, app connectors, and automation templates for white-label integration delivery.
common:
  - url: https://albato.com
    type: Website
  - url: https://wiki.albato.com/en
    type: Documentation
  - url: https://albato.com/embedded
    type: GettingStarted
    title: Albato Embedded iPaaS
  - url: https://albato.com/pricing
    type: Pricing
  - url: https://albato.com/embedded/pricing
    type: Pricing
    title: Albato Embedded Pricing
  - url: https://albato.com/apps/all-integrations
    type: Integrations
    title: 1,000+ App Integrations
  - url: https://albato.com/blog/all
    type: Blog
  - url: https://albato.com/blog/case-studies
    type: CaseStudies
  - url: https://wiki.albato.com/en/collections/8343168-faq
    type: FAQ
  - url: https://albato.com/license
    type: Licensing
  - url: https://albato.com/privacy
    type: PrivacyPolicy
  - url: https://www.facebook.com/groups/albatocommunity
    type: FacebookGroup
  - url: https://roadmap.albato.com/public
    type: Roadmap
  - url: rules/albato-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/albato-vocabulary.yaml
    type: Vocabulary
  - url: json-ld/albato-albato-context.jsonld
    type: JSONLD
  - url: capabilities/shared/automations-api.yaml
    type: NaftikoCapability
    title: Albato Automations Shared Capability
  - url: capabilities/shared/embedded-api.yaml
    type: NaftikoCapability
    title: Albato Embedded Shared Capability
  - url: capabilities/ipaas-automation.yaml
    type: NaftikoCapability
    title: iPaaS Automation Workflow
  - type: Features
    data:
      - name: No-Code Automation Builder
        description: Visual automation builder for creating multi-step workflows connecting 1,000+ apps without writing code, with conditions, delays, and data transformations.
      - name: 1,000+ App Integrations
        description: Pre-built connectors for CRM, marketing, e-commerce, communication, and productivity apps including HubSpot, Salesforce, Google Workspace, Slack, Shopify, and more.
      - name: Albato Embedded iPaaS
        description: White-label integration platform for SaaS companies to embed Albato's automation capabilities natively in their products with full branding control.
      - name: Multi-Step Workflows
        description: Support for complex automations with sequential and conditional steps, delays, loops, and data transformations without coding.
      - name: Real-Time and Scheduled Triggers
        description: Webhook-based real-time triggers for instant event processing and scheduled polling triggers for API-based app integrations.
      - name: Custom App Integrator
        description: Build custom API connectors from any REST API using the App Integrator without development handoff, supporting all major auth methods.
      - name: Execution Monitoring
        description: Detailed execution history with step-level logging, success/error rates, real-time notifications, and dashboard insights.
      - name: Data Transformation
        description: Built-in data mapping, field transformation, and JavaScript code steps for processing data between connected apps.
  - type: UseCases
    data:
      - name: CRM and Marketing Automation
        description: Sync leads between CRM and marketing tools, automate email campaigns, and route prospects based on behavioral conditions.
      - name: E-Commerce Order Processing
        description: Automate order notifications, inventory updates, fulfillment triggers, and customer communication across e-commerce platforms.
      - name: SaaS Native Integration Delivery
        description: Use Albato Embedded to offer customers white-labeled integrations in your SaaS product without in-house iPaaS development.
      - name: Customer Support Automation
        description: Route tickets, trigger alerts, and sync customer data between helpdesk, CRM, and communication platforms automatically.
      - name: Data Synchronization
        description: Keep data consistent across business systems with bidirectional syncs, scheduled automations, and event-driven updates.
  - type: Integrations
    data:
      - name: HubSpot
        description: CRM and marketing automation for contact and deal management.
      - name: Salesforce
        description: Enterprise CRM for sales pipeline and opportunity workflows.
      - name: Google Workspace
        description: Google Sheets, Gmail, Drive, Calendar, and Forms integrations.
      - name: Slack
        description: Team messaging integration for workflow notifications and alerts.
      - name: Shopify
        description: E-commerce integration for order, product, and customer automation.
      - name: Stripe
        description: Payment processing integration for subscription and payment workflows.
      - name: Notion
        description: Workspace integration for task and project data synchronization.
      - name: Airtable
        description: Database integration for spreadsheet and grid data workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

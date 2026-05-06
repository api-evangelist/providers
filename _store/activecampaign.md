---
aid: activecampaign
url: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/apis.yml
apis:
  - aid: activecampaign:activecampaign-v3
    name: ActiveCampaign API v3
    tags:
      - Marketing Automation
      - CRM
      - Email Marketing
      - Contacts
      - Deals
    humanURL: https://developers.activecampaign.com/reference/overview
    baseURL: https://youraccountname.api-us1.com/api/3
    properties:
      - url: https://developers.activecampaign.com/reference/overview
        type: Documentation
      - url: https://developers.activecampaign.com/reference/authentication
        type: Authentication
      - url: openapi/activecampaign-v3.json
        type: OpenAPI
    description: The primary REST API for ActiveCampaign, organized around resources such as contacts, deals, accounts, automations, campaigns, messages, lists, tags, webhooks, custom objects, and ecommerce entities. Uses API key header authentication.
  - aid: activecampaign:activecampaign-sms
    name: ActiveCampaign SMS Broadcast API
    tags:
      - SMS
      - Marketing Automation
      - Messaging
    humanURL: https://developers.activecampaign.com/reference/overview
    baseURL: https://youraccountname.api-us1.com/api/3
    properties:
      - url: https://developers.activecampaign.com/reference/overview
        type: Documentation
      - url: openapi/activecampaign-sms.json
        type: OpenAPI
      - url: json-schema/activecampaign-sms-broadcast-message-schema.json
        type: JSONSchema
        title: Broadcast Message
      - url: json-schema/activecampaign-sms-broadcast-create-request-schema.json
        type: JSONSchema
        title: Broadcast Create Request
      - url: json-schema/activecampaign-sms-broadcast-update-request-schema.json
        type: JSONSchema
        title: Broadcast Update Request
      - url: json-schema/activecampaign-sms-broadcast-metrics-schema.json
        type: JSONSchema
        title: Broadcast Metrics
      - url: json-schema/activecampaign-sms-recipient-schema.json
        type: JSONSchema
        title: Recipient
      - url: json-schema/activecampaign-sms-credits-response-schema.json
        type: JSONSchema
        title: Credits Response
      - url: json-schema/activecampaign-sms-ai-broadcast-request-schema.json
        type: JSONSchema
        title: AI Broadcast Request
      - url: json-structure/activecampaign-sms-broadcast-message-structure.json
        type: JSONStructure
        title: Broadcast Message
      - url: json-structure/activecampaign-sms-recipient-structure.json
        type: JSONStructure
        title: Recipient
      - url: examples/activecampaign-sms-broadcast-message-example.json
        type: Example
        title: Broadcast Message Example
      - url: examples/activecampaign-sms-recipient-example.json
        type: Example
        title: Recipient Example
    description: API for managing SMS broadcasts, lists, metrics, and AI-powered content generation in ActiveCampaign. Supports creating, scheduling, and tracking SMS broadcast campaigns.
name: ActiveCampaign
tags:
  - Marketing Automation
  - Email Marketing
  - CRM
  - Sales Automation
  - Customer Experience
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://developers.activecampaign.com/
    type: Portal
  - url: https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API
    type: GettingStarted
  - url: https://developers.activecampaign.com/reference/authentication
    type: Authentication
  - url: https://www.activecampaign.com/pricing
    type: Pricing
  - url: https://www.activecampaign.com/blog
    type: Blog
  - url: https://www.activecampaign.com/about/faq
    type: FAQ
  - url: https://community.activecampaign.com/latest
    type: Forums
  - url: https://status.activecampaign.com/
    type: StatusPage
  - url: https://www.postman.com/acdevrel/activecampaign-developer-relations/overview
    type: PostmanWorkspace
  - url: https://github.com/ActiveCampaign
    type: GitHubOrganization
  - url: https://github.com/ActiveCampaign/activecampaign-api-php
    type: SDK
    title: PHP SDK
  - url: https://github.com/ActiveCampaign/activecampaign-api-nodejs
    type: SDK
    title: Node.js SDK
  - url: rules/activecampaign-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/activecampaign-vocabulary.yaml
    type: Vocabulary
  - url: capabilities/shared/activecampaign-v3.yaml
    type: NaftikoCapability
    title: ActiveCampaign API v3 Shared Definition
  - url: capabilities/marketing-automation.yaml
    type: NaftikoCapability
    title: Marketing Automation Workflow
  - url: capabilities/crm-sales.yaml
    type: NaftikoCapability
    title: CRM and Sales Workflow
  - url: json-ld/activecampaign-sms-context.jsonld
    type: JSON-LD
    title: SMS API Context
  - type: Features
    data:
      - name: Email Marketing
        description: Create and send conversion-focused email campaigns with personalization and segmentation.
      - name: Marketing Automation
        description: Build automated customer journeys and workflows triggered by contact behavior and events.
      - name: CRM
        description: Built-in sales CRM for managing deals, pipelines, tasks, and customer relationships.
      - name: SMS Marketing
        description: Reach contacts via SMS broadcast campaigns with AI-powered content generation.
      - name: WhatsApp Messaging
        description: Automate growth and customer engagement through WhatsApp communications.
      - name: Transactional Email
        description: Automate transactional alerts, password resets, and notifications via Postmark integration.
      - name: Custom Objects
        description: Create custom data schemas to activate complex data for segmentation and personalized automation.
      - name: Contact Event Tracking
        description: Track contact behaviors and activities across web properties and integrations.
      - name: Webhooks
        description: Receive real-time event notifications for contact, campaign, automation, and custom object activities.
      - name: Landing Pages
        description: Deploy conversion-ready landing pages for lead capture and campaigns.
      - name: Active Intelligence
        description: AI-powered orchestration and autonomous marketing agents for campaign suggestions and personalization.
      - name: MCP Server
        description: Connect AI applications to ActiveCampaign using the Model Context Protocol server.
  - type: UseCases
    data:
      - name: Lead Nurturing
        description: Automate email sequences to nurture leads through the sales funnel based on behavior.
      - name: E-Commerce Automation
        description: Trigger post-purchase emails, abandoned cart recovery, and personalized product recommendations.
      - name: Customer Onboarding
        description: Automate onboarding sequences for SaaS products to improve activation and retention.
      - name: Contact Segmentation
        description: Segment contacts using tags, custom fields, and custom objects for targeted campaigns.
      - name: Sales Pipeline Management
        description: Manage deals, tasks, and pipeline stages with CRM and automation integration.
      - name: SMS Broadcast Campaigns
        description: Send targeted SMS campaigns to subscriber lists with engagement tracking.
      - name: Webhook-Driven Integrations
        description: Build real-time integrations using webhooks for contact and campaign activity events.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync contact and deal data between ActiveCampaign and Salesforce CRM.
      - name: Zapier
        description: Connect ActiveCampaign to 1000+ apps via Zapier automation workflows.
      - name: Slack
        description: Send notifications and trigger automations from Slack using OAuth2 integration.
      - name: Calendly
        description: Sync scheduling data and trigger automations with custom objects via OAuth2.
      - name: Twilio
        description: Integrate SMS workflows using Twilio with Basic Auth for outbound messaging.
      - name: Shopify
        description: Sync ecommerce customers, orders, and products for automated campaigns.
      - name: WordPress
        description: Embed forms and capture leads from WordPress sites.
      - name: Wix
        description: Connect Wix websites for lead capture and customer journey automation.
  - type: Solutions
    data:
      - name: Starter
        description: Entry-level plan with marketing automation, up to 5 automation actions, and 1 user.
      - name: Plus
        description: Mid-tier plan with unlimited automation actions, landing pages, and standard segmentation.
      - name: Pro
        description: Advanced plan with predictive content, advanced segmentation, and 3 users.
      - name: Enterprise
        description: Full-featured plan with custom objects, dedicated account team, and premium segmentation.
created: '2025-02-17'
modified: '2026-04-19'
position: Consumer
description: ActiveCampaign is a leading marketing automation platform that helps businesses of all sizes seamlessly engage with their customers. With its user-friendly interface and powerful features, ActiveCampaign allows businesses to create personalized email campaigns, automate workflows, and track customer interactions in real-time. The platform offers a REST API (v3), SMS Broadcast API, webhooks, and custom object schemas for building deep integrations and automations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---

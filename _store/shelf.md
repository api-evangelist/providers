---
aid: shelf
url: https://raw.githubusercontent.com/api-evangelist/shelf/refs/heads/main/apis.yml
apis:
  - aid: shelf:shelf-rest-api
    name: Shelf REST API
    tags:
      - Artificial Intelligence
      - Knowledge Management
      - REST
      - Search
    humanURL: https://shelf.io/technology/
    properties:
      - url: https://shelf.io/technology/
        type: Documentation
      - url: https://help.shelf.io/technical-guidelines-10162c4f
        type: GettingStarted
      - url: https://help.shelf.io/technical-guidelines-10162c4f/shelf-api-token-feature-introductory-guide-aac2ec62
        type: Authentication
    description: The Shelf REST API enables developers to programmatically interact with the Shelf knowledge management platform. Access, search, create, and manage knowledge articles, gems (curated content), decision trees, and user permissions. Supports regional endpoints for US (api.shelf.io), Canada (api.shelf-ca.com), and Europe (api.shelf-eu.com).
  - aid: shelf:shelf-content-intelligence-api
    name: Shelf Content Intelligence API
    tags:
      - Artificial Intelligence
      - Content
      - Knowledge Management
      - Search
    humanURL: https://shelf.io/integrations/
    properties:
      - url: https://shelf.io/integrations/
        type: Documentation
    description: The Shelf Content Intelligence API provides AI-powered knowledge retrieval, semantic search, and content quality analysis capabilities. Enables applications to query Shelf's knowledge base with natural language, retrieve contextually relevant answers, and integrate Shelf's AI knowledge engine into contact centers, chatbots, and enterprise applications.
  - aid: shelf:shelf-webhooks
    name: Shelf Webhooks
    tags:
      - Events
      - Knowledge Management
      - Webhooks
    humanURL: https://shelf.io/integrations/
    properties:
      - url: https://shelf.io/integrations/
        type: Documentation
    description: Shelf Webhooks enable real-time event notifications when knowledge content is created, updated, archived, or reviewed. Supports integration with external workflow automation tools, content management systems, and third-party applications via HTTP event payloads.
name: Shelf.io
tags:
  - Artificial Intelligence
  - Contact Center
  - Knowledge Management
  - SaaS
  - Search
type: Contract
image: https://shelf.io/wp-content/uploads/2021/07/shelf-logo.svg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-05-02'
position: Consumer
description: Shelf.io is the first knowledge automation platform and next-generation AI agentic platform for knowledge management. The platform serves as a knowledge hub for brands with contact centers and large customer bases, enabling organizations to manage, improve, and deploy unstructured knowledge for accurate AI-generated answers and self-service experiences. Shelf provides developer-friendly REST APIs, SDKs (Python and JavaScript), webhooks, and 100+ integrations with platforms including Salesforce, Zendesk, ServiceNow, and Microsoft Teams. The platform offers Content Connectors, Decision Trees, multilingual support for 100+ languages, and analytics dashboards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://shelf.io
    type: Website
  - url: https://shelf.io/technology/
    type: Developer Portal
  - url: https://help.shelf.io/technical-guidelines-10162c4f
    type: Documentation
  - url: https://shelf.io/integrations/
    type: Integrations
  - url: https://shelf.io/partners/integrations/
    type: Partner Integrations
  - url: https://github.com/shelfio
    type: GitHub Organization
  - url: https://apitracker.io/a/shelf-io
    type: API Tracker
  - type: Features
    data:
      - name: REST API Access
        description: Programmatic access to all Shelf knowledge resources via REST API with regional endpoints for US, Canada, and Europe.
      - name: Content Intelligence API
        description: AI-powered semantic search and knowledge retrieval for building intelligent knowledge experiences.
      - name: API Token Authentication
        description: Secure API access via token-based authentication with standard and full admin access levels.
      - name: Webhooks
        description: Real-time event notifications for knowledge content lifecycle events.
      - name: Python SDK
        description: Official Python SDK for integrating Shelf knowledge management into Python applications.
      - name: JavaScript SDK
        description: Official JavaScript SDK for integrating Shelf into web and Node.js applications.
      - name: Content Connectors
        description: Pre-built connectors to sync knowledge from SharePoint, Confluence, Google Drive, Zendesk, and 100+ sources.
      - name: Decision Trees
        description: Interactive decision tree builder for guided troubleshooting and self-service content.
      - name: Multilingual Support
        description: Knowledge management and AI responses in 100+ languages.
  - type: UseCases
    data:
      - name: Contact Center Knowledge
        description: Equip contact center agents with instant access to accurate, up-to-date knowledge during customer interactions.
      - name: AI Chatbot Grounding
        description: Ground AI chatbots and virtual assistants with verified organizational knowledge via the Content Intelligence API.
      - name: Self-Service Portal
        description: Build customer self-service portals backed by Shelf's knowledge base and semantic search.
      - name: Knowledge Automation
        description: Automate knowledge curation, quality checks, and content lifecycle management via APIs.
      - name: Enterprise Search
        description: Integrate Shelf search into enterprise portals for unified access to distributed knowledge.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync Shelf knowledge with Salesforce Service Cloud for agent and customer knowledge access.
      - name: Zendesk
        description: Embed Shelf knowledge into Zendesk for agent assist and self-service ticket deflection.
      - name: ServiceNow
        description: Integrate Shelf with ServiceNow for IT service management knowledge automation.
      - name: Microsoft Teams
        description: Surface Shelf knowledge directly within Microsoft Teams for employee self-service.
      - name: Genesys
        description: Integrate Shelf with Genesys contact center platform for agent assist.
      - name: Google Drive
        description: Content Connector to sync and manage knowledge from Google Drive documents.
      - name: Confluence
        description: Content Connector to sync Confluence wiki content into Shelf knowledge base.
---

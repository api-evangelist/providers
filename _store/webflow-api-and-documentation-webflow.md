---
aid: webflow-api-and-documentation-webflow
name: Webflow API and Documentation
description: Webflow provides a visual web development platform with a comprehensive REST API for programmatically managing sites, CMS collections, ecommerce, assets, users, and forms. The Webflow Data API v2 enables developers to build integrations, automate content workflows, and extend Webflow's core functionality. All V2 API endpoints start with https://api.webflow.com/v2 and support OAuth 2.0 and API key authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMS
  - Content Management
  - Ecommerce
  - No-Code
  - Publishing
  - Web Development
url: https://raw.githubusercontent.com/api-evangelist/webflow-api-and-documentation-webflow/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: webflow-api-and-documentation-webflow:data-api
    name: Webflow Data API
    description: The Webflow Data API is a comprehensive RESTful API providing programmatic access to Webflow sites, workspaces, CMS collections and items, ecommerce products and orders, assets, users, forms, and webhooks. All V2 endpoints use https://api.webflow.com/v2 as the base URL and require OAuth 2.0 or API key authentication.
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    tags:
      - CMS
      - Content Management
      - Ecommerce
      - REST
      - Sites
    properties:
      - type: Documentation
        url: https://developers.webflow.com/data/reference/rest-introduction
      - type: OpenAPI
        url: openapi/webflow-data-api-openapi.yml
      - type: Authentication
        url: https://developers.webflow.com/data/reference/authentication
      - type: RateLimits
        url: https://developers.webflow.com/data/reference/rate-limits
      - type: ChangeLog
        url: https://developers.webflow.com/data/v2.0.0/changelog
      - type: JSONSchema
        url: json-schema/webflow-site-schema.json
      - type: JSONSchema
        url: json-schema/webflow-collection-item-schema.json
      - type: JSONSchema
        url: json-schema/webflow-order-schema.json
      - type: JSONSchema
        url: json-schema/webflow-webhook-schema.json
  - aid: webflow-api-and-documentation-webflow:sites-api
    name: Webflow Sites API
    description: Site management endpoints for creating, updating, publishing, and deleting Webflow sites, plus managing custom domains, redirects, robots.txt, and site activity logs.
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    tags:
      - Domains
      - Publishing
      - Sites
    properties:
      - type: Documentation
        url: https://developers.webflow.com/data/reference/rest-introduction
      - type: OpenAPI
        url: openapi/webflow-sites-openapi.yml
  - aid: webflow-api-and-documentation-webflow:collections-api
    name: Webflow Collections API
    description: CMS collection management endpoints for creating, listing, and deleting collections, and managing collection field configurations.
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    tags:
      - CMS
      - Collections
      - Fields
    properties:
      - type: Documentation
        url: https://developers.webflow.com/data/reference/rest-introduction
      - type: OpenAPI
        url: openapi/webflow-collections-openapi.yml
  - aid: webflow-api-and-documentation-webflow:items-api
    name: Webflow CMS Items API
    description: CMS item endpoints for creating, reading, updating, deleting, and publishing collection items, including support for bulk operations and live/staged item management.
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    tags:
      - CMS
      - Content Management
      - Items
    properties:
      - type: Documentation
        url: https://developers.webflow.com/data/reference/rest-introduction
      - type: OpenAPI
        url: openapi/webflow-items-openapi.yml
  - aid: webflow-api-and-documentation-webflow:webhooks-api
    name: Webflow Webhooks API
    description: Webhook registration and management endpoints for receiving real-time event notifications from Webflow sites including form submissions, ecommerce events, and CMS changes.
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    tags:
      - Events
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.webflow.com/data/reference/rest-introduction
      - type: OpenAPI
        url: openapi/webflow-webhooks-openapi.yml
common:
  - url: https://developers.webflow.com/
    name: Webflow Developer Documentation
    type: Portal
    description: Main developer portal for Webflow APIs, guides, and reference.
  - url: https://developers.webflow.com/data/reference/rest-introduction/quick-start
    name: Webflow API Quick Start
    type: GettingStarted
    description: Quick start guide for making your first Webflow API request.
  - url: https://developers.webflow.com/data/reference/authentication
    name: Webflow Authentication
    type: Authentication
    description: OAuth 2.0 and API key authentication for Webflow APIs.
  - url: https://developers.webflow.com/data/reference/rate-limits
    name: Webflow Rate Limits
    type: RateLimits
    description: API rate limiting documentation for Webflow Data API.
  - url: https://developers.webflow.com/data/v2.0.0/changelog
    name: Webflow API Changelog
    type: ChangeLog
    description: Version history and breaking changes for the Webflow Data API.
  - url: https://developers.webflow.com/data/reference/sdks
    name: Webflow SDKs
    type: SDK
    description: Official Webflow SDKs for JavaScript, Python, and other languages.
  - url: https://webflow.com/
    name: Webflow Website
    type: Website
    description: Main Webflow website and product information.
  - url: https://webflow.com/blog
    name: Webflow Blog
    type: Blog
    description: Product news, tutorials, and design inspiration from Webflow.
  - url: https://help.webflow.com/
    name: Webflow Help Center
    type: Support
    description: Help articles and support resources for Webflow users.
  - url: https://forum.webflow.com/
    name: Webflow Forum
    type: Community
    description: Community forum for Webflow users and developers.
  - url: https://university.webflow.com/
    name: Webflow University
    type: Academy
    description: Free courses and tutorials for learning Webflow.
  - url: https://github.com/webflow
    name: Webflow GitHub Organization
    type: GitHubOrganization
    description: Official Webflow GitHub organization with SDKs and tools.
  - url: https://webflow.com/legal/terms
    name: Webflow Terms of Service
    type: TermsOfService
    description: Terms of service for Webflow platform and APIs.
  - url: https://webflow.com/legal/privacy
    name: Webflow Privacy Policy
    type: PrivacyPolicy
    description: Privacy policy for Webflow services.
  - url: https://status.webflow.com/
    name: Webflow Status
    type: StatusPage
    description: Real-time status and uptime information for Webflow services.
  - url: https://webflow.com/marketplace
    name: Webflow Marketplace
    type: Marketplace
    description: Apps, integrations, and templates for the Webflow ecosystem.
  - type: SpectralRules
    url: rules/webflow-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/webflow-api-and-documentation-webflow-vocabulary.yml
  - type: NaftikoCapability
    url: capabilities/cms-management.yaml
  - type: JSONLD
    url: json-ld/webflow-context.jsonld
  - name: Webflow Features
    type: Features
    data:
      - name: Visual Web Builder
        description: Drag-and-drop visual web design with clean, semantic HTML/CSS output.
      - name: CMS API
        description: Programmatic management of CMS collections and items for dynamic content.
      - name: Ecommerce API
        description: Full ecommerce API for products, orders, inventory, and payment processing.
      - name: OAuth 2.0
        description: Secure OAuth 2.0 authorization for building Webflow apps and integrations.
      - name: Webhooks
        description: Real-time event notifications for form submissions, publishing, and ecommerce events.
      - name: Designer Extensions
        description: Build custom panels and tools that run inside the Webflow Designer.
      - name: Site Publishing API
        description: Programmatically publish Webflow sites to staging or production domains.
      - name: Multisite Support
        description: Manage multiple Webflow sites across workspaces from a single API key.
  - name: Webflow Use Cases
    type: UseCases
    data:
      - name: Headless CMS
        description: Use Webflow as a headless CMS, managing content via the API and rendering with any frontend framework.
      - name: Content Automation
        description: Automatically create and publish CMS items from external data sources like spreadsheets or databases.
      - name: Ecommerce Integration
        description: Sync Webflow product catalog and orders with ERP or inventory management systems.
      - name: Multi-Site Management
        description: Manage content across multiple Webflow sites programmatically from a centralized platform.
      - name: Form Lead Processing
        description: Process form submissions via webhooks to integrate with CRM or marketing automation platforms.
      - name: Site Deployment Automation
        description: Automate Webflow site publishing as part of CI/CD pipelines or content approval workflows.
  - name: Webflow Integrations
    type: Integrations
    data:
      - name: Zapier
        description: No-code Webflow integration for connecting with 5,000+ apps via Zapier.
      - name: Make (Integromat)
        description: Visual automation platform for Webflow workflow automation.
      - name: Airtable
        description: Connect Airtable as a data source for Webflow CMS content.
      - name: HubSpot
        description: Sync Webflow form submissions with HubSpot CRM.
      - name: Shopify
        description: Import Shopify product catalog into Webflow ecommerce.
      - name: Cloudflare
        description: Deploy Webflow sites behind Cloudflare for CDN and security.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

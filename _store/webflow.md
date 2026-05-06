---
aid: webflow
name: Webflow
description: Webflow provides a visual web development platform with a comprehensive REST API for programmatically managing sites, CMS collections, ecommerce, assets, users, and forms. The Data API enables developers to build integrations, automate workflows, and extend Webflow's core functionality.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMS
  - Ecommerce
  - No-Code
  - Web Development
url: https://raw.githubusercontent.com/api-evangelist/webflow/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: webflow:data-api
    name: Webflow Data API
    description: The Webflow Data API is a RESTful API that provides access to Webflow sites, pages, CMS collections, ecommerce products and orders, assets, users, and forms. All V2 API endpoints start with https://api.webflow.com/v2 and use OAuth 2.0 for authentication.
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    tags:
      - CMS
      - Content Management
      - Ecommerce
      - Sites
    properties:
      - type: Documentation
        url: https://developers.webflow.com/data/reference/rest-introduction
      - type: Getting Started
        url: https://developers.webflow.com/data/reference/rest-introduction/quick-start
      - type: Authentication
        url: https://developers.webflow.com/data/reference/authentication
      - type: Rate Limits
        url: https://developers.webflow.com/data/reference/rate-limits
      - type: Change Log
        url: https://developers.webflow.com/data/v2.0.0/changelog
      - type: SDKs
        url: https://developers.webflow.com/data/reference/sdks
      - type: OpenAPI
        url: openapi/webflow-data-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/webflow-webhooks-asyncapi.yml
  - aid: webflow:designer-extension-api
    name: Webflow Designer Extension API
    description: The Webflow Designer Extension API allows developers to build extensions that run inside the Webflow Designer, enabling custom UI panels and interactions with the designer canvas and site content.
    humanURL: https://developers.webflow.com/designer/reference/introduction
    tags:
      - Designer
      - Extensions
      - Plugins
    properties:
      - type: Documentation
        url: https://developers.webflow.com/designer/reference/introduction
      - type: Getting Started
        url: https://developers.webflow.com/designer/docs/getting-started-designer-extensions
  - aid: webflow:meta-api
    name: Webflow Meta API
    description: The Webflow Meta API provides endpoints for retrieving information about the authorized user and introspecting API tokens, including scopes and permissions.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Authentication
      - Meta
      - Tokens
    properties:
      - type: OpenAPI
        url: openapi/webflow-meta-openapi.yml
  - aid: webflow:sites-api
    name: Webflow Sites API
    description: The Webflow Sites API provides endpoints for managing Webflow sites within a workspace, including creating, updating, publishing, and deleting sites, as well as managing custom domains, redirects, robots.txt, and site activity logs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Domains
      - Publishing
      - Sites
    properties:
      - type: OpenAPI
        url: openapi/webflow-sites-openapi.yml
  - aid: webflow:pages-api
    name: Webflow Pages API
    description: The Webflow Pages API provides endpoints for listing, retrieving, and updating page metadata and DOM content for pages within a Webflow site.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Content
      - DOM
      - Pages
    properties:
      - type: OpenAPI
        url: openapi/webflow-pages-openapi.yml
  - aid: webflow:collections-api
    name: Webflow Collections API
    description: The Webflow Collections API provides endpoints for managing CMS collections, including creating, listing, and deleting collections, as well as managing collection fields and their configurations.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - CMS
      - Collections
      - Fields
    properties:
      - type: OpenAPI
        url: openapi/webflow-collections-openapi.yml
  - aid: webflow:items-api
    name: Webflow CMS Items API
    description: The Webflow CMS Items API provides endpoints for creating, reading, updating, deleting, and publishing collection items, including support for bulk operations and live/staged item management.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - CMS
      - Content Management
      - Items
    properties:
      - type: OpenAPI
        url: openapi/webflow-items-openapi.yml
  - aid: webflow:components-api
    name: Webflow Components API
    description: The Webflow Components API provides endpoints for listing components within a site, and retrieving or updating component content and properties.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Components
      - Design
      - Reusable
    properties:
      - type: OpenAPI
        url: openapi/webflow-components-openapi.yml
  - aid: webflow:assets-api
    name: Webflow Assets API
    description: The Webflow Assets API provides endpoints for uploading, listing, updating, and deleting assets and asset folders within a Webflow site.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Assets
      - Files
      - Media
    properties:
      - type: OpenAPI
        url: openapi/webflow-assets-openapi.yml
  - aid: webflow:forms-api
    name: Webflow Forms API
    description: The Webflow Forms API provides endpoints for listing forms, retrieving form schemas, and managing form submissions including listing, modifying, and deleting submissions.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Forms
      - Submissions
    properties:
      - type: OpenAPI
        url: openapi/webflow-forms-openapi.yml
  - aid: webflow:products-api
    name: Webflow Products and SKUs API
    description: The Webflow Products and SKUs API provides endpoints for managing ecommerce products and their SKU variants, including creating, listing, updating products and creating or updating SKUs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Ecommerce
      - Products
      - SKUs
    properties:
      - type: OpenAPI
        url: openapi/webflow-products-openapi.yml
  - aid: webflow:orders-api
    name: Webflow Orders API
    description: The Webflow Orders API provides endpoints for listing, retrieving, and updating ecommerce orders, as well as fulfilling, unfulfilling, and refunding orders.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Ecommerce
      - Fulfillment
      - Orders
    properties:
      - type: OpenAPI
        url: openapi/webflow-orders-openapi.yml
  - aid: webflow:inventory-api
    name: Webflow Inventory API
    description: The Webflow Inventory API provides endpoints for listing and updating inventory quantities for ecommerce product SKUs.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Ecommerce
      - Inventory
      - Stock
    properties:
      - type: OpenAPI
        url: openapi/webflow-inventory-openapi.yml
  - aid: webflow:ecommerce-settings-api
    name: Webflow Ecommerce Settings API
    description: The Webflow Ecommerce Settings API provides an endpoint for retrieving the ecommerce configuration settings for a Webflow site.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Configuration
      - Ecommerce
      - Settings
    properties:
      - type: OpenAPI
        url: openapi/webflow-ecommerce-settings-openapi.yml
  - aid: webflow:webhooks-api
    name: Webflow Webhooks API
    description: The Webflow Webhooks API provides endpoints for registering, listing, retrieving, and removing webhooks that deliver real-time event notifications for a Webflow site.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Events
      - Notifications
      - Webhooks
    properties:
      - type: OpenAPI
        url: openapi/webflow-webhooks-openapi.yml
  - aid: webflow:custom-code-api
    name: Webflow Custom Code API
    description: The Webflow Custom Code API provides endpoints for adding, updating, and deleting custom JavaScript code on sites and pages, as well as registering and managing hosted or inline scripts.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Custom Code
      - JavaScript
      - Scripts
    properties:
      - type: OpenAPI
        url: openapi/webflow-custom-code-openapi.yml
  - aid: webflow:comments-api
    name: Webflow Comments API
    description: The Webflow Comments API provides endpoints for listing comment threads and retrieving comment replies within a Webflow site.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.webflow.com/data/reference/rest-introduction
    baseURL: https://api.webflow.com/v2
    tags:
      - Collaboration
      - Comments
    properties:
      - type: OpenAPI
        url: openapi/webflow-comments-openapi.yml
common:
  - url: https://developers.webflow.com/
    name: Webflow Developer Documentation
    type: Portal
    description: 'null'
  - url: https://developers.webflow.com/data/docs/data-clients
    name: Working with the Data API
    type: Documentation
    description: 'null'
  - url: https://developers.webflow.com/data/reference/rest-introduction/quick-start
    name: Getting Started | Webflow Developer Documentation
    type: Getting Started
    description: 'null'
  - url: https://webflow.com/
    name: Webflow - Website Builder
    type: Website
    description: 'null'
  - url: https://webflow.com/blog
    name: Webflow Blog
    type: Blog
    description: 'null'
  - url: https://help.webflow.com/
    name: Webflow Help Center
    type: Support
    description: 'null'
  - url: https://forum.webflow.com/
    name: Webflow Forum
    type: Community
    description: 'null'
  - url: https://university.webflow.com/
    name: Webflow University
    type: LearningCenter
    description: 'null'
  - url: https://github.com/webflow
    name: Webflow GitHub Organization
    type: GitHubOrganization
    description: 'null'
  - url: https://webflow.com/legal/terms
    name: Terms of Service | Webflow
    type: TermsOfService
    description: 'null'
  - url: https://webflow.com/legal/privacy
    name: Privacy Policy | Webflow
    type: PrivacyPolicy
    description: 'null'
  - url: https://status.webflow.com/
    name: Webflow Status
    type: Status
    description: 'null'
  - url: https://webflow.com/login
    name: Webflow Login
    type: Login
    description: 'null'
  - url: https://webflow.com/signup
    name: Webflow Sign Up
    type: Sign Up
    description: 'null'
  - url: https://webflow.com/marketplace
    name: Webflow Marketplace
    type: Marketplace
    description: 'null'
  - url: https://developers.webflow.com/apps/data/docs/register-an-app
    name: Register an App
    type: Getting Started
    description: 'null'
  - url: https://developers.webflow.com/data/reference/authentication
    name: Webflow Authentication
    type: Authentication
    description: 'null'
  - url: https://developers.webflow.com/data/reference/rate-limits
    name: Webflow Rate Limits
    type: Rate Limits
    description: 'null'
  - url: https://developers.webflow.com/data/v2.0.0/changelog
    name: Webflow API Changelog
    type: Change Log
    description: 'null'
  - url: https://developers.webflow.com/data/reference/sdks
    name: Webflow SDKs
    type: SDKs
    description: 'null'
  - url: https://developers.webflow.com/data/docs/working-with-webhooks
    name: Working with Webhooks
    type: Webhooks
    description: 'null'
  - type: JSONSchema
    url: json-schema/webflow-site-schema.json
  - type: JSONSchema
    url: json-schema/webflow-collection-item-schema.json
  - type: JSONSchema
    url: json-schema/webflow-order-schema.json
  - type: JSONSchema
    url: json-schema/webflow-webhook-schema.json
  - type: JSONLD
    url: json-ld/webflow-context.jsonld
  - type: SpectralRules
    url: rules/webflow-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/cms-and-ecommerce.yaml
  - type: Vocabulary
    url: vocabulary/webflow-vocabulary.yml
  - name: Webflow Features
    type: Features
    data:
      - name: Visual Web Builder
        description: Drag-and-drop visual design with clean, production-ready HTML/CSS/JS output.
      - name: CMS API
        description: Programmatic management of CMS collections and items for dynamic content publishing.
      - name: Ecommerce API
        description: Complete ecommerce API for products, SKUs, orders, inventory, and payment integration.
      - name: OAuth 2.0
        description: Secure OAuth 2.0 authorization for building Webflow App integrations.
      - name: Webhooks
        description: Real-time event notifications for form submissions, publishing, ecommerce events, and CMS changes.
      - name: AsyncAPI Webhooks
        description: AsyncAPI specification documenting all Webflow webhook event schemas.
      - name: Designer Extensions
        description: Build custom panels and tools that run inside the Webflow Designer application.
      - name: Site Publishing API
        description: Programmatically publish Webflow sites to staging or custom production domains.
  - name: Webflow Use Cases
    type: UseCases
    data:
      - name: Headless CMS
        description: Use Webflow as a headless CMS, managing content via the API with any frontend framework.
      - name: Content Automation
        description: Automatically create, update, and publish CMS items from external databases or APIs.
      - name: Ecommerce Integration
        description: Sync Webflow product catalog and orders with ERP, PIM, or inventory management systems.
      - name: Multi-Site Management
        description: Manage content and publishing across multiple Webflow sites from a centralized platform.
      - name: Form Processing
        description: Process form submissions via webhooks to integrate with CRM or marketing automation.
      - name: Site Deployment Pipeline
        description: Trigger Webflow site publishing as part of automated content approval or CI/CD workflows.
  - name: Webflow Integrations
    type: Integrations
    data:
      - name: Zapier
        description: No-code Webflow integration for automating workflows with 5,000+ apps.
      - name: Make (Integromat)
        description: Visual automation platform for complex Webflow workflow automation.
      - name: Airtable
        description: Connect Airtable as a data source for Webflow CMS content.
      - name: HubSpot
        description: Sync Webflow form submissions and data with HubSpot CRM.
      - name: Shopify
        description: Import Shopify product catalog into Webflow ecommerce.
      - name: Memberstack
        description: Add membership and authentication features to Webflow sites.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

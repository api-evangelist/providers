---
aid: optimizely
name: Optimizely
description: Optimizely is a digital experience platform that provides A/B testing, feature flagging, content management, and commerce solutions for enterprises. Their developer platform offers a comprehensive suite of REST and GraphQL APIs spanning experimentation, content delivery, customer data, campaign management, and e-commerce capabilities.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - A/B Testing
  - Content Management
  - Customer Data
  - E-Commerce
  - Experimentation
  - Feature Flags
  - Marketing
created: '2025-03-04'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: optimizely:web-experimentation
    name: Optimizely Web Experimentation REST API
    description: The Optimizely Web Experimentation REST API provides programmatic access to Optimizely's A/B testing and web experimentation platform. Developers can manage experiments, projects, audiences, and other resources through RESTful endpoints defined using the OpenAPI Specification. The API uses OAuth2 Bearer token authentication and provides access to data and services like Stats Engine and customer profiles, enabling integration of experimentation workflows into custom applications.
    humanURL: https://docs.developers.optimizely.com/web-experimentation/docs/rest-api-introduction
    baseURL: https://api.optimizely.com/v2
    tags:
      - A/B Testing
      - Analytics
      - Experimentation
      - Web Optimization
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/web-experimentation/docs/rest-api-introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-web-experimentation-openapi.yml
  - aid: optimizely:feature-experimentation
    name: Optimizely Feature Experimentation REST API
    description: The Optimizely Feature Experimentation REST API enables developers to programmatically manage feature flags, experiments, rollouts, and environments within the Optimizely Feature Experimentation platform. It provides endpoints for creating and configuring experiments, managing feature variables, and controlling feature rollouts across different environments. The API also includes a flags endpoint at api.optimizely.com/flags/v1 for flag-specific operations, and supports Bearer token authentication.
    humanURL: https://docs.developers.optimizely.com/feature-experimentation/reference/feature-experimentation-api-overview
    baseURL: https://api.optimizely.com/flags/v1
    tags:
      - Experimentation
      - Feature Flags
      - Feature Management
      - Rollouts
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/feature-experimentation/reference/feature-experimentation-api-overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-feature-experimentation-openapi.yml
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/asyncapi/optimizely-feature-experimentation-asyncapi.yml
  - aid: optimizely:campaign
    name: Optimizely Campaign REST API
    description: The Optimizely Campaign REST API provides programmatic access to Optimizely's email and omnichannel campaign management capabilities. Developers can use the API to manage campaigns, recipients, mailing lists, and messaging workflows. The API is hosted at api.campaign.episerver.net and supports automation of marketing campaign operations, enabling integration with external systems and custom marketing workflows.
    humanURL: https://docs.developers.optimizely.com/optimizely-campaign/docs/rest-api
    baseURL: https://api.campaign.episerver.net
    tags:
      - Campaigns
      - Email Marketing
      - Marketing Automation
      - Messaging
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/optimizely-campaign/docs/rest-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-campaign-openapi.yml
  - aid: optimizely:content-delivery
    name: Optimizely Content Delivery API
    description: The Optimizely Content Delivery API is a flexible REST API for building headless CMS solutions with Optimizely CMS. It provides a pluggable and configurable web API for querying content, enabling developers to deliver content to any frontend framework or channel. The API is distributed as the EPiServer.ContentDeliveryApi.Cms NuGet package and supports content retrieval, filtering, and expansion of content references for building decoupled architectures.
    humanURL: https://docs.developers.optimizely.com/content-management-system/v1.5.0-content-delivery-api/docs/content-delivery-api
    tags:
      - Content Delivery
      - Content Management
      - Headless CMS
      - REST
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/content-management-system/v1.5.0-content-delivery-api/docs/content-delivery-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-content-delivery-openapi.yml
  - aid: optimizely:content-management
    name: Optimizely Content Management API
    description: The Optimizely Content Management API provides REST endpoints for performing content operations within Optimizely CMS. Developers can create, read, update, and delete content items programmatically, enabling automated content workflows and integration with external systems. The API supports managing pages, blocks, media, and other content types within the Optimizely CMS ecosystem.
    humanURL: https://docs.developers.optimizely.com/content-management-system/v1.6.0-content-management-api/docs/getting-started
    tags:
      - CMS
      - Content Management
      - Content Operations
      - REST
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/content-management-system/v1.6.0-content-management-api/docs/getting-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-content-management-openapi.yml
  - aid: optimizely:graph
    name: Optimizely Graph API
    description: Optimizely Graph is a unified content query and delivery service that provides access to content across Optimizely products through a single GraphQL API. It enables flexible data retrieval, high-performance search, and dynamic content delivery for both Optimizely CMS and custom applications. Developers can explore their content model, run GraphQL queries, and power fast content delivery experiences without needing to query individual content repositories directly.
    humanURL: https://docs.developers.optimizely.com/platform-optimizely/docs/getting-started-with-graphql-api
    tags:
      - Content Delivery
      - Content Query
      - GraphQL
      - Search
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/platform-optimizely/docs/getting-started-with-graphql-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-graph-openapi.yml
  - aid: optimizely:data-platform
    name: Optimizely Data Platform REST API
    description: The Optimizely Data Platform (ODP) REST API enables developers to integrate customer data with the Optimizely Data Platform. It provides endpoints for managing customer profiles, events, segments, and audiences, enabling a unified view of customer data across channels. The API supports real-time data ingestion and retrieval, allowing developers to build personalized experiences powered by comprehensive customer intelligence.
    humanURL: https://docs.developers.optimizely.com/optimizely-data-platform/reference/introduction
    tags:
      - Analytics
      - CDP
      - Customer Data
      - Data Platform
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/optimizely-data-platform/reference/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-data-platform-openapi.yml
  - aid: optimizely:cmp
    name: Optimizely CMP Open REST API
    description: The Optimizely Content Marketing Platform (CMP) Open REST API provides programmatic access to Optimizely's content marketing and planning tools. Developers can manage content workflows, campaigns, assets, and editorial calendars through RESTful endpoints hosted at api.cmp.optimizely.com. The API enables integration of content marketing operations with external systems, supporting automated content production and distribution workflows.
    humanURL: https://docs.developers.optimizely.com/content-marketing-platform/docs/open-api-introduction
    baseURL: https://api.cmp.optimizely.com
    tags:
      - Content Marketing
      - Content Planning
      - Marketing
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/content-marketing-platform/docs/open-api-introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-cmp-openapi.yml
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/asyncapi/optimizely-cmp-asyncapi.yml
  - aid: optimizely:commerce-service
    name: Optimizely Commerce Service API
    description: The Optimizely Commerce Service API provides RESTful access to Optimizely's e-commerce platform capabilities. It enables developers to manage product catalogs, orders, customers, and inventory programmatically. The API supports integration with external commerce systems and enables building custom storefronts and order management workflows on top of the Optimizely Commerce platform.
    humanURL: https://docs.developers.optimizely.com/commerce-connect/v1.3.0-service-api-developer-guide/docs/optimizely-service-api
    tags:
      - Catalog
      - Commerce
      - E-Commerce
      - Orders
    properties:
      - type: Documentation
        url: https://docs.developers.optimizely.com/commerce-connect/v1.3.0-service-api-developer-guide/docs/optimizely-service-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/openapi/optimizely-commerce-service-openapi.yml
common:
  - type: Developer Portal
    url: https://docs.developers.optimizely.com/
  - type: Website
    url: https://www.optimizely.com/
  - type: Blog
    url: https://www.optimizely.com/blog/
  - type: Support
    url: https://support.optimizely.com/
  - type: Login
    url: https://app.optimizely.com/signin
  - type: Privacy Policy
    url: https://www.optimizely.com/legal/privacy-policy/
  - type: Terms of Service
    url: https://www.optimizely.com/legal/terms-of-service/
  - type: Features
    data:
      - 'Entry: ~$36K/year for basic Optimizely use'
      - 'Mid: ~$63,700 per 10M impressions for Web Experimentation'
      - 'Enterprise: $200K-$400K+/year for full DXP suite'
      - 'Modular: pick CMS / Commerce / Experimentation independently'
      - Web Experimentation (A/B + multivariate)
      - Feature Experimentation (server-side flags)
      - Personalization with audiences and Stats Engine
      - Content Cloud (CMS)
      - Commerce Cloud and Configured Commerce
      - Optimizely AI Copilot
      - REST API at api.optimizely.com
      - Default 100 req/min/project
      - OAuth 2.0 + Personal API tokens
      - Webhooks for project events
      - Datafile-based Feature Experimentation SDKs (10+)
      - Stats Engine with Sequential Testing
    sources:
      - https://www.optimizely.com/plans/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: contentstack
url: https://raw.githubusercontent.com/api-evangelist/contentstack/refs/heads/main/apis.yml
modified: '2026-04-28'
apis:
  - aid: contentstack:content-delivery-api
    name: Contentstack Content Delivery API
    tags:
      - Content Delivery
      - Content Management
      - Headless CMS
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cdn.contentstack.io
    humanURL: https://www.contentstack.com/docs/developers/apis/content-delivery-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/content-delivery-api
        type: Documentation
      - url: openapi/contentstack-content-delivery-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Content Delivery API (CDA) allows developers to retrieve published content from their Contentstack stacks and deliver it to web or mobile applications. It supports fetching entries, assets, and content types through REST endpoints using stack API keys and delivery tokens for authentication. The API is read-only and optimized for high-performance content retrieval at scale.
  - aid: contentstack:content-management-api
    name: Contentstack Content Management API
    tags:
      - Content Management
      - CRUD
      - Headless CMS
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.contentstack.io
    humanURL: https://www.contentstack.com/docs/developers/apis/content-management-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/content-management-api
        type: Documentation
      - url: openapi/contentstack-content-management-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Content Management API (CMA) provides programmatic access to manage all aspects of a Contentstack stack, including content types, entries, assets, environments, workflows, and users. It supports full CRUD operations using standard HTTP verbs (GET, POST, PUT, DELETE) and authenticates via management tokens or user session tokens.
  - aid: contentstack:graphql-content-delivery-api
    name: Contentstack GraphQL Content Delivery API
    tags:
      - Content Delivery
      - GraphQL
      - Headless CMS
      - Query Language
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graphql.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/graphql-content-delivery-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/graphql-content-delivery-api
        type: Documentation
    description: The Contentstack GraphQL Content Delivery API enables developers to query content from their Contentstack stack using GraphQL syntax, allowing precise retrieval of only the fields and relationships needed in a single request. It is built on top of the Content Delivery API and supports querying entries, assets, and nested references across content types. The GraphQL API does not support mutations or subscriptions; it is strictly read-only and intended for front-end and application data fetching.
  - aid: contentstack:image-delivery-api
    name: Contentstack Image Delivery API
    tags:
      - Asset Delivery
      - Images
      - Media
      - Transformation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://images.contentstack.io
    humanURL: https://www.contentstack.com/docs/developers/apis/image-delivery-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/image-delivery-api
        type: Documentation
    description: The Contentstack Image Delivery API allows developers to retrieve and transform images stored as assets in their Contentstack stacks. It supports on-the-fly image manipulation operations including resizing, cropping, format conversion, quality adjustment, and overlay compositing via URL query parameters. Images are served from a CDN for fast delivery, and transformations are applied at request time without creating additional stored copies.
  - aid: contentstack:personalize-management-api
    name: Contentstack Personalize Management API
    tags:
      - Audiences
      - Content Management
      - Experiences
      - Personalization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://personalize-api.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/personalize-management-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/personalize-management-api
        type: Documentation
      - url: openapi/contentstack-personalize-management-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Personalize Management API provides programmatic control over the resources in a Contentstack Personalize project, including Attributes, Audiences, Events, and Experiences. Developers can use this API to create and manage audience segments based on user attributes and behavioral events, and to configure personalized content experiences for those segments.
  - aid: contentstack:personalize-edge-api
    name: Contentstack Personalize Edge API
    tags:
      - Edge Computing
      - Events
      - Personalization
      - User Attributes
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://personalize-edge.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/personalize-edge-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/personalize-edge-api
        type: Documentation
      - url: openapi/contentstack-personalize-edge-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Personalize Edge API enables real-time, dynamic personalization interactions using edge computing to retrieve personalized content experiences. It allows applications to retrieve personalization manifests of active experiences, set and update user attributes for audience matching, merge user identity records, and track behavioral events.
  - aid: contentstack:automate-management-api
    name: Contentstack Automate Management API
    tags:
      - Automation
      - Content Management
      - Integration
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://automations-api.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/automation-hub-management-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/automation-hub-management-api
        type: Documentation
      - url: openapi/contentstack-automate-management-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Automate Management API allows developers to programmatically manage automation projects and workflows within a Contentstack organization. It supports creating, updating, retrieving, and deleting automations that connect Contentstack content events to third-party services and internal processes. This API is part of the Contentstack Automate (formerly Automation Hub) product, which provides a no-code/low-code automation layer built on top of the CMS.
  - aid: contentstack:analytics-api
    name: Contentstack Analytics API
    tags:
      - Analytics
      - Metrics
      - Monitoring
      - Reporting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.contentstack.io
    humanURL: https://www.contentstack.com/docs/developers/apis/analytics-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/analytics-api
        type: Documentation
      - url: openapi/contentstack-analytics-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Analytics API provides access to usage and performance metrics for CMS, Launch, and Automate products within a Contentstack organization. Developers can retrieve analytics data programmatically to build custom dashboards, monitor content delivery performance, and track platform usage against plan limits.
  - aid: contentstack:scim-api
    name: Contentstack SCIM API
    tags:
      - Identity Management
      - SCIM
      - Security
      - User Provisioning
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://auth-api.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/scim-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/scim-api
        type: Documentation
      - url: openapi/contentstack-scim-api-openapi.yml
        type: OpenAPI
    description: The Contentstack SCIM API implements the System for Cross-domain Identity Management (SCIM 2.0) standard to enable automated user lifecycle management within a Contentstack organization. It allows Identity Providers (IdPs) to provision and deprovision users, manage group memberships, and synchronize user attributes between the IdP and Contentstack.
  - aid: contentstack:brand-kit-management-api
    name: Contentstack Brand Kit Management API
    tags:
      - AI
      - Brand Management
      - Content Generation
      - Voice Profiles
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://brand-kits-api.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/brand-kit-management-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/brand-kit-management-api
        type: Documentation
      - url: openapi/contentstack-brand-kit-management-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Brand Kit Management API provides programmatic control over Brand Kit resources within a Contentstack organization. Brand Kits serve as centralized hubs for an organization's brand identity, encompassing detailed brand information, writing guidelines, and persona configurations.
  - aid: contentstack:knowledge-vault-api
    name: Contentstack Knowledge Vault API
    tags:
      - AI
      - Knowledge Management
      - RAG
      - Vector Database
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://ai.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/knowledge-vault-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/knowledge-vault-api
        type: Documentation
      - url: openapi/contentstack-knowledge-vault-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Knowledge Vault API provides endpoints for ingesting, updating, and deleting content items stored in a Brand Kit's Knowledge Vault. The Knowledge Vault is a vector database that stores brand-specific knowledge content which is retrieved during AI content generation to provide accurate, brand-aligned responses. Content ingested via this API is vectorized and made available to the Generative AI API for retrieval augmented generation (RAG) workflows.
  - aid: contentstack:generative-ai-api
    name: Contentstack Generative AI API
    tags:
      - AI
      - Brand Kit
      - Content Generation
      - Generative AI
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://ai.contentstack.com/brand-kits
    humanURL: https://www.contentstack.com/docs/developers/apis/generative-ai-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/generative-ai-api
        type: Documentation
      - url: openapi/contentstack-generative-ai-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Generative AI API provides an endpoint for generating AI-powered content using a Brand Kit's knowledge vault and voice profiles. It acts as a communication channel between the vector database and large language models, processing prompts with retrieval augmented generation (RAG) to produce brand-aligned content.
  - aid: contentstack:launch-api
    name: Contentstack Launch API
    tags:
      - CI/CD
      - Deployment
      - Frontend
      - Hosting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://launch-api.contentstack.com
    humanURL: https://www.contentstack.com/docs/developers/apis/launch-api
    properties:
      - url: https://www.contentstack.com/docs/developers/apis/launch-api
        type: Documentation
      - url: openapi/contentstack-launch-api-openapi.yml
        type: OpenAPI
    description: The Contentstack Launch API allows developers to programmatically manage web application deployments within Contentstack Launch. It supports full lifecycle management of Launch projects, environments, and deployments, including creating deployments from uploaded build artifacts, monitoring deployment logs, revalidating CDN caches, and retrieving signed upload URLs for build file transfers.
common:
  - url: asyncapi/contentstack-webhooks-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/contentstack-entry-schema.json
    type: JSONSchema
  - url: json-schema/contentstack-stack-schema.json
    type: JSONSchema
  - url: json-schema/contentstack-webhook-payload-schema.json
    type: JSONSchema
  - url: json-ld/contentstack-context.jsonld
    type: JSON-LD
  - url: vocabulary/contentstack-vocabulary.yml
    type: Vocabulary
  - url: rules/contentstack-rules.yml
    type: SpectralRules
  - url: capabilities/deliver-headless-content.yml
    type: Capability
  - url: capabilities/manage-stack-content.yml
    type: Capability
  - url: capabilities/personalize-experiences.yml
    type: Capability
  - url: capabilities/automate-content-workflows.yml
    type: Capability
  - url: capabilities/generate-brand-aligned-ai-content.yml
    type: Capability
  - url: capabilities/deploy-launch-frontends.yml
    type: Capability
  - url: capabilities/provision-users-via-scim.yml
    type: Capability
description: This document is a detailed reference to Contentstack’s Content Delivery API. Retrieve content from your account and deliver it to web and mobile properties.
---

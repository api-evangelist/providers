---
aid: storyblok
name: Storyblok
description: Storyblok is a headless content management system (CMS) with a visual editor that enables developers and content editors to collaboratively build and manage digital experiences. It provides APIs for content delivery, content management, image optimization, and webhook-based event notifications. Storyblok supports composable content through reusable components, multi-language content, and multi-site management with real-time collaboration features.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMS
  - Content Delivery
  - Content Management
  - Headless CMS
  - Image Optimization
  - REST API
  - Visual Editor
  - Webhooks
created: '2026-05-02'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/storyblok/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: storyblok:storyblok-content-delivery-api
    name: Storyblok Content Delivery API
    description: The Storyblok Content Delivery API v2 enables developers to fetch published content from a Storyblok space for delivery to web, mobile, and other channels. Provides access to stories, datasources, links, tags, and asset metadata with filtering, pagination, and relation resolution. Available across multiple regional endpoints for global low-latency delivery.
    humanURL: https://www.storyblok.com/docs/api/content-delivery/v2
    baseURL: https://api.storyblok.com/v2/cdn
    tags:
      - Content Delivery
      - Headless CMS
      - REST API
      - Stories
    properties:
      - type: Documentation
        url: https://www.storyblok.com/docs/api/content-delivery/v2
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/storyblok/refs/heads/main/openapi/storyblok-content-delivery-api-v2-openapi.yml
  - aid: storyblok:storyblok-management-api
    name: Storyblok Management API
    description: The Storyblok Management API is a REST API for programmatically creating, reading, updating, and deleting content and configuration within a Storyblok space. Supports managing stories, components, assets, datasources, collaborators, webhooks, and space settings. Used for editorial tooling, content migration, CI/CD pipelines, and automated publishing workflows.
    humanURL: https://www.storyblok.com/docs/api/management
    baseURL: https://mapi.storyblok.com/v1
    tags:
      - Assets
      - CMS
      - Components
      - Content Management
      - REST API
      - Stories
      - Webhooks
    properties:
      - type: Documentation
        url: https://www.storyblok.com/docs/api/management
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/storyblok/refs/heads/main/openapi/storyblok-management-api-openapi.yml
  - aid: storyblok:storyblok-image-service
    name: Storyblok Image Service
    description: The Storyblok Image Service provides on-the-fly image resizing, cropping, filtering, and format conversion for assets stored in Storyblok. Supports fit-in resizing, smart cropping, focus-point-based cropping, and custom filter chains for quality adjustment, grayscale, and blur effects.
    humanURL: https://www.storyblok.com/docs/image-service
    baseURL: https://a.storyblok.com
    tags:
      - Image Optimization
      - Image Processing
      - Media
    properties:
      - type: Documentation
        url: https://www.storyblok.com/docs/image-service
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/storyblok/refs/heads/main/openapi/storyblok-image-service-openapi.yml
  - aid: storyblok:storyblok-webhooks
    name: Storyblok Webhooks
    description: Storyblok emits webhook events when content actions occur in a space such as story publication, unpublication, deletion, asset upload, and pipeline stage transitions. AsyncAPI specification for webhook event schemas.
    humanURL: https://www.storyblok.com/docs/guide/in-depth/webhooks
    tags:
      - AsyncAPI
      - Events
      - Real-Time
      - Webhooks
    properties:
      - type: Documentation
        url: https://www.storyblok.com/docs/guide/in-depth/webhooks
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/storyblok/refs/heads/main/asyncapi/storyblok-webhooks-asyncapi.yml
common:
  - type: Portal
    url: https://www.storyblok.com/
  - type: Documentation
    url: https://www.storyblok.com/docs
  - type: Pricing
    url: https://www.storyblok.com/pricing
  - type: Blog
    url: https://www.storyblok.com/blog
  - type: About
    url: https://www.storyblok.com/about
  - type: Changelog
    url: https://www.storyblok.com/changelog
  - type: CaseStudies
    url: https://www.storyblok.com/customer-stories
  - type: Contact
    url: https://www.storyblok.com/contact
  - type: Status
    url: https://status.storyblok.com/
  - type: Support
    url: https://www.storyblok.com/support
  - type: PrivacyPolicy
    url: https://www.storyblok.com/legal/privacy-policy
  - type: TermsOfService
    url: https://www.storyblok.com/legal/terms-of-service
  - type: Sign Up
    url: https://app.storyblok.com/#!/signup
  - type: Login
    url: https://app.storyblok.com/
  - type: GitHubOrg
    url: https://github.com/storyblok
  - type: SDK
    url: https://www.storyblok.com/technologies
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

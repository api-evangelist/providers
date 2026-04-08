---
aid: adobe-suite
url: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/apis.yml
apis:
- name: Adobe Photoshop API
  description: Automate Photoshop workflows including image editing, layer manipulation, and batch processing.
  image: https://www.adobe.com/content/dam/cc/icons/photoshop.svg
  humanURL: https://developer.adobe.com/photoshop/
  baseURL: https://image.adobe.io
  tags:
  - Automation
  - Creative
  - Editing
  - Images
  properties:
  - type: Documentation
    url: https://developer.adobe.com/photoshop/api/docs/
  - type: OpenAPI
    url: https://developer.adobe.com/photoshop/api/openapi/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
  contact:
  - FN: Adobe Developer Support
    email: support@adobe.com
    url: https://developer.adobe.com/support/
- name: Adobe Lightroom API
  description: Integrate Lightroom functionality for photo organization and editing.
  image: https://www.adobe.com/content/dam/cc/icons/lightroom.svg
  humanURL: https://developer.adobe.com/lightroom/
  baseURL: https://lr.adobe.io
  tags:
  - Editing
  - Organization
  - Photography
  - Raw
  properties:
  - type: Documentation
    url: https://developer.adobe.com/lightroom/api/docs/
  - type: OpenAPI
    url: https://developer.adobe.com/lightroom/api/openapi/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- name: Adobe Illustrator API
  description: Automate vector graphics creation and manipulation.
  image: https://www.adobe.com/content/dam/cc/icons/illustrator.svg
  humanURL: https://developer.adobe.com/illustrator/
  baseURL: https://illustrator.adobe.io
  tags:
  - Automation
  - Design
  - Graphics
  - Vector
  properties:
  - type: Documentation
    url: https://developer.adobe.com/illustrator/api/docs/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- name: Adobe InDesign API
  description: Automate document layout and publishing workflows.
  image: https://www.adobe.com/content/dam/cc/icons/indesign.svg
  humanURL: https://developer.adobe.com/indesign/
  baseURL: https://indesign.adobe.io
  tags:
  - Documents
  - Layout
  - Print
  - Publishing
  properties:
  - type: Documentation
    url: https://developer.adobe.com/indesign/docs/
- name: Adobe PDF Services API
  description: Create, convert, OCR, and manipulate PDF documents.
  image: https://www.adobe.com/content/dam/cc/icons/acrobat.svg
  humanURL: https://developer.adobe.com/document-services/apis/pdf-services/
  baseURL: https://pdf-services.adobe.io
  tags:
  - Conversion
  - Documents
  - Ocr
  - Pdf
  properties:
  - type: Documentation
    url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/
  - type: OpenAPI
    url: https://developer.adobe.com/document-services/docs/apis/
  - type: Pricing
    url: https://developer.adobe.com/document-services/pricing/
  - type: SDKs
    url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/sdks/
  - type: Release Notes
    url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/releasenotes
- name: Adobe PDF Extract API
  description: Extract content and structural information from PDF documents using AI-powered analysis including text, tables, and images.
  image: https://www.adobe.com/content/dam/cc/icons/acrobat.svg
  humanURL: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/
  baseURL: https://pdf-services.adobe.io
  tags:
  - Ai
  - Documents
  - Extraction
  - Pdf
  properties:
  - type: Documentation
    url: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/
  - type: Getting Started
    url: https://developer.adobe.com/document-services/docs/overview/pdf-extract-api/gettingstarted/
  - type: OpenAPI
    url: https://developer.adobe.com/document-services/docs/apis/
- name: Adobe PDF Accessibility Auto-Tag API
  description: Automatically tag PDF documents for accessibility compliance using AI to identify headings, reading order, tables, and document structure.
  image: https://www.adobe.com/content/dam/cc/icons/acrobat.svg
  humanURL: https://developer.adobe.com/document-services/apis/pdf-accessibility-auto-tag/
  baseURL: https://pdf-services.adobe.io
  tags:
  - Accessibility
  - Ai
  - Compliance
  - Pdf
  properties:
  - type: Documentation
    url: https://developer.adobe.com/document-services/docs/overview/pdf-accessibility-auto-tag-api/
  - type: OpenAPI
    url: https://developer.adobe.com/document-services/docs/apis/
- name: Adobe Sign API
  description: Integrate e-signature workflows and document signing.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-sign.svg
  humanURL: https://developer.adobe.com/sign/
  baseURL: https://api.adobe.io/sign
  tags:
  - Documents
  - Esignature
  - Legal
  - Workflow
  properties:
  - type: Documentation
    url: https://developer.adobe.com/sign/docs/
  - type: API Reference
    url: https://secure.na1.adobesign.com/public/docs/restapi/v6
  - type: Webhooks
    url: https://developer.adobe.com/sign/docs/webhooks/
- name: Adobe Analytics API
  description: Access and analyze digital marketing analytics data.
  image: https://www.adobe.com/content/dam/cc/icons/analytics.svg
  humanURL: https://developer.adobe.com/analytics-apis/
  baseURL: https://analytics.adobe.io
  tags:
  - Analytics
  - Data
  - Marketing
  - Reporting
  properties:
  - type: Documentation
    url: https://developer.adobe.com/analytics-apis/docs/
  - type: API Reference
    url: https://developer.adobe.com/analytics-apis/docs/2.0/
  - type: Guides
    url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/
- name: Adobe Experience Manager API
  description: Content management and digital asset management APIs.
  image: https://www.adobe.com/content/dam/cc/icons/experience-manager.svg
  humanURL: https://developer.adobe.com/experience-manager/
  baseURL: https://aem.adobe.io
  tags:
  - Assets
  - Cms
  - Content
  - Dam
  properties:
  - type: Documentation
    url: https://developer.adobe.com/experience-manager/reference-materials/
  - type: Cloud Service
    url: https://experienceleague.adobe.com/docs/experience-manager-cloud-service.html
- name: Adobe Stock API
  description: Search and license stock photos, videos, and assets.
  image: https://www.adobe.com/content/dam/cc/icons/stock.svg
  humanURL: https://developer.adobe.com/stock/
  baseURL: https://stock.adobe.io
  tags:
  - Assets
  - Images
  - Licensing
  - Stock
  properties:
  - type: Documentation
    url: https://developer.adobe.com/stock/docs/
  - type: API Reference
    url: https://developer.adobe.com/stock/docs/api/
  - type: Affiliate
    url: https://developer.adobe.com/stock/docs/affiliate/
- name: Adobe Firefly API
  description: AI-powered generative image creation and editing.
  image: https://www.adobe.com/content/dam/cc/icons/firefly.svg
  humanURL: https://developer.adobe.com/firefly-services/
  baseURL: https://firefly.adobe.io
  tags:
  - Ai
  - Creative
  - Generative
  - Images
  properties:
  - type: Documentation
    url: https://developer.adobe.com/firefly-services/docs/
  - type: API Reference
    url: https://developer.adobe.com/firefly-services/docs/api/
  - type: Guides
    url: https://developer.adobe.com/firefly-services/docs/guides/
- name: Adobe Firefly Audio/Video APIs
  description: AI-powered audio and video APIs for automated content production at scale including dynamic graphics rendering, video reframing, translation and lip sync, text to speech, and text to avatar.
  image: https://www.adobe.com/content/dam/cc/icons/firefly.svg
  humanURL: https://developer.adobe.com/audio-video-firefly-services/
  baseURL: https://firefly.adobe.io
  tags:
  - Ai
  - Audio
  - Generative
  - Translation
  - Video
  properties:
  - type: Documentation
    url: https://developer.adobe.com/audio-video-firefly-services/
  - type: Getting Started
    url: https://developer.adobe.com/audio-video-firefly-services/getting-started/
  - type: Usage Notes
    url: https://developer.adobe.com/audio-video-firefly-services/getting_started/usage/
- name: Adobe Creative Cloud Libraries API
  description: Connect applications to Creative Cloud Libraries giving users access to stored creative elements like logos, colors, character styles, and graphics.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://developer.adobe.com/creative-cloud-libraries
  baseURL: https://cc-libraries.adobe.io
  tags:
  - Assets
  - Collaboration
  - Creative
  - Libraries
  properties:
  - type: Documentation
    url: https://developer.adobe.com/creative-cloud-libraries/docs/
  - type: API Reference
    url: https://developer.adobe.com/creative-cloud-libraries/docs/api/
  - type: Overview
    url: https://developer.adobe.com/creative-cloud-libraries/docs/overview/
  - type: Integration Guide
    url: https://developer.adobe.com/creative-cloud-libraries/docs/integrate/
- name: Adobe Express Embed SDK
  description: Embed the full Adobe Express editor and quick actions into web applications for creating and editing visual content with thousands of templates and assets.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://developer.adobe.com/express/
  baseURL: https://express.adobe.com
  tags:
  - Creative
  - Design
  - Embed
  - Templates
  properties:
  - type: Documentation
    url: https://developer.adobe.com/express/embed-sdk/docs/guides/
  - type: API Reference
    url: https://developer.adobe.com/express/embed-sdk/docs/v4/
  - type: Getting Started
    url: https://developer.adobe.com/express/embed-sdk/docs/guides/quickstart/
- name: Adobe Premiere Pro API
  description: Extend Premiere Pro with plugins, panels, and automation for video editing workflows including support for new file formats, effects, and transitions.
  image: https://www.adobe.com/content/dam/cc/icons/premiere.svg
  humanURL: https://developer.adobe.com/premiere-pro/
  baseURL: https://premiere.adobe.io
  tags:
  - Automation
  - Creative
  - Editing
  - Video
  properties:
  - type: Documentation
    url: https://developer.adobe.com/premiere-pro/
  - type: UXP API Reference
    url: https://developer.adobe.com/premiere-pro/uxp/ppro_reference/
- name: Adobe After Effects API
  description: Create visual effects, manipulate project elements, and automate complex tasks in After Effects through plugins, scripts, and panels.
  image: https://www.adobe.com/content/dam/cc/icons/aftereffects.svg
  humanURL: https://developer.adobe.com/after-effects/
  baseURL: https://aftereffects.adobe.io
  tags:
  - Animation
  - Creative
  - Effects
  - Video
  properties:
  - type: Documentation
    url: https://developer.adobe.com/after-effects/
- name: Adobe Experience Platform API
  description: Programmatically perform operations against Experience Platform data including data ingestion, catalog management, query services, and identity resolution.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://developer.adobe.com/experience-platform-apis/
  baseURL: https://platform.adobe.io
  tags:
  - Data
  - Experience
  - Marketing
  - Platform
  properties:
  - type: Documentation
    url: https://developer.adobe.com/experience-platform-apis/
  - type: Getting Started
    url: https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-guide
  - type: API Fundamentals
    url: https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-fundamentals
- name: Adobe Target API
  description: Manage personalization activities, audiences, offers, and deliver experiences across web, mobile, and IoT channels.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://developer.adobe.com/target/administer/admin-api/
  baseURL: https://mc.adobe.io
  tags:
  - Marketing
  - Optimization
  - Personalization
  - Testing
  properties:
  - type: Documentation
    url: https://experienceleague.adobe.com/en/docs/target-dev/developer/overview
  - type: Admin API
    url: https://developer.adobe.com/target/administer/admin-api/
  - type: Delivery API
    url: https://developer.adobe.com/target/implement/delivery-api/
  - type: API Overview
    url: https://experienceleague.adobe.com/en/docs/target-dev/developer/api/target-api-overview
- name: Adobe Campaign API
  description: Manage marketing campaigns, deliveries, workflows, subscriptions, and profiles through REST APIs for cross-channel campaign orchestration.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://experienceleague.adobe.com/en/docs/campaign/campaign-v8/developer/api
  baseURL: https://mc.adobe.io
  tags:
  - Automation
  - Campaigns
  - Email
  - Marketing
  properties:
  - type: Documentation
    url: https://experienceleague.adobe.com/en/docs/campaign/campaign-v8/developer/api
  - type: API Reference
    url: https://experienceleague.adobe.com/developer/campaign-api/api/index.html
- name: Adobe Marketo Engage API
  description: Access and manage marketing automation data including leads, accounts, opportunities, campaigns, and assets through REST APIs.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://developer.adobe.com/marketo-apis/
  baseURL: https://marketo.adobe.io
  tags:
  - Automation
  - Crm
  - Leads
  - Marketing
  properties:
  - type: Documentation
    url: https://developer.adobe.com/marketo-apis/
  - type: Developer Guide
    url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/home
  - type: REST API
    url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/rest-api
  - type: Authentication
    url: https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/authentication
- name: Adobe Commerce API
  description: Integrate with Adobe Commerce through REST and GraphQL APIs for managing products, orders, customers, and building headless commerce experiences.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://developer.adobe.com/commerce/webapi/
  baseURL: https://commerce.adobe.io
  tags:
  - Commerce
  - Ecommerce
  - Graphql
  - Rest
  properties:
  - type: Documentation
    url: https://developer.adobe.com/commerce/docs/
  - type: REST API
    url: https://developer.adobe.com/commerce/webapi/rest/
  - type: GraphQL API
    url: https://developer.adobe.com/commerce/webapi/graphql-api/
  - type: Getting Started
    url: https://developer.adobe.com/commerce/webapi/get-started/
  - type: REST API Reference
    url: https://developer.adobe.com/commerce/webapi/reference/rest/paas/
- name: Adobe User Management API
  description: Programmatically manage users, groups, and product entitlements for Adobe enterprise organizations.
  image: https://www.adobe.com/content/dam/cc/icons/adobe-logo.svg
  humanURL: https://developer.adobe.com/umapi/
  baseURL: https://usermanagement.adobe.io
  tags:
  - Enterprise
  - Identity
  - Management
  - Users
  properties:
  - type: Documentation
    url: https://developer.adobe.com/umapi/
  - type: API Reference
    url: https://adobe-apiplatform.github.io/umapi-documentation/en/RefOverview.html
  - type: Getting Started
    url: https://adobe-apiplatform.github.io/umapi-documentation/en/getstarted.html
name: Adobe Suite
tags:
- Ai
- Analytics
- Automation
- Commerce
- Creative
- Design
- Documents
- Experience
- Marketing
- Personalization
- Video
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of Adobe Creative Cloud and Experience Cloud APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


---
aid: adobe-creative-suite
url: https://raw.githubusercontent.com/api-evangelist/adobe-creative-suite/refs/heads/main/apis.yml
name: Adobe Creative Suite
description: Adobe Creative Suite is a collection of professional software applications for graphic design, video editing, web development, and photography.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
created: '2024-01-01'
modified: '2026-04-17'
specificationVersion: '0.19'
tags:
  - Creative
  - Design
  - Graphics
  - Photography
  - Video
apis:
  - name: Adobe Photoshop API
    description: The Adobe Photoshop API provides programmatic access to Photoshop image manipulation capabilities including automated editing, masking, and compositing. It enables developers to integrate Photoshop processing into workflows and applications without requiring a desktop installation. The API supports common Photoshop operations such as layer manipulation, smart object editing, and image transformation.
    image: https://www.adobe.com/content/dam/cc/icons/photoshop.svg
    humanURL: https://developer.adobe.com/photoshop/
    baseURL: https://image.adobe.io
    tags:
      - Automation
      - Graphics
      - Image Editing
      - Photoshop
    properties:
      - type: Documentation
        url: https://developer.adobe.com/photoshop/api/
      - type: OpenAPI
        url: https://developer.adobe.com/photoshop/api/openapi.json
      - type: OpenAPI
        url: openapi/adobe-creative-suite-photoshop-openapi.yml
      - type: JSONSchema
        url: json-schema/adobe-creative-suite-image-job-schema.json
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:photoshop-api
  - name: Adobe Lightroom API
    description: The Adobe Lightroom API provides access to photo management features including albums, collections, and editing presets stored in the Lightroom cloud catalog. Developers can use it to build integrations that read, organize, and manage photos on behalf of Lightroom users. The API uses OAuth 2.0 for user authentication and follows RESTful conventions.
    image: https://www.adobe.com/content/dam/cc/icons/lightroom.svg
    humanURL: https://developer.adobe.com/lightroom/
    baseURL: https://lr.adobe.io
    tags:
      - Editing
      - Lightroom
      - Photo Management
      - Photography
    properties:
      - type: Documentation
        url: https://developer.adobe.com/lightroom/api/
      - type: OpenAPI
        url: https://developer.adobe.com/lightroom/api/openapi.json
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:lightroom-api
  - name: Adobe Illustrator API
    description: The Adobe Illustrator API enables programmatic creation and manipulation of vector graphics through scripting and plugin interfaces. It exposes the Illustrator object model so developers can automate repetitive design tasks, generate artwork, and integrate Illustrator into production pipelines. The API is available via UXP plugins and CEP extensions as well as scripting environments.
    image: https://www.adobe.com/content/dam/cc/icons/illustrator.svg
    humanURL: https://developer.adobe.com/illustrator/
    baseURL: https://image.adobe.io
    tags:
      - Automation
      - Design
      - Illustrator
      - Vector Graphics
    properties:
      - type: Documentation
        url: https://developer.adobe.com/illustrator/api/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:illustrator-api
  - name: Adobe InDesign API
    description: The Adobe InDesign API allows developers to automate document layout and publishing workflows through scripting and UXP plugins. It exposes InDesign's document model for tasks such as batch exporting, template population, and preflight automation. The API supports JavaScript, AppleScript, and VBScript as well as the newer UXP plugin architecture.
    image: https://www.adobe.com/content/dam/cc/icons/indesign.svg
    humanURL: https://developer.adobe.com/indesign/
    baseURL: https://indesign-api.adobe.io
    tags:
      - Documents
      - InDesign
      - Layout
      - Publishing
    properties:
      - type: Documentation
        url: https://developer.adobe.com/indesign/uxp/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:indesign-api
  - name: Adobe Premiere Pro API
    description: The Adobe Premiere Pro API gives developers access to video editing automation through scripting and panel extensions. It allows integration with external media asset management systems, automated sequence assembly, and custom export workflows. The API is accessible through CEP extensions and the UXP plugin framework.
    image: https://www.adobe.com/content/dam/cc/icons/premiere.svg
    humanURL: https://developer.adobe.com/premiere-pro/
    baseURL: https://premiere-api.adobe.io
    tags:
      - Automation
      - Media
      - Premiere Pro
      - Video Editing
    properties:
      - type: Documentation
        url: https://developer.adobe.com/premiere-pro/docs/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:premiere-pro-api
  - name: Adobe After Effects API
    description: The Adobe After Effects API enables scripting and plugin development for motion graphics and visual effects workflows. Developers can automate rendering, manipulate compositions programmatically, and build custom effects using the SDK. The API supports ExtendScript, CEP panels, and the newer UXP and plugin SDK approaches.
    image: https://www.adobe.com/content/dam/cc/icons/after-effects.svg
    humanURL: https://developer.adobe.com/after-effects/
    baseURL: https://aftereffects-api.adobe.io
    tags:
      - After Effects
      - Animation
      - Motion Graphics
      - Visual Effects
    properties:
      - type: Documentation
        url: https://developer.adobe.com/after-effects/docs/
      - type: Reference
        url: https://ae-scripting.docsforadobe.dev/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:after-effects-api
  - name: Adobe Creative Cloud Libraries API
    description: The Adobe Creative Cloud Libraries API provides access to shared design assets stored in Creative Cloud Libraries, including colors, character styles, graphics, and components. It allows applications to read and write library elements on behalf of authenticated users. The API is commonly used to sync brand assets across design tools and third-party platforms.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/creative-cloud-libraries/
    baseURL: https://cc-libraries.adobe.io
    tags:
      - Assets
      - Collaboration
      - Creative Cloud
      - Libraries
    properties:
      - type: Documentation
        url: https://developer.adobe.com/creative-cloud-libraries/docs/
      - type: Reference
        url: https://developer.adobe.com/creative-cloud-libraries/api/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:creative-cloud-libraries-api
  - name: Adobe Stock API
    description: The Adobe Stock API enables search, licensing, and retrieval of stock photos, illustrations, vectors, videos, and templates from the Adobe Stock marketplace. It supports both editorial and commercial licensing workflows and can be integrated into creative applications and DAM systems. The API uses OAuth 2.0 and API key authentication depending on the operation.
    image: https://www.adobe.com/content/dam/cc/icons/stock.svg
    humanURL: https://developer.adobe.com/stock/
    baseURL: https://stock.adobe.io
    tags:
      - Images
      - Licensing
      - Stock
      - Video
    properties:
      - type: Documentation
        url: https://developer.adobe.com/stock/docs/
      - type: Reference
        url: https://developer.adobe.com/stock/docs/api/
      - type: OpenAPI
        url: https://developer.adobe.com/stock/docs/api/openapi.json
      - type: OpenAPI
        url: openapi/adobe-creative-suite-stock-openapi.yml
      - type: JSONSchema
        url: json-schema/adobe-creative-suite-stock-file-schema.json
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:stock-api
  - name: Adobe Firefly API
    description: The Adobe Firefly API provides access to Adobe's generative AI capabilities for creating and editing images, vectors, and text effects from natural language prompts. It is built on the Firefly family of creative generative models trained on licensed and public domain content. The API supports text-to-image generation, generative fill, generative expand, and style transfer operations.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/firefly-api/
    baseURL: https://firefly-api.adobe.io/v3
    tags:
      - Creative AI
      - Firefly
      - Generative AI
      - Image Generation
    properties:
      - type: Documentation
        url: https://developer.adobe.com/firefly-api/docs/
      - type: GettingStarted
        url: https://developer.adobe.com/firefly-api/docs/guides/get-started/
      - type: Reference
        url: https://developer.adobe.com/firefly-api/docs/api/
      - type: OpenAPI
        url: openapi/adobe-creative-suite-firefly-openapi.yml
      - type: JSONSchema
        url: json-schema/adobe-creative-suite-firefly-generation-schema.json
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:firefly-api
  - name: Adobe PDF Services API
    description: The Adobe PDF Services API provides cloud-based tools for creating, converting, combining, compressing, and extracting content from PDF documents. It is part of the Adobe Acrobat Services platform and supports operations such as HTML-to-PDF, PDF-to-Word, OCR, and PDF accessibility auto-tagging. The API offers SDKs for Java, Node.js, .NET, and Python.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/document-services/
    baseURL: https://pdf-services.adobe.io
    tags:
      - Acrobat
      - Document Conversion
      - Document Services
      - PDF
    properties:
      - type: Documentation
        url: https://developer.adobe.com/document-services/docs/overview/
      - type: GettingStarted
        url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/gettingstarted/
      - type: Reference
        url: https://developer.adobe.com/document-services/docs/apis/
      - type: Client Libraries
        url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/sdks/
      - type: OpenAPI
        url: openapi/adobe-creative-suite-pdf-services-openapi.yml
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:pdf-services-api
  - name: Adobe Analytics API
    description: The Adobe Analytics API provides programmatic access to Adobe Analytics report suites for retrieving, segmenting, and analyzing web and app behavioral data. It supports both the Reporting API for querying metrics and dimensions and the Data Insertion API for sending custom event data. The API is used to automate reporting, build custom dashboards, and integrate analytics data into external systems.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/analytics-apis/docs/2.0/
    baseURL: https://analytics.adobe.io/api
    tags:
      - Analytics
      - Data
      - Experience Cloud
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/2.0/
      - type: GettingStarted
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/
      - type: Reference
        url: https://developer.adobe.com/analytics-apis/docs/2.0/api/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:analytics-api
  - name: Adobe Experience Manager Assets API
    description: The Adobe Experience Manager Assets API provides access to the AEM digital asset management system for uploading, retrieving, and managing assets stored in AEM as a Cloud Service. It enables integration with external systems for asset ingestion, metadata management, and rendition retrieval. The API follows RESTful conventions and uses Adobe IMS for authentication.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/experience-manager/
    baseURL: https://author-{program}-{environment}.adobeaemcloud.com/api
    tags:
      - AEM
      - Content Management
      - Digital Asset Management
      - Experience Manager
    properties:
      - type: Documentation
        url: https://developer.adobe.com/experience-manager/reference-materials/cloud-service/javadoc/
      - type: GettingStarted
        url: https://developer.adobe.com/experience-manager/documentation/
      - type: Reference
        url: https://developer.adobe.com/experience-manager/reference-materials/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:experience-manager-assets-api
  - name: Adobe Acrobat Sign API
    description: The Adobe Acrobat Sign API enables sending, tracking, and managing electronic signature agreements programmatically. It supports creating agreements from documents or templates, managing signers and routing, and retrieving signed documents and audit trails. The API is available in region-specific deployments and uses OAuth 2.0 for authentication.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/adobesign/docs/
    baseURL: https://api.na1.adobesign.com/api/rest/v6
    tags:
      - Acrobat Sign
      - Agreements
      - Documents
      - Electronic Signatures
    properties:
      - type: Documentation
        url: https://developer.adobe.com/adobesign/docs/
      - type: GettingStarted
        url: https://developer.adobe.com/adobesign/docs/gstarted/
      - type: Reference
        url: https://developer.adobe.com/adobesign/docs/apis/
      - type: Authentication
        url: https://developer.adobe.com/adobesign/docs/gstarted/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:acrobat-sign-api
  - name: Adobe Fonts API
    description: The Adobe Fonts API provides access to the Adobe Fonts library for discovering and embedding web fonts in applications and websites. It allows querying font families, retrieving font metadata, and generating web font embed codes for use with Creative Cloud subscriptions. The API is commonly used by design tools and CMSs to expose the Adobe Fonts catalog to users.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://fonts.adobe.com/
    baseURL: https://fonts.adobe.io
    tags:
      - Design
      - Fonts
      - Typography
      - Web Fonts
    properties:
      - type: Documentation
        url: https://developer.adobe.com/fonts/docs/
      - type: Reference
        url: https://developer.adobe.com/fonts/docs/api/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:fonts-api
  - name: Adobe Express Embed SDK
    description: The Adobe Express Embed SDK allows developers to embed Adobe Express editing capabilities directly into their own web applications. It provides a customizable in-app editing experience for images, videos, and templates powered by the Adobe Express platform. The SDK supports use cases such as branded template creation, social media asset editing, and document design within third-party products.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/express/embed-sdk/
    baseURL: https://express-api.adobe.io
    tags:
      - Design
      - Embed SDK
      - Express
      - Templates
    properties:
      - type: Documentation
        url: https://developer.adobe.com/express/embed-sdk/docs/
      - type: GettingStarted
        url: https://developer.adobe.com/express/embed-sdk/docs/guides/getting_started/
      - type: Reference
        url: https://developer.adobe.com/express/embed-sdk/docs/reference/
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:express-embed-sdk
  - name: Adobe UXP
    description: Adobe UXP (Unified Extensibility Platform) is the modern plugin and scripting platform used across Adobe creative applications including Photoshop, InDesign, Illustrator, and XD. It provides a JavaScript-based runtime with access to application APIs, a React-compatible UI framework, and a unified plugin distribution system via the Creative Cloud marketplace. UXP replaces the older CEP (Common Extensibility Platform) and ExtendScript plugin architectures.
    image: https://www.adobe.com/content/dam/cc/icons/cc-icon.svg
    humanURL: https://developer.adobe.com/uxp/
    baseURL: https://developer.adobe.com/uxp/
    tags:
      - Creative Cloud
      - Extensibility
      - Plugins
      - UXP
    properties:
      - type: Documentation
        url: https://developer.adobe.com/uxp/docs/
      - type: GettingStarted
        url: https://developer.adobe.com/uxp/docs/guides/
      - type: Reference
        url: https://developer.adobe.com/uxp/docs/reference/
      - type: GitHubRepository
        url: https://github.com/adobe/uxp-photoshop
      - type: Authentication
        url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    contact:
      - FN: Adobe Developer Support
        url: https://developer.adobe.com/support/
    aid: adobe-creative-suite:uxp
common:
  - type: JSON-LD
    url: json-ld/adobe-creative-suite-context.jsonld
  - type: JSONSchema
    url: json-schema/adobe-creative-suite-image-job-schema.json
  - type: JSONSchema
    url: json-schema/adobe-creative-suite-firefly-generation-schema.json
  - type: JSONSchema
    url: json-schema/adobe-creative-suite-stock-file-schema.json
  - type: Portal
    url: https://developer.adobe.com/
  - type: SignUp
    url: https://developer.adobe.com/console/home
  - type: GettingStarted
    url: https://developer.adobe.com/developer-console/docs/guides/getting-started/
  - type: Documentation
    url: https://developer.adobe.com/developer-console/docs/
  - type: Blog
    url: https://blog.developer.adobe.com/
  - type: GitHub Organization
    url: https://github.com/adobe
  - type: Community
    url: https://community.adobe.com/t5/developers/ct-p/developers
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/adobe
  - type: Console
    url: https://developer.adobe.com/console/
  - type: Authentication
    url: https://developer.adobe.com/developer-console/docs/guides/authentication/
  - type: ChangeLog
    url: https://developer.adobe.com/developer-console/docs/release-notes/
  - type: Support
    url: https://developer.adobe.com/support/
  - type: StatusPage
    url: https://status.adobe.com/
  - type: TermsOfService
    url: https://www.adobe.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.adobe.com/privacy.html
  - type: Features
    data:
      - name: Cloud Image Processing
        description: Photoshop and Lightroom APIs for cloud-based image editing, background removal, and rendition generation.
      - name: Generative AI
        description: Adobe Firefly API for text-to-image generation, generative fill, and style transfer.
      - name: PDF Document Services
        description: Create, convert, extract, compress, and protect PDF documents programmatically.
      - name: Electronic Signatures
        description: Acrobat Sign API for creating and managing electronic signature workflows.
      - name: Stock Asset Licensing
        description: Search, preview, and license photos, vectors, and videos from Adobe Stock.
      - name: Creative Cloud Libraries
        description: Sync colors, styles, and design assets across Adobe applications.
      - name: Font Delivery
        description: Adobe Fonts API for web font delivery and typography management.
      - name: Video Editing Automation
        description: Premiere Pro and After Effects scripting for video production automation.
      - name: Vector Graphics Automation
        description: Illustrator scripting for vector artwork creation and batch processing.
      - name: Desktop Publishing
        description: InDesign Server and scripting for document layout automation.
      - name: Embeddable Creative Tools
        description: Adobe Express Embed SDK for integrating creative editing into web apps.
      - name: Plugin Development
        description: UXP framework for building modern plugins across Creative Cloud apps.
  - type: UseCases
    data:
      - name: Product Photography Automation
        description: Automate background removal, cropping, and enhancement for e-commerce.
      - name: Content Personalization at Scale
        description: Generate personalized visual content using Firefly and template automation.
      - name: Document Workflow Automation
        description: PDF creation, conversion, signing, and archiving workflows.
      - name: Brand Asset Management
        description: Centralize brand assets in Creative Cloud Libraries for consistent usage.
      - name: Video Production Pipeline
        description: Automate video editing, rendering, and export with Premiere Pro APIs.
      - name: Print Production
        description: Automate layout, typesetting, and print-ready output with InDesign.
      - name: Design System Generation
        description: Generate icon sets, components, and design tokens from data.
      - name: Web Asset Pipeline
        description: Export optimized SVGs, images, and fonts for web applications.
  - type: Solutions
    data:
      - name: Adobe Creative Cloud
        description: Complete suite of 20+ creative applications with API access.
      - name: Adobe Firefly Services
        description: Generative AI APIs combining Firefly, Photoshop, and Lightroom.
      - name: Adobe Acrobat Services
        description: PDF Services, Document Generation, and Acrobat Sign APIs.
      - name: Adobe Express
        description: Embeddable creative tools with quick actions and templates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

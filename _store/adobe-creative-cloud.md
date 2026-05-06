---
aid: adobe-creative-cloud
name: Adobe Creative Cloud
description: Adobe Creative Cloud is a suite of software and cloud services for graphic design, video editing, web development, photography, and 3D content creation. Its developer platform provides APIs for generative AI via Firefly Services, cloud storage and asset management, PDF document processing, electronic signatures, stock asset licensing, font delivery, and embeddable creative tools via the Express Embed SDK.
url: https://raw.githubusercontent.com/api-evangelist/adobe-creative-cloud/refs/heads/main/apis.yml
tags:
  - AI/ML
  - Cloud
  - Creative
  - Design
  - Documents
  - Photography
  - SaaS
  - Video
created: '2025-02-26'
modified: '2026-04-17'
specificationVersion: '0.19'
type: Index
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
apis:
  - aid: adobe-creative-cloud:firefly-api
    name: Adobe Firefly API
    tags:
      - AI/ML
      - Generative AI
      - Generative Fill
      - Image Generation
      - Text-To-Image
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://firefly-api.adobe.io/v2
    humanURL: https://developer.adobe.com/firefly-services/docs/firefly-api/
    properties:
      - url: https://developer.adobe.com/firefly-services/docs/firefly-api/
        type: Documentation
      - url: https://developer.adobe.com/firefly-services/docs/firefly-api/guides/
        type: GettingStarted
      - url: https://developer.adobe.com/firefly-services/docs/firefly-api/guides/api/
        type: APIReference
      - url: openapi/adobe-firefly-api-openapi-original.yml
        type: OpenAPI
    description: The Adobe Firefly API provides programmatic access to generative AI capabilities for image creation and manipulation. Key endpoints include text-to-image generation, generative fill for inpainting masked regions, image expansion for extending content beyond original boundaries, and style transfer for matching visual aesthetics.
  - aid: adobe-creative-cloud:express-embed-sdk
    name: Adobe Express Embed SDK
    tags:
      - Editor
      - Embed SDK
      - JavaScript
      - Quick Actions
      - Web Components
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/express/embed-sdk/docs/guides/
    properties:
      - url: https://developer.adobe.com/express/embed-sdk/docs/guides/
        type: Documentation
      - url: https://developer.adobe.com/express/embed-sdk/docs/guides/quickstart/
        type: GettingStarted
      - url: https://developer.adobe.com/express/embed-sdk/docs/v4/
        type: APIReference
      - url: https://github.com/AdobeDocs/cc-everywhere
        type: GitHubRepository
    description: A JavaScript SDK for embedding Adobe Express creative editing tools directly into web applications. The SDK provides a full editor component for design creation, quick actions for common image and video operations such as resize, crop, remove background, and convert formats, and template access for professional design starting points. Developers integrate using API keys from the Adobe Developer Console.
  - aid: adobe-creative-cloud:cc-libraries-api
    name: Creative Cloud Libraries API
    tags:
      - Assets
      - Collaboration
      - Colors
      - Libraries
      - Styles
      - Sync
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cc-libraries.adobe.io
    humanURL: https://developer.adobe.com/creative-cloud-libraries/
    properties:
      - url: https://developer.adobe.com/creative-cloud-libraries/docs/
        type: Documentation
      - url: https://developer.adobe.com/creative-cloud-libraries/docs/api/
        type: APIReference
      - url: https://github.com/AdobeDocs/creative-cloud-libraries
        type: GitHubRepository
      - url: openapi/adobe-cc-libraries-api-openapi-original.yml
        type: OpenAPI
    description: A REST API for accessing and managing Creative Cloud Libraries, enabling synchronization of colors, character styles, paragraph styles, graphics, and other creative assets across Adobe applications and custom integrations. The API supports creating, reading, updating, and deleting library elements, and includes an Asset Browser SDK for building web-based library browsing experiences.
  - aid: adobe-creative-cloud:cloud-storage-api
    name: Adobe Cloud Storage and Collaboration API
    tags:
      - Cloud Storage
      - Collaboration
      - Files
      - Projects
      - REST API
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/cloud-storage/
    properties:
      - url: https://developer.adobe.com/cloud-storage/
        type: Documentation
      - url: https://developer.adobe.com/cloud-storage/guides/api/
        type: APIReference
    description: A REST API for managing files, folders, and projects in Adobe Creative Cloud cloud storage. The API supports creating and organizing projects with hierarchical folder structures, uploading and downloading files, assigning user roles for collaboration, and integrating cloud storage operations into automated creative workflows. It provides programmatic access to the same cloud storage that Creative Cloud desktop and mobile applications use for file synchronization.
  - aid: adobe-creative-cloud:stock-api
    name: Adobe Stock API
    tags:
      - Assets
      - Licensing
      - Media
      - Search
      - Stock Photos
      - Vectors
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://stock.adobe.io
    humanURL: https://developer.adobe.com/stock/
    properties:
      - url: https://developer.adobe.com/stock/docs/
        type: Documentation
      - url: https://developer.adobe.com/stock/docs/api/
        type: APIReference
      - url: https://developer.adobe.com/stock/docs/api/11-search-reference/
        type: APIReference
      - url: https://developer.adobe.com/stock/docs/api/12-licensing-reference/
        type: APIReference
      - url: https://github.com/adobe/stock-api-sdk
        type: GitHubRepository
      - url: openapi/adobe-stock-api-openapi-original.yml
        type: OpenAPI
    description: A REST API for searching, licensing, and integrating Adobe Stock assets including photos, vectors, illustrations, videos, templates, and 3D content into applications and workflows. The Search API enables querying the Stock catalog with filters for asset type, orientation, color, and keywords. The Licensing API handles asset licensing and high-resolution download. Additional endpoints provide license history retrieval and member profile information.
  - aid: adobe-creative-cloud:fonts-api
    name: Adobe Fonts API
    tags:
      - Fonts
      - Kits
      - Typekit
      - Typography
      - Web Fonts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://typekit.com/api
    humanURL: https://developer.adobe.com/fonts/
    properties:
      - url: https://fonts.adobe.com/docs/api
        type: Documentation
      - url: https://github.com/typekit/fonts-api-docs
        type: GitHubRepository
    description: The Adobe Fonts API (formerly Typekit API) provides programmatic access to Adobe's font library for web and application integration. The API supports querying font family information and variations, creating and managing font kits for web deployment, generating font preview data, and retrieving font metadata. Kits are collections of fonts configured for specific domains and published to Adobe's CDN for web font delivery. Authentication uses user tokens generated via the Typekit API Token page.
  - aid: adobe-creative-cloud:pdf-services-api
    name: Adobe PDF Services API
    tags:
      - Acrobat Services
      - Conversion
      - Document Processing
      - Extraction
      - OCR
      - PDF
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pdf-services.adobe.io
    humanURL: https://developer.adobe.com/document-services/apis/pdf-services/
    properties:
      - url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/
        type: Documentation
      - url: https://developer.adobe.com/document-services/docs/apis/
        type: APIReference
      - url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/quickstarts/
        type: GettingStarted
      - url: openapi/adobe-pdf-services-api-openapi-original.yml
        type: OpenAPI
    description: A cloud-based REST API for creating, converting, and manipulating PDF documents programmatically. Part of Adobe Acrobat Services, the API supports PDF creation from HTML, images, and Office formats, conversion to and from multiple formats, OCR for scanned documents, document compression, password protection, content extraction with AI-powered text, table, and image recognition, and accessibility auto-tagging. SDKs are available for Java, Node.js, Python, and .NET.
  - aid: adobe-creative-cloud:document-generation-api
    name: Adobe Document Generation API
    tags:
      - Data Merge
      - Document Generation
      - PDF
      - Templates
      - Word
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://pdf-services.adobe.io
    humanURL: https://developer.adobe.com/document-services/docs/overview/document-generation-api/
    properties:
      - url: https://developer.adobe.com/document-services/docs/overview/document-generation-api/
        type: Documentation
      - url: https://developer.adobe.com/document-services/docs/overview/document-generation-api/gettingstarted/
        type: GettingStarted
    description: A REST API for generating PDF and Word documents by merging JSON data into Microsoft Word templates. Part of Adobe Acrobat Services, the API supports conditional content insertion, dynamic table generation, ordered and unordered list creation, image placement, and JSONata expression evaluation within templates. The Adobe Document Tagger Word add-in assists with template authoring by inserting tags for data binding.
  - aid: adobe-creative-cloud:acrobat-sign-api
    name: Acrobat Sign API
    tags:
      - Agreements
      - Compliance
      - Documents
      - Electronic Signatures
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/document-services/apis/sign-api/
    properties:
      - url: https://developer.adobe.com/document-services/apis/sign-api/
        type: Documentation
      - url: https://opensource.adobe.com/acrobat-sign/developer_guide/index.html
        type: APIReference
      - url: https://experienceleague.adobe.com/en/docs/acrobat-services-learn/tutorials/acrobatsign/signapi
        type: GettingStarted
    description: A REST API for creating and managing electronic signature workflows programmatically. The API supports document upload, agreement creation with configurable signing flows, real-time status tracking via webhooks, signed document retrieval, and embedded e-signature experiences within custom applications. Acrobat Sign is compliant with SOC 2 Type 2, ISO 27001, FedRAMP Tailored, and PCI DSS.
  - aid: adobe-creative-cloud:io-events
    name: Adobe I/O Events
    tags:
      - Event-Driven
      - Events
      - Notifications
      - Real-Time
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/events/
    properties:
      - url: https://developer.adobe.com/events/docs/guides/
        type: Documentation
      - url: https://github.com/AdobeDocs/adobeio-events
        type: GitHubRepository
      - url: asyncapi/adobe-io-events-asyncapi-original.yml
        type: AsyncAPI
    description: Adobe I/O Events provides an event-driven webhook infrastructure for subscribing to changes across Adobe services. Developers register webhook endpoints to receive real-time HTTP POST notifications when events occur, such as Creative Cloud Libraries asset updates, Photoshop API job completions, or Experience Cloud data changes. Webhook payloads include an x-adobe-signature header for authenticity verification.
  - aid: adobe-creative-cloud:io-runtime
    name: Adobe I/O Runtime
    tags:
      - Cloud Computing
      - FaaS
      - Functions
      - OpenWhisk
      - Serverless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/app-builder/docs/get_started/runtime_getting_started/
    properties:
      - url: https://developer.adobe.com/app-builder/docs/get_started/runtime_getting_started/
        type: Documentation
      - url: https://adobedocs.github.io/adobeio-runtime/
        type: Documentation
    description: A serverless computing platform built on Apache OpenWhisk that enables developers to deploy and execute custom code on Adobe's cloud infrastructure. I/O Runtime supports event-driven and HTTP-triggered function execution in JavaScript, Python, and other languages. Functions can be invoked via REST API or CLI and integrate natively with Adobe I/O Events for reactive workflows.
  - aid: adobe-creative-cloud:app-builder
    name: Adobe App Builder
    tags:
      - Application Framework
      - Custom Apps
      - Enterprise
      - React Spectrum
      - SPA
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/app-builder/
    properties:
      - url: https://developer.adobe.com/app-builder/docs/overview/
        type: Documentation
      - url: https://developer.adobe.com/app-builder/docs/intro_and_overview/
        type: GettingStarted
    description: A complete application development framework for building custom enterprise applications on Adobe infrastructure. App Builder combines Adobe I/O Runtime for serverless backend functions, Adobe I/O Events for event-driven architecture, and React Spectrum for consistent UI components. Developers can build headful single-page applications or headless microservices that extend Adobe Experience Cloud solutions.
  - aid: adobe-creative-cloud:uxp
    name: Adobe UXP (Unified Extensibility Platform)
    tags:
      - Cross-App
      - Extensions
      - HTML/CSS
      - JavaScript
      - Modern
      - Plugin Framework
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/photoshop/uxp/2022/
    properties:
      - url: https://developer.adobe.com/photoshop/uxp/2022/
        type: Documentation
      - url: https://github.com/adobe/cc-ext-uxp-types
        type: GitHubRepository
    description: The Unified Extensibility Platform (UXP) is Adobe's modern cross-app plugin development framework replacing the legacy CEP platform. UXP uses a JavaScript engine with support for ES6+ and provides a common set of platform APIs for file system access, network I/O, and UI rendering using HTML, CSS, and curated Spectrum design components. Plugins built with UXP run natively within Creative Cloud desktop applications including Photoshop, InDesign, Illustrator, Premiere Pro, and XD.
  - aid: adobe-creative-cloud:cep
    name: Adobe CEP (Common Extensibility Platform)
    tags:
      - ExtendScript
      - HTML5
      - Legacy
      - Panels
      - Plugin Framework
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://adobe-cep.github.io/CEP-Resources/
    properties:
      - url: https://adobe-cep.github.io/CEP-Resources/
        type: Documentation
      - url: https://github.com/Adobe-CEP/CEP-Resources
        type: GitHubRepository
      - url: https://github.com/Adobe-CEP/Getting-Started-guides
        type: GitHubRepository
      - url: json-schema/adobe-cep-extension-manifest-schema.json
        type: JSONSchema
    description: The Common Extensibility Platform (CEP) is Adobe's legacy framework for building integrated HTML5 panels across multiple Creative Cloud desktop applications. CEP panels use HTML5, CSS, and JavaScript for the UI layer and communicate with application DOMs through ExtendScript. The framework supports InDesign, Photoshop, Illustrator, Premiere Pro, Audition, After Effects, and other CC applications.
  - aid: adobe-creative-cloud:photoshop-api
    name: Adobe Photoshop API
    tags:
      - Automation
      - Cloud
      - Firefly Services
      - Image Processing
      - Photoshop
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://image.adobe.io
    humanURL: https://developer.adobe.com/photoshop/
    properties:
      - url: https://developer.adobe.com/firefly-services/docs/photoshop/
        type: Documentation
      - url: https://developer.adobe.com/firefly-services/docs/photoshop/api/
        type: APIReference
    description: A cloud-based REST API that provides programmatic access to Photoshop's image editing capabilities without requiring a local installation. Part of Adobe Firefly Services, the API supports PSD document operations, layer editing, Smart Object replacement, text layer editing, background removal, mask creation, product crop, depth blur, and Photoshop Actions execution. All operations are asynchronous, returning a polling URL to check job status.
  - aid: adobe-creative-cloud:lightroom-api
    name: Adobe Lightroom API
    tags:
      - Cloud
      - Image Editing
      - Photo Management
      - Photography
      - Presets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://lr.adobe.io
    humanURL: https://developer.adobe.com/lightroom/
    properties:
      - url: https://developer.adobe.com/lightroom/lightroom-api-docs/
        type: Documentation
      - url: https://developer.adobe.com/lightroom/lightroom-api-docs/api/
        type: APIReference
    description: A REST API for managing photos, albums, and applying presets in Adobe Lightroom, enabling automated photo organization and editing workflows. The API provides programmatic access to Lightroom's cloud-based photo library including uploading and downloading photos, creating and managing albums, applying editing presets, and retrieving photo metadata. Part of Adobe Firefly Services for cloud-based image processing automation.
  - aid: adobe-creative-cloud:developer-distribution
    name: Adobe Developer Distribution
    tags:
      - Exchange
      - Marketplace
      - Plugin Distribution
      - Publishing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/developer-distribution/creative-cloud/
    properties:
      - url: https://developer.adobe.com/developer-distribution/creative-cloud/
        type: Documentation
      - url: https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/getting-started
        type: GettingStarted
      - url: https://developer.adobe.com/developer-distribution/creative-cloud/docs/guides/submission/overview
        type: Documentation
    description: The Adobe Developer Distribution portal for publishing and managing plugins and extensions in the Creative Cloud Marketplace and Adobe Exchange. Supports UXP plugins, CEP extensions (ZXP format), and other extension types across Creative Cloud applications. The portal provides listing management, version control, metadata editing, scheduled and immediate publication, and the ability to recall or retract published listings.
common:
  - url: https://developer.adobe.com/
    type: Portal
    description: Adobe Developer portal with centralized access to all APIs, SDKs, documentation, and developer tools.
  - url: https://developer.adobe.com/creative-cloud/
    type: Portal
    description: Creative Cloud developer platform with resources for extension development, API integration, and creative workflow automation.
  - url: https://developer.adobe.com/apis
    type: Documentation
    description: Adobe API catalog listing all available APIs with documentation links, categories, and access information.
  - url: https://developer.adobe.com/developer-console/
    type: Portal
    description: Adobe Developer Console for creating projects, managing API credentials, configuring OAuth, and monitoring usage.
  - url: https://developer.adobe.com/developer-console/docs/guides/authentication/
    type: Authentication
    description: Authentication documentation covering OAuth Server-to-Server credentials, user authentication, and API key configuration.
  - url: https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/
    type: Authentication
    description: OAuth Server-to-Server credential documentation, the current standard replacing deprecated JWT Service Account credentials.
  - url: https://www.adobe.com/creativecloud.html
    type: Website
    description: Adobe Creative Cloud product page with plans, pricing, and application information.
  - url: https://blog.developer.adobe.com/
    type: Blog
    description: Adobe Developers blog with technical articles, API updates, and developer community news.
  - url: https://medium.com/adobetech
    type: Blog
    description: Adobe Tech Blog on Medium with in-depth technical posts from Adobe engineers.
  - url: https://forums.creativeclouddeveloper.com
    type: Forum
    description: Creative Cloud developer forums for plugin development, API integration, and extension discussions.
  - url: https://community.adobe.com/
    type: Forum
    description: Adobe Community forums for general product support, questions, and peer discussions.
  - url: https://github.com/adobe
    type: GitHubOrganization
    description: Adobe GitHub organization with open source projects, SDKs, and developer tools.
  - url: https://github.com/AdobeDocs
    type: GitHubOrganization
    description: Adobe documentation GitHub organization with API documentation source repositories and samples.
  - url: https://github.com/Adobe-CEP
    type: GitHubOrganization
    description: Adobe CEP GitHub organization with Common Extensibility Platform resources, samples, and getting started guides.
  - url: https://developer.adobe.com/support/
    type: Support
    description: Adobe Developer support center for API and SDK technical assistance.
  - url: https://developer.adobe.com/document-services/pricing/main/
    type: Pricing
    description: Adobe Acrobat Services pricing for PDF Services API and Document Generation API including free tier details.
  - url: https://status.adobe.com/
    type: Status
    description: Adobe service status dashboard showing availability for Creative Cloud APIs and services.
  - url: https://developer.adobe.com/adobe-status/
    type: Documentation
    description: Adobe Status API documentation for programmatic service health monitoring.
  - url: https://helpx.adobe.com/security.html
    type: Security
    description: Adobe security bulletins and advisories with vulnerability disclosures across Adobe products.
  - url: https://x.com/AdobeDevs
    type: X
    description: Adobe Developers account on X with API updates, developer events, and community highlights.
  - url: https://www.youtube.com/@AdobeCreativeCloud
    type: YouTube
    description: Adobe Creative Cloud YouTube channel with tutorials, feature demos, and developer content.
  - url: https://www.adobe.com/legal/terms.html
    type: TermsOfService
    description: Adobe General Terms of Use governing the use of Adobe products and services.
  - url: https://www.adobe.com/privacy/policy.html
    type: PrivacyPolicy
    description: Adobe Privacy Policy detailing data collection, usage, and protection practices.
  - url: https://www.adobe.com/legal/licenses-terms.html
    type: License
    description: Adobe product licenses and terms including end user license agreements for Creative Cloud applications.
  - type: Features
    data:
      - name: Generative AI Image Creation
        description: Generate images from text prompts, fill masked regions, and expand images using Adobe Firefly AI models.
      - name: PDF Document Processing
        description: Create, convert, extract, compress, OCR, and protect PDF documents programmatically.
      - name: Electronic Signatures
        description: Create and manage electronic signature workflows with Acrobat Sign for agreement lifecycle management.
      - name: Stock Asset Licensing
        description: Search, preview, and license photos, vectors, videos, and templates from Adobe Stock.
      - name: Creative Cloud Libraries
        description: Sync colors, styles, graphics, and design assets across Adobe applications and custom integrations.
      - name: Cloud Storage
        description: Manage files, folders, and projects in Creative Cloud cloud storage with collaboration.
      - name: Font Delivery
        description: Access and deliver Adobe Fonts (formerly Typekit) for web and application typography.
      - name: Embeddable Creative Tools
        description: Embed Adobe Express editor and quick actions in web applications via the Embed SDK.
      - name: Plugin Development
        description: Build extensions for Photoshop, InDesign, Illustrator, and other CC apps using UXP or CEP.
      - name: Event-Driven Webhooks
        description: Subscribe to real-time notifications for changes across Adobe services via I/O Events.
      - name: Cloud Image Processing
        description: Automate Photoshop and Lightroom operations in the cloud without local installations.
      - name: Document Generation
        description: Generate PDFs and Word documents by merging JSON data into templates.
  - type: UseCases
    data:
      - name: Creative Asset Automation
        description: Automate image generation, editing, and processing workflows using Firefly and Photoshop APIs.
      - name: Document Workflow Automation
        description: Generate, convert, sign, and archive documents using PDF Services and Acrobat Sign.
      - name: E-commerce Product Images
        description: Use Firefly generative fill and Photoshop background removal for product photography automation.
      - name: Brand Asset Management
        description: Sync brand colors, fonts, and assets across teams using Creative Cloud Libraries API.
      - name: Content Personalization
        description: Generate personalized visual content at scale using Firefly text-to-image for marketing campaigns.
      - name: Digital Publishing
        description: Automate PDF creation, compression, and accessibility tagging for digital publication workflows.
      - name: Contract Management
        description: Create, send, sign, and track electronic agreements with Acrobat Sign API integration.
      - name: Stock Asset Integration
        description: Embed Adobe Stock search and licensing into content management and publishing platforms.
  - type: Integrations
    data:
      - name: Microsoft Office
        description: PDF Services integration with Word, Excel, and PowerPoint for document conversion.
      - name: Salesforce
        description: Acrobat Sign integration with Salesforce for electronic signature workflows in CRM.
      - name: Workday
        description: Acrobat Sign integration with Workday for HR document signing workflows.
      - name: Adobe Experience Cloud
        description: Integration with AEM, Analytics, and Target for enterprise content management.
      - name: Slack
        description: Acrobat Sign notifications and signing workflows within Slack channels.
      - name: GitHub
        description: Open-source SDKs and documentation repositories for developer integration.
  - type: Solutions
    data:
      - name: Creative Cloud All Apps
        description: Complete suite of 20+ creative applications with API access for desktop and cloud workflows.
      - name: Adobe Firefly Services
        description: Generative AI APIs combining Firefly, Photoshop, and Lightroom for cloud image processing.
      - name: Adobe Acrobat Services
        description: PDF Services, Document Generation, and Acrobat Sign APIs for document workflow automation.
      - name: Adobe App Builder
        description: Full-stack application framework for building custom enterprise extensions on Adobe infrastructure.
---

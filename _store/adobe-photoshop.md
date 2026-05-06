---
aid: adobe-photoshop
name: Adobe Photoshop
description: Adobe Photoshop is the industry-standard image editing and digital design application. Its developer platform offers a cloud-based REST API for programmatic image processing via Firefly Services, the UXP plugin framework for building desktop extensions with modern JavaScript, a C++ plugin SDK for native filters and file formats, and scripting interfaces for workflow automation.
url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/apis.yml
tags:
  - AI/ML
  - Creative Cloud
  - Image Editing
  - Photoshop
  - Plugins
  - REST API
  - Scripting
created: '2025-02-28'
modified: '2026-04-17'
specificationVersion: '0.19'
type: Index
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
apis:
  - aid: adobe-photoshop:photoshop-api
    name: Adobe Photoshop API
    tags:
      - AI/ML
      - Asynchronous
      - Background Removal
      - Cloud
      - Image Processing
      - PSD Editing
      - REST API
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://image.adobe.io
    humanURL: https://developer.adobe.com/firefly-services/docs/photoshop/
    properties:
      - url: https://developer.adobe.com/firefly-services/docs/photoshop/
        type: Documentation
      - url: openapi/adobe-photoshop-api-openapi-original.yml
        type: OpenAPI
      - url: asyncapi/adobe-photoshop-api-asyncapi-original.yml
        type: AsyncAPI
      - url: https://developer.adobe.com/firefly-services/docs/photoshop/api/
        type: APIReference
      - url: https://developer.adobe.com/firefly-services/docs/photoshop/getting_started/
        type: GettingStarted
    description: A cloud-based REST API that provides programmatic access to Photoshop's image editing capabilities without requiring a local installation. Part of Adobe Firefly Services, the API supports PSD document operations including layer editing, Smart Object replacement, text layer editing, and artboard creation. It also provides AI-powered features such as background removal, mask creation, product crop, and depth blur.
  - aid: adobe-photoshop:firefly-services-sdk
    name: Adobe Firefly Services SDK for JavaScript
    tags:
      - Client Library
      - Node.js
      - NPM
      - SDK
      - TypeScript
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://image.adobe.io
    humanURL: https://developer.adobe.com/firefly-services/docs/guides/sdks/
    properties:
      - url: https://developer.adobe.com/firefly-services/docs/guides/sdks/
        type: Documentation
      - url: https://github.com/Firefly-Services/firefly-services-sdk-js
        type: GitHubRepository
      - url: https://www.npmjs.com/package/@adobe/photoshop-apis
        type: NPMPackage
    description: A unified Node.js and TypeScript SDK that provides typed client libraries for accessing the Photoshop API and other Firefly Services. The PhotoshopClient class offers methods for background removal, mask creation, PSD rendition generation, document creation and modification, Smart Object replacement, text layer editing, Photoshop Actions execution, auto crop, and depth blur.
  - aid: adobe-photoshop:uxp-plugin-api
    name: Adobe Photoshop UXP Plugin API
    tags:
      - Desktop
      - DOM API
      - HTML/CSS
      - JavaScript
      - Plugin Platform
      - Spectrum UI
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/photoshop/uxp/2022/
    properties:
      - url: https://developer.adobe.com/photoshop/uxp/2022/
        type: Documentation
      - url: https://developer.adobe.com/photoshop/uxp/2022/ps_reference/
        type: APIReference
      - url: https://developer.adobe.com/photoshop/uxp/2022/uxp-api/
        type: APIReference
      - url: https://developer.adobe.com/photoshop/uxp/2022/guides/
        type: GettingStarted
      - url: json-schema/adobe-photoshop-uxp-plugin-manifest-schema.json
        type: JSONSchema
    description: The modern plugin development platform for Photoshop, replacing the legacy CEP framework. UXP (Unified Extensibility Platform) is powered by a V8 JavaScript engine supporting ES6+ and provides Spectrum design components for building panels and dialogs using HTML, CSS, and modern JavaScript. Plugins access a rich Photoshop DOM API for interacting with documents, layers, and actions, along with platform APIs for file system access, network I/O, clipboard operations, and more.
  - aid: adobe-photoshop:uxp-scripting
    name: Adobe Photoshop UXP Scripting
    tags:
      - Automation
      - JavaScript
      - Modern JS
      - Scripting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/photoshop/uxp/2022/scripting/
    properties:
      - url: https://developer.adobe.com/photoshop/uxp/2022/scripting/
        type: Documentation
      - url: https://developer.adobe.com/photoshop/uxp/2022/ps_reference/media/uxpscripting/
        type: APIReference
    description: A modern scripting system for Photoshop that allows developers to execute standalone JavaScript files with the .psjs extension to automate tasks. Unlike full UXP plugins, scripts are single files that run once and complete, similar to the legacy ExtendScript workflow but using modern JavaScript powered by the V8 engine.
  - aid: adobe-photoshop:uxp-hybrid-plugins
    name: Adobe Photoshop UXP Hybrid Plugins
    tags:
      - C++
      - Filters
      - Hybrid
      - Native Code
      - Performance
      - Plugin
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/photoshop/uxp/2022/guides/hybrid-plugins/
    properties:
      - url: https://developer.adobe.com/photoshop/uxp/2022/guides/hybrid-plugins/
        type: Documentation
      - url: https://developer.adobe.com/photoshop/uxp/2022/guides/hybrid-plugins/getting-started/
        type: GettingStarted
      - url: https://developer.adobe.com/photoshop/uxp/2022/ps_reference/media/cpp-pluginsdk/
        type: APIReference
    description: A specialized plugin type that combines UXP's JavaScript, HTML, and CSS plugin framework with native C++ code compiled as a .uxpaddon. This allows developers to write performance-critical code in C++ such as pixel-level image processing while using UXP for the user interface layer. Hybrid plugins can integrate with the traditional Photoshop C++ SDK to create filters that appear in Photoshop's Filter menu or implement new file format support. Requires Photoshop v24.2.0 or later.
  - aid: adobe-photoshop:cpp-plugin-sdk
    name: Adobe Photoshop C++ Plugin SDK
    tags:
      - C++
      - Desktop
      - File Formats
      - Filters
      - Native SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.adobe.com/photoshop/
    properties:
      - url: https://developer.adobe.com/photoshop/
        type: Documentation
      - url: https://github.com/AdobeDocs/photoshop-cpp-sdk
        type: GitHubRepository
    description: A C++ based SDK for building low-level native Photoshop plugins. The SDK enables developers to extend Photoshop in seven categories including filters appearing under the Filter menu, file format import and export support, selection tools, color pickers, automation plugins, measurement tools, and 3D import and export. It provides direct access to Photoshop's internal pixel data and rendering pipeline for maximum performance.
  - aid: adobe-photoshop:extendscript-scripting
    name: Adobe Photoshop ExtendScript Scripting API
    tags:
      - Automation
      - ExtendScript
      - JSX
      - Legacy
      - Scripting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://extendscript.docsforadobe.dev/
    properties:
      - url: https://extendscript.docsforadobe.dev/
        type: Documentation
      - url: https://developer.adobe.com/photoshop/uxp/2022/guides/uxp_for_you/uxp_for_extendscript_devs/
        type: Documentation
      - url: https://github.com/adobe-uxp/ps-es-to-uxp
        type: GitHubRepository
    description: The legacy scripting system based on ExtendScript, Adobe's implementation of ECMAScript 3. ExtendScript scripts use the .jsx file extension and can automate nearly all Photoshop operations through a comprehensive Application, Document, and Layer object model. Scripts can also be written in AppleScript on macOS or VBScript on Windows.
common:
  - url: https://developer.adobe.com/photoshop/
    type: Portal
    description: Adobe Photoshop developer landing page with links to all APIs, SDKs, plugins, and scripting resources.
  - url: https://developer.adobe.com/firefly-services/docs/photoshop/
    type: Documentation
    description: Adobe Photoshop API documentation as part of Firefly Services with guides, API reference, and code samples.
  - url: https://developer.adobe.com/photoshop/uxp/2022/
    type: Documentation
    description: UXP plugin and scripting documentation for Adobe Photoshop desktop development.
  - url: https://developer.adobe.com/firefly-services/docs/photoshop/getting_started/
    type: GettingStarted
    description: Getting started guide for the Photoshop API including authentication setup and first API calls.
  - url: https://developer.adobe.com/developer-console/
    type: Portal
    description: Adobe Developer Console for managing API credentials, projects, and OAuth integrations.
  - url: https://developer.adobe.com/firefly-services/docs/photoshop/api/
    type: APIReference
    description: Complete API reference for all Photoshop API endpoints including request and response schemas.
  - url: https://developer.adobe.com/firefly-services/docs/guides/sdks/
    type: Documentation
    description: Firefly Services SDK documentation for Node.js and TypeScript client libraries.
  - url: https://github.com/Firefly-Services/firefly-services-sdk-js
    type: GitHubRepository
    description: GitHub repository for the Firefly Services SDK for JavaScript including PhotoshopClient source code and documentation.
  - url: https://github.com/AdobeDocs/photoshop-cpp-sdk
    type: GitHubRepository
    description: GitHub repository for the Photoshop C++ Plugin SDK documentation and resources.
  - url: https://www.adobe.com/products/photoshop.html
    type: Website
    description: Adobe Photoshop product page with features, pricing, and plan information.
  - url: https://blog.developer.adobe.com/
    type: Blog
    description: Adobe Developers blog with technical articles, API updates, and developer community news.
  - url: https://community.adobe.com/t5/photoshop-ecosystem-discussions/bd-p/photoshop
    type: Forum
    description: Adobe Community forum for Photoshop discussions, plugin development questions, and peer support.
  - url: https://forums.creativeclouddeveloper.com
    type: Forum
    description: Creative Cloud developer forums for plugin and extension development discussions across Adobe products.
  - url: https://status.adobe.com/
    type: Status
    description: Adobe service status dashboard showing availability for Photoshop API and other Adobe services.
  - url: https://helpx.adobe.com/security/products/photoshop.html
    type: Security
    description: Adobe Photoshop security bulletins and advisories with vulnerability disclosures and patch information.
  - url: https://x.com/Photoshop
    type: X
    description: Official Adobe Photoshop account on X with product updates and creative inspiration.
  - url: https://www.youtube.com/@AdobeCreativeCloud
    type: YouTube
    description: Adobe Creative Cloud YouTube channel with Photoshop tutorials, feature demos, and workflow tips.
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
      - name: Cloud Image Processing
        description: Process images in the cloud without local Photoshop installation via the REST API.
      - name: Background Removal
        description: AI-powered automatic background removal and mask generation.
      - name: PSD Document Editing
        description: Create, read, and modify PSD files including layers, Smart Objects, and text.
      - name: Generative Fill
        description: AI-powered content generation to fill, extend, or replace image regions.
      - name: Smart Object Replacement
        description: Replace embedded Smart Object content across PSD templates programmatically.
      - name: Text Layer Editing
        description: Modify text content, fonts, colors, and styling in PSD text layers.
      - name: Photoshop Actions Execution
        description: Run recorded Photoshop Actions (.atn files) on images in the cloud.
      - name: UXP Plugin Framework
        description: Build desktop plugins with modern JavaScript, HTML, CSS, and Spectrum UI components.
      - name: C++ Plugin SDK
        description: Create native filters, file format support, and selection tools with the C++ SDK.
      - name: ExtendScript Automation
        description: Legacy scripting interface for batch processing and workflow automation.
      - name: Product Crop
        description: AI-powered automatic cropping to isolate product subjects.
      - name: Depth Blur
        description: Apply realistic depth-of-field blur effects using AI depth estimation.
  - type: UseCases
    data:
      - name: Product Photography Automation
        description: Automate background removal, product crop, and image enhancement for e-commerce catalogs.
      - name: Template-Based Design Generation
        description: Replace Smart Objects in PSD templates to generate personalized marketing materials at scale.
      - name: Batch Image Processing
        description: Process thousands of images with consistent edits using the cloud API or Actions.
      - name: Creative Workflow Plugins
        description: Build UXP plugins that add custom panels, automate tasks, and integrate with external services.
      - name: Image Format Conversion
        description: Convert between PSD, JPEG, PNG, TIFF, and other formats programmatically.
      - name: Content-Aware Editing
        description: Use generative fill and AI features to extend, modify, or enhance image content.
      - name: Print Production Automation
        description: Automate print-ready output generation with proper color spaces and bleed settings.
      - name: DAM Integration
        description: Connect digital asset management systems with Photoshop for automated processing pipelines.
  - type: Integrations
    data:
      - name: Adobe Creative Cloud
        description: Native integration with other Creative Cloud apps via shared libraries and cloud storage.
      - name: Adobe Lightroom
        description: Roundtrip editing between Lightroom and Photoshop for photography workflows.
      - name: Adobe Firefly
        description: Generative AI features powered by Adobe Firefly for content creation.
      - name: Cloud Storage Providers
        description: API supports input/output from AWS S3, Azure Blob, Google Cloud Storage, and Dropbox.
  - type: Solutions
    data:
      - name: Photoshop API (Firefly Services)
        description: Cloud-based REST API for programmatic image processing at scale.
      - name: Photoshop Desktop (UXP)
        description: Modern plugin platform for extending Photoshop with JavaScript and HTML.
      - name: Photoshop Desktop (C++ SDK)
        description: Native plugin SDK for filters, file formats, and performance-critical extensions.
      - name: Photoshop Scripting
        description: Automation via UXP scripts (.psjs) or legacy ExtendScript (.jsx).
---

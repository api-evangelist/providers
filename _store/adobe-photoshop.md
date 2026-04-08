---
aid: adobe-photoshop
url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/apis.yml
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
name: Adobe Photoshop
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Adobe Photoshop is the industry-standard image editing and digital design application. Its developer platform offers a cloud-based REST API for programmatic image processing via Firefly Services, the UXP plugin framework for building desktop extensions with modern JavaScript, a C++ plugin SDK for native filters and file formats, and scripting interfaces for workflow automation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


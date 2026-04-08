---
aid: adobe-illustrator
url: https://raw.githubusercontent.com/api-evangelist/adobe-illustrator/refs/heads/main/apis.yml
apis:
- aid: adobe-illustrator:scripting-api
  name: Adobe Illustrator Scripting API
  tags:
  - AppleScript
  - Automation
  - JavaScript
  - Scripting
  - VBScript
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.adobe.com/illustrator/
  properties:
  - url: https://developer.adobe.com/illustrator/
    type: Documentation
  - url: openapi/adobe-illustrator-scripting-openapi-original.yml
    type: OpenAPI
  description: The Adobe Illustrator Scripting API provides programmatic access to Illustrator's functionality through JavaScript, AppleScript, and VBScript. It allows developers to automate repetitive tasks, manipulate documents, select and edit text, generate art from data, and batch process files. Scripts can control nearly every aspect of Illustrator, from creating and modifying paths and shapes to managing layers, colors, and typography, enabling efficient workflow automation for designers and developers.
- aid: adobe-illustrator:plugin-sdk
  name: Adobe Illustrator Plugin SDK
  tags:
  - C++
  - Extensions
  - Plugins
  - SDK
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.adobe.com/illustrator/
  properties:
  - url: https://developer.adobe.com/illustrator/
    type: Documentation
  description: The Adobe Illustrator Plugin SDK enables developers to build native C++ plug-ins for Illustrator on Windows and macOS. The SDK opens the entire application to developer control, allowing extensions to add new functions, automate workflows, parse and manipulate image data, apply custom effects, add custom tools to the toolbar, and extend menu functionality. It provides deep integration with Illustrator's architecture for building high-performance extensions.
- aid: adobe-illustrator:cep-extensions
  name: Adobe Illustrator CEP Extensions API
  tags:
  - CEP
  - CSS
  - Extensions
  - HTML
  - JavaScript
  - Panels
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.adobe.com/illustrator/
  properties:
  - url: https://developer.adobe.com/illustrator/
    type: Documentation
  description: The Adobe Illustrator Common Extensibility Platform (CEP) allows developers to build panels and extensions using HTML, CSS, and JavaScript. CEP extensions run inside Illustrator and can communicate with the application through its scripting interface, enabling developers to create custom user interfaces, integrate with web services, and extend Illustrator's capabilities with modern web technologies. CEP provides a cross-application framework used across Adobe Creative Cloud products.
name: Adobe Illustrator
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Adobe Illustrator is the industry-standard vector graphics application. Its developer platform offers scripting APIs, UXP plugins, CEP extensions, and a C++ SDK for building custom integrations and automating workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


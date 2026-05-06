---
aid: microsoft-edge
name: Microsoft Edge
description: APIs and resources for Microsoft Edge browser development and integration, including the Edge Add-ons API for extension management, DevTools Protocol for browser debugging and automation, Extensions API for building browser extensions, and Web Platform APIs for progressive web app development.
image: https://www.microsoft.com/edge/favicon.ico
url: https://www.microsoft.com/edge
humanURL: https://developer.microsoft.com/microsoft-edge/
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Browser
  - Chromium
  - Developer Tools
  - Edge
  - Extensions
  - Microsoft
  - Progressive Web Apps
  - Web Development
  - WebView
apis:
  - aid: microsoft-edge:edge-addons-api
    name: Microsoft Edge Add-ons API
    description: REST API for managing Microsoft Edge browser extensions through the Partner Center. Enables programmatic publishing, updating, and managing Edge extensions in the Microsoft Edge Add-ons store, supporting the full extension lifecycle from upload to publication.
    image: https://docs.microsoft.com/en-us/media/logos/logo_edge.svg
    humanURL: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/api/using-addons-api
    baseURL: https://api.addons.microsoftedge.microsoft.com
    tags:
      - Add-Ons
      - Browser Extensions
      - Extension Publishing
      - Package Management
      - Partner Center
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/api/using-addons-api
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/api/using-addons-api#before-you-begin
      - type: APIReference
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/api/addons-api-reference
      - type: Authentication
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/api/using-addons-api#registering-the-client-application-in-azure-active-directory
      - type: OpenAPI
        url: openapi/microsoft-edge-addons-api.yaml
      - type: JSONSchema
        url: json-schema/addons-api-product-schema.json
        title: Product Schema
      - type: JSONSchema
        url: json-schema/addons-api-submission-schema.json
        title: Submission Schema
      - type: JSONSchema
        url: json-schema/addons-api-product-list-schema.json
        title: Product List Schema
      - type: JSONSchema
        url: json-schema/addons-api-package-upload-result-schema.json
        title: Package Upload Result Schema
      - type: JSONLD
        url: json-ld/microsoft-edge-addons-api-context.jsonld
      - type: JSONSchema
        url: json-structure/addons-api-product-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/addons-api-submission-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/addons-api-product-list-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/addons-api-package-upload-result-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/addons-api-product-example.json
      - type: CodeExamples
        url: examples/addons-api-product-list-example.json
      - type: CodeExamples
        url: examples/addons-api-submission-example.json
      - type: CodeExamples
        url: examples/addons-api-package-upload-result-example.json
  - aid: microsoft-edge:edge-devtools-api
    name: Microsoft Edge DevTools Protocol HTTP API
    description: HTTP endpoints for the Microsoft Edge DevTools Protocol, based on the Chromium DevTools Protocol. These endpoints allow programmatic discovery and management of debuggable browser targets including pages, service workers, and extensions.
    image: https://docs.microsoft.com/en-us/media/logos/logo_edge.svg
    humanURL: https://learn.microsoft.com/en-us/microsoft-edge/devtools-protocol-chromium/
    baseURL: http://localhost:9222
    tags:
      - Automation
      - Browser Debugging
      - DevTools
      - Remote Debugging
      - Testing
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-edge/devtools-protocol-chromium/
      - type: APIReference
        url: https://chromedevtools.github.io/devtools-protocol/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/microsoft-edge/devtools-protocol-chromium/
      - type: OpenAPI
        url: openapi/microsoft-edge-devtools-api.yaml
      - type: JSONSchema
        url: json-schema/devtools-api-target-schema.json
        title: Target Schema
      - type: JSONSchema
        url: json-schema/devtools-api-browser-version-schema.json
        title: Browser Version Schema
      - type: JSONSchema
        url: json-schema/devtools-api-protocol-schema-schema.json
        title: Protocol Schema Schema
      - type: JSONLD
        url: json-ld/microsoft-edge-devtools-api-context.jsonld
      - type: JSONSchema
        url: json-structure/devtools-api-target-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/devtools-api-browser-version-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/devtools-api-protocol-schema-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/devtools-api-target-example.json
      - type: CodeExamples
        url: examples/devtools-api-browser-version-example.json
      - type: CodeExamples
        url: examples/devtools-api-protocol-schema-example.json
  - aid: microsoft-edge:edge-extensions-api
    name: Microsoft Edge Extensions API
    description: Build browser extensions for Microsoft Edge using the Chromium-based extensions platform. Supports the WebExtensions API standard for cross-browser compatibility.
    image: https://docs.microsoft.com/en-us/media/logos/logo_edge.svg
    humanURL: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/
    baseURL: https://microsoftedge.microsoft.com/addons
    tags:
      - Add-Ons
      - Browser Extensions
      - Chromium Extensions
      - Web Extensions
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/getting-started/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/developer-guide/api-support
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/getting-started/part1-simple-extension
  - aid: microsoft-edge:edge-web-platform-apis
    name: Microsoft Edge Web Platform APIs
    description: Modern web APIs and standards supported in Microsoft Edge, including Progressive Web App capabilities, Web Components, and emerging web platform features.
    image: https://docs.microsoft.com/en-us/media/logos/logo_edge.svg
    humanURL: https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/
    baseURL: https://www.microsoft.com/edge
    tags:
      - Progressive Web Apps
      - PWA
      - Web Platform
      - Web Standards
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/
      - type: ReleaseNotes
        url: https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/whats-new/
common:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/microsoft-edge/
    name: Microsoft Edge Documentation
  - type: DeveloperPortal
    url: https://developer.microsoft.com/microsoft-edge/
    name: Microsoft Edge Developer Portal
  - type: Blog
    url: https://blogs.windows.com/msedgedev/
    name: Microsoft Edge Blog
  - type: GitHubOrganization
    url: https://github.com/MicrosoftEdge
    name: MicrosoftEdge GitHub Organization
  - type: GitHubRepository
    url: https://github.com/MicrosoftEdge/WebView2Samples
    name: WebView2 Samples Repository
  - type: GitHubRepository
    url: https://github.com/nicedoc/nicedoc.io
    name: Microsoft Edge DevTools Repository
  - type: Support
    url: https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/
    name: Microsoft Edge DevTools Documentation
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/microsoft-edge/web-platform/release-notes/
    name: Microsoft Edge Release Notes
  - type: ChangeLog
    url: https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel
    name: Microsoft Edge Stable Channel Release Notes
  - type: StatusPage
    url: https://developer.microsoft.com/en-us/microsoft-edge/status/
    name: Microsoft Edge Platform Status
  - type: X
    url: https://twitter.com/MSEdgeDev
    name: Microsoft Edge Dev on X
  - type: TermsOfService
    url: https://www.microsoft.com/legal/terms-of-use
    name: Microsoft Terms of Use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/privacystatement
    name: Microsoft Privacy Statement
  - type: SDK
    url: https://www.nuget.org/packages/Microsoft.Web.WebView2
    name: WebView2 SDK (NuGet)
  - type: SignUp
    url: https://partner.microsoft.com/dashboard/microsoftedge/
    name: Microsoft Edge Partner Center
  - type: Login
    url: https://partner.microsoft.com/dashboard/
    name: Microsoft Partner Center Login
  - type: Marketplace
    url: https://microsoftedge.microsoft.com/addons/
    name: Microsoft Edge Add-ons Store
  - type: JSONLD
    url: json-ld/microsoft-edge-devtools-api-context.jsonld
    title: DevTools API Context
  - type: JSONLD
    url: json-ld/microsoft-edge-addons-api-context.jsonld
    title: Add-ons API Context
  - type: SpectralRules
    url: rules/microsoft-edge-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/browser-development.yaml
    title: Browser Development Workflow
  - type: NaftikoCapability
    url: capabilities/shared/devtools-api.yaml
    title: DevTools API Shared Definition
  - type: NaftikoCapability
    url: capabilities/shared/addons-api.yaml
    title: Add-ons API Shared Definition
  - type: Vocabulary
    url: vocabulary/microsoft-edge-vocabulary.yaml
  - type: Features
    name: Features
    data:
      - name: Extension Publishing API
        description: Programmatically publish, update, and manage browser extensions in the Edge Add-ons store via REST API.
      - name: Remote Debugging Protocol
        description: Debug and inspect web pages, service workers, and extensions using the Chrome DevTools Protocol over WebSocket.
      - name: WebView2 Embedding
        description: Embed Microsoft Edge rendering engine in native desktop applications using the WebView2 SDK.
      - name: Progressive Web App Support
        description: Build installable PWAs with offline capability, push notifications, and system integration.
      - name: Cross-Browser Extension Compatibility
        description: Build extensions using the Chromium WebExtensions API standard for cross-browser portability.
      - name: Browser Automation
        description: Automate browser tasks including page navigation, target management, and performance profiling.
      - name: Extension Sideloading
        description: Load and test unpacked extensions locally during development without publishing to the store.
      - name: Manifest V3 Support
        description: Build extensions using the latest Manifest V3 specification with service workers and declarative APIs.
  - type: UseCases
    name: Use Cases
    data:
      - name: Automated Extension Deployment
        description: Use the Add-ons API to automate CI/CD pipelines for publishing and updating browser extensions.
      - name: Browser Testing and QA
        description: Leverage DevTools Protocol for automated browser testing, performance auditing, and regression detection.
      - name: Custom Browser Controls
        description: Embed Edge rendering in desktop applications for custom browser experiences using WebView2.
      - name: Enterprise Content Filtering
        description: Build enterprise extensions for content filtering, security policy enforcement, and compliance monitoring.
      - name: Web Scraping and Data Extraction
        description: Use DevTools Protocol to programmatically navigate pages and extract structured data.
      - name: Accessibility Testing
        description: Automate accessibility audits using DevTools Protocol to inspect DOM, ARIA attributes, and contrast ratios.
      - name: Performance Monitoring
        description: Collect real-time performance metrics, network traces, and JavaScript profiling data via DevTools Protocol.
      - name: Progressive Web App Distribution
        description: Build and distribute PWAs through the Microsoft Store with native-like installation and system integration.
  - type: Integrations
    name: Integrations
    data:
      - name: Azure Active Directory
        description: Authenticate to the Edge Add-ons API using Azure AD OAuth 2.0 client credentials flow.
      - name: Microsoft Partner Center
        description: Manage extension listings, submissions, and analytics through the Partner Center dashboard.
      - name: Visual Studio Code
        description: Debug Edge browser content directly from VS Code using the Edge DevTools extension.
      - name: Selenium WebDriver
        description: Automate Microsoft Edge browser for testing using Selenium with the Edge WebDriver.
      - name: Playwright
        description: Cross-browser automation framework with first-class support for Microsoft Edge testing.
      - name: Puppeteer
        description: Control headless Microsoft Edge instances programmatically using the Puppeteer Node.js library.
      - name: GitHub Actions
        description: Automate extension publishing and browser testing in CI/CD workflows using GitHub Actions.
      - name: Windows App SDK
        description: Integrate WebView2 into Windows desktop applications built with WinUI 3 and the Windows App SDK.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

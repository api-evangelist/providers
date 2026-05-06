---
aid: adobe-illustrator
url: https://raw.githubusercontent.com/api-evangelist/adobe-illustrator/refs/heads/main/apis.yml
name: Adobe Illustrator
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Creative Cloud
  - Design
  - Illustrator
  - Vector Graphics
description: Adobe Illustrator is the industry-standard vector graphics application. Its developer platform offers scripting APIs, UXP plugins, CEP extensions, and a C++ SDK for building custom integrations and automating workflows.
created: '2025-01-01'
modified: '2026-04-17'
specificationVersion: '0.19'
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
common:
  - url: https://www.adobe.com/products/illustrator.html
    type: Website
    description: Adobe Illustrator product page with overview of features, use cases, and plan options for the industry-standard vector graphics software.
  - url: https://developer.adobe.com/illustrator/
    type: Documentation
    description: Adobe Illustrator developer portal with scripting documentation, plugin SDK guides, and extension development resources.
  - url: https://helpx.adobe.com/illustrator/desktop/new-features/whats-new.html
    type: WhatsNew
    description: Latest features and improvements added to Adobe Illustrator across recent releases.
  - url: https://helpx.adobe.com/illustrator/desktop/new-features/release-notes.html
    type: ChangeLog
    description: Release notes with summaries of updates, new features, and fixed issues for each Illustrator release.
  - url: https://helpx.adobe.com/support/illustrator.html
    type: Support
    description: Adobe Illustrator help and support hub with troubleshooting guides, FAQs, and known issue documentation.
  - url: https://developer.adobe.com/developer-console/
    type: Portal
    description: Adobe Developer Console for accessing APIs, SDKs, managing projects, and building integrations with Adobe products.
  - url: https://blog.developer.adobe.com/
    type: Blog
    description: Adobe Developers blog featuring technical articles, API updates, and developer community news.
  - url: https://github.com/adobe
    type: GitHubOrganization
    description: Adobe official GitHub organization with open source projects, SDKs, and developer tools.
  - url: https://community.adobe.com/t5/illustrator-discussions/bd-p/illustrator
    type: Forum
    description: Adobe Community forum for Illustrator discussions, questions, and peer support from designers and developers.
  - url: https://forums.creativeclouddeveloper.com
    type: Forum
    description: Creative Cloud developer forums for extension and plugin development discussions across Adobe products.
  - url: https://www.adobe.com/learn/illustrator
    type: Tutorials
    description: Official Adobe Illustrator learning resources with tutorials, guides, and learning paths for all skill levels.
  - url: https://ai-scripting.docsforadobe.dev/
    type: Documentation
    description: Community-maintained Adobe Illustrator scripting guide covering JavaScript, AppleScript, and VBScript with detailed object reference.
  - url: https://stackoverflow.com/questions/tagged/adobe-illustrator
    type: StackOverflow
    description: Stack Overflow questions tagged with adobe-illustrator for developer Q&A and troubleshooting.
  - url: https://status.adobe.com/
    type: Status
    description: Adobe service status dashboard showing real-time availability and incident information for Adobe products and services.
  - url: https://x.com/Illustrator
    type: X
    description: Official Adobe Illustrator account on X (formerly Twitter) with product updates and design inspiration.
  - url: https://www.youtube.com/@AdobeCreativeCloud
    type: YouTube
    description: Adobe Creative Cloud YouTube channel with Illustrator tutorials, feature demos, and creative workflow tips.
  - url: https://www.linkedin.com/company/adobe
    type: LinkedIn
    description: Adobe official LinkedIn company page with news, job openings, and industry updates.
  - url: https://www.adobe.com/products/illustrator/pricing-info.html
    type: Pricing
    description: Adobe Illustrator pricing information with annual and monthly plan options.
  - url: https://helpx.adobe.com/security/products/illustrator.html
    type: Security
    description: Adobe Illustrator security bulletins and advisories with vulnerability disclosures and patch information.
  - url: https://www.adobe.com/trust.html
    type: TrustCenter
    description: Adobe Trust Center covering security practices, privacy commitments, compliance certifications, and data governance.
  - url: https://www.adobe.com/legal/terms.html
    type: TermsOfService
    description: Adobe General Terms of Use governing the use of Adobe products and services.
  - url: https://www.adobe.com/privacy/policy.html
    type: PrivacyPolicy
    description: Adobe Privacy Policy detailing how Adobe collects, uses, and protects user data across its products and services.
  - url: https://www.adobe.com/legal/licenses-terms.html
    type: License
    description: Adobe product licenses and terms including end user license agreements for Creative Cloud applications.
  - type: Features
    data:
      - name: Vector Document Automation
        description: Create, modify, and export vector artwork programmatically via scripting APIs.
      - name: UXP Plugin Framework
        description: Build modern plugins using JavaScript, HTML, CSS, and Adobe Spectrum UI components.
      - name: Text Manipulation
        description: Create, edit, and format text frames, paragraphs, and character styles.
      - name: Path and Shape Operations
        description: Create and manipulate vector paths, compound shapes, and bezier curves.
      - name: Color Management
        description: Work with swatches, gradients, patterns, and color spaces programmatically.
      - name: Artboard Management
        description: Create, resize, reorder, and export individual artboards.
      - name: SVG Export
        description: Export artwork as optimized SVG for web and interactive use.
      - name: Data-Driven Graphics
        description: Generate artwork variations from data using variables and data sets.
      - name: Batch Processing
        description: Process multiple files with consistent operations using Actions and scripts.
      - name: Symbol Libraries
        description: Create, manage, and reuse symbol instances across documents.
  - type: UseCases
    data:
      - name: Design System Automation
        description: Generate icon sets, component libraries, and design tokens from data.
      - name: Brand Asset Production
        description: Batch produce branded materials with consistent styling and color palettes.
      - name: Print Production
        description: Automate print-ready output with bleed, crop marks, and color separation.
      - name: SVG Asset Pipeline
        description: Export optimized SVGs for web applications from Illustrator artwork.
      - name: Data Visualization
        description: Create charts, maps, and infographics from data using scripting.
      - name: Custom Tool Panels
        description: Build UXP plugin panels for specialized workflows and asset management.
  - type: Solutions
    data:
      - name: Illustrator UXP Plugins
        description: Modern plugin platform for extending Illustrator with JavaScript and HTML.
      - name: Illustrator Scripting
        description: Automation via JavaScript, AppleScript, or VBScript for batch workflows.
      - name: Illustrator C++ SDK
        description: Native plugin SDK for performance-critical tools and filters.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: vs-code-marketplace
url: https://raw.githubusercontent.com/api-evangelist/vs-code-marketplace/refs/heads/main/apis.yml
apis:
  - aid: vs-code-marketplace:vs-code-marketplace-gallery-api
    name: VS Code Marketplace Gallery API
    description: The VS Code Marketplace Gallery API provides programmatic access to the Visual Studio Marketplace, enabling search, discovery, and retrieval of extensions for Visual Studio Code and other Microsoft developer tools. It supports querying extensions by name, publisher, category, and tags, as well as fetching extension details, versions, statistics, and reviews.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/microsoft/vscode/blob/main/src/vs/platform/extensionManagement/common/extensionGalleryService.ts
    baseURL: https://marketplace.visualstudio.com/_apis/public/gallery
    tags:
      - Developer Tools
      - Extensions
      - IDE
      - Marketplace
      - Microsoft
      - Visual Studio Code
    properties:
      - url: https://marketplace.visualstudio.com/
        type: Documentation
      - url: https://marketplace.visualstudio.com/_apis/public/gallery
        type: BaseURL
      - url: https://github.com/microsoft/vscode/blob/main/src/vs/platform/extensionManagement/common/extensionGalleryService.ts
        type: SourceCode
      - url: https://code.visualstudio.com/api/working-with-extensions/publishing-extension
        type: Guide
      - url: https://raw.githubusercontent.com/api-evangelist/vs-code-marketplace/refs/heads/main/openapi/vs-code-marketplace-gallery-api-openapi.yml
        type: OpenAPI
name: VS Code Marketplace
description: VS Code Marketplace is Microsoft's official extension marketplace for Visual Studio Code, offering thousands of extensions for languages, debuggers, themes, and developer tools. It provides a Gallery API for programmatically searching, discovering, and retrieving extension metadata, enabling integration with editors, tooling, and automation workflows.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Tools
  - Extensions
  - IDE
  - Microsoft
type: Index
access: 3rd-Party
common:
  - url: https://marketplace.visualstudio.com/
    name: VS Code Marketplace Website
    type: Website
  - url: https://code.visualstudio.com/docs
    name: Documentation
    type: Documentation
  - url: https://code.visualstudio.com/api/working-with-extensions/publishing-extension
    name: Publishing Extensions Guide
    type: Guide
  - url: https://marketplace.visualstudio.com/manage
    name: Publisher Management
    type: Portal
  - url: https://code.visualstudio.com/api
    name: Extension API Documentation
    type: Documentation
  - url: https://code.visualstudio.com/api/get-started/your-first-extension
    name: Getting Started
    type: GettingStarted
  - url: https://marketplace.visualstudio.com/VSCode
    name: VS Code Extensions
    type: Catalog
  - url: https://code.visualstudio.com/updates
    name: Release Notes
    type: ChangeLog
  - url: https://code.visualstudio.com/blogs
    name: Blog
    type: Blog
  - url: https://github.com/microsoft/vscode
    name: GitHub
    type: GitHub
  - url: https://github.com/microsoft/vscode/issues
    name: GitHub Issues
    type: IssueTracker
  - url: https://code.visualstudio.com/community
    name: Community
    type: Community
  - url: https://stackoverflow.com/questions/tagged/visual-studio-code
    name: Stack Overflow
    type: StackOverflow
  - url: https://x.com/code
    name: X (Twitter)
    type: X
  - url: https://www.linkedin.com/showcase/microsoft-visual-studio-code
    name: LinkedIn
    type: LinkedIn
  - url: https://www.youtube.com/@code
    name: YouTube
    type: YouTube
  - url: https://marketplace.visualstudio.com/policies/agree
    name: Terms of Use
    type: TermsOfService
  - url: https://privacy.microsoft.com/privacystatement
    name: Privacy Policy
    type: PrivacyPolicy
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
---

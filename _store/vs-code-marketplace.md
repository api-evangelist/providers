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
name: VS Code Marketplace
tags:
- Developer Tools
- Extensions
- IDE
- Microsoft
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: VS Code Marketplace is Microsoft's official extension marketplace for Visual Studio Code, offering thousands of extensions for languages, debuggers, themes, and developer tools. It provides a Gallery API for programmatically searching, discovering, and retrieving extension metadata, enabling integration with editors, tooling, and automation workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


---
aid: microsoft-visual-studio
name: Microsoft Visual Studio
description: Microsoft Visual Studio is an integrated development environment (IDE) for building applications. It provides APIs for extending the IDE functionality, publishing extensions to the marketplace, and building VS Code extensions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Tools
  - Extensions
  - IDE
  - Microsoft
  - VS Code
url: https://raw.githubusercontent.com/api-evangelist/microsoft-visual-studio/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-visual-studio:extensibility-api
    name: Visual Studio Extensibility API
    tags:
      - Developer Tools
      - Extensions
      - IDE
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/visualstudio/extensibility/
    properties:
      - url: https://learn.microsoft.com/en-us/visualstudio/extensibility/
        type: Documentation
    description: The Visual Studio Extensibility API enables developers to create extensions that customize and extend Visual Studio IDE functionality. Extensions can add custom tool windows, commands, code analyzers, project templates, debugger visualizers, and language services using the VSIX packaging format and MEF composition model.
  - aid: microsoft-visual-studio:marketplace-api
    name: Visual Studio Marketplace API
    tags:
      - Distribution
      - Extensions
      - Marketplace
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://marketplace.visualstudio.com/_apis/
    humanURL: https://learn.microsoft.com/en-us/azure/devops/extend/develop/data-storage
    properties:
      - url: https://learn.microsoft.com/en-us/azure/devops/extend/develop/data-storage
        type: Documentation
    description: The Visual Studio Marketplace API provides access to the extension marketplace for Visual Studio, VS Code, and Azure DevOps. Developers can search extensions, retrieve metadata, manage publisher profiles, and publish extensions programmatically through REST endpoints.
  - aid: microsoft-visual-studio:vscode-extension-api
    name: VS Code Extension API
    tags:
      - Editor
      - Extensions
      - VS Code
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://code.visualstudio.com/api
    properties:
      - url: https://code.visualstudio.com/api
        type: Documentation
      - url: https://code.visualstudio.com/api/get-started/your-first-extension
        type: Getting Started
    description: The VS Code Extension API enables developers to build extensions for Visual Studio Code. It provides APIs for language support, debugging, source control, terminal integration, webviews, custom editors, notebooks, and testing. Extensions can contribute commands, menus, settings, and keybindings to the editor experience.
common:
  - type: Portal
    url: https://marketplace.visualstudio.com/
  - type: Website
    url: https://visualstudio.microsoft.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/visualstudio/ide/
  - type: GitHub Organization
    url: https://github.com/microsoft/vscode
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

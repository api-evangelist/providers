---
aid: speclynx
url: https://raw.githubusercontent.com/api-evangelist/speclynx/refs/heads/main/apis.yml
name: SpecLynx
description: SpecLynx provides enterprise-ready API tooling for authors and maintainers of OpenAPI, AsyncAPI, and Arazzo specifications. Built by veterans with 15+ years of Swagger and OpenAPI development experience, SpecLynx products prioritize security (specs never leave your machine), accuracy, and developer productivity. Core products include a VS Code extension, browser-based editor, CLI, language service library, and the ApiDOM semantic parsing engine.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - API Design
  - AsyncAPI
  - Developer Tools
  - JSON Schema
  - OpenAPI
  - Toolkit
  - VSCode
created: '2026-01-02'
modified: '2026-05-02'
position: Consumer
segments:
  - Developer Tools
  - API Design
apis:
  - aid: speclynx:speclynx
    name: SpecLynx
    tags:
      - API Design
      - Developer Tools
      - OpenAPI
      - Toolkit
      - VSCode
    humanURL: https://speclynx.com/
    properties:
      - url: https://speclynx.com/
        type: Website
      - url: https://speclynx.com/openapi-toolkit/
        type: Documentation
      - url: https://github.com/speclynx/vscode-openapi-toolkit
        type: GitHubRepo
      - url: https://marketplace.visualstudio.com/items?itemName=SpecLynx.vscode-openapi-toolkit
        type: Marketplace
    description: Stop wrestling with OpenAPI specs. SpecLynx OpenAPI Toolkit delivers the most effective way to author and manage your API specs, bringing unprecedented ease, pinpoint accuracy, and unmatched power directly to your VSCode workflow. Supports OpenAPI 2.0/3.0/3.1, AsyncAPI 2.x, Arazzo 1.x, and JSON Schema.
  - aid: speclynx:openapi-toolkit
    name: SpecLynx OpenAPI Toolkit
    tags:
      - API Design
      - AsyncAPI
      - Developer Tools
      - Linting
      - OpenAPI
      - Spectral
      - VSCode
    humanURL: https://speclynx.com/openapi-toolkit/
    properties:
      - url: https://speclynx.com/openapi-toolkit/
        type: Documentation
      - url: https://marketplace.visualstudio.com/items?itemName=SpecLynx.vscode-openapi-toolkit
        type: Marketplace
      - url: https://open-vsx.org/extension/SpecLynx/vscode-openapi-toolkit
        type: OpenVSX
      - url: https://github.com/speclynx/vscode-openapi-toolkit
        type: GitHubRepo
    description: A VS Code extension providing semantic editing, real-time validation, linting, and live preview for OpenAPI, AsyncAPI, and Arazzo specifications. Features context-aware autocompletion, Go to Definition, Find References, JSON/YAML conversion, Spectral ruleset integration, and Scalar/SwaggerUI live preview. Works on desktop VS Code, vscode.dev, github.dev, and GitHub Codespaces.
  - aid: speclynx:editor
    name: SpecLynx Editor
    tags:
      - API Design
      - Browser
      - Developer Tools
      - OpenAPI
      - Online Tool
    humanURL: https://speclynx.com/editor/
    properties:
      - url: https://speclynx.com/editor/
        type: Documentation
      - url: https://editor.speclynx.com/
        type: Portal
    description: A browser-based OpenAPI editor with real-time validation, smart autocompletion, and live preview. No installation required — runs entirely client-side with all processing in-browser. Supports OpenAPI 2.0, 3.0.x, and 3.1.x in both JSON and YAML. Free and open-source under Apache 2.0.
  - aid: speclynx:cli
    name: SpecLynx CLI
    tags:
      - CLI
      - Developer Tools
      - JSON Schema
      - OpenAPI
      - Tooling
    humanURL: https://speclynx.com/
    properties:
      - url: https://speclynx.com/
        type: Documentation
    description: A command-line interface for overlay operations, dereferencing, bundling, format conversion (JSON/YAML), and validation of OpenAPI, AsyncAPI, Arazzo, and JSON Schema documents.
  - aid: speclynx:language-service
    name: SpecLynx Language Service
    tags:
      - API Design
      - Developer Tools
      - LSP
      - Library
      - OpenAPI
    humanURL: https://speclynx.com/language-service/
    properties:
      - url: https://speclynx.com/language-service/
        type: Documentation
    description: An LSP-compatible npm library (@speclynx/apidom-ls) providing 13 intelligent editing capabilities for API description languages, including validation, completion, hover documentation, Go to Definition, Find References, semantic tokens, formatting, dereferencing, and format conversion. Composable with any editor through an LSP wrapper.
  - aid: speclynx:apidom
    name: SpecLynx ApiDOM
    tags:
      - API Design
      - Developer Tools
      - Library
      - OpenAPI
      - Parser
    humanURL: https://speclynx.com/apidom/
    properties:
      - url: https://speclynx.com/apidom/
        type: Documentation
    description: A unified semantic parsing engine that underpins all SpecLynx products. ApiDOM parses OpenAPI, AsyncAPI, Arazzo, and JSON Schema specifications into a semantic data model with lossless preservation of comments, key ordering, and source maps. Built on Tree-sitter for error recovery during editing. Isomorphic — works identically in Node.js and browser environments.
common:
  - url: https://speclynx.com/
    name: Website | SpecLynx
    type: Website
    description: 'null'
  - url: https://speclynx.com/openapi-toolkit/
    name: OpenAPI Toolkit Documentation | SpecLynx
    type: Documentation
    description: 'null'
  - url: https://marketplace.visualstudio.com/items?itemName=SpecLynx.vscode-openapi-toolkit
    name: VS Code Marketplace | SpecLynx OpenAPI Toolkit
    type: Marketplace
    description: 'null'
  - url: https://github.com/speclynx/vscode-openapi-toolkit
    name: GitHub Repository | SpecLynx OpenAPI Toolkit
    type: GitHubRepo
    description: 'null'
  - url: https://open-vsx.org/extension/SpecLynx/vscode-openapi-toolkit
    name: Open VSX Registry | SpecLynx OpenAPI Toolkit
    type: OpenVSX
    description: 'null'
  - url: mailto:info@speclynx.com
    name: Contact | SpecLynx
    type: Contact
    description: 'null'
  - name: Features
    type: Features
    data:
      - name: Semantic Editing
      - name: Context-Aware Autocompletion
      - name: Real-Time Validation
      - name: Spectral Integration
      - name: Semantic Validation
      - name: Live Preview
      - name: Scalar Renderer
      - name: SwaggerUI Renderer
      - name: Go to Definition
      - name: Find References
      - name: JSON/YAML Conversion
      - name: Formatting
      - name: Dereferencing
      - name: Overlay Support
      - name: No Telemetry
      - name: Offline-First
      - name: Multi-Spec Support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---

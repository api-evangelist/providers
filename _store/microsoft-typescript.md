---
aid: microsoft-typescript
name: Microsoft TypeScript
description: TypeScript is a strongly typed programming language that builds on JavaScript developed by Microsoft. It provides a Compiler API and Language Service API for building tools, linters, code generators, and IDE integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Compiler
  - JavaScript
  - Language Tools
  - Microsoft
  - TypeScript
url: https://raw.githubusercontent.com/api-evangelist/microsoft-typescript/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-typescript:compiler-api
    name: TypeScript Compiler API
    tags:
      - Compiler
      - Language Tools
      - TypeScript
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API
    properties:
      - url: https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API
        type: Documentation
    description: The TypeScript Compiler API provides programmatic access to the TypeScript compiler for parsing, analyzing, and transforming TypeScript and JavaScript code. Developers can create custom linters, code generators, documentation tools, and IDE integrations using the AST manipulation and type checking capabilities.
  - aid: microsoft-typescript:language-service-api
    name: TypeScript Language Service API
    tags:
      - IDE Integration
      - Language Service
      - TypeScript
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/microsoft/TypeScript/wiki/Using-the-Language-Service-API
    properties:
      - url: https://github.com/microsoft/TypeScript/wiki/Using-the-Language-Service-API
        type: Documentation
    description: The TypeScript Language Service API powers IDE features like autocomplete, go to definition, find references, refactoring, and error diagnostics. It provides the same intelligence used by VS Code and other editors for TypeScript and JavaScript development.
common:
  - type: Portal
    url: https://www.typescriptlang.org/
  - type: Website
    url: https://www.typescriptlang.org/
  - type: Documentation
    url: https://www.typescriptlang.org/docs/
  - type: GitHub Organization
    url: https://github.com/microsoft/TypeScript
  - type: Getting Started
    url: https://www.typescriptlang.org/docs/handbook/intro.html
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://github.com/microsoft/TypeScript/issues
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

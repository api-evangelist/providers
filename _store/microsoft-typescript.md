---
aid: microsoft-typescript
url: https://raw.githubusercontent.com/api-evangelist/microsoft-typescript/refs/heads/main/apis.yml
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
name: Microsoft TypeScript
tags:
- Compiler
- JavaScript
- Language Tools
- Microsoft
- TypeScript
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: TypeScript is a strongly typed programming language that builds on JavaScript developed by Microsoft. It provides a Compiler API and Language Service API for building tools, linters, code generators, and IDE integrations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


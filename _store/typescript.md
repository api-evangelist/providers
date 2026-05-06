---
aid: typescript
name: TypeScript
description: TypeScript is a strongly typed programming language that builds on JavaScript, adding optional static type checking and other features. Developed and maintained by Microsoft, TypeScript compiles to plain JavaScript and is widely used for large-scale web applications, Node.js services, and developer tooling. The TypeScript Compiler API and Language Service API enable programmatic compilation, type checking, code transformation, and IDE integrations.
image: https://www.typescriptlang.org/favicon-32x32.png
url: https://raw.githubusercontent.com/api-evangelist/typescript/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Compiler
  - JavaScript
  - Language Service
  - Programming Language
  - Static Typing
  - Web Development
type: Index
apis:
  - aid: typescript:typescript-compiler-api
    name: TypeScript Compiler API
    description: Programmatic access to the TypeScript compiler. The Compiler API allows developers to parse TypeScript files into ASTs, perform type checking, emit JavaScript, and transform code programmatically.
    image: https://www.typescriptlang.org/favicon-32x32.png
    humanURL: https://www.typescriptlang.org/docs/handbook/compiler-options.html
    baseURL: https://www.typescriptlang.org
    tags:
      - Compiler
      - Transpilation
      - Type Checking
      - AST
      - Code Generation
    properties:
      - type: Documentation
        url: https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API
      - type: GitHub Repository
        url: https://github.com/microsoft/TypeScript
      - type: npm Package
        url: https://www.npmjs.com/package/typescript
      - type: API Reference
        url: https://www.typescriptlang.org/tsconfig
      - type: Compiler Options
        url: https://www.typescriptlang.org/tsconfig/
  - aid: typescript:typescript-language-service-api
    name: TypeScript Language Service API
    description: API for editor integration and language tooling. The Language Service API provides completions, diagnostics, quick fixes, rename, go-to-definition, find references, and other IDE features that power editors like VS Code.
    image: https://www.typescriptlang.org/favicon-32x32.png
    humanURL: https://www.typescriptlang.org
    baseURL: https://www.typescriptlang.org
    tags:
      - Autocomplete
      - Diagnostics
      - IDE
      - Language Service
      - Refactoring
    properties:
      - type: Documentation
        url: https://github.com/microsoft/TypeScript/wiki/Using-the-Language-Service-API
      - type: GitHub Repository
        url: https://github.com/microsoft/TypeScript
  - aid: typescript:typescript-transform-api
    name: TypeScript Transform API
    description: The TypeScript Transform API enables custom AST transformations during compilation. Transformers can modify, add, or remove nodes in the TypeScript AST before code emission.
    image: https://www.typescriptlang.org/favicon-32x32.png
    humanURL: https://www.typescriptlang.org/docs/handbook/2/types-from-types.html
    baseURL: https://www.typescriptlang.org
    tags:
      - AST
      - Code Transformation
      - Compilation
      - Custom Transformers
    properties:
      - type: Documentation
        url: https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API#traversing-the-ast-with-a-little-linter
      - type: GitHub Repository
        url: https://github.com/microsoft/TypeScript
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://www.typescriptlang.org
  - type: Documentation
    url: https://www.typescriptlang.org/docs/
  - type: GitHub Organization
    url: https://github.com/microsoft/TypeScript
  - type: Blog
    url: https://devblogs.microsoft.com/typescript/
  - type: Community
    url: https://www.typescriptlang.org/community
  - type: npm
    url: https://www.npmjs.com/package/typescript
  - type: Playground
    url: https://www.typescriptlang.org/play
  - type: Handbook
    url: https://www.typescriptlang.org/docs/handbook/intro.html
  - type: Release Notes
    url: https://www.typescriptlang.org/docs/handbook/release-notes/overview.html
  - type: GitHub Issues
    url: https://github.com/microsoft/TypeScript/issues
  - type: Twitter
    url: https://twitter.com/typescript
  - type: JSON-LD
    url: json-ld/typescript-context.jsonld
  - type: Vocabulary
    url: vocabulary/typescript-vocabulary.yml
  - type: JSONSchema
    url: json-schema/typescript-diagnostic-schema.json
  - type: JSONSchema
    url: json-schema/typescript-compiler-options-schema.json
  - type: JSONStructure
    url: json-structure/typescript-diagnostic-structure.json
---

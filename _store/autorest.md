---
aid: autorest
name: AutoRest
description: 'AutoRest is an open source tool from Microsoft (MIT License) that generates client libraries for accessing RESTful APIs from OpenAPI specifications. It powers generation of Azure SDKs across C#, Python, Java, TypeScript, Go, PowerShell, and Swift with an extensible plugin architecture. Note: AutoRest is deprecated as of 2026 with retirement on July 1, 2026. The recommended successor is TypeSpec, a modern API description language and code generation platform from Microsoft.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Code Generation
  - Microsoft
  - OpenAPI
  - SDK Generation
  - Azure SDK
  - Deprecated
url: https://raw.githubusercontent.com/api-evangelist/autorest/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: autorest:autorest-core
    name: AutoRest Core
    description: The AutoRest Core package (@autorest/core) is the central engine that orchestrates code generation from OpenAPI specifications. It handles input processing, configuration resolution, pipeline management, and plugin coordination. All language-specific generators are plugins that extend the core pipeline.
    humanURL: https://github.com/Azure/autorest
    tags:
      - Code Generation
      - OpenAPI
      - Plugin System
      - Pipeline
    properties:
      - type: Documentation
        url: https://github.com/Azure/autorest/blob/main/docs/readme.md
      - type: GettingStarted
        url: https://github.com/Azure/autorest/blob/main/docs/install/readme.md
      - type: GitHubRepository
        url: https://github.com/Azure/autorest
      - type: SDK
        url: https://www.npmjs.com/package/@autorest/core
        title: npm Package
  - aid: autorest:autorest-csharp
    name: AutoRest C# Generator
    description: The AutoRest C# generator (@autorest/csharp) produces .NET client libraries from OpenAPI specifications. It generates strongly-typed C# code with HttpClient-based REST clients, model classes, and async/await patterns compatible with .NET 6+.
    humanURL: https://github.com/Azure/autorest.csharp
    tags:
      - C#
      - .NET
      - Code Generation
      - Azure SDK
    properties:
      - type: Documentation
        url: https://github.com/Azure/autorest.csharp
      - type: GitHubRepository
        url: https://github.com/Azure/autorest.csharp
  - aid: autorest:autorest-python
    name: AutoRest Python Generator
    description: The AutoRest Python generator (@autorest/python) produces Python client libraries from OpenAPI specifications, generating typed Python code compatible with the Azure SDK for Python and azure-core library.
    humanURL: https://github.com/Azure/autorest.python
    tags:
      - Python
      - Code Generation
      - Azure SDK
    properties:
      - type: Documentation
        url: https://github.com/Azure/autorest.python
      - type: GitHubRepository
        url: https://github.com/Azure/autorest.python
  - aid: autorest:autorest-java
    name: AutoRest Java Generator
    description: The AutoRest Java generator (@autorest/java) produces Java client libraries from OpenAPI specifications, generating Java code compatible with azure-core and the Azure SDK for Java ecosystem.
    humanURL: https://github.com/Azure/autorest.java
    tags:
      - Java
      - Code Generation
      - Azure SDK
    properties:
      - type: Documentation
        url: https://github.com/Azure/autorest.java
      - type: GitHubRepository
        url: https://github.com/Azure/autorest.java
  - aid: autorest:autorest-typescript
    name: AutoRest TypeScript Generator
    description: The AutoRest TypeScript generator (@autorest/typescript) produces TypeScript and JavaScript client libraries from OpenAPI specifications, generating type-safe clients for Node.js and browser environments compatible with the Azure SDK for JavaScript.
    humanURL: https://github.com/Azure/autorest.typescript
    tags:
      - TypeScript
      - JavaScript
      - Code Generation
      - Azure SDK
    properties:
      - type: Documentation
        url: https://github.com/Azure/autorest.typescript
      - type: GitHubRepository
        url: https://github.com/Azure/autorest.typescript
  - aid: autorest:autorest-go
    name: AutoRest Go Generator
    description: The AutoRest Go generator (@autorest/go) produces Go client libraries from OpenAPI specifications, generating idiomatic Go code compatible with the Azure SDK for Go and azure-sdk-for-go ecosystem.
    humanURL: https://github.com/Azure/autorest.go
    tags:
      - Go
      - Code Generation
      - Azure SDK
    properties:
      - type: Documentation
        url: https://github.com/Azure/autorest.go
      - type: GitHubRepository
        url: https://github.com/Azure/autorest.go
common:
  - type: Website
    url: https://github.com/Azure/autorest
  - type: Documentation
    url: https://github.com/Azure/autorest/blob/main/docs/readme.md
  - type: GitHubOrganization
    url: https://github.com/Azure
  - type: GitHubRepository
    url: https://github.com/Azure/autorest
  - type: GettingStarted
    url: https://github.com/Azure/autorest/blob/main/docs/install/readme.md
  - type: ReleaseNotes
    url: https://github.com/Azure/autorest/releases
  - type: Features
    data:
      - name: Multi-Language Code Generation
        description: Generate client SDKs from OpenAPI specifications in C#, Python, Java, TypeScript, JavaScript, Go, PowerShell, and Swift using language-specific generator plugins.
      - name: Extensible Plugin Architecture
        description: AutoRest uses a pipeline-based plugin architecture where language generators, transformers, and validators are loaded as npm packages. Custom plugins can be developed to extend the generation pipeline.
      - name: OpenAPI Processing
        description: Supports OpenAPI 2.0 (Swagger) and OpenAPI 3.0 specification formats. The modelerfour plugin normalizes OpenAPI schemas into a consistent code model shared across all language generators.
      - name: Azure SDK Integration
        description: Tightly integrated with Microsoft Azure SDK generation for all Azure services, producing SDK packages published to npm, PyPI, Maven, NuGet, and Go Modules.
      - name: Configuration File Support
        description: Supports literate configuration using Markdown code blocks for per-client customization of generated output including namespace, output folder, and generator-specific options.
  - type: UseCases
    data:
      - name: Azure Service SDK Generation
        description: Primary use case for generating Azure SDK client libraries for all Azure services from the azure-rest-api-specs OpenAPI repository.
      - name: REST API Client Generation
        description: Generate strongly-typed client SDKs for any REST API described in OpenAPI format across multiple programming languages simultaneously.
      - name: SDK Customization
        description: Use AutoRest configuration files and directives to customize generated code including renames, suppressions, and additional properties.
  - type: Integrations
    data:
      - name: Azure REST API Specs
        description: AutoRest is the primary tool consuming the Azure/azure-rest-api-specs repository to generate official Azure SDK client libraries.
      - name: TypeSpec
        description: TypeSpec is the recommended successor to AutoRest for new API definitions, with AutoRest generators serving as code generation backends.
      - name: npm
        description: AutoRest and all language generator plugins are distributed as npm packages under the @autorest scope.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

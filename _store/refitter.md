---
aid: refitter
name: Refitter
description: Refitter is a .NET tool and source generator that produces Refit HTTP client interfaces from OpenAPI specifications. It runs at compile time as a source generator or as a standalone CLI tool (dotnet-refitter), enabling type-safe API consumption in .NET projects. Refitter reads OpenAPI 2.0 (Swagger) and OpenAPI 3.x specifications and generates strongly-typed C# interface definitions and model classes compatible with the Refit library.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/refitter/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - .NET
  - C#
  - Code Generation
  - OpenAPI
  - Refit
  - Source Generator
  - Type-Safe
apis:
  - aid: refitter:refitter
    name: Refitter
    description: Refitter is a .NET source generator and CLI tool that produces Refit HTTP client interfaces from OpenAPI 2.0 and 3.x specifications. Supports compile-time code generation via MSBuild source generators and on-demand generation via the dotnet-refitter global tool. Generates C# interfaces, model classes, and optional Refit settings for use with the Refit HttpClient library.
    humanURL: https://github.com/christianhelle/refitter
    baseURL: https://refitter.github.io
    tags:
      - .NET
      - C#
      - Code Generation
      - OpenAPI
      - Refit
      - Source Generator
    properties:
      - type: Documentation
        url: https://refitter.github.io
      - type: GettingStarted
        url: https://refitter.github.io/articles/getting-started.html
      - type: GitHubRepository
        url: https://github.com/christianhelle/refitter
      - type: NuGetPackage
        url: https://www.nuget.org/packages/Refitter
      - type: NuGetPackage
        url: https://www.nuget.org/packages/dotnet-refitter
      - type: Changelog
        url: https://github.com/christianhelle/refitter/releases
      - type: License
        url: https://github.com/christianhelle/refitter/blob/main/LICENSE
      - type: Issues
        url: https://github.com/christianhelle/refitter/issues
      - type: Discussions
        url: https://github.com/christianhelle/refitter/discussions
  - aid: refitter:refit
    name: Refit
    description: The type-safe REST library for .NET that Refitter generates interfaces for. Refit turns REST APIs into live interfaces by decorating C# interfaces with attributes describing the HTTP endpoints, then generating HttpClient calls at runtime via Castle DynamicProxy or source generators.
    humanURL: https://reactiveui.github.io/refit/
    tags:
      - .NET
      - HttpClient
      - REST Client
      - Type-Safe
    properties:
      - type: Documentation
        url: https://reactiveui.github.io/refit/
      - type: GitHubRepository
        url: https://github.com/reactiveui/refit
      - type: NuGetPackage
        url: https://www.nuget.org/packages/Refit
common:
  - type: Website
    url: https://refitter.github.io
  - type: GitHubRepository
    url: https://github.com/christianhelle/refitter
  - type: Documentation
    url: https://refitter.github.io
  - type: Issues
    url: https://github.com/christianhelle/refitter/issues
  - type: NuGetPackage
    url: https://www.nuget.org/packages/Refitter
  - type: License
    url: https://github.com/christianhelle/refitter/blob/main/LICENSE
  - type: JSONSchema
    url: json-schema/refitter-settings-schema.json
  - type: JSONStructure
    url: json-structure/refitter-output-structure.json
  - type: JSONLDContext
    url: json-ld/refitter-context.jsonld
  - type: Vocabulary
    url: vocabulary/refitter-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

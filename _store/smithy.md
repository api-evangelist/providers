---
aid: smithy
name: Smithy
description: Smithy is an open source, protocol-agnostic interface definition language (IDL) and toolchain developed at AWS for defining, validating, and generating API clients, servers, and documentation for any programming language. It powers the AWS SDK code generation pipeline and supports protocol-agnostic API modeling with traits, validators, and code generators. Smithy IDL 2.0 is the current stable version.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Code Generation
  - IDL
  - SDKs
  - API Design
  - Interface Definition Language
  - Toolchain
created: '2026-03-25'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/smithy/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: smithy:smithy-idl
    name: Smithy IDL
    description: The Smithy Interface Definition Language (IDL) is a specification for defining API models using shapes and traits. Models can be written in the Smithy IDL syntax or the JSON AST representation. Smithy 2.0 is the current stable version with improved nullability, enums, resource properties, and mixins.
    humanURL: https://smithy.io/2.0/
    tags:
      - IDL
      - API Design
      - Specification
    properties:
      - type: Documentation
        url: https://smithy.io/2.0/
      - type: Specification
        url: https://smithy.io/2.0/spec/
      - type: Getting Started
        url: https://smithy.io/2.0/quickstart.html
      - type: GitHub Repository
        url: https://github.com/smithy-lang/smithy
  - aid: smithy:smithy-cli
    name: Smithy CLI
    description: The Smithy CLI is a command-line tool for building, validating, diffing, and transforming Smithy models. It can generate JSON AST representations, run model validation, perform backwards-compatibility checks, and generate artifacts from Smithy models.
    humanURL: https://smithy.io/2.0/guides/smithy-cli/index.html
    tags:
      - CLI
      - Build Tools
      - Validation
    properties:
      - type: Documentation
        url: https://smithy.io/2.0/guides/smithy-cli/index.html
      - type: GitHub Repository
        url: https://github.com/smithy-lang/smithy
      - type: Homebrew
        url: https://github.com/smithy-lang/homebrew-tap
common:
  - type: Website
    url: https://smithy.io
  - type: Documentation
    url: https://smithy.io/2.0/
  - type: Specification
    url: https://smithy.io/2.0/spec/
  - type: Getting Started
    url: https://smithy.io/2.0/quickstart.html
  - type: GitHub Organization
    url: https://github.com/smithy-lang
  - type: GitHub Repository
    url: https://github.com/smithy-lang/smithy
  - type: Examples
    url: https://github.com/smithy-lang/smithy-examples
  - type: Awesome List
    url: https://github.com/smithy-lang/awesome-smithy
  - type: AWS API Models
    url: https://github.com/aws/api-models-aws
  - type: Blog
    url: https://aws.amazon.com/blogs/developer/tag/smithy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

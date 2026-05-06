---
aid: sideko
url: https://raw.githubusercontent.com/api-evangelist/sideko/refs/heads/main/apis.yml
apis:
  - aid: sideko:sideko-api
    name: Sideko API
    tags:
      - CLI
      - Documentation
      - Mock Servers
      - Platform
      - SDKs
    humanURL: https://docs.sideko.dev/
    baseURL: https://api.sideko.dev
    properties:
      - url: https://docs.sideko.dev/
        type: Documentation
      - url: https://docs.sideko.dev/reference/
        type: OpenAPI
      - url: openapi/sideko-openapi.yml
        type: OpenAPI
      - url: rules/sideko-rules.yml
        type: SpectralRules
      - url: capabilities/api-tooling-lifecycle.yaml
        type: Capabilities
      - url: json-schema/sideko-api-project-schema.json
        type: JSONSchema
      - url: json-schema/sideko-sdk-generation-schema.json
        type: JSONSchema
      - url: json-ld/sideko-context.jsonld
        type: JSONLD
      - url: vocabulary/sideko-vocabulary.yml
        type: Vocabulary
      - url: https://authentication.sideko.dev/sign-up
        type: Sign Up
      - url: https://sideko.dev/pricing
        type: Pricing
      - url: https://github.com/Sideko-Inc/sideko
        type: GitHub
    description: The Sideko REST API allows developers to programmatically interact with the Sideko platform to manage API projects, generate SDKs, create CLI tools, deploy mock servers, and publish API documentation. The API enables automation of the entire API tooling lifecycle from spec ingestion through SDK generation and documentation publishing.
    contact:
      FN: Sideko Support
      email: support@sideko.dev
      url: https://docs.sideko.dev/
  - aid: sideko:sideko-cli
    name: Sideko CLI
    tags:
      - CLI
      - Developer Tools
      - SDKs
    humanURL: https://github.com/Sideko-Inc/sideko
    properties:
      - url: https://github.com/Sideko-Inc/sideko
        type: GitHub
      - url: https://docs.sideko.dev/cli/
        type: Documentation
    description: The Sideko CLI provides command-line access to the Sideko platform, enabling developers to generate SDKs, manage API projects, deploy documentation, and run mock servers from the terminal. Built in Rust, it wraps the Sideko REST API in an ergonomic CLI experience.
  - aid: sideko:sideko-node-sdk
    name: Sideko Node.js SDK
    tags:
      - SDK
      - Node.js
      - TypeScript
      - JavaScript
    humanURL: https://github.com/Sideko-Inc/sideko-node-sdk
    properties:
      - url: https://github.com/Sideko-Inc/sideko-node-sdk
        type: GitHub
      - url: https://www.npmjs.com/package/sideko-sdk
        type: SDK
    description: The Sideko Node.js SDK provides TypeScript and JavaScript bindings for the Sideko API. Generated from the Sideko OpenAPI specification, it enables Node.js developers to manage API projects, generate SDKs, and interact with the Sideko platform programmatically.
  - aid: sideko:sideko-python-sdk
    name: Sideko Python SDK
    tags:
      - SDK
      - Python
    humanURL: https://github.com/Sideko-Inc/sideko-python-sdk
    properties:
      - url: https://github.com/Sideko-Inc/sideko-python-sdk
        type: GitHub
      - url: https://pypi.org/project/sideko-sdk/
        type: SDK
    description: The Sideko Python SDK provides Python bindings for the Sideko API. Generated from the Sideko OpenAPI specification, it enables Python developers to manage API projects, trigger SDK generation, and automate documentation workflows programmatically.
name: Sideko
tags:
  - CLI
  - Documentation
  - Mock Servers
  - Platform
  - SDKs
  - API Tooling
  - SDK Generation
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-30'
modified: '2026-05-02'
position: Consuming
segments:
  - Documentation
  - SDKs
  - Developer Tools
description: Sideko is an API tooling generation platform that uses OpenAPI Specifications to create SDKs, documentation sites, CLIs, and mock servers. The platform enables organizations to offer a complete suite of API developer tools without writing code, as Sideko generates the tooling automatically from OpenAPI specs. Sideko serves some of the largest organizations in the world, helping improve API developer experience at scale.
common:
  - type: Website
    url: https://www.sideko.dev/
  - type: Documentation
    url: https://docs.sideko.dev/
  - type: Sign Up
    url: https://authentication.sideko.dev/sign-up
  - type: Pricing
    url: https://sideko.dev/pricing
  - type: Blog
    url: https://www.sideko.dev/blog
  - type: GitHub
    url: https://github.com/Sideko-Inc
  - type: ChangeLog
    url: https://docs.sideko.dev/changelog/
  - type: TermsOfService
    url: https://www.sideko.dev/legal/terms
  - type: PrivacyPolicy
    url: https://www.sideko.dev/legal/privacy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---

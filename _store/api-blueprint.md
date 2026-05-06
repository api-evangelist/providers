---
aid: api-blueprint
name: API Blueprint
description: API Blueprint is a high-level API description language using Markdown-based syntax for designing, documenting, and prototyping web APIs. Created by Apiary and released under the MIT License, API Blueprint uses .apib files with a concise Markdown format that makes APIs accessible to both technical and non-technical stakeholders. The project is no longer actively maintained (all apiaryio GitHub repos are archived as of 2024) but remains a notable specification in API design history, influencing later formats like OpenAPI.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - Specification Language
  - Markdown
  - Documentation
url: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: api-blueprint:api-blueprint
    name: API Blueprint
    description: API Blueprint is a high-level API description language using Markdown-based syntax for designing, documenting, and prototyping APIs. Files use the .apib extension with media type text/vnd.apiblueprint. The project was archived in 2024 after being developed by Apiary (acquired by Oracle).
    humanURL: https://apiblueprint.org
    tags:
      - API Design
      - Specification Language
      - Markdown
    properties:
      - type: Documentation
        url: https://apiblueprint.org/documentation/
      - type: GitHubRepository
        url: https://github.com/apiaryio/api-blueprint
      - type: Specification
        url: https://github.com/apiaryio/api-blueprint/blob/master/API%20Blueprint%20Specification.md
      - type: GettingStarted
        url: https://apiblueprint.org/documentation/tutorial.html
common:
  - type: Website
    url: https://apiblueprint.org
  - type: Documentation
    url: https://apiblueprint.org/documentation/
  - type: GitHubOrganization
    url: https://github.com/apiaryio
  - type: TermsOfService
    url: https://github.com/apiaryio/api-blueprint/blob/master/LICENSE
  - type: Features
    data:
      - name: Markdown-Based Syntax
        description: API Blueprint uses concise Markdown syntax making API descriptions readable by both developers and non-technical stakeholders. Files use the .apib extension with media type text/vnd.apiblueprint.
      - name: Data Structure Modeling
        description: Supports reusable data structure definitions using MSON (Markdown Syntax for Object Notation) for describing complex request and response schemas.
      - name: Mock Server Generation
        description: API Blueprint documents can drive mock server generation for rapid prototyping and front-end development before backend implementation.
      - name: Testing with Dredd
        description: The Dredd HTTP testing tool uses API Blueprint specs to run contract tests validating that API implementations match their documented contracts.
      - name: RFC-Driven Governance
        description: API Blueprint evolution was governed through an RFC process similar to Rust and Django, with proposals submitted to the api-blueprint-rfcs repository.
  - type: UseCases
    data:
      - name: API Documentation
        description: Write human-readable API documentation in Markdown that doubles as a machine-parseable specification for tooling.
      - name: Contract Testing
        description: Use API Blueprint specs with Dredd to verify that API implementations conform to their documented contracts in CI pipelines.
      - name: API Prototyping
        description: Rapidly prototype APIs by writing Blueprint specs first, then generating mock servers from the specification.
  - type: Integrations
    data:
      - name: Apiary
        description: API Blueprint was the native specification format of the Apiary platform (acquired by Oracle), which provided hosted documentation, mock servers, and testing.
      - name: Drafter Parser
        description: The canonical API Blueprint parser written in C++ with bindings for Node.js (drafter.js, drafter-npm) and other languages.
      - name: Dredd Testing Framework
        description: Language-agnostic HTTP API testing tool that validates live API implementations against API Blueprint or Swagger/OpenAPI specs.
      - name: Swagger Conversion
        description: The swagger2blueprint tool converted Swagger API descriptions into API Blueprint format for migration workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

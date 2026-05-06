---
aid: uml
name: UML
description: UML (Unified Modeling Language) is the standard modeling language for software architecture, system design, and technical documentation. Governed by the Object Management Group (OMG), UML defines a set of notation conventions and diagram types — class, sequence, activity, use case, state, component, deployment, and more — used across the software development lifecycle. This collection profiles the ecosystem of tools, APIs, and services that work with UML diagrams programmatically.
url: https://raw.githubusercontent.com/api-evangelist/uml/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - UML
  - Modeling
  - Diagrams
  - Software Architecture
  - Design
  - Standards
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: uml:plantuml-server
    name: PlantUML Server API
    tags:
      - UML
      - Diagrams
      - PlantUML
      - Text-To-Diagram
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.plantuml.com/plantuml
    humanURL: https://plantuml.com/
    properties:
      - url: https://plantuml.com/
        type: Documentation
      - url: https://deepwiki.com/plantuml/plantuml-server/6-api-reference
        type: Documentation
      - url: openapi/plantuml-server-openapi.yml
        type: OpenAPI
    description: PlantUML Server provides a public REST API for generating UML diagrams from plain-text descriptions. Diagrams are encoded in the URL path using a deflate + base64 scheme. The server supports multiple output formats including PNG, SVG, ASCII art, and PDF. Diagram types include class, sequence, activity, component, state, use case, deployment, timing, and more.
  - aid: uml:kroki
    name: Kroki Diagram API
    tags:
      - UML
      - Diagrams
      - Multi-Format
      - Text-To-Diagram
      - Open Source
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://kroki.io
    humanURL: https://kroki.io/
    properties:
      - url: https://docs.kroki.io/kroki/
        type: Documentation
      - url: https://docs.kroki.io/kroki/setup/usage/
        type: Getting Started
      - url: openapi/kroki-openapi.yml
        type: OpenAPI
    description: Kroki provides a unified HTTP API for generating diagrams from textual descriptions. It supports over 20 diagram types including PlantUML, Mermaid, GraphViz, BlockDiag, BPMN, C4, Structurizr, Excalidraw, Vega, and WaveDrom. Requests can be sent as GET (diagram encoded in URL) or POST (diagram in request body). Output formats include SVG, PNG, PDF, and JPEG. Kroki is open source and can be self-hosted.
common:
  - type: GitHub Org
    url: https://github.com/plantuml
  - type: GitHub Org
    url: https://github.com/yuzutech
  - type: Website
    url: https://www.omg.org/uml/
  - type: Standard
    url: https://www.omg.org/spec/UML/
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Unified_Modeling_Language
  - type: GitHub
    url: https://github.com/plantuml/plantuml
  - type: GitHub
    url: https://github.com/yuzutech/kroki
  - type: Documentation
    url: https://plantuml.com/
  - type: Documentation
    url: https://docs.kroki.io/kroki/
  - type: JSON-LD
    url: json-ld/uml-context.jsonld
  - type: Vocabulary
    url: vocabulary/uml-vocabulary.yml
  - type: JSONSchema
    url: json-schema/uml-diagram-schema.json
  - type: Spectral Rules
    url: rules/uml-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: wireframes
name: Wireframes
description: Wireframes are low-fidelity visual representations of user interface layouts used in early design stages to establish structure, hierarchy, and functionality before high-fidelity design work begins. Major wireframing tools including Figma, Balsamiq, Axure, UXPin, Sketch, and Miro offer APIs and developer integrations for programmatic access to design assets, metadata, and collaboration workflows.
type: Index
url: https://en.wikipedia.org/wiki/Website_wireframe
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Design
  - Figma
  - Prototyping
  - UI Design
  - UX
  - Wireframing
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wireframes:figma-api
    name: Figma REST API
    description: The Figma REST API provides programmatic access to Figma design files, components, styles, comments, and webhooks. It is the primary developer API for the most widely used wireframing and design collaboration tool. Fully described in an OpenAPI specification at github.com/figma/rest-api-spec.
    humanURL: https://developers.figma.com/docs/rest-api/
    baseURL: https://api.figma.com
    tags:
      - Design
      - Figma
      - Prototyping
      - UI Design
      - UX
    properties:
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/
      - type: Portal
        url: https://developers.figma.com/
      - type: OpenAPI
        url: https://github.com/figma/rest-api-spec
  - aid: wireframes:balsamiq-api
    name: Balsamiq Cloud API
    description: Balsamiq provides a fast, focused wireframing tool used by lean product teams. Balsamiq Cloud offers API access for project management and asset integration. Balsamiq is widely used for quick, low-fidelity wireframe sketching.
    humanURL: https://balsamiq.com/
    baseURL: https://balsamiq.cloud
    tags:
      - Balsamiq
      - Design
      - Prototyping
      - Wireframing
    properties:
      - type: Documentation
        url: https://balsamiq.com/support/
      - type: Website
        url: https://balsamiq.com/
common:
  - url: https://en.wikipedia.org/wiki/Website_wireframe
    name: Wireframe (Wikipedia)
    type: Reference
    description: Wikipedia article on wireframe design methodology.
  - url: https://developers.figma.com/
    name: Figma Developer Portal
    type: Portal
    description: Developer portal for the Figma REST API and webhooks.
  - url: https://www.figma.com/resource-library/what-is-wireframing/
    name: What is Wireframing? (Figma)
    type: Guide
    description: Figma's guide to wireframing concepts and best practices.
  - url: https://balsamiq.com/
    name: Balsamiq
    type: Website
    description: Balsamiq wireframing tool website.
  - url: https://www.figma.com/wireframe-tool/
    name: Figma Wireframe Tool
    type: Tool
    description: Figma's online wireframing tool.
  - url: https://raw.githubusercontent.com/api-evangelist/wireframes/refs/heads/main/json-ld/wireframes-context.jsonld
    name: Wireframes JSON-LD Context
    type: JSONLDContext
    description: JSON-LD context for wireframe design domain vocabulary.
  - url: https://raw.githubusercontent.com/api-evangelist/wireframes/refs/heads/main/vocabulary/wireframes-vocabulary.yml
    name: Wireframes Vocabulary
    type: Vocabulary
    description: Domain vocabulary for wireframe design concepts and tooling.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

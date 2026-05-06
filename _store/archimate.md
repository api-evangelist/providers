---
aid: archimate
name: ArchiMate
description: ArchiMate is an open and independent enterprise architecture modeling language developed by The Open Group, supporting description, analysis and visualization of architecture within and across business domains in an unambiguous way. The current version is ArchiMate 3.2.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise Architecture
  - Architecture Framework
  - Modeling Language
  - Business Architecture
  - Technology Architecture
  - Standard
  - Open Group
url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: archimate:archimate-model-exchange-api
    name: ArchiMate Model Exchange API
    description: API for exchanging ArchiMate models between tools and repositories using the Open Group ArchiMate Model Exchange File Format (AMEFF). Enables interoperability between enterprise architecture tools.
    humanURL: https://www.opengroup.org/archimate-forum/archimate-overview
    tags:
      - Enterprise Architecture
      - Model Exchange
      - Interoperability
      - XML Schema
    properties:
      - type: Documentation
        url: https://pubs.opengroup.org/architecture/archimate3-doc/
      - type: GettingStarted
        url: https://www.opengroup.org/archimate-forum/archimate-overview
      - type: APIReference
        url: https://pubs.opengroup.org/architecture/archimate3-doc/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/openapi/archimate-model-exchange-api.yaml
  - aid: archimate:archimate-repository-api
    name: ArchiMate Repository API
    description: RESTful API for accessing and managing ArchiMate models, elements, relationships, and views stored in a central enterprise architecture repository.
    humanURL: https://www.opengroup.org/archimate-forum
    tags:
      - Repository Management
      - Model Management
      - REST API
      - Enterprise Architecture
    properties:
      - type: Documentation
        url: https://pubs.opengroup.org/architecture/archimate3-doc/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/openapi/archimate-repository-api.yaml
common:
  - type: Portal
    url: https://www.opengroup.org/archimate-forum
  - type: Documentation
    url: https://pubs.opengroup.org/architecture/archimate32-doc/
  - type: GettingStarted
    url: https://www.opengroup.org/archimate-forum/archimate-overview
  - type: GitHubOrganization
    url: https://github.com/archimate-org
  - type: Support
    url: https://www.opengroup.org/archimate-forum/forums
  - type: Blog
    url: https://blog.opengroup.org/tag/archimate/
  - type: Training
    url: https://www.opengroup.org/certifications/archimate
  - type: Features
    data:
      - name: Enterprise Architecture Modeling
        description: Standardized language for modeling business, application, and technology architecture layers.
      - name: Model Exchange Format
        description: ArchiMate Model Exchange File Format (AMEFF) for tool interoperability using XML.
      - name: Three Architecture Layers
        description: Business, Application, and Technology layers for comprehensive EA modeling.
      - name: Motivation and Strategy
        description: Strategy and motivation aspect elements for stakeholder and driver modeling.
      - name: Implementation and Migration
        description: Work package and implementation elements for roadmap and migration planning.
      - name: Tool Ecosystem
        description: Supported by 20+ enterprise architecture tools including Archi, Sparx EA, BiZZdesign, and MEGA.
      - name: Open Standard
        description: Open Group standard freely available for implementation without licensing fees.
  - type: UseCases
    data:
      - name: Enterprise Architecture Documentation
        description: Document and communicate enterprise architecture across business, application, and technology layers.
      - name: Architecture Analysis
        description: Analyze dependencies, impacts, and gaps in enterprise architecture using standardized notation.
      - name: Tool Migration
        description: Migrate ArchiMate models between EA tools using the standardized exchange format.
      - name: Architecture Governance
        description: Establish governance controls and compliance checking for enterprise architecture standards.
      - name: IT Portfolio Management
        description: Manage IT application portfolios and rationalize technology investments using ArchiMate models.
  - type: Integrations
    data:
      - name: Archi
        description: Open source ArchiMate modelling tool with full AMEFF import/export support.
      - name: Sparx Enterprise Architect
        description: Commercial EA tool with ArchiMate 3 profile and exchange format support.
      - name: BiZZdesign
        description: Enterprise architecture platform with native ArchiMate support.
      - name: MEGA HOPEX
        description: Enterprise architecture management platform supporting ArchiMate standard.
      - name: TOGAF
        description: ArchiMate is the recommended modeling language for TOGAF enterprise architecture framework.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/rules/archimate-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/vocabulary/archimate-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/archimate/refs/heads/main/json-ld/archimate-model-exchange-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

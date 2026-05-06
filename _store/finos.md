---
aid: finos
name: FINOS
description: The Fintech Open Source Foundation (FINOS) is a Linux Foundation project dedicated to open source innovation in the financial services industry. It fosters collaboration between banks, fintech companies, and technology firms on standards and projects spanning desktop interoperability (FDC3), financial product modeling (Common Domain Model), cloud compliance (Common Cloud Controls), business and technology modeling (Morphir), and messaging APIs (Symphony API Spec), among others.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial Services
  - Fintech
  - Linux Foundation
  - Open Source
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/finos/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: finos:fdc3
    name: FDC3
    description: FDC3 is an open standard for financial desktop interoperability, defining how applications launch, share context, and resolve intents across the financial desktop. The standard includes a Desktop Agent API and an App Directory specification.
    humanURL: https://fdc3.finos.org/
    tags:
      - Desktop Interoperability
      - FDC3
      - Financial Services
      - Open Standard
    properties:
      - type: Documentation
        url: https://fdc3.finos.org/docs/fdc3-intro
      - type: GitHubRepository
        url: https://github.com/finos/FDC3
      - type: Reference
        url: https://fdc3.finos.org/docs/app-directory/overview
  - aid: finos:common-domain-model
    name: Common Domain Model
    description: The Common Domain Model (CDM) is a standardized, machine-readable, and machine-executable model that represents financial products, trades in those products, and the lifecycle events of those trades.
    humanURL: https://www.finos.org/common-domain-model
    tags:
      - Common Domain Model
      - Financial Products
      - Open Standard
      - Trade Lifecycle
    properties:
      - type: Documentation
        url: https://cdm.finos.org/
      - type: GitHubRepository
        url: https://github.com/finos/common-domain-model
  - aid: finos:common-cloud-controls
    name: Common Cloud Controls
    description: FINOS Common Cloud Controls is an open standard project that describes consistent controls for compliant public cloud deployments in the financial services sector.
    humanURL: https://www.finos.org/common-cloud-controls-project
    tags:
      - Cloud
      - Compliance
      - Financial Services
      - Open Standard
    properties:
      - type: Documentation
        url: https://www.finos.org/common-cloud-controls-project
      - type: GitHubRepository
        url: https://github.com/finos/common-cloud-controls
  - aid: finos:morphir
    name: Morphir
    description: Morphir is a universal language for business and technology that captures business logic in a portable, technology-agnostic intermediate representation that can be compiled to multiple target languages and runtimes.
    humanURL: https://morphir.finos.org/
    tags:
      - Business Modeling
      - Domain Modeling
      - Morphir
      - Open Source
    properties:
      - type: Documentation
        url: https://morphir.finos.org/
      - type: GitHubRepository
        url: https://github.com/finos/morphir
  - aid: finos:symphony-api
    name: Symphony API Spec
    description: The Symphony API Spec project hosted at FINOS publishes the OpenAPI definitions for the Symphony platform, including the Pod API, Agent API, and Authenticator API used to send messages, manage users, and authenticate bots and integrations.
    humanURL: https://github.com/finos/symphony-api-spec
    tags:
      - Authentication
      - Messaging
      - OpenAPI
      - Symphony
    properties:
      - type: Documentation
        url: https://github.com/finos/symphony-api-spec
      - type: GitHubRepository
        url: https://github.com/finos/symphony-api-spec
      - type: OpenAPI
        url: openapi/finos-symphony-pod-api-openapi.yml
      - type: OpenAPI
        url: openapi/finos-symphony-agent-api-openapi.yml
      - type: OpenAPI
        url: openapi/finos-symphony-authenticator-api-openapi.yml
common:
  - type: Website
    url: https://www.finos.org/
  - type: Documentation
    url: https://www.finos.org/about
  - type: GitHubOrg
    url: https://github.com/finos
  - type: Landscape
    url: https://landscape.finos.org/
  - type: Community
    url: https://www.finos.org/community
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: stoplight
name: Stoplight
description: Stoplight is a collaborative, design-first API platform providing a visual editor for OpenAPI specifications, interactive hosted documentation, automatic mock servers, API style guides and governance, and open-source tools including Prism (mock server), Spectral (JSON/YAML linter), and Elements (documentation components). Acquired by SmartBear in 2023, Stoplight enables teams to design, document, and govern APIs at scale using a design-first approach. The platform supports OpenAPI v3.1, v3.0, v2.0, Arazzo v1.0, and AsyncAPI v2.x, with integrations for GitHub, GitLab, Bitbucket, and Azure DevOps.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - API Documentation
  - API Governance
  - AsyncAPI
  - Design-First
  - Linting
  - Mock Servers
  - OpenAPI
  - Style Guides
created: '2026-03-03'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/stoplight/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: stoplight:stoplight-platform
    name: Stoplight Platform
    description: Stoplight Platform is a SaaS collaborative API design and documentation management tool providing a visual editor for OpenAPI specifications, interactive hosted documentation, automatic mock servers, API style guides, governance features, and multi-branch Git integration. Teams design, document, mock, and govern APIs using a design-first approach. Supports OpenAPI v3.1/v3.0/v2.0, Arazzo v1.0, and AsyncAPI v2.x. Integrates with GitHub, GitLab, Bitbucket, and Azure DevOps.
    humanURL: https://stoplight.io
    tags:
      - API Design
      - API Documentation
      - API Governance
      - Design-First
      - Mock Servers
      - OpenAPI
      - Style Guides
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/platform/vrjs3xapm31b7-stoplight-documentation
      - type: Portal
        url: https://stoplight.io
      - type: Pricing
        url: https://stoplight.io/pricing
      - type: GettingStarted
        url: https://docs.stoplight.io/docs/platform/vrjs3xapm31b7-stoplight-documentation
      - type: Sign Up
        url: https://stoplight.io/welcome
      - type: Login
        url: https://stoplight.io/login
      - type: CaseStudies
        url: https://stoplight.io/case-studies
      - type: Solutions
        url: https://stoplight.io/solutions
  - aid: stoplight:prism
    name: Stoplight Prism
    description: Prism is an open-source HTTP mock and proxy server that turns any OpenAPI v2/v3 or Postman Collection file into a realistic API server with mocking, transformations, and validations. Enables frontend and backend teams to develop in parallel using API descriptions. Can be used as a local CLI tool or via hosted Stoplight mock servers. Supports dynamic example generation, request/response validation, and content negotiation.
    humanURL: https://stoplight.io/open-source/prism
    tags:
      - API Testing
      - Mock Servers
      - Open Source
      - OpenAPI
      - Postman
      - Proxy
      - Validation
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/prism
      - type: GitHubRepository
        url: https://github.com/stoplightio/prism
      - type: NPM
        url: https://www.npmjs.com/package/@stoplight/prism-cli
  - aid: stoplight:spectral
    name: Stoplight Spectral
    description: Spectral is an open-source JSON and YAML linter for creating automated API style guides and governance rulesets. Provides built-in support for OpenAPI v3.1, v3.0, and v2.0, Arazzo v1.0, and AsyncAPI v2.x. Enables teams to validate API descriptions against custom rulesets, enforce consistent design standards, and integrate API governance into CI/CD pipelines. Supports custom functions and third-party ruleset packages via npm.
    humanURL: https://stoplight.io/open-source/spectral
    tags:
      - API Governance
      - AsyncAPI
      - CI/CD
      - Linting
      - Open Source
      - OpenAPI
      - Style Guides
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/spectral
      - type: GitHubRepository
        url: https://github.com/stoplightio/spectral
      - type: NPM
        url: https://www.npmjs.com/package/@stoplight/spectral-cli
      - type: Docker
        url: https://hub.docker.com/r/stoplight/spectral
  - aid: stoplight:elements
    name: Stoplight Elements
    description: Elements is an open-source toolkit for building beautiful, interactive API documentation from OpenAPI specifications using embeddable React or Web Components. Provides highly customizable, interactive API reference documentation, including operation listings, request/response examples, schema viewers, and try-it functionality. Can be embedded in any web application or used as a standalone documentation site.
    humanURL: https://stoplight.io/open-source/elements
    tags:
      - API Documentation
      - Components
      - Open Source
      - OpenAPI
      - React
      - Web Components
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/elements
      - type: GitHubRepository
        url: https://github.com/stoplightio/elements
      - type: NPM
        url: https://www.npmjs.com/package/@stoplight/elements
      - type: Demo
        url: https://elements-demo.stoplight.io/
  - aid: stoplight:studio
    name: Stoplight Studio
    description: Stoplight Studio is the visual API design and technical writing editor included in the Stoplight Platform. Provides a form-based editor for creating and editing OpenAPI v2 and v3 specifications with full validation, mocking, and modeling support. Includes a built-in Markdown editor, image manager, and the ability to publish documentation to the Stoplight documentation platform. Available as a web app and desktop application.
    humanURL: https://stoplight.io/api-design
    tags:
      - API Design
      - Editor
      - OpenAPI
      - Technical Writing
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/studio
      - type: GitHubRepository
        url: https://github.com/stoplightio/studio
  - aid: stoplight:cli
    name: Stoplight CLI
    description: The Stoplight CLI enables programmatic linting of API descriptions and pushing analysis results to the Stoplight Platform from CI/CD pipelines. Supports analyzing local projects, running Spectral rulesets, and integrating API governance checks into automated build workflows with GitHub Actions, CircleCI, Jenkins, and other CI platforms.
    humanURL: https://docs.stoplight.io/docs/platform/1e78f9c9bfc1e-stoplight-cli
    tags:
      - CI/CD
      - CLI
      - DevOps
      - Open Source
      - OpenAPI
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/platform/1e78f9c9bfc1e-stoplight-cli
      - type: NPM
        url: https://www.npmjs.com/package/@stoplight/cli
common:
  - type: Portal
    url: https://stoplight.io
  - type: Documentation
    url: https://docs.stoplight.io/
  - type: Pricing
    url: https://stoplight.io/pricing
  - type: Blog
    url: https://blog.stoplight.io/
  - type: About
    url: https://stoplight.io/about
  - type: Support
    url: https://support.stoplight.io/
  - type: Contact
    url: https://stoplight.io/contact
  - type: Status
    url: https://status.stoplight.io/
  - type: PrivacyPolicy
    url: https://stoplight.io/privacy
  - type: TermsOfService
    url: https://stoplight.io/terms
  - type: Security
    url: https://stoplight.io/security-practices
  - type: Sign Up
    url: https://stoplight.io/welcome
  - type: Login
    url: https://stoplight.io/login
  - type: GitHubOrg
    url: https://github.com/stoplightio
  - type: OpenSource
    url: https://stoplight.io/open-source
  - type: GettingStarted
    url: https://stoplight.io/api-development-guide
  - type: Solutions
    url: https://stoplight.io/solutions
  - type: CaseStudies
    url: https://stoplight.io/case-studies
  - type: Webinars
    url: https://stoplight.io/webinars
  - type: Guides
    url: https://stoplight.io/guides
  - type: Press
    url: https://stoplight.io/press
  - type: YouTube
    url: https://www.youtube.com/stoplight
  - type: APIGovernance
    url: https://stoplight.io/api-governance
  - type: APIDocumentation
    url: https://stoplight.io/api-documentation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

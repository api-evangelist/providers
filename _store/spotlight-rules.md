---
aid: api-evangelist-standards
name: Spotlight Rules
description: Spotlight Rules shines a light on the evolution of API linting rules, specifically Spectral rules and their transformation into Vacuum rules, and the broader ecosystem of tools, platforms, and rulesets that support API governance. The site documents the Spectral rule format (JSON/YAML-based configuration for linting OpenAPI, AsyncAPI, and Arazzo specs), the Vacuum rules format (a backward-compatible fork adding howToFix, id, and category fields), and curates integrations across IDEs, CI/CD pipelines, commercial API management platforms, and open-source developer tools. Spotlight Rules is published by API Evangelist (Kin Lane) as part of ongoing API governance research.
specificationVersion: '0.19'
type: Index
position: Provider
access: Public
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
tags:
  - API Governance
  - Linting
  - Spectral
  - Vacuum
  - OpenAPI
  - Standards
created: '2024-11-11'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/spotlight-rules/refs/heads/main/apis.yml
apis:
  - aid: api-evangelist-standards:spectral-rules
    name: Spectral Rules
    description: Spectral is the open-source API linting framework developed by Stoplight that validates JSON and YAML artifacts including OpenAPI (v2, v3.0, v3.1), AsyncAPI (v2.x), and Arazzo specifications. Spectral rules are defined in YAML or JavaScript configuration files and consist of rule names, descriptions, severity levels (error/warn/info/hint), given (JSONPath selectors), and then (assertion functions). Originally released in 2018, Spectral has become the de facto standard for API governance linting.
    humanURL: https://stoplight.io/open-source/spectral
    baseURL: https://spectral.stoplight.io
    tags:
      - Spectral
      - Linting
      - OpenAPI
      - API Governance
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.stoplight.io/docs/spectral
      - type: Repository
        url: https://github.com/stoplightio/spectral
      - type: NPM
        url: https://www.npmjs.com/package/@stoplight/spectral-cli
      - type: VSCode Extension
        url: https://marketplace.visualstudio.com/items?itemName=stoplight.spectral
      - type: GitHub Action
        url: https://github.com/marketplace/actions/spectral-linting
    features:
      - type: OpenAPILinting
        description: Validate OpenAPI 2.0, 3.0, and 3.1 specifications against custom rules
      - type: AsyncAPILinting
        description: Validate AsyncAPI 2.x specifications for consistency and standards
      - type: ArazzoLinting
        description: Lint Arazzo workflow specifications
      - type: CustomFunctions
        description: Extend rules with custom JavaScript functions for complex validation logic
      - type: MultiFormatSupport
        description: Validate YAML, JSON, and other structured document formats
      - type: CIIntegration
        description: GitHub Actions, GitLab CI, Jenkins, Azure DevOps, and CircleCI support
  - aid: api-evangelist-standards:vacuum-rules
    name: Vacuum Rules
    description: 'Vacuum is an ultra-fast OpenAPI linter written in Go, created by pb33f (Dave Shanley) as a high-performance alternative to Spectral CLI. Vacuum rules are a fork of Spectral rules that maintain full backward compatibility while adding three new fields: howToFix (remediation guidance), id (stable rule identifier), and category (organizational grouping). Vacuum supports both RFC 9535 JSONPath and JSON Path Plus extensions, and includes a built-in dashboard UI for visualizing lint results.'
    humanURL: https://quobix.com/vacuum/
    baseURL: https://quobix.com/vacuum
    tags:
      - Vacuum
      - Linting
      - OpenAPI
      - API Governance
      - Go
      - High Performance
    properties:
      - type: Documentation
        url: https://quobix.com/vacuum/
      - type: Repository
        url: https://github.com/daveshanley/vacuum
      - type: JSONSchema
        url: https://spotlight-rules.com/vacuum-rules-schema.json
    features:
      - type: SpectralCompatibility
        description: 100% compatible with Spectral rulesets - run existing rules without modification
      - type: HighPerformance
        description: Written in Go for blazing-fast linting of large OpenAPI specifications
      - type: HowToFix
        description: Optional howToFix field providing remediation guidance to developers
      - type: RuleCategories
        description: Optional category field for organizing rules into governance domains
      - type: DashboardUI
        description: Built-in visual dashboard for browsing and understanding lint results
      - type: JSONPathRFC9535
        description: Supports the official RFC 9535 JSONPath standard plus JSON Path Plus extensions
  - aid: api-evangelist-standards:published-rulesets
    name: Published Community Rulesets
    description: A curated collection of publicly available Spectral and Vacuum rulesets published by major organizations as governance references, including Adidas, Microsoft Azure, Digital Ocean, and OWASP. These rulesets demonstrate real-world API governance practices and can be extended or adopted by other organizations.
    humanURL: https://spotlight-rules.com/
    tags:
      - Governance
      - Community
      - Standards
      - OpenAPI
    properties:
      - type: Reference
        url: https://github.com/adidas/api-guidelines
      - type: Reference
        url: https://github.com/Azure/azure-api-style-guide
      - type: Reference
        url: https://github.com/digitalocean/openapi
      - type: Reference
        url: https://github.com/stoplightio/spectral-owasp-ruleset
common:
  - type: Website
    url: https://spotlight-rules.com/
  - type: Standards
    url: https://github.com/api-evangelist/standards/standards.yml
  - type: GitHub
    url: https://github.com/api-evangelist/spotlight-rules
  - type: Email
    url: mailto:kin@apievangelist.com
  - type: LinkedIn
    url: https://www.linkedin.com/in/kinlane/
  - type: JSONSchema
    url: json-schema/spectral-rule-schema.json
  - type: JSONSchema
    url: json-schema/vacuum-rule-schema.json
  - type: Vocabulary
    url: vocabulary/spotlight-rules-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    X-github: kinlane
---

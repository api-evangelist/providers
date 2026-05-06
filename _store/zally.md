---
aid: zally
name: Zally
description: Zally is an open source API linter from Zalando that validates OpenAPI 2 and 3 specifications against configurable rule sets for API design consistency. It exposes a REST API, command-line interface, and web UI for checking API designs against Zalando's RESTful API Guidelines or custom rule sets.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - API Linting
  - API Quality
  - Open Source
  - OpenAPI
  - Zalando
url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zally:zally-api
    name: Zally API
    description: The Zally REST API performs linting of OpenAPI specifications against configurable rule sets. It returns violations grouped by rule severity (MUST, SHOULD, COULD, MAY, HINT), tracks linting statistics, and lists supported rules. Authentication is via Bearer JWT.
    humanURL: https://opensource.zalando.com/zally/
    baseURL: https://zally.on.inter.net
    tags:
      - API Linting
      - API Quality
      - OpenAPI
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/openapi/zally-api.yml
      - type: Documentation
        url: https://opensource.zalando.com/zally/
      - type: APIReference
        url: https://github.com/zalando/zally/blob/main/server/zally-server/src/main/resources/api/zally-api.yaml
      - type: Authentication
        url: https://github.com/zalando/zally/tree/main/server#authentication
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/json-schema/
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/json-structure/
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/json-ld/zally-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/examples/
common:
  - type: Website
    url: https://opensource.zalando.com/zally/
    name: Zally Project Website
  - type: Documentation
    url: https://github.com/zalando/zally#readme
    name: Zally README
  - type: GitHubRepository
    url: https://github.com/zalando/zally
    name: Zalando Zally Repository
  - type: GitHubOrganization
    url: https://github.com/zalando
    name: Zalando GitHub Organization
  - type: License
    url: https://github.com/zalando/zally/blob/main/LICENSE
    name: MIT License
  - type: Issues
    url: https://github.com/zalando/zally/issues
    name: GitHub Issues
  - type: ChangeLog
    url: https://github.com/zalando/zally/releases
    name: Releases
  - type: CLI
    url: https://github.com/zalando/zally/tree/main/cli
    name: Zally CLI
  - type: SDK
    url: https://github.com/zalando/zally/tree/main/web-ui
    name: Zally Web UI
  - type: Specification
    url: https://opensource.zalando.com/restful-api-guidelines/
    name: Zalando RESTful API Guidelines
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/rules/zally-rules.yml
    name: Zally Spectral Ruleset
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/vocabulary/zally-vocabulary.yml
    name: Zally Vocabulary
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/capabilities/zally-workflow.yaml
    name: Zally Workflow Capability
  - data:
      - name: API Linting
        description: Validate OpenAPI 2/3 specifications against rule sets to enforce design consistency.
      - name: Configurable Rules
        description: Customize default Zalando RESTful API Guidelines rules or define custom rule sets.
      - name: Multiple Interfaces
        description: REST API for programmatic access, CLI for local checking, and Web UI for visual review.
      - name: Ignore Extension
        description: Use x-zally-ignore extension in specs to selectively bypass rules.
      - name: Rule Severity Levels
        description: Rules categorized as MUST, SHOULD, COULD, MAY, and HINT for graduated enforcement.
      - name: Linting Statistics
        description: Track linting requests and aggregate review statistics over time.
    name: Features
    type: Features
  - data:
      - name: API Design Review
        description: Review OpenAPI specs in pull requests to enforce design standards before merge.
      - name: API Governance
        description: Enforce organizational API guidelines across teams via shared rule sets.
      - name: API Quality Gate
        description: Block API releases that violate critical MUST rules in CI/CD pipelines.
      - name: Style Guide Enforcement
        description: Encode an API style guide as executable rules and apply consistently.
    name: UseCases
    type: UseCases
  - data:
      - name: GitHub Actions
        description: Run Zally linting in GitHub Actions workflows on PRs.
      - name: Spectral
        description: Translate Zally rule sets to Spectral rulesets for OpenAPI 3 alignment.
      - name: Zalando RESTful API Guidelines
        description: Default rule set ships with rules from Zalando's public API guidelines.
    name: Integrations
    type: Integrations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

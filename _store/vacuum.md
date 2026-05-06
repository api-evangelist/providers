---
aid: vacuum
name: Vacuum
description: Vacuum is the world's fastest and most versatile OpenAPI linter and toolkit, built in Go for validating and linting API specifications at scale. It is 100% compatible with Spectral rulesets and supports OpenAPI 3.0, 3.1, and 3.2.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - Documentation
  - Linting
  - OpenAPI
  - Spectral
  - Developer Tools
  - Go
url: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vacuum:vacuum
    name: Vacuum
    description: Vacuum is the world's fastest OpenAPI linter written in Go. It processes API specifications at lightning speed with full Spectral ruleset compatibility, interactive dashboards, HTML reports, and Language Server Protocol support.
    humanURL: https://quobix.com/vacuum
    tags:
      - API Linting
      - OpenAPI
      - Spectral
      - Documentation
      - Developer Tools
      - CI/CD
    properties:
      - type: Documentation
        url: https://quobix.com/vacuum/about
      - type: Getting Started
        url: https://quobix.com/vacuum/start
      - type: GitHub
        url: https://github.com/daveshanley/vacuum
      - type: Docker
        url: https://hub.docker.com/r/dshanley/vacuum
      - type: NPM
        url: https://www.npmjs.com/package/@quobix/vacuum
    features:
      - name: OpenAPI Linting
        description: Validate and lint OpenAPI 3.0, 3.1, and 3.2 specifications
      - name: Spectral Compatibility
        description: 100% compatible with existing Spectral rulesets
      - name: Interactive Dashboard
        description: Console UI for exploring violations and rules interactively
      - name: HTML Reports
        description: Generate browser-viewable HTML linting reports
      - name: Vacuum Sealed Reports
        description: Portable report snapshots that can be re-rendered without re-running analysis
      - name: Language Server Protocol
        description: LSP support for IDE integration including VSCode
      - name: Custom Rules
        description: Create custom rulesets in Go or JavaScript
      - name: OWASP Security Rules
        description: Built-in OWASP API security rule support
      - name: Overlay Support
        description: Apply non-destructive modifications to specs using OpenAPI Overlays
      - name: Auto-fixing
        description: Automatically resolve certain rule violations
      - name: Change Detection
        description: Detect changes between OpenAPI spec versions
      - name: Bundle
        description: Combine exploded OpenAPI specs into single files
      - name: GitHub Actions
        description: Native GitHub Actions integration for CI/CD pipelines
    useCases:
      - name: CI/CD Pipeline Integration
        description: Enforce OpenAPI quality standards in automated build pipelines
      - name: Enterprise API Governance
        description: Validate large collections of API specs across an organization
      - name: API Design Reviews
        description: Automated quality checks during API design and development
      - name: Spectral Migration
        description: Drop-in replacement for Spectral with better performance
    integrations:
      - name: GitHub Actions
        description: CI/CD integration via official GitHub Action
        url: https://github.com/marketplace/actions/vacuum-openapi-linter
      - name: VSCode
        description: IDE plugin via Language Server Protocol
      - name: Spectral
        description: Compatible with Spectral rulesets and report formats
common:
  - type: Website
    url: https://quobix.com/vacuum
  - type: Documentation
    url: https://quobix.com/vacuum/about
  - type: GitHub Organization
    url: https://github.com/daveshanley
  - type: GitHub Repository
    url: https://github.com/daveshanley/vacuum
  - type: NPM Package
    url: https://www.npmjs.com/package/@quobix/vacuum
  - type: Docker Image
    url: https://hub.docker.com/r/dshanley/vacuum
  - type: Discord
    url: https://discord.gg/UAcUF78MQN
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/json-schema/vacuum-ruleset-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/json-schema/vacuum-report-schema.json
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/vacuum/refs/heads/main/vocabulary/vacuum-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

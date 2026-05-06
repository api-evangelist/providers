---
aid: sonarqube
name: SonarQube
description: SonarQube is a leading code quality and security platform that provides Web APIs for managing projects, quality gates, issues, and integrations with CI/CD pipelines to deliver clean, secure code.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Code Quality
  - DevOps
  - Security
  - Static Analysis
url: https://raw.githubusercontent.com/api-evangelist/sonarqube/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sonarqube:web-api
    name: SonarQube Web API
    description: HTTP API for programmatic interaction with SonarQube Server, enabling management of projects, quality gates, issues, rules, users, and integrations with external tools.
    humanURL: https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/
    tags:
      - Code Quality
      - Security
      - Static Analysis
    properties:
      - type: Documentation
        url: https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/
      - type: Reference
        url: https://api-docs.sonarsource.com/
      - type: OpenAPI
        url: openapi/sonarqube-web-api-openapi.yml
      - type: JSONSchema
        url: json-schema/sonarqube-issue-schema.json
        title: Issue Schema
      - type: JSONSchema
        url: json-schema/sonarqube-project-schema.json
        title: Project Schema
      - type: JSONSchema
        url: json-schema/sonarqube-quality-gate-schema.json
        title: Quality Gate Schema
      - type: JSONStructure
        url: json-structure/sonarqube-web-api-structure.json
      - type: JSONLD
        url: json-ld/sonarqube-context.jsonld
      - type: SpectralRules
        url: rules/sonarqube-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/sonarqube-web-api.yaml
      - type: Example
        url: examples/sonarqube-search-issues-example.json
        title: Search Issues Example
      - type: Example
        url: examples/sonarqube-quality-gate-status-example.json
        title: Quality Gate Status Example
      - type: Example
        url: examples/sonarqube-component-measures-example.json
        title: Component Measures Example
common:
  - type: Portal
    url: https://www.sonarsource.com/products/sonarqube/
  - type: Documentation
    url: https://docs.sonarsource.com/sonarqube-server/
  - type: Reference
    url: https://api-docs.sonarsource.com/
  - type: Website
    url: https://www.sonarsource.com/
  - type: GitHubOrganization
    url: https://github.com/SonarSource
  - type: Blog
    url: https://www.sonarsource.com/blog/
  - type: Support
    url: https://community.sonarsource.com/
  - type: Status
    url: https://status.sonarsource.com/
  - type: Pricing
    url: https://www.sonarsource.com/plans-and-pricing/
  - type: TermsOfService
    url: https://www.sonarsource.com/terms/
  - type: PrivacyPolicy
    url: https://www.sonarsource.com/privacy/
  - type: NaftikoCapability
    url: capabilities/code-quality-governance.yaml
    title: Code Quality Governance Workflow
  - type: Vocabulary
    url: vocabulary/sonarqube-vocabulary.yml
    title: SonarQube Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

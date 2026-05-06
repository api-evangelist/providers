---
aid: sonar
name: Sonar
description: Sonar (SonarSource) provides code quality and security analysis tools for developers. Products include SonarQube (self-hosted), SonarCloud (cloud-hosted), and SonarLint (IDE plugin), offering continuous inspection through static code analysis across 30+ programming languages.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CI/CD
  - Code Quality
  - DevOps
  - Security
  - SonarCloud
  - SonarQube
  - Static Analysis
url: https://raw.githubusercontent.com/api-evangelist/sonar/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sonar:sonarqube-web-api
    name: SonarQube Web API
    description: REST API for interacting with SonarQube Server, enabling management of projects, quality gates, issues, rules, users, and CI/CD integrations. Uses token-based authentication.
    humanURL: https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/
    tags:
      - Code Quality
      - DevOps
      - Security
      - SonarQube
      - Static Analysis
      - Technical Debt
    properties:
      - type: Documentation
        url: https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/
      - type: Reference
        url: https://api-docs.sonarsource.com/
      - type: Authentication
        url: https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/
  - aid: sonar:sonarcloud-api
    name: SonarCloud API
    description: Cloud-based code quality and security analysis API for analyzing code repositories from GitHub, GitLab, Bitbucket, and Azure DevOps organizations. Provides organization management, project analysis, issue tracking, quality gate monitoring, and metric retrieval.
    humanURL: https://sonarcloud.io/web_api
    tags:
      - Bitbucket
      - CI/CD
      - Cloud
      - Code Quality
      - GitHub
      - GitLab
      - SonarCloud
    properties:
      - type: Documentation
        url: https://sonarcloud.io/web_api
      - type: GettingStarted
        url: https://docs.sonarcloud.io/
      - type: Authentication
        url: https://docs.sonarcloud.io/advanced-setup/api-authentication/
      - type: OpenAPI
        url: openapi/sonar-sonarcloud-api-openapi.yml
      - type: JSONSchema
        url: json-schema/sonar-organization-schema.json
        title: Organization Schema
      - type: JSONSchema
        url: json-schema/sonar-issue-schema.json
        title: Issue Schema
      - type: JSONStructure
        url: json-structure/sonar-sonarcloud-structure.json
      - type: JSONLD
        url: json-ld/sonar-context.jsonld
      - type: SpectralRules
        url: rules/sonar-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/sonarcloud-api.yaml
      - type: Example
        url: examples/sonar-search-organizations-example.json
        title: Search Organizations Example
      - type: Example
        url: examples/sonar-quality-gate-status-example.json
        title: Quality Gate Status Example
common:
  - type: Website
    url: https://www.sonarsource.com/
  - type: Blog
    url: https://www.sonarsource.com/blog/
  - type: GitHubOrganization
    url: https://github.com/SonarSource
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
    url: capabilities/cloud-code-quality.yaml
    title: Cloud Code Quality Workflow
  - type: Vocabulary
    url: vocabulary/sonar-vocabulary.yml
    title: Sonar Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

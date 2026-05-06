---
aid: 42crunch
url: https://raw.githubusercontent.com/api-evangelist/42crunch/refs/heads/main/apis.yml
name: 42Crunch
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Security
  - Platform
  - Scanning
  - Security
  - OpenAPI
  - DevSecOps
description: 42Crunch is a leading API security company that specializes in protecting and securing APIs. They provide innovative solutions that help organizations safeguard their sensitive data and critical assets from potential cyber threats. With their comprehensive API security platform, 42Crunch offers a range of services such as API scanning, traffic monitoring, and runtime protection to ensure that APIs are secure and compliant with industry standards. Their platform covers the full API security lifecycle from design and audit through dynamic testing and runtime firewall protection.
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: 42crunch:42crunch-api-security-audit
    name: 42Crunch API Security Audit
    tags:
      - API Security
      - Static Analysis
      - OpenAPI
      - Vulnerability Scanning
    humanURL: https://docs.42crunch.com/latest/content/concepts/api_contract_security_audit.htm
    properties:
      - url: https://docs.42crunch.com/latest/content/concepts/api_contract_security_audit.htm
        type: Documentation
      - url: https://docs.42crunch.com/latest/content/home.htm
        type: APIReference
    description: The 42Crunch API Security Audit performs automated static analysis of API definitions (OpenAPI 2, 3.0, 3.1 and GraphQL), running over 200 checks across format validation, data definition quality, and security analysis. APIs are scored 0-100 with recommendations to reach 70+ before runtime protection is applied. Integrates with CI/CD pipelines for continuous monitoring.
  - aid: 42crunch:42crunch-api-scan
    name: 42Crunch API Scan
    tags:
      - API Security
      - Dynamic Testing
      - DAST
      - Contract Testing
    humanURL: https://docs.42crunch.com/latest/content/home.htm
    properties:
      - url: https://docs.42crunch.com/latest/content/home.htm
        type: Documentation
    description: 42Crunch API Scan performs dynamic API security testing (DAST) that evaluates runtime API behavior against its OpenAPI specification. It tests how well an API adheres to its contract and identifies vulnerabilities that only appear at runtime. Supports integration with CI/CD pipelines and Kubernetes via the scand-manager Kubernetes wrapper.
  - aid: 42crunch:42crunch-api-protection
    name: 42Crunch API Protection
    tags:
      - API Security
      - Runtime Protection
      - Firewall
      - API Gateway
    humanURL: https://docs.42crunch.com/latest/content/home.htm
    properties:
      - url: https://docs.42crunch.com/latest/content/home.htm
        type: Documentation
    description: 42Crunch API Protection deploys an API-native micro firewall (API Firewall) that provides runtime defense against API attacks. The firewall is tailor-made for each API based on its OpenAPI specification and enforces API contract compliance in real time, blocking malformed requests and unauthorized access.
  - aid: 42crunch:42crunch-scand-manager
    name: 42Crunch API Conformance Scan Jobs Manager
    tags:
      - API Security
      - Kubernetes
      - Conformance Scanning
      - DevSecOps
    humanURL: https://github.com/42Crunch/scand-manager
    properties:
      - url: https://github.com/42Crunch/scand-manager
        type: Documentation
      - url: openapi/42crunch-scand-manager.yaml
        type: OpenAPI
      - url: json-schema/scand-manager-job-name-schema.json
        type: JSONSchema
        title: Job Name Schema
      - url: json-schema/scand-manager-jobs-schema.json
        type: JSONSchema
        title: Jobs Schema
      - url: json-schema/scand-manager-job-spec-schema.json
        type: JSONSchema
        title: Job Spec Schema
      - url: json-schema/scand-manager-job-status-schema.json
        type: JSONSchema
        title: Job Status Schema
      - url: json-schema/scand-manager-error-schema.json
        type: JSONSchema
        title: Error Schema
      - url: json-structure/scand-manager-job-name-structure.json
        type: JSONStructure
        title: Job Name Structure
      - url: json-structure/scand-manager-jobs-structure.json
        type: JSONStructure
        title: Jobs Structure
      - url: json-structure/scand-manager-job-spec-structure.json
        type: JSONStructure
        title: Job Spec Structure
      - url: json-structure/scand-manager-job-status-structure.json
        type: JSONStructure
        title: Job Status Structure
      - url: json-structure/scand-manager-error-structure.json
        type: JSONStructure
        title: Error Structure
      - url: examples/scand-manager-job-name-example.json
        type: Example
        title: Job Name Example
      - url: examples/scand-manager-jobs-example.json
        type: Example
        title: Jobs Example
      - url: examples/scand-manager-job-spec-example.json
        type: Example
        title: Job Spec Example
      - url: examples/scand-manager-job-status-example.json
        type: Example
        title: Job Status Example
      - url: examples/scand-manager-error-example.json
        type: Example
        title: Error Example
    description: The 42Crunch Scand Manager provides a convenient way to run 42Crunch API Conformance Scans on-premises as Kubernetes Jobs. It manages the full lifecycle of scan jobs including creation, status monitoring, log retrieval, and deletion.
common:
  - type: Website
    url: https://42crunch.com/
  - type: Documentation
    url: https://docs.42crunch.com/latest/content/home.htm
  - type: Blog
    url: https://42crunch.com/blog/
  - type: Support
    url: https://support.42crunch.com/hc/en-us
  - type: Pricing
    url: https://42crunch.com/pricing/
  - type: Tutorials
    url: https://42crunch.com/tutorials/
  - type: Webinars
    url: https://42crunch.com/webinars/
  - type: Partners
    url: https://42crunch.com/partners/
  - type: Login
    url: https://platform.42crunch.com/login
  - type: GitHubOrganization
    url: https://github.com/42Crunch
  - type: IDESupport
    url: https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi
  - type: IDESupport
    url: https://plugins.jetbrains.com/plugin/14837-openapi-swagger-editor
  - type: GitHubRepository
    url: https://github.com/42Crunch/vscode-openapi
  - type: GitHubRepository
    url: https://github.com/42Crunch/api-security-audit-action
  - type: GitHubRepository
    url: https://github.com/42Crunch/api-security-audit-action-freemium
  - type: GitHubRepository
    url: https://github.com/42Crunch/api-security-scan-action-freemium
  - type: GitHubRepository
    url: https://github.com/42Crunch/cicd-github-actions
  - type: GitHubRepository
    url: https://github.com/42Crunch/scand-manager
  - type: GitHubRepository
    url: https://github.com/42Crunch/resources
  - type: SpectralRules
    url: rules/42crunch-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/42crunch-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/scand-manager.yaml
  - type: NaftikoCapability
    url: capabilities/api-security-scanning.yaml
  - type: JSON-LD
    url: json-ld/42crunch-scand-manager-context.jsonld
  - type: Features
    data:
      - name: API Security Audit
        description: Automated static analysis of OpenAPI and GraphQL definitions running over 200 security checks, scoring APIs 0-100 for vulnerability and compliance issues.
      - name: API Scan (DAST)
        description: Dynamic API Security Testing that evaluates runtime API behavior against its OpenAPI contract, identifying vulnerabilities that appear only at runtime.
      - name: API Firewall
        description: API-native micro firewall that enforces OpenAPI contract compliance at runtime, blocking malformed requests, unauthorized access, and API attacks.
      - name: API Discovery
        description: Identifies and catalogs APIs across environments to provide full visibility into the API attack surface.
      - name: CI/CD Integration
        description: GitHub Actions and other CI/CD pipeline integrations for automated security scanning in deployment workflows.
      - name: IDE Integration
        description: Plugins for VS Code and IntelliJ/JetBrains IDEs that provide real-time OpenAPI editing, validation, and security feedback during API design.
      - name: OpenAPI Contract Security
        description: Enforces security best practices in OpenAPI specifications covering authentication, data validation, input/output schemas, and transport security.
      - name: Kubernetes Support
        description: Scand Manager provides a Kubernetes wrapper for running 42Crunch API Scan in containerized environments.
  - type: UseCases
    data:
      - name: API Security Testing in CI/CD
        description: Embed automated API security scanning into CI/CD pipelines via GitHub Actions to catch vulnerabilities before they reach production.
      - name: OpenAPI Specification Review
        description: Audit OpenAPI definitions for security flaws, missing authentication, weak data validation, and schema gaps before API deployment.
      - name: Runtime API Protection
        description: Deploy the API Firewall in front of production APIs to enforce contract compliance and block attacks in real time.
      - name: DevSecOps API Governance
        description: Provide development, security, and operations teams with shared visibility into API security posture throughout the API lifecycle.
      - name: OWASP API Top 10 Compliance
        description: Systematically identify and remediate OWASP API Security Top 10 vulnerabilities in API definitions and runtime behavior.
      - name: API Security for Financial Services
        description: Address regulatory and compliance requirements for API security in banking, financial services, and insurance sectors.
      - name: Healthcare API Security
        description: Secure healthcare APIs handling sensitive patient data against unauthorized access and data exposure vulnerabilities.
  - type: Integrations
    data:
      - name: GitHub Actions
        description: Native GitHub Actions for API Security Audit and API Scan, enabling automated security checks in GitHub CI/CD workflows.
      - name: VS Code
        description: OpenAPI extension for Visual Studio Code providing real-time API editing, validation, and security feedback with 42Crunch integration.
      - name: IntelliJ / JetBrains
        description: OpenAPI/Swagger Editor plugin for IntelliJ IDEA and other JetBrains IDEs.
      - name: Kubernetes
        description: Scand Manager provides Kubernetes-native deployment of API Scan for containerized API security testing.
      - name: Tekton
        description: Tekton Pipelines catalog integration for CI/CD security scanning tasks.
      - name: SonarQube
        description: SonarQube plugin that integrates 42Crunch API security audit results into code quality dashboards.
      - name: API Gateways
        description: API Firewall integrates with API gateway infrastructure to enforce contract compliance at the network edge.
      - name: SIEM / SOC Systems
        description: Runtime protection events can be forwarded to SIEM and SOC platforms for centralized threat monitoring and alerting.
      - name: Atlassian
        description: Data Center App Performance Toolkit support for Atlassian platform integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

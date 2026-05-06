---
aid: synopsys
name: Synopsys
description: Synopsys is a global leader in semiconductor design EDA tools and software security testing. The company's Software Integrity Group (now rebranded as Black Duck) provides application security testing products including Polaris, Coverity (SAST), Black Duck (SCA), and Seeker (IAST). Synopsys also offers cloud-based EDA and semiconductor design services through the Synopsys Cloud platform with the OpenLink API for license entitlement management.
url: https://raw.githubusercontent.com/api-evangelist/synopsys/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
tags:
  - Software Security
  - Application Security Testing
  - Static Analysis
  - Software Composition Analysis
  - EDA Tools
  - Semiconductor Design
apis:
  - aid: synopsys:polaris
    name: Synopsys Polaris API
    description: The Polaris Software Integrity Platform API provides programmatic access to application security testing orchestration, project management, scan configuration, and issue tracking. Polaris integrates with GitHub, GitLab, Bitbucket, and Azure DevOps for event-driven security scanning automation across SAST, SCA, and IAST testing.
    humanURL: https://polaris.synopsys.com/developer/default/documentation
    baseURL: https://polaris.synopsys.com/api
    tags:
      - Application Security
      - Static Analysis
      - Software Composition Analysis
      - DevSecOps
      - CI/CD Integration
    properties:
      - type: Documentation
        url: https://polaris.synopsys.com/developer/default/documentation
      - type: APIQuickstart
        url: https://polaris.synopsys.com/developer/default/documentation/t_api-quickstart
      - type: OpenAPI
        url: openapi/synopsys-polaris-openapi.yml
      - type: SpectralRules
        url: rules/synopsys-rules.yml
  - aid: synopsys:coverity
    name: Synopsys Coverity REST API
    description: The Coverity Platform REST API provides programmatic access to Coverity static analysis results, project and stream management, defect management, and security findings. Coverity performs deep source code examination across 20+ programming languages and 70+ frameworks to detect critical quality and security defects.
    humanURL: https://community.synopsys.com/s/topic/0TO34000000LmwWGAS/rest-api
    baseURL: https://coverity.synopsys.com/api
    tags:
      - Static Analysis
      - SAST
      - Code Quality
      - Defect Management
      - Security Testing
    properties:
      - type: Documentation
        url: https://community.synopsys.com/s/topic/0TO34000000LmwWGAS/rest-api
      - type: OpenAPISpec
        url: https://documentation.blackduck.com/bundle/coverity-docs/page/cim-api-docs/openapi/cim-openapi.html
  - aid: synopsys:cloud-openlink
    name: Synopsys Cloud OpenLink API
    description: The Synopsys Cloud OpenLink API enables semiconductor vendors to interoperate with Synopsys Cloud for managing product entitlements and license distribution. The API supports API key and OAuth2 authentication with JSON payloads over HTTPS. It exposes vendor entitlement endpoints and license request endpoints for both synchronous and asynchronous license delivery.
    humanURL: https://www.synopsys.com/cloud/openlink/api.html
    baseURL: https://api.synopsys.com/openlink
    tags:
      - EDA Tools
      - License Management
      - Semiconductor Design
      - Cloud Platform
    properties:
      - type: Documentation
        url: https://www.synopsys.com/cloud/openlink/api.html
      - type: OpenAPI
        url: openapi/synopsys-cloud-openlink-openapi.yml
  - aid: synopsys:seeker
    name: Synopsys Seeker REST API
    description: The Seeker REST API provides programmatic access to Seeker IAST (Interactive Application Security Testing) functionality including project management, vulnerability export, compliance reporting, and administration automation.
    humanURL: https://demo.seeker.synopsys.com/internal/help/en/topics/r_using_apis.html
    baseURL: https://seeker.synopsys.com/api
    tags:
      - IAST
      - Interactive Testing
      - Vulnerability Management
      - Application Security
    properties:
      - type: Documentation
        url: https://demo.seeker.synopsys.com/internal/help/en/topics/r_using_apis.html
common:
  - type: Website
    url: https://www.synopsys.com
  - type: DeveloperPortal
    url: https://polaris.synopsys.com/developer/
  - type: Community
    url: https://community.synopsys.com/
  - type: GitHubOrg
    url: https://github.com/synopsys-sig
  - type: JSONLDContext
    url: json-ld/synopsys-context.jsonld
  - type: Vocabulary
    url: vocabulary/synopsys-vocabulary.yml
features:
  - Static Application Security Testing (SAST)
  - Software Composition Analysis (SCA)
  - Interactive Application Security Testing (IAST)
  - Dynamic Application Security Testing (DAST)
  - License Compliance
  - DevSecOps Pipeline Integration
  - CI/CD Plugin Support
  - Multi-Language Support (20+ Languages)
  - EDA Cloud Platform
  - License Entitlement Management
useCases:
  - Application Security Testing Automation
  - DevSecOps Integration
  - Open Source Risk Management
  - Code Quality and Security Analysis
  - Compliance Reporting
  - Semiconductor Design Tool Licensing
integrations:
  - type: GitHub
    description: GitHub Actions and App integration
  - type: GitLab
    description: GitLab CI/CD integration
  - type: AzureDevOps
    description: Azure DevOps pipeline integration
  - type: Jenkins
    description: Jenkins plugin for CI/CD
solutions:
  - Secure Software Development Lifecycle (SSDLC)
  - Cloud-Native Application Security
  - Enterprise Code Security Platform
---

---
aid: jfrog
url: https://raw.githubusercontent.com/api-evangelist/jfrog/refs/heads/main/apis.yml
apis:
- name: JFrog Artifactory REST API
  description: REST API for managing artifacts, repositories, security, and system configuration in JFrog Artifactory. Provides endpoints for uploading, downloading, searching, and managing binary artifacts across all package types.
  image: https://jfrog.com/brand/artifactory-logo.png
  baseURL: https://myserver.jfrog.io/artifactory/api
  humanURL: https://jfrog.com/artifactory/
  tags:
  - Artifacts
  - Binary Management
  - DevOps
  - Package Management
  - Repository Management
  properties:
  - type: Documentation
    url: https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API
  - type: OpenAPI
    url: openapi/jfrog-artifactory-openapi.yml
  - type: Authentication
    url: https://www.jfrog.com/confluence/display/JFROG/Access+Tokens
  - type: Getting Started
    url: https://jfrog.com/help/r/jfrog-artifactory-documentation/use-the-rest-api
  - type: Reference
    url: https://jfrog.com/help/r/jfrog-rest-apis/artifactory-rest-apis
- name: JFrog Artifactory REST API V2
  description: The next generation Artifactory REST API providing improved endpoints for repository management, artifact operations, and system administration with enhanced consistency and functionality.
  baseURL: https://myserver.jfrog.io/artifactory/api/v2
  humanURL: https://jfrog.com/artifactory/
  tags:
  - API V2
  - Artifacts
  - Binary Management
  - Package Management
  - Repository Management
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-rest-apis/artifactory-rest-api-v2
  - type: OpenAPI
    url: openapi/jfrog-artifactory-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- name: JFrog Xray REST API
  description: API for vulnerability scanning, license compliance, and impact analysis. Provides Software Composition Analysis capabilities tightly integrated with Artifactory to ensure security and compliance governance.
  image: https://jfrog.com/brand/xray-logo.png
  baseURL: https://myserver.jfrog.io/xray/api
  humanURL: https://jfrog.com/xray/
  tags:
  - DevSecOps
  - License Compliance
  - Security
  - Software Composition Analysis
  - Vulnerability Scanning
  properties:
  - type: Documentation
    url: https://www.jfrog.com/confluence/display/JFROG/Xray+REST+API
  - type: OpenAPI
    url: openapi/jfrog-xray-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
  - type: Reference
    url: https://jfrog.com/help/r/xray-rest-apis
  - type: Getting Started
    url: https://jfrog.com/help/r/xray-rest-apis/introduction-to-the-xray-rest-apis
- name: JFrog Distribution REST API
  description: API for distributing release binaries to multiple remote locations. Enables secure, reliable distribution of release bundles across edge nodes and remote sites at scale.
  baseURL: https://myserver.jfrog.io/distribution/api
  humanURL: https://jfrog.com/distribution/
  tags:
  - CDN
  - Distribution
  - Edge Nodes
  - Release Management
  - Software Distribution
  properties:
  - type: Documentation
    url: https://www.jfrog.com/confluence/display/JFROG/Distribution+REST+API
  - type: OpenAPI
    url: openapi/jfrog-distribution-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
  - type: Reference
    url: https://jfrog.com/help/r/jfrog-rest-apis/distribution-rest-apis
- name: JFrog Pipelines REST API
  description: API for managing CI/CD pipelines and automation workflows. Provides endpoints for creating, executing, and monitoring pipelines, runs, resources, and pipeline artifacts.
  baseURL: https://myserver.jfrog.io/pipelines/api
  humanURL: https://jfrog.com/pipelines/
  tags:
  - Automation
  - CI/CD
  - DevOps
  - Pipelines
  - Workflows
  properties:
  - type: Documentation
    url: https://www.jfrog.com/confluence/display/JFROG/Pipelines+REST+API
  - type: OpenAPI
    url: openapi/jfrog-pipelines-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
  - type: Getting Started
    url: https://jfrog.com/help/r/jfrog-rest-apis/introduction-to-the-pipelines-rest-apis
  - type: Reference
    url: https://jfrog.com/help/r/jfrog-rest-apis/pipelines-rest-apis
- name: JFrog Platform REST API
  description: Unified API for JFrog Platform services and administration. Provides centralized endpoints for managing platform-wide configuration, system health, licenses, and cross-service operations.
  baseURL: https://myserver.jfrog.io/
  humanURL: https://jfrog.com/platform/
  tags:
  - Access Management
  - Administration
  - Configuration
  - Platform
  - System Health
  properties:
  - type: Documentation
    url: https://www.jfrog.com/confluence/display/JFROG/JFrog+Platform+REST+API
  - type: OpenAPI
    url: openapi/jfrog-platform-openapi.yml
  - type: Authentication
    url: https://www.jfrog.com/confluence/display/JFROG/Access+Tokens
  - type: Getting Started
    url: https://jfrog.com/help/r/jfrog-rest-apis/introduction-to-the-jfrog-platform-rest-apis
  - type: Reference
    url: https://jfrog.com/help/r/jfrog-rest-apis/jfrog-platform-rest-apis
- name: JFrog Access REST API
  description: API for managing users, groups, permissions, projects, and access tokens across the JFrog Platform. Handles identity management, role-based access control, and scoped token creation.
  baseURL: https://myserver.jfrog.io/access/api
  humanURL: https://jfrog.com/platform/
  tags:
  - Access Management
  - Authentication
  - Permissions
  - Tokens
  - Users
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-token-rest-api
  - type: OpenAPI
    url: openapi/jfrog-access-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
  - type: Getting Started
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/introduction-to-access-tokens
- name: JFrog Curation REST API
  description: API for managing package curation policies that automatically vet and block malicious, vulnerable, or risky open-source packages before they enter the development environment.
  baseURL: https://myserver.jfrog.io/curation/api
  humanURL: https://jfrog.com/curation/
  tags:
  - Curation
  - Open Source
  - Policy Management
  - Security
  - Software Supply Chain
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-rest-apis/jfrog-curation-rest-apis
  - type: OpenAPI
    url: openapi/jfrog-curation-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- name: JFrog Mission Control REST API
  description: API for centralized management and monitoring of multiple JFrog Platform instances, including Artifactory servers, configurations, and cross-instance operations.
  baseURL: https://myserver.jfrog.io/mc/api
  humanURL: https://jfrog.com/platform/
  tags:
  - Administration
  - Mission Control
  - Monitoring
  - Multi-Instance Management
  - Operations
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-rest-apis/mission-control-rest-apis
  - type: OpenAPI
    url: openapi/jfrog-mission-control-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- name: JFrog Release Lifecycle Management REST API
  description: API for managing release bundles, promotion workflows, and evidence collection throughout the software release lifecycle from development to production.
  baseURL: https://myserver.jfrog.io/lifecycle/api
  humanURL: https://jfrog.com/rlm/
  tags:
  - Evidence
  - Lifecycle
  - Promotion
  - Release Bundles
  - Release Management
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-rest-apis/release-lifecycle-management
  - type: OpenAPI
    url: openapi/jfrog-release-lifecycle-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- name: JFrog Workers REST API
  description: API for creating and managing custom serverless workers that extend JFrog Platform functionality through synchronized hooks and automation in a secure, isolated execution environment.
  baseURL: https://myserver.jfrog.io/worker/api
  humanURL: https://jfrog.com/platform/workers/
  tags:
  - Automation
  - Extensibility
  - Plugins
  - Serverless
  - Workers
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-rest-apis/workers-rest-apis
  - type: OpenAPI
    url: openapi/jfrog-workers-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- name: JFrog ML REST API
  description: API for managing machine learning models, experiments, and deployments including model registry, versioning, and serving capabilities.
  baseURL: https://myserver.jfrog.io/ml/api
  humanURL: https://jfrog.com/jfrog-ml/
  tags:
  - AI
  - Machine Learning
  - MLOps
  - Model Management
  - Model Registry
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-ml-documentation/jfrog-ml-rest-api
  - type: OpenAPI
    url: openapi/jfrog-ml-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- name: JFrog Connect REST API
  description: API for managing IoT and edge devices, deploying over-the-air software updates, and monitoring device fleets at scale.
  baseURL: https://api.connect.jfrog.io/v2
  humanURL: https://jfrog.com/connect/
  tags:
  - Device Management
  - Edge Computing
  - Fleet Management
  - IoT
  - OTA Updates
  properties:
  - type: Documentation
    url: https://docs.connect.jfrog.io/rest-api-v2/connect-api-reference
  - type: OpenAPI
    url: openapi/jfrog-connect-openapi.yml
  - type: Authentication
    url: https://docs.connect.jfrog.io/developers
- name: JFrog Catalog REST API
  description: API for querying and managing package metadata, searching for packages and CVEs, and managing custom labels for software components through a GraphQL-based interface.
  baseURL: https://myserver.jfrog.io/catalog/api/v1
  humanURL: https://jfrog.com/platform/
  tags:
  - Catalog
  - CVE Search
  - Package Metadata
  - Security
  - Software Supply Chain
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-security-user-guide/products/catalog
  - type: OpenAPI
    url: openapi/jfrog-catalog-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- name: JFrog Evidence REST API
  description: API for creating and attaching cryptographically signed evidence to artifacts, builds, packages, and release bundles, enabling supply chain verification and compliance attestation throughout the software delivery lifecycle.
  baseURL: https://myserver.jfrog.io/evidence/api
  humanURL: https://jfrog.com/platform/
  tags:
  - Attestation
  - Compliance
  - Evidence
  - Software Supply Chain
  - Supply Chain Security
  properties:
  - type: Documentation
    url: https://jfrog.com/help/r/jfrog-artifactory-documentation/create-evidence-using-rest-apis
  - type: OpenAPI
    url: openapi/jfrog-evidence-openapi.yml
  - type: Authentication
    url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
name: JFrog
tags:
- Artifactory
- CI/CD
- Container Registry
- DevOps
- MLOps
- Package Management
- Security
- Software Supply Chain
type: Contract
image: https://jfrog.com/brand/jfrog-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: JFrog provides universal DevOps solutions for software supply chain automation and security, offering a unified platform for managing binaries, securing the software supply chain, and automating DevOps workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


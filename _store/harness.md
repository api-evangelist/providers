---
aid: harness
url: https://raw.githubusercontent.com/api-evangelist/harness/refs/heads/main/apis.yml
apis:
- aid: harness:harness
  name: Harness
  tags:
  - DevOps
  - GitOps
  - Internal Developer Portal
  - Lifecycle
  - Software Delivery
  humanURL: ' https://www.harness.io/'
  properties:
  - url: ' https://www.harness.io/'
    type: Documentation
  - url: https://apidocs.harness.io
    type: Portal
  - url: https://developer.harness.io/docs/platform/automation/api/api-quickstart/
    type: Getting Started
  - url: https://developer.harness.io/docs/platform/automation/api/add-and-manage-api-keys/
    type: Authentication
  - url: https://developer.harness.io/docs/platform/automation/api/api-permissions-reference/
    type: Reference
  description: Harness delivers intelligent AI automation, so your team ships code faster, safer, and smarter. The Harness API is a RESTful API that uses standard HTTP verbs and allows you to send requests in JSON, YAML, or form-data format. API authentication uses API keys sent in the x-api-key header.
- aid: harness:harness-platform-api
  name: Harness Platform API
  tags:
  - Access Management
  - Accounts
  - Administration
  - Organizations
  - Platform
  - Projects
  humanURL: https://apidocs.harness.io
  properties:
  - url: https://apidocs.harness.io
    type: Documentation
  - url: https://developer.harness.io/docs/category/api/
    type: Reference
  - url: https://developer.harness.io/docs/platform/automation/api/api-quickstart/
    type: Getting Started
  description: The Harness Platform API provides access to core platform resources including projects, organizations, connectors, secrets, users, roles, resource groups, service accounts, variables, pipelines, triggers, input sets, approvals, and pipeline execution. It supports account-scoped, organization-scoped, and project-scoped operations across the Harness platform.
- aid: harness:harness-continuous-integration-api
  name: Harness Continuous Integration API
  tags:
  - Builds
  - CI
  - Continuous Integration
  - Pipelines
  humanURL: https://developer.harness.io/docs/continuous-integration
  properties:
  - url: https://developer.harness.io/docs/continuous-integration
    type: Documentation
  - url: https://apidocs.harness.io/pipeline
    type: Reference
  description: The Harness Continuous Integration module helps build faster and be more productive with features including code building, testing, dependency management, artifact uploads, and build monitoring. It supports Harness AI, Test Intelligence, Cache Intelligence, and plugins for custom scripts and third-party integrations.
- aid: harness:harness-continuous-delivery-api
  name: Harness Continuous Delivery and GitOps API
  tags:
  - CD
  - Continuous Delivery
  - Deployments
  - GitOps
  - Pipelines
  humanURL: https://developer.harness.io/docs/continuous-delivery
  properties:
  - url: https://developer.harness.io/docs/continuous-delivery
    type: Documentation
  - url: https://apidocs.harness.io/pipeline
    type: Reference
  - url: https://apidocs.harness.io/pipeline-execute
    type: Reference
  description: The Harness Continuous Delivery and GitOps module automates all of the steps necessary to get changes into production. It provides APIs for performing CRUD operations on pipelines, executing pipelines, managing input sets, triggers, and approvals, and supports multi-cloud, multi-region deployments.
- aid: harness:harness-feature-management-api
  name: Harness Feature Management and Experimentation API
  tags:
  - A/B Testing
  - Experimentation
  - Feature Flags
  - Feature Management
  humanURL: https://developer.harness.io/docs/feature-management-experimentation
  properties:
  - url: https://developer.harness.io/docs/feature-management-experimentation
    type: Documentation
  - url: https://apidocs.harness.io/feature-flags
    type: Reference
  - url: https://apidocs.harness.io/targets
    type: Reference
  - url: https://apidocs.harness.io/target-groups
    type: Reference
  description: The Harness Feature Management and Experimentation module provides APIs to create and manage feature flags, targets, target groups, and tags. It enables feature release management, performance monitoring, and experimentation for data-driven development with server-side SDKs available in Go, Java, .NET, and other languages.
- aid: harness:harness-cloud-cost-management-api
  name: Harness Cloud Cost Management API
  tags:
  - CCM
  - Cloud Cost Management
  - Cost Optimization
  - FinOps
  humanURL: https://developer.harness.io/docs/cloud-cost-management
  properties:
  - url: https://developer.harness.io/docs/cloud-cost-management
    type: Documentation
  - url: https://apidocs.harness.io/costs
    type: Reference
  description: The Harness Cloud Cost Management module is a cloud cost management solution that empowers FinOps, infrastructure, and engineering teams with intelligent tools to optimize cloud spend. It provides APIs for cost recommendations, AutoStopping rules, commitment orchestration, cost categories, anomaly detection, asset governance, cluster orchestration, perspectives, budgets, and BI dashboards.
- aid: harness:harness-chaos-engineering-api
  name: Harness Chaos Engineering API
  tags:
  - Chaos Engineering
  - Reliability
  - Resilience Testing
  humanURL: https://developer.harness.io/docs/resilience-testing
  properties:
  - url: https://developer.harness.io/docs/resilience-testing
    type: Documentation
  - url: https://apidocs.harness.io/chaos.html
    type: Reference
  description: The Harness Resilience Testing module provides chaos engineering, load testing, and disaster recovery testing capabilities to help organizations build confidence in system reliability. It provides APIs for managing chaos experiments, probes, actions, faults, and resilience scoring to proactively validate system resilience.
- aid: harness:harness-security-testing-orchestration-api
  name: Harness Security Testing Orchestration API
  tags:
  - DevSecOps
  - Security Testing
  - STO
  - Vulnerability Scanning
  humanURL: https://developer.harness.io/docs/security-testing-orchestration
  properties:
  - url: https://developer.harness.io/docs/security-testing-orchestration
    type: Documentation
  description: The Harness Security Testing Orchestration module enables pipelines to detect security vulnerabilities automatically with over 40 scanner integrations. It provides APIs for running scans, viewing results, and enforcing security policies across the software delivery lifecycle.
- aid: harness:harness-internal-developer-portal-api
  name: Harness Internal Developer Portal API
  tags:
  - Backstage
  - Developer Experience
  - IDP
  - Internal Developer Portal
  - Software Catalog
  humanURL: https://developer.harness.io/docs/internal-developer-portal
  properties:
  - url: https://developer.harness.io/docs/internal-developer-portal
    type: Documentation
  - url: https://developer.harness.io/docs/internal-developer-portal/api-refernces/overview/
    type: Reference
  - url: https://developer.harness.io/docs/internal-developer-portal/api-refernces/public-api/
    type: Reference
  description: The Harness Internal Developer Portal, powered by Backstage, helps developers create, manage, and explore software while adhering to organizational best practices. It provides two types of APIs - the Backstage API for programmatically adding and removing entities in the catalog, and the Platform API for native Harness IDP operations including software catalog management, self-service workflows, and scorecards.
- aid: harness:harness-code-repository-api
  name: Harness Code Repository API
  tags:
  - Code Repository
  - Git
  - Source Control
  humanURL: https://developer.harness.io/docs/code-repository
  properties:
  - url: https://developer.harness.io/docs/code-repository
    type: Documentation
  - url: https://apidocs.harness.io/repository/importrepository
    type: Reference
  description: The Harness Code Repository module provides source control management capabilities including repositories, collaboration tools, pull requests, and pipeline integration. It provides APIs for managing repositories, importing code, and integrating source control with the Harness platform.
- aid: harness:harness-service-reliability-management-api
  name: Harness Service Reliability Management API
  tags:
  - Monitoring
  - Service Reliability
  - SLO
  - SRM
  humanURL: https://developer.harness.io/docs/service-reliability-management
  properties:
  - url: https://developer.harness.io/docs/service-reliability-management
    type: Documentation
  - url: https://apidocs.harness.io/services
    type: Reference
  description: The Harness Service Reliability Management module helps engineering and DevOps teams balance feature velocity and bug fixes with the stability and reliability needs of a production environment. It provides APIs for managing service level objectives, monitored services, and service dashboards.
- aid: harness:harness-infrastructure-as-code-management-api
  name: Harness Infrastructure as Code Management API
  tags:
  - IaCM
  - Infrastructure as Code
  - Provisioning
  - Terraform
  humanURL: https://developer.harness.io/docs/infrastructure-as-code-management
  properties:
  - url: https://developer.harness.io/docs/infrastructure-as-code-management
    type: Documentation
  description: The Harness Infrastructure as Code Management module allows you to define, deploy, and manage infrastructure across environments, ensuring compliance and control. It integrates with Terraform and other IaC tools to provide infrastructure provisioning through the Harness platform.
- aid: harness:harness-supply-chain-security-api
  name: Harness Supply Chain Security API
  tags:
  - Compliance
  - SBOM
  - Software Supply Chain
  - Supply Chain Security
  humanURL: https://developer.harness.io/docs/software-supply-chain-assurance
  properties:
  - url: https://developer.harness.io/docs/software-supply-chain-assurance
    type: Documentation
  description: The Harness Supply Chain Security module addresses the challenges of securing your software supply chain. It provides capabilities for software bill of materials generation, artifact integrity verification, and policy enforcement to ensure compliance across the delivery pipeline.
- aid: harness:harness-software-engineering-insights-api
  name: Harness Software Engineering Insights API
  tags:
  - Analytics
  - Engineering Productivity
  - SEI
  - Software Engineering Insights
  humanURL: https://developer.harness.io/docs/software-engineering-insights
  properties:
  - url: https://developer.harness.io/docs/software-engineering-insights
    type: Documentation
  - url: https://developer.harness.io/docs/software-engineering-insights/propelo-sei/sei-administration/sei-api-reference/sei-api-guide/
    type: Reference
  description: The Harness Software Engineering Insights module enables engineering leaders to make data-driven decisions that improve engineering productivity, efficiency, alignment, planning, and execution. It provides APIs for accessing engineering metrics and analytics data.
- aid: harness:harness-cloud-development-environments-api
  name: Harness Cloud Development Environments API
  tags:
  - CDE
  - Cloud Development Environments
  - Developer Tools
  - Gitspaces
  humanURL: https://developer.harness.io/docs/cloud-development-environments
  properties:
  - url: https://developer.harness.io/docs/cloud-development-environments
    type: Documentation
  description: The Harness Cloud Development Environments module, also known as Gitspaces, provides on-demand remote development environments that can be instantly spun up with a click. These environments come pre-configured with dependencies, tools, libraries, and IDE options to provide a ready-to-use setup for developers.
name: Harness
tags:
- DevOps
- GitOps
- Internal Developer Portal
- Lifecycle
- Software Delivery
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-07'
position: Consuming
description: Harness is an AI-powered software delivery platform that automates and accelerates the entire software development lifecycle from code to production. The platform provides intelligent automation across DevOps, testing and resilience, security and compliance, and cost optimization, helping engineering teams ship code faster, safer, and smarter as they scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


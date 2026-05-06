---
aid: harness
name: Harness
description: Harness is an AI-powered software delivery platform that automates and accelerates the entire software development lifecycle from code to production. The platform provides intelligent automation across DevOps, testing and resilience, security and compliance, and cost optimization, helping engineering teams ship code faster, safer, and smarter as they scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/harness/refs/heads/main/apis.yml
access: 3rd-Party
position: Consuming
created: '2026-01-02'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - DevOps
  - GitOps
  - Internal Developer Portal
  - Lifecycle
  - Software Delivery
segments:
  - FinOps
apis:
  - aid: harness:platform-api
    name: Harness Platform API
    description: The Harness Platform API provides access to core platform resources including projects, organizations, connectors, secrets, users, roles, resource groups, service accounts, variables, pipelines, triggers, input sets, approvals, and pipeline execution.
    humanURL: https://apidocs.harness.io
    tags:
      - Access Management
      - Accounts
      - Administration
      - Organizations
      - Platform
      - Projects
    properties:
      - type: Documentation
        url: https://apidocs.harness.io
      - type: APIReference
        url: https://developer.harness.io/docs/category/api/
      - type: GettingStarted
        url: https://developer.harness.io/docs/platform/automation/api/api-quickstart/
  - aid: harness:ci-api
    name: Harness Continuous Integration API
    description: The Harness CI module helps build faster with features including code building, testing, dependency management, artifact uploads, and build monitoring with AI-powered Test Intelligence.
    humanURL: https://developer.harness.io/docs/continuous-integration
    tags:
      - Builds
      - CI
      - Continuous Integration
      - Pipelines
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/continuous-integration
      - type: APIReference
        url: https://apidocs.harness.io/pipeline
  - aid: harness:cd-api
    name: Harness Continuous Delivery and GitOps API
    description: The Harness CD and GitOps module automates all steps necessary to get changes into production with APIs for pipelines, execution, input sets, triggers, and approvals supporting multi-cloud deployments.
    humanURL: https://developer.harness.io/docs/continuous-delivery
    tags:
      - CD
      - Continuous Delivery
      - Deployments
      - GitOps
      - Pipelines
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/continuous-delivery
      - type: APIReference
        url: https://apidocs.harness.io/pipeline
  - aid: harness:feature-flags-api
    name: Harness Feature Management and Experimentation API
    description: APIs to create and manage feature flags, targets, target groups, and tags for feature release management, performance monitoring, and A/B testing.
    humanURL: https://developer.harness.io/docs/feature-management-experimentation
    tags:
      - A/B Testing
      - Experimentation
      - Feature Flags
      - Feature Management
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/feature-management-experimentation
      - type: APIReference
        url: https://apidocs.harness.io/feature-flags
  - aid: harness:ccm-api
    name: Harness Cloud Cost Management API
    description: Cloud cost management APIs for cost recommendations, AutoStopping rules, commitment orchestration, cost categories, anomaly detection, asset governance, and BI dashboards.
    humanURL: https://developer.harness.io/docs/cloud-cost-management
    tags:
      - CCM
      - Cloud Cost Management
      - Cost Optimization
      - FinOps
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/cloud-cost-management
      - type: APIReference
        url: https://apidocs.harness.io/costs
  - aid: harness:chaos-api
    name: Harness Chaos Engineering API
    description: APIs for chaos engineering, load testing, and disaster recovery testing including chaos experiments, probes, actions, faults, and resilience scoring.
    humanURL: https://developer.harness.io/docs/resilience-testing
    tags:
      - Chaos Engineering
      - Reliability
      - Resilience Testing
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/resilience-testing
      - type: APIReference
        url: https://apidocs.harness.io/chaos.html
  - aid: harness:sto-api
    name: Harness Security Testing Orchestration API
    description: APIs for security vulnerability detection with over 40 scanner integrations for running scans, viewing results, and enforcing security policies across the software delivery lifecycle.
    humanURL: https://developer.harness.io/docs/security-testing-orchestration
    tags:
      - DevSecOps
      - Security Testing
      - STO
      - Vulnerability Scanning
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/security-testing-orchestration
  - aid: harness:idp-api
    name: Harness Internal Developer Portal API
    description: Backstage-powered Internal Developer Portal APIs for software catalog management, self-service workflows, scorecards, and developer experience.
    humanURL: https://developer.harness.io/docs/internal-developer-portal
    tags:
      - Backstage
      - Developer Experience
      - IDP
      - Software Catalog
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/internal-developer-portal
      - type: APIReference
        url: https://developer.harness.io/docs/internal-developer-portal/api-refernces/overview/
  - aid: harness:code-repo-api
    name: Harness Code Repository API
    description: Source control management APIs for repositories, collaboration tools, pull requests, and pipeline integration.
    humanURL: https://developer.harness.io/docs/code-repository
    tags:
      - Code Repository
      - Git
      - Source Control
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/code-repository
  - aid: harness:srm-api
    name: Harness Service Reliability Management API
    description: APIs for managing service level objectives, monitored services, and service dashboards for balancing feature velocity with reliability.
    humanURL: https://developer.harness.io/docs/service-reliability-management
    tags:
      - Monitoring
      - Service Reliability
      - SLO
      - SRM
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/service-reliability-management
  - aid: harness:iacm-api
    name: Harness Infrastructure as Code Management API
    description: APIs for defining, deploying, and managing infrastructure across environments with Terraform and IaC tool integration.
    humanURL: https://developer.harness.io/docs/infrastructure-as-code-management
    tags:
      - IaCM
      - Infrastructure as Code
      - Provisioning
      - Terraform
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/infrastructure-as-code-management
  - aid: harness:ssca-api
    name: Harness Supply Chain Security API
    description: APIs for SBOM generation, artifact integrity verification, and policy enforcement for software supply chain security and compliance.
    humanURL: https://developer.harness.io/docs/software-supply-chain-assurance
    tags:
      - Compliance
      - SBOM
      - Software Supply Chain
      - Supply Chain Security
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/software-supply-chain-assurance
  - aid: harness:sei-api
    name: Harness Software Engineering Insights API
    description: APIs for accessing engineering metrics and analytics data to improve engineering productivity, efficiency, and alignment.
    humanURL: https://developer.harness.io/docs/software-engineering-insights
    tags:
      - Analytics
      - Engineering Productivity
      - SEI
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/software-engineering-insights
      - type: APIReference
        url: https://developer.harness.io/docs/software-engineering-insights/propelo-sei/sei-administration/sei-api-reference/sei-api-guide/
common:
  - type: Portal
    url: https://developer.harness.io/docs/
  - type: Documentation
    url: https://apidocs.harness.io
  - type: GettingStarted
    url: https://developer.harness.io/docs/platform/automation/api/api-quickstart/
  - type: Authentication
    url: https://developer.harness.io/docs/platform/automation/api/add-and-manage-api-keys/
  - type: Pricing
    url: https://www.harness.io/pricing
  - type: SignUp
    url: https://app.harness.io/auth/
  - type: Blog
    url: https://www.harness.io/blog
  - type: Support
    url: https://www.harness.io/support
  - type: StatusPage
    url: https://status.harness.io
  - type: ChangeLog
    url: https://developer.harness.io/release-notes/
  - type: TermsOfService
    url: https://www.harness.io/legal/website-terms-of-use
  - type: PrivacyPolicy
    url: https://www.harness.io/legal/privacy
  - type: GitHubOrganization
    url: https://github.com/harness
  - type: Training
    url: https://developer.harness.io/university/
  - type: Security
    url: https://www.harness.io/security
  - type: Features
    data:
      - name: AI-Powered Automation
        description: Intelligent automation with Harness AI for test intelligence, deployment verification, and cost optimization.
      - name: Pipeline Orchestration
        description: Visual pipeline builder with conditional logic, parallel execution, and approval gates.
      - name: GitOps Deployments
        description: Declarative GitOps deployments with Argo CD integration for Kubernetes workloads.
      - name: Feature Flag Management
        description: Progressive feature rollouts with targeting, experimentation, and A/B testing capabilities.
      - name: Cloud Cost Optimization
        description: FinOps capabilities including AutoStopping, commitment orchestration, and cost anomaly detection.
      - name: Chaos Engineering
        description: Resilience testing with chaos experiments, load testing, and disaster recovery validation.
      - name: Security Testing Orchestration
        description: Automated security scanning with 40+ scanner integrations and policy enforcement.
      - name: Internal Developer Portal
        description: Backstage-powered developer portal for software catalog, self-service workflows, and scorecards.
  - type: UseCases
    data:
      - name: CI/CD Pipeline Automation
        description: Automate build, test, and deploy workflows across multi-cloud and hybrid environments.
      - name: Progressive Feature Delivery
        description: Roll out features progressively with feature flags, canary deployments, and blue-green strategies.
      - name: Cloud Cost Management
        description: Optimize cloud spend with automated cost recommendations, idle resource detection, and budget alerts.
      - name: Security Compliance
        description: Enforce security policies with automated scanning, SBOM generation, and supply chain verification.
      - name: Platform Engineering
        description: Build internal developer platforms with self-service workflows, templates, and software catalogs.
      - name: SRE and Reliability
        description: Manage SLOs, monitor service health, and validate resilience with chaos engineering.
  - type: Integrations
    data:
      - name: GitHub
        description: Source code management, GitHub Actions, and GitHub App integration for CI/CD workflows.
      - name: Kubernetes
        description: Native Kubernetes deployment support with Helm, Kustomize, and GitOps.
      - name: AWS
        description: Multi-service AWS integration including ECS, EKS, Lambda, S3, and CloudFormation.
      - name: Azure
        description: Azure DevOps, AKS, Azure Functions, and Azure Resource Manager integration.
      - name: GCP
        description: Google Cloud integration with GKE, Cloud Run, Cloud Functions, and Cloud Build.
      - name: Terraform
        description: Infrastructure as Code management with Terraform plan, apply, and state management.
      - name: Jira
        description: Issue tracking integration for deployment approvals, change management, and traceability.
      - name: Slack
        description: Notifications and approval workflows within Slack channels.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---

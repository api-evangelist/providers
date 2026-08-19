---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Harness Agentic Access
  operation_count: 4
  slug: harness-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 17
apis:
- description: The Harness Platform API provides access to core platform resources including projects, organizations, connectors, secrets, users, roles, resource groups, service accounts, variables, pipelines, trigg
  name: Harness Platform API
  slug: platform-api
- description: The Harness CI module helps build faster with features including code building, testing, dependency management, artifact uploads, and build monitoring with AI-powered Test Intelligence.
  name: Harness Continuous Integration API
  slug: ci-api
- description: The Harness CD and GitOps module automates all steps necessary to get changes into production with APIs for pipelines, execution, input sets, triggers, and approvals supporting multi-cloud deployments
  name: Harness Continuous Delivery and GitOps API
  slug: cd-api
- description: APIs to create and manage feature flags, targets, target groups, and tags for feature release management, performance monitoring, and A/B testing.
  name: Harness Feature Management and Experimentation API
  slug: feature-flags-api
- description: Cloud cost management APIs for cost recommendations, AutoStopping rules, commitment orchestration, cost categories, anomaly detection, asset governance, and BI dashboards.
  name: Harness Cloud Cost Management API
  slug: ccm-api
- description: APIs for chaos engineering, load testing, and disaster recovery testing including chaos experiments, probes, actions, faults, and resilience scoring.
  name: Harness Chaos Engineering API
  slug: chaos-api
- description: APIs for security vulnerability detection with over 40 scanner integrations for running scans, viewing results, and enforcing security policies across the software delivery lifecycle.
  name: Harness Security Testing Orchestration API
  slug: sto-api
- description: Backstage-powered Internal Developer Portal APIs for software catalog management, self-service workflows, scorecards, and developer experience.
  name: Harness Internal Developer Portal API
  slug: idp-api
- description: Source control management APIs for repositories, collaboration tools, pull requests, and pipeline integration.
  name: Harness Code Repository API
  slug: code-repo-api
- description: APIs for managing service level objectives, monitored services, and service dashboards for balancing feature velocity with reliability.
  name: Harness Service Reliability Management API
  slug: srm-api
- description: APIs for defining, deploying, and managing infrastructure across environments with Terraform and IaC tool integration.
  name: Harness Infrastructure as Code Management API
  slug: iacm-api
- description: APIs for SBOM generation, artifact integrity verification, and policy enforcement for software supply chain security and compliance.
  name: Harness Supply Chain Security API
  slug: ssca-api
- description: APIs for accessing engineering metrics and analytics data to improve engineering productivity, efficiency, and alignment.
  name: Harness Software Engineering Insights API
  slug: sei-api
- description: Manage organizations
  name: Harness Organizations API
  slug: harness-organizations-api
- description: Execute pipelines
  name: Harness Pipeline Execution API
  slug: harness-pipeline-execution-api
- description: Manage pipelines
  name: Harness Pipelines API
  slug: harness-pipelines-api
- description: Manage projects
  name: Harness Projects API
  slug: harness-projects-api
artifact_total: 82
collections:
- collection_type: postman
  name: Harness Platform Organizations API
  slug: postman-harness-organizations-api
- collection_type: postman
  name: Harness Platform Organizations Pipeline Execution API
  slug: postman-harness-pipeline-execution-api
- collection_type: postman
  name: Harness Platform Organizations Pipelines API
  slug: postman-harness-pipelines-api
- collection_type: postman
  name: Harness Platform Organizations Projects API
  slug: postman-harness-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harness Platform Organizations API
  slug: open-harness-organizations-api
- collection_type: open
  name: Harness Platform Organizations Pipeline Execution API
  slug: open-harness-pipeline-execution-api
- collection_type: open
  name: Harness Platform Organizations Pipelines API
  slug: open-harness-pipelines-api
- collection_type: open
  name: Harness Platform Organizations Projects API
  slug: open-harness-projects-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/harness/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harness-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/harness-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harness-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harness-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harnessinc
- group: start
  title: ''
  type: Portal
  url: https://developer.harness.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.harness.io
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.harness.io/docs/platform/automation/api/api-quickstart/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.harness.io/docs/platform/automation/api/add-and-manage-api-keys/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.harness.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.harness.io/auth/
- group: company
  title: ''
  type: Blog
  url: https://www.harness.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.harness.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harness.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.harness.io/release-notes/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harness.io/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harness.io/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harness
- group: learn
  title: ''
  type: Training
  url: https://developer.harness.io/university/
- group: auth
  title: ''
  type: Security
  url: https://www.harness.io/security
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/harness/mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/harness/harness-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://apidocs.harness.io/llms.txt
created: '2026-01-02'
description: Harness is an AI-powered software delivery platform that automates and accelerates the entire software development lifecycle from code to production. The platform provides intelligent automation across DevOps, testing and resilience, security and compliance, and cost optimization, helping engineering teams ship code faster, safer, and smarter as they scale.
features:
- description: Intelligent automation with Harness AI for test intelligence, deployment verification, and cost optimization.
  name: AI-Powered Automation
- description: Visual pipeline builder with conditional logic, parallel execution, and approval gates.
  name: Pipeline Orchestration
- description: Declarative GitOps deployments with Argo CD integration for Kubernetes workloads.
  name: GitOps Deployments
- description: Progressive feature rollouts with targeting, experimentation, and A/B testing capabilities.
  name: Feature Flag Management
- description: FinOps capabilities including AutoStopping, commitment orchestration, and cost anomaly detection.
  name: Cloud Cost Optimization
- description: Resilience testing with chaos experiments, load testing, and disaster recovery validation.
  name: Chaos Engineering
- description: Automated security scanning with 40+ scanner integrations and policy enforcement.
  name: Security Testing Orchestration
- description: Backstage-powered developer portal for software catalog, self-service workflows, and scorecards.
  name: Internal Developer Portal
finops:
- name: Harness Finops
  service_category: Developer Tools / DevOps Platform
  slug: harness-finops
image: /assets/icons/harness.png
integrations:
- description: Source code management, GitHub Actions, and GitHub App integration for CI/CD workflows.
  name: GitHub
- description: Native Kubernetes deployment support with Helm, Kustomize, and GitOps.
  name: Kubernetes
- description: Multi-service AWS integration including ECS, EKS, Lambda, S3, and CloudFormation.
  name: AWS
- description: Azure DevOps, AKS, Azure Functions, and Azure Resource Manager integration.
  name: Azure
- description: Google Cloud integration with GKE, Cloud Run, Cloud Functions, and Cloud Build.
  name: GCP
- description: Infrastructure as Code management with Terraform plan, apply, and state management.
  name: Terraform
- description: Issue tracking integration for deployment approvals, change management, and traceability.
  name: Jira
- description: Notifications and approval workflows within Slack channels.
  name: Slack
jsonld:
- class_count: 4
  name: Harness Context
  property_count: 7
  slug: harness-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Harness
nav: Providers
network: true
overview: 'Harness publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Organizations API, Pipeline Execution API, Pipelines API, and 1 more. Tagged areas include DevOps, GitOps, Internal Developer Portal, Lifecycle, and Software Delivery.


  The Harness catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Harness'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Harness Plans Pricing
  plan_count: 3
  slug: harness-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Harness Rate Limits
  slug: harness-rate-limits
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Harness API Rules
  rule_count: 16
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 10
  slug: harness-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: -2.9
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 13.6
    contract_quality: 17.3
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 13.6
    operational_transparency: 52.6
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harness/refs/heads/main/screenshots/harness-2026-06-20T182519.png
security:
- kind: authentication
  name: Harness Authentication
  slug: harness-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Harness Domain Security
  slug: harness-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Harness Trust Center
  slug: harness-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, CSA STAR
skill_count: 44
skills:
- name: ai-operations
  slug: ai-operations
- name: analyze-costs
  slug: analyze-costs
- name: audit-report
  slug: audit-report
- name: chaos-experiment
  slug: chaos-experiment
- name: configure-container-scan
  slug: configure-container-scan
- name: configure-repo-scan
  slug: configure-repo-scan
- name: configure-secret-scan
  slug: configure-secret-scan
- name: create-agent-template
  slug: create-agent-template
- name: create-agent
  slug: create-agent
- name: create-connector
  slug: create-connector
- name: create-environment
  slug: create-environment
- name: create-infrastructure
  slug: create-infrastructure
- name: create-pipeline-v1
  slug: create-pipeline-v1
- name: create-pipeline
  slug: create-pipeline
- name: create-policy
  slug: create-policy
- name: create-secret
  slug: create-secret
- name: create-service
  slug: create-service
- name: create-template
  slug: create-template
- name: create-trigger
  slug: create-trigger
- name: debug-pipeline
  slug: debug-pipeline
- name: deployment-readiness
  slug: deployment-readiness
- name: dora-metrics
  slug: dora-metrics
- name: gitops-status
  slug: gitops-status
- name: incident-response
  slug: incident-response
slug: harness
tags:
- DevOps
- GitOps
- Internal Developer Portal
- Lifecycle
- Software Delivery
use_cases:
- description: Automate build, test, and deploy workflows across multi-cloud and hybrid environments.
  name: CI/CD Pipeline Automation
- description: Roll out features progressively with feature flags, canary deployments, and blue-green strategies.
  name: Progressive Feature Delivery
- description: Optimize cloud spend with automated cost recommendations, idle resource detection, and budget alerts.
  name: Cloud Cost Management
- description: Enforce security policies with automated scanning, SBOM generation, and supply chain verification.
  name: Security Compliance
- description: Build internal developer platforms with self-service workflows, templates, and software catalogs.
  name: Platform Engineering
- description: Manage SLOs, monitor service health, and validate resilience with chaos engineering.
  name: SRE and Reliability
website: https://developer.harness.io/docs/
---

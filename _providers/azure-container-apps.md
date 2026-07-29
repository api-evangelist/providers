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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Azure Container Apps Agentic Access
  operation_count: 22
  slug: azure-container-apps-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 5
apis:
- description: Manage container app authentication
  name: Azure Container Apps Authentication API
  slug: azure-container-apps-authentication-api
- description: Manage container apps
  name: Azure Container Apps Container Apps API
  slug: azure-container-apps-container-apps-api
- description: Manage container app jobs
  name: Azure Container Apps Jobs API
  slug: azure-container-apps-jobs-api
- description: Manage container app environments
  name: Azure Container Apps Managed Environments API
  slug: azure-container-apps-managed-environments-api
- description: Manage container app revisions
  name: Azure Container Apps Revisions API
  slug: azure-container-apps-revisions-api
arazzos:
- description: Find the most recent revision of an app, inspect it, and activate it if it is inactive.
  name: Azure Container Apps Activate Latest Revision
  slug: azure-container-apps-activate-latest-revision-workflow
- description: Read an app, then enumerate its secrets and authentication configurations for a security review.
  name: Azure Container Apps Audit App Security
  slug: azure-container-apps-audit-app-security-workflow
- description: Delete a container app and confirm it no longer appears in the resource group listing.
  name: Azure Container Apps Decommission App
  slug: azure-container-apps-decommission-app-workflow
- description: Create a managed environment, wait for it, then create a container app inside it and wait for that too.
  name: Azure Container Apps Deploy App Into New Environment
  slug: azure-container-apps-deploy-app-into-new-environment-workflow
- description: Enable the Dapr sidecar on a container app, wait for the new revision to provision, then list revisions.
  name: Azure Container Apps Enable Dapr Sidecar
  slug: azure-container-apps-enable-dapr-sidecar-workflow
- description: Create a manually triggered job, wait until it is provisioned, then start an execution.
  name: Azure Container Apps Provision and Run Job
  slug: azure-container-apps-provision-and-run-job-workflow
- description: Verify the target environment is ready, create a container app, and poll until it is provisioned.
  name: Azure Container Apps Provision Container App
  slug: azure-container-apps-provision-container-app-workflow
- description: Create a managed environment and poll its provisioning state until it reaches Succeeded.
  name: Azure Container Apps Provision Managed Environment
  slug: azure-container-apps-provision-managed-environment-workflow
- description: Restart the active revision of an app and poll its revision replicas until it is running again.
  name: Azure Container Apps Restart Active Revision
  slug: azure-container-apps-restart-active-revision-workflow
- description: Write a new secret value to an app, wait for provisioning, then list secrets to confirm it is present.
  name: Azure Container Apps Rotate and Verify Secrets
  slug: azure-container-apps-rotate-and-verify-secrets-workflow
- description: Confirm a job is provisioned and manually triggerable, then start an execution.
  name: Azure Container Apps Run Existing Job
  slug: azure-container-apps-run-existing-job-workflow
- description: List an app's revisions, shift ingress traffic to a chosen revision, then wait for the change to apply.
  name: Azure Container Apps Shift Revision Traffic
  slug: azure-container-apps-shift-revision-traffic-workflow
- description: Roll out a new image to a container app, wait for provisioning, then list the resulting revisions.
  name: Azure Container Apps Update App and List Revisions
  slug: azure-container-apps-update-app-and-list-revisions-workflow
artifact_total: 91
collections:
- collection_type: postman
  name: Azure Container Apps Authentication API
  slug: postman-azure-container-apps-authentication-api
- collection_type: postman
  name: Azure Authentication Container Apps API
  slug: postman-azure-container-apps-container-apps-api
- collection_type: postman
  name: Azure Container Apps Authentication Jobs API
  slug: postman-azure-container-apps-jobs-api
- collection_type: postman
  name: Azure Container Apps Authentication Managed Environments API
  slug: postman-azure-container-apps-managed-environments-api
- collection_type: postman
  name: Azure Container Apps Authentication Revisions API
  slug: postman-azure-container-apps-revisions-api
- collection_type: open
  name: Azure Container Apps API
  slug: open-azure-container-apps
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-container-apps/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-container-apps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-container-apps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-container-apps-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-container-apps-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-activate-latest-revision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-audit-app-security-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-decommission-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-deploy-app-into-new-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-enable-dapr-sidecar-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-provision-and-run-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-provision-container-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-provision-managed-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-restart-active-revision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-rotate-and-verify-secrets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-run-existing-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-shift-revision-traffic-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-container-apps-update-app-and-list-revisions-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/container-apps/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/container-apps/get-started
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/azure-container-apps
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/blog/appsonazureblog/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/container-apps/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/azure/container-apps/faq
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/rules/azure-container-apps-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/vocabulary/azure-container-apps-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/json-ld/azure-container-apps-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-26'
description: Azure Container Apps is a serverless container service for running microservices and containerized applications with built-in autoscaling, traffic splitting, and Dapr integration. It enables developers to deploy containers without managing complex infrastructure while supporting event-driven architectures and microservices patterns.
examples:
- key_count: 4
  name: Azure Container Apps Auth Config Example
  slug: azure-container-apps-auth-config-example
- key_count: 6
  name: Azure Container Apps Configuration Example
  slug: azure-container-apps-configuration-example
- key_count: 7
  name: Azure Container Apps Container App Example
  slug: azure-container-apps-container-app-example
- key_count: 2
  name: Azure Container Apps Container App Secret Example
  slug: azure-container-apps-container-app-secret-example
- key_count: 8
  name: Azure Container Apps Container Example
  slug: azure-container-apps-container-example
- key_count: 6
  name: Azure Container Apps Job Example
  slug: azure-container-apps-job-example
- key_count: 4
  name: Azure Container Apps Job Execution Example
  slug: azure-container-apps-job-execution-example
- key_count: 2
  name: Azure Container Apps Job Execution Template Example
  slug: azure-container-apps-job-execution-template-example
- key_count: 6
  name: Azure Container Apps Managed Environment Example
  slug: azure-container-apps-managed-environment-example
- key_count: 4
  name: Azure Container Apps Revision Example
  slug: azure-container-apps-revision-example
- key_count: 4
  name: Azure Container Apps Secret Example
  slug: azure-container-apps-secret-example
- key_count: 7
  name: Azure Container Apps Template Example
  slug: azure-container-apps-template-example
features:
- description: Run containers without managing servers or Kubernetes cluster infrastructure.
  name: Serverless Containers
- description: Automatically scale based on HTTP traffic, event messages, or custom KEDA scalers.
  name: Built-in Autoscaling
- description: Gradually shift traffic between container revisions for canary deployments and A/B testing.
  name: Traffic Splitting
- description: Built-in support for the Dapr distributed application runtime for service discovery and state management.
  name: Dapr Integration
- description: Shared networking and logging infrastructure for groups of container apps.
  name: Managed Environments
- description: Secure, ephemeral code-interpreter and custom container sessions with data-plane REST APIs.
  name: Dynamic Sessions
- description: Schedule and run containerized batch jobs on demand or on a schedule.
  name: Jobs Support
- description: Deploy AI/ML workloads on GPU-enabled container instances.
  name: GPU Support
finops:
- name: Azure Container Apps Finops
  service_category: API
  slug: azure-container-apps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-container-apps.png
integrations:
- description: Share underlying Kubernetes infrastructure while abstracting cluster management complexity.
  name: Azure Kubernetes Service
- description: Pull container images directly from private ACR registries with managed identity.
  name: Azure Container Registry
- description: Trigger container app scaling based on Service Bus queue depth.
  name: Azure Service Bus
- description: Process streaming data from Event Hubs with auto-scaling.
  name: Azure Event Hubs
- description: Deploy container apps directly from GitHub Actions CI/CD workflows.
  name: GitHub Actions
- description: Built-in Dapr runtime support for distributed systems patterns.
  name: Dapr
- description: Native integration with Azure Monitor and Log Analytics for observability.
  name: Azure Monitor
json_schemas:
- name: AuthConfig
  property_count: 4
  slug: azure-container-apps-auth-config
- name: Configuration
  property_count: 6
  slug: azure-container-apps-configuration
- name: ContainerApp
  property_count: 7
  slug: azure-container-apps-container-app
- name: ContainerAppSecret
  property_count: 2
  slug: azure-container-apps-container-app-secret
- name: Container
  property_count: 8
  slug: azure-container-apps-container
- name: JobExecution
  property_count: 4
  slug: azure-container-apps-job-execution
- name: JobExecutionTemplate
  property_count: 2
  slug: azure-container-apps-job-execution-template
- name: Job
  property_count: 6
  slug: azure-container-apps-job
- name: ManagedEnvironment
  property_count: 6
  slug: azure-container-apps-managed-environment
- name: Revision
  property_count: 4
  slug: azure-container-apps-revision
- name: Secret
  property_count: 4
  slug: azure-container-apps-secret
- name: Template
  property_count: 7
  slug: azure-container-apps-template
json_structures:
- name: Azure Container Apps Auth Config Structure
  property_count: 4
  slug: azure-container-apps-auth-config-structure
- name: Azure Container Apps Configuration Structure
  property_count: 6
  slug: azure-container-apps-configuration-structure
- name: Azure Container Apps Container App Secret Structure
  property_count: 2
  slug: azure-container-apps-container-app-secret-structure
- name: Azure Container Apps Container App Structure
  property_count: 7
  slug: azure-container-apps-container-app-structure
- name: Azure Container Apps Container Structure
  property_count: 8
  slug: azure-container-apps-container-structure
- name: Azure Container Apps Job Execution Structure
  property_count: 4
  slug: azure-container-apps-job-execution-structure
- name: Azure Container Apps Job Execution Template Structure
  property_count: 2
  slug: azure-container-apps-job-execution-template-structure
- name: Azure Container Apps Job Structure
  property_count: 6
  slug: azure-container-apps-job-structure
- name: Azure Container Apps Managed Environment Structure
  property_count: 6
  slug: azure-container-apps-managed-environment-structure
- name: Azure Container Apps Revision Structure
  property_count: 4
  slug: azure-container-apps-revision-structure
- name: Azure Container Apps Secret Structure
  property_count: 4
  slug: azure-container-apps-secret-structure
- name: Azure Container Apps Template Structure
  property_count: 7
  slug: azure-container-apps-template-structure
jsonld:
- class_count: 13
  name: Azure Container Apps Context
  property_count: 28
  slug: azure-container-apps-context
layout: provider
modified: '2026-05-19'
name: Azure Container Apps
nav: Providers
network: true
overview: 'Azure Container Apps publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Container Apps API, Jobs API, and 2 more. Tagged areas include Azure, Containers, Dapr, Kubernetes, and Microservices.


  The Azure Container Apps catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Container Apps'' developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Azure Container Apps Plans Pricing
  plan_count: 3
  slug: azure-container-apps-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Azure Container Apps Rate Limits
  slug: azure-container-apps-rate-limits
rules:
- name: Azure Container Apps API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-container-apps-jsonschema-spectral-rules
- name: Azure Container Apps API Rules
  rule_count: 23
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 13
  slug: azure-container-apps-spectral-rules
scopes:
- name: Azure Container Apps Scopes
  scope_count: 1
  slug: azure-container-apps-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 65.7
  delta: -3.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 79.7
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-container-apps/refs/heads/main/screenshots/azure-container-apps-2026-06-20T172841.png
security:
- kind: authentication
  name: Azure Container Apps Authentication
  slug: azure-container-apps-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Container Apps Domain Security
  slug: azure-container-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-container-apps
tags:
- Azure
- Containers
- Dapr
- Kubernetes
- Microservices
- Serverless
use_cases:
- description: Deploy and scale individual microservices independently with built-in service discovery.
  name: Microservices Architecture
- description: Host REST APIs with automatic HTTPS, custom domains, and traffic management.
  name: API Backend Deployment
- description: Process messages from Service Bus, Event Hubs, and storage queues with KEDA-based scaling.
  name: Event-Driven Processing
- description: Run AI inference workloads on GPU-enabled container instances with dynamic sessions.
  name: AI and ML Workloads
- description: Run scheduled and on-demand batch jobs without maintaining dedicated infrastructure.
  name: Background Jobs
- description: Build microservices with Dapr for pub/sub messaging, service invocation, and state management.
  name: Dapr Microservices
website: https://portal.azure.com
---

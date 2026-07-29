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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft Azure Pipelines Agentic Access
  operation_count: 20
  slug: microsoft-azure-pipelines-agentic-access
  summary_line: 20 operations · 6 acting
api_count: 11
apis:
- description: REST API for managing build definitions, queuing builds, and retrieving build results, artifacts, tags, and logs. Supports the full lifecycle of continuous integration builds in Azure DevOps, includin
  name: Azure Pipelines Build REST API
  slug: azure-pipelines-build-rest-api
- description: REST API for managing release definitions, creating and tracking releases, and configuring deployment approvals. Enables programmatic control of the continuous delivery process including defining rele
  name: Azure Pipelines Release REST API
  slug: azure-pipelines-release-rest-api
- description: REST API for managing pipeline approvals and checks on resources such as environments, service connections, agent pools, variable groups, and secure files. Provides the ability to create and modify ch
  name: Azure Pipelines Approvals and Checks REST API
  slug: azure-pipelines-approvals-and-checks-rest-api
- description: Operations for listing and retrieving artifacts produced by pipeline runs including compiled outputs, test results, and published files.
  name: Azure Pipelines Artifacts API
  slug: microsoft-azure-pipelines-artifacts-api
- description: Operations for listing and retrieving build artifacts including compiled binaries, test results, and other published output files.
  name: Azure Pipelines Build Artifacts API
  slug: microsoft-azure-pipelines-build-artifacts-api
- description: Operations for creating, listing, retrieving, and updating build pipeline definitions that specify how builds are executed.
  name: Azure Pipelines Build Definitions API
  slug: microsoft-azure-pipelines-build-definitions-api
- description: Operations for managing tags on builds for categorization, filtering, and retention policy purposes.
  name: Azure Pipelines Build Tags API
  slug: microsoft-azure-pipelines-build-tags-api
- description: Operations for queuing, listing, retrieving, and updating builds including filtering by status, result, branch, and definition.
  name: Azure Pipelines Builds API
  slug: microsoft-azure-pipelines-builds-api
- description: Operations for retrieving pipeline run execution logs for debugging, auditing, and monitoring purposes.
  name: Azure Pipelines Logs API
  slug: microsoft-azure-pipelines-logs-api
- description: Operations for managing YAML-based pipeline definitions including creating, listing, and retrieving pipeline configurations.
  name: Azure Pipelines Pipelines API
  slug: microsoft-azure-pipelines-pipelines-api
- description: Operations for triggering, monitoring, and retrieving pipeline run executions including run state, result, and parameters.
  name: Azure Pipelines Runs API
  slug: microsoft-azure-pipelines-runs-api
artifact_total: 27
collections:
- collection_type: postman
  name: Azure Pipelines Build REST Artifacts API
  slug: postman-microsoft-azure-pipelines-artifacts-api
- collection_type: postman
  name: Azure Pipelines Build REST Artifacts Build Artifacts API
  slug: postman-microsoft-azure-pipelines-build-artifacts-api
- collection_type: postman
  name: Azure Pipelines Build REST Artifacts Build Definitions API
  slug: postman-microsoft-azure-pipelines-build-definitions-api
- collection_type: postman
  name: Azure Pipelines Build REST Artifacts Build Tags API
  slug: postman-microsoft-azure-pipelines-build-tags-api
- collection_type: postman
  name: Azure Pipelines Build REST Artifacts Builds API
  slug: postman-microsoft-azure-pipelines-builds-api
- collection_type: postman
  name: Azure Pipelines Build REST Artifacts Logs API
  slug: postman-microsoft-azure-pipelines-logs-api
- collection_type: postman
  name: Azure Build REST Artifacts Pipelines API
  slug: postman-microsoft-azure-pipelines-pipelines-api
- collection_type: postman
  name: Azure Pipelines Build REST Artifacts Runs API
  slug: postman-microsoft-azure-pipelines-runs-api
- collection_type: open
  name: Azure Pipelines Build REST API
  slug: open-azure-pipelines-build-api
- collection_type: open
  name: Azure Pipelines REST API
  slug: open-azure-pipelines-rest-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-pipelines/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-pipelines-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-pipelines-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-pipelines-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines
- group: start
  title: ''
  type: Portal
  url: https://dev.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/devops/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/devops/pipelines/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/devops
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/products/devops
- group: start
  title: ''
  type: Login
  url: https://dev.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/devops/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/devops/release-notes/features-timeline-released
- group: build
  title: ''
  type: Client Libraries
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries
- group: operate
  title: ''
  type: Community
  url: https://developercommunity.visualstudio.com/AzureDevOps
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftDocs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/MicrosoftDocs/azure-devops-docs
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-devops
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.visualstudio.com/azuredevops
- group: build
  title: ''
  type: CLI
  url: https://github.com/Azure/azure-devops-cli-extension
- group: docs
  title: ''
  type: Task Reference
  url: https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/
created: '2024'
description: Azure Pipelines is a cloud service that you can use to automatically build and test your code project and make it available to other users. It works with just about any language or project type.
finops:
- name: Microsoft Azure Pipelines Finops
  service_category: Developer Tools / CI-CD
  slug: microsoft-azure-pipelines-finops
image: https://azure.microsoft.com/svghandler/devops/?width=600&height=315
layout: provider
modified: '2026-05-19'
name: Azure Pipelines
nav: Providers
network: true
overview: 'Azure Pipelines publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Build Artifacts API, Build Definitions API, and 5 more. Tagged areas include Automation, Build, CI/CD, Deployment, and DevOps.


  Azure Pipelines'' developer surface includes authentication, getting-started guide, developer portal, pricing, engineering blog, documentation, signup flow, and 18 more developer resources.'
plans:
- name: Microsoft Azure Pipelines Plans Pricing
  plan_count: 6
  slug: microsoft-azure-pipelines-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Microsoft Azure Pipelines Rate Limits
  slug: microsoft-azure-pipelines-rate-limits
score:
  band: strong
  composite: 59.0
  delta: -1.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 61.9
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-pipelines/refs/heads/main/screenshots/microsoft-azure-pipelines-2026-06-20T185430.png
security:
- kind: authentication
  name: Microsoft Azure Pipelines Authentication
  slug: microsoft-azure-pipelines-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Microsoft Azure Pipelines Domain Security
  slug: microsoft-azure-pipelines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-pipelines
tags:
- Automation
- Build
- CI/CD
- Deployment
- DevOps
- Pipelines
website: https://azure.microsoft.com/en-us/products/devops
---

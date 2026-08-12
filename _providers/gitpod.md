---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 388
  human_in_the_loop: 5
  name: Gitpod Agentic Access
  operation_count: 388
  slug: gitpod-agentic-access
  summary_line: 388 operations · 388 acting · 5 human-in-the-loop
api_count: 34
apis:
- description: REST API for managing organizations, groups, members, role assignments, permissions, and organization-level policies. Supports SSO login providers, secrets scoped to organizations, and audit trails fo
  name: Gitpod Organizations API
  slug: organizations-api
- description: REST API for managing projects and repositories within a Gitpod organization. Supports creating and listing projects, associating repositories, and configuring project-level policies for environment a
  name: Gitpod Projects API
  slug: projects-api
- description: REST API for managing user accounts, SSO login sessions, and billing information including invoices and spending data. Supports listing joinable organizations, deleting accounts, and retrieving billin
  name: Gitpod Accounts and Billing API
  slug: accounts-billing-api
- description: The gitpod.v1.AccountService API from Gitpod — 10 operation(s) for gitpod.v1.accountservice.
  name: Gitpod gitpod.v1.AccountService API
  slug: gitpod-gitpod-v1-accountservice-api
- description: AgentSecurityService receives agent security events from runners. Authenticated with runner tokens (same as RunnerInteractionService).
  name: Gitpod gitpod.v1.AgentSecurityService API
  slug: gitpod-gitpod-v1-agentsecurityservice-api
- description: The gitpod.v1.AgentService API from Gitpod — 25 operation(s) for gitpod.v1.agentservice.
  name: Gitpod gitpod.v1.AgentService API
  slug: gitpod-gitpod-v1-agentservice-api
- description: BillingService provides billing and subscription management functionality.
  name: Gitpod gitpod.v1.BillingService API
  slug: gitpod-gitpod-v1-billingservice-api
- description: The gitpod.v1.EditorService API from Gitpod — 3 operation(s) for gitpod.v1.editorservice.
  name: Gitpod gitpod.v1.EditorService API
  slug: gitpod-gitpod-v1-editorservice-api
- description: The gitpod.v1.EnvironmentAutomationService API from Gitpod — 18 operation(s) for gitpod.v1.environmentautomationservice.
  name: Gitpod gitpod.v1.EnvironmentAutomationService API
  slug: gitpod-gitpod-v1-environmentautomationservice-api
- description: The gitpod.v1.EnvironmentService API from Gitpod — 15 operation(s) for gitpod.v1.environmentservice.
  name: Gitpod gitpod.v1.EnvironmentService API
  slug: gitpod-gitpod-v1-environmentservice-api
- description: ErrorsService provides endpoints for clients to report errors that will be sent to error reporting systems.
  name: Gitpod gitpod.v1.ErrorsService API
  slug: gitpod-gitpod-v1-errorsservice-api
- description: The gitpod.v1.EventService API from Gitpod — 2 operation(s) for gitpod.v1.eventservice.
  name: Gitpod gitpod.v1.EventService API
  slug: gitpod-gitpod-v1-eventservice-api
- description: The gitpod.v1.GatewayService API from Gitpod — 1 operation(s) for gitpod.v1.gatewayservice.
  name: Gitpod gitpod.v1.GatewayService API
  slug: gitpod-gitpod-v1-gatewayservice-api
- description: The gitpod.v1.GroupService API from Gitpod — 14 operation(s) for gitpod.v1.groupservice.
  name: Gitpod gitpod.v1.GroupService API
  slug: gitpod-gitpod-v1-groupservice-api
- description: The gitpod.v1.IdentityService API from Gitpod — 3 operation(s) for gitpod.v1.identityservice.
  name: Gitpod gitpod.v1.IdentityService API
  slug: gitpod-gitpod-v1-identityservice-api
- description: InsightsService provides AI code attribution analytics for projects. The CLI reports per-commit co-author data from git history, and the dashboard reads aggregated stats.
  name: Gitpod gitpod.v1.InsightsService API
  slug: gitpod-gitpod-v1-insightsservice-api
- description: The gitpod.v1.IntegrationService API from Gitpod — 11 operation(s) for gitpod.v1.integrationservice.
  name: Gitpod gitpod.v1.IntegrationService API
  slug: gitpod-gitpod-v1-integrationservice-api
- description: NotificationService manages in-app notifications for users.
  name: Gitpod gitpod.v1.NotificationService API
  slug: gitpod-gitpod-v1-notificationservice-api
- description: OnaIntelligenceService manages organization-level LLM configurations for Ona Intelligence. This service is restricted to Ona employees with the OnaIntelligenceAdmin role.
  name: Gitpod gitpod.v1.OnaIntelligenceService API
  slug: gitpod-gitpod-v1-onaintelligenceservice-api
- description: The gitpod.v1.OrganizationService API from Gitpod — 39 operation(s) for gitpod.v1.organizationservice.
  name: Gitpod gitpod.v1.OrganizationService API
  slug: gitpod-gitpod-v1-organizationservice-api
- description: PrebuildService manages prebuilds for projects to enable faster environment startup times. Prebuilds create snapshots of environments that can be used to provision new environments quickly.
  name: Gitpod gitpod.v1.PrebuildService API
  slug: gitpod-gitpod-v1-prebuildservice-api
- description: The gitpod.v1.ProjectService API from Gitpod — 15 operation(s) for gitpod.v1.projectservice.
  name: Gitpod gitpod.v1.ProjectService API
  slug: gitpod-gitpod-v1-projectservice-api
- description: The gitpod.v1.RunnerConfigurationService API from Gitpod — 21 operation(s) for gitpod.v1.runnerconfigurationservice.
  name: Gitpod gitpod.v1.RunnerConfigurationService API
  slug: gitpod-gitpod-v1-runnerconfigurationservice-api
- description: RunnerInteractionService provides a way for the backend to interact with environment runners.
  name: Gitpod gitpod.v1.RunnerInteractionService API
  slug: gitpod-gitpod-v1-runnerinteractionservice-api
- description: The gitpod.v1.RunnerManagerService API from Gitpod — 6 operation(s) for gitpod.v1.runnermanagerservice.
  name: Gitpod gitpod.v1.RunnerManagerService API
  slug: gitpod-gitpod-v1-runnermanagerservice-api
- description: The gitpod.v1.RunnerService API from Gitpod — 16 operation(s) for gitpod.v1.runnerservice.
  name: Gitpod gitpod.v1.RunnerService API
  slug: gitpod-gitpod-v1-runnerservice-api
- description: The gitpod.v1.SecretService API from Gitpod — 5 operation(s) for gitpod.v1.secretservice.
  name: Gitpod gitpod.v1.SecretService API
  slug: gitpod-gitpod-v1-secretservice-api
- description: The gitpod.v1.ServiceAccountService API from Gitpod — 10 operation(s) for gitpod.v1.serviceaccountservice.
  name: Gitpod gitpod.v1.ServiceAccountService API
  slug: gitpod-gitpod-v1-serviceaccountservice-api
- description: The gitpod.v1.SessionService API from Gitpod — 9 operation(s) for gitpod.v1.sessionservice.
  name: Gitpod gitpod.v1.SessionService API
  slug: gitpod-gitpod-v1-sessionservice-api
- description: TeamService manages teams and team memberships within an organization. A team is an organizational unit that users can belong to. Each user can belong to at most one team per organization.
  name: Gitpod gitpod.v1.TeamService API
  slug: gitpod-gitpod-v1-teamservice-api
- description: UsageService provides usage information about environments, users, and projects.
  name: Gitpod gitpod.v1.UsageService API
  slug: gitpod-gitpod-v1-usageservice-api
- description: The gitpod.v1.UserService API from Gitpod — 14 operation(s) for gitpod.v1.userservice.
  name: Gitpod gitpod.v1.UserService API
  slug: gitpod-gitpod-v1-userservice-api
- description: The gitpod.v1.WebhookService API from Gitpod — 8 operation(s) for gitpod.v1.webhookservice.
  name: Gitpod gitpod.v1.WebhookService API
  slug: gitpod-gitpod-v1-webhookservice-api
- description: The gitpod.v1.WorkflowService API from Gitpod — 16 operation(s) for gitpod.v1.workflowservice.
  name: Gitpod gitpod.v1.WorkflowService API
  slug: gitpod-gitpod-v1-workflowservice-api
artifact_total: 52
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitpod-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gitpod-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitpod-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitpod-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gitpod.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.gitpod.io/docs/references/gitpod-public-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitpod-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitpod/
- group: company
  title: ''
  type: Blog
  url: https://www.gitpod.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gitpod.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitpod.io/
- group: other
  title: ''
  type: X
  url: https://x.com/gitpod
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.gitpod.io/changelog
- group: build
  title: ''
  type: SDKTypeScript
  url: https://github.com/gitpod-io/gitpod-sdk-typescript
- group: build
  title: ''
  type: SDKPython
  url: https://github.com/gitpod-io/gitpod-sdk-python
- group: build
  title: ''
  type: SDKGo
  url: https://github.com/gitpod-io/gitpod-sdk-go
- group: commercial
  title: ''
  type: Plans
  url: plans/gitpod-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gitpod-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gitpod-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/gitpod-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/gitpod-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: Gitpod is a cloud development environment platform that provides on-demand, ephemeral workspaces spun up from git repositories, enabling developers to write, review, and ship code from any device without local setup. Originally focused on browser-based IDEs, the platform evolved into Gitpod Flex, offering REST APIs and SDKs for workspace lifecycle management, environment automation, and organization administration. The Gitpod API supports TypeScript, Python, and Go SDKs and uses bearer token authentication via API keys. In September 2025 Gitpod rebranded to Ona, shifting focus to AI software engineering agents built on top of its secure, isolated environment infrastructure.
examples:
- key_count: 5
  name: Gitpod Create Environment Example
  slug: gitpod-create-environment-example
- key_count: 5
  name: Gitpod Create Organization Example
  slug: gitpod-create-organization-example
- key_count: 5
  name: Gitpod Get Environment Example
  slug: gitpod-get-environment-example
- key_count: 5
  name: Gitpod List Environments Example
  slug: gitpod-list-environments-example
- key_count: 4
  name: Gitpod List Organizations Example
  slug: gitpod-list-organizations-example
finops:
- name: Gitpod Finops
  service_category: Developer Tools
  slug: gitpod-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitpod.png
json_schemas:
- name: Account
  property_count: 10
  slug: gitpod-account
- name: Environment
  property_count: 4
  slug: gitpod-environment
- name: Organization
  property_count: 6
  slug: gitpod-organization
- name: Project
  property_count: 12
  slug: gitpod-project
jsonld:
- class_count: 42
  name: Gitpod Context
  property_count: 2
  slug: gitpod-context
layout: provider
modified: '2026-06-12'
name: Gitpod
nav: Providers
network: true
overview: 'Gitpod publishes 31 APIs on the [APIs.io](https://apis.io/) network, including gitpod.v1.AccountService API, gitpod.v1.AgentSecurityService API, gitpod.v1.AgentService API, and 28 more. Tagged areas include Developer Tools, Cloud Development Environments, Workspaces, AI Agents, and DevOps.


  The Gitpod catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gitpod''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 17 more developer resources.'
plans:
- name: Gitpod Plans Pricing
  plan_count: 2
  slug: gitpod-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Gitpod Rate Limits
  slug: gitpod-rate-limits
rules:
- name: Gitpod API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gitpod-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.6
  delta: -0.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 62.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitpod/refs/heads/main/screenshots/gitpod-2026-06-20T181852.png
security:
- kind: authentication
  name: Gitpod Authentication
  slug: gitpod-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gitpod Domain Security
  slug: gitpod-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gitpod Trust Center
  slug: gitpod-trust-center
  summary_line: SOC 2, GDPR
slug: gitpod
tags:
- Developer Tools
- Cloud Development Environments
- Workspaces
- AI Agents
- DevOps
website: https://www.gitpod.io
---

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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Buildkite Com Agentic Access
  operation_count: 32
  slug: buildkite-com-agentic-access
  summary_line: 32 operations · 9 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: GraphQL endpoint that returns deeply nested data on organizations, pipelines, builds, jobs, agents, clusters, queues, teams, audit events, suites, test executions, and package registries in a single r
  name: Buildkite GraphQL API
  slug: buildkite-graphql-api
- description: 'Backplane consumed by the Buildkite Agent (open source, Go) to register, deregister, accept and finish jobs, upload artifacts, stream job logs, and emit metrics for cluster autoscaling. Authenticated '
  name: Buildkite Agent API
  slug: buildkite-agent-api
- description: Outbound HTTP notifications fired in response to build, job, agent, ping, deployment, and package events across Pipelines, Test Engine, and Package Registries. Verified with the `X-Buildkite-Token` he
  name: Buildkite Webhooks
  slug: buildkite-webhooks
- description: Official Model Context Protocol server that exposes Buildkite REST API surfaces (pipelines, builds, jobs, agents, artifacts, annotations) as MCP tools and toolsets for AI coding agents. Available as b
  name: Buildkite MCP Server
  slug: buildkite-mcp-server
- description: The Access Token API from Buildkite — 1 operation(s) for access token.
  name: Buildkite Access Token API
  slug: buildkite-com-access-token-api
- description: The Agent Tokens API from Buildkite — 1 operation(s) for agent tokens.
  name: Buildkite Agent Tokens API
  slug: buildkite-com-agent-tokens-api
- description: The Agents API from Buildkite — 3 operation(s) for agents.
  name: Buildkite Agents API
  slug: buildkite-com-agents-api
- description: The Annotations API from Buildkite — 1 operation(s) for annotations.
  name: Buildkite Annotations API
  slug: buildkite-com-annotations-api
- description: The Artifacts API from Buildkite — 1 operation(s) for artifacts.
  name: Buildkite Artifacts API
  slug: buildkite-com-artifacts-api
- description: The Builds API from Buildkite — 4 operation(s) for builds.
  name: Buildkite Builds API
  slug: buildkite-com-builds-api
- description: The Clusters API from Buildkite — 1 operation(s) for clusters.
  name: Buildkite Clusters API
  slug: buildkite-com-clusters-api
- description: The Emojis API from Buildkite — 1 operation(s) for emojis.
  name: Buildkite Emojis API
  slug: buildkite-com-emojis-api
- description: The Jobs API from Buildkite — 2 operation(s) for jobs.
  name: Buildkite Jobs API
  slug: buildkite-com-jobs-api
- description: The Meta API from Buildkite — 1 operation(s) for meta.
  name: Buildkite Meta API
  slug: buildkite-com-meta-api
- description: The Metrics API from Buildkite — 1 operation(s) for metrics.
  name: Buildkite Metrics API
  slug: buildkite-com-metrics-api
- description: The Organizations API from Buildkite — 2 operation(s) for organizations.
  name: Buildkite Organizations API
  slug: buildkite-com-organizations-api
- description: The Pipeline Templates API from Buildkite — 1 operation(s) for pipeline templates.
  name: Buildkite Pipeline Templates API
  slug: buildkite-com-pipeline-templates-api
- description: The Pipelines API from Buildkite — 2 operation(s) for pipelines.
  name: Buildkite Pipelines API
  slug: buildkite-com-pipelines-api
- description: The Queues API from Buildkite — 1 operation(s) for queues.
  name: Buildkite Queues API
  slug: buildkite-com-queues-api
- description: The Rules API from Buildkite — 1 operation(s) for rules.
  name: Buildkite Rules API
  slug: buildkite-com-rules-api
- description: The Stacks API from Buildkite — 1 operation(s) for stacks.
  name: Buildkite Stacks API
  slug: buildkite-com-stacks-api
- description: The Teams API from Buildkite — 1 operation(s) for teams.
  name: Buildkite Teams API
  slug: buildkite-com-teams-api
- description: The User API from Buildkite — 1 operation(s) for user.
  name: Buildkite User API
  slug: buildkite-com-user-api
arazzos:
- description: Inspect a finished build, then pull its annotations and artifacts for triage.
  name: Buildkite Build Failure Triage
  slug: buildkite-com-build-failure-triage-workflow
- description: Find the latest running build on a pipeline and cancel it.
  name: Buildkite Cancel Running Build
  slug: buildkite-com-cancel-running-build-workflow
- description: Look up a build, confirm it finished, then list its artifacts.
  name: Buildkite Collect Build Artifacts
  slug: buildkite-com-collect-build-artifacts-workflow
- description: Read a build, pick a finished job, and fetch its log output.
  name: Buildkite Fetch Job Log
  slug: buildkite-com-fetch-job-log-workflow
- description: Create a pipeline in an organization, then trigger its first build.
  name: Buildkite Provision Pipeline And First Build
  slug: buildkite-com-provision-pipeline-and-first-build-workflow
- description: Find the most recent build on a pipeline, rebuild it, then poll the new build.
  name: Buildkite Rebuild Latest Build
  slug: buildkite-com-rebuild-latest-build-workflow
- description: Find a failed job in a build, retry it, then poll the build to completion.
  name: Buildkite Retry Failed Job
  slug: buildkite-com-retry-failed-job-workflow
- description: List agents, inspect one, and stop it when it is no longer connected.
  name: Buildkite Stop Disconnected Agent
  slug: buildkite-com-stop-disconnected-agent-workflow
- description: Create a build on a pipeline, then poll until it reaches a terminal state.
  name: Buildkite Trigger And Poll Build
  slug: buildkite-com-trigger-and-poll-build-workflow
artifact_total: 117
collections:
- collection_type: postman
  name: Buildkite REST API
  slug: postman-buildkite-rest-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Buildkite Agent API
  slug: open-buildkite-agent-api
- collection_type: open
  name: Buildkite Agent Access Token API
  slug: open-buildkite-com-access-token-api
- collection_type: open
  name: Buildkite Agent Access Token Agent Tokens API
  slug: open-buildkite-com-agent-tokens-api
- collection_type: open
  name: Buildkite Agent Access Token Agents API
  slug: open-buildkite-com-agents-api
- collection_type: open
  name: Buildkite Agent Access Token Annotations API
  slug: open-buildkite-com-annotations-api
- collection_type: open
  name: Buildkite Agent Access Token Artifacts API
  slug: open-buildkite-com-artifacts-api
- collection_type: open
  name: Buildkite Agent Access Token Builds API
  slug: open-buildkite-com-builds-api
- collection_type: open
  name: Buildkite Agent Access Token Clusters API
  slug: open-buildkite-com-clusters-api
- collection_type: open
  name: Buildkite Agent Access Token Emojis API
  slug: open-buildkite-com-emojis-api
- collection_type: open
  name: Buildkite Agent Access Token Jobs API
  slug: open-buildkite-com-jobs-api
- collection_type: open
  name: Buildkite Agent Access Token Meta API
  slug: open-buildkite-com-meta-api
- collection_type: open
  name: Buildkite Agent Access Token Metrics API
  slug: open-buildkite-com-metrics-api
- collection_type: open
  name: Buildkite Agent Access Token Organizations API
  slug: open-buildkite-com-organizations-api
- collection_type: open
  name: Buildkite Agent Access Token Pipeline Templates API
  slug: open-buildkite-com-pipeline-templates-api
- collection_type: open
  name: Buildkite Agent Access Token Pipelines API
  slug: open-buildkite-com-pipelines-api
- collection_type: open
  name: Buildkite Agent Access Token Queues API
  slug: open-buildkite-com-queues-api
- collection_type: open
  name: Buildkite Agent Access Token Rules API
  slug: open-buildkite-com-rules-api
- collection_type: open
  name: Buildkite Agent Access Token Stacks API
  slug: open-buildkite-com-stacks-api
- collection_type: open
  name: Buildkite Agent Access Token Teams API
  slug: open-buildkite-com-teams-api
- collection_type: open
  name: Buildkite Agent Access Token User API
  slug: open-buildkite-com-user-api
- collection_type: open
  name: Buildkite REST API
  slug: open-buildkite-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buildkite-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/buildkite-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buildkite-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buildkite-com-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/buildkite-com-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/buildkite-com-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/buildkite-com-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/buildkite-com-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buildkite-com-llms.txt
- group: build
  title: ''
  type: CLI
  url: cli/buildkite-com-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/buildkite-com-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buildkite-com-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/buildkite-com-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buildkite-com-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/buildkite-com-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/buildkite-com-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/buildkite-com-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/buildkite-com-agent-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/buildkite/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-build-failure-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-cancel-running-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-collect-build-artifacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-fetch-job-log-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-provision-pipeline-and-first-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-rebuild-latest-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-retry-failed-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-stop-disconnected-agent-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/buildkite-com-trigger-and-poll-build-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://buildkite.com
- group: docs
  title: ''
  type: Documentation
  url: https://buildkite.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://buildkite.com/docs/tutorials/getting-started
- group: start
  title: ''
  type: Signup
  url: https://buildkite.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://buildkite.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildkite.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildkite.com/legal/privacy-policy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://buildkite.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://buildkite.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://buildkitestatus.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://buildkite.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://buildkite.com/blog
- group: operate
  title: ''
  type: Forums
  url: https://forum.buildkite.community
- group: operate
  title: ''
  type: Support
  url: https://buildkite.com/support
- group: auth
  title: ''
  type: Authentication
  url: https://buildkite.com/docs/apis/managing-api-tokens
- group: operate
  title: ''
  type: RateLimits
  url: https://buildkite.com/docs/apis/rest-api#rate-limits
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buildkite
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/buildkite/agent
- group: build
  title: ''
  type: CLI
  url: https://github.com/buildkite/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/buildkite/go-buildkite
- group: build
  title: ''
  type: SDKs
  url: https://github.com/buildkite/go-pipeline
- group: docs
  title: ''
  type: JSONSchema
  url: https://github.com/buildkite/pipeline-schema
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildkite/buildkite-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildkite/skills
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildkite/agent-stack-k8s
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildkite/elastic-ci-stack-for-aws
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildkite/buildkite-agent-scaler
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildkite/cleanroom
- group: build
  title: ''
  type: Tools
  url: https://github.com/buildkite/emojis
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/buildkite/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/buildkite-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buildkite-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buildkite-com-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/buildkite-com-vocabulary.yml
- group: design
  title: ''
  type: Spectral
  url: rules/buildkite-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Buildkite is a hybrid CI/CD platform that combines a hosted control plane (pipelines.buildkite.com) with self-hosted or Buildkite-Hosted agents that run jobs on customer-controlled infrastructure. The platform spans three core products — Pipelines, Test Engine, and Package Registries — and exposes them through a v2 REST API, a Relay-compliant GraphQL API at graphql.buildkite.com/v1, an Agent API at agent.buildkite.com/v3 consumed by the open-source Go agent, webhooks, and an official MCP server that surfaces those APIs to AI coding agents. Customers route work to specific agent pools through clusters and queues, define pipelines as YAML with dynamic uploads, and integrate with the major source control, cloud, identity, secrets, and observability vendors.
examples:
- key_count: 2
  name: Buildkite Create Build Example
  slug: buildkite-create-build-example
- key_count: 2
  name: Buildkite Graphql Builds Example
  slug: buildkite-graphql-builds-example
- key_count: 2
  name: Buildkite List Agents Example
  slug: buildkite-list-agents-example
features:
- Hybrid CI/CD — self-hosted agents on customer infrastructure plus optional Buildkite Hosted Agents
- Pipelines as YAML with dynamic pipeline upload from inside jobs
- Open source agent (Go) running on Linux, macOS, Windows, FreeBSD
- Clusters and Queues for routing jobs to specific agent pools
- Pipeline Templates for standardizing pipelines across teams
- Rules engine for organizational policies and automation
- Annotations, artifacts, and job logs as first-class API resources
- Buildkite Hosted Agents — Linux, Mac M4, with cache volumes and tunable vCPU sizes
- Test Engine with flaky test management, real-time test analytics, and intelligent test splitting
- Test Engine duration-threshold monitor for long-running test alerts
- Package Registries for npm, PyPI, RubyGems, Maven, Container, Debian, RPM, Terraform, Helm
- SLSA provenance, license checks, and threat scanning on Enterprise Package Registries
- OIDC and OAuth Token Exchange (RFC 8693) for short-lived API tokens from identity providers
- bktec build tooling with automatic OIDC token generation
- Per-user API rate limits with org-wide caps
- GraphQL Portals for scoped, schema-filtered API access
- Batch retry API for failed jobs with optional state filtering
- GitHub webhook trigger expansion (PR reviews, releases, issue comments, deployment status)
- Build page redesign with searchable job list and state-based filters
- SCIM, SAML, ADFS for Enterprise identity
- Audit logs and build exports for compliance and FinOps
- Official MCP server for AI coding agent integration
- Buildkite Skills for Claude Code and Cursor
finops:
- name: Buildkite Com Finops
  service_category: ''
  slug: buildkite-com-finops
graphqls:
- description: GraphQL endpoint that returns deeply nested data on organizations, pipelines, builds, jobs, agents, clusters, queues, teams, audit events, suites, test executions, and package registries in a single r
  name: Buildkite GraphQL API
  slug: buildkite-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buildkite-com.png
integrations:
- GitHub, GitLab, Bitbucket source control providers
- GitHub App, Apps for GitLab and Bitbucket Cloud
- AWS (Elastic CI Stack, EC2, ECS, EKS, Lambda autoscaler)
- Google Cloud (GCE, GKE)
- Microsoft Azure (AKS, Azure DevOps)
- Kubernetes via agent-stack-k8s
- Terraform provider community modules
- Slack, Microsoft Teams, email notifications
- PagerDuty, Opsgenie, Datadog observability
- Honeycomb, OpenTelemetry tracing
- 1Password, HashiCorp Vault, AWS Secrets Manager secrets
- Sentry, Rollbar error tracking
- Snyk, Aikido, Semgrep security scanning
- Docker, Docker Hub, ECR, GCR, GHCR container registries
- Test Engine integrations for RSpec, Jest, pytest, JUnit, Go, Cypress, Playwright
- Package Registries for npm, PyPI, RubyGems, Maven, Container, Debian, RPM, Terraform, Helm
- OIDC integrations with AWS, GCP, Azure, HashiCorp Vault
- OAuth Token Exchange (RFC 8693) for identity provider integrations
- Buildkite MCP Server for Claude, Cursor, and other AI coding agents
json_schemas:
- name: Buildkite Agent
  property_count: 15
  slug: buildkite-agent
- name: Buildkite Build
  property_count: 20
  slug: buildkite-build
- name: Buildkite Pipeline
  property_count: 20
  slug: buildkite-pipeline
json_structures:
- name: Buildkite Com Pipeline Structure
  property_count: 0
  slug: buildkite-com-pipeline-structure
jsonld:
- class_count: 34
  name: Buildkite Com Context
  property_count: 5
  slug: buildkite-com-context
layout: provider
mcp_servers:
- description: Buildkite operates an official Model Context Protocol server that exposes the REST API (organizations, clusters, agents, pipelines, builds, jobs, artifacts, annotations, logs, Test Engine) as MCP tool
  name: Buildkite MCP Server
  slug: buildkite-mcp-server
modified: '2026-06-20'
name: Buildkite
nav: Providers
network: true
overview: 'Buildkite publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Agent Tokens API, Agents API, and 16 more. Tagged areas include CI/CD, Continuous Integration, Continuous Delivery, DevOps, and Pipelines.


  The Buildkite catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Buildkite''s developer surface includes authentication, CLI, changelog, developer portal, documentation, getting-started guide, signup flow, and 56 more developer resources.'
plans:
- name: Buildkite Com Plans Pricing
  plan_count: 4
  slug: buildkite-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Buildkite Com Rate Limits
  slug: buildkite-com-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Buildkite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: buildkite-com-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Buildkite API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: buildkite-rules
scopes:
- name: Buildkite Com Scopes
  scope_count: 42
  slug: buildkite-com-scopes
  summary_line: 42 scopes
score:
  band: strong
  composite: 65.9
  coverage:
    artifact_dirs: 33
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 33.3
    contract_quality: 61.7
    developer_ergonomics: 76.2
    discoverability: 66.7
    governance: 33.3
    operational_transparency: 47.4
  previous_composite: 66.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buildkite-com/refs/heads/main/screenshots/buildkite-com-2026-06-20T173752.png
security:
- kind: authentication
  name: Buildkite Com Authentication
  slug: buildkite-com-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Buildkite Com Domain Security
  slug: buildkite-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Buildkite Com Trust Center
  slug: buildkite-com-trust-center
  summary_line: SOC 2
slug: buildkite-com
tags:
- CI/CD
- Continuous Integration
- Continuous Delivery
- DevOps
- Pipelines
- Hybrid CI
- Build Automation
- Test Engine
- Package Registries
- Agents
- GraphQL
- REST
- MCP
- Webhook
website: https://buildkite.com
---

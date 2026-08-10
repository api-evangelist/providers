---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gitar Agentic Access
  operation_count: 3
  slug: gitar-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: The GitLab MR Status API from Gitar — 1 operation(s) for gitlab mr status.
  name: Gitar GitLab MR Status API
  slug: gitar-gitlab-mr-status-api
- description: The GitLab Projects API from Gitar — 1 operation(s) for gitlab projects.
  name: Gitar GitLab Projects API
  slug: gitar-gitlab-projects-api
- description: The Installation Health API from Gitar — 1 operation(s) for installation health.
  name: Gitar Installation Health API
  slug: gitar-installation-health-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://gitar.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gitar.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitar.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gitar.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gitar.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://gitar.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gitar.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gitar.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.gitar.ai/sign-in
- group: operate
  title: ''
  type: Support
  url: https://go.gitar.ai/community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitarcode
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gitar.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitar.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitar.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gitar.ai/
- group: auth
  title: ''
  type: Compliance
  url: security/gitar-trust-center.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/gitar-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gitar-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gitar-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gitar-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gitar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gitar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gitar-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gitar-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gitar-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitar-domain-security.yml
created: '2026-07-17'
description: Gitar is an AI code review platform that goes beyond commenting on pull and merge requests — it automatically fixes broken builds, failing tests, linting errors, and code-review findings, and validates every change against your CI pipeline before it is pushed. It works directly in the GitHub and GitLab PR interface, analyzes CI failures, deduplicates flaky tests, and runs natural-language repository rules from a .gitar/rules directory. Built by engineers from Uber's development stack and acquired by Sonar (SonarQube), Gitar is used by teams including SoFi, DeepL, and Altruist. It exposes a Bearer-token External API (api.gitar.ai/v1) on the Enterprise plan for installation health checks and GitLab project onboarding, and integrates with Buildkite, CircleCI, Bitrise, Jira, Linear, and Slack.
image: https://gitar.ai/assets/meta-banner.png
layout: provider
mcp_servers:
- description: ''
  name: gitar-mcp.yml
  slug: gitar-mcpyml
modified: '2026-07-19'
name: Gitar
nav: Providers
network: true
overview: 'Gitar publishes 3 APIs on the [APIs.io](https://apis.io/) network: GitLab MR Status API, GitLab Projects API, and Installation Health API. Tagged areas include Company, Developer Tools, Code Review, CI/CD, and Code Quality.


  Gitar''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 52.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.0
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitar/refs/heads/main/screenshots/gitar-2026-07-25T215835.png
security:
- kind: authentication
  name: Gitar Authentication
  slug: gitar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gitar Domain Security
  slug: gitar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gitar Trust Center
  slug: gitar-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: gitar
tags:
- Company
- Developer Tools
- Code Review
- CI/CD
- Code Quality
- AI
- Developer Productivity
- Automation
website: https://gitar.ai/
---

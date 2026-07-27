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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Release Agentic Access
  operation_count: 79
  slug: release-agentic-access
  summary_line: 79 operations · 37 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The Accounts API from Release — 11 operation(s) for accounts.
  name: Release Accounts API
  slug: release-accounts-api
- description: The Apps API from Release — 8 operation(s) for apps.
  name: Release Apps API
  slug: release-apps-api
- description: The Builds API from Release — 5 operation(s) for builds.
  name: Release Builds API
  slug: release-builds-api
- description: The Clusters API from Release — 10 operation(s) for clusters.
  name: Release Clusters API
  slug: release-clusters-api
- description: The Configs API from Release — 9 operation(s) for configs.
  name: Release Configs API
  slug: release-configs-api
- description: The Deploys API from Release — 5 operation(s) for deploys.
  name: Release Deploys API
  slug: release-deploys-api
- description: The Environments API from Release — 6 operation(s) for environments.
  name: Release Environments API
  slug: release-environments-api
- description: The Instances API from Release — 2 operation(s) for instances.
  name: Release Instances API
  slug: release-instances-api
- description: The Remote Development API from Release — 2 operation(s) for remote development.
  name: Release Remote Development API
  slug: release-remote-development-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/release-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/release-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/release-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/release-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/release-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://release.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.release.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.release.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.release.com/reference-documentation/release-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.release.com/getting-started/quickstart.md
- group: operate
  title: ''
  type: Support
  url: mailto:hello@release.com
- group: company
  title: ''
  type: Blog
  url: https://release.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/releasehub-com
- group: commercial
  title: ''
  type: Pricing
  url: https://release.com/pricing
- group: start
  title: ''
  type: Login
  url: https://web.release.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://release.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://release.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.release.com/
- group: auth
  title: ''
  type: Security
  url: https://release.com/legal/security
- group: auth
  title: ''
  type: Compliance
  url: https://release.com/legal/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/release-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/release-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/release-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/release-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/release-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/release-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/release-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/release-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.release.com/reference-documentation/release-api/environments-api.md
- group: design
  title: ''
  type: Conventions
  url: conventions/release-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/release-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Release is a developer-tools platform that provisions on-demand, full-stack ephemeral environments inside your own AWS or GCP cloud accounts. Positioned as a Heroku replacement and a Vercel alternative for full-stack apps, Release turns a repository plus a .release.yaml (or Docker Compose) file into reproducible environments spun up per pull request, per branch, or on demand, with managed Kubernetes clusters, datasets, remote development, and a Release.ai AI sandbox. Teams automate it through a REST Platform API (accounts, apps, environments, deploys, clusters, builds), a GraphQL API, an AI Sandbox API, and a first-party CLI, all authenticated with X-User-Email and X-User-Token headers and described by a canonical OpenAPI contract at https://api.release.com/openapi.json.
image: https://release.com/og/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: release-mcp.yml
  slug: release-mcpyml
modified: '2026-07-21'
name: Release
nav: Providers
network: true
overview: 'Release publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Apps API, Builds API, and 6 more. Tagged areas include Company, Developer Tools, Ephemeral Environments, Platform Engineering, and Deployment.


  Release''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
random_paper: 57
score:
  band: developing
  composite: 55.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.1
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 55.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Release Authentication
  slug: release-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Release Domain Security
  slug: release-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Release Vulnerability Disclosure
  slug: release-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Release Trust Center
  slug: release-trust-center
  summary_line: SOC 2
slug: release
tags:
- Company
- Developer Tools
- Ephemeral Environments
- Platform Engineering
- Deployment
- Kubernetes
- Environments as a Service
- DevOps
- CI/CD
- AI Sandbox
website: https://release.com/
---

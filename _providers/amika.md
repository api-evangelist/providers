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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-07-28'
api_count: 12
apis:
- description: The API keys API from Amika — 2 operation(s) for api keys.
  name: Amika API keys API
  slug: amika-api-keys-api
- description: The Docker registries API from Amika — 2 operation(s) for docker registries.
  name: Amika Docker registries API
  slug: amika-docker-registries-api
- description: The Downloads API from Amika — 1 operation(s) for downloads.
  name: Amika Downloads API
  slug: amika-downloads-api
- description: The Git user settings API from Amika — 1 operation(s) for git user settings.
  name: Amika Git user settings API
  slug: amika-git-user-settings-api
- description: The Integrations API from Amika — 2 operation(s) for integrations.
  name: Amika Integrations API
  slug: amika-integrations-api
- description: The Repositories API from Amika — 5 operation(s) for repositories.
  name: Amika Repositories API
  slug: amika-repositories-api
- description: The Sandboxes API from Amika — 16 operation(s) for sandboxes.
  name: Amika Sandboxes API
  slug: amika-sandboxes-api
- description: The SandboxSnapshots API from Amika — 3 operation(s) for sandboxsnapshots.
  name: Amika SandboxSnapshots API
  slug: amika-sandboxsnapshots-api
- description: The Secrets API from Amika — 11 operation(s) for secrets.
  name: Amika Secrets API
  slug: amika-secrets-api
- description: The Services API from Amika — 2 operation(s) for services.
  name: Amika Services API
  slug: amika-services-api
- description: The Slack API from Amika — 2 operation(s) for slack.
  name: Amika Slack API
  slug: amika-slack-api
- description: The Uploads API from Amika — 2 operation(s) for uploads.
  name: Amika Uploads API
  slug: amika-uploads-api
artifact_total: 15
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.amika.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amika.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amika.dev/reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amika.dev/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/amika-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amika-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/amika-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/amika-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amika-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amika-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amika-lifecycle.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.amika.dev/architecture/roadmap
- group: design
  title: ''
  type: Conventions
  url: conventions/amika-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amika-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amika-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amika-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amika-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gofixpoint
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/gofixpoint/amika
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amika.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.amika.dev/signup
- group: start
  title: ''
  type: Login
  url: https://app.amika.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amika.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amika.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/xDXk4KjGWg
- group: company
  title: ''
  type: Website
  url: https://www.amika.dev
created: '2026-07-17'
description: Amika is a Y Combinator-backed infrastructure company for running AI coding agents in isolated cloud sandboxes. Teams spawn agents from Slack, Linear, GitHub, a CLI, a TypeScript SDK, or the hosted HTTP API to understand a codebase, run in a root-access VM, execute programmable checks (tests, linters, type checkers), and open validated pull requests autonomously. The platform exposes a REST API (v0beta1) for managing repositories, sandboxes, snapshots, agent sessions, secrets, services, storage, and Slack integration, with API-key and OAuth device-flow authentication. Core primitives are shipped open source under the gofixpoint GitHub organization, including the amika CLI, the amikalog session-capture tool, and the @amika/sdk TypeScript client.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amika.png
layout: provider
mcp_servers:
- description: ''
  name: amika-mcp.yml
  slug: amika-mcpyml
modified: '2026-07-17'
name: Amika
nav: Providers
network: true
overview: 'Amika publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API keys API, Docker registries API, Downloads API, and 9 more. Tagged areas include Company, AI Agents, Coding Agents, Developer Tools, and Sandboxes.


  Amika''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, pricing, signup flow, and 20 more developer resources.'
random_paper: 29
score:
  band: developing
  composite: 44.3
  delta: -2.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 39.8
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 46.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amika/refs/heads/main/screenshots/amika-2026-07-25T200103.png
security:
- kind: authentication
  name: Amika Authentication
  slug: amika-authentication
  summary_line: http/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Amika Domain Security
  slug: amika-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amika
tags:
- Company
- AI Agents
- Coding Agents
- Developer Tools
- Sandboxes
- Infrastructure
- CI/CD
- Automation
- Software Factory
- API
website: https://www.amika.dev
---

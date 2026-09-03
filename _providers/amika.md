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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The API keys API from Amika — 2 operation(s) for api keys.
  name: Amika API keys API
  slug: amika-api-keys-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Docker registries API from Amika — 2 operation(s) for docker registries.
  name: Amika Docker registries API
  slug: amika-docker-registries-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Downloads API from Amika — 1 operation(s) for downloads.
  name: Amika Downloads API
  slug: amika-downloads-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Git user settings API from Amika — 1 operation(s) for git user settings.
  name: Amika Git user settings API
  slug: amika-git-user-settings-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Integrations API from Amika — 2 operation(s) for integrations.
  name: Amika Integrations API
  slug: amika-integrations-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Repositories API from Amika — 5 operation(s) for repositories.
  name: Amika Repositories API
  slug: amika-repositories-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Sandboxes API from Amika — 16 operation(s) for sandboxes.
  name: Amika Sandboxes API
  slug: amika-sandboxes-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The SandboxSnapshots API from Amika — 3 operation(s) for sandboxsnapshots.
  name: Amika SandboxSnapshots API
  slug: amika-sandboxsnapshots-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Secrets API from Amika — 11 operation(s) for secrets.
  name: Amika Secrets API
  slug: amika-secrets-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Services API from Amika — 2 operation(s) for services.
  name: Amika Services API
  slug: amika-services-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Slack API from Amika — 2 operation(s) for slack.
  name: Amika Slack API
  slug: amika-slack-api
- baseURL: https://app.amika.dev/api/v0beta1
  baseurl_source: declared
  description: The Uploads API from Amika — 2 operation(s) for uploads.
  name: Amika Uploads API
  slug: amika-uploads-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amika API — v0beta1 API keys API
  slug: open-amika-api-keys-api
- collection_type: open
  name: Amika API — v0beta1 API keys Docker registries API
  slug: open-amika-docker-registries-api
- collection_type: open
  name: Amika API — v0beta1 API keys Downloads API
  slug: open-amika-downloads-api
- collection_type: open
  name: Amika API — v0beta1 API keys Git user settings API
  slug: open-amika-git-user-settings-api
- collection_type: open
  name: Amika API — v0beta1 API keys Integrations API
  slug: open-amika-integrations-api
- collection_type: open
  name: Amika API — v0beta1 API keys Repositories API
  slug: open-amika-repositories-api
- collection_type: open
  name: Amika API — v0beta1 API keys Sandboxes API
  slug: open-amika-sandboxes-api
- collection_type: open
  name: Amika API — v0beta1 API keys SandboxSnapshots API
  slug: open-amika-sandboxsnapshots-api
- collection_type: open
  name: Amika API — v0beta1 API keys Secrets API
  slug: open-amika-secrets-api
- collection_type: open
  name: Amika API — v0beta1 API keys Services API
  slug: open-amika-services-api
- collection_type: open
  name: Amika API — v0beta1 API keys Slack API
  slug: open-amika-slack-api
- collection_type: open
  name: Amika API — v0beta1 API keys Uploads API
  slug: open-amika-uploads-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amika-openapi-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/gofixpoint/amika/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/gofixpoint/amika/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/gofixpoint/amika/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/gofixpoint/amika/blob/main/LICENSE
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
  name: Amika MCP Server
  slug: amika-mcp-server
modified: '2026-07-17'
name: Amika
nav: Providers
network: true
overview: 'Amika publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API keys API, Docker registries API, Downloads API, and 9 more. Tagged areas include Company, AI Agents, Coding Agents, Developer Tools, and Sandboxes.


  Amika''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, pricing, signup flow, and 25 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 46.4
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 85.0
  previous_composite: 48.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
website: https://www.amika.dev
---

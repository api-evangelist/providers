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
api_count: 4
apis:
- description: Account/application metadata.
  name: Moises Application API
  slug: moises-application-api
- description: Create, retrieve, list, and delete processing jobs.
  name: Moises Jobs API
  slug: moises-jobs-api
- description: Temporary file staging for input audio.
  name: Moises Upload API
  slug: moises-upload-api
- description: List the workflows configured in your account.
  name: Moises Workflows API
  slug: moises-workflows-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://moises.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://music.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://music.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://music.ai/docs/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://music.ai/docs/getting-started/quick-start/
- group: commercial
  title: ''
  type: Pricing
  url: https://music.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://music.ai/dash
- group: operate
  title: ''
  type: Support
  url: https://help.moises.ai/hc/
- group: company
  title: ''
  type: Blog
  url: https://moises.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moises-ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/moises-music-ai-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moises-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/moises-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moises-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/moises-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moises-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moises-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/moises-music-ai-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/moises-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moises-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moises-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moises-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moises-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Moises is the creative suite for musicians from Music AI, Inc., serving more than 70 million musicians worldwide with AI-powered tools for practice, performance, and creation — stem separation to isolate vocals and instruments, chord and key detection, AI-generated stems, and voice synthesis across web, desktop, iOS, and Android. The same models power the Music AI developer platform (music.ai, formerly reached at developer.moises.ai), a B2B REST API that exposes those capabilities as composable Modules assembled into Workflows and executed as asynchronous Jobs. Developers upload audio to temporary storage, submit a job against a workflow, and poll for results, with official Node.js and Python SDKs and a command-line client. Moises won iPad App of the Year (2024) and was an Apple Design Awards finalist (2025), and is backed by Norwest Venture Partners.
image: https://music.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: moises-mcp.yml
  slug: moises-mcpyml
modified: '2026-07-20'
name: Moises
nav: Providers
network: true
overview: 'Moises publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Application API, Jobs API, Upload API, and 1 more. Tagged areas include Company, Music, Audio, Artificial Intelligence, and Machine Learning.


  Moises'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 43.9
  delta: -2.3
  facets:
    commercial_clarity: 23.7
    contract_quality: 60.6
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 46.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Moises Authentication
  slug: moises-authentication
  summary_line: apiKey · 1 scheme
slug: moises
tags:
- Company
- Music
- Audio
- Artificial Intelligence
- Machine Learning
- Stem Separation
- Audio Processing
- Media
- Developer Platform
- SDKs
website: https://moises.ai
---

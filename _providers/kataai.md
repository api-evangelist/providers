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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-11'
api_count: 9
apis:
- description: Login and token issuance.
  name: Kata.ai Auth API
  slug: kataai-auth-api
- description: Bot revisions and drafts.
  name: Kata.ai Bots API
  slug: kataai-bots-api
- description: Messaging channels (LINE, Telegram, WhatsApp, etc.).
  name: Kata.ai Channels API
  slug: kataai-channels-api
- description: Deployment versions of a project bot.
  name: Kata.ai Deployments API
  slug: kataai-deployments-api
- description: Named environments binding a deployment version.
  name: Kata.ai Environments API
  slug: kataai-environments-api
- description: Natural Language Understanding models.
  name: Kata.ai NLU API
  slug: kataai-nlu-api
- description: Run entity prediction against a deployed NLU model.
  name: Kata.ai Prediction API
  slug: kataai-prediction-api
- description: A project bundles one Bot, CMS, and/or NLU.
  name: Kata.ai Projects API
  slug: kataai-projects-api
- description: Teams and membership.
  name: Kata.ai Teams API
  slug: kataai-teams-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Log in, create a project, push a bot revision, cut a deployment version, and bind an environment.
  name: Build and deploy a Kata.ai bot
  slug: kataai-build-and-deploy-bot
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://kata.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kata.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kata.ai/kata-platform
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/kata-ai/kata-platform-docs/blob/master/docs/api/kataai-public-api.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kata-ai
- group: start
  title: ''
  type: SignUp
  url: https://cx.kata.ai/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kata.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://kata.ai/contact
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/kataai-platform-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/kataai-nlu-prediction-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kataai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kataai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kataai-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/kataai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kataai-cli.yml
- group: design
  title: ''
  type: Components
  url: components/kataai-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kataai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kataai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kataai-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kataai-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kataai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kataai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kataai-platform-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
created: '2026-07-17'
description: Kata.ai is an Indonesian enterprise conversational-AI company that builds AI agents and chatbots for customer experience, marketing, sales, and HR across financial services, retail, healthcare, automotive, and government. Its developer-facing Kata Platform lets teams create bot projects that bundle a Bot, CMS, and a Natural Language Understanding (NLU) model, then deploy them and connect messaging channels such as LINE, Telegram, WhatsApp, Facebook Messenger, Slack, and Qiscus. Kata.ai exposes a public REST API for managing projects, bots, deployments, environments, channels, teams, and NLUs, an NL Prediction API for entity extraction from a trained model, the kata command line tool, and the Aksara design system. Backed by 500 Global.
image: https://kata.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: kataai-mcp.yml
  slug: kataai-mcpyml
modified: '2026-07-19'
name: Kata.ai
nav: Providers
network: true
overview: 'Kata.ai publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Bots API, Channels API, and 6 more. Tagged areas include Company, Conversational AI, Chatbots, AI Agents, and Natural Language Understanding.


  Kata.ai''s developer surface includes documentation, API reference, signup flow, support, authentication, CLI, and 19 more developer resources.'
random_paper: 39
score:
  band: thin
  composite: 28.4
  delta: -0.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 14.0
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 28.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kataai/refs/heads/main/screenshots/kataai-2026-07-25T223526.png
security:
- kind: authentication
  name: Kataai Authentication
  slug: kataai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kataai Domain Security
  slug: kataai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: kataai
tags:
- Company
- Conversational AI
- Chatbots
- AI Agents
- Natural Language Understanding
- NLU
- Customer Experience
- Messaging
- Indonesia
- Bots
website: https://kata.ai
---

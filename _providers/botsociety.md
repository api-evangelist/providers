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
- description: Manage conversations (legacy apisociety 2.0 API)
  name: BotSociety Conversations API
  slug: botsociety-conversations-api
- description: Retrieve design/integration content (current API)
  name: BotSociety Designs API
  slug: botsociety-designs-api
- description: Manage messages within a conversation (legacy apisociety 2.0 API)
  name: BotSociety Messages API
  slug: botsociety-messages-api
- description: Manage variables within a conversation (legacy apisociety 2.0 API)
  name: BotSociety Variables API
  slug: botsociety-variables-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://botsociety.io
- group: docs
  title: ''
  type: Documentation
  url: https://botsociety.github.io
- group: docs
  title: ''
  type: APIReference
  url: https://botsociety.docs.apiary.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/botsociety
- group: auth
  title: ''
  type: Authentication
  url: authentication/botsociety-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/botsociety-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/botsociety-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/botsociety-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/botsociety-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/botsociety-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/botsociety-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/botsociety-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/botsociety-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/botsociety-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/botsociety-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/botsociety-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/botsociety-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Botsociety is a tool to design, preview, and prototype conversational interfaces — chatbots and voice assistants — before they are built. Its API lets applications retrieve the content of a design (messages, intents, variables, and integration data) at runtime, so bot content can be updated in the design tool without redeploying bot code. The API exposes design retrieval plus a legacy apisociety 2.0 surface for managing conversations, messages, and variables, authenticated with a user id and a public API key sent as request headers. Botsociety, backed by 500 Global, is winding down ("working on a new direction") and its API host is presently unreachable; the artifacts in this repo are reconstructed from the official first-party npm client and public API documentation. Surfaced originally as a 500 Global portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/botsociety.png
layout: provider
mcp_servers:
- description: ''
  name: botsociety-mcp.yml
  slug: botsociety-mcpyml
modified: '2026-07-18'
name: BotSociety
nav: Providers
network: true
overview: 'BotSociety publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Conversations API, Designs API, Messages API, and 1 more. Tagged areas include Company, Chatbots, Conversational AI, Voice Assistants, and Bot Design.


  BotSociety''s developer surface includes documentation, API reference, authentication, changelog, and 14 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 33.7
  delta: -2.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 56.4
    developer_ergonomics: 36.4
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 35.9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/botsociety/refs/heads/main/screenshots/botsociety-2026-07-25T203642.png
security:
- kind: authentication
  name: Botsociety Authentication
  slug: botsociety-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Botsociety Domain Security
  slug: botsociety-domain-security
  summary_line: TLSv1.3 · DMARC
slug: botsociety
tags:
- Company
- Chatbots
- Conversational AI
- Voice Assistants
- Bot Design
- Prototyping
- Developer Tools
website: https://botsociety.io
---

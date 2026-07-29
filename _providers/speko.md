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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Speko Agentic Access
  operation_count: 40
  slug: speko-agentic-access
  summary_line: 40 operations · 22 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: The Agents API from Speko — 2 operation(s) for agents.
  name: Speko Agents API
  slug: speko-agents-api
- description: The Providers API from Speko — 1 operation(s) for providers.
  name: Speko Providers API
  slug: speko-providers-api
- description: The Telephony API from Speko — 22 operation(s) for telephony.
  name: Speko Telephony API
  slug: speko-telephony-api
- description: The Voice API from Speko — 8 operation(s) for voice.
  name: Speko Voice API
  slug: speko-voice-api
artifact_total: 9
asyncapis:
- description: ''
  name: Speko Webhooks
  slug: speko-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.speko.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.speko.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.speko.dev/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.speko.dev/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://speko.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.speko.dev/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://speko.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://speko.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://speko.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpekoAI
- group: operate
  title: ''
  type: StatusPage
  url: https://status.speko.ai
- group: operate
  title: ''
  type: Support
  url: mailto:founders@speko.ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/speko-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/speko-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/speko-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/speko-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/speko-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://speko.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/speko-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/speko-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speko-domain-security.yml
created: '2026-07-17'
description: Speko is a voice-AI gateway - "one API for the whole voice stack." It continuously benchmarks speech-to-text, LLM, and text-to-speech providers and routes every call to the best provider for your language, latency, and cost intent, with transparent server-side failover. Developers ship voice agents in minutes over one REST API (no provider keys required, or bring your own), deploying to phone numbers, web widgets, or one-shot transcribe/synthesize/ complete calls. Speko is a Y Combinator (S26) company based in San Francisco, founded by Beknazar Abdikamalov. The platform advertises SOC 2 Type II, HIPAA, and GDPR posture and ships TypeScript and Python SDKs, a browser SDK, a LiveKit adapter, and a hosted MCP server.
image: https://speko.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: speko-mcp.yml
  slug: speko-mcpyml
modified: '2026-07-21'
name: Speko
nav: Providers
network: true
overview: 'Speko publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Providers API, Telephony API, and 1 more. Tagged areas include Voice, Voice AI, Speech to Text, Text to Speech, and LLM.


  The Speko catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Speko''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 15 more developer resources.'
random_paper: 60
score:
  band: developing
  composite: 53.8
  delta: -1.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 68.3
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Speko Authentication
  slug: speko-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Speko Domain Security
  slug: speko-domain-security
  summary_line: TLSv1.3
slug: speko
tags:
- Voice
- Voice AI
- Speech to Text
- Text to Speech
- LLM
- Telephony
- API Gateway
- Conversational AI
- Developer Tools
- AI Infrastructure
website: https://docs.speko.dev
---

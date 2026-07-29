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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Anam Agentic Access
  operation_count: 44
  slug: anam-agentic-access
  summary_line: 44 operations · 26 acting
api_count: 9
apis:
- description: The Auth API from Anam — 1 operation(s) for auth.
  name: Anam Auth API
  slug: anam-auth-api
- description: The Avatars API from Anam — 2 operation(s) for avatars.
  name: Anam Avatars API
  slug: anam-avatars-api
- description: The Knowledge API from Anam — 5 operation(s) for knowledge.
  name: Anam Knowledge API
  slug: anam-knowledge-api
- description: The Llms API from Anam — 2 operation(s) for llms.
  name: Anam Llms API
  slug: anam-llms-api
- description: The Personas API from Anam — 2 operation(s) for personas.
  name: Anam Personas API
  slug: anam-personas-api
- description: The Sessions API from Anam — 2 operation(s) for sessions.
  name: Anam Sessions API
  slug: anam-sessions-api
- description: The Share Links API from Anam — 2 operation(s) for share links.
  name: Anam Share Links API
  slug: anam-share-links-api
- description: The Tools API from Anam — 2 operation(s) for tools.
  name: Anam Tools API
  slug: anam-tools-api
- description: The Voices API from Anam — 2 operation(s) for voices.
  name: Anam Voices API
  slug: anam-voices-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.anam.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anam.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://anam.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anam.ai/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://anam.ai/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://lab.anam.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://anam.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://anam.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anam.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anam.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@anam.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anam-org
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anam.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anam-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.anam.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.anam.ai/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/anam-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anam-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/anam-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anam-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anam-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/anam-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/anam-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anam-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anam-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anam-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anam-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anam-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anam-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anam-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/anam-security.txt
- group: auth
  title: ''
  type: Security
  url: well-known/anam-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anam-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Anam builds real-time, interactive AI avatars — photorealistic conversational personas that hold face-to-face video conversations for customer support, sales, tutoring, medical and training use cases. Its CARA avatar engine streams over WebRTC with sub-200ms latency and 70+ languages, fronted by a REST API (api.anam.ai) for managing personas, avatars, voices, LLM routing, knowledge (RAG) groups, function-calling tools, session tokens, share links and session analytics. Developers integrate via first-party JavaScript and Python SDKs, a Kotlin Multiplatform SDK, and a Pipecat plugin, or embed a no-code widget. Anam is a Redpoint Ventures portfolio company.
image: https://framerusercontent.com/assets/cyASyHEg6g3WK5dCwQoOyyVbFZU.png
layout: provider
mcp_servers:
- description: ''
  name: anam-mcp.yml
  slug: anam-mcpyml
modified: '2026-07-17'
name: Anam
nav: Providers
network: true
overview: 'Anam publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Avatars API, Knowledge API, and 6 more. Tagged areas include Company, Ai, Avatars, Conversational AI, and Video.


  Anam''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 28 more developer resources.'
random_paper: 13
score:
  band: strong
  composite: 57.2
  delta: -0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.9
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anam/refs/heads/main/screenshots/anam-2026-07-25T200152.png
security:
- kind: authentication
  name: Anam Authentication
  slug: anam-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Anam Domain Security
  slug: anam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anam Vulnerability Disclosure
  slug: anam-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anam Trust Center
  slug: anam-trust-center
  summary_line: SOC 2, HIPAA
slug: anam
tags:
- Company
- Ai
- Avatars
- Conversational AI
- Video
- Real-Time
- Voice
- Agents
website: https://www.anam.ai/
---

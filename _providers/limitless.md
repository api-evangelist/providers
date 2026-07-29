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
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Limitless Agentic Access
  operation_count: 8
  slug: limitless-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 4
apis:
- description: The Chats API from Limitless — 2 operation(s) for chats.
  name: Limitless Chats API
  slug: limitless-chats-api
- description: The Download Audio API from Limitless — 1 operation(s) for download audio.
  name: Limitless Download Audio API
  slug: limitless-download-audio-api
- description: The Lifelogs API from Limitless — 2 operation(s) for lifelogs.
  name: Limitless Lifelogs API
  slug: limitless-lifelogs-api
- description: The Limitless Developer API API from Limitless — 1 operation(s) for limitless developer api.
  name: Limitless Limitless Developer API API
  slug: limitless-limitless-developer-api-api
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.limitless.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.limitless.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.limitless.ai/developers#endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://www.limitless.ai/developers#setup
- group: company
  title: ''
  type: Website
  url: https://www.limitless.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.limitless.ai
- group: start
  title: ''
  type: Login
  url: https://app.limitless.ai
- group: operate
  title: ''
  type: Support
  url: https://www.limitless.ai/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.limitless.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.limitless.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.limitless.ai/privacy-policy
- group: commercial
  title: ''
  type: Privacy
  url: https://www.limitless.ai/privacy
- group: company
  title: ''
  type: About
  url: https://www.limitless.ai/about
- group: company
  title: ''
  type: Careers
  url: https://www.limitless.ai/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/limitless-ai-inc
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/limitless-ai-inc/limitless-api-examples
- group: agent
  title: ''
  type: MCPServer
  url: mcp/limitless-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/limitless-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/limitless-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/limitless-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/limitless-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/limitless-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/limitless-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/limitless-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/limitless-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/limitless-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.limitless.ai/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/limitless-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/limitless-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/limitless-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/limitless-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/limitless-developer-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/limitless-domain-security.yml
created: '2026-07-17'
description: 'Limitless builds the Pendant, a wearable AI device that continuously captures and transcribes the conversations its wearer has, paired with a desktop, web, and mobile app plus "Ask AI" for searching that personal history. The Limitless Developer API gives users programmatic access to their own data: lifelogs (Pendant recordings with markdown transcripts and a speaker-attributed structured contents tree), Ask AI chat history including the assistant''s tool calls and the entries it retrieved, and raw Ogg Opus audio export. The API is authenticated with an X-API-Key header, is cursor paginated, and supports hybrid keyword plus semantic search across a user''s lifelogs. Limitless also runs an official hosted MCP server at https://api.limitless.ai/mcp, backed by a complete OAuth 2.0 and OpenID Connect discovery surface with PKCE and dynamic client registration. Limitless was acquired by Meta; Pendant sales ended 2025-12-05 and existing customers are supported through 2026 on a free
  Unlimited Plan.'
image: https://www.limitless.ai/media/og-preview.jpg
layout: provider
mcp_servers:
- description: ''
  name: limitless-mcp.yml
  slug: limitless-mcpyml
modified: '2026-07-19'
name: Limitless
nav: Providers
network: true
overview: 'Limitless publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chats API, Download Audio API, Lifelogs API, and 1 more. Tagged areas include Artificial Intelligence, Wearables, Voice, Transcription, and Personal Data.


  Limitless'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, privacy policy, authentication, and 27 more developer resources.'
random_paper: 34
rate_limits:
- limit_count: 0
  name: Limitless Rate Limits
  slug: limitless-rate-limits
scopes:
- name: Limitless Scopes
  scope_count: 4
  slug: limitless-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 42.2
  delta: 1.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
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
    score: 58.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/limitless/refs/heads/main/screenshots/limitless-2026-07-25T225205.png
security:
- kind: authentication
  name: Limitless Authentication
  slug: limitless-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Limitless Domain Security
  slug: limitless-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: limitless
tags:
- Artificial Intelligence
- Wearables
- Voice
- Transcription
- Personal Data
- Consumer Hardware
- Search
- Productivity
- Meeting Notes
- Model Context Protocol
website: https://www.limitless.ai/
---

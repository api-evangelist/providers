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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Supernormal Agentic Access
  operation_count: 13
  slug: supernormal-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 5
apis:
- description: The Agent Sessions API from supernormal — 2 operation(s) for agent sessions.
  name: supernormal Agent Sessions API
  slug: supernormal-agent-sessions-api
- description: Operations about agents
  name: supernormal Agents API
  slug: supernormal-agents-api
- description: Operations about calendar
  name: supernormal Calendar Events API
  slug: supernormal-calendar-events-api
- description: Operations about user
  name: supernormal Current User API
  slug: supernormal-current-user-api
- description: Operations about posts
  name: supernormal Posts API
  slug: supernormal-posts-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/supernormal-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://supernormal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.supernormal.com/api-reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supernormal.com/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.supernormal.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.supernormal.com/api-reference/introduction
- group: start
  title: ''
  type: SignUp
  url: https://app.supernormal.com/settings
- group: operate
  title: ''
  type: Support
  url: https://help.supernormal.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.supernormal.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://supernormal.statuspage.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supernormal-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/supernormal-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supernormal-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/supernormal-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supernormal-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/supernormal-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/supernormal-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/supernormal-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/supernormal-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supernormal-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/supernormal-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supernormal-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/supernormal-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Supernormal is an AI meeting assistant and AI-agents platform (backed by Balderton Capital and EQT Ventures) that joins Google Meet, Zoom, and Microsoft Teams calls to capture, transcribe, and summarize meetings into shareable notes with action items. Beyond meeting notes, Supernormal offers configurable AI voice agents that can host or join calls, run surveys and screening interviews, and produce transcripts and structured posts. Its public REST API (https://api.supernormal.com/api/v1) exposes the current user, upcoming calendar events, meeting posts with notes and transcripts, agents, and agent sessions, authenticated with a scoped X-API-TOKEN API key. Supernormal additionally runs an OAuth 2.0 authorization server with dynamic client registration and PKCE, and a published, OAuth-protected Model Context Protocol (MCP) server so agents can access recordings and projects.
image: https://supernormal.com/og-card.png
layout: provider
mcp_servers:
- description: ''
  name: supernormal-mcp.yml
  slug: supernormal-mcpyml
modified: '2026-07-21'
name: supernormal
nav: Providers
network: true
overview: 'supernormal publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agent Sessions API, Agents API, Calendar Events API, and 2 more. Tagged areas include Company, Meetings, Meeting Notes, Transcription, and AI Agents.


  supernormal''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 74
scopes:
- name: Supernormal Scopes
  scope_count: 11
  slug: supernormal-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 39.3
  delta: 0.2
  facets:
    commercial_clarity: 13.2
    contract_quality: 47.6
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Supernormal Authentication
  slug: supernormal-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Supernormal Domain Security
  slug: supernormal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: supernormal
tags:
- Company
- Meetings
- Meeting Notes
- Transcription
- AI Agents
- Voice Agents
- Productivity
- Collaboration
- Model Context Protocol
- REST API
website: https://supernormal.com/
---

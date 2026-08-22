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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Groupthink's hosted, remote Model Context Protocol (MCP) server and API, served from api.groupthink.com. Authenticated with a Bearer API token minted in the app, it lets an AI assistant join live meet
  name: Groupthink MCP & API
  slug: groupthink-mcp-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://groupthink.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://groupthink.com/docs/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/groupthink-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/groupthink-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/groupthink-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groupthink-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/groupthink-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groupthink-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groupthink-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groupthink-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://groupthink.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.groupthink.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://groupthink.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://groupthink.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://groupthink.com/releases/
- group: operate
  title: ''
  type: Support
  url: mailto:support@groupthink.com
- group: other
  title: ''
  type: Download
  url: https://groupthink.com/download/
created: '2026-07-17'
description: Groupthink is a note-taker and professional-relationship memory built by Firstparty Labs, Inc. It sends a notetaker bot into Zoom, Google Meet, and Microsoft Teams meetings, transcribes and summarizes them, then organizes what it captures around the people involved rather than around the meetings — building a living relationship record with pre-meeting briefs, structured decisions and action items, and a daily intelligence brief of who needs attention. Groupthink exposes a hosted, remote Model Context Protocol (MCP) server at api.groupthink.com so Claude, Cursor, and other MCP-compatible AI assistants can join live meetings, read transcripts, speak and chat in the call, and query relationship intelligence using Bearer-token API tokens.
image: https://groupthink.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: groupthink-mcp.yml
  slug: groupthink-mcpyml
modified: '2026-07-19'
name: Groupthink
nav: Providers
network: true
overview: 'Groupthink publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Meetings, Transcription, and Note Taking.


  Groupthink''s developer surface includes documentation, authentication, changelog, pricing, signup flow, engineering blog, support, and 11 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.0
  delta: -0.4
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 39.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 28.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groupthink/refs/heads/main/screenshots/groupthink-2026-07-25T220349.png
security:
- kind: authentication
  name: Groupthink Authentication
  slug: groupthink-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Groupthink Domain Security
  slug: groupthink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groupthink
tags:
- Company
- SaaS
- Meetings
- Transcription
- Note Taking
- Relationship Intelligence
- MCP
- AI Assistant
- Productivity
- CRM
website: https://groupthink.com/docs/
---

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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'Armature''s programmable surface: an ingest API fed by the TypeScript/Python/Go MCP-analytics SDKs, and a read-only hosted MCP server (mcp.armature.tech) that serves reconstructed sessions, use-case cl'
  name: Armature MCP Analytics
  slug: armature-mcp-analytics
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.armature.tech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.armature.tech
- group: docs
  title: ''
  type: APIReference
  url: https://docs.armature.tech/armature-mcp/tools
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.armature.tech/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.armature.tech
- group: start
  title: ''
  type: Login
  url: https://app.armature.tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armature-tech
- group: operate
  title: ''
  type: Support
  url: mailto:contact@armature.tech
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.armature.tech/security/privacy
- group: build
  title: ''
  type: Packages
  url: packages/armature-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/armature-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/armature-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/armature-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/armature-authentication.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/armature-agent-review.md
- group: design
  title: ''
  type: Conventions
  url: conventions/armature-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/armature-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/armature-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/armature-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/armature-domain-security.yml
created: '2026-07-17'
description: Armature is a Y Combinator (Spring 2026) startup building product analytics for AI agent sessions. Instead of tracking clicks in a human UI, Armature captures how users interact with a product through Claude, ChatGPT, Claude Code, Cursor and other agents by way of MCP servers. Drop-in SDKs for TypeScript, Python and Go instrument an MCP server, streaming tool names, timing, outcomes and size-capped previews (with PII and secrets redacted before storage) to Armature, which reconstructs replayable, scored sessions. The platform clusters use cases by volume and pass rate, detects issues ranked by blast radius, and exposes a read-only hosted MCP server so teams can query their own agent-experience analytics from any MCP client. Armature also publishes an open "agent-review" Agent Skill that lets agents submit compact, privacy-safe experience reports about the software flows they use.
image: https://mcp.armature.tech/frontend/assets/armature-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: armature-mcp.yml
  slug: armature-mcpyml
modified: '2026-07-18'
name: Armature
nav: Providers
network: true
overview: 'Armature publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agent Experience, Model Context Protocol, MCP, and Analytics.


  Armature''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 14 more developer resources.'
random_paper: 74
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 30.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/armature/refs/heads/main/screenshots/armature-2026-07-25T201219.png
security:
- kind: authentication
  name: Armature Authentication
  slug: armature-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Armature Domain Security
  slug: armature-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: armature
tags:
- Company
- Agent Experience
- Model Context Protocol
- MCP
- Analytics
- Observability
- AI Agents
- Product Analytics
- Developer Tools
website: https://docs.armature.tech
---

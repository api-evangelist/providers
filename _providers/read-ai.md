---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Open-beta public REST API for programmatic access to a user's Read AI meeting data. Three documented meeting endpoints — list meetings with cursor pagination and epoch-millisecond time filters, retrie
  name: Read AI REST API
  slug: read-ai-rest-api
- description: First-party remote Model Context Protocol server exposing a user's Read AI meeting reports to any MCP client over Streamable HTTP. Two published tools — list_meetings and get_meeting_by_id — return me
  name: Read AI MCP Server
  slug: read-ai-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Read Ai Webhooks
  slug: read-ai-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/read-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.read.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.read.ai/hc/en-us/sections/49378920415891-API-and-MCP
- group: docs
  title: ''
  type: Documentation
  url: https://support.read.ai/hc/en-us/articles/49381161088659-API-Reference
- group: docs
  title: ''
  type: APIReference
  url: https://support.read.ai/hc/en-us/articles/49381161088659-API-Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://support.read.ai/hc/en-us/articles/49379985941523-Read-AI-API-and-MCP-Overview
- group: operate
  title: ''
  type: Support
  url: https://support.read.ai/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.read.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Read-AI-Inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.read.ai/plans-pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.read.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.read.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.read.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/read-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://support.read.ai/hc/en-us/articles/25702259763091-Security-Privacy-Overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.read.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/read-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/read-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/read-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/read-ai-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/read-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/read-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/read-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/read-ai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/read-ai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/read-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/read-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/read-ai-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/read-ai-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/read-ai-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/read-ai-plans.yml
created: '2026-08-05'
description: Read AI is an AI-powered meeting intelligence platform that joins Zoom, Microsoft Teams and Google Meet calls as an authorized notetaker and turns them into structured meeting reports — summaries, chapter summaries, action items, key questions, topics, full speaker-attributed transcripts and engagement metrics — plus enterprise search across email, messaging and calendar. Founded in 2021 in Seattle by the team behind Placed and Foursquare, it reports more than five million monthly active users. For developers, Read AI ships an open-beta public REST API at api.read.ai (v1 meetings, live meetings, cursor pagination, expandable fields), a remote Model Context Protocol server at api.read.ai/mcp listed in the Anthropic and ChatGPT connector directories, HMAC-signed user and workspace webhooks, three provider-authored downloadable Agent Skills, and an OAuth 2.1 authorization server with dynamic client registration. It publishes no OpenAPI.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: read-ai-mcp.yml
  slug: read-ai-mcpyml
modified: '2026-08-05'
name: Read AI
nav: Providers
network: true
overview: 'Read AI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Meeting Intelligence, Artificial Intelligence, Transcription, and Productivity.


  The Read AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Read AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Read Ai Plans
  plan_count: 4
  slug: read-ai-plans
random_paper: 63
rate_limits:
- limit_count: 1
  name: Read Ai Rate Limits
  slug: read-ai-rate-limits
scopes:
- name: Read Ai Scopes
  scope_count: 7
  slug: read-ai-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: strong
  composite: 57.0
  delta: -4.5
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 64.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 61.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/read-ai/refs/heads/main/screenshots/read-ai-2026-08-17T081449.png
security:
- kind: authentication
  name: Read Ai Authentication
  slug: read-ai-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Read Ai Domain Security
  slug: read-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Read Ai Vulnerability Disclosure
  slug: read-ai-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Read Ai Trust Center
  slug: read-ai-trust-center
  summary_line: SOC 2 Type 2, HIPAA, GDPR, EU-U.S. Data Privacy Framework
slug: read-ai
tags:
- Company
- Meeting Intelligence
- Artificial Intelligence
- Transcription
- Productivity
- Collaboration
- Model Context Protocol
- Agents
- Webhooks
- SaaS
website: https://www.read.ai/
---

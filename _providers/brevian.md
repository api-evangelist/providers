---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Brevian's hosted (remote) Model Context Protocol server, exposing revenue-execution context (knowledge, deals, conversations, pipeline) to MCP-capable agents. Access is gated by OAuth 2.1 (authorizati
  name: Brevian MCP Server
  slug: brevian-mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://brevian.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.brevian.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brevian.ai/
- group: operate
  title: ''
  type: Support
  url: https://docs.brevian.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.brevian.ai/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.brevian.ai/
- group: start
  title: ''
  type: Login
  url: https://app.brevian.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.brevian.ai/security/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.brevian.ai/security/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brevian-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.brevian.ai/release_notes/all_release_notes
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.brevian.ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brevian-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brevian-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brevian-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brevian-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brevian-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brevian-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brevian-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brevian-domain-security.yml
created: '2026-07-17'
description: Brevian is a Revenue Execution AI platform for enterprise sales teams. It operates across the full deal lifecycle — preparing reps before calls, guiding them in real time during conversations, automatically capturing deal context into the CRM, and detecting patterns across deals. Brevian connects product knowledge, deals, conversations, and pipeline into a single knowledge graph that sits on top of an existing stack (Salesforce or HubSpot for CRM, Gong or Chorus for conversation intelligence, Zoom, Google Meet, or Microsoft Teams for calls). It exposes a hosted Model Context Protocol (MCP) server so agents can access that revenue-execution context under OAuth. Founded by Vinay Wagh (CEO, ex-Databricks) and Anupreet Walia (CTO); backed by Felicis.
image: https://cdn.prod.website-files.com/68ae7d3f5a3cc059a9f4e2bb/695d011141b1c3f8e8de87eb_opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: brevian-mcp.yml
  slug: brevian-mcpyml
modified: '2026-07-18'
name: Brevian
nav: Providers
network: true
overview: 'Brevian publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, Revenue Execution, and AI Agents.


  Brevian''s developer surface includes documentation, support, engineering blog, signup flow, changelog, authentication, and 14 more developer resources.'
random_paper: 63
scopes:
- name: Brevian Scopes
  scope_count: 1
  slug: brevian-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 29.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brevian/refs/heads/main/screenshots/brevian-2026-07-25T203755.png
security:
- kind: authentication
  name: Brevian Authentication
  slug: brevian-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Brevian Domain Security
  slug: brevian-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Brevian Trust Center
  slug: brevian-trust-center
  summary_line: trust center published
slug: brevian
tags:
- Company
- Artificial Intelligence
- Sales
- Revenue Execution
- AI Agents
- CRM
- Model Context Protocol
- Enterprise
website: https://brevian.ai
---

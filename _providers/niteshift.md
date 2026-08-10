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
    agent_skills: false
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
  score: 23.4
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://niteshift.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.niteshift.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.niteshift.dev
- group: start
  title: ''
  type: Quickstart
  url: https://docs.niteshift.dev/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://niteshift.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://niteshift.dev/blog
- group: start
  title: ''
  type: Login
  url: https://niteshift.dev/login
- group: operate
  title: ''
  type: Support
  url: https://niteshift.dev/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://niteshift.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://niteshift.dev/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://niteshift.dev/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/niteshift-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/niteshift-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/niteshift-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/niteshift-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/niteshift-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/niteshift-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/niteshift-domain-security.yml
created: '2026-07-17'
description: Niteshift is the full-stack cloud for coding agents. Engineering teams define their dev environment, tools, and policies once, then run frontier or open-source coding agents (Claude Code, Codex, Cursor, OpenCode, Pi) inside fully configured, isolated cloud environments that provision databases, auth, workers, and seeded data, then verify changes with tests, browser checks, and CI before opening a PR. Tasks are triggered and observed from GitHub, Linear, and Slack, extended via the Model Context Protocol, and billed as usage-based active agent time. Founded 2026 by Datadog veterans Sajid Mehmood and Conor Branagan; seed-funded by Greylock.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/niteshift.png
layout: provider
mcp_servers:
- description: ''
  name: niteshift-mcp.yml
  slug: niteshift-mcpyml
modified: '2026-07-20'
name: Niteshift
nav: Providers
network: true
overview: 'Niteshift is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Coding Agents, AI Agents, and Developer Tools.


  Niteshift''s developer surface includes documentation, quickstart, pricing, engineering blog, support, changelog, authentication, and 11 more developer resources.'
random_paper: 46
scopes:
- name: Niteshift Scopes
  scope_count: 4
  slug: niteshift-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: thin
  composite: 28.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 28.7
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/niteshift/refs/heads/main/screenshots/niteshift-2026-08-07T185339.png
security:
- kind: authentication
  name: Niteshift Authentication
  slug: niteshift-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Niteshift Domain Security
  slug: niteshift-domain-security
  summary_line: TLSv1.2 · DMARC
slug: niteshift
tags:
- Company
- Infrastructure
- Coding Agents
- AI Agents
- Developer Tools
- Cloud Development Environments
- DevOps
- Automation
website: https://niteshift.dev/
---

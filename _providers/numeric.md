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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: OAuth-protected Model Context Protocol server exposing Numeric's close-automation toolkit to AI agents. Streamable-HTTP MCP endpoint at api.numeric.io/mcp, guarded by OAuth 2.0 / OIDC (auth.numeric.io
  name: Numeric MCP API
  slug: numeric-mcp-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.numeric.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.numeric.io/claude-skills-library
- group: company
  title: ''
  type: Blog
  url: https://numeric.substack.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.numeric.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.numeric.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.numeric.io/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.numeric.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/numeric-io
- group: agent
  title: ''
  type: MCPServer
  url: mcp/numeric-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/numeric-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/numeric-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/numeric-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/numeric-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/numeric-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numeric-domain-security.yml
created: '2026-07-17'
description: Numeric is an AI close-automation platform that unifies close management, financial reporting, and cash operations for complex, high-volume accounting teams (customers include Brex, Plaid, and Stash). Its products span close checklists and account reconciliation, cash matching and journal-entry automation with bank integrations, and an analytics suite for flux/variance analysis and CFO-ready reporting. Numeric's programmable surface is an OAuth 2.0 / OIDC-protected Model Context Protocol (MCP) server at api.numeric.io/mcp, paired with a published library of Claude Agent Skills ("Numeric Toolkit") that automate month-end close, accruals, reconciliation, audit evidence export, and board-ready reporting. Backed by IVP and Menlo Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numeric.png
layout: provider
mcp_servers:
- description: ''
  name: numeric-mcp.yml
  slug: numeric-mcpyml
modified: '2026-07-20'
name: Numeric
nav: Providers
network: true
overview: 'Numeric publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Accounting, Financial Close, and Reconciliation.


  Numeric''s developer surface includes documentation, engineering blog, pricing, authentication, and 12 more developer resources.'
random_paper: 35
scopes:
- name: Numeric Scopes
  scope_count: 4
  slug: numeric-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: emerging
  composite: 27.2
  delta: 0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 26.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Numeric Authentication
  slug: numeric-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Numeric Domain Security
  slug: numeric-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: numeric
tags:
- Company
- Fintech
- Accounting
- Financial Close
- Reconciliation
- MCP
- Agent Skills
- OAuth
website: https://www.numeric.io
---

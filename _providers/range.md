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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: JSON-over-REST API for managing Range Teams, Users, and Check-ins (Updates). API-key (HTTP Basic) or OAuth 2.0 bearer authentication; HTTPS/TLS 1.2+ required.
  name: Range API
  slug: range-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.range.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.range.co/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.range.co/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.range.co/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.range.co/docs/api
- group: company
  title: ''
  type: Blog
  url: https://www.range.co/blog
- group: operate
  title: ''
  type: Support
  url: https://www.range.co/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/range-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.range.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://range.co/signup
- group: start
  title: ''
  type: Login
  url: https://app.range.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.range.co/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policy.range.co/
- group: operate
  title: ''
  type: StatusPage
  url: https://range.statuspage.io/
- group: build
  title: ''
  type: Packages
  url: packages/range-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/range-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/range-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/range-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/range-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/range-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.range.co/security
- group: design
  title: ''
  type: DataModel
  url: data-model/range-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/range-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/range-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/range-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/range-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://policy.range.co/disclosure.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/range-trust-center.yml
created: '2026-07-17'
description: Range is team-communication and collaboration software from Range Labs that centralizes how teams stay in sync. It replaces status meetings with asynchronous daily check-ins, runs meetings with shared agendas and notes, tracks OKRs and goals against daily work, and provides a team directory, connecting to 75+ workplace tools including Slack, Microsoft Teams, Zoom, GitHub, Jira, Asana, and Google Workspace. Range publishes a JSON-over-REST API (base https://api.range.co/v1) for managing Teams, Users, and Check-ins (Updates), authenticated with API keys over HTTP Basic or OAuth 2.0 bearer tokens, plus an official Node.js SDK (range-sdk). It is backed by Bloomberg Beta and Scale Venture Partners.
image: https://www.range.co/img/apple-icon.png
layout: provider
mcp_servers:
- description: ''
  name: range-mcp.yml
  slug: range-mcpyml
modified: '2026-07-20'
name: Range
nav: Providers
network: true
overview: 'Range publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Team Collaboration, Async Communication, Standups, and Check-ins.


  Range''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 63
score:
  band: thin
  composite: 36.4
  delta: -2.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 31.6
  previous_composite: 38.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Range Authentication
  slug: range-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Range Domain Security
  slug: range-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Range Vulnerability Disclosure
  slug: range-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Range Trust Center
  slug: range-trust-center
  summary_line: SOC 2, GDPR, CCPA
slug: range
tags:
- Company
- Team Collaboration
- Async Communication
- Standups
- Check-ins
- Meetings
- Goals
- OKRs
- Productivity
- Workplace
website: https://www.range.co/
---

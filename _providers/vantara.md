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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vantara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getmilana.ai
- group: company
  title: ''
  type: FormerWebsite
  url: https://vantara.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmilana.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getmilana.ai/sdk/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getmilana.ai/quickstart/js-package
- group: company
  title: ''
  type: Blog
  url: https://getmilana.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.getmilana.ai/troubleshooting
- group: start
  title: ''
  type: Login
  url: https://app.getmilana.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getmilana.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getmilana.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getmilana.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VantaraAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/milana-ai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/getmilana
- group: company
  title: ''
  type: Careers
  url: https://getmilana.ai/careers
- group: auth
  title: ''
  type: Security
  url: https://github.com/VantaraAI/milana-sdk/blob/main/SECURITY.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vantara-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vantara-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/vantara-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vantara-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vantara-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vantara-security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vantara-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vantara-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vantara-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vantara-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vantara-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vantara-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/vantara-install-milana.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vantara-changelog.yml
created: '2026-07-17'
description: Milana (formerly Vantara, a Homebrew-backed AI startup) is "the AI product engineer" — it records user sessions through a lightweight open-source browser SDK (milana-js) and uses vision AI to watch the replays, understand what users came to do and whether they succeeded, and surface friction that traditional analytics miss. Beyond the dashboard it exposes a hosted remote MCP server so Claude, Cursor, ChatGPT, and other agents can search sessions, trace user journeys, and run analyses, plus a GitHub codebase integration that lets the Milana agent read code alongside session data and open pull requests that ship fixes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vantara.png
layout: provider
mcp_servers:
- description: ''
  name: vantara-mcp.yml
  slug: vantara-mcpyml
modified: '2026-07-21'
name: Milana
nav: Providers
network: true
overview: 'Milana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Session Replay, Product Analytics, and Developer Tools.


  Milana''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 24 more developer resources.'
random_paper: 29
scopes:
- name: Vantara Scopes
  scope_count: 7
  slug: vantara-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 36.0
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 36.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Vantara Authentication
  slug: vantara-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Vantara Domain Security
  slug: vantara-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vantara Vulnerability Disclosure
  slug: vantara-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Vantara Trust Center
  slug: vantara-trust-center
  summary_line: trust center published
slug: vantara
tags:
- Company
- AI
- Session Replay
- Product Analytics
- Developer Tools
- Agents
- SDK
website: https://getmilana.ai
---

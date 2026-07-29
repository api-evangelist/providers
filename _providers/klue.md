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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Klue Content API returns an organization's published Klue cards and battlecards to external tools and agents, filterable by competitor, battlecard, tag and date range. Access is authenticated with
  name: Klue Content API
  slug: content-api
- description: 'Klue''s Model Context Protocol server lets internal AI agents and enterprise copilots retrieve permissioned competitive intelligence from Klue. It ships two distinct connector surfaces: v1 exposes card'
  name: Klue MCP Server
  slug: mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://klue.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.klue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.app.klue.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://klue.com/blog/how-to-connect-klue-to-chatgpt
- group: operate
  title: ''
  type: Support
  url: https://klue.com/contact
- group: company
  title: ''
  type: Blog
  url: https://klue.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kluein
- group: start
  title: ''
  type: SignUp
  url: https://klue.com/engage/get-demo
- group: start
  title: ''
  type: Login
  url: https://app.klue.com/account/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://klue.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://klue.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://klue.com/product/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/klue-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://klue.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/klue-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/klue-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klue-well-known.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://kluestatus.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klue-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klue-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klue-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klue-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/klue-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klue-llms.txt
created: '2026-07-17'
description: Klue is a Vancouver, BC based B2B SaaS company founded in 2015 that builds a competitive enablement platform combining competitive intelligence and win-loss analysis for revenue teams. The platform collects, curates and distributes competitor intel as cards and battlecards, and layers AI on top through its Compete Agent, Auto Insights, Deal Tips and Smart Answers products, alongside a win-loss suite spanning human expert interviews, an AI interviewer and blindspot interviews. Klue exposes its curated intelligence to developers and AI agents through a Content API secured with bearer API keys and a production Model Context Protocol server offering two connector surfaces plus read and writeback tooling, with an Agent Skill published openly on GitHub. It integrates with Salesforce, Gong, Slack, Microsoft Teams, HubSpot, Highspot, Seismic, Guru and others, and maintains SOC 2 Type II compliance.
image: https://avatars.githubusercontent.com/u/5720878?v=4
layout: provider
mcp_servers:
- description: ''
  name: klue-mcp.yml
  slug: klue-mcpyml
modified: '2026-07-19'
name: Klue
nav: Providers
network: true
overview: 'Klue publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Competitive Intelligence, Competitive Enablement, and Sales Enablement.


  Klue''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 33
score:
  band: thin
  composite: 36.5
  delta: 1.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 35.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klue/refs/heads/main/screenshots/klue-2026-07-25T223952.png
security:
- kind: authentication
  name: Klue Authentication
  slug: klue-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Klue Domain Security
  slug: klue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Klue Vulnerability Disclosure
  slug: klue-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Klue Trust Center
  slug: klue-trust-center
  summary_line: SOC 2 Type II
slug: klue
tags:
- Company
- SaaS
- Competitive Intelligence
- Competitive Enablement
- Sales Enablement
- Win-Loss Analysis
- Market Intelligence
- Battlecards
- Agents
- MCP
website: https://klue.com
---

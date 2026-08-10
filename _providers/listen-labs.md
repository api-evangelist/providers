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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Public API from Listen Labs — 9 operation(s) for public.
  name: Listen Labs Public API
  slug: listen-labs-public-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/listen-labs-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.listenlabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.listenlabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.listenlabs.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.listenlabs.ai/api-v2/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.listenlabs.ai/api-v2/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://listenlabs.ai/auth
- group: operate
  title: ''
  type: Support
  url: mailto:support@listenlabs.ai
- group: company
  title: ''
  type: Blog
  url: https://blog.listenlabs.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.listenlabs.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.listenlabs.ai/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.listenlabs.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MerlinAGI
- group: company
  title: ''
  type: Careers
  url: https://www.listenlabs.ai/careers
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ListenLabsAI
- group: auth
  title: ''
  type: Authentication
  url: authentication/listen-labs-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/listen-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/listen-labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/listen-labs-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/listen-labs-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/listen-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/listen-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/listen-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/listen-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/listen-labs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/listen-labs-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listen-labs-domain-security.yml
created: '2026-07-17'
description: 'Listen Labs is an AI-powered customer research platform that runs AI-moderated user interviews end to end: you define a research goal and a study guide, Listen recruits and screens participants from its panel or your own list, conducts multilingual voice interviews with an AI moderator, and then analyzes the transcripts into themes, segments, executive summaries, video highlight reels, and sourced quotes. The platform is programmable through a public REST API that lets you create a draft study from a JSON study guide, launch it to obtain a self-recruit link, and pull back responses, answers, transcripts, and per-question analysis. Listen Labs also publishes an officially hosted remote MCP server with OAuth 2.1 so agents in Claude, ChatGPT, and Codex can create, edit, launch, and analyze studies conversationally.'
image: https://framerusercontent.com/images/RGXJ1tjBzZi8qrkze1vrTFOQw.webp
layout: provider
mcp_servers:
- description: ''
  name: listen-labs-mcp.yml
  slug: listen-labs-mcpyml
modified: '2026-07-19'
name: Listen Labs
nav: Providers
network: true
overview: 'Listen Labs publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Ai, Market Research, Customer Research, and User Interviews.


  Listen Labs'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, YouTube channel, and 21 more developer resources.'
random_paper: 74
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.7
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 51.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listen-labs/refs/heads/main/screenshots/listen-labs-2026-07-25T225342.png
security:
- kind: authentication
  name: Listen Labs Authentication
  slug: listen-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Listen Labs Domain Security
  slug: listen-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Listen Labs Trust Center
  slug: listen-labs-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701, ISO 42001, GDPR
slug: listen-labs
tags:
- Company
- Ai
- Market Research
- Customer Research
- User Interviews
- Surveys
- Qualitative Research
- Voice AI
- Insights
- Agents
website: https://www.listenlabs.ai
---

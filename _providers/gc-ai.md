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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 76.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 34
  human_in_the_loop: 3
  name: Gc Ai Agentic Access
  operation_count: 58
  slug: gc-ai-agentic-access
  summary_line: 58 operations · 34 acting · 3 human-in-the-loop
api_count: 9
apis:
- description: AI chat completion endpoints
  name: GC AI Chat API
  slug: gc-ai-chat-api
- description: File upload and management endpoints
  name: GC AI Files API
  slug: gc-ai-files-api
- description: Folder management endpoints
  name: GC AI Folders API
  slug: gc-ai-folders-api
- description: Playbook review endpoints
  name: GC AI Playbooks API
  slug: gc-ai-playbooks-api
- description: Personal and company profile endpoints
  name: GC AI Profiles API
  slug: gc-ai-profiles-api
- description: Project management endpoints
  name: GC AI Projects API
  slug: gc-ai-projects-api
- description: Skill library management endpoints
  name: GC AI Skills API
  slug: gc-ai-skills-api
- description: Usage and credit/billing reporting endpoints
  name: GC AI Usage API
  slug: gc-ai-usage-api
- description: Health check and connectivity endpoints
  name: GC AI Utility API
  slug: gc-ai-utility-api
artifact_total: 15
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gc.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gc.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gc.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gc.ai/guides/getting-started/first-steps
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.gc.ai/
- group: operate
  title: ''
  type: Support
  url: mailto:support@gc.ai
- group: operate
  title: ''
  type: Community
  url: https://gc.ai/slack
- group: company
  title: ''
  type: Blog
  url: https://gc.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gc.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gc.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gc.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gc.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gc.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gc.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gc-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gc.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/gc-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gc-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gc-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gc-ai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gc-ai-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gc-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gc-ai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gc-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gc-ai-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gc-ai-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gc-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gc-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gc-ai-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gc-ai-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://gc.ai
created: '2026-07-17'
description: GC AI is the AI platform for in-house legal teams, built by three-time General Counsel Cecilia Ziniti. It helps corporate counsel draft and review contracts, run reusable review Playbooks, conduct grounded legal research across 13M+ US court opinions, and work directly inside Microsoft Word. The GC AI External API (v1) gives programmatic access to chat completions, files, folders, projects, playbooks, and skills for workflow automation (Zapier, Make, n8n, or custom apps), and GC AI also operates an OAuth-protected Model Context Protocol (MCP) server. The platform is SOC 2 Type II, SOC 3, and GDPR compliant, with zero data-retention agreements with its model providers.
image: https://framerusercontent.com/images/Zth3qSTP7QF72InJJ60jCoqi190.png
layout: provider
mcp_servers:
- description: ''
  name: gc-ai-mcp.yml
  slug: gc-ai-mcpyml
modified: '2026-07-19'
name: GC AI
nav: Providers
network: true
overview: 'GC AI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Files API, Folders API, and 6 more. Tagged areas include Company, Legal, Legal AI, Contracts, and In-House Counsel.


  GC AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 2
  name: Gc Ai Rate Limits
  slug: gc-ai-rate-limits
score:
  band: developing
  composite: 57.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.1
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 57.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gc Ai Authentication
  slug: gc-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gc Ai Domain Security
  slug: gc-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Gc Ai Trust Center
  slug: gc-ai-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, SOC 3, GDPR
slug: gc-ai
tags:
- Company
- Legal
- Legal AI
- Contracts
- In-House Counsel
- Artificial Intelligence
- Document Review
- Enterprise
- MCP
website: https://gc.ai
---

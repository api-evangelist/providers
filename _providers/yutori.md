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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Yutori Agentic Access
  operation_count: 29
  slug: yutori-agentic-access
  summary_line: 29 operations · 17 acting
api_count: 5
apis:
- description: The Browsing API from Yutori — 3 operation(s) for browsing.
  name: Yutori Browsing API
  slug: yutori-browsing-api
- description: The Chat Completions API from Yutori — 1 operation(s) for chat completions.
  name: Yutori Chat Completions API
  slug: yutori-chat-completions-api
- description: The Health API from Yutori — 1 operation(s) for health.
  name: Yutori Health API
  slug: yutori-health-api
- description: The Research API from Yutori — 2 operation(s) for research.
  name: Yutori Research API
  slug: yutori-research-api
- description: The Scouting API from Yutori — 16 operation(s) for scouting.
  name: Yutori Scouting API
  slug: yutori-scouting-api
artifact_total: 10
asyncapis:
- description: ''
  name: Yutori Webhooks
  slug: yutori-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.yutori.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yutori.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.yutori.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yutori.com/llm-quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/yutori-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/yutori-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/yutori-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yutori-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yutori-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yutori-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/yutori-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yutori-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yutori-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yutori-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yutori-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/yutori-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/yutori-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yutori-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yutori-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.yutori.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.yutori.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yutori.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yutori.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://yutori.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yutori-ai
- group: operate
  title: ''
  type: Support
  url: mailto:api@yutori.com
- group: company
  title: ''
  type: Website
  url: https://yutori.com
created: '2026-07-17'
description: 'Yutori builds AI web agents delivered as an API. Its Navigator (n1.5) computer-use model drives cloud browsers to navigate, click, type, and extract structured data, and is OpenAI Chat Completions compatible. Scouts are always-on agents that monitor the web and alert on changes; the Research API runs one-time multi-source web research; and a hosted MCP server exposes the same capabilities over the Model Context Protocol. Founded in 2024 by former Meta AI researchers and backed by Radical Ventures and Felicis, Yutori is strongly agent-native: API-key bearer auth, published llms.txt, agent Skills, an RFC 9727 API catalog, and OAuth resource metadata. Pay-as-you-go pricing with $5 in free credits.'
image: https://yutori.com/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: yutori-mcp.yml
  slug: yutori-mcpyml
modified: '2026-07-21'
name: Yutori
nav: Providers
network: true
overview: 'Yutori publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Browsing API, Chat Completions API, Health API, and 2 more. Tagged areas include Company, AI, Agents, Web Automation, and Browser Automation.


  The Yutori catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yutori''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, engineering blog, and 21 more developer resources.'
random_paper: 36
score:
  band: developing
  composite: 53.4
  delta: 0.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.3
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Yutori Authentication
  slug: yutori-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Yutori Domain Security
  slug: yutori-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yutori
tags:
- Company
- AI
- Agents
- Web Automation
- Browser Automation
- Web Monitoring
- Research
- MCP
- LLM
website: https://yutori.com
---

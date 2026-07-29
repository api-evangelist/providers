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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Trust3 API server is the public AI Governance API edge of the Trust3 control plane. AI Assets Collectors running in the customer data plane authenticate every request with a Trust3 API key (AI_GOV
  name: Trust3 AI Governance API
  slug: trust3-ai-governance-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://trust3.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trust3ai.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trust3ai.com/get-started/quick-start.html
- group: company
  title: ''
  type: Blog
  url: https://trust3.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://trust3.ai/feed/
- group: start
  title: ''
  type: Login
  url: https://na.trust3ai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust3.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust3.ai/privacy-policy/
- group: operate
  title: ''
  type: FAQ
  url: https://trust3.ai/faq/
- group: operate
  title: ''
  type: Support
  url: https://privacera.zendesk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/privacera
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trust3-ai-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/trust3-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trust3-ai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trust3-ai-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trust3-ai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trust3-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trust3-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://privacera.com/trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: security/trust3-ai-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trust3-ai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trust3-ai-domain-security.yml
created: '2026-07-17'
description: 'Trust3 AI is the agent-first trust layer for the enterprise, founded by the creators of Apache Ranger and Apache Atlas (the team behind Privacera). The platform discovers every AI agent running across platforms like Databricks and Microsoft Copilot Studio, scores each one with a 1.0-10.0 Trust Score, evaluates agents against policy packs for NERC CIP, the EU AI Act, FERC, and internal AI governance, and gates new agents through structured approval workflows - with MCP and A2A protocol-layer security and the GIA governance assistant built in. Programmatic access uses scoped API keys: AI Assets Collectors authenticate to the Trust3 API server with a Trust3 API key, and external AI clients connect to the hosted MCP server at api.na.trust3ai.com/mcp with an MCP (read) scoped key. Backed by Insight Partners, Sapphire Ventures, Battery Ventures, Accel, Cervin Ventures, and Point72 Ventures ($63.5M raised).'
image: https://trust3.ai/wp-content/uploads/2026/05/cropped-T3-mark_indigo-1-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: trust3-ai-mcp.yml
  slug: trust3-ai-mcpyml
modified: '2026-07-21'
name: Trust3 AI
nav: Providers
network: true
overview: 'Trust3 AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Governance, AI Agents, and Agent Security.


  Trust3 AI''s developer surface includes documentation, getting-started guide, engineering blog, FAQ, support, authentication, changelog, and 15 more developer resources.'
random_paper: 76
score:
  band: thin
  composite: 33.4
  delta: 1.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 32.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Trust3 Ai Authentication
  slug: trust3-ai-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Trust3 Ai Domain Security
  slug: trust3-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trust3 Ai Trust Center
  slug: trust3-ai-trust-center
  summary_line: SOC 2 Type II
slug: trust3-ai
tags:
- Company
- Artificial Intelligence
- AI Governance
- AI Agents
- Agent Security
- MCP Security
- Data Governance
- Compliance
- Observability
- Access Control
website: https://trust3.ai/
---

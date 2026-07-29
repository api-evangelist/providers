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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtue-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.virtueai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.virtueai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtueai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.virtueai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Virtue-AI
- group: start
  title: ''
  type: SignUp
  url: https://www.virtueai.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virtueai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtueai.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/virtue-ai-trust-center.yml
- group: other
  title: ''
  type: X
  url: https://x.com/VirtueAI_co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virtue-ai/
- group: build
  title: ''
  type: Packages
  url: packages/virtue-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/virtue-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/virtue-ai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virtue-ai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtue-ai-authentication.yml
created: '2026-07-17'
description: Virtue AI is an enterprise AI security and safety company that secures AI agents, models, and applications across an organization. Its platform pairs real-time guardrails (VirtueGuard) with automated red-teaming (VirtueRed) and an agent-security suite (AgentSuite-Blue and AgentSuite-Red) to detect and prevent AI-related risks such as prompt injection, unsafe tool use, data exfiltration, and unsanctioned agents and apps running across cloud and endpoints. Virtue AI also ships an MCP gateway that proxies Model Context Protocol tool calls through policy enforcement, an official CLI connector for wiring agent runtimes into that gateway, and a Python package for building on its guardrail and evaluation tooling. The company is backed by Lightspeed Venture Partners and maintains a public developer docs site, research and benchmark leaderboards, and a Vanta-hosted trust center.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/virtue-ai.png
layout: provider
mcp_servers:
- description: ''
  name: virtue-ai-mcp.yml
  slug: virtue-ai-mcpyml
modified: '2026-07-21'
name: Virtue Ai
nav: Providers
network: true
overview: 'Virtue Ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Security, AI Safety, LLM Guardrails, and AI Agents.


  Virtue Ai''s developer surface includes documentation, engineering blog, signup flow, CLI, authentication, and 12 more developer resources.'
random_paper: 71
score:
  band: emerging
  composite: 24.5
  delta: -1.8
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.3
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Virtue Ai Authentication
  slug: virtue-ai-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Virtue Ai Domain Security
  slug: virtue-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Virtue Ai Trust Center
  slug: virtue-ai-trust-center
  summary_line: trust center published
slug: virtue-ai
tags:
- Company
- AI Security
- AI Safety
- LLM Guardrails
- AI Agents
- Red Teaming
- Model Context Protocol
- Agent Security
- Compliance
website: https://www.virtueai.com/
---

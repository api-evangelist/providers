---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Brightai Agentic Access
  operation_count: 6
  slug: brightai-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: A public, read-only Model Context Protocol server (protocol 2025-06-18, serverInfo brightai-public 0.1.0) requiring no authentication. Exposes six tools over BrightAI's Global Observability Database —
  name: BrightAI Public MCP Server
  slug: public-mcp
- description: 'Two unauthenticated JSON endpoints published in BrightAI''s llms.txt: /api/public/industries returns live worldwide aggregates and per-vertical addressable annual impact from the Global Observability D'
  name: BrightAI Public Observatory Data API
  slug: public-data
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bright.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://public.stateful.world/start.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brightai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brightai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brightai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brightai-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brightai-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brightai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brightai-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/brightai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bright.ai/trust-and-security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bright.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://bright.ai/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://bright.ai/get-started/
created: '2026-08-08'
description: BrightAI builds Physical AI for essential services — continuous, AI-driven awareness of the real-time state of physical infrastructure for operators of water, power, energy, transportation and industrial systems. Founded in 2019 by SmartThings founder Alex Hawkinson, the company ships a four-layer Stateful platform (Data Acquisition, AI Hub, Stateful OS, Foundation Models) combining peel-and-stick sensors (Stateful Sticker), autonomous drone and quadruped inspection, a voice-interactive field Stateful Wearable, and infrastructure foundation models trained on operational outcomes across millions of industrial assets. BrightAI publishes no conventional developer portal or OpenAPI, but it does operate a public, no-authentication Model Context Protocol server at public.stateful.world/mcp exposing six read-only tools over its Global Observability Database, alongside an llms.txt index, agent-addressed markdown briefs, and two unauthenticated public JSON endpoints.
image: https://cdn.prod.website-files.com/6a4ea9e79536d28883c64986/6a4ea9e79536d28883c64b40_bright-ai-favicon-256x256.jpg
layout: provider
mcp_servers:
- description: ''
  name: BrightAI MCP Server
  slug: brightai-mcp-server
modified: '2026-08-08'
name: BrightAI
nav: Providers
network: true
overview: 'BrightAI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Physical AI, Industrial IoT, Infrastructure Monitoring, and Predictive Maintenance.


  BrightAI''s developer surface includes documentation, authentication, support, signup flow, and 13 more developer resources.'
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/brightai/refs/heads/main/screenshots/brightai-2026-09-02T144947.png
security:
- kind: authentication
  name: Brightai Authentication
  slug: brightai-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Brightai Domain Security
  slug: brightai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Brightai Trust Center
  slug: brightai-trust-center
  summary_line: SOC 2
slug: brightai
tags:
- Company
- Physical AI
- Industrial IoT
- Infrastructure Monitoring
- Predictive Maintenance
- Edge AI
- Foundation Models
- MCP
- Energy and Utilities
- Water and Wastewater
website: https://www.bright.ai/
---

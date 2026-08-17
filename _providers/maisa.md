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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'Maisa''s developer REST API. Key-authenticated (X-API-Key), base URL https://api.maisa.ai, all operations under /v1. Surfaces: capabilities (compare/extract/summarize over text and media), models (embe'
  name: Maisa API
  slug: maisa-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maisa-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maisa-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/maisa-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/maisa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/maisa-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maisa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/maisa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/maisa-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/maisa-mcp.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.maisa.ai/docs/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maisaai
- group: company
  title: ''
  type: Website
  url: https://maisa.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.maisa.ai/
- group: company
  title: ''
  type: Blog
  url: https://maisa.ai/agentic-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://maisa.ai/agentic-insights/feed/
- group: operate
  title: ''
  type: Support
  url: https://maisa.ai/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://maisa.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maisa.ai/privacy-policy/
created: '2026-07-17'
description: Maisa is an enterprise agentic-AI company whose platform, Maisa Studio, lets non-technical teams build, deploy, and manage "Digital Workers" — AI agents that automate complex, regulated, end-to-end business processes. Its proprietary Knowledge Processing Unit (KPU) and Chain-of-Work approach combine large and small language models to deliver deterministic, auditable, hallucination-resistant execution rather than probabilistic responses, making it regulator-ready from day one. Maisa targets highly regulated verticals — banking and financial services, insurance, manufacturing and supply chain, and engineering/infrastructure — with an employee-based pricing model instead of per-token API billing. Maisa also exposes a developer REST API at api.maisa.ai (API-key authenticated via X-API-Key) with capabilities (compare/extract/summarize over text and media), models (embeddings, rerank), a KPU run endpoint, a file-interpreter (PDF/DOCX/HTML/image/audio), and Mainet search — with official
  first-party Python and Node SDKs both named "maisa"; the Maisa Studio product and the docs portal (docs.maisa.ai) sit behind an AWS Cognito login. Backed by Creandum and ForgePoint, Maisa has raised a $25M seed round and been named a Gartner front-runner in agentic AI. This profile was enriched from Maisa's public marketing surface, llms.txt, and the official open-source SDK repositories.
image: https://maisa.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: maisa-mcp.yml
  slug: maisa-mcpyml
modified: '2026-07-20T12:00:00Z'
name: Maisa
nav: Providers
network: true
overview: 'Maisa publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Agentic AI, AI Agents, and Digital Workers.


  Maisa''s developer surface includes authentication, API reference, documentation, engineering blog, support, and 13 more developer resources.'
random_paper: 76
score:
  band: emerging
  composite: 22.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maisa/refs/heads/main/screenshots/maisa-2026-07-25T225927.png
security:
- kind: authentication
  name: Maisa Authentication
  slug: maisa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Maisa Domain Security
  slug: maisa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maisa
tags:
- Company
- Ai
- Agentic AI
- AI Agents
- Digital Workers
- Business Process Automation
- Enterprise Automation
- Banking
- Insurance
website: https://maisa.ai/
---

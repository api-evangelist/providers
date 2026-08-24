---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/naboo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.naboo.ai/
- group: start
  title: ''
  type: Login
  url: https://app.naboo.ai
- group: auth
  title: ''
  type: TrustCenter
  url: security/naboo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.naboo.ai/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.naboo.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.naboo.ai/terms-of-use.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/naboo-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/naboo-llms.txt
created: '2026-07-17'
description: 'Naboo is Reasoning Layer infrastructure for enterprise AI agents, built on a Decision Graph that models how a company actually decides, ships, and unblocks - who decided what, what triggered each decision, what blocks it, and what depends on it - across code, tickets, pull requests, docs, Slack, runtime, and internal services. Any AI agent in the organization queries the graph in GraphQL, or through an MCP server that turns plain intent into a structured query, and gets a structured answer instead of a list of search results. Naboo deploys on-premise or in a customer VPC with zero data egress, integrates with any LLM (OpenAI, Anthropic, Llama, Mistral) and agentic framework (LangChain, AutoGen, CrewAI), and enforces existing role-based access controls at retrieval time. Founded in 2023 by Gilad Salinger (CEO) and Dror Wolmer (CTO), with production customers Global-E (NASDAQ: GLBE) and Melio.'
image: https://www.naboo.ai/naboo-logo.svg
layout: provider
modified: '2026-07-20'
name: Naboo
nav: Providers
network: true
overview: Naboo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Knowledge Graph, and Reasoning Layer.
random_paper: 2
score:
  band: emerging
  composite: 14.4
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/naboo/refs/heads/main/screenshots/naboo-2026-08-07T184604.png
security:
- kind: domain-security
  name: Naboo Domain Security
  slug: naboo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Naboo Trust Center
  slug: naboo-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, GDPR, HIPAA, Penetration Testing
slug: naboo
tags:
- Company
- Artificial Intelligence
- AI Agents
- Knowledge Graph
- Reasoning Layer
- GraphQL
- MCP
- Enterprise Software
- Developer Infrastructure
- RAG
website: https://www.naboo.ai/
---

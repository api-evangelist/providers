---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Mastra Agentic Access
  operation_count: 37
  slug: mastra-agentic-access
  summary_line: 37 operations · 17 acting
api_count: 11
apis:
- description: Mastra is an open-source TypeScript AI agent framework that enables developers to build and deploy AI-powered applications with agents, workflows, RAG pipelines, and third-party integrations.
  name: Mastra
  slug: mastra
- description: The Agents API from Mastra — 6 operation(s) for agents.
  name: Mastra Agents API
  slug: mastra-agents-api
- description: The Conversations API from Mastra — 3 operation(s) for conversations.
  name: Mastra Conversations API
  slug: mastra-conversations-api
- description: The Logs API from Mastra — 1 operation(s) for logs.
  name: Mastra Logs API
  slug: mastra-logs-api
- description: The Mcp API from Mastra — 2 operation(s) for mcp.
  name: Mastra Mcp API
  slug: mastra-mcp-api
- description: The Memory API from Mastra — 3 operation(s) for memory.
  name: Mastra Memory API
  slug: mastra-memory-api
- description: The Responses API from Mastra — 2 operation(s) for responses.
  name: Mastra Responses API
  slug: mastra-responses-api
- description: The Telemetry API from Mastra — 2 operation(s) for telemetry.
  name: Mastra Telemetry API
  slug: mastra-telemetry-api
- description: The Tools API from Mastra — 3 operation(s) for tools.
  name: Mastra Tools API
  slug: mastra-tools-api
- description: The Vectors API from Mastra — 3 operation(s) for vectors.
  name: Mastra Vectors API
  slug: mastra-vectors-api
- description: The Workflows API from Mastra — 8 operation(s) for workflows.
  name: Mastra Workflows API
  slug: mastra-workflows-api
artifact_total: 18
collections:
- collection_type: open
  name: Mastra Server REST API
  slug: open-mastra
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mastra-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mastra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mastra-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mastra-ai
- group: company
  title: ''
  type: Website
  url: https://mastra.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mastra-ai
- group: docs
  title: ''
  type: Documentation
  url: https://mastra.ai/docs
- group: agent
  title: ''
  type: LlmsText
  url: https://mastra.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://mastra.ai/blog
created: '2026-01-02'
description: Mastra is an open-source TypeScript AI agent framework from the team that built Gatsby. It enables developers to prototype and productionize AI features using a modern JavaScript stack with tools for agents, workflows, RAG, and integrations.
finops:
- name: Mastra Finops
  service_category: API
  slug: mastra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mastra.png
layout: provider
modified: '2026-04-28'
name: Mastra
nav: Providers
network: true
overview: 'Mastra publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Conversations API, Logs API, and 7 more. Tagged areas include Agents, AI, JavaScript, RAG, and TypeScript.


  Mastra''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Mastra Plans Pricing
  plan_count: 3
  slug: mastra-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Mastra Rate Limits
  slug: mastra-rate-limits
score:
  band: thin
  composite: 35.2
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 46.6
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mastra/refs/heads/main/screenshots/mastra-2026-06-20T185031.png
security:
- kind: authentication
  name: Mastra Authentication
  slug: mastra-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mastra Domain Security
  slug: mastra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mastra
tags:
- Agents
- AI
- JavaScript
- RAG
- TypeScript
- Workflows
website: https://mastra.ai/
---

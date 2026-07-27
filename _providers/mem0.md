---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Mem0 Agentic Access
  operation_count: 52
  slug: mem0-agentic-access
  summary_line: 52 operations · 34 acting
api_count: 15
apis:
- description: The Mem0 Platform API provides hosted memory services for AI agents, exposing endpoints for adding, searching, retrieving, updating, and deleting memories, plus entities, events, organizations, projec
  name: Mem0 Platform API
  slug: platform-api
- description: The agents API from Mem0 — 1 operation(s) for agents.
  name: Mem0 agents API
  slug: mem0-agents-api
- description: The apps API from Mem0 — 1 operation(s) for apps.
  name: Mem0 apps API
  slug: mem0-apps-api
- description: The entities API from Mem0 — 3 operation(s) for entities.
  name: Mem0 entities API
  slug: mem0-entities-api
- description: The events API from Mem0 — 2 operation(s) for events.
  name: Mem0 events API
  slug: mem0-events-api
- description: The exports API from Mem0 — 2 operation(s) for exports.
  name: Mem0 exports API
  slug: mem0-exports-api
- description: The feedback API from Mem0 — 1 operation(s) for feedback.
  name: Mem0 feedback API
  slug: mem0-feedback-api
- description: The memories API from Mem0 — 12 operation(s) for memories.
  name: Mem0 memories API
  slug: mem0-memories-api
- description: The organizations API from Mem0 — 3 operation(s) for organizations.
  name: Mem0 organizations API
  slug: mem0-organizations-api
- description: The Project API from Mem0 — 1 operation(s) for project.
  name: Mem0 Project API
  slug: mem0-project-api
- description: The projects API from Mem0 — 3 operation(s) for projects.
  name: Mem0 projects API
  slug: mem0-projects-api
- description: The runs API from Mem0 — 1 operation(s) for runs.
  name: Mem0 runs API
  slug: mem0-runs-api
- description: The stats API from Mem0 — 1 operation(s) for stats.
  name: Mem0 stats API
  slug: mem0-stats-api
- description: The users API from Mem0 — 1 operation(s) for users.
  name: Mem0 users API
  slug: mem0-users-api
- description: The webhooks API from Mem0 — 2 operation(s) for webhooks.
  name: Mem0 webhooks API
  slug: mem0-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: Mem0 API Docs
  slug: open-mem0
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mem0-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mem0-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mem0-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mem0.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mem0.ai
- group: company
  title: ''
  type: Blog
  url: https://mem0.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mem0ai
- group: commercial
  title: ''
  type: Pricing
  url: https://mem0.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mem0.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mem0.ai/privacy
- group: operate
  title: ''
  type: Discord
  url: https://mem0.dev/DiD
- group: other
  title: ''
  type: X
  url: https://x.com/mem0ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mem0
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mem0.ai/llms.txt
created: '2026-05-23'
description: Mem0 is a memory infrastructure layer that gives AI agents and applications persistent context across sessions. The platform automatically condenses chat history into compact memories that reduce tokens and latency while preserving the right context for retrieval. Mem0 offers both a managed cloud platform and a permissively licensed open source project, with multi-tenant organizations, projects, users, and webhooks. It integrates with most popular agent frameworks including LangChain, LangGraph, CrewAI, AutoGen, LlamaIndex, the OpenAI Agents SDK, and the Vercel AI SDK. Enterprise features cover SOC 2, HIPAA, BYOK, auditable logging, and observability for production agent deployments.
finops:
- name: Mem0 Finops
  service_category: API
  slug: mem0-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mem0.png
layout: provider
modified: '2026-05-23'
name: Mem0
nav: Providers
network: true
overview: 'Mem0 publishes 14 APIs on the [APIs.io](https://apis.io/) network, including agents API, apps API, entities API, and 11 more. Tagged areas include Memory, AI Agents, Agent Memory, Context, and LLMs.


  Mem0''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Mem0 Plans Pricing
  plan_count: 1
  slug: mem0-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 2
  name: Mem0 Rate Limits
  slug: mem0-rate-limits
score:
  band: thin
  composite: 42.3
  delta: 3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mem0/refs/heads/main/screenshots/mem0-2026-06-20T185233.png
security:
- kind: authentication
  name: Mem0 Authentication
  slug: mem0-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mem0 Domain Security
  slug: mem0-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mem0
tags:
- Memory
- AI Agents
- Agent Memory
- Context
- LLMs
- Retrieval
- Vector
- LangChain
- CrewAI
- AutoGen
- LlamaIndex
- Open Source
- Infrastructure
website: https://mem0.ai
---

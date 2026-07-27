---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: Open-source Python framework for building agents with memory, knowledge, and tools. Provides Agent, Team, Workflow, Tools, Memory, Knowledge, and Storage primitives. Multi-modal and type-safe; support
  name: Agno Python Framework
  slug: agno-framework
- description: Pre-built FastAPI runtime that exposes 50+ REST, SSE, and WebSocket endpoints for running agents, teams, and workflows in production. Deployable as a Docker container in any cloud or data center, keep
  name: AgentOS Runtime API
  slug: agentos-runtime
- description: Hosted web UI at os.agno.com for managing, monitoring, debugging, and testing AgentOS deployments. Connects directly from the browser to the customer's AgentOS runtime without proxying data through Ag
  name: AgentOS Control Plane
  slug: agentos-control-plane
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phidata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agno.com
- group: company
  title: ''
  type: Website
  url: https://www.phidata.com
- group: start
  title: ''
  type: Portal
  url: https://docs.agno.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agno.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/agno-agi
- group: other
  title: ''
  type: Repository
  url: https://github.com/agno-agi/agno
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/agno/
- group: start
  title: ''
  type: Login
  url: https://os.agno.com
- group: build
  title: ''
  type: Examples
  url: https://docs.agno.com/examples/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.agno.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agno.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agno.com/privacy
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/4MtYHHrgA8
created: '2026-05-23'
description: Agno (formerly Phidata) is a Python framework, runtime, and control plane for building, running, and managing fleets of AI agents. The core agno library provides Agent, Team, Workflow, Tools, Memory, and Knowledge primitives across many LLM providers. AgentOS adds a FastAPI runtime with 50+ REST/SSE/WebSocket endpoints, plus a hosted control plane UI at os.agno.com for tracing, scheduling, RBAC, audit, and human approval - while user data stays inside the customer's own cloud.
finops:
- name: Phidata Finops
  service_category: API
  slug: phidata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phidata.png
layout: provider
modified: '2026-05-23'
name: Phidata / Agno
nav: Providers
network: true
overview: 'Phidata / Agno publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Agno, Phidata, Python, and Framework.


  Phidata / Agno''s developer surface includes developer portal, documentation, GitHub presence, code examples, engineering blog, and 9 more developer resources.'
plans:
- name: Phidata Plans Pricing
  plan_count: 1
  slug: phidata-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 2
  name: Phidata Rate Limits
  slug: phidata-rate-limits
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phidata/refs/heads/main/screenshots/phidata-2026-06-20T191648.png
security:
- kind: domain-security
  name: Phidata Domain Security
  slug: phidata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: phidata
tags:
- AI Agents
- Agno
- Phidata
- Python
- Framework
- Runtime
- AgentOS
- Multi-Agent
- Memory
- Tools
- Open Source
website: https://agno.com
---

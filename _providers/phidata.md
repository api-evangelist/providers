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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-08-30'
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/agno-agi/agno/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/agno-agi/agno/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/agno-agi/agno/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/agno-agi/agno/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/agno-agi/agno/blob/main/LICENSE
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


  Phidata / Agno''s developer surface includes developer portal, documentation, GitHub presence, code examples, engineering blog, and 14 more developer resources.'
plans:
- name: Phidata Plans Pricing
  plan_count: 1
  slug: phidata-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Phidata Rate Limits
  slug: phidata-rate-limits
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 65.0
  previous_composite: 31.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Open-Source
website: https://agno.com
---

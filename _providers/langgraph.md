---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Langgraph Agentic Access
  operation_count: 39
  slug: langgraph-agentic-access
  summary_line: 39 operations · 20 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.host.langchain.com
  baseurl_source: declared
  description: The Agent Connections (v2) API from LangGraph — 2 operation(s) for agent connections (v2).
  name: LangGraph Agent Connections (v2) API
  slug: langgraph-agent-connections-v2-api
- baseURL: https://api.host.langchain.com
  baseurl_source: declared
  description: The Auth Service (v2) API from LangGraph — 13 operation(s) for auth service (v2).
  name: LangGraph Auth Service (v2) API
  slug: langgraph-auth-service-v2-api
- baseURL: https://api.host.langchain.com
  baseurl_source: declared
  description: The Deployments (v2) API from LangGraph — 5 operation(s) for deployments (v2).
  name: LangGraph Deployments (v2) API
  slug: langgraph-deployments-v2-api
- baseURL: https://api.host.langchain.com
  baseurl_source: declared
  description: The Integrations (v1) API from LangGraph — 4 operation(s) for integrations (v1).
  name: LangGraph Integrations (v1) API
  slug: langgraph-integrations-v1-api
- baseURL: https://api.host.langchain.com
  baseurl_source: declared
  description: The Listeners (v2) API from LangGraph — 2 operation(s) for listeners (v2).
  name: LangGraph Listeners (v2) API
  slug: langgraph-listeners-v2-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LangSmith Deployment Control Plane Agent Connections (v2) Agent Connections (v2) Agent Connections (v2) API
  slug: open-langgraph-agent-connections-v2-api
- collection_type: open
  name: LangSmith Deployment Control Plane Agent Connections (v2) Agent Connections (v2) Auth Service (v2) API
  slug: open-langgraph-auth-service-v2-api
- collection_type: open
  name: LangSmith Deployment Control Plane Agent Connections (v2) Agent Connections (v2) Deployments (v2) API
  slug: open-langgraph-deployments-v2-api
- collection_type: open
  name: LangSmith Deployment Control Plane Agent Connections (v2) Agent Connections (v2) Integrations (v1) API
  slug: open-langgraph-integrations-v1-api
- collection_type: open
  name: LangSmith Deployment Control Plane Agent Connections (v2) Agent Connections (v2) Listeners (v2) API
  slug: open-langgraph-listeners-v2-api
- collection_type: open
  name: LangSmith Deployment Control Plane API
  slug: open-langgraph
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/langchain-ai/langgraph/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/langchain-ai/langgraph/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/langchain-ai/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/langchain-ai/.github/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/langchain-ai/langgraph/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/langgraph-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langgraph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/langgraph-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.langchain.com/langgraph
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langchain.com/langgraph-platform
- group: build
  title: ''
  type: GitHub
  url: https://github.com/langchain-ai/langgraph
- group: other
  title: ''
  type: ParentCompany
  url: https://www.langchain.com/
- group: company
  title: ''
  type: Blog
  url: https://www.langchain.com/blog/rss.xml
created: '2026-01-02'
description: LangGraph is an open-source framework from LangChain for building stateful, multi-actor agent workflows with low-level primitives for greater control over agent behavior. LangGraph Platform (LangSmith Deployment) provides managed infrastructure for running agents in production with assistants, threads, and runs.
finops:
- name: Langgraph Finops
  service_category: API
  slug: langgraph-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/langgraph.png
layout: provider
modified: '2026-05-19'
name: LangGraph
nav: Providers
network: true
overview: 'LangGraph publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agent Connections (v2) API, Auth Service (v2) API, Deployments (v2) API, and 2 more. Tagged areas include Agents, Artificial Intelligence, Large Language Models, Workflows, and Orchestration.


  LangGraph''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Langgraph Plans Pricing
  plan_count: 3
  slug: langgraph-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Langgraph Rate Limits
  slug: langgraph-rate-limits
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 59.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 65.0
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/langgraph/refs/heads/main/screenshots/langgraph-2026-06-20T184305.png
security:
- kind: authentication
  name: Langgraph Authentication
  slug: langgraph-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Langgraph Domain Security
  slug: langgraph-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: langgraph
tags:
- Agents
- Artificial Intelligence
- Large Language Models
- Workflows
- Orchestration
website: https://www.langchain.com/langgraph
---

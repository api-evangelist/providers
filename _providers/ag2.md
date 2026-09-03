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
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: Core open-source Python library for building agentic AI applications. Provides ConversableAgent, AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager, tool/function registration, code execution
  name: AG2 Python Framework
  slug: python-framework
- description: Visual interface for building, configuring, and running AG2 agents and multi-agent workflows. Distributed as the ag2studio Python package and open source on GitHub.
  name: AG2 Studio
  slug: studio
- description: Official collection of sample applications, notebooks, and reference integrations for AG2, including a packaged AutoGen Studio sample app.
  name: Build with AG2 Samples
  slug: build-with-ag2
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ag2ai/ag2/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ag2ai/ag2/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/ag2ai/ag2/blob/main/.github/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ag2ai/ag2/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/ag2ai/ag2/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ag2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ag2.ai
- group: start
  title: ''
  type: Portal
  url: https://docs.ag2.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ag2.ai/latest/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ag2ai
- group: other
  title: ''
  type: Repository
  url: https://github.com/ag2ai/ag2
- group: company
  title: ''
  type: Blog
  url: https://docs.ag2.ai/latest/docs/blog/
- group: build
  title: ''
  type: Examples
  url: https://docs.ag2.ai/latest/docs/use-cases/notebooks/Notebooks/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/sNGSwQME3x
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ag2.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ag2.ai/privacy
created: '2026-05-23'
description: AG2 (formerly AutoGen) is an open-source multi-agent framework and AgentOS hosted by the AG2AI organization. It provides Python building blocks for ConversableAgent, GroupChat, GroupChatManager, RetrieveUserProxyAgent, function/tool use, code execution, and human-in-the-loop patterns. The ecosystem includes the core ag2 / autogen library, the AG2 Studio visual workflow builder, and the build-with-ag2 samples.
finops:
- name: Ag2 Finops
  service_category: API
  slug: ag2-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ag2.png
layout: provider
modified: '2026-05-23'
name: AG2
nav: Providers
network: true
overview: 'AG2 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Multi-Agent, AgentOS, AutoGen, and Python.


  AG2''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, code examples, and 11 more developer resources.'
plans:
- name: Ag2 Plans Pricing
  plan_count: 1
  slug: ag2-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Ag2 Rate Limits
  slug: ag2-rate-limits
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 50.0
  previous_composite: 31.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ag2/refs/heads/main/screenshots/ag2-2026-06-20T165746.png
security:
- kind: domain-security
  name: Ag2 Domain Security
  slug: ag2-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ag2
tags:
- AI Agents
- Multi-Agent
- AgentOS
- AutoGen
- Python
- Open-Source
- LLM
- Group Chat
- Tool Use
- Human-in-the-Loop
website: https://ag2.ai
---

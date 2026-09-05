---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Klavis Agentic Access
  operation_count: 5
  slug: klavis-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The Klavis API manages hosted MCP servers, OAuth flows for 50+ integrated services, Strata multi-tool servers, and live sandbox environments. Endpoints cover MCP server CRUD and tool invocation, sandb
  name: Klavis MCP Platform API
  slug: mcp-platform
- baseURL: https://api.klavis.ai
  baseurl_source: declared
  description: Create and manage hosted MCP server instances
  name: Klavis AI MCP Servers API
  slug: klavis-mcp-servers-api
- baseURL: https://api.klavis.ai
  baseurl_source: declared
  description: Acquire and manage isolated sandbox VMs
  name: Klavis AI Sandbox API
  slug: klavis-sandbox-api
- baseURL: https://api.klavis.ai
  baseurl_source: declared
  description: List and invoke MCP server tools
  name: Klavis AI Tools API
  slug: klavis-tools-api
- baseURL: https://api.klavis.ai
  baseurl_source: declared
  description: End-user metadata for agent integrations
  name: Klavis AI Users API
  slug: klavis-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Klavis AI MCP Platform MCP Servers API
  slug: open-klavis-mcp-servers-api
- collection_type: open
  name: Klavis AI MCP Platform MCP Servers Sandbox API
  slug: open-klavis-sandbox-api
- collection_type: open
  name: Klavis AI MCP Platform MCP Servers Tools API
  slug: open-klavis-tools-api
- collection_type: open
  name: Klavis AI MCP Platform MCP Servers Users API
  slug: open-klavis-users-api
- collection_type: open
  name: Klavis AI MCP Platform API
  slug: open-klavis
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Klavis-AI/klavis/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Klavis-AI/klavis/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Klavis-AI/klavis/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Klavis-AI/klavis/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/klavis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klavis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klavis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.klavis.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.klavis.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.klavis.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Klavis-AI
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Klavis-AI/klavis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.klavis.ai/pricing
- group: operate
  title: ''
  type: Contact
  url: https://www.klavis.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klavis.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klavis.ai/privacy
created: '2026-05-23'
description: Klavis AI is an open-source MCP integration platform that lets AI agents reliably use external tools at production scale. The product line is organized around Strata (intelligent connectors that compress and route tool context), 100+ prebuilt MCP integrations with OAuth, and an MCP Sandbox for live agent training and evaluation. Target customers are AI agent companies, RL teams, and enterprises that need long-horizon multi-app environments with seeded state, resets, and verifiable outcomes, plus SOC 2 Type II and GDPR posture. SDKs are available for Python and TypeScript/JavaScript, integrations cover Claude, OpenAI, Gemini, Cohere, Mistral, LangChain/LangGraph, LlamaIndex, CrewAI, Mastra, Agno, Fireworks, Together, and Google ADK, and the project is Apache-2.0 on GitHub.
finops:
- name: Klavis Finops
  service_category: API
  slug: klavis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klavis.png
layout: provider
modified: '2026-05-23'
name: Klavis AI
nav: Providers
network: true
overview: 'Klavis AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including MCP Servers API, Sandbox API, Tools API, and 1 more. Tagged areas include MCP, MCP Servers, MCP Hosting, Connectors, and Authentication.


  Klavis AI''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Klavis Plans Pricing
  plan_count: 1
  slug: klavis-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Klavis Rate Limits
  slug: klavis-rate-limits
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 57.7
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 50.0
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klavis/refs/heads/main/screenshots/klavis-2026-06-20T184058.png
security:
- kind: authentication
  name: Klavis Authentication
  slug: klavis-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Klavis Domain Security
  slug: klavis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klavis
tags:
- MCP
- MCP Servers
- MCP Hosting
- Connectors
- Authentication
- Sandboxes
- Agent Training
- Reinforcement Learning
- White Label
- Open-Source
- Strata
website: https://www.klavis.ai
---

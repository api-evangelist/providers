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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The health API from Taste — 2 operation(s) for health.
  name: Taste health API
  slug: taste-health-api
- description: The Prompt Enhancement API from Taste — 2 operation(s) for prompt enhancement.
  name: Taste Prompt Enhancement API
  slug: taste-prompt-enhancement-api
- description: The Taste Engine API API from Taste — 1 operation(s) for taste engine api.
  name: Taste Taste Engine API API
  slug: taste-taste-engine-api-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taste-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tastelabs.com/
- group: company
  title: ''
  type: Blog
  url: https://tastelabs.com/blog
- group: auth
  title: ''
  type: Authentication
  url: authentication/taste-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taste-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taste-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taste-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/taste-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taste-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/taste-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taste-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taste-lifecycle.yml
created: '2026-07-17'
description: Taste Labs is a San Francisco research lab and infrastructure company building "the taste layer for AI" — decoding subjective design domains to end AI slop. Its Taste Engine API extracts brand and design guidelines from a reference site or a prior submission and enhances website and slide-deck prompts so AI generation stays on-brand, returning an enhanced prompt plus structured brand context and reasoning. The company is backed by CRV and Amplify Partners and runs the TasteMakers community program. This profile was enriched from the provider's live public surface, including the Taste Engine API OpenAPI.
image: https://cdn.prod.website-files.com/6a1d5baf94efef5f7c435fc3/6a306ae79b1ce1b28e27e16b_taste_Logo.png
layout: provider
mcp_servers:
- description: ''
  name: taste-mcp.yml
  slug: taste-mcpyml
modified: '2026-07-21'
name: Taste
nav: Providers
network: true
overview: 'Taste publishes 3 APIs on the [APIs.io](https://apis.io/) network: health API, Prompt Enhancement API, and Taste Engine API API. Tagged areas include Company, Ai, Design, Machine Learning, and Developer Tools.


  Taste''s developer surface includes engineering blog, authentication, and 11 more developer resources.'
random_paper: 35
score:
  band: emerging
  composite: 27.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 47.8
    developer_ergonomics: 28.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Taste Authentication
  slug: taste-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taste Domain Security
  slug: taste-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taste
tags:
- Company
- Ai
- Design
- Machine Learning
- Developer Tools
- Prompt Engineering
- Content Generation
website: https://tastelabs.com/
---

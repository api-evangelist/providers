---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Deterministic INR pricing for a freelance or agency project scope. POST /api/v1/project-quote; validates its input and returns a structured quote.
  name: Scopewise Project Quote API
  slug: scopewise-project-quote-api
- description: Generates follow-up on an overdue invoice. POST /api/v1/overdue-invoice-follow-up. Shares the same OpenAPI document and base URL as the quote API.
  name: Scopewise Overdue Invoice Follow-up API
  slug: scopewise-overdue-invoice-follow-up-api
artifact_total: 2
common:
- group: other
  title: ''
  type: APIsJSON
  url: well-known/youworkagent-provider-apis.json
- group: other
  title: ''
  type: APICatalog
  url: well-known/youworkagent-api-catalog.json
- group: start
  title: ''
  type: Onboarding
  url: well-known/youworkagent-api-onboarding.json
- group: other
  title: ''
  type: AgentCard
  url: a2a/youworkagent-agent-card.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/youworkagent-agent-skills.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/youworkagent-llms.txt
- group: company
  title: ''
  type: Website
  url: https://youworkagent.online
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scopewise.youworkagent.online/api-docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scopewise.youworkagent.online/privacy
created: '2026-08-23'
description: 'YouWork Agent publishes Scopewise, a deterministic commercial API for Indian freelancers and agencies: a project-quote endpoint that prices a scope of work in INR, and an overdue-invoice follow-up endpoint. The contract is an OpenAPI 3.1 document of two operations and four schemas served from scopewise.youworkagent.online. The provider is unusually agent-native for its size — alongside the specification it serves an A2A agent card, a declared agent-skills index, an RFC 9727 api-catalog (as application/linkset+json carrying the RFC profile parameter), a machine- readable API onboarding document, and an llms.txt.'
image: https://scopewise.youworkagent.online/scopewise-logo-512.png
layout: provider
modified: '2026-08-23'
name: YouWork Agent
nav: Providers
network: true
overview: 'YouWork Agent publishes 2 APIs on the [APIs.io](https://apis.io/) network: Scopewise Project Quote API and Scopewise Overdue Invoice Follow-up API. Tagged areas include Freelance, Project Pricing, Invoicing, Business, and Agents.'
random_paper: 4
score:
  band: thin
  composite: 27.4
  delta: 1.9
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
slug: youworkagent
tags:
- Freelance
- Project Pricing
- Invoicing
- Business
- Agents
- Agent Commerce
- India
website: https://youworkagent.online
---

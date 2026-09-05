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
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://scopewise.youworkagent.online/api/v1
  baseurl_source: declared
  description: The Overdue Invoice Follow Up API from YouWork Agent — 1 operation(s) for overdue invoice follow up.
  name: YouWork Agent Overdue Invoice Follow Up API
  slug: youworkagent-overdue-invoice-follow-up-api
- baseURL: https://scopewise.youworkagent.online/api/v1
  baseurl_source: declared
  description: The Project Quote API from YouWork Agent — 1 operation(s) for project quote.
  name: YouWork Agent Project Quote API
  slug: youworkagent-project-quote-api
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
overview: 'YouWork Agent publishes 2 APIs on the [APIs.io](https://apis.io/) network: Overdue Invoice Follow Up API and Project Quote API. Tagged areas include Freelance, Project Pricing, INR, Business, and Deterministic API.'
random_paper: 4
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
slug: youworkagent
tags:
- Freelance
- Project Pricing
- INR
- Business
- Deterministic API
- Agent API
website: https://youworkagent.online
---

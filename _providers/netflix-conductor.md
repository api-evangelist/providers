---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Netflix Conductor Agentic Access
  operation_count: 26
  slug: netflix-conductor-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: The Events API from Netflix Conductor — 1 operation(s) for events.
  name: Netflix Conductor Events API
  slug: netflix-conductor-events-api
- description: The Metadata API from Netflix Conductor — 4 operation(s) for metadata.
  name: Netflix Conductor Metadata API
  slug: netflix-conductor-metadata-api
- description: The Tasks API from Netflix Conductor — 5 operation(s) for tasks.
  name: Netflix Conductor Tasks API
  slug: netflix-conductor-tasks-api
- description: The Workflow API from Netflix Conductor — 9 operation(s) for workflow.
  name: Netflix Conductor Workflow API
  slug: netflix-conductor-workflow-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Netflix Conductor REST API
  slug: open-conductor-api
- collection_type: open
  name: Netflix Conductor REST Events API
  slug: open-netflix-conductor-events-api
- collection_type: open
  name: Netflix Conductor REST Events Metadata API
  slug: open-netflix-conductor-metadata-api
- collection_type: open
  name: Netflix Conductor REST Events Tasks API
  slug: open-netflix-conductor-tasks-api
- collection_type: open
  name: Netflix Conductor REST Events Workflow API
  slug: open-netflix-conductor-workflow-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netflix-conductor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netflix-conductor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conductor-oss.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conductor-oss.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.conductor-oss.org/getting-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/conductor-oss/conductor
- group: company
  title: ''
  type: Blog
  url: https://conductor-oss.org/blog
created: '2026-03-26'
description: Conductor is a microservices orchestration platform originally created by Netflix, providing a workflow engine for coordinating and managing complex distributed processes across multiple services with built-in retries, error handling, and observability.
finops:
- name: Netflix Conductor Finops
  service_category: API
  slug: netflix-conductor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netflix-conductor.png
layout: provider
modified: '2026-05-19'
name: Netflix Conductor
nav: Providers
network: true
overview: 'Netflix Conductor publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events API, Metadata API, Tasks API, and 1 more. Tagged areas include Event-Driven, Microservices, Netflix, Open-Source, and Orchestration.


  Netflix Conductor''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, and 3 more developer resources.'
plans:
- name: Netflix Conductor Plans Pricing
  plan_count: 3
  slug: netflix-conductor-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Netflix Conductor Rate Limits
  slug: netflix-conductor-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.2
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netflix-conductor/refs/heads/main/screenshots/netflix-conductor-2026-06-20T190151.png
security:
- kind: domain-security
  name: Netflix Conductor Domain Security
  slug: netflix-conductor-domain-security
  summary_line: TLSv1.3
slug: netflix-conductor
tags:
- Event-Driven
- Microservices
- Netflix
- Open-Source
- Orchestration
- Workflows
website: https://conductor-oss.org/
---

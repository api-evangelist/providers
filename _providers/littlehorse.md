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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Littlehorse Agentic Access
  operation_count: 22
  slug: littlehorse-agentic-access
  summary_line: 22 operations · 12 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The External Events API from LittleHorse — 3 operation(s) for external events.
  name: LittleHorse External Events API
  slug: littlehorse-external-events-api
- description: The Node Runs API from LittleHorse — 1 operation(s) for node runs.
  name: LittleHorse Node Runs API
  slug: littlehorse-node-runs-api
- description: The Task Definitions API from LittleHorse — 2 operation(s) for task definitions.
  name: LittleHorse Task Definitions API
  slug: littlehorse-task-definitions-api
- description: The User Tasks API from LittleHorse — 3 operation(s) for user tasks.
  name: LittleHorse User Tasks API
  slug: littlehorse-user-tasks-api
- description: The Workflow Runs API from LittleHorse — 5 operation(s) for workflow runs.
  name: LittleHorse Workflow Runs API
  slug: littlehorse-workflow-runs-api
- description: The Workflow Specs API from LittleHorse — 2 operation(s) for workflow specs.
  name: LittleHorse Workflow Specs API
  slug: littlehorse-workflow-specs-api
artifact_total: 12
collections:
- collection_type: open
  name: LittleHorse REST API
  slug: open-littlehorse-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/littlehorse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/littlehorse-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/littlehorse-enterprises
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/littlehorse
- group: company
  title: ''
  type: Website
  url: https://littlehorse.dev/
- group: company
  title: ''
  type: Blog
  url: https://littlehorse.dev/blog/rss.xml
created: '2026-03-26'
description: LittleHorse is an open source workflow engine for orchestrating distributed systems with support for Java, Go, Python, and .NET.
finops:
- name: Littlehorse Finops
  service_category: API
  slug: littlehorse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/littlehorse.png
layout: provider
modified: '2026-05-19'
name: LittleHorse
nav: Providers
network: true
overview: 'LittleHorse publishes 6 APIs on the [APIs.io](https://apis.io/) network, including External Events API, Node Runs API, Task Definitions API, and 3 more. Tagged areas include Microservices.


  LittleHorse''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Littlehorse Plans Pricing
  plan_count: 3
  slug: littlehorse-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Littlehorse Rate Limits
  slug: littlehorse-rate-limits
score:
  band: thin
  composite: 30.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.7
    developer_ergonomics: 2.2
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/littlehorse/refs/heads/main/screenshots/littlehorse-2026-06-20T184611.png
security:
- kind: domain-security
  name: Littlehorse Domain Security
  slug: littlehorse-domain-security
  summary_line: TLSv1.3 · HSTS
slug: littlehorse
tags:
- Microservices
website: https://littlehorse.dev/
---

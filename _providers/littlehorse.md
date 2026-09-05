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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Littlehorse Agentic Access
  operation_count: 22
  slug: littlehorse-agentic-access
  summary_line: 22 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The External Events API from LittleHorse — 3 operation(s) for external events.
  name: LittleHorse External Events API
  slug: littlehorse-external-events-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The Node Runs API from LittleHorse — 1 operation(s) for node runs.
  name: LittleHorse Node Runs API
  slug: littlehorse-node-runs-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The Task Definitions API from LittleHorse — 2 operation(s) for task definitions.
  name: LittleHorse Task Definitions API
  slug: littlehorse-task-definitions-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The User Tasks API from LittleHorse — 3 operation(s) for user tasks.
  name: LittleHorse User Tasks API
  slug: littlehorse-user-tasks-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The Workflow Runs API from LittleHorse — 5 operation(s) for workflow runs.
  name: LittleHorse Workflow Runs API
  slug: littlehorse-workflow-runs-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The Workflow Specs API from LittleHorse — 2 operation(s) for workflow specs.
  name: LittleHorse Workflow Specs API
  slug: littlehorse-workflow-specs-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LittleHorse REST API
  slug: open-littlehorse-api
- collection_type: open
  name: LittleHorse REST External Events API
  slug: open-littlehorse-external-events-api
- collection_type: open
  name: LittleHorse REST External Events Node Runs API
  slug: open-littlehorse-node-runs-api
- collection_type: open
  name: LittleHorse REST External Events Task Definitions API
  slug: open-littlehorse-task-definitions-api
- collection_type: open
  name: LittleHorse REST External Events User Tasks API
  slug: open-littlehorse-user-tasks-api
- collection_type: open
  name: LittleHorse REST External Events Workflow Runs API
  slug: open-littlehorse-workflow-runs-api
- collection_type: open
  name: LittleHorse REST External Events Workflow Specs API
  slug: open-littlehorse-workflow-specs-api
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
random_paper: 2
rate_limits:
- limit_count: 5
  name: Littlehorse Rate Limits
  slug: littlehorse-rate-limits
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.3
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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

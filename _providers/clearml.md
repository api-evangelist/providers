---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 34
  human_in_the_loop: 3
  name: Clearml Agentic Access
  operation_count: 34
  slug: clearml-agentic-access
  summary_line: 34 operations · 34 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: 'The ClearML REST API is organized into services: auth (login/credentials), projects, tasks (experiments), workers, models, queues, events, pipelines, and reports. Authentication uses access/secret-key'
  name: ClearML REST API
  slug: clearml-rest-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Auth API from ClearML — 5 operation(s) for auth.
  name: ClearML Auth API
  slug: clearml-auth-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Debug API from ClearML — 1 operation(s) for debug.
  name: ClearML Debug API
  slug: clearml-debug-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Events API from ClearML — 4 operation(s) for events.
  name: ClearML Events API
  slug: clearml-events-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Models API from ClearML — 4 operation(s) for models.
  name: ClearML Models API
  slug: clearml-models-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Projects API from ClearML — 2 operation(s) for projects.
  name: ClearML Projects API
  slug: clearml-projects-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Queues API from ClearML — 2 operation(s) for queues.
  name: ClearML Queues API
  slug: clearml-queues-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Tasks API from ClearML — 15 operation(s) for tasks.
  name: ClearML Tasks API
  slug: clearml-tasks-api
- baseURL: https://api.clear.ml
  baseurl_source: declared
  description: The Workers API from ClearML — 1 operation(s) for workers.
  name: ClearML Workers API
  slug: clearml-workers-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClearML REST Auth API
  slug: open-clearml-auth-api
- collection_type: open
  name: ClearML REST Auth Debug API
  slug: open-clearml-debug-api
- collection_type: open
  name: ClearML REST Auth Events API
  slug: open-clearml-events-api
- collection_type: open
  name: ClearML REST Auth Models API
  slug: open-clearml-models-api
- collection_type: open
  name: ClearML REST Auth Projects API
  slug: open-clearml-projects-api
- collection_type: open
  name: ClearML REST Auth Queues API
  slug: open-clearml-queues-api
- collection_type: open
  name: ClearML REST Auth Tasks API
  slug: open-clearml-tasks-api
- collection_type: open
  name: ClearML REST Auth Workers API
  slug: open-clearml-workers-api
- collection_type: open
  name: ClearML REST API
  slug: open-clearml
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/clearml/clearml-server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/clearml/clearml-server/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clearml-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearml-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearml-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clearml-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearml
- group: company
  title: ''
  type: Website
  url: https://clear.ml/
- group: start
  title: ''
  type: Portal
  url: https://clear.ml/docs/latest/docs/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/clearml/clearml-server
- group: commercial
  title: ''
  type: Pricing
  url: https://clear.ml/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/clearml-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clearml-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clearml-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://clear.ml/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://clear.ml/feed/
created: '2026-05-08'
description: ClearML is an open-source MLOps platform with experiment tracking, datasets, model serving, and orchestration. The ClearML Server exposes a versioned REST API split across services (auth, projects, tasks, workers, models, queues, events, pipelines).
finops:
- name: Clearml Finops
  service_category: ML
  slug: clearml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearml.png
layout: provider
modified: '2026-05-08'
name: ClearML
nav: Providers
network: true
overview: 'ClearML publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Debug API, Events API, and 5 more. Tagged areas include ML, MLOps, Open-Source, Experiment Tracking, and Orchestration.


  ClearML''s developer surface includes authentication, developer portal, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Clearml Plans Pricing
  plan_count: 1
  slug: clearml-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Clearml Rate Limits
  slug: clearml-rate-limits
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearml/refs/heads/main/screenshots/clearml-2026-06-20T174458.png
security:
- kind: authentication
  name: Clearml Authentication
  slug: clearml-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Clearml Domain Security
  slug: clearml-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clearml Vulnerability Disclosure
  slug: clearml-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clearml
tags:
- ML
- MLOps
- Open-Source
- Experiment Tracking
- Orchestration
website: https://clear.ml/
---

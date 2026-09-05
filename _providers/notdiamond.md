---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Notdiamond Agentic Access
  operation_count: 6
  slug: notdiamond-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Custom Routers API from Not Diamond — 2 operation(s) for custom routers.
  name: Not Diamond Custom Routers API
  slug: notdiamond-custom-routers-api
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Feedback API from Not Diamond — 2 operation(s) for feedback.
  name: Not Diamond Feedback API
  slug: notdiamond-feedback-api
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Model Routing API from Not Diamond — 1 operation(s) for model routing.
  name: Not Diamond Model Routing API
  slug: notdiamond-model-routing-api
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Models API from Not Diamond — 1 operation(s) for models.
  name: Not Diamond Models API
  slug: notdiamond-models-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Not Diamond Custom Routers API
  slug: open-notdiamond-custom-routers-api
- collection_type: open
  name: Not Diamond Custom Routers Feedback API
  slug: open-notdiamond-feedback-api
- collection_type: open
  name: Not Diamond Custom Routers Model Routing API
  slug: open-notdiamond-model-routing-api
- collection_type: open
  name: Not Diamond Custom Routers Models API
  slug: open-notdiamond-models-api
- collection_type: open
  name: Not Diamond API
  slug: open-notdiamond
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/notdiamond-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notdiamond-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notdiamond-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.notdiamond.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Not-Diamond
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/not-diamond
- group: company
  title: ''
  type: Website
  url: https://www.notdiamond.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.notdiamond.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/notdiamond-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/notdiamond-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/notdiamond-finops.yml
created: '2026-06-20'
description: Not Diamond is an AI model router that determines the best LLM to call for any given prompt. Its REST API routes each request to the optimal model across providers based on quality, cost, and latency tradeoffs, accepts real-time feedback to personalize routing, and can train custom routers from evaluation datasets.
finops:
- name: Notdiamond Finops
  service_category: AI and Machine Learning
  slug: notdiamond-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/notdiamond.png
layout: provider
modified: '2026-06-20'
name: Not Diamond
nav: Providers
network: true
overview: 'Not Diamond publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Custom Routers API, Feedback API, Model Routing API, and 1 more. Tagged areas include Artificial Intelligence, LLM, Model Routing, Router, and Orchestration.


  Not Diamond''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Notdiamond Plans Pricing
  plan_count: 2
  slug: notdiamond-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Notdiamond Rate Limits
  slug: notdiamond-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/notdiamond/refs/heads/main/screenshots/notdiamond-2026-06-20T190525.png
security:
- kind: authentication
  name: Notdiamond Authentication
  slug: notdiamond-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Notdiamond Domain Security
  slug: notdiamond-domain-security
  summary_line: TLSv1.3 · HSTS
slug: notdiamond
tags:
- Artificial Intelligence
- LLM
- Model Routing
- Router
- Orchestration
website: https://www.notdiamond.ai
---

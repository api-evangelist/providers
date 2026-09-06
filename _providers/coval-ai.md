---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Coval Ai Agentic Access
  operation_count: 80
  slug: coval-ai-agentic-access
  summary_line: 80 operations · 43 acting
api_count: 1
apis:
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Connect and manage AI agents under test.
  name: Coval Agents API
  slug: coval-ai-agents-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Submit and evaluate production conversations.
  name: Coval Conversations API
  slug: coval-ai-conversations-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Define scoring criteria, thresholds, and baselines.
  name: Coval Metrics API
  slug: coval-ai-metrics-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Manage agent configuration variants (mutations).
  name: Coval Mutations API
  slug: coval-ai-mutations-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Configure simulated callers, voices, and scenario behavior.
  name: Coval Personas API
  slug: coval-ai-personas-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Create and manage evaluation reports.
  name: Coval Reports API
  slug: coval-ai-reports-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Save reusable run configurations.
  name: Coval Run Templates API
  slug: coval-ai-run-templates-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Launch and manage simulation runs.
  name: Coval Runs API
  slug: coval-ai-runs-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Schedule recurring simulation runs.
  name: Coval Scheduled Runs API
  slug: coval-ai-scheduled-runs-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Inspect individual simulation results.
  name: Coval Simulations API
  slug: coval-ai-simulations-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Manage individual evaluation inputs within a test set.
  name: Coval Test Cases API
  slug: coval-ai-test-cases-api
- baseURL: https://api.coval.dev/v1
  baseurl_source: declared
  description: Manage collections of test cases (datasets).
  name: Coval Test Sets API
  slug: coval-ai-test-sets-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coval Agents API
  slug: open-coval-ai-agents-api
- collection_type: open
  name: Coval Agents Conversations API
  slug: open-coval-ai-conversations-api
- collection_type: open
  name: Coval Agents Metrics API
  slug: open-coval-ai-metrics-api
- collection_type: open
  name: Coval Agents Mutations API
  slug: open-coval-ai-mutations-api
- collection_type: open
  name: Coval Agents Personas API
  slug: open-coval-ai-personas-api
- collection_type: open
  name: Coval Agents Reports API
  slug: open-coval-ai-reports-api
- collection_type: open
  name: Coval Agents Run Templates API
  slug: open-coval-ai-run-templates-api
- collection_type: open
  name: Coval Agents Runs API
  slug: open-coval-ai-runs-api
- collection_type: open
  name: Coval Agents Scheduled Runs API
  slug: open-coval-ai-scheduled-runs-api
- collection_type: open
  name: Coval Agents Simulations API
  slug: open-coval-ai-simulations-api
- collection_type: open
  name: Coval Agents Test Cases API
  slug: open-coval-ai-test-cases-api
- collection_type: open
  name: Coval Agents Test Sets API
  slug: open-coval-ai-test-sets-api
- collection_type: open
  name: Coval API
  slug: open-coval-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coval-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coval-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coval-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coval-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/covaldev
- group: company
  title: ''
  type: Website
  url: https://www.coval.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coval.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/coval-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coval-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coval-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.coval.ai/blog
created: '2026-06-21'
description: Coval is a simulation and evaluation platform for AI voice and chat agents. Inspired by autonomous-vehicle testing, it simulates end customers across realistic scenarios, personas, accents, and background noise, then scores agent behavior with built-in and custom metrics. The REST API manages agents, test sets and test cases, personas, metrics, simulation runs, and production conversations.
finops:
- name: Coval Ai Finops
  service_category: AI and Machine Learning
  slug: coval-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coval-ai.png
layout: provider
modified: '2026-06-21'
name: Coval
nav: Providers
network: true
overview: 'Coval publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Conversations API, Metrics API, and 9 more. Tagged areas include Artificial Intelligence, Agents, Voice AI, Simulation, and Evaluation.


  Coval''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Coval Ai Plans Pricing
  plan_count: 2
  slug: coval-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Coval Ai Rate Limits
  slug: coval-ai-rate-limits
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coval-ai/refs/heads/main/screenshots/coval-ai-2026-07-25T210547.png
security:
- kind: authentication
  name: Coval Ai Authentication
  slug: coval-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coval Ai Domain Security
  slug: coval-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coval-ai
tags:
- Artificial Intelligence
- Agents
- Voice AI
- Simulation
- Evaluation
- Testing
website: https://www.coval.dev
---

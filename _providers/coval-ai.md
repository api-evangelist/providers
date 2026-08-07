---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Coval Ai Agentic Access
  operation_count: 80
  slug: coval-ai-agentic-access
  summary_line: 80 operations · 43 acting
api_count: 12
apis:
- description: Connect and manage AI agents under test.
  name: Coval Agents API
  slug: coval-ai-agents-api
- description: Submit and evaluate production conversations.
  name: Coval Conversations API
  slug: coval-ai-conversations-api
- description: Define scoring criteria, thresholds, and baselines.
  name: Coval Metrics API
  slug: coval-ai-metrics-api
- description: Manage agent configuration variants (mutations).
  name: Coval Mutations API
  slug: coval-ai-mutations-api
- description: Configure simulated callers, voices, and scenario behavior.
  name: Coval Personas API
  slug: coval-ai-personas-api
- description: Create and manage evaluation reports.
  name: Coval Reports API
  slug: coval-ai-reports-api
- description: Save reusable run configurations.
  name: Coval Run Templates API
  slug: coval-ai-run-templates-api
- description: Launch and manage simulation runs.
  name: Coval Runs API
  slug: coval-ai-runs-api
- description: Schedule recurring simulation runs.
  name: Coval Scheduled Runs API
  slug: coval-ai-scheduled-runs-api
- description: Inspect individual simulation results.
  name: Coval Simulations API
  slug: coval-ai-simulations-api
- description: Manage individual evaluation inputs within a test set.
  name: Coval Test Cases API
  slug: coval-ai-test-cases-api
- description: Manage collections of test cases (datasets).
  name: Coval Test Sets API
  slug: coval-ai-test-sets-api
artifact_total: 19
collections:
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
overview: 'Coval publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Conversations API, Metrics API, and 9 more. Tagged areas include AI, Agents, Voice AI, Simulation, and Evaluation.


  Coval''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Coval Ai Plans Pricing
  plan_count: 2
  slug: coval-ai-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 3
  name: Coval Ai Rate Limits
  slug: coval-ai-rate-limits
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
- AI
- Agents
- Voice AI
- Simulation
- Evaluation
- Testing
website: https://www.coval.dev
---

---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 2
  name: Toloka Agentic Access
  operation_count: 39
  slug: toloka-agentic-access
  summary_line: 39 operations · 20 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: Retrieve Toloker responses and accept or reject completed assignments.
  name: Toloka Assignments API
  slug: toloka-assignments-api
- description: Retrieve files Tolokers attached to their assignments.
  name: Toloka Attachments API
  slug: toloka-attachments-api
- description: Track the status of asynchronous operations.
  name: Toloka Operations API
  slug: toloka-operations-api
- description: Create, configure, open, and close pools of tasks for Tolokers.
  name: Toloka Pools API
  slug: toloka-pools-api
- description: Create and manage projects that define task interface and instructions.
  name: Toloka Projects API
  slug: toloka-projects-api
- description: Create and manage skills assigned to Tolokers.
  name: Toloka Skills API
  slug: toloka-skills-api
- description: Upload and retrieve task suites (groups of tasks shown together).
  name: Toloka Task Suites API
  slug: toloka-task-suites-api
- description: Upload and retrieve individual tasks.
  name: Toloka Tasks API
  slug: toloka-tasks-api
- description: Create and manage training pools used to qualify Tolokers.
  name: Toloka Training API
  slug: toloka-training-api
- description: Issue bonus payments to Tolokers.
  name: Toloka User Bonuses API
  slug: toloka-user-bonuses-api
- description: Restrict Tolokers from a pool, project, or all projects.
  name: Toloka User Restrictions API
  slug: toloka-user-restrictions-api
- description: Subscribe to platform events delivered to your endpoint.
  name: Toloka Webhook Subscriptions API
  slug: toloka-webhook-subscriptions-api
artifact_total: 20
collections:
- collection_type: open
  name: Toloka API
  slug: open-toloka
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toloka-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/toloka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toloka-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toloka-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Toloka
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toloka
- group: company
  title: ''
  type: Website
  url: https://toloka.ai
- group: docs
  title: ''
  type: Documentation
  url: https://toloka.ai/docs/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/toloka-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/toloka-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/toloka-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://toloka.ai/blog
created: '2026-06-21'
description: Toloka is a data-labeling and human-data platform that powers human-in-the-loop pipelines for training and evaluating AI. The Toloka API lets requesters programmatically create projects, configure pools of crowdsourced tasks, upload tasks and task suites, collect and review Toloker responses, and track asynchronous operations, with a companion toloka-kit Python SDK.
finops:
- name: Toloka Finops
  service_category: AI and Machine Learning
  slug: toloka-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toloka.png
layout: provider
modified: '2026-06-21'
name: Toloka
nav: Providers
network: true
overview: 'Toloka publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Attachments API, Operations API, and 9 more. Tagged areas include Data Labeling, Crowdsourcing, Human-in-the-Loop, Training Data, and AI.


  Toloka''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Toloka Plans Pricing
  plan_count: 2
  slug: toloka-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Toloka Rate Limits
  slug: toloka-rate-limits
score:
  band: thin
  composite: 35.2
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Toloka Authentication
  slug: toloka-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Toloka Domain Security
  slug: toloka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Toloka Vulnerability Disclosure
  slug: toloka-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: toloka
tags:
- Data Labeling
- Crowdsourcing
- Human-in-the-Loop
- Training Data
- AI
website: https://toloka.ai
---

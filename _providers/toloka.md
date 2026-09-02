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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 20
  human_in_the_loop: 2
  name: Toloka Agentic Access
  operation_count: 39
  slug: toloka-agentic-access
  summary_line: 39 operations · 20 acting · 2 human-in-the-loop
api_count: 1
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
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Toloka Assignments API
  slug: open-toloka-assignments-api
- collection_type: open
  name: Toloka Assignments Attachments API
  slug: open-toloka-attachments-api
- collection_type: open
  name: Toloka Assignments Operations API
  slug: open-toloka-operations-api
- collection_type: open
  name: Toloka Assignments Pools API
  slug: open-toloka-pools-api
- collection_type: open
  name: Toloka Assignments Projects API
  slug: open-toloka-projects-api
- collection_type: open
  name: Toloka Assignments Skills API
  slug: open-toloka-skills-api
- collection_type: open
  name: Toloka Assignments Task Suites API
  slug: open-toloka-task-suites-api
- collection_type: open
  name: Toloka Assignments Tasks API
  slug: open-toloka-tasks-api
- collection_type: open
  name: Toloka Assignments Training API
  slug: open-toloka-training-api
- collection_type: open
  name: Toloka Assignments User Bonuses API
  slug: open-toloka-user-bonuses-api
- collection_type: open
  name: Toloka Assignments User Restrictions API
  slug: open-toloka-user-restrictions-api
- collection_type: open
  name: Toloka Assignments Webhook Subscriptions API
  slug: open-toloka-webhook-subscriptions-api
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
overview: 'Toloka publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Attachments API, Operations API, and 9 more. Tagged areas include Data Labeling, Crowdsourcing, Human-in-the-Loop, Training Data, and Artificial Intelligence.


  Toloka''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Toloka Plans Pricing
  plan_count: 2
  slug: toloka-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Toloka Rate Limits
  slug: toloka-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Artificial Intelligence
website: https://toloka.ai
---

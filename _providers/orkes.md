---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
- acting_count: 22
  human_in_the_loop: 1
  name: Orkes Agentic Access
  operation_count: 35
  slug: orkes-agentic-access
  summary_line: 35 operations · 22 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Authentication API from Orkes — 1 operation(s) for authentication.
  name: Orkes Authentication API
  slug: orkes-authentication-api
- description: The Human Tasks API from Orkes — 5 operation(s) for human tasks.
  name: Orkes Human Tasks API
  slug: orkes-human-tasks-api
- description: The Schedules API from Orkes — 4 operation(s) for schedules.
  name: Orkes Schedules API
  slug: orkes-schedules-api
- description: The Secrets API from Orkes — 2 operation(s) for secrets.
  name: Orkes Secrets API
  slug: orkes-secrets-api
- description: The Task Metadata API from Orkes — 2 operation(s) for task metadata.
  name: Orkes Task Metadata API
  slug: orkes-task-metadata-api
- description: The Tasks API from Orkes — 2 operation(s) for tasks.
  name: Orkes Tasks API
  slug: orkes-tasks-api
- description: The Workflow Execution API from Orkes — 7 operation(s) for workflow execution.
  name: Orkes Workflow Execution API
  slug: orkes-workflow-execution-api
- description: The Workflow Metadata API from Orkes — 2 operation(s) for workflow metadata.
  name: Orkes Workflow Metadata API
  slug: orkes-workflow-metadata-api
artifact_total: 17
collections:
- collection_type: open
  name: Orkes Conductor REST API
  slug: open-orkes-conductor-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orkes-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/orkes-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orkes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orkes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orkes-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orkes-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orkes-inc
- group: company
  title: ''
  type: Website
  url: https://orkes.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://orkes.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://orkes.io/blog
created: '2026-03-26'
description: Orkes is a modern workflow orchestration platform built on Netflix Conductor for orchestrating microservices, AI agents, and durable workflows.
finops:
- name: Orkes Finops
  service_category: API
  slug: orkes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orkes.png
layout: provider
modified: '2026-05-19'
name: Orkes
nav: Providers
network: true
overview: 'Orkes publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Human Tasks API, Schedules API, and 5 more. Tagged areas include Microservices.


  Orkes'' developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Orkes Plans Pricing
  plan_count: 3
  slug: orkes-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 5
  name: Orkes Rate Limits
  slug: orkes-rate-limits
score:
  band: thin
  composite: 36.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.1
    developer_ergonomics: 13.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orkes/refs/heads/main/screenshots/orkes-2026-06-20T191209.png
security:
- kind: authentication
  name: Orkes Authentication
  slug: orkes-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orkes Domain Security
  slug: orkes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orkes Vulnerability Disclosure
  slug: orkes-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Orkes Trust Center
  slug: orkes-trust-center
  summary_line: SOC 2
slug: orkes
tags:
- Microservices
website: https://orkes.io/
---

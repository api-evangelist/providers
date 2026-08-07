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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Flowable Api Agentic Access
  operation_count: 20
  slug: flowable-api-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 7
apis:
- description: 'Flowable also ships a packaged REST API webapp that exposes the Process Engine services over HTTP. The REST API covers process definitions and deployments, process instances and variables, user tasks '
  name: Flowable REST API
  slug: rest-api
- description: The CMMN API from Flowable — 4 operation(s) for cmmn.
  name: Flowable CMMN API
  slug: flowable-api-cmmn-api
- description: The Deployments API from Flowable — 3 operation(s) for deployments.
  name: Flowable Deployments API
  slug: flowable-api-deployments-api
- description: The Models API from Flowable — 1 operation(s) for models.
  name: Flowable Models API
  slug: flowable-api-models-api
- description: The ProcessDefinitions API from Flowable — 2 operation(s) for processdefinitions.
  name: Flowable ProcessDefinitions API
  slug: flowable-api-processdefinitions-api
- description: The ProcessInstances API from Flowable — 1 operation(s) for processinstances.
  name: Flowable ProcessInstances API
  slug: flowable-api-processinstances-api
- description: The Tasks API from Flowable — 2 operation(s) for tasks.
  name: Flowable Tasks API
  slug: flowable-api-tasks-api
artifact_total: 14
collections:
- collection_type: open
  name: Flowable REST API
  slug: open-flowable-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flowable-api-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flowable-api-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flowable-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flowable-group
- group: company
  title: ''
  type: Website
  url: https://www.flowable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flowable.com/open-source/docs/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/flowable/flowable-engine
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flowable
- group: company
  title: ''
  type: Blog
  url: https://blog.flowable.org/
created: '2024-11-07'
description: Flowable connects systems, data, and people for faster and smarter process automation, drawing on a long heritage of open source BPM. Flowable provides a model-driven, low-code platform for end-to-end automation of BPMN, CMMN, and DMN processes, delivered through a programmatic Java Process Engine API and a packaged REST API. The Process Engine exposes RepositoryService, RuntimeService, TaskService, IdentityService, HistoryService, ManagementService, FormService, and DynamicBpmnService for managing process definitions, instances, tasks, history, and runtime behavior.
finops:
- name: Flowable Api Finops
  service_category: API
  slug: flowable-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flowable-api.png
layout: provider
modified: '2026-05-19'
name: Flowable
nav: Providers
network: true
overview: 'Flowable publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CMMN API, Deployments API, Models API, and 3 more. Tagged areas include Automation, BPM, BPMN, Business Process, and CMMN.


  Flowable''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Flowable Api Plans Pricing
  plan_count: 3
  slug: flowable-api-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 5
  name: Flowable Api Rate Limits
  slug: flowable-api-rate-limits
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 45.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flowable-api/refs/heads/main/screenshots/flowable-api-2026-06-20T181328.png
security:
- kind: domain-security
  name: Flowable Api Domain Security
  slug: flowable-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flowable Api Trust Center
  slug: flowable-api-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: flowable-api
tags:
- Automation
- BPM
- BPMN
- Business Process
- CMMN
- DMN
- Workflows
website: https://www.flowable.com/
---

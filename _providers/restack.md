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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Restack Agentic Access
  operation_count: 5
  slug: restack-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 3
apis:
- description: The Agents API from Restack — 2 operation(s) for agents.
  name: Restack Agents API
  slug: restack-agents-api
- description: The System API from Restack — 1 operation(s) for system.
  name: Restack System API
  slug: restack-system-api
- description: The Workflows API from Restack — 2 operation(s) for workflows.
  name: Restack Workflows API
  slug: restack-workflows-api
artifact_total: 19
collections:
- collection_type: open
  name: Restack API
  slug: open-restack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/restack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/restack-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.restack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.restack.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/restackio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/restackio/
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/restackio/examples-python
- group: build
  title: ''
  type: TypeScript SDK
  url: https://github.com/restackio/examples-typescript
- group: other
  title: ''
  type: Kubernetes Helm
  url: https://github.com/restackio/helm
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.restack.io/llms.txt
created: '2025-02-17'
description: Restack is an enterprise AI agent platform and backend framework for building accurate, reliable, and scalable AI products. It provides durable workflow orchestration, long-running agent execution, and infrastructure for deploying AI agents at enterprise scale using Python and Kubernetes.
examples:
- key_count: 2
  name: Restack Get Agent Run Example
  slug: restack-get-agent-run-example
- key_count: 2
  name: Restack Schedule Agent Example
  slug: restack-schedule-agent-example
- key_count: 2
  name: Restack Schedule Workflow Example
  slug: restack-schedule-workflow-example
finops:
- name: Restack Finops
  service_category: API
  slug: restack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restack.png
json_schemas:
- name: Agent Run
  property_count: 8
  slug: restack-agent-run
- name: Workflow Run
  property_count: 8
  slug: restack-workflow-run
json_structures:
- name: Restack Agent Run Structure
  property_count: 0
  slug: restack-agent-run-structure
jsonld:
- class_count: 29
  name: Restack Context
  property_count: 0
  slug: restack-context
layout: provider
modified: '2026-05-19'
name: Restack
nav: Providers
network: true
overview: 'Restack publishes 3 APIs on the [APIs.io](https://apis.io/) network: Agents API, System API, and Workflows API. Tagged areas include AI Agents, Workflows, Orchestration, Enterprise, and Python.


  The Restack catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Restack''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Restack Plans Pricing
  plan_count: 3
  slug: restack-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Restack Rate Limits
  slug: restack-rate-limits
rules:
- name: Restack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restack-jsonschema-spectral-rules
- name: Restack API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 7
  slug: restack-rules
score:
  band: developing
  composite: 51.0
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 74.6
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restack/refs/heads/main/screenshots/restack-2026-06-20T193006.png
security:
- kind: authentication
  name: Restack Authentication
  slug: restack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Restack Domain Security
  slug: restack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: restack
tags:
- AI Agents
- Workflows
- Orchestration
- Enterprise
- Python
website: https://www.restack.io/
---

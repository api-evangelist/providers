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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: Manage Access Control List (ACL) policies for fine-grained permission control.
  name: Rundeck ACL Policies API
  slug: rundeck-acl-policies-api
- description: Monitor running executions, retrieve execution history, and manage execution state.
  name: Rundeck Executions API
  slug: rundeck-executions-api
- description: List, create, import, export, run, and delete automation jobs.
  name: Rundeck Jobs API
  slug: rundeck-jobs-api
- description: Query and manage nodes (target machines) associated with Rundeck projects.
  name: Rundeck Nodes API
  slug: rundeck-nodes-api
- description: Create and manage Rundeck projects which organize jobs and node configurations.
  name: Rundeck Projects API
  slug: rundeck-projects-api
- description: Access system information, health checks, execution modes, metrics, and configuration.
  name: Rundeck System API
  slug: rundeck-system-api
- description: Create, list, and delete API authentication tokens.
  name: Rundeck Tokens API
  slug: rundeck-tokens-api
- description: Manage user profiles, roles, and API token generation.
  name: Rundeck Users API
  slug: rundeck-users-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rundeck ACL Policies API
  slug: open-rundeck-acl-policies-api
- collection_type: open
  name: Rundeck Executions API
  slug: open-rundeck-executions-api
- collection_type: open
  name: Rundeck Jobs API
  slug: open-rundeck-jobs-api
- collection_type: open
  name: Rundeck Nodes API
  slug: open-rundeck-nodes-api
- collection_type: open
  name: Rundeck Projects API
  slug: open-rundeck-projects-api
- collection_type: open
  name: Rundeck System API
  slug: open-rundeck-system-api
- collection_type: open
  name: Rundeck Tokens API
  slug: open-rundeck-tokens-api
- collection_type: open
  name: Rundeck Users API
  slug: open-rundeck-users-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rundeck-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rundeck
- group: company
  title: ''
  type: Website
  url: https://www.rundeck.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rundeck.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rundeck
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/rundeck/rundeck
- group: company
  title: ''
  type: Blog
  url: https://www.rundeck.com/blog
- group: operate
  title: ''
  type: Community
  url: https://community.rundeck.com
- group: other
  title: ''
  type: Download
  url: https://www.rundeck.com/downloads
- group: operate
  title: ''
  type: Support
  url: https://www.rundeck.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rundeck.com/pricing
created: '2024-01-01'
description: Rundeck is an open source runbook automation service with a web console, command line tools, and a REST WebAPI. It enables IT teams to easily run automation tasks across a set of nodes, providing self-service operations, job scheduling, and execution history. Rundeck is developed by PagerDuty and supports enterprise runbook automation with role-based access control, multi-tenant project management, and integrations with popular DevOps tools including Jenkins, Ansible, Chef, and Puppet. The REST API is versioned and supports authentication via API tokens, password-based session tokens, and JWT (commercial).
examples:
- key_count: 2
  name: Rundeck List Jobs Example
  slug: rundeck-list-jobs-example
- key_count: 2
  name: Rundeck Run Job Example
  slug: rundeck-run-job-example
finops:
- name: Rundeck Finops
  service_category: API
  slug: rundeck-finops
image: https://www.rundeck.com/hubfs/Assets/Images/logos/rundeck-logo-black.png
json_schemas:
- name: Rundeck Job
  property_count: 14
  slug: rundeck-job
json_structures:
- name: Rundeck Job Structure
  property_count: 0
  slug: rundeck-job-structure
jsonld:
- class_count: 0
  name: Rundeck Context
  property_count: 6
  slug: rundeck-context
layout: provider
modified: '2026-05-02'
name: Rundeck
nav: Providers
network: true
overview: 'Rundeck publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ACL Policies API, Executions API, Jobs API, and 5 more. Tagged areas include Automation, DevOps, Job Scheduling, Orchestration, and Workflow.


  The Rundeck catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rundeck''s developer surface includes documentation, engineering blog, support, pricing, and 7 more developer resources.'
plans:
- name: Rundeck Plans Pricing
  plan_count: 3
  slug: rundeck-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Rundeck Rate Limits
  slug: rundeck-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Rundeck API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rundeck-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Rundeck API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 11
  slug: rundeck-rules
score:
  band: thin
  composite: 30.9
  delta: -8.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 61.6
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 39.7
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rundeck/refs/heads/main/screenshots/rundeck-2026-06-20T193250.png
security:
- kind: domain-security
  name: Rundeck Domain Security
  slug: rundeck-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rundeck
tags:
- Automation
- DevOps
- Job Scheduling
- Orchestration
- Workflow
- Runbook
- Open Source
- IT Operations
website: https://www.rundeck.com
---

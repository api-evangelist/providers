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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Rundeck REST API provides programmatic access to job execution, project management, node management, execution history, user management, ACL policies, system administration, cluster operations, an
  name: Rundeck API
  slug: rundeck-api
artifact_total: 12
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
overview: 'Rundeck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, DevOps, Job Scheduling, Orchestration, and Workflow.


  The Rundeck catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rundeck''s developer surface includes documentation, engineering blog, support, pricing, and 7 more developer resources.'
plans:
- name: Rundeck Plans Pricing
  plan_count: 3
  slug: rundeck-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Rundeck Rate Limits
  slug: rundeck-rate-limits
rules:
- name: Rundeck API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rundeck-jsonschema-spectral-rules
- name: Rundeck API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 11
  slug: rundeck-rules
score:
  band: developing
  composite: 47.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.4
    developer_ergonomics: 15.2
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 47.6
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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

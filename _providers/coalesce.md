---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
- acting_count: 21
  human_in_the_loop: 0
  name: Coalesce Agentic Access
  operation_count: 36
  slug: coalesce-agentic-access
  summary_line: 36 operations · 21 acting
api_count: 7
apis:
- description: Manage Coalesce deployment environments
  name: Coalesce Environments API
  slug: coalesce-environments-api
- description: Manage Git account integrations
  name: Coalesce Git Accounts API
  slug: coalesce-git-accounts-api
- description: Manage environment and workspace nodes
  name: Coalesce Nodes API
  slug: coalesce-nodes-api
- description: Manage Coalesce projects
  name: Coalesce Projects API
  slug: coalesce-projects-api
- description: List and inspect pipeline run records
  name: Coalesce Runs API
  slug: coalesce-runs-api
- description: Start, stop, retry, and monitor pipeline runs
  name: Coalesce Scheduler API
  slug: coalesce-scheduler-api
- description: Manage organization users and roles
  name: Coalesce Users API
  slug: coalesce-users-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coalesce-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/coalesce-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coalesce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coalesce-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coalesce.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coalesce.io/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/coalesceio
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Coalesce-Software-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coalesceio
- group: company
  title: ''
  type: Blog
  url: https://coalesce.io/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://coalesce.io/product/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coalesce.io/
- group: other
  title: ''
  type: X
  url: https://x.com/coalesceIO
- group: commercial
  title: ''
  type: Plans
  url: plans/coalesce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coalesce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coalesce-finops.yml
created: '2026-06-13'
description: Coalesce is a unified data transformation platform built for Snowflake that combines transformation, cataloging, and quality monitoring into a single operating layer. It provides REST APIs for managing projects, environments, nodes, deployments, runs, and column-level documentation in data warehouse pipelines, enabling teams to automate runs, query metadata, and integrate Coalesce into CI/CD workflows.
examples:
- key_count: 4
  name: List Environments
  slug: list-environments
- key_count: 4
  name: Start Run
  slug: start-run
finops:
- name: Coalesce Finops
  service_category: ''
  slug: coalesce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coalesce.png
json_schemas:
- name: Environment
  property_count: 6
  slug: environment
- name: Node
  property_count: 7
  slug: node
- name: Run
  property_count: 5
  slug: run
jsonld:
- class_count: 30
  name: Coalesce Context
  property_count: 4
  slug: coalesce-context
layout: provider
modified: '2026-06-13'
name: Coalesce
nav: Providers
network: true
overview: 'Coalesce publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Environments API, Git Accounts API, Nodes API, and 4 more. Tagged areas include Data Transformation, Snowflake, Data Pipelines, Data Catalog, and Data Quality.


  The Coalesce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coalesce''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Coalesce Plans Pricing
  plan_count: 3
  slug: coalesce-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Coalesce Rate Limits
  slug: coalesce-rate-limits
rules:
- name: Coalesce API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: coalesce-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.8
  delta: -4.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coalesce/refs/heads/main/screenshots/coalesce-2026-06-20T174640.png
security:
- kind: authentication
  name: Coalesce Authentication
  slug: coalesce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coalesce Domain Security
  slug: coalesce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Coalesce Trust Center
  slug: coalesce-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: coalesce
tags:
- Data Transformation
- Snowflake
- Data Pipelines
- Data Catalog
- Data Quality
- Analytics
- AI
website: https://coalesce.io
---

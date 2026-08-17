---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'RESTful HTTP API for the Zenput operations-execution platform — retrieve activity/form submissions (including large-batch paged retrieval), manage locations, users, user roles, teams, tasks, sensors, '
  name: Zenput API
  slug: zenput-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenput-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zenput.com
- group: company
  title: ''
  type: Website
  url: https://www.zenput.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zenput.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.zenput.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zenput.com/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.crunchtime.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenput
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenput-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenput-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zenput-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zenput-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zenput-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zenput-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zenput-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zenput-mcp.yml
created: '2026-07-17'
description: Zenput (now Crunchtime Ops Execution) is an operations-execution platform for multi-unit restaurant and convenience-store operators, used across 60,000+ locations in 100+ countries to run task management, audits and food-safety compliance, temperature monitoring, food-prep labeling, and store-level operational workflows. Zenput exposes a RESTful HTTP API (documented at developer.zenput.com) for submissions/form data, locations, users and roles, teams, tasks, sensors, calendar events / operating hours, general attributes, and field-business-consultant (FBC) assignments. The API authenticates with a per-user X-API-TOKEN header, is versioned in the URL path (v1 and v3), and provides a large-batch submissions retrieval flow with token-based paging plus a staging environment for testing. Zenput was acquired by Crunchtime in 2022 and continues to operate its developer platform under the Zenput brand.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenput.png
layout: provider
mcp_servers:
- description: ''
  name: zenput-mcp.yml
  slug: zenput-mcpyml
modified: '2026-07-21'
name: Zenput
nav: Providers
network: true
overview: 'Zenput publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant Operations, Operations Execution, Food Safety, and Compliance.


  Zenput''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, sandbox, and 9 more developer resources.'
random_paper: 82
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.1
  provenance:
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Zenput Authentication
  slug: zenput-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zenput Domain Security
  slug: zenput-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zenput
tags:
- Company
- Restaurant Operations
- Operations Execution
- Food Safety
- Compliance
- Task Management
- Convenience Stores
- Field Operations
- Restaurant Technology
website: https://www.zenput.com
---

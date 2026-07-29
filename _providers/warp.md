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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Warp Agentic Access
  operation_count: 28
  slug: warp-agentic-access
  summary_line: 28 operations · 12 acting
api_count: 5
apis:
- description: The Enterprise Analytics API provides team usage metrics and administrative insights for Enterprise plan customers. It enables organizations to track agent usage, monitor spend, and audit team activit
  name: Warp Enterprise Analytics API
  slug: enterprise-analytics-api
- description: The Oz CLI is a command-line interface for interacting with the Warp Oz agent platform. It allows developers to trigger cloud agent runs, manage environments, and authenticate headlessly using API key
  name: Warp Oz CLI
  slug: oz-cli
- description: Operations for running and managing cloud agents
  name: Warp agent API
  slug: warp-agent-api
- description: The harness-support API from Warp — 1 operation(s) for harness-support.
  name: Warp harness-support API
  slug: warp-harness-support-api
- description: Operations for creating and managing scheduled agents
  name: Warp schedules API
  slug: warp-schedules-api
artifact_total: 23
collections:
- collection_type: postman
  name: Oz agent API
  slug: postman-warp-agent-api
- collection_type: postman
  name: Oz agent harness-support API
  slug: postman-warp-harness-support-api
- collection_type: postman
  name: Oz agent schedules API
  slug: postman-warp-schedules-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/warp/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/warp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/warp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/warp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.warp.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.warp.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/warpdotdev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/warpdotdev
- group: other
  title: ''
  type: X
  url: https://x.com/warpdotdev
- group: company
  title: ''
  type: Blog
  url: https://www.warp.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.warp.dev/changelog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.warp.dev/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.warp.dev/
- group: agent
  title: ''
  type: MCP
  url: https://docs.warp.dev/agent-platform/capabilities/mcp/
- group: commercial
  title: ''
  type: Plans
  url: plans/warp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/warp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/warp-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/warp-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/warp-context.jsonld
created: '2026-06-12'
description: Warp is an open-source, Rust-based, GPU-accelerated agentic development environment built on top of a modern terminal. It combines a high-performance terminal with AI-powered cloud agents (the Oz platform) to help developers build, test, deploy, and debug code autonomously. The Oz API lets external systems trigger and monitor cloud agent runs over HTTP, making it suitable for CI pipelines, backend services, and internal tooling. Warp also provides Warp Drive for team collaboration and workflow sharing, and supports MCP servers for extending agent capabilities with custom tools and data sources.
examples:
- key_count: 3
  name: Warp Create Schedule Example
  slug: warp-create-schedule-example
- key_count: 3
  name: Warp List Runs Example
  slug: warp-list-runs-example
- key_count: 3
  name: Warp Run Agent Example
  slug: warp-run-agent-example
finops:
- name: Warp Finops
  service_category: Developer Tools
  slug: warp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/warp.png
json_schemas:
- name: RunAgentRequest
  property_count: 11
  slug: warp-run-agent-request
- name: RunItem
  property_count: 20
  slug: warp-run
- name: ScheduledAgentItem
  property_count: 12
  slug: warp-scheduled-agent
jsonld:
- class_count: 42
  name: Warp Context
  property_count: 9
  slug: warp-context
layout: provider
modified: '2026-06-12'
name: Warp
nav: Providers
network: true
overview: 'Warp publishes 3 APIs on the [APIs.io](https://apis.io/) network: agent API, harness-support API, and schedules API. Tagged areas include Developer Tools, Terminal, AI Agents, Cloud Agents, and Agentic Development.


  The Warp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Warp''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 15 more developer resources.'
plans:
- name: Warp Plans Pricing
  plan_count: 5
  slug: warp-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 3
  name: Warp Rate Limits
  slug: warp-rate-limits
rules:
- name: Warp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: warp-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.1
  delta: -3.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 70.6
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 61.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/warp/refs/heads/main/screenshots/warp-2026-06-20T201231.png
security:
- kind: authentication
  name: Warp Authentication
  slug: warp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Warp Domain Security
  slug: warp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Warp Trust Center
  slug: warp-trust-center
  summary_line: SOC 2
slug: warp
tags:
- Developer Tools
- Terminal
- AI Agents
- Cloud Agents
- Agentic Development
website: https://www.warp.dev/
---

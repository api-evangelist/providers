---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Warp Agentic Access
  operation_count: 28
  slug: warp-agentic-access
  summary_line: 28 operations · 12 acting
api_count: 1
apis:
- description: The Enterprise Analytics API provides team usage metrics and administrative insights for Enterprise plan customers. It enables organizations to track agent usage, monitor spend, and audit team activit
  name: Warp Enterprise Analytics API
  slug: enterprise-analytics-api
- description: The Oz CLI is a command-line interface for interacting with the Warp Oz agent platform. It allows developers to trigger cloud agent runs, manage environments, and authenticate headlessly using API key
  name: Warp Oz CLI
  slug: oz-cli
- baseURL: https://app.warp.dev/api/v1
  baseurl_source: declared
  description: Operations for running and managing cloud agents
  name: Warp Agent API
  slug: warp-agent-api
- baseURL: https://app.warp.dev/api/v1
  baseurl_source: declared
  description: The harness-support API from Warp — 1 operation(s) for harness-support.
  name: Warp Harness Support API
  slug: warp-harness-support-api
- baseURL: https://app.warp.dev/api/v1
  baseurl_source: declared
  description: Operations for creating and managing scheduled agents
  name: Warp Schedules API
  slug: warp-schedules-api
artifact_total: 27
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
- collection_type: open
  name: Oz agent API
  slug: open-warp-agent-api
- collection_type: open
  name: Oz agent harness-support API
  slug: open-warp-harness-support-api
- collection_type: open
  name: Oz agent schedules API
  slug: open-warp-schedules-api
common:
- group: other
  href: https://artifacts.apis.io/warp/capabilities/warp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/warp-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/warp/overview
- group: agent
  href: https://artifacts.apis.io/warp/agentic-access/warp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/warp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/warp/security/warp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/warp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/warp/security/warp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/warp-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/warp/authentication/warp-authentication.yml
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
- group: docs
  title: ''
  type: Documentation
  url: https://docs.warp.dev/agent-platform/capabilities/mcp/
- group: commercial
  href: https://artifacts.apis.io/warp/plans/warp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/warp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/warp/rate-limits/warp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/warp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/warp/finops/warp-finops.yml
  title: ''
  type: FinOps
  url: finops/warp-finops.yml
- group: design
  href: https://artifacts.apis.io/warp/vocabulary/warp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/warp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/warp/json-ld/warp-context.jsonld
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
- has_sources: true
  method: derived
  name: Warp Finops
  primary_unit: user
  service_category: ''
  slug: warp-finops
  template: false
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
overview: 'Warp publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Harness Support API, Schedules API, and 2 more. Tagged areas include Developer Tools, Terminal, AI Agents, Cloud Agents, and Agentic Development.


  The Warp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Warp''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 16 more developer resources.'
plans:
- name: Warp Plans Pricing
  plan_count: 12
  slug: warp-plans-pricing
- name: Warp Price Estimates
  plan_count: 0
  slug: warp-price-estimates
random_paper: 10
rate_limits:
- limit_count: 3
  name: Warp Rate Limits
  slug: warp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Warp — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: warp-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 57.9
    contract_governance: 23.5
    contract_quality: 64.3
    developer_ergonomics: 36.9
    discoverability: 57.1
    operational_transparency: 44.7
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/warp/warp-2026-06-20T201231.png
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

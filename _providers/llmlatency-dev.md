---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read-only API providing latency and uptime metrics for various LLM providers.
  name: AI Latency Tracker API
  slug: ai-latency-tracker-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/llmlatency-dev/conformance/llmlatency-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llmlatency-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/llmlatency-dev/llms/llmlatency-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/llmlatency-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/llmlatency-dev/mcp/llmlatency-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/llmlatency-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/llmlatency-dev/well-known/llmlatency-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llmlatency-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/llmlatency-dev/hosts/llmlatency-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmlatency-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmlatency-dev/vendors/llmlatency-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmlatency-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mazamaka
- group: operate
  title: ''
  type: ChangeLog
  url: https://llmlatency.dev/changelog
- group: auth
  href: https://artifacts.apis.io/llmlatency-dev/security/llmlatency-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmlatency-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmlatency.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://llmlatency.dev/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://llmlatency.dev/blog
created: '2026-10-30'
description: llmlatency-dev provides tools and services focused on measuring and optimizing latency for large language model (LLM) deployments. The platform offers APIs that allow developers to benchmark response times, monitor performance across different model versions, and receive actionable insights to reduce latency in production environments. By integrating with popular LLM providers, it helps improve user experience and cost efficiency for AI-driven applications.
image: https://llmlatency.dev/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at llmlatency.dev.
  name: llmlatency-dev MCP Server
  slug: llmlatency-dev-mcp-yml
modified: '2026-10-30'
name: llmlatency-dev
nav: Providers
network: true
overview: 'llmlatency-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Latency, Monitoring, and Performance.


  llmlatency-dev''s developer surface includes changelog, API reference, engineering blog, and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 10.9
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/llmlatency-dev/llmlatency-dev-2026-11-03T134959.png
security:
- kind: domain-security
  name: Llmlatency Dev Domain Security
  slug: llmlatency-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: llmlatency-dev
tags:
- Company
- Artificial Intelligence
- Latency
- Monitoring
- Performance
website: https://llmlatency.dev/
---

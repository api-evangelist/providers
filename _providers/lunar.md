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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Lunar Agentic Access
  operation_count: 13
  slug: lunar-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 8
apis:
- description: The Lunar API Consumption Gateway is a proxy-based infrastructure layer that routes outbound HTTP/HTTPS API traffic through configurable YAML-based flows. It enforces rate limits, quota policies, prio
  name: Lunar API Consumption Gateway
  slug: api-consumption-gateway
- description: The Lunar MCPX Gateway is an agent-native Model Context Protocol gateway that governs tool invocation for AI agents. It consolidates multiple MCP servers into a single endpoint, providing authenticati
  name: Lunar MCPX Gateway
  slug: mcpx-gateway
- description: Contract-based configuration management
  name: Lunar Configuration API
  slug: lunar-configuration-api
- description: API discovery and remedy state reporting
  name: Lunar Discovery API
  slug: lunar-discovery-api
- description: Gateway diagnostic reporting
  name: Lunar Doctor API
  slug: lunar-doctor-api
- description: Manage Lunar Flows (streams-based traffic shaping rules)
  name: Lunar Flows API
  slug: lunar-flows-api
- description: Gateway health and connectivity check
  name: Lunar Handshake API
  slug: lunar-handshake-api
- description: Manage Lunar Policies (legacy traffic control rules)
  name: Lunar Policies API
  slug: lunar-policies-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lunar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lunar.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lunar.dev/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/TheLunarCompany
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/TheLunarCompany/lunar
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/lunar-api
- group: other
  title: ''
  type: X
  url: https://twitter.com/_lunardev
- group: company
  title: ''
  type: Blog
  url: https://www.lunar.dev/lunar-blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lunar.dev/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.lunar.dev
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/T2VvD3hpxD
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@LunarDev-api/videos
- group: company
  title: ''
  type: News
  url: https://www.lunar.dev/in-the-news
- group: commercial
  title: ''
  type: Plans
  url: plans/lunar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lunar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lunar-finops.yml
created: '2026-06-13'
description: Lunar is an enterprise-grade API management and AI control plane platform that provides a unified gateway for managing API traffic policies, rate limiting, quota enforcement, and API monetization across gateways. The platform combines an API consumption gateway with an MCP (Model Context Protocol) gateway to govern, secure, and observe interactions between AI agents, APIs, and data sources. Lunar delivers real-time visibility into model, API, and tool invocations alongside policy-based enforcement, cost controls, and advanced traffic shaping including retries, priority queues, and circuit breakers.
examples:
- key_count: 2
  name: Lunar Apply Flows Payload
  slug: lunar-apply-flows-payload
- key_count: 1
  name: Lunar Handshake Response
  slug: lunar-handshake-response
- key_count: 4
  name: Lunar Proxy Request Headers
  slug: lunar-proxy-request-headers
finops:
- name: Lunar Finops
  service_category: ''
  slug: lunar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lunar.png https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Lunar Flows Configuration
  property_count: 2
  slug: lunar-flows-configuration
- name: Lunar Gateway Proxy Request Headers
  property_count: 4
  slug: lunar-gateway-proxy-request
jsonld:
- class_count: 4
  name: Lunar Context
  property_count: 37
  slug: lunar-context
layout: provider
modified: '2026-06-13'
name: Lunar
nav: Providers
network: true
overview: 'Lunar publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Discovery API, Doctor API, and 3 more. Tagged areas include API Management, API Gateway, AI Gateway, MCP Gateway, and Rate Limiting.


  The Lunar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lunar''s developer surface includes documentation, engineering blog, pricing, signup flow, YouTube channel, product news, and 11 more developer resources.'
plans:
- name: Lunar Plans Pricing
  plan_count: 3
  slug: lunar-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Lunar Rate Limits
  slug: lunar-rate-limits
rules:
- name: Lunar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: lunar-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.3
  delta: -5.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lunar/refs/heads/main/screenshots/lunar-2026-06-20T184757.png
security:
- kind: domain-security
  name: Lunar Domain Security
  slug: lunar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lunar
tags:
- API Management
- API Gateway
- AI Gateway
- MCP Gateway
- Rate Limiting
- Quota Enforcement
- API Monetization
- Traffic Management
- API Governance
- Cost Controls
- Observability
website: https://www.lunar.dev/
---

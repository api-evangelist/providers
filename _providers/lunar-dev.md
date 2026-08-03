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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Lunar Dev Agentic Access
  operation_count: 11
  slug: lunar-dev-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 5
apis:
- description: API endpoint discovery and metrics.
  name: Lunar.dev Discovery API
  slug: lunar-dev-discovery-api
- description: Flow configuration management for traffic control.
  name: Lunar.dev Flows API
  slug: lunar-dev-flows-api
- description: Gateway health monitoring endpoints.
  name: Lunar.dev Health API
  slug: lunar-dev-health-api
- description: Policy management for the Lunar Gateway.
  name: Lunar.dev Policies API
  slug: lunar-dev-policies-api
- description: Proxy endpoints for routing third-party API traffic through the Lunar Gateway with policy enforcement, traffic controls, and observability.
  name: Lunar.dev Proxy API
  slug: lunar-dev-proxy-api
artifact_total: 54
collections:
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery API
  slug: postman-lunar-dev-discovery-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Flows API
  slug: postman-lunar-dev-flows-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Health API
  slug: postman-lunar-dev-health-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Policies API
  slug: postman-lunar-dev-policies-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Proxy API
  slug: postman-lunar-dev-proxy-api
- collection_type: open
  name: Lunar.dev Gateway Admin API
  slug: open-lunar-dev-gateway-admin
- collection_type: open
  name: Lunar.dev Gateway Proxy API
  slug: open-lunar-dev-gateway-proxy
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lunardev/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lunar-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunar-dev-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lunar-api
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCgWge-0djZcm-JWU82FbR7A
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheLunarCompany
- group: company
  title: ''
  type: Website
  url: https://www.lunar.dev/
- group: company
  title: ''
  type: Blog
  url: https://www.lunar.dev/lunar-blog
- group: docs
  title: ''
  type: Guide
  url: https://www.lunar.dev/guides-resources
- group: operate
  title: ''
  type: FAQ
  url: https://www.lunar.dev/faqs
- group: other
  title: ''
  type: Customers
  url: https://www.lunar.dev/case-study
- group: other
  title: ''
  type: Customers
  url: https://www.lunar.dev/case-study
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lunar.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lunar.dev/quick-start-guide/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.lunar.dev/quotas/quotas-overview
- group: operate
  title: ''
  type: FAQ
  url: https://docs.lunar.dev/additional-resources/faqs/faqIndex
- group: company
  title: ''
  type: About
  url: https://www.lunar.dev/about-us
- group: start
  title: ''
  type: Login
  url: https://login.lunar.dev/u/login?state=hKFo2SBYaVVrZmZpMHhLN3M3RFlmV0s1WUZCYzZjb2Nwa2FNWaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEtDRC1iM2d3Z1ltMTNSYmpKZEloOHFHUFp3aG5FMk9vo2NpZNkgQTZBOVRoUnJ6anp2eEx6cFUwRm5JZE1Id0xUUmdnSFE
- group: start
  title: ''
  type: Signup
  url: https://login.lunar.dev/u/login?state=hKFo2SBkZkoxMlV1VVFQQmZ3ejlTQjU2QWdteFBEbG1tSWNERaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFVCVnEySHI0MHlSLTdmRU0ydzBGeTd6aFlxLTFYUlhMo2NpZNkgQTZBOVRoUnJ6anp2eEx6cFUwRm5JZE1Id0xUUmdnSFE
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lunar.dev/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lunar.dev/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://www.lunar.dev/lunar-blog
- group: operate
  title: ''
  type: Support
  url: https://www.lunar.dev/demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lunar.dev/pricing
created: '2025-01-08'
description: Lunar.dev is an enterprise-grade gateway platform for AI governance and third-party API consumption control. It unifies an MCP Gateway, AI Gateway, and API Consumption Gateway into a single control point that gives organizations observability, access control, policy enforcement, quota management, rate limiting, and real-time monitoring over how applications and AI agents authenticate, discover tools, and consume third-party APIs.
features:
- name: Additional Features
- name: Advanced Traffic Controls
- name: Broad Sdk Support
- name: Centralized Consumption
- name: Configurable Policies
- name: Consumer Tags
- name: Egress API Proxy
- name: Fail-Safe Mechanisms
- name: Generic Approach
- name: Inventory of APIs
- name: Insights
- name: Lunar Proxy
- name: Lunar Interceptor
- name: No Code Changes
- name: Plugin System
- name: Prioritized API Queuing
- name: Production-Grade Ready
- name: Quota Management
- name: Real-Time Insights
- name: Real-Time Controls
- name: Real-Time Monitoring
- name: Visibility
finops:
- name: Lunar Dev Finops
  service_category: API
  slug: lunar-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lunar-dev.png
json_schemas:
- name: Lunar.dev Discovered Endpoint
  property_count: 5
  slug: discovered-endpoint
- name: Lunar.dev Flow
  property_count: 5
  slug: flow
- name: Lunar.dev Health Status
  property_count: 1
  slug: health-status
- name: Lunar.dev Policy
  property_count: 8
  slug: policy
- name: Lunar.dev Validation Result
  property_count: 2
  slug: validation-result
jsonld:
- class_count: 0
  name: Lunar Dev Context
  property_count: 5
  slug: lunar-dev-context
layout: provider
modified: '2026-05-19'
name: Lunar.dev
nav: Providers
network: true
overview: 'Lunar.dev publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Flows API, Health API, and 2 more. Tagged areas include AI Gateway, Automation, Consumption Gateway, Control, and Deployment.


  The Lunar.dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lunar.dev''s developer surface includes YouTube channel, engineering blog, FAQ, documentation, getting-started guide, signup flow, support, and 17 more developer resources.'
plans:
- name: Lunar Dev Plans Pricing
  plan_count: 3
  slug: lunar-dev-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Lunar Dev Rate Limits
  slug: lunar-dev-rate-limits
rules:
- name: Lunar.dev API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lunar-dev-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.0
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 63.3
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lunar-dev/refs/heads/main/screenshots/lunar-dev-2026-06-20T184803.png
security:
- kind: domain-security
  name: Lunar Dev Domain Security
  slug: lunar-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lunar-dev
tags:
- AI Gateway
- Automation
- Consumption Gateway
- Control
- Deployment
- Integrations
- MCP Gateway
- Performance
- Platform
- Version Control
- Visibility
- Workflows
use_cases:
- name: AI-Aware API Consumption
- name: API Consumption Management
- name: Consolidating Mcp Servers
- name: Cost Optimization
- name: Egress API Proxy
- name: Managing Api-Driven Tasks
- name: Policy Enforcement
- name: Visibility and Alerts
website: https://www.lunar.dev/
---

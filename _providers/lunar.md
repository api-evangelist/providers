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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Lunar Agentic Access
  operation_count: 13
  slug: lunar-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 3
apis:
- description: The Lunar API Consumption Gateway is a proxy-based infrastructure layer that routes outbound HTTP/HTTPS API traffic through configurable YAML-based flows. It enforces rate limits, quota policies, prio
  name: Lunar API Consumption Gateway
  slug: api-consumption-gateway
- description: The Lunar MCPX Gateway is an agent-native Model Context Protocol gateway that governs tool invocation for AI agents. It consolidates multiple MCP servers into a single endpoint, providing authenticati
  name: Lunar MCPX Gateway
  slug: mcpx-gateway
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: Contract-based configuration management
  name: Lunar Configuration API
  slug: lunar-configuration-api
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: API discovery and remedy state reporting
  name: Lunar Discovery API
  slug: lunar-discovery-api
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: Gateway diagnostic reporting
  name: Lunar Doctor API
  slug: lunar-doctor-api
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: Manage Lunar Flows (streams-based traffic shaping rules)
  name: Lunar Flows API
  slug: lunar-flows-api
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: Gateway health and connectivity check
  name: Lunar Handshake API
  slug: lunar-handshake-api
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: Manage Lunar Policies (legacy traffic control rules)
  name: Lunar Policies API
  slug: lunar-policies-api
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: Gateway health monitoring endpoints.
  name: Lunar Health API
  slug: lunar-health-api
- baseURL: https://app.lunar.dev
  baseurl_source: declared
  description: Proxy endpoints for routing third-party API traffic through the Lunar Gateway with policy enforcement, traffic controls, and observability.
  name: Lunar Proxy API
  slug: lunar-proxy-api
artifact_total: 65
collections:
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery API
  slug: postman-lunar-discovery-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Flows API
  slug: postman-lunar-flows-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Health API
  slug: postman-lunar-health-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Policies API
  slug: postman-lunar-policies-api
- collection_type: postman
  name: Lunar.dev Gateway Admin Discovery Proxy API
  slug: postman-lunar-proxy-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lunar API Consumption Gateway Admin Configuration API
  slug: open-lunar-configuration-api
- collection_type: open
  name: Lunar API Consumption Gateway Admin Configuration Discovery API
  slug: open-lunar-discovery-api
- collection_type: open
  name: Lunar API Consumption Gateway Admin Configuration Doctor API
  slug: open-lunar-doctor-api
- collection_type: open
  name: Lunar API Consumption Gateway Admin Configuration Flows API
  slug: open-lunar-flows-api
- collection_type: open
  name: Lunar.dev Gateway Admin API
  slug: open-lunar-gateway-admin
- collection_type: open
  name: Lunar.dev Gateway Proxy API
  slug: open-lunar-gateway-proxy
- collection_type: open
  name: Lunar API Consumption Gateway Admin Configuration Handshake API
  slug: open-lunar-handshake-api
- collection_type: open
  name: Lunar.dev Gateway Admin Discovery Health API
  slug: open-lunar-health-api
- collection_type: open
  name: Lunar API Consumption Gateway Admin Configuration Policies API
  slug: open-lunar-policies-api
- collection_type: open
  name: Lunar.dev Gateway Admin Discovery Proxy API
  slug: open-lunar-proxy-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TheLunarCompany/lunar/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/TheLunarCompany/lunar/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/TheLunarCompany/lunar/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/TheLunarCompany/lunar/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/TheLunarCompany/lunar/blob/main/LICENSE
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lunardev/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheLunarCompany
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
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lunar.dev/quick-start-guide/
- group: company
  title: ''
  type: About
  url: https://www.lunar.dev/about-us
- group: start
  title: ''
  type: Login
  url: https://login.lunar.dev/u/login?state=hKFo2SBYaVVrZmZpMHhLN3M3RFlmV0s1WUZCYzZjb2Nwa2FNWaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEtDRC1iM2d3Z1ltMTNSYmpKZEloOHFHUFp3aG5FMk9vo2NpZNkgQTZBOVRoUnJ6anp2eEx6cFUwRm5JZE1Id0xUUmdnSFE
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lunar.dev/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lunar.dev/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.lunar.dev/demo
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
- name: Lunar Finops
  service_category: ''
  slug: lunar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lunar.png https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
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
- name: Lunar Flows Configuration
  property_count: 2
  slug: lunar-flows-configuration
- name: Lunar Gateway Proxy Request Headers
  property_count: 4
  slug: lunar-gateway-proxy-request
- name: Lunar.dev Policy
  property_count: 8
  slug: policy
- name: Lunar.dev Validation Result
  property_count: 2
  slug: validation-result
jsonld:
- class_count: 4
  name: Lunar Context
  property_count: 37
  slug: lunar-context
layout: provider
modified: '2026-08-08'
name: Lunar
nav: Providers
network: true
overview: 'Lunar publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Discovery API, Doctor API, and 5 more. Tagged areas include API Management, API Gateway, AI Gateway, MCP Gateway, and Rate Limiting.


  The Lunar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lunar''s developer surface includes documentation, engineering blog, pricing, signup flow, YouTube channel, product news, FAQ, and 26 more developer resources.'
plans:
- name: Lunar Plans Pricing
  plan_count: 3
  slug: lunar-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Lunar Rate Limits
  slug: lunar-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Lunar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: lunar-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 78.3
    catalog_earned_first_party: 0.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 9.8
    contract_quality: 53.8
    developer_ergonomics: 29.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 65.0
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lunar/refs/heads/main/screenshots/lunar-2026-06-20T184803.png
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

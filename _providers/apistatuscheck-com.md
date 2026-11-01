---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Model Context Protocol (MCP) endpoint providing eight tools for API status checking.
  name: MCP
  slug: mcp
- description: 'apistatuscheck-com API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: apistatuscheck-com API
  slug: apistatuscheck-com-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/apistatuscheck-com/rate-limits/apistatuscheck-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apistatuscheck-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apistatuscheck-com/plans/apistatuscheck-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apistatuscheck-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apistatuscheck-com/rules/apistatuscheck-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apistatuscheck-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apistatuscheck-com/json-ld/apistatuscheck-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apistatuscheck-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/apistatuscheck-com/vocabulary/apistatuscheck-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apistatuscheck-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apistatuscheck-com/data-model/apistatuscheck-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apistatuscheck-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apistatuscheck-com/authentication/apistatuscheck-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apistatuscheck-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/apistatuscheck-com/conformance/apistatuscheck-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apistatuscheck-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apistatuscheck-com/llms/apistatuscheck-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apistatuscheck-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/apistatuscheck-com/mcp/apistatuscheck-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apistatuscheck-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/apistatuscheck-com/hosts/apistatuscheck-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apistatuscheck-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/apistatuscheck-com/vendors/apistatuscheck-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apistatuscheck-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://apistatuscheck.com/blog/grok-api-key-setup-guide
- group: auth
  href: https://artifacts.apis.io/apistatuscheck-com/security/apistatuscheck-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apistatuscheck-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apistatuscheck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apistatuscheck.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apistatuscheck.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://apistatuscheck.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://apistatuscheck.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apistatuscheck.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apistatuscheck.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://apistatuscheck.com/support
created: '2026-10-30'
description: API Status Check provides real-time outage monitoring for over 285 developer APIs and websites, including popular services like ChatGPT, YouTube, Instagram, Fortnite, Stripe, and AWS. Users can instantly check if a website or API is down, view a dashboard of monitored services, receive free email alerts for selected APIs, and access detailed troubleshooting guides. The platform offers a free tier with unlimited status checks and a paid Pro plan for advanced alerts.
image: https://apistatuscheck.com/logo.png
json_schemas:
- name: GetApiStatusResponse
  property_count: 2
  slug: apistatuscheck-com-get-api-status-response
- name: GetApiUptimeSlugResponse
  property_count: 5
  slug: apistatuscheck-com-get-api-uptime-slug-response
- name: PostApiBadgeOpenaiRequest
  property_count: 3
  slug: apistatuscheck-com-post-api-badge-openai-request
- name: PostApiMcpRequest
  property_count: 3
  slug: apistatuscheck-com-post-api-mcp-request
- name: PostApiWebhookDiscordRequest
  property_count: 3
  slug: apistatuscheck-com-post-api-webhook-discord-request
- name: PostApiWebhookSlackRequest
  property_count: 3
  slug: apistatuscheck-com-post-api-webhook-slack-request
jsonld:
- class_count: 6
  name: Apistatuscheck Com Context
  property_count: 13
  slug: apistatuscheck-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at apistatuscheck.com.
  name: apistatuscheck-com MCP Server
  slug: apistatuscheck-com-mcp-yml
modified: '2026-10-30'
name: apistatuscheck-com
nav: Providers
network: true
overview: 'apistatuscheck-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Monitoring, Outage Detection, Free Service, and Developer Tools.


  The apistatuscheck-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apistatuscheck-com''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Apistatuscheck Com Plans Pricing
  plan_count: 4
  slug: apistatuscheck-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Apistatuscheck Com Rate Limits
  slug: apistatuscheck-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: apistatuscheck-com API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: apistatuscheck-com-rules
scopes:
- name: Apistatuscheck Com Scopes
  scope_count: 0
  slug: apistatuscheck-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 91.6
    catalog_earned_first_party: 0.0
    catalog_gap: 23.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 70.9
    contract_quality: 53.7
    developer_ergonomics: 47.6
    discoverability: 56.7
    operational_transparency: 28.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apistatuscheck Com Authentication
  slug: apistatuscheck-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apistatuscheck Com Domain Security
  slug: apistatuscheck-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apistatuscheck-com
tags:
- Company
- API Monitoring
- Outage Detection
- Free Service
- Developer Tools
website: https://apistatuscheck.com/
---

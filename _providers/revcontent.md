---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
- acting_count: 7
  human_in_the_loop: 0
  name: Revcontent Agentic Access
  operation_count: 17
  slug: revcontent-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 7
apis:
- description: REST API providing programmatic access to RevContent's advertising platform for managing boosts (campaigns), widgets, content, targeting, bidding, and statistical reporting. Authenticated via OAuth 2.
  name: RevContent Stats & Management API
  slug: revcontent-stats-management-api
- description: OAuth authentication and account access
  name: RevContent Access API
  slug: revcontent-access-api
- description: Campaign management (boosts)
  name: RevContent Boosts API
  slug: revcontent-boosts-api
- description: CCPA data request and deletion
  name: RevContent CCPA API
  slug: revcontent-ccpa-api
- description: Ad content management and performance
  name: RevContent Content API
  slug: revcontent-content-api
- description: Reference data for devices, OS, traffic types, and DMAs
  name: RevContent Helpers API
  slug: revcontent-helpers-api
- description: Widget and audience targeting
  name: RevContent Targeting API
  slug: revcontent-targeting-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revcontent-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revcontent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revcontent-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.revcontent.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.revcontent.com/knowledge/native-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/RevContent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revcontent
- group: company
  title: ''
  type: Blog
  url: https://www.revcontent.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revcontent.com/advertisers/
- group: operate
  title: ''
  type: StatusPage
  url: http://status.revcontent.com/
- group: other
  title: ''
  type: X
  url: https://x.com/RevContent
- group: commercial
  title: ''
  type: Plans
  url: plans/revcontent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revcontent-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revcontent-finops.yml
created: '2026-06-13'
description: RevContent is a performance-driven native advertising and content recommendation network offering a REST API for managing widgets, campaigns (boosts), ad content, audience targeting, bidding, and performance reporting. Publishers and advertisers access the platform through OAuth 2.0 authenticated endpoints to programmatically control campaign settings, device and geo targeting, content delivery, and statistical reporting at scale.
examples:
- key_count: 10
  name: Add Boost Request
  slug: add-boost-request
- key_count: 7
  name: Boost Performance Response
  slug: boost-performance-response
- key_count: 5
  name: Ccpa Data Request
  slug: ccpa-data-request
finops:
- name: Revcontent Finops
  service_category: ''
  slug: revcontent-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revcontent.png
json_schemas:
- name: Boost
  property_count: 11
  slug: boost
- name: CCPADataRequest
  property_count: 5
  slug: ccpa-data-request
- name: ContentItem
  property_count: 10
  slug: content-item
jsonld:
- class_count: 9
  name: Revcontent Context
  property_count: 34
  slug: revcontent-context
layout: provider
modified: '2026-06-13'
name: RevContent
nav: Providers
network: true
overview: 'RevContent publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Access API, Boosts API, CCPA API, and 3 more. Tagged areas include Native Advertising, Content Recommendation, Ad Network, Publisher Monetization, and Programmatic Advertising.


  The RevContent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RevContent''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Revcontent Plans Pricing
  plan_count: 2
  slug: revcontent-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 0
  name: Revcontent Rate Limits
  slug: revcontent-rate-limits
rules:
- name: RevContent API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: revcontent-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.8
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revcontent/refs/heads/main/screenshots/revcontent-2026-06-20T193044.png
security:
- kind: authentication
  name: Revcontent Authentication
  slug: revcontent-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Revcontent Domain Security
  slug: revcontent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revcontent
tags:
- Native Advertising
- Content Recommendation
- Ad Network
- Publisher Monetization
- Programmatic Advertising
website: https://www.revcontent.com
---

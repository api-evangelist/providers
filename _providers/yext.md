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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 121
  human_in_the_loop: 0
  name: Yext Agentic Access
  operation_count: 248
  slug: yext-agentic-access
  summary_line: 248 operations · 121 acting
api_count: 23
apis:
- description: The Account Settings API from Yext — 10 operation(s) for account settings.
  name: Yext Account Settings API
  slug: yext-account-settings-api
- description: The Accounts API from Yext — 8 operation(s) for accounts.
  name: Yext Accounts API
  slug: yext-accounts-api
- description: 'NOTE: You need a sandbox account to test your Administrative API integration. Contact your Account Manager to have one created for you.'
  name: Yext Administrative API API
  slug: yext-administrative-api-api
- description: The Analytics API from Yext — 4 operation(s) for analytics.
  name: Yext Analytics API
  slug: yext-analytics-api
- description: The Computations API from Yext — 2 operation(s) for computations.
  name: Yext Computations API
  slug: yext-computations-api
- description: The Configuration API from Yext — 3 operation(s) for configuration.
  name: Yext Configuration API
  slug: yext-configuration-api
- description: The Connectors API from Yext — 5 operation(s) for connectors.
  name: Yext Connectors API
  slug: yext-connectors-api
- description: The Content API API from Yext — 2 operation(s) for content api.
  name: Yext Content API API
  slug: yext-content-api-api
- description: The Domains API from Yext — 7 operation(s) for domains.
  name: Yext Domains API
  slug: yext-domains-api
- description: The Health Check API from Yext — 1 operation(s) for health check.
  name: Yext Health Check API
  slug: yext-health-check-api
- description: The Knowledge Manager API from Yext — 30 operation(s) for knowledge manager.
  name: Yext Knowledge Manager API
  slug: yext-knowledge-manager-api
- description: The Licenses API from Yext — 3 operation(s) for licenses.
  name: Yext Licenses API
  slug: yext-licenses-api
- description: The Listings API from Yext — 26 operation(s) for listings.
  name: Yext Listings API
  slug: yext-listings-api
- description: The Lists API from Yext — 1 operation(s) for lists.
  name: Yext Lists API
  slug: yext-lists-api
- description: The Live API API from Yext — 21 operation(s) for live api.
  name: Yext Live API API
  slug: yext-live-api-api
- description: The LogsAPI API from Yext — 3 operation(s) for logsapi.
  name: Yext LogsAPI API
  slug: yext-logsapi-api
- description: The Optimization Tasks API from Yext — 2 operation(s) for optimization tasks.
  name: Yext Optimization Tasks API
  slug: yext-optimization-tasks-api
- description: The Plpixel API from Yext — 1 operation(s) for plpixel.
  name: Yext Plpixel API
  slug: yext-plpixel-api
- description: The Publisher Disruptions API from Yext — 2 operation(s) for publisher disruptions.
  name: Yext Publisher Disruptions API
  slug: yext-publisher-disruptions-api
- description: The Webhooks API from Yext — 0 operation(s) for webhooks.
  name: Yext Webhooks API
  slug: yext-publisher-notify-review-api
- description: The Reviews API from Yext — 14 operation(s) for reviews.
  name: Yext Reviews API
  slug: yext-reviews-api
- description: The Social API from Yext — 10 operation(s) for social.
  name: Yext Social API
  slug: yext-social-api
- description: The Suggestions API from Yext — 2 operation(s) for suggestions.
  name: Yext Suggestions API
  slug: yext-suggestions-api
artifact_total: 40
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yext-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yext-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yext-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.yext.com
- group: docs
  title: ''
  type: Documentation
  url: https://hitchhikers.yext.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yext.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/yext
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yext
- group: company
  title: ''
  type: Blog
  url: https://www.yext.com/blog
- group: company
  title: ''
  type: Blog
  url: https://developer.yext.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yext.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.yexttrust.com/
- group: other
  title: ''
  type: X
  url: https://x.com/yext
- group: commercial
  title: ''
  type: Plans
  url: plans/yext-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yext-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yext-finops.yml
created: '2026-06-13'
description: Yext is a digital presence platform that enables businesses to manage their listings across 200+ publishers, update location data, manage reviews, and power AI search experiences. Its REST APIs provide programmatic access to the Knowledge Graph, Listings, Reviews, Analytics, and Content Delivery capabilities.
examples:
- key_count: 2
  name: Yext Chat Message Example
  slug: yext-chat-message-example
- key_count: 2
  name: Yext Listing Status Example
  slug: yext-listing-status-example
- key_count: 2
  name: Yext Location Entity Example
  slug: yext-location-entity-example
- key_count: 2
  name: Yext Search Query Example
  slug: yext-search-query-example
- key_count: 5
  name: Yext Webhook Entity Update Example
  slug: yext-webhook-entity-update-example
finops:
- name: Yext Finops
  service_category: ''
  slug: yext-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yext.png
json_schemas:
- name: Yext Address
  property_count: 8
  slug: yext-address
- name: Yext Entity
  property_count: 4
  slug: yext-entity
- name: Yext Hours
  property_count: 4
  slug: yext-hours
- name: Yext Search Query Response
  property_count: 2
  slug: yext-search-query
jsonld:
- class_count: 14
  name: Yext Context
  property_count: 75
  slug: yext-context
layout: provider
modified: '2026-06-13'
name: Yext
nav: Providers
network: true
overview: 'Yext publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Account Settings API, Accounts API, Administrative API API, and 20 more. Tagged areas include Digital Presence, Business Listings, Location Data, Reviews, and AI Search.


  The Yext catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yext''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Yext Plans Pricing
  plan_count: 5
  slug: yext-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Yext Rate Limits
  slug: yext-rate-limits
rules:
- name: Yext API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: yext-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.4
  delta: -4.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yext/refs/heads/main/screenshots/yext-2026-06-20T201740.png
security:
- kind: authentication
  name: Yext Authentication
  slug: yext-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Yext Domain Security
  slug: yext-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yext
tags:
- Digital Presence
- Business Listings
- Location Data
- Reviews
- AI Search
- Knowledge Graph
website: https://www.yext.com
---

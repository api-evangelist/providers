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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Goatcounter Agentic Access
  operation_count: 16
  slug: goatcounter-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 6
apis:
- description: The Exports API from GoatCounter — 3 operation(s) for exports.
  name: GoatCounter Exports API
  slug: goatcounter-exports-api
- description: The Pageviews API from GoatCounter — 1 operation(s) for pageviews.
  name: GoatCounter Pageviews API
  slug: goatcounter-pageviews-api
- description: The Paths API from GoatCounter — 1 operation(s) for paths.
  name: GoatCounter Paths API
  slug: goatcounter-paths-api
- description: The Sites API from GoatCounter — 2 operation(s) for sites.
  name: GoatCounter Sites API
  slug: goatcounter-sites-api
- description: The Statistics API from GoatCounter — 5 operation(s) for statistics.
  name: GoatCounter Statistics API
  slug: goatcounter-statistics-api
- description: The Users API from GoatCounter — 1 operation(s) for users.
  name: GoatCounter Users API
  slug: goatcounter-users-api
artifact_total: 13
collections:
- collection_type: open
  name: GoatCounter API
  slug: open-goatcounter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goatcounter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goatcounter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goatcounter-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.goatcounter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.goatcounter.com/help/api
- group: start
  title: ''
  type: Signup
  url: https://www.goatcounter.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arp242/goatcounter
created: '2025-02-08'
description: The GoatCounter API can be used to manage sites, users, count pageviews, export raw data, retrieve statistics, and build custom dashboards on top of GoatCounter web analytics.
finops:
- name: Goatcounter Finops
  service_category: API
  slug: goatcounter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goatcounter.png
layout: provider
modified: '2026-05-19'
name: GoatCounter
nav: Providers
network: true
overview: 'GoatCounter publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Exports API, Pageviews API, Paths API, and 3 more. Tagged areas include Analytics, Pageviews, Privacy, Statistics, and Web Analytics.


  GoatCounter''s developer surface includes authentication, documentation, signup flow, and 4 more developer resources.'
plans:
- name: Goatcounter Plans Pricing
  plan_count: 3
  slug: goatcounter-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Goatcounter Rate Limits
  slug: goatcounter-rate-limits
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.9
    developer_ergonomics: 19.6
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goatcounter/refs/heads/main/screenshots/goatcounter-2026-06-20T181940.png
security:
- kind: authentication
  name: Goatcounter Authentication
  slug: goatcounter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Goatcounter Domain Security
  slug: goatcounter-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: goatcounter
tags:
- Analytics
- Pageviews
- Privacy
- Statistics
- Web Analytics
website: https://www.goatcounter.com/
---

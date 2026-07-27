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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Meltwater Agentic Access
  operation_count: 80
  slug: meltwater-agentic-access
  summary_line: 80 operations · 32 acting
api_count: 12
apis:
- description: Account Management API and Usage APIs
  name: Meltwater Account Management API
  slug: meltwater-account-management-api
- description: Upload your own content into the Meltwater Platform.
  name: Meltwater Bring Your Own Content (BYOC) API
  slug: meltwater-bring-your-own-content-byoc-api
- description: Fetch analytics on data within your private index.
  name: Meltwater Explore+ Analytics API
  slug: meltwater-explore-analytics-api
- description: Manage your Explore+ assets including searches and custom fields.
  name: Meltwater Explore+ Assets API
  slug: meltwater-explore-assets-api
- description: Export earned documents from your private index.
  name: Meltwater Explore+ Search API
  slug: meltwater-explore-search-api
- description: Analyse multiple types of Meltwater data, run volume time series, top tags and sentiment counts.
  name: Meltwater Listening Analytics API
  slug: meltwater-listening-analytics-api
- description: Data exports for onetime and recurring jobs.
  name: Meltwater Listening Exports API
  slug: meltwater-listening-exports-api
- description: Search Meltwater data using saved searches to integrate with your own API connectors and internal systems.
  name: Meltwater Listening Search API
  slug: meltwater-listening-search-api
- description: Manage Saved Searches
  name: Meltwater Listening Search Management API
  slug: meltwater-listening-search-management-api
- description: Streaming of Meltwater data to integrate with your internal systems and workflows.
  name: Meltwater Listening Streaming API
  slug: meltwater-listening-streaming-api
- description: AI-powered chat completion and project listing features.
  name: Meltwater Mira API API
  slug: meltwater-mira-api-api
- description: Retrieve owned social metrics and analytics.
  name: Meltwater Owned Analytics API
  slug: meltwater-owned-analytics-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meltwater-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meltwater-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meltwater-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meltwater-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.meltwater.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.meltwater.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/meltwater
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meltwater
- group: company
  title: ''
  type: Blog
  url: https://www.meltwater.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meltwater.com/en/suite/data-api-integration
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.meltwater.com
- group: other
  title: ''
  type: X
  url: https://x.com/Meltwater
- group: commercial
  title: ''
  type: Plans
  url: plans/meltwater-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meltwater-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/meltwater-finops.yml
created: '2026-06-13'
description: Meltwater is a media intelligence platform providing REST APIs for media monitoring, social listening, journalist outreach, PR analytics, and brand reputation management. The API enables programmatic access to billions of editorial, blog, and social media conversations across news sources and social networks, with capabilities for searching, exporting, streaming, and analyzing mentions, as well as fetching owned social account analytics.
examples:
- key_count: 80
  name: Meltwater Api Examples
  slug: meltwater-api-examples
finops:
- name: Meltwater Finops
  service_category: ''
  slug: meltwater-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meltwater.png
json_schemas:
- name: Meltwater API Schemas
  property_count: 0
  slug: meltwater-schemas
jsonld:
- class_count: 52
  name: Meltwater Api Context
  property_count: 1
  slug: meltwater-api
layout: provider
modified: '2026-06-13'
name: Meltwater
nav: Providers
network: true
overview: 'Meltwater publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Bring Your Own Content (BYOC) API, Explore+ Analytics API, and 9 more. Tagged areas include Media Monitoring, Social Listening, PR Analytics, Brand Intelligence, and News API.


  The Meltwater catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Meltwater''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Meltwater Plans Pricing
  plan_count: 3
  slug: meltwater-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Meltwater Rate Limits
  slug: meltwater-rate-limits
rules:
- name: Meltwater API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: meltwater-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.6
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 54.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meltwater/refs/heads/main/screenshots/meltwater-2026-06-20T185137.png
security:
- kind: authentication
  name: Meltwater Authentication
  slug: meltwater-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Meltwater Domain Security
  slug: meltwater-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meltwater Vulnerability Disclosure
  slug: meltwater-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meltwater
tags:
- Media Monitoring
- Social Listening
- PR Analytics
- Brand Intelligence
- News API
- Social Analytics
- Media Intelligence
website: https://www.meltwater.com
---

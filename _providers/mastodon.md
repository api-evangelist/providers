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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: This is an OpenAPI for the Mastodon API.
  name: Mastodon API
  slug: mastodon
artifact_total: 8
asyncapis:
- description: 'AsyncAPI 2.6 description of the Mastodon real-time surface. Mastodon exposes two complementary asynchronous interfaces: * Streaming API - delivers timeline and notification events to a connected clien'
  name: Mastodon Streaming and Web Push API
  slug: mastodon-streaming
collections:
- collection_type: open
  name: Mastodon API
  slug: open-mastodon
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mastodon-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mastodon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/joinmastodon
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinmastodon.org/client/intro/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.joinmastodon.org/api/rate-limits/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.joinmastodon.org/api/oauth-tokens/
- group: auth
  title: ''
  type: OauthScopes
  url: https://docs.joinmastodon.org/api/oauth-scopes/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/mastodon/overview
- group: company
  title: ''
  type: Blog
  url: https://blog.joinmastodon.org/index.xml
created: '2024-11-16'
description: Mastodon is a open source, self-hosted, social networking service. Mastodon uses the ActivityPub protocol for federation which allows users to communicate between independent Mastodon instances and other ActivityPub compatible services. Mastodon has microblogging features similar to Twitter, and is generally considered to be a part of the Fediverse.
finops:
- name: Mastodon Finops
  service_category: API
  slug: mastodon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mastodon.png
layout: provider
modified: '2026-05-30'
name: Mastodon
nav: Providers
network: true
overview: 'Mastodon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open-Source and Social Networks.


  The Mastodon catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mastodon''s developer surface includes getting-started guide, authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Mastodon Plans Pricing
  plan_count: 3
  slug: mastodon-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 5
  name: Mastodon Rate Limits
  slug: mastodon-rate-limits
rules:
- name: Mastodon API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: mastodon-asyncapi-spectral-rules
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 41.9
    developer_ergonomics: 28.3
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 13.2
  previous_composite: 31.0
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mastodon/refs/heads/main/screenshots/mastodon-2026-06-20T185024.png
security:
- kind: domain-security
  name: Mastodon Domain Security
  slug: mastodon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mastodon
tags:
- Open-Source
- Social Networks
---

---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: A REST API delivering consistently formatted jokes with filtering by category, language, content flags, and joke type. Supports multiple response formats and requires no authentication.
  name: JokeAPI
  slug: joke-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/joke-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jokeapi.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://jokeapi.dev/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Sv443-Network
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sv443.net/
- group: commercial
  title: ''
  type: Plans
  url: plans/joke-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/joke-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/joke-api-finops.yml
created: '2026-06-13'
description: JokeAPI is a free, open-source REST API that delivers consistently formatted jokes with no authentication, registration, or payment required. It provides over 1,368 jokes across categories including Programming, Misc, Dark, Pun, Spooky, and Christmas in 6 languages. The API supports rich filtering by category, language, content flags (NSFW, Religious, Political, Racist, Sexist, Explicit), and joke type (single or two-part). Response formats include JSON, XML, YAML, and plain text. A safe mode ensures family-friendly content for appropriate applications.
finops:
- name: Joke Api Finops
  service_category: ''
  slug: joke-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/joke-api.png
layout: provider
modified: '2026-06-13'
name: JokeAPI
nav: Providers
network: true
overview: 'JokeAPI publishes 1 API on the [APIs.io](https://apis.io/) network: JokeAPI. Tagged areas include Jokes, Humor, Entertainment, Programming Jokes, and Dark Humor.


  JokeAPI''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Joke Api Plans Pricing
  plan_count: 1
  slug: joke-api-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 0
  name: Joke Api Rate Limits
  slug: joke-api-rate-limits
score:
  band: emerging
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 37.7
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/joke-api/refs/heads/main/screenshots/joke-api-2026-06-20T183754.png
security:
- kind: domain-security
  name: Joke Api Domain Security
  slug: joke-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: joke-api
tags:
- Jokes
- Humor
- Entertainment
- Programming Jokes
- Dark Humor
- Puns
- Free API
- Open Source
website: https://jokeapi.dev/
---

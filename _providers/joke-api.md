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
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 19.4
  scored_at: '2026-08-03'
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
random_paper: 24
rate_limits:
- limit_count: 2
  name: Joke Api Rate Limits
  slug: joke-api-rate-limits
score:
  band: emerging
  composite: 27.9
  delta: 2.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 25.2
  schema_version: 0.9
  scored_at: '2026-08-03'
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

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
    agentic_access: true
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
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dad Jokes Agentic Access
  operation_count: 6
  slug: dad-jokes-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 2
apis:
- description: Slack and Discord integration endpoints
  name: Dad Jokes (icanhazdadjoke) Integrations API
  slug: dad-jokes-integrations-api
- description: Dad joke retrieval and search
  name: Dad Jokes (icanhazdadjoke) Jokes API
  slug: dad-jokes-jokes-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dad-jokes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dad-jokes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://icanhazdadjoke.com/
- group: docs
  title: ''
  type: Documentation
  url: https://icanhazdadjoke.com/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/brettlangdon
- group: other
  title: ''
  type: X
  url: https://twitter.com/icanhazdadjoke
- group: commercial
  title: ''
  type: Plans
  url: plans/dad-jokes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dad-jokes-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dad-jokes-finops.yml
created: '2026-06-13'
description: icanhazdadjoke is a free REST API providing access to the internet's largest selection of dad jokes. It offers random joke retrieval, a searchable joke database, Slack slash command integration, Discord bot support, and plain-text or JSON responses — all with no authentication required.
examples:
- key_count: 1
  name: Graphql Query
  slug: graphql-query
- key_count: 1
  name: Graphql Response
  slug: graphql-response
- key_count: 3
  name: Random Joke Response
  slug: random-joke-response
- key_count: 9
  name: Search Jokes Response
  slug: search-jokes-response
- key_count: 3
  name: Slack Response
  slug: slack-response
finops:
- name: Dad Jokes Finops
  service_category: ''
  slug: dad-jokes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dad-jokes.png
json_schemas:
- name: JokeSearchResults
  property_count: 9
  slug: joke-search-results
- name: Joke
  property_count: 3
  slug: joke
- name: SlackResponse
  property_count: 3
  slug: slack-response
jsonld:
- class_count: 1
  name: Dad Jokes Context
  property_count: 11
  slug: dad-jokes-context
layout: provider
modified: '2026-06-13'
name: Dad Jokes (icanhazdadjoke)
nav: Providers
network: true
overview: 'Dad Jokes (icanhazdadjoke) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Integrations API and Jokes API. Tagged areas include Dad Jokes, Humor, Comedy, Random, and Jokes.


  The Dad Jokes (icanhazdadjoke) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dad Jokes (icanhazdadjoke)''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Dad Jokes Plans Pricing
  plan_count: 1
  slug: dad-jokes-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Dad Jokes Rate Limits
  slug: dad-jokes-rate-limits
rules:
- name: Dad Jokes (icanhazdadjoke) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dad-jokes-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.3
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 41.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dad-jokes/refs/heads/main/screenshots/dad-jokes-2026-06-20T175419.png
security:
- kind: domain-security
  name: Dad Jokes Domain Security
  slug: dad-jokes-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: dad-jokes
tags:
- Dad Jokes
- Humor
- Comedy
- Random
- Jokes
- Slack
- Discord
website: https://icanhazdadjoke.com/
---

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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chuck Norris Agentic Access
  operation_count: 4
  slug: chuck-norris-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Chuck Norris joke operations
  name: Chuck Norris API jokes API
  slug: chuck-norris-jokes-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chuck-norris-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chuck-norris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.chucknorris.io
- group: docs
  title: ''
  type: Documentation
  url: https://api.chucknorris.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/chucknorris-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chucknorris-io
- group: company
  title: ''
  type: Blog
  url: https://api.chucknorris.io
- group: commercial
  title: ''
  type: Pricing
  url: https://api.chucknorris.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chucknorris.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/MatChilling
- group: commercial
  title: ''
  type: Plans
  url: plans/chuck-norris-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chuck-norris-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chuck-norris-finops.yml
created: '2026-06-13'
description: Free REST API providing random Chuck Norris jokes, categories, and the ability to search the joke database with no authentication required. The service is hosted on AWS and supported by Jugendstil.io sponsorship, making it permanently free for developers. Responses are returned as JSON and include a joke identifier, URL, icon, and the joke text. Integrations are available for Slack and Facebook Messenger.
examples:
- key_count: 7
  name: Random Joke
  slug: random-joke
- key_count: 2
  name: Search Result
  slug: search-result
finops:
- name: Chuck Norris Finops
  service_category: ''
  slug: chuck-norris-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chuck-norris.png
json_schemas:
- name: JokeSearchResult
  property_count: 2
  slug: joke-search-result
- name: Joke
  property_count: 7
  slug: joke
jsonld:
- class_count: 4
  name: context Context
  property_count: 8
  slug: context
layout: provider
modified: '2026-06-13'
name: Chuck Norris API
nav: Providers
network: true
overview: 'Chuck Norris API publishes 1 API on the [APIs.io](https://apis.io/) network: jokes API. Tagged areas include Jokes, Humor, Entertainment, Chuck Norris, and Free.


  The Chuck Norris API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chuck Norris API''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Chuck Norris Plans Pricing
  plan_count: 1
  slug: chuck-norris-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 0
  name: Chuck Norris Rate Limits
  slug: chuck-norris-rate-limits
rules:
- name: Chuck Norris API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chuck-norris-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.1
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chuck-norris/refs/heads/main/screenshots/chuck-norris-2026-06-20T174331.png
security:
- kind: domain-security
  name: Chuck Norris Domain Security
  slug: chuck-norris-domain-security
  summary_line: TLSv1.3
slug: chuck-norris
tags:
- Jokes
- Humor
- Entertainment
- Chuck Norris
- Free
website: https://api.chucknorris.io
---

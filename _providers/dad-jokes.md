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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dad Jokes Agentic Access
  operation_count: 6
  slug: dad-jokes-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://icanhazdadjoke.com
  baseurl_source: declared
  description: Slack and Discord integration endpoints
  name: Dad Jokes (icanhazdadjoke) Integrations API
  slug: dad-jokes-integrations-api
- baseURL: https://icanhazdadjoke.com
  baseurl_source: declared
  description: Dad joke retrieval and search
  name: Dad Jokes (icanhazdadjoke) Jokes API
  slug: dad-jokes-jokes-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: icanhazdadjoke Integrations API
  slug: open-dad-jokes-integrations-api
- collection_type: open
  name: icanhazdadjoke Integrations Jokes API
  slug: open-dad-jokes-jokes-api
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
random_paper: 0
rate_limits:
- limit_count: 0
  name: Dad Jokes Rate Limits
  slug: dad-jokes-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Dad Jokes (icanhazdadjoke) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dad-jokes-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 59.3
    catalog_earned_first_party: 0.0
    catalog_gap: 55.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 56.5
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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

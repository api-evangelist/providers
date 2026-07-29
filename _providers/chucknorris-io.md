---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chucknorris Io Agentic Access
  operation_count: 4
  slug: chucknorris-io-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Joke category metadata.
  name: chucknorris.io Categories API
  slug: chucknorris-io-categories-api
- description: Chuck Norris jokes (facts) endpoints.
  name: chucknorris.io Jokes API
  slug: chucknorris-io-jokes-api
- description: Full-text search across the joke corpus.
  name: chucknorris.io Search API
  slug: chucknorris-io-search-api
artifact_total: 40
collections:
- collection_type: open
  name: Chuck Norris Jokes API
  slug: open-chucknorris-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chucknorris-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chucknorris-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.chucknorris.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chucknorris-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/chucknorris-io/chuck-api
- group: commercial
  title: ''
  type: License
  url: https://github.com/chucknorris-io/chuck-api/blob/master/LICENSE
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/chucknorris-io-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/chucknorris-io-vocabulary.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chucknorris-io/client-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chucknorris-io/client-java
- group: build
  title: ''
  type: Tools
  url: ''
created: '2026-05-28'
description: Free JSON REST API for hand-curated Chuck Norris jokes (facts) maintained by @matchilling. Supports random retrieval, category filtering, full-text search, and direct lookup by joke identifier. Hosted at api.chucknorris.io with an open-source Spring Boot service (chuck-api), official Node.js and Java client SDKs, a Chrome extension, a Storybook addon, and Messenger / Alexa companion apps published under the chucknorris-io GitHub organization.
examples:
- key_count: 4
  name: Chucknorris Io Error Example
  slug: chucknorris-io-error-example
- key_count: 5
  name: Chucknorris Io Getjokebyid Example
  slug: chucknorris-io-getJokeById-example
- key_count: 5
  name: Chucknorris Io Getrandomjoke By Category Example
  slug: chucknorris-io-getRandomJoke-by-category-example
- key_count: 5
  name: Chucknorris Io Getrandomjoke Example
  slug: chucknorris-io-getRandomJoke-example
- key_count: 7
  name: Chucknorris Io Joke Example
  slug: chucknorris-io-joke-example
- key_count: 5
  name: Chucknorris Io Listcategories Example
  slug: chucknorris-io-listCategories-example
- key_count: 2
  name: Chucknorris Io Search Result Example
  slug: chucknorris-io-search-result-example
- key_count: 5
  name: Chucknorris Io Searchjokes Example
  slug: chucknorris-io-searchJokes-example
features:
- description: GET /jokes/random returns a single random Chuck Norris fact.
  name: Random Joke
- description: GET /jokes/random?category={category} constrains random selection.
  name: Random Joke By Category
- description: GET /jokes/categories returns the 16 supported category identifiers.
  name: List Categories
- description: GET /jokes/search?query={query} returns matching jokes with a total count.
  name: Free-Text Search
- description: GET /jokes/{id} retrieves a single joke by its identifier.
  name: Lookup By Id
- description: All endpoints honor Accept text/plain for shell-friendly output.
  name: Plain-Text Variant
image: https://api.chucknorris.io/img/avatar/chuck-norris.png
integrations:
- description: Slack slash command integration referenced in the public docs.
  name: Slack
- description: Companion Messenger bot (chucknorris-io/app-facebook-messenger).
  name: Facebook Messenger
- description: Companion Alexa skill (chucknorris-io/app-alexa-skill).
  name: Alexa
- description: Official Chrome extension surfacing facts in the browser.
  name: Google Chrome
- description: Storybook addon injecting Chuck Norris facts into dev workflows.
  name: Storybook
json_schemas:
- name: CategoryList
  property_count: 0
  slug: chucknorris-io-category-list
- name: Error
  property_count: 5
  slug: chucknorris-io-error
- name: Joke
  property_count: 7
  slug: chucknorris-io-joke
- name: SearchResult
  property_count: 2
  slug: chucknorris-io-search-result
json_structures:
- name: Chucknorris Io Category List Structure
  property_count: 0
  slug: chucknorris-io-category-list-structure
- name: Chucknorris Io Error Structure
  property_count: 5
  slug: chucknorris-io-error-structure
- name: Chucknorris Io Joke Structure
  property_count: 7
  slug: chucknorris-io-joke-structure
- name: Chucknorris Io Search Result Structure
  property_count: 2
  slug: chucknorris-io-search-result-structure
jsonld:
- class_count: 5
  name: Chucknorris Io Context
  property_count: 8
  slug: chucknorris-io-context
layout: provider
modified: '2026-05-30'
name: chucknorris.io
nav: Providers
network: true
overview: 'chucknorris.io publishes 3 APIs on the [APIs.io](https://apis.io/) network: Categories API, Jokes API, and Search API. Tagged areas include Entertainment, Jokes, Chuck Norris, Open Source, and Public APIs.


  The chucknorris.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  chucknorris.io''s developer surface includes tooling and 10 more developer resources.'
random_paper: 70
rules:
- name: chucknorris.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chucknorris-io-jsonschema-spectral-rules
- name: chucknorris.io API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: chucknorris-io-rules
score:
  band: thin
  composite: 36.7
  delta: -3.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 73.4
    developer_ergonomics: 6.5
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chucknorris-io/refs/heads/main/screenshots/chucknorris-io-2026-06-20T174333.png
security:
- kind: domain-security
  name: Chucknorris Io Domain Security
  slug: chucknorris-io-domain-security
  summary_line: TLSv1.3
slug: chucknorris-io
tags:
- Entertainment
- Jokes
- Chuck Norris
- Open Source
- Public APIs
use_cases:
- description: Tutorial-friendly free public API for learning HTTP clients, SDKs, and AI tool patterns.
  name: Demo Data Source
- description: Slack, Messenger, and Alexa surfaces inject random facts on demand.
  name: Chat & Bot Surfaces
- description: Storybook addon and Chrome extension use the API to entertain developers.
  name: Developer Toy
- description: Lightweight, no-auth endpoints are useful targets for HTTP client smoke tests.
  name: Load & Reliability Testing
website: https://api.chucknorris.io
---

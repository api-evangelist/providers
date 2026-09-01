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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ron Swanson Quotes Agentic Access
  operation_count: 3
  slug: ron-swanson-quotes-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Read-only operations that return one or more Ron Swanson quotes from the static quote corpus.
  name: Ron Swanson Quotes Quotes API
  slug: ron-swanson-quotes-quotes-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ron Swanson Quotes API
  slug: open-ron-swanson-quotes-quotes-api
- collection_type: open
  name: Ron Swanson Quotes API
  slug: open-ron-swanson-quotes
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jamesseanwright/ron-swanson-quotes/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/jamesseanwright/ron-swanson-quotes/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ron-swanson-quotes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ron-swanson-quotes-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jamesseanwright/ron-swanson-quotes
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/jamesseanwright/ron-swanson-quotes/blob/master/CHANGELOG.md
- group: auth
  title: No Authentication Required
  type: Authentication
  url: https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api
- group: operate
  title: Per-Client Rate Limit Headers
  type: RateLimits
  url: https://github.com/jamesseanwright/ron-swanson-quotes#ron-swanson-quotes-api
- group: build
  title: Hubot Swanson (npm) - Chatbot Integration by Author
  type: SDKs
  url: https://github.com/jamesseanwright/hubot-swanson
- group: build
  title: Browser JavaScript Demo (JSFiddle)
  type: CodeExamples
  url: http://jsfiddle.net/7g2w4dhc/27/
- group: commercial
  title: Apache License 2.0
  type: License
  url: https://github.com/jamesseanwright/ron-swanson-quotes/blob/master/LICENCE
- group: design
  title: Ron Swanson Quotes Spectral Ruleset
  type: SpectralRules
  url: rules/ron-swanson-quotes-rules.yml
- group: design
  title: Ron Swanson Quotes JSON-LD Context
  type: JSONLD
  url: json-ld/ron-swanson-quotes-context.jsonld
- group: design
  title: Ron Swanson Quotes Vocabulary
  type: Vocabulary
  url: vocabulary/ron-swanson-quotes-vocabulary.yml
created: '2026-05-28'
description: A community-built, open source HTTP API that returns Ron Swanson quotes from the NBC television series Parks and Recreation. Returns one or more quotes per request as a JSON array of strings, with an optional case-insensitive full-text search over the quote corpus. The service is a small Node.js / TypeScript Express app authored by James Wright and hosted on Heroku.
examples:
- key_count: 2
  name: Ron Swanson Quotes Rate Limit Error Example
  slug: ron-swanson-quotes-rate-limit-error-example
features:
- description: Return a single random Ron Swanson quote as a one-element JSON array.
  name: Random Quote
- description: Return N random Ron Swanson quotes in a single response via /quotes/{count}.
  name: Batch Random Quotes
- description: Search the quote corpus for a substring with case-insensitive matching via /quotes/search/{term}; returns every matching quote.
  name: Full-Text Search
- description: Public endpoint with no API key, OAuth, or signup required.
  name: No Authentication
- description: Access-Control-Allow-Origin is set to * so the API can be called directly from any browser-based frontend without a proxy.
  name: CORS Enabled
- description: Live OpenAPI 3.0 specification served by the API itself at GET /v2/schema, contributed by Chris Gali.
  name: Self-Describing OpenAPI 3.0 Schema
- description: Standard X-RateLimit-Limit / X-RateLimit-Remaining / X-RateLimit-Reset headers are returned on every response.
  name: Rate Limit Headers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ron-swanson-quotes.png
integrations:
- description: Official Hubot script (hubot-swanson, by the API author) that pulls quotes into Hubot-powered chatops bots.
  name: Hubot
- description: Service is deployed on the Heroku platform; the production host is ron-swanson-quotes.herokuapp.com.
  name: Heroku
- description: Multiple community-built Amazon Alexa skills consume this API to read Ron Swanson quotes on Echo devices.
  name: Alexa Skills
- description: Used as a quote source by various community chatbots.
  name: Slack and Discord Bots
json_schemas:
- name: QuoteList
  property_count: 0
  slug: ron-swanson-quotes-quote-list
- name: Quote
  property_count: 0
  slug: ron-swanson-quotes-quote
- name: RateLimitError
  property_count: 2
  slug: ron-swanson-quotes-rate-limit-error
json_structures:
- name: Ron Swanson Quotes Quote List Structure
  property_count: 0
  slug: ron-swanson-quotes-quote-list-structure
- name: Ron Swanson Quotes Quote Structure
  property_count: 0
  slug: ron-swanson-quotes-quote-structure
- name: Ron Swanson Quotes Rate Limit Error Structure
  property_count: 2
  slug: ron-swanson-quotes-rate-limit-error-structure
jsonld:
- class_count: 4
  name: Ron Swanson Quotes Context
  property_count: 6
  slug: ron-swanson-quotes-context
layout: provider
modified: '2026-05-30'
name: Ron Swanson Quotes
nav: Providers
network: true
overview: 'Ron Swanson Quotes publishes 1 API on the [APIs.io](https://apis.io/) network: Quotes API. Tagged areas include Entertainment, Television, Parks and Recreation, Quotes, and Open-Source.


  The Ron Swanson Quotes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ron Swanson Quotes'' developer surface includes documentation, changelog, authentication, code examples, and 12 more developer resources.'
random_paper: 6
rules:
- effective_rule_count: 4
  extends: []
  name: Ron Swanson Quotes API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: ron-swanson-quotes-jsonschema-spectral-rules
- effective_rule_count: 78
  extends:
  - spectral:oas
  name: Ron Swanson Quotes API Rules
  rule_count: 37
  severity_counts:
    error: 17
    hint: 0
    info: 6
    warn: 14
  slug: ron-swanson-quotes-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 66.7
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ron-swanson-quotes/refs/heads/main/screenshots/ron-swanson-quotes-2026-06-20T193218.png
security:
- kind: domain-security
  name: Ron Swanson Quotes Domain Security
  slug: ron-swanson-quotes-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: ron-swanson-quotes
tags:
- Entertainment
- Television
- Parks and Recreation
- Quotes
- Open-Source
- Public APIs
- Node.js
- TypeScript
- Heroku
- REST
use_cases:
- description: Widely used in beginner Node.js, JavaScript, and HTTP tutorials and bootcamp coursework as a friendly, no-auth public API to learn fetch, async/await, and JSON parsing.
  name: API Tutorial Fixture
- description: Powers Alexa skills and other voice-assistant demos that deliver a Ron Swanson quote on request.
  name: Voice Assistant Skill
- description: Supplies the underlying quote source for Hubot, Slack, and Discord bot examples (see hubot-swanson npm package by the same author).
  name: Chatbot Integration
- description: CORS-enabled endpoint makes it suitable for in-browser SPA demos (React, Vue, Svelte) without requiring a backend proxy.
  name: Frontend Demo App
- description: Stable shape and no auth make it a practical test target for HTTP-client libraries and SDK generators.
  name: API Client Library Test Target
- description: Used in conference talks and workshops to illustrate REST, OpenAPI-from-code, and API mocking concepts.
  name: Workshop and Conference Demo
---

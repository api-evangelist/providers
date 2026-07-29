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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Numbers Agentic Access
  operation_count: 10
  slug: numbers-agentic-access
  summary_line: 10 operations
api_count: 5
apis:
- description: Multiple facts returned in a single request as a JSON map.
  name: Numbers API Batch API
  slug: numbers-batch-api
- description: Historical facts associated with a day of the year.
  name: Numbers API Date API
  slug: numbers-date-api
- description: Mathematical properties of integers.
  name: Numbers API Math API
  slug: numbers-math-api
- description: Trivia facts about integers.
  name: Numbers API Trivia API
  slug: numbers-trivia-api
- description: Historical facts associated with a year.
  name: Numbers API Year API
  slug: numbers-year-api
artifact_total: 44
collections:
- collection_type: open
  name: Numbers API
  slug: open-numbers
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/numbers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numbers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://numbersapi.com/
- group: docs
  title: ''
  type: Documentation
  url: http://numbersapi.com/#api
- group: company
  title: ''
  type: Blog
  url: http://david-hu.com/2012/03/05/announcing-numbers-api.html
- group: operate
  title: ''
  type: Contact
  url: mailto:numbersapi@gmail.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/numbers-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/numbers-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/numbers-context.jsonld
created: '2026-05-28'
description: Numbers API by David Hu and Mack Duan — a free, community-contributed HTTP API for interesting facts about numbers. Returns trivia, math, date, and year facts as plain text or JSON. Supports random numbers, ranges/batches, JSONP callbacks, document.write embedding, sentence-fragment responses, and configurable not-found behavior.
examples:
- key_count: 4
  name: Numbers Batch Facts Example
  slug: numbers-batch-facts-example
- key_count: 5
  name: Numbers Date Fact Example
  slug: numbers-date-fact-example
- key_count: 4
  name: Numbers Fact Example
  slug: numbers-fact-example
- key_count: 4
  name: Numbers Math Fact Example
  slug: numbers-math-fact-example
- key_count: 4
  name: Numbers Trivia Fact Example
  slug: numbers-trivia-fact-example
- key_count: 4
  name: Numbers Year Fact Example
  slug: numbers-year-fact-example
features:
- description: Return a piece of trivia about a number, e.g. `42 is the number of little squares forming the left side trail of Microsoft's Windows 98 logo`.
  name: Trivia Facts
- description: Return a mathematical property of a number, e.g. `5 is the number of platonic solids`.
  name: Math Facts
- description: Return a fact about a day of the year (month/day), e.g. `February 29 is the day in 1504 that Christopher Columbus uses his knowledge of a lunar eclipse to convince Native Americans to provide him with supplies`.
  name: Date Facts
- description: Return a fact about a year, e.g. `1969 is the year that an estimated 500 million people worldwide watch Neil Armstrong take his historic first steps on the Moon`.
  name: Year Facts
- description: Use the keyword `random` in place of a number to get a random fact, optionally bounded by `min` and `max` query parameters.
  name: Random Numbers
- description: 'Append `?json` (or send `Content-Type: application/json`) to receive the fact wrapped in an object with `text`, `found`, `number`, `type`, and optional `date`/`year` fields.'
  name: JSON Responses
- description: Append `?fragment` to get the fact rephrased as a lowercase, no- terminal-punctuation fragment suitable for embedding in a larger sentence.
  name: Sentence Fragment Mode
- description: Use `notfound=default|floor|ceil` to control what happens when no fact exists for the requested number, with an optional custom `default=...` message.
  name: Configurable Not Found Behavior
- description: Pass `callback=functionName` to wrap the response in a JSONP function call.
  name: JSONP Callback
- description: Pass `write` to wrap the response in `document.write(...)`, allowing a single `<script src="...">` to render the fact inline.
  name: Document.write Embed
- description: Request facts for multiple numbers in one call using comma-separated values and `min..max` ranges (up to 100 numbers), returned as a JSON map.
  name: Batch Requests
- description: Supports cross-origin requests, allowing direct browser calls from any domain.
  name: CORS Support
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numbers.png
integrations:
- description: The docs show a `$.get()` example loading a trivia fact directly into a DOM element.
  name: jQuery
- description: Direct cross-origin requests via fetch/XHR are supported because the service emits permissive CORS headers.
  name: Browser JavaScript
- description: The `callback` query parameter lets legacy JSONP clients consume facts as `functionName("...")` invocations.
  name: JSONP Consumers
- description: The `write` query parameter wraps responses in `document.write()`, so a single `<script src="numbersapi.com/...">` tag can render a fact inline in static HTML.
  name: HTML script tag
- description: Listed in public-apis/public-apis under the Science & Math category as a free, no-auth API.
  name: Public APIs Directory
json_schemas:
- name: BatchFacts
  property_count: 0
  slug: numbers-batch-facts
- name: Fact
  property_count: 6
  slug: numbers-fact
json_structures:
- name: Numbers Batch Facts Structure
  property_count: 0
  slug: numbers-batch-facts-structure
- name: Numbers Fact Structure
  property_count: 6
  slug: numbers-fact-structure
jsonld:
- class_count: 2
  name: Numbers Context
  property_count: 6
  slug: numbers-context
layout: provider
modified: '2026-05-30'
name: Numbers API
nav: Providers
network: true
overview: 'Numbers API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Date API, Math API, and 2 more. Tagged areas include Science And Math, Public APIs, Trivia, Numbers, and Dates.


  The Numbers API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Numbers API''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 71
rules:
- name: Numbers API API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: numbers-jsonschema-spectral-rules
- name: Numbers API API Rules
  rule_count: 37
  severity_counts:
    error: 16
    hint: 0
    info: 5
    warn: 16
  slug: numbers-rules
score:
  band: thin
  composite: 36.0
  delta: -3.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 69.7
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 0.0
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numbers/refs/heads/main/screenshots/numbers-2026-06-20T190517.png
security:
- kind: domain-security
  name: Numbers Domain Security
  slug: numbers-domain-security
  summary_line: TLSv1.3 · HSTS
slug: numbers
tags:
- Science And Math
- Public APIs
- Trivia
- Numbers
- Dates
- Open Source
use_cases:
- description: Insert living facts into marketing copy or dashboards, e.g. `We now have more users than the number of times Julius Caesar was stabbed`.
  name: Engagement Copy
- description: Pair `month/day/date` with a date picker or daily widget to surface a historical fact for the current day.
  name: Calendar Widgets
- description: Use `/{year}/year` to enrich anniversary, retrospective, and year-in-review content with curated facts.
  name: Anniversary and Year-in-Review
- description: Power "fact of the day" features for chatbots, newsletters, screen savers, and home assistants using `/random/trivia`.
  name: Daily Random Trivia
- description: Surface mathematical properties of numbers in educational tools and worksheets via `/{n}/math`.
  name: Math Education
- description: Provide free, unauthenticated, low-latency text responses ideal for tutorials, demos, and beginner HTTP client exercises.
  name: Mock and Demo Data
website: http://numbersapi.com/
---

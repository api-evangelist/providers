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
    dry_run_mode: true
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jokeapi Agentic Access
  operation_count: 10
  slug: jokeapi-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 3
apis:
- description: Operations for retrieving and submitting jokes.
  name: JokeAPI Jokes API
  slug: jokeapi-jokes-api
- description: Operations describing the API surface — categories, flags, formats, languages.
  name: JokeAPI Metadata API
  slug: jokeapi-metadata-api
- description: Health and discovery endpoints.
  name: JokeAPI System API
  slug: jokeapi-system-api
artifact_total: 53
collections:
- collection_type: open
  name: JokeAPI
  slug: open-jokeapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jokeapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jokeapi-domain-security.yml
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
  type: GitHub
  url: https://github.com/Sv443-Network/JokeAPI
- group: build
  title: ''
  type: SourceCode
  url: https://git.sv443.net/sv443/JokeAPI-v2
- group: commercial
  title: ''
  type: License
  url: https://github.com/Sv443-Network/JokeAPI/blob/main/LICENSE.txt
- group: operate
  title: ''
  type: Discord
  url: https://dc.sv443.net/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sv443.net/
- group: other
  title: ''
  type: Sponsor
  url: https://github.com/sponsors/Sv443
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/jokeapi/refs/heads/main/openapi/jokeapi-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/jokeapi/refs/heads/main/json-schema/jokeapi-single-joke-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/jokeapi/refs/heads/main/json-ld/jokeapi-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/jokeapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jokeapi-rate-limits.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/jokeapi-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/jokeapi-vocabulary.yml
created: '2026-05-28'
description: JokeAPI is a free, open source REST API that delivers consistently formatted jokes in JSON, XML, YAML, or plain text. It exposes seven joke categories (Any, Misc, Programming, Dark, Pun, Spooky, Christmas), six blacklist content flags (nsfw, religious, political, racist, sexist, explicit), and filters for language, joke type, ID range, contains-text search, amount, and safe-mode. No sign-up is required and CORS is enabled. The service is rate-limited at 120 requests per minute per IP (5 per minute on submissions) and is maintained by Sv443 under the MIT license. The canonical source lives on Sv443's own Git server, with this GitHub repo kept open for issues and the community wrapper-library index.
examples:
- key_count: 4
  name: Jokeapi Categories Response Example
  slug: jokeapi-categories-response-example
- key_count: 3
  name: Jokeapi Endpoints Response Example
  slug: jokeapi-endpoints-response-example
- key_count: 3
  name: Jokeapi Flags Response Example
  slug: jokeapi-flags-response-example
- key_count: 3
  name: Jokeapi Formats Response Example
  slug: jokeapi-formats-response-example
- key_count: 8
  name: Jokeapi Info Response Example
  slug: jokeapi-info-response-example
- key_count: 3
  name: Jokeapi Joke Batch Example
  slug: jokeapi-joke-batch-example
- key_count: 6
  name: Jokeapi Joke Flags Example
  slug: jokeapi-joke-flags-example
- key_count: 8
  name: Jokeapi Joke Submission Example
  slug: jokeapi-joke-submission-example
- key_count: 3
  name: Jokeapi Langcode Response Example
  slug: jokeapi-langcode-response-example
- key_count: 6
  name: Jokeapi Languages Response Example
  slug: jokeapi-languages-response-example
- key_count: 3
  name: Jokeapi Ping Response Example
  slug: jokeapi-ping-response-example
- key_count: 8
  name: Jokeapi Single Joke Example
  slug: jokeapi-single-joke-example
- key_count: 4
  name: Jokeapi Submission Response Example
  slug: jokeapi-submission-response-example
- key_count: 9
  name: Jokeapi Twopart Joke Example
  slug: jokeapi-twopart-joke-example
image: https://sv443.net/cdn/jokeapi/icon_readme.png
json_schemas:
- name: CategoriesResponse
  property_count: 4
  slug: jokeapi-categories-response
- name: EndpointsResponse
  property_count: 3
  slug: jokeapi-endpoints-response
- name: FlagsResponse
  property_count: 3
  slug: jokeapi-flags-response
- name: FormatsResponse
  property_count: 3
  slug: jokeapi-formats-response
- name: InfoResponse
  property_count: 8
  slug: jokeapi-info-response
- name: JokeBatch
  property_count: 3
  slug: jokeapi-joke-batch
- name: JokeFlags
  property_count: 6
  slug: jokeapi-joke-flags
- name: JokeSubmission
  property_count: 8
  slug: jokeapi-joke-submission
- name: LangcodeResponse
  property_count: 3
  slug: jokeapi-langcode-response
- name: LanguagesResponse
  property_count: 6
  slug: jokeapi-languages-response
- name: PingResponse
  property_count: 3
  slug: jokeapi-ping-response
- name: SingleJoke
  property_count: 8
  slug: jokeapi-single-joke
- name: SubmissionResponse
  property_count: 4
  slug: jokeapi-submission-response
- name: TwopartJoke
  property_count: 9
  slug: jokeapi-twopart-joke
json_structures:
- name: Jokeapi Categories Response Structure
  property_count: 4
  slug: jokeapi-categories-response-structure
- name: Jokeapi Endpoints Response Structure
  property_count: 3
  slug: jokeapi-endpoints-response-structure
- name: Jokeapi Flags Response Structure
  property_count: 3
  slug: jokeapi-flags-response-structure
- name: Jokeapi Formats Response Structure
  property_count: 3
  slug: jokeapi-formats-response-structure
- name: Jokeapi Info Response Structure
  property_count: 8
  slug: jokeapi-info-response-structure
- name: Jokeapi Joke Batch Structure
  property_count: 3
  slug: jokeapi-joke-batch-structure
- name: Jokeapi Joke Flags Structure
  property_count: 6
  slug: jokeapi-joke-flags-structure
- name: Jokeapi Joke Submission Structure
  property_count: 8
  slug: jokeapi-joke-submission-structure
- name: Jokeapi Langcode Response Structure
  property_count: 3
  slug: jokeapi-langcode-response-structure
- name: Jokeapi Languages Response Structure
  property_count: 6
  slug: jokeapi-languages-response-structure
- name: Jokeapi Ping Response Structure
  property_count: 3
  slug: jokeapi-ping-response-structure
- name: Jokeapi Single Joke Structure
  property_count: 8
  slug: jokeapi-single-joke-structure
- name: Jokeapi Submission Response Structure
  property_count: 4
  slug: jokeapi-submission-response-structure
- name: Jokeapi Twopart Joke Structure
  property_count: 9
  slug: jokeapi-twopart-joke-structure
jsonld:
- class_count: 14
  name: Jokeapi Context
  property_count: 47
  slug: jokeapi-context
layout: provider
modified: '2026-05-29'
name: JokeAPI
nav: Providers
network: true
overview: 'JokeAPI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Jokes API, Metadata API, and System API. Tagged areas include Jokes, Humor, Entertainment, Open Source, and REST API.


  The JokeAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  JokeAPI''s developer surface includes documentation, GitHub presence, and 16 more developer resources.'
plans:
- name: Jokeapi Plans Pricing
  plan_count: 2
  slug: jokeapi-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 2
  name: Jokeapi Rate Limits
  slug: jokeapi-rate-limits
rules:
- name: JokeAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jokeapi-jsonschema-spectral-rules
- name: JokeAPI API Rules
  rule_count: 46
  severity_counts:
    error: 15
    hint: 0
    info: 10
    warn: 21
  slug: jokeapi-spectral-rules
score:
  band: thin
  composite: 40.1
  delta: -7.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 52.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/jokeapi/refs/heads/main/screenshots/jokeapi-2026-06-20T183755.png
security:
- kind: domain-security
  name: Jokeapi Domain Security
  slug: jokeapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jokeapi
tags:
- Jokes
- Humor
- Entertainment
- Open Source
- REST API
- Games And Comics
- Public APIs
website: https://jokeapi.dev/
---

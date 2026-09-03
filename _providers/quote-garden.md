---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Quote Garden Agentic Access
  operation_count: 4
  slug: quote-garden-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://quote-garden.onrender.com/api/v3
  baseurl_source: declared
  description: Master list of authors represented in the quote corpus.
  name: Quote Garden Authors API
  slug: quote-garden-authors-api
- baseURL: https://quote-garden.onrender.com/api/v3
  baseurl_source: declared
  description: Master list of genres / categories represented in the quote corpus.
  name: Quote Garden Genres API
  slug: quote-garden-genres-api
- baseURL: https://quote-garden.onrender.com/api/v3
  baseurl_source: declared
  description: Operations for retrieving quote records, individually at random or as a paginated list.
  name: Quote Garden Quotes API
  slug: quote-garden-quotes-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quote Garden Authors API
  slug: open-quote-garden-authors-api
- collection_type: open
  name: Quote Garden Authors Genres API
  slug: open-quote-garden-genres-api
- collection_type: open
  name: Quote Garden Authors Quotes API
  slug: open-quote-garden-quotes-api
- collection_type: open
  name: Quote Garden API
  slug: open-quote-garden
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pprathameshmore/QuoteGarden/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quote-garden-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quote-garden-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pprathameshmore.github.io/QuoteGarden/
- group: start
  title: ''
  type: Portal
  url: https://pprathameshmore.github.io/QuoteGarden/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/pprathameshmore/QuoteGarden
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pprathameshmore
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pprathameshmore/QuoteGarden
- group: commercial
  title: MIT License
  type: License
  url: https://opensource.org/licenses/MIT
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/quote-garden/refs/heads/main/rules/quote-garden-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/quote-garden/refs/heads/main/vocabulary/quote-garden-vocabulary.yml
created: '2026-05-28'
description: Quote Garden is a free, open-source REST API that serves more than 75,000 famous quotes. Built by Prathamesh More (pprathameshmore) in Node.js + Express + MongoDB, it exposes a small read-only HTTP surface for fetching random quotes, paginated quote lists filterable by author, genre, and full-text query, plus master lists of all authors and genres. There is no authentication and no cost to use; the canonical reference implementation is hosted on Render at https://quote-garden.onrender.com/api/v3 and was previously deployed on Heroku at quote-garden.herokuapp.com. The project also ships an official npm client wrapper (`@pprathameshmore/quotegardennpm`) and is widely embedded in third-party chrome extensions, mobile apps, and Twitter bots that need a lightweight inspirational-quote source.
examples:
- key_count: 6
  name: Quote Garden Get Random Quote Example
  slug: quote-garden-get-random-quote-example
- key_count: 6
  name: Quote Garden List Authors Example
  slug: quote-garden-list-authors-example
- key_count: 6
  name: Quote Garden List Genres Example
  slug: quote-garden-list-genres-example
- key_count: 6
  name: Quote Garden List Quotes Example
  slug: quote-garden-list-quotes-example
- key_count: 5
  name: Quote Garden Quote Example
  slug: quote-garden-quote-example
- key_count: 5
  name: Quote Garden Response Envelope Example
  slug: quote-garden-response-envelope-example
features:
- description: Curated MongoDB collection of more than seventy-five thousand famous quotes attributed to a long tail of authors.
  name: 75,000+ Quotes
- description: Single-call endpoint that returns one or more randomly selected quotes, optionally filtered by author, genre, or search query.
  name: Random Quote Retrieval
- description: Page-and-limit paginated access to the full quote corpus with deterministic ordering, suitable for browsing or full-dump use cases.
  name: Paginated Quote Listing
- description: MongoDB text index on quoteText, quoteAuthor, and quoteGenre exposed via the `query` parameter on quote listing endpoints.
  name: Full-Text Search
- description: Filter quotes by exact author name via the `author` query parameter and discover the full author list via the `/authors` endpoint.
  name: Author Filter
- description: Filter quotes by genre (e.g., love, life, success, business) via the `genre` query parameter and discover the full genre list via the `/genres` endpoint.
  name: Genre Filter
- description: Completely open access with no API key, OAuth, or signup; CORS-enabled for direct browser use.
  name: No Authentication Required
- description: Every endpoint returns the same shape (statusCode, message, pagination, totalQuotes, data) for predictable client parsing.
  name: Consistent Response Envelope
- description: Official `quotegarden` npm package wraps the HTTP API for Node.js and browser projects.
  name: NPM Client Wrapper
- description: Entire backend (Express + MongoDB) and NPM client are MIT-licensed, allowing self-hosting and modification.
  name: Open Source MIT License
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quote-garden.png
integrations:
- description: New-tab Chrome extension by the same author that originally motivated the API; displays a daily quote with imagery.
  name: Achieve Chrome Extension
- description: Community-built Android app on Google Play that surfaces Quote Garden quotes on the device.
  name: QuoteGarden Android App
- description: Independent iOS app published on the App Store that consumes Quote Garden for randomized inspiration.
  name: Spontaneous (iOS)
- description: '@quotegardenbot Twitter bot that publishes scheduled quotes pulled from the API.'
  name: QuoteGarden Twitter Bot
- description: Third-party Chrome extension by AmitGujar that shows quotes on new-tab.
  name: Bink Chrome Extension
- description: GitHub open-source project by Shankhanil Ghosh that wraps Quote Garden into a motivational web experience.
  name: MotivateU
- description: Official `quotegarden` npm wrapper for JavaScript and TypeScript clients.
  name: QuoteGarden NPM
json_schemas:
- name: Quote
  property_count: 5
  slug: quote-garden-quote
- name: ResponseEnvelope
  property_count: 5
  slug: quote-garden-response-envelope
json_structures:
- name: Quote Garden Quote Structure
  property_count: 5
  slug: quote-garden-quote-structure
- name: Quote Garden Response Envelope Structure
  property_count: 5
  slug: quote-garden-response-envelope-structure
jsonld:
- class_count: 3
  name: Quote Garden Context
  property_count: 12
  slug: quote-garden-context
layout: provider
modified: '2026-05-30'
name: Quote Garden
nav: Providers
network: true
overview: 'Quote Garden publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authors API, Genres API, and Quotes API. Tagged areas include Quotes, Inspiration, Open-Source, Free API, and Node.js.


  The Quote Garden catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Quote Garden''s developer surface includes developer portal and 11 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 5
  extends: []
  name: Quote Garden API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quote-garden-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Quote Garden API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: quote-garden-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 35.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 66.7
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 2.6
  open_source:
    applies: true
    score: 0.0
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Quote Garden Domain Security
  slug: quote-garden-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: quote-garden
solutions:
- description: Clone the GitHub repo and run via Docker / docker-compose (Dockerfile and Procfile included) against your own MongoDB instance for full control of data and SLAs.
  name: Self-Hosted Deployment
- description: Free public reference deployment at quote-garden.onrender.com/api/v3 — no SLA, intended for hobby and prototype use.
  name: Hosted Reference API
- description: Drop-in `quotegarden` npm package for Node.js or browser apps that prefer a typed client over raw fetch calls.
  name: NPM SDK Integration
tags:
- Quotes
- Inspiration
- Open-Source
- Free API
- Node.js
- MongoDB
- Express
- Personality
- Public APIs
use_cases:
- description: Browser new-tab extensions and home screen widgets call `/quotes/random` to display a fresh inspirational quote on each page load.
  name: Inspirational Daily Quote Widgets
- description: Chatbots, Slack bots, and Alexa skills pull random quotes by genre to inject contextual inspiration into conversations.
  name: Chatbot and Voice Assistant Prompts
- description: Twitter, Mastodon, and Bluesky bots schedule recurring posts from filtered author or genre slices of the corpus.
  name: Social Media Automation
- description: Mobile apps for students, athletes, and remote workers surface goal-aligned quotes filtered by genre (success, perseverance, focus).
  name: Educational and Motivational Apps
- description: Jamstack sites embed a random quote at build time by hitting the API during the build step.
  name: Static Site Generators
- description: Indie games and AR experiences sprinkle randomly fetched quotes into loading screens and reward moments.
  name: Game and AR Easter Eggs
- description: Transactional and marketing email systems append a daily quote to footer templates fetched at send-time.
  name: Email and Newsletter Personalization
- description: Bootcamps and university courses use the unauthenticated API as a teaching example for HTTP, JSON parsing, and pagination.
  name: Learning Projects for API Consumption
website: https://pprathameshmore.github.io/QuoteGarden/
---

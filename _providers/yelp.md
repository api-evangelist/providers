---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Yelp Agentic Access
  operation_count: 11
  slug: yelp-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 5
apis:
- description: Conversational Yelp Fusion AI search and chat
  name: Yelp AI API
  slug: yelp-ai-api
- description: Search, match, and retrieve local business data
  name: Yelp Businesses API
  slug: yelp-businesses-api
- description: Yelp business category taxonomy
  name: Yelp Categories API
  slug: yelp-categories-api
- description: Local event search and details
  name: Yelp Events API
  slug: yelp-events-api
- description: Business review excerpts and ratings
  name: Yelp Reviews API
  slug: yelp-reviews-api
artifact_total: 85
collections:
- collection_type: postman
  name: Yelp Fusion AI API
  slug: postman-yelp-ai-api
- collection_type: postman
  name: Yelp Fusion AI Businesses API
  slug: postman-yelp-businesses-api
- collection_type: postman
  name: Yelp Fusion AI Categories API
  slug: postman-yelp-categories-api
- collection_type: postman
  name: Yelp Fusion AI Events API
  slug: postman-yelp-events-api
- collection_type: postman
  name: Yelp Fusion AI Reviews API
  slug: postman-yelp-reviews-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yelp Fusion AI API
  slug: open-yelp-ai-api
- collection_type: open
  name: Yelp Fusion AI Businesses API
  slug: open-yelp-businesses-api
- collection_type: open
  name: Yelp Fusion AI Categories API
  slug: open-yelp-categories-api
- collection_type: open
  name: Yelp Fusion AI Events API
  slug: open-yelp-events-api
- collection_type: open
  name: Yelp Fusion API
  slug: open-yelp
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/Yelp/yelp-fusion/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/yelp/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yelp-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yelp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yelp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yelp-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.yelp.com/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.yelp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developer.yelp.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developer.yelp.com/reference/v3_business_search
- group: auth
  title: ''
  type: Authentication
  url: https://docs.developer.yelp.com/docs/oauth-authorization
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.yelp.com/developers
- group: start
  title: ''
  type: Signup
  url: https://www.yelp.com/developers/v3/manage_app
- group: start
  title: ''
  type: Console
  url: https://www.yelp.com/developers/fusion-ai/chat
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.developer.yelp.com/docs/plans
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.developer.yelp.com/docs/places-rate-limiting
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.developer.yelp.com/docs/api-errors
- group: operate
  title: ''
  type: FAQ
  url: https://docs.developer.yelp.com/docs/places-faq
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.developer.yelp.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.developer.yelp.com/docs/policies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Yelp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Yelp/yelp-fusion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yelp-com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.developer.yelp.com/llms.txt
- group: build
  title: Yelp Fusion Code Samples
  type: SDKs
  url: https://github.com/Yelp/yelp-fusion
- group: build
  title: Python (yelp-python)
  type: SDKs
  url: https://github.com/Yelp/yelp-python
- group: build
  title: Ruby (yelp-ruby)
  type: SDKs
  url: https://github.com/Yelp/yelp-ruby
- group: build
  title: Android (yelp-android)
  type: SDKs
  url: https://github.com/Yelp/yelp-android
- group: build
  title: iOS (yelp-ios)
  type: SDKs
  url: https://github.com/Yelp/yelp-ios
- group: build
  title: MCP Server (Fusion AI)
  type: Tools
  url: https://github.com/Yelp/yelp-mcp
- group: design
  title: ''
  type: SpectralRules
  url: rules/yelp-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/yelp-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/yelp-fusion-api-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/yelp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yelp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yelp-finops.yml
created: '2025-02-08'
description: Yelp connects people with great local businesses. The Yelp Fusion API gives developers programmatic access to Yelp's database of millions of local businesses, ratings, reviews, photos, events, and category taxonomy, plus the Yelp Fusion AI conversational search endpoint. Core public capabilities include business search and discovery, business details, review excerpts, autocomplete, phone and address matching, and local event search. Partner-tier APIs add reviews response, leads, advertising, reservations, waitlist, checkout, and reporting. Authentication uses a Yelp API key passed as a bearer token.
examples:
- key_count: 4
  name: Yelp Ai Chat Request Example
  slug: yelp-ai-chat-request-example
- key_count: 5
  name: Yelp Ai Chat Response Example
  slug: yelp-ai-chat-response-example
- key_count: 3
  name: Yelp Autocomplete Response Example
  slug: yelp-autocomplete-response-example
- key_count: 23
  name: Yelp Business Detail Example
  slug: yelp-business-detail-example
- key_count: 17
  name: Yelp Business Example
  slug: yelp-business-example
- key_count: 3
  name: Yelp Business Hours Example
  slug: yelp-business-hours-example
- key_count: 3
  name: Yelp Business Search Response Example
  slug: yelp-business-search-response-example
- key_count: 5
  name: Yelp Category Example
  slug: yelp-category-example
- key_count: 2
  name: Yelp Coordinates Example
  slug: yelp-coordinates-example
- key_count: 20
  name: Yelp Event Example
  slug: yelp-event-example
- key_count: 2
  name: Yelp Event Search Response Example
  slug: yelp-event-search-response-example
- key_count: 9
  name: Yelp Location Example
  slug: yelp-location-example
- key_count: 6
  name: Yelp Review Example
  slug: yelp-review-example
- key_count: 3
  name: Yelp Reviews Response Example
  slug: yelp-reviews-response-example
features:
- description: Search up to 240 businesses by location, term, category, price, and attributes.
  name: Business Search
- description: Retrieve rich detail for a business by id or alias, including hours, photos, and attributes.
  name: Business Details
- description: Retrieve review excerpts, ratings, and reviewer details for a business.
  name: Reviews
- description: Return search-term, business, and category suggestions as the user types.
  name: Autocomplete
- description: Resolve a phone number or postal address to Yelp businesses.
  name: Phone and Address Match
- description: Search and retrieve local events with timing, location, cost, and ticketing.
  name: Events
- description: Access the full Yelp business category list and per-category details.
  name: Category Taxonomy
- description: Natural language, multi-turn conversational search and business questions.
  name: Fusion AI
finops:
- name: Yelp Finops
  service_category: API
  slug: yelp-finops
graphqls:
- description: Yelp exposes a GraphQL endpoint alongside its REST Fusion API, available at `https://api.yelp.com/v3/graphql`. The same bearer-token authentication used for the REST API applies here. The GraphQL surf
  name: Yelp GraphQL API
  slug: yelp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yelp.png
integrations:
- description: Yelp Leads and Conversions APIs offer Zapier integrations for no-code workflows.
  name: Zapier
- description: Official Yelp MCP server exposes Fusion AI as an agent tool over MCP.
  name: Model Context Protocol
- description: Reviews and Leads webhooks push real-time events to partner endpoints.
  name: Webhooks
json_schemas:
- name: AiChatRequest
  property_count: 4
  slug: yelp-ai-chat-request
- name: AiChatResponse
  property_count: 5
  slug: yelp-ai-chat-response
- name: AutocompleteResponse
  property_count: 3
  slug: yelp-autocomplete-response
- name: BusinessDetail
  property_count: 0
  slug: yelp-business-detail
- name: BusinessHours
  property_count: 3
  slug: yelp-business-hours
- name: Business
  property_count: 17
  slug: yelp-business
- name: BusinessSearchResponse
  property_count: 3
  slug: yelp-business-search-response
- name: Category
  property_count: 5
  slug: yelp-category
- name: Coordinates
  property_count: 2
  slug: yelp-coordinates
- name: Event
  property_count: 20
  slug: yelp-event
- name: EventSearchResponse
  property_count: 2
  slug: yelp-event-search-response
- name: Location
  property_count: 9
  slug: yelp-location
- name: Review
  property_count: 6
  slug: yelp-review
- name: ReviewsResponse
  property_count: 3
  slug: yelp-reviews-response
json_structures:
- name: Yelp Ai Chat Request Structure
  property_count: 4
  slug: yelp-ai-chat-request-structure
- name: Yelp Ai Chat Response Structure
  property_count: 5
  slug: yelp-ai-chat-response-structure
- name: Yelp Autocomplete Response Structure
  property_count: 3
  slug: yelp-autocomplete-response-structure
- name: Yelp Business Detail Structure
  property_count: 0
  slug: yelp-business-detail-structure
- name: Yelp Business Hours Structure
  property_count: 3
  slug: yelp-business-hours-structure
- name: Yelp Business Search Response Structure
  property_count: 3
  slug: yelp-business-search-response-structure
- name: Yelp Business Structure
  property_count: 17
  slug: yelp-business-structure
- name: Yelp Category Structure
  property_count: 5
  slug: yelp-category-structure
- name: Yelp Coordinates Structure
  property_count: 2
  slug: yelp-coordinates-structure
- name: Yelp Event Search Response Structure
  property_count: 2
  slug: yelp-event-search-response-structure
- name: Yelp Event Structure
  property_count: 20
  slug: yelp-event-structure
- name: Yelp Location Structure
  property_count: 9
  slug: yelp-location-structure
- name: Yelp Review Structure
  property_count: 6
  slug: yelp-review-structure
- name: Yelp Reviews Response Structure
  property_count: 3
  slug: yelp-reviews-response-structure
jsonld:
- class_count: 13
  name: Yelp Fusion Api Context
  property_count: 80
  slug: yelp-fusion-api-context
layout: provider
modified: '2026-06-03'
name: Yelp
nav: Providers
network: true
overview: 'Yelp publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AI API, Businesses API, Categories API, and 2 more. Tagged areas include Restaurant, Local Search, Reviews, Business Data, and Location.


  The Yelp catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Yelp''s developer surface includes authentication, engineering blog, documentation, getting-started guide, API reference, signup flow, developer console, and 29 more developer resources.'
plans:
- name: Yelp Plans Pricing
  plan_count: 5
  slug: yelp-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Yelp Rate Limits
  slug: yelp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Yelp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: yelp-jsonschema-spectral-rules
- effective_rule_count: 80
  extends:
  - spectral:oas
  name: Yelp API Rules
  rule_count: 39
  severity_counts:
    error: 6
    hint: 0
    info: 9
    warn: 24
  slug: yelp-spectral-rules
score:
  band: strong
  composite: 55.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 79.4
    developer_ergonomics: 66.7
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yelp/refs/heads/main/screenshots/yelp-2026-06-20T201740.png
security:
- kind: authentication
  name: Yelp Authentication
  slug: yelp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yelp Domain Security
  slug: yelp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yelp Vulnerability Disclosure
  slug: yelp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: yelp
tags:
- Restaurant
- Local Search
- Reviews
- Business Data
- Location
use_cases:
- description: Power restaurant and food discovery experiences with search, ratings, and photos.
  name: Restaurant Discovery
- description: Surface nearby, open, and highly-rated businesses based on user coordinates.
  name: Location-Aware Recommendations
- description: Track ratings and review excerpts for a portfolio of businesses.
  name: Reputation Monitoring
- description: Build AI agents that answer natural language questions about local businesses.
  name: Conversational Concierge
- description: Embed curated local event listings into apps and sites.
  name: Local Events Listings
website: https://www.yelp.com/developers
---

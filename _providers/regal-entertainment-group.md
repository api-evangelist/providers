---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Regal Entertainment Group Agentic Access
  operation_count: 9
  slug: regal-entertainment-group-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 5
apis:
- description: Regal Crown Club loyalty rewards
  name: regal-entertainment-group Loyalty API
  slug: regal-entertainment-group-loyalty-api
- description: Movie catalog and metadata
  name: regal-entertainment-group Movies API
  slug: regal-entertainment-group-movies-api
- description: Showtime schedules and availability
  name: regal-entertainment-group Showtimes API
  slug: regal-entertainment-group-showtimes-api
- description: Theatre locations and details
  name: regal-entertainment-group Theatres API
  slug: regal-entertainment-group-theatres-api
- description: Ticket purchasing and reservations
  name: regal-entertainment-group Tickets API
  slug: regal-entertainment-group-tickets-api
artifact_total: 21
collections:
- collection_type: open
  name: Regal Cinema API
  slug: open-regal-cinema
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/regal-entertainment-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regal-entertainment-group-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/regal-entertainment-group-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.regmovies.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.regmovies.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regal-entertainment-group
- group: company
  title: ''
  type: Twitter
  url: https://x.com/regalmovies
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/regal-entertainment-group/refs/heads/main/openapi/regal-cinema-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/regal-entertainment-group/refs/heads/main/vocabulary/regal-entertainment-group-vocabulary.yml
description: Regal Entertainment Group operates one of the largest motion picture theatre circuits in the United States, with theatres located in densely populated metropolitan markets. Regal provides a developer API portal at developer.regmovies.com, built on Azure API Management, enabling partners and developers to integrate movie showtimes, theatre listings, ticketing, and loyalty reward capabilities into applications. Regal was acquired by Cineworld Group in 2018 and continues to operate under the Regal brand.
examples:
- key_count: 2
  name: Regal Cinema List Movies Example
  slug: regal-cinema-list-movies-example
- key_count: 2
  name: Regal Cinema List Showtimes Example
  slug: regal-cinema-list-showtimes-example
finops:
- name: Regal Entertainment Group Finops
  service_category: Entertainment
  slug: regal-entertainment-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regal-entertainment-group.png
json_schemas:
- name: Movie
  property_count: 12
  slug: regal-movie
- name: Showtime
  property_count: 8
  slug: regal-showtime
json_structures:
- name: Regal Movie Structure
  property_count: 0
  slug: regal-movie-structure
- name: Regal Showtime Structure
  property_count: 0
  slug: regal-showtime-structure
jsonld:
- class_count: 35
  name: Regal Entertainment Group Context
  property_count: 0
  slug: regal-entertainment-group-context
layout: provider
modified: '2026-05-19'
name: regal-entertainment-group
nav: Providers
network: true
overview: 'regal-entertainment-group publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Loyalty API, Movies API, Showtimes API, and 2 more. Tagged areas include Cinema, Entertainment, Movies, Ticketing, and Loyalty.


  The regal-entertainment-group catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  regal-entertainment-group''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Regal Entertainment Group Plans Pricing
  plan_count: 1
  slug: regal-entertainment-group-plans-pricing
press:
- date: '2026-05-25'
  title: Regal Entertainment Group Ratings Placed On Credi
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/1366316
- date: '2026-05-25'
  title: Entertainment Goes Mobile with Regal App - RMN Digital
  url: https://www.rmndigital.com/entertainment-goes-mobile-with-regal-app/
- date: '2026-05-25'
  title: COMPANY NEWS; REGAL, A MOVIE THEATER CHAIN, PLANS ...
  url: https://www.nytimes.com/2002/04/23/business/company-news-regal-a-movie-theater-chain-plans-a-public-offering.html
- date: '2026-05-25'
  title: Regal Cinemas Partners with Diet Coke to Offer ...
  url: https://www.prnewswire.com/news-releases/regal-cinemas-partners-with-diet-coke-to-offer-moviegoers-a-chance-to-meet-global-superstar-taylor-swift-during-her-upcoming-tour-279342882.html
- date: '2026-05-25'
  title: News
  url: https://www.motionpictures.org/news/
random_paper: 65
rate_limits:
- limit_count: 1
  name: Regal Entertainment Group Rate Limits
  slug: regal-entertainment-group-rate-limits
rules:
- name: regal-entertainment-group API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: regal-cinema-rules
- name: regal-entertainment-group API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: regal-entertainment-group-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.8
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.9
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 31.3
    operational_transparency: 21.1
  previous_composite: 42.8
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
security:
- kind: authentication
  name: Regal Entertainment Group Authentication
  slug: regal-entertainment-group-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Regal Entertainment Group Domain Security
  slug: regal-entertainment-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: regal-entertainment-group
tags:
- Cinema
- Entertainment
- Movies
- Ticketing
- Loyalty
- Theatre
- Fortune 500
website: https://www.regmovies.com
---

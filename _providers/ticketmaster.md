---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ticketmaster Agentic Access
  operation_count: 2
  slug: ticketmaster-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: The Ticketmaster Partner API is a restricted API for authorized distribution partners that enables reserving, purchasing, and retrieving ticket and event information programmatically. Authentication u
  name: Ticketmaster Partner API
  slug: ticketmaster-partner-api
- description: Check ticket availability for events
  name: Ticketmaster Availability API
  slug: ticketmaster-availability-api
- description: Retrieve ticket offerings and pricing
  name: Ticketmaster Offerings API
  slug: ticketmaster-offerings-api
- description: Search artists, sports teams, and other attractions
  name: Ticketmaster Attractions API
  slug: ticketmaster-attractions-api
- description: Browse event segments, genres, and sub-genres
  name: Ticketmaster Classifications API
  slug: ticketmaster-classifications-api
- description: Search and retrieve live event information
  name: Ticketmaster Events API
  slug: ticketmaster-events-api
- description: Search suggestions and autocomplete
  name: Ticketmaster Suggestions API
  slug: ticketmaster-suggestions-api
- description: Search and retrieve venue information
  name: Ticketmaster Venues API
  slug: ticketmaster-venues-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ticketmaster Discovery Attractions API
  slug: open-ticketmaster-attractions-api
- collection_type: open
  name: Ticketmaster Commerce Availability API
  slug: open-ticketmaster-availability-api
- collection_type: open
  name: Ticketmaster Discovery Classifications API
  slug: open-ticketmaster-classifications-api
- collection_type: open
  name: Ticketmaster Commerce API
  slug: open-ticketmaster-commerce
- collection_type: open
  name: Ticketmaster Discovery Events API
  slug: open-ticketmaster-events-api
- collection_type: open
  name: Ticketmaster Commerce Availability Offerings API
  slug: open-ticketmaster-offerings-api
- collection_type: open
  name: Ticketmaster Discovery Suggestions API
  slug: open-ticketmaster-suggestions-api
- collection_type: open
  name: Ticketmaster Discovery Venues API
  slug: open-ticketmaster-venues-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ticketmaster-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ticketmaster-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ticketmaster-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ticketmaster
- group: start
  title: ''
  type: Portal
  url: https://developer.ticketmaster.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ticketmaster.com/products-and-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
- group: other
  title: ''
  type: API Explorer
  url: https://developer.ticketmaster.com/api-explorer/v2/
- group: company
  title: ''
  type: Website
  url: https://www.ticketmaster.com
- group: company
  title: ''
  type: Blog
  url: https://developer.ticketmaster.com/blog/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ticketmaster
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ticketmaster
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.ticketmaster.com/support/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ticketmaster.com/h/privacy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ticketmaster-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ticketmaster-event-schema.json
created: '2025-01-08'
description: Ticketmaster is the world's largest live entertainment ticketing company, providing access to tickets for concerts, sports, theater, and other live events globally. Their developer platform offers APIs for event discovery, ticket commerce, venue data, and partner integrations, giving developers access to over 230,000 events across dozens of countries.
examples:
- key_count: 2
  name: Ticketmaster Get Event Offers Example
  slug: ticketmaster-get-event-offers-example
- key_count: 2
  name: Ticketmaster Search Events Example
  slug: ticketmaster-search-events-example
- key_count: 2
  name: Ticketmaster Search Venues Example
  slug: ticketmaster-search-venues-example
finops:
- name: Ticketmaster Finops
  service_category: Events & Ticketing Data
  slug: ticketmaster-finops
image: https://www.ticketmaster.com/favicon.ico
json_schemas:
- name: Ticketmaster Event
  property_count: 9
  slug: ticketmaster-event
- name: Ticketmaster Venue
  property_count: 12
  slug: ticketmaster-venue
json_structures:
- name: Ticketmaster Event Structure
  property_count: 0
  slug: ticketmaster-event-structure
jsonld:
- class_count: 31
  name: Ticketmaster Context
  property_count: 7
  slug: ticketmaster-context
layout: provider
modified: '2026-05-19'
name: Ticketmaster
nav: Providers
network: true
overview: 'Ticketmaster publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Offerings API, Attractions API, and 4 more. Tagged areas include Commerce, Concerts, Entertainment, Event, and Sports.


  The Ticketmaster catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ticketmaster''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Ticketmaster Plans Pricing
  plan_count: 2
  slug: ticketmaster-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Ticketmaster Rate Limits
  slug: ticketmaster-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Ticketmaster API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: ticketmaster-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Ticketmaster API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 4
  slug: ticketmaster-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 57.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 58.8
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ticketmaster/refs/heads/main/screenshots/ticketmaster-2026-06-20T195332.png
security:
- kind: authentication
  name: Ticketmaster Authentication
  slug: ticketmaster-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ticketmaster Domain Security
  slug: ticketmaster-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ticketmaster
tags:
- Commerce
- Concerts
- Entertainment
- Event
- Sports
- Tickets
- Venues
website: https://www.ticketmaster.com
---

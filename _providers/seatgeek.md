---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Seatgeek Agentic Access
  operation_count: 9
  slug: seatgeek-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.seatgeek.com/2
  baseurl_source: declared
  description: The Events API from SeatGeek — 2 operation(s) for events.
  name: SeatGeek Events API
  slug: seatgeek-events-api
- baseURL: https://api.seatgeek.com/2
  baseurl_source: declared
  description: The Performers API from SeatGeek — 2 operation(s) for performers.
  name: SeatGeek Performers API
  slug: seatgeek-performers-api
- baseURL: https://api.seatgeek.com/2
  baseurl_source: declared
  description: The Recommendations API from SeatGeek — 2 operation(s) for recommendations.
  name: SeatGeek Recommendations API
  slug: seatgeek-recommendations-api
- baseURL: https://api.seatgeek.com/2
  baseurl_source: declared
  description: The Taxonomies API from SeatGeek — 1 operation(s) for taxonomies.
  name: SeatGeek Taxonomies API
  slug: seatgeek-taxonomies-api
- baseURL: https://api.seatgeek.com/2
  baseurl_source: declared
  description: The Venues API from SeatGeek — 2 operation(s) for venues.
  name: SeatGeek Venues API
  slug: seatgeek-venues-api
artifact_total: 30
collections:
- collection_type: postman
  name: SeatGeek Platform Events API
  slug: postman-seatgeek-events-api
- collection_type: postman
  name: SeatGeek Platform Events Performers API
  slug: postman-seatgeek-performers-api
- collection_type: postman
  name: SeatGeek Platform Events Recommendations API
  slug: postman-seatgeek-recommendations-api
- collection_type: postman
  name: SeatGeek Platform Events Taxonomies API
  slug: postman-seatgeek-taxonomies-api
- collection_type: postman
  name: SeatGeek Platform Events Venues API
  slug: postman-seatgeek-venues-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SeatGeek Platform Events API
  slug: open-seatgeek-events-api
- collection_type: open
  name: SeatGeek Platform Events Performers API
  slug: open-seatgeek-performers-api
- collection_type: open
  name: SeatGeek Platform API
  slug: open-seatgeek-platform
- collection_type: open
  name: SeatGeek Platform Events Recommendations API
  slug: open-seatgeek-recommendations-api
- collection_type: open
  name: SeatGeek Platform Events Taxonomies API
  slug: open-seatgeek-taxonomies-api
- collection_type: open
  name: SeatGeek Platform Events Venues API
  slug: open-seatgeek-venues-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/seatgeek/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/seatgeek-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seatgeek-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seatgeek-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seatgeek
- group: company
  title: ''
  type: Website
  url: https://seatgeek.com
- group: start
  title: ''
  type: Portal
  url: https://seatgeek.com/build
- group: docs
  title: ''
  type: Documentation
  url: https://seatgeek.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seatgeek
- group: build
  title: ''
  type: SDKs
  url: https://github.com/seatgeek/SGAPI
- group: operate
  title: ''
  type: Support
  url: https://github.com/seatgeek/api-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seatgeek.com/api-terms
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/seatgeek-event-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/seatgeek-event-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/seatgeek-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/seatgeek-list-events-example.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/seatgeek-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/seatgeek-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/seatgeek/mcp-pdb
created: '2026-05-02'
description: SeatGeek is a live event ticketing and discovery platform that aggregates ticket inventory from multiple sources and provides a transparent, data-driven ticket buying experience. The SeatGeek Platform API gives developers access to a canonical dataset of live events including concerts, sports, and theater performances, along with performer and venue information, seating maps, ticket pricing, and personalized event recommendations. The API uses HTTP Basic Auth or query parameter authentication with a client ID and supports RESTful access to events, performers, venues, and taxonomies.
examples:
- key_count: 2
  name: Seatgeek List Events Example
  slug: seatgeek-list-events-example
finops:
- name: Seatgeek Finops
  service_category: API
  slug: seatgeek-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seatgeek.png
json_schemas:
- name: SeatGeek Event
  property_count: 14
  slug: seatgeek-event
json_structures:
- name: Seatgeek Event Structure
  property_count: 13
  slug: seatgeek-event-structure
jsonld:
- class_count: 27
  name: Seatgeek Context
  property_count: 4
  slug: seatgeek-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: SeatGeek
nav: Providers
network: true
overview: 'SeatGeek publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Events API, Performers API, Recommendations API, and 2 more. Tagged areas include Event, Tickets, Live Events, Concerts, and Sports.


  The SeatGeek catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SeatGeek''s developer surface includes authentication, developer portal, documentation, support, code examples, and 14 more developer resources.'
plans:
- name: Seatgeek Plans Pricing
  plan_count: 3
  slug: seatgeek-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Seatgeek Rate Limits
  slug: seatgeek-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SeatGeek API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: seatgeek-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: SeatGeek API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: seatgeek-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 61.9
    developer_ergonomics: 44.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seatgeek/refs/heads/main/screenshots/seatgeek-2026-06-20T193620.png
security:
- kind: authentication
  name: Seatgeek Authentication
  slug: seatgeek-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seatgeek Domain Security
  slug: seatgeek-domain-security
  summary_line: TLSv1.3 · DMARC
slug: seatgeek
tags:
- Event
- Tickets
- Live Events
- Concerts
- Sports
- Venues
- Ticketing
website: https://seatgeek.com
---

---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 66.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Seatgeek Agentic Access
  operation_count: 9
  slug: seatgeek-agentic-access
  summary_line: 9 operations
api_count: 5
apis:
- description: The Events API from SeatGeek — 2 operation(s) for events.
  name: SeatGeek Events API
  slug: seatgeek-events-api
- description: The Performers API from SeatGeek — 2 operation(s) for performers.
  name: SeatGeek Performers API
  slug: seatgeek-performers-api
- description: The Recommendations API from SeatGeek — 2 operation(s) for recommendations.
  name: SeatGeek Recommendations API
  slug: seatgeek-recommendations-api
- description: The Taxonomies API from SeatGeek — 1 operation(s) for taxonomies.
  name: SeatGeek Taxonomies API
  slug: seatgeek-taxonomies-api
- description: The Venues API from SeatGeek — 2 operation(s) for venues.
  name: SeatGeek Venues API
  slug: seatgeek-venues-api
artifact_total: 19
collections:
- collection_type: open
  name: SeatGeek Platform API
  slug: open-seatgeek-platform
common:
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
overview: 'SeatGeek publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Events API, Performers API, Recommendations API, and 2 more. Tagged areas include Events, Tickets, Live Events, Concerts, and Sports.


  The SeatGeek catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SeatGeek''s developer surface includes authentication, developer portal, documentation, support, code examples, and 13 more developer resources.'
plans:
- name: Seatgeek Plans Pricing
  plan_count: 3
  slug: seatgeek-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Seatgeek Rate Limits
  slug: seatgeek-rate-limits
rules:
- name: SeatGeek API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: seatgeek-jsonschema-spectral-rules
- name: SeatGeek API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: seatgeek-rules
score:
  band: strong
  composite: 60.8
  delta: 3.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.1
    developer_ergonomics: 47.8
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 57.5
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Events
- Tickets
- Live Events
- Concerts
- Sports
- Venues
- Ticketing
website: https://seatgeek.com
---

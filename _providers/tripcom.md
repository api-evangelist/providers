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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Tripcom Agentic Access
  operation_count: 4
  slug: tripcom-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: The SearchAttractionAndActivity API from Trip.com — 1 operation(s) for searchattractionandactivity.
  name: Trip.com SearchAttractionAndActivity API
  slug: tripcom-searchattractionandactivity-api
- description: The SearchCars API from Trip.com — 1 operation(s) for searchcars.
  name: Trip.com SearchCars API
  slug: tripcom-searchcars-api
- description: The SearchFlightTicket API from Trip.com — 1 operation(s) for searchflightticket.
  name: Trip.com SearchFlightTicket API
  slug: tripcom-searchflightticket-api
- description: The SearchHotel API from Trip.com — 1 operation(s) for searchhotel.
  name: Trip.com SearchHotel API
  slug: tripcom-searchhotel-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripcom-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tripcom-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tripcom-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tripcom-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tripcom-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tripcom-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tripcom-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tripcom-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.trip.com
- group: company
  title: ''
  type: Blog
  url: https://www.trip.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.trip.com/ask/questions/trip.com-customer-service.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pages.trip.com/service-guideline/terms-en-xx.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pages.trip.com/service-guideline/privacy-policy-en-xx.html
created: '2026-07-17'
description: Trip.com is a leading global online travel agency and part of Trip.com Group, offering one-stop travel booking for flights, hotels, trains, car rentals, airport transfers, attraction tickets, tours, and vacation packages across 39 countries and regions in 24 languages. Trip.com publishes a public AI travel-assistant plugin API (an OpenAI-plugin-style OpenAPI at www.trip.com/ai-resource) that lets assistants search flights, hotels, car hire, and attractions/activities and return deep booking links, alongside a published llms.txt describing its site structure for AI agents.
image: https://ak-d.tripcdn.com/images/1o14712000bc9tm39E62A.jpg
layout: provider
mcp_servers:
- description: ''
  name: tripcom-mcp.yml
  slug: tripcom-mcpyml
modified: '2026-07-21'
name: Trip.com
nav: Providers
network: true
overview: 'Trip.com publishes 4 APIs on the [APIs.io](https://apis.io/) network, including SearchAttractionAndActivity API, SearchCars API, SearchFlightTicket API, and 1 more. Tagged areas include Company, Travel, Hotels, Flights, and Car Rental.


  Trip.com''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 28
score:
  band: thin
  composite: 31.4
  delta: -1.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 50.8
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Tripcom Domain Security
  slug: tripcom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tripcom
tags:
- Company
- Travel
- Hotels
- Flights
- Car Rental
- Attractions
- Trains
- Booking
- Itinerary
- AI Plugin
website: https://developer.trip.com
---

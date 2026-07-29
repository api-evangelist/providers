---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: American Airlines Agentic Access
  operation_count: 4
  slug: american-airlines-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- description: Booking management operations
  name: American Airlines Bookings API
  slug: american-airlines-bookings-api
- description: Flight information and status operations
  name: American Airlines Flights API
  slug: american-airlines-flights-api
artifact_total: 41
collections:
- collection_type: open
  name: American Airlines Runway Developer API
  slug: open-american-airlines-runway-developer-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/american-airlines-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-airlines-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-airlines
- group: company
  title: ''
  type: Website
  url: https://www.aa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aa.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmericanAirlines
- group: company
  title: ''
  type: Blog
  url: https://tech.aa.com/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AmericanAirlines/backstage
- group: build
  title: Flight Engine Mock API
  type: Tools
  url: https://github.com/AmericanAirlines/Flight-Engine
- group: build
  title: Hangar Hackathon Tool
  type: Tools
  url: https://github.com/AmericanAirlines/Hangar
created: '2026-04-19'
description: American Airlines is one of the world's largest airlines, operating an extensive domestic and international route network. The company's Runway developer experience platform, built on Spotify's Backstage, provides internal developer tooling and API management for engineering teams. American Airlines exposes flight data, status, and booking capabilities through its developer portal, and maintains an active open-source presence via the AmericanAirlines GitHub organization.
examples:
- key_count: 4
  name: Runway Developer Api Booking Example
  slug: runway-developer-api-booking-example
- key_count: 2
  name: Runway Developer Api Booking Request Example
  slug: runway-developer-api-booking-request-example
- key_count: 7
  name: Runway Developer Api Flight Example
  slug: runway-developer-api-flight-example
- key_count: 1
  name: Runway Developer Api Flight List Example
  slug: runway-developer-api-flight-list-example
- key_count: 4
  name: Runway Developer Api Flight Status Example
  slug: runway-developer-api-flight-status-example
features:
- description: Internal developer platform built on Spotify's Backstage providing centralized API management, service catalog, and self-service infrastructure tooling for engineering teams.
  name: Runway Developer Experience Platform
- description: APIs for querying flight schedules, routes, status information, and operational data across American Airlines' domestic and international network.
  name: Flight Data APIs
- description: APIs supporting flight search, booking, reservation management, and passenger services integration for travel applications.
  name: Booking and Reservation APIs
- description: Runway provides integrated API management with security, authentication toggles, and corporate authentication capabilities for development teams.
  name: Built-In API Management
- description: Kong-based service mesh enabling reliable microservices communication and traffic management across the American Airlines platform.
  name: Service Mesh Integration
- description: American Airlines maintains open-source tools including Flight Engine (mock flight data API), Hangar (hackathon management), and Backstage plugins via the AmericanAirlines GitHub organization.
  name: Open Source Tooling
finops:
- name: American Airlines Finops
  service_category: Airlines / Travel
  slug: american-airlines-finops
graphqls:
- description: This conceptual GraphQL schema models the American Airlines travel and flight API domain. It covers the full lifecycle of air travel including flight search, booking, reservations, passenger managemen
  name: American Airlines GraphQL Schema
  slug: american-airlines-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-airlines.png
integrations:
- description: Runway developer portal is built on Spotify's Backstage platform for internal developer experience and service catalog management.
  name: Spotify Backstage
- description: American Airlines uses Kong's Kuma service mesh for microservices networking and API gateway capabilities.
  name: Kong Service Mesh
- description: Integration with HashiCorp Vault for secrets management in build pipelines via open-source vault-action GitHub Action.
  name: HashiCorp Vault
- description: Python API client for Dynatrace integration maintained in the AmericanAirlines GitHub organization.
  name: Dynatrace
json_schemas:
- name: BookingRequest
  property_count: 2
  slug: runway-developer-api-booking-request
- name: Booking
  property_count: 4
  slug: runway-developer-api-booking
- name: FlightList
  property_count: 1
  slug: runway-developer-api-flight-list
- name: Flight
  property_count: 7
  slug: runway-developer-api-flight
- name: FlightStatus
  property_count: 4
  slug: runway-developer-api-flight-status
json_structures:
- name: Runway Developer Api Booking Request Structure
  property_count: 2
  slug: runway-developer-api-booking-request-structure
- name: Runway Developer Api Booking Structure
  property_count: 4
  slug: runway-developer-api-booking-structure
- name: Runway Developer Api Flight List Structure
  property_count: 1
  slug: runway-developer-api-flight-list-structure
- name: Runway Developer Api Flight Status Structure
  property_count: 4
  slug: runway-developer-api-flight-status-structure
- name: Runway Developer Api Flight Structure
  property_count: 7
  slug: runway-developer-api-flight-structure
jsonld:
- class_count: 5
  name: American Airlines Runway Context
  property_count: 12
  slug: american-airlines-runway-context
layout: provider
modified: '2026-05-19'
name: American Airlines
nav: Providers
network: true
overview: 'American Airlines publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bookings API and Flights API. Tagged areas include Airlines, Aviation, Flights, Travel, and Booking.


  The American Airlines catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  American Airlines'' developer surface includes engineering blog, tooling, and 8 more developer resources.'
plans:
- name: American Airlines Plans Pricing
  plan_count: 1
  slug: american-airlines-plans-pricing
press:
- date: '2026-05-25'
  title: American Airlines Reports Second-Quarter 2025 Financial ...
  url: https://americanairlines.gcs-web.com/news-releases/news-release-details/american-airlines-reports-second-quarter-2025-financial-results
- date: '2026-05-25'
  title: News - Corporate - American Airlines Newsroom
  url: https://news.aa.com/news/corporate/2025/default.aspx
- date: '2026-05-25'
  title: 100 years of American Airlines, and they're just getting ...
  url: https://www.instagram.com/p/DXLGgj2DTJg/
- date: '2026-05-25'
  title: How American Airlines Uses AI to Strengthen Human ...
  url: https://adchatdfw.com/how-american-airlines-uses-ai-to-strengthen-human-decision-making/
- date: '2026-05-25'
  title: American Airlines reports fourth-quarter and full-year 2025 ...
  url: https://news.aa.com/news/news-details/2026/American-Airlines-reports-fourth-quarter-and-full-year-2025-financial-results-CORP-FI-01/default.aspx
random_paper: 52
rate_limits:
- limit_count: 1
  name: American Airlines Rate Limits
  slug: american-airlines-rate-limits
rules:
- name: American Airlines API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: american-airlines-jsonschema-spectral-rules
- name: American Airlines API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: american-airlines-spectral-rules
score:
  band: thin
  composite: 41.3
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: American Airlines Domain Security
  slug: american-airlines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-airlines
tags:
- Airlines
- Aviation
- Flights
- Travel
- Booking
- Developer Experience
- Fortune 100
use_cases:
- description: Travel agencies and booking platforms integrate flight availability, pricing, and reservation APIs to offer American Airlines flights.
  name: Flight Search and Booking
- description: Applications query real-time flight status, departure, arrival, and delay information for American Airlines flights.
  name: Flight Status Tracking
- description: American Airlines engineering teams use Runway to self-service infrastructure, register APIs in the service catalog, and manage deployments.
  name: Internal Developer Tooling
- description: Open-source Hangar tool enables hackathon management for tech innovation events sponsored by or affiliated with American Airlines.
  name: Hackathon and Innovation
website: https://www.aa.com/
---

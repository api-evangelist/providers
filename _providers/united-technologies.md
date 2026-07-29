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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: United Technologies Agentic Access
  operation_count: 4
  slug: united-technologies-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: Flight information and tracking operations
  name: United Technologies Flights API
  slug: united-technologies-flights-api
- description: Aviation message transmission and retrieval operations
  name: United Technologies Messages API
  slug: united-technologies-messages-api
- description: Aviation weather data operations
  name: United Technologies Weather API
  slug: united-technologies-weather-api
artifact_total: 54
collections:
- collection_type: open
  name: Collins Aerospace ARINC Messaging API
  slug: open-united-technologies-arinc-messaging
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-technologies-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-technologies
- group: company
  title: ''
  type: Website
  url: https://www.rtx.com/collinsaerospace
- group: start
  title: ''
  type: Portal
  url: https://arinconline.collinsaerospace.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.rtx.com/collinsaerospace/what-we-do/industries/commercial-aviation/ground-operations/messaging-data-exchange
- group: design
  title: ''
  type: SpectralRules
  url: rules/united-technologies-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/united-technologies-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.rtx.com/rss-feeds/news
description: United Technologies Corporation (UTC) was an American multinational conglomerate that merged with Raytheon Company in 2020 to form Raytheon Technologies, later renamed RTX Corporation in 2023. Prior to the merger, UTC's major subsidiaries included Otis Elevator (now independent), Carrier Global (now independent), Pratt & Whitney, and Collins Aerospace. Today, Collins Aerospace (formerly UTC Aerospace Systems and Rockwell Collins) provides aviation connectivity and data exchange services through the ARINC Digital Exchange platform, including messaging, flight operations, and weather data APIs for commercial aviation.
examples:
- key_count: 2
  name: Arinc Messaging Cloud Layer Example
  slug: arinc-messaging-cloud-layer-example
- key_count: 13
  name: Arinc Messaging Flight Example
  slug: arinc-messaging-flight-example
- key_count: 2
  name: Arinc Messaging Flight List Example
  slug: arinc-messaging-flight-list-example
- key_count: 10
  name: Arinc Messaging Message Example
  slug: arinc-messaging-message-example
- key_count: 2
  name: Arinc Messaging Message List Example
  slug: arinc-messaging-message-list-example
- key_count: 6
  name: Arinc Messaging Send Message Request Example
  slug: arinc-messaging-send-message-request-example
- key_count: 3
  name: Arinc Messaging Send Message Response Example
  slug: arinc-messaging-send-message-response-example
- key_count: 8
  name: Arinc Messaging Weather Data Example
  slug: arinc-messaging-weather-data-example
features:
- description: Industry-standard aviation communications network connecting aircraft, airlines, airports, and ground operations worldwide.
  name: ARINC Global Network
- description: Aircraft Communications Addressing and Reporting System messaging for digital communications between aircraft and ground.
  name: ACARS Messaging
- description: Real-time Out, Off, On, In flight event tracking for operational efficiency and on-time performance monitoring.
  name: OOOI Flight Events
- description: METARs, TAFs, SIGMETs, PIREPs, and graphical weather services for flight operations and dispatch.
  name: Aviation Weather Data
- description: Flexible integration platform deployable on-premise, SaaS, or in customer cloud for managing aviation data exchange.
  name: ARINC Integrator Platform
- description: InteliSight, GlobalConnect, and FlightHub platforms for comprehensive connected aircraft and ground operations.
  name: Connected Aircraft Solutions
- description: AviNet Airport and GLOBALink network infrastructure for airport ground operations and avionics connectivity.
  name: Airport Network Connectivity
finops:
- name: United Technologies Finops
  service_category: API
  slug: united-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-technologies.png
integrations:
- description: Collins Aerospace joined the Digital Alliance for Aviation powered by Airbus Skywise for predictive maintenance and health monitoring.
  name: Airbus Skywise
- description: ARINC flight operations data integrates with SAP IS-A for airline operations and financial management.
  name: SAP Aviation
- description: OOOI and flight status data integrates with Amadeus Altea CM for airline departure control and passenger services.
  name: Amadeus
- description: Complementary aviation communications network for shared messaging and airport data exchange services.
  name: SITA
json_schemas:
- name: CloudLayer
  property_count: 2
  slug: arinc-messaging-cloud-layer
- name: FlightList
  property_count: 2
  slug: arinc-messaging-flight-list
- name: Flight
  property_count: 13
  slug: arinc-messaging-flight
- name: MessageList
  property_count: 2
  slug: arinc-messaging-message-list
- name: Message
  property_count: 10
  slug: arinc-messaging-message
- name: SendMessageRequest
  property_count: 6
  slug: arinc-messaging-send-message-request
- name: SendMessageResponse
  property_count: 3
  slug: arinc-messaging-send-message-response
- name: WeatherData
  property_count: 8
  slug: arinc-messaging-weather-data
json_structures:
- name: Arinc Messaging Cloud Layer Structure
  property_count: 2
  slug: arinc-messaging-cloud-layer-structure
- name: Arinc Messaging Flight List Structure
  property_count: 2
  slug: arinc-messaging-flight-list-structure
- name: Arinc Messaging Flight Structure
  property_count: 13
  slug: arinc-messaging-flight-structure
- name: Arinc Messaging Message List Structure
  property_count: 2
  slug: arinc-messaging-message-list-structure
- name: Arinc Messaging Message Structure
  property_count: 10
  slug: arinc-messaging-message-structure
- name: Arinc Messaging Send Message Request Structure
  property_count: 6
  slug: arinc-messaging-send-message-request-structure
- name: Arinc Messaging Send Message Response Structure
  property_count: 3
  slug: arinc-messaging-send-message-response-structure
- name: Arinc Messaging Weather Data Structure
  property_count: 8
  slug: arinc-messaging-weather-data-structure
jsonld:
- class_count: 8
  name: United Technologies Arinc Messaging Context
  property_count: 32
  slug: united-technologies-arinc-messaging-context
layout: provider
modified: '2026-05-19'
name: United Technologies
nav: Providers
network: true
overview: 'United Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: Flights API, Messages API, and Weather API. Tagged areas include Aerospace, Defense, Aviation, Manufacturing, and Connectivity.


  The United Technologies catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United Technologies'' developer surface includes authentication, developer portal, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: United Technologies Plans Pricing
  plan_count: 3
  slug: united-technologies-plans-pricing
press:
- date: '2026-05-25'
  title: Raytheon and United Technologies Aerospace Businesses ...
  url: https://www.prnewswire.com/news-releases/raytheon-and-united-technologies-aerospace-businesses-to-combine-in-merger-of-equals-300864268.html
- date: '2026-05-25'
  title: United Technologies Press Release
  url: https://www.pressreleasepoint.com/united-technologies-0
- date: '2026-05-25'
  title: 'Press Release: Raytheon and UTC businesses to combine'
  url: https://runwaygirlnetwork.com/2019/06/press-release-raytheon-and-utc-businesses-to-combine/
- date: '2026-05-25'
  title: United Technologies Aerospace Businesses and Raytheon ...
  url: https://investors.rtx.com/static-files/0e5ad90b-0e03-4d32-96a3-6504e5d6310b
- date: '2026-05-25'
  title: United Technologies - Oak Ridge Leadership Computing Facility
  url: https://www.olcf.ornl.gov/tag/united-technologies/
random_paper: 53
rate_limits:
- limit_count: 5
  name: United Technologies Rate Limits
  slug: united-technologies-rate-limits
rules:
- name: United Technologies API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-technologies-jsonschema-spectral-rules
- name: United Technologies API Rules
  rule_count: 31
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 13
  slug: united-technologies-spectral-rules
score:
  band: developing
  composite: 51.3
  delta: -7.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.3
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 59.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/united-technologies/refs/heads/main/screenshots/united-technologies-2026-06-20T200101.png
security:
- kind: authentication
  name: United Technologies Authentication
  slug: united-technologies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: United Technologies Domain Security
  slug: united-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: united-technologies
tags:
- Aerospace
- Defense
- Aviation
- Manufacturing
- Connectivity
- Fortune 100
use_cases:
- description: Monitor real-time flight status, OOOI events, and aircraft communications for dispatch and operations center workflows.
  name: Airline Operations Control
- description: Automate gate assignments, crew notifications, and turnaround communications using ACARS uplink messaging.
  name: Ground Operations Automation
- description: Access METARs, TAFs, and SIGMETs for pre-flight weather briefings and in-flight weather monitoring.
  name: Flight Dispatch
- description: Receive ACARS maintenance messages and fault codes from aircraft for predictive maintenance workflows.
  name: Maintenance MRO Integration
- description: Send gate change and operational update messages to aircraft for cabin crew announcements.
  name: Passenger Service Messaging
- description: Integrate OOOI flight data into airport management systems for terminal planning and resource allocation.
  name: Airport Operations Management
website: https://www.rtx.com/collinsaerospace
---

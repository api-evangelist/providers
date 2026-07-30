---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Flight Network Agentic Access
  operation_count: 0
  slug: flight-network-agentic-access
  summary_line: 0 operations
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.flightnetwork.com/
- group: company
  title: ''
  type: Website
  url: https://ca.flightnetwork.com/
- group: company
  title: ''
  type: About
  url: https://ca.flightnetwork.com/c/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ca.flightnetwork.com/rf/travel-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ca.flightnetwork.com/rf/privacy-policy
- group: other
  title: ''
  type: Robots
  url: https://ca.flightnetwork.com/robots.txt
- group: other
  title: ''
  type: Sitemap
  url: https://ca.flightnetwork.com/sitemap.xml
- group: operate
  title: ''
  type: FAQ
  url: https://ca.flightnetwork.com/c/faq
- group: docs
  title: ''
  type: Documentation
  url: https://ca.flightnetwork.com/rf/carriers
- group: operate
  title: ''
  type: Support
  url: https://www.flightnetwork.com/rf/contact-us
- group: start
  title: ''
  type: Login
  url: https://www.flightnetwork.com/rf/order-login
- group: other
  title: ''
  type: MobileApp
  url: https://www.flightnetwork.com/rf/mobile-app-download
- group: other
  title: ''
  type: Accessibility
  url: https://www.flightnetwork.com/c/accessibility
- group: other
  title: ''
  type: Sustainability
  url: https://www.flightnetwork.com/rf/sustainability
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlightNetwork
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flight-network
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flight-network-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flight-network-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/flight-network-security.txt
- group: auth
  title: ''
  type: Security
  url: https://ca.flightnetwork.com/.well-known/security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/flight-network-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flight-network-agentic-access.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://www.etraveligroup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.etraveligroup.com/our-platform/b2b/trip-stack/
- group: company
  title: ''
  type: Website
  url: https://www.tripstack.com/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-28'
description: 'Flight Network (Flight Network Ltd, 145 King St. West Suite 2850, Toronto, Ontario, TICO Registration 50009248) is a Canadian online travel agency founded in 2005 and owned by Sweden''s Etraveli Group since 2019. It retails flights plus hotels and car rentals to consumers across 75+ markets in 35 languages, sourcing air content through the GDSs - its own About Us page carries the Amadeus and Sabre marks and claims "IATA Certified Travel Agents" - and reaching buyers through its own sites, its iOS/Android apps, metasearch deep links from Skyscanner and Kayak, and third-party affiliate networks. It sits in the distribution chain as a retailer downstream of the GDSs and of its Etraveli sibling TripStack (the group''s B2B LCC/NDC/virtual-interlining API), not as a content owner. Its API posture is honest and thin: no developer portal, no published API documentation, no machine-readable specification, and no exit path. developer/developers/docs/api.flightnetwork.com are all NXDOMAIN,
  /openapi.json and /swagger.json return 404, and the only machine-readable surfaces reachable are the consumer booking site, a security.txt pointing at security@etraveligroup.com, the iOS/Android app-link declarations, and - the one genuine find - a substantial provider-published llms.txt at the site root that hands agents a regional domain map, a product and ancillary catalogue, a support-escalation hierarchy, and explicit DO/DON''T directives for AI systems. Flight Network is thus addressable by agents as a referral target while remaining entirely uncallable. Any B2B or travel-seller access is arranged by commercial agreement off-web.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-28'
name: Flight Network
nav: Providers
network: true
overview: 'Flight Network is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Canada, Aviation, Airline, and OTA.


  Flight Network''s developer surface includes FAQ, documentation, support, and 23 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 18.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 15.8
  provenance:
    agentic_access: first-party
    conformance: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: domain-security
  name: Flight Network Domain Security
  slug: flight-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flight Network Vulnerability Disclosure
  slug: flight-network-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flight-network
tags:
- Travel
- Canada
- Aviation
- Airline
- OTA
- Booking
- Distribution
- Flights
- Hotels
- Car Rental
- GDS
website: https://www.flightnetwork.com/
---

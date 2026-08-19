---
access_model:
  confidence: high
  label: Documented APIs · Enrolment and Azure AD account required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - developer-portal
  - terms
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Heathrow's Flights API provides up to date information on real time flights to and from Heathrow, covering destinations, arrivals, airlines, aircraft types, flight status, gates and terminals, with sc
  name: Heathrow Flights API
  slug: heathrow-flights-api
- description: Heathrow's Connections API provides up to date information on real time flight connections to and from Heathrow, returning connection information together with flight detail. The portal documents four
  name: Heathrow Flight Connections API
  slug: heathrow-connections-api
- description: 'Heathrow''s Weather API provides up to date information on weather conditions at most airports worldwide, exposing temperature, weather categories, a countries list and lookup of weather by IATA code, '
  name: Heathrow Weather API
  slug: heathrow-weather-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heathrow-airport-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heathrow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.heathrow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.heathrow.com/apis
- group: commercial
  title: ''
  type: Plans
  url: https://developer.heathrow.com/products
- group: start
  title: ''
  type: Onboarding
  url: https://developer.heathrow.com/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://developer.heathrow.com/signup
- group: auth
  title: ''
  type: Authentication
  url: https://developer.heathrow.com/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.heathrow.com/api-changelog
- group: operate
  title: ''
  type: Support
  url: mailto:support@heathrow.com
- group: other
  title: ''
  type: Company
  url: https://www.heathrow.com/company
- group: operate
  title: ''
  type: FlightStatus
  url: https://www.heathrow.com/arrivals
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heathrow.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heathrow.com/privacy-notice
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heathrow-airport/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.heathrow.com/how-it-works
- group: company
  title: ''
  type: Blog
  url: https://mediacentre.heathrow.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/heathrow-airport-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/heathrow-airport-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/heathrow-airport-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heathrow-airport-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/heathrow-airport-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/heathrow-airport-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/heathrow-airport-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heathrow-airport-llms.txt
created: '2026-07-28'
description: Heathrow Airport Limited operates London Heathrow (IATA LHR, ICAO EGLL), the United Kingdom's principal international hub and Europe's busiest airport by passenger numbers, under the ultimate ownership of FGP Topco Limited - whose largest shareholder since December 2024 is Ardian, alongside Saudi Arabia's Public Investment Fund and a residual Ferrovial holding. In the travel distribution chain Heathrow is infrastructure, not an intermediary - it sells no seats, holds no bookable inventory, issues no PNRs or e-tickets, and sits entirely outside the GDS and IATA NDC value chain, earning aeronautical charges, retail concessions, car parking and property income instead. Its API posture is unusual for an airport - Heathrow does run a real, branded, publicly reachable developer portal at developer.heathrow.com, built on Microsoft Azure API Management, which publicly describes three products in prose - Flights, Flight Connections and Weather - but publishes no OpenAPI, no endpoint
  reference, no rate limits, no pricing and no SLA to anonymous visitors. The API catalogue and Products list return empty to unauthenticated callers, sign-in is via Azure Active Directory, and the portal's own How It Works page requires a prospective developer to email support@heathrow.com and be enrolled before any access is granted. The gateway at api.heathrow.com goes further and rejects requests with "400 No required SSL certificate was sent", meaning mutual TLS with a Heathrow-issued client certificate. So - public docs, gated contracts, no exit path beyond a UK GDPR data portability request to privacy@heathrow.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Heathrow Airport
nav: Providers
network: true
overview: 'Heathrow Airport publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United Kingdom, Airports, Aviation, and Airport Infrastructure.


  Heathrow Airport''s developer surface includes documentation, signup flow, authentication, changelog, support, getting-started guide, engineering blog, and 18 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 27.6
  delta: 1.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 26.6
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heathrow-airport/refs/heads/main/screenshots/heathrow-airport-2026-08-07T170046.png
security:
- kind: authentication
  name: Heathrow Airport Authentication
  slug: heathrow-airport-authentication
  summary_line: mutualTLS/federated-sso · 2 schemes
- kind: domain-security
  name: Heathrow Airport Domain Security
  slug: heathrow-airport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heathrow-airport
tags:
- Travel
- United Kingdom
- Airports
- Aviation
- Airport Infrastructure
- Flight Information
- Transportation
- Passenger Experience
website: https://www.heathrow.com/
---

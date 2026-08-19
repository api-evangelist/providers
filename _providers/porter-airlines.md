---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/porter-airlines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flyporter.com/
- group: start
  title: ''
  type: TravelAgentPortal
  url: https://www.flyporter.com/en-ca/services/travel-agents
- group: start
  title: ''
  type: SignUp
  url: https://www.flyporter.com/en-ca/services/travel-agents/agency-registration
- group: start
  title: ''
  type: Login
  url: https://www.flyporter.com/en-ca/services/travel-agents/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flyporter.com/Content/Documents/TravelAgents/en/terms-and-conditions.pdf
- group: other
  title: ''
  type: Policy
  url: https://www.flyporter.com/Content/Documents/TravelAgents/en/booking-and-ticketing-policy.pdf
- group: other
  title: ''
  type: Policy
  url: https://www.flyporter.com/Content/Documents/TravelAgents/en/porter-airlines-commission-policy.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flyporter.com/en-ca/privacy
- group: operate
  title: ''
  type: Support
  url: https://porteragency.zendesk.com/hc/en-ca/requests/new
- group: company
  title: ''
  type: Newsroom
  url: https://www.flyporter.com/en-ca/about-porter/media-centre
- group: company
  title: ''
  type: About
  url: https://www.flyporter.com/en-ca/about-porter/who-we-are
- group: start
  title: ''
  type: Registry
  url: https://www.iata.org/en/about/members/airline-list/porter-airlines/670/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/porter-airlines
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/porter-airlines-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/porter-airlines-conformance.yml
created: '2026-07-28'
description: 'Porter Airlines is a Canadian carrier headquartered in Toronto, operating as Porter Airlines (Canada) Limited and Porter Airlines Inc. under IATA designator PD, IATA ticketing plate 451, and ICAO code POE. It is the challenger to the Air Canada / WestJet duopoly in Canada, flying an Embraer E195-E2 and De Havilland Dash 8 fleet across domestic, transborder and sun destinations, and it joined IATA as a member in 2026 following IOSA certification. Porter sits in the distribution chain as a conventional GDS-intermediated carrier: agencies reach its inventory through the GDSs (Sabre is named explicitly in Porter''s agency terms, and Travelport is the channel Duffel uses to resell Porter content) or through Porter''s own ticketless Travel Agency Portal on flyporter.com. Porter''s API posture is honestly stated as none-published. There is no developer portal, no public or partner API documentation, no OpenAPI, and no NDC endpoint of any kind. The developer, developers and apis subdomains
  do not resolve; api.flyporter.com resolves but does not answer on 80 or 443; docs.flyporter.com redirects to an internal Google Drive. Every well-known spec path returns 404 and the whole site sits behind a Cloudflare bot challenge with ai-train=no content signals. Access is accreditation-gated: an agency must hold ARC accreditation or an IATA Passenger Sales Agency Agreement, register on flyporter.com, and accept Porter''s Agency Terms and Conditions, which assert Porter ownership of all Porter Data, prohibit scraping and redistribution, and revoke all data rights the moment an appointment is suspended or terminated. There is no exit path beyond a written PIPEDA access request to Porter''s Privacy Officer.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Porter Airlines
nav: Providers
network: true
overview: 'Porter Airlines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Canada, Aviation, Airline, and Flights.


  Porter Airlines'' developer surface includes signup flow, support, and 14 more developer resources.'
random_paper: 78
score:
  band: emerging
  composite: 14.1
  delta: 0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 13.8
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Porter Airlines Domain Security
  slug: porter-airlines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: porter-airlines
tags:
- Travel
- Canada
- Aviation
- Airline
- Flights
- Distribution
- GDS
- Booking
- Travel Agents
- Loyalty
website: https://www.flyporter.com/
---

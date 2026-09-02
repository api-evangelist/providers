---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: British Airways' IATA New Distribution Capability API - a direct link into BA's host reservation system for flight shopping, ordering, ticketing and post-booking servicing, operated jointly across IAG
  name: British Airways NDC API
  slug: british-airways-ndc-api
artifact_total: 6
asyncapis:
- description: ''
  name: British Airways Ndc Notifications
  slug: british-airways-ndc-notifications
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/british-airways-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/british-airways-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/british_airways_vdp
- group: auth
  title: ''
  type: Authentication
  url: authentication/british-airways-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/british-airways-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/british-airways-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/british-airways-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/british-airways-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/british-airways-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/british-airways-ndc-notifications.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/british-airways-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/british-airways-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/british-airways-llms.txt
- group: operate
  title: ''
  type: Roadmap
  url: https://ndc.ba.com/developer/ndc-product-api-roadmap
- group: company
  title: ''
  type: Website
  url: https://www.britishairways.com/
- group: start
  title: ''
  type: Portal
  url: https://ndc.ba.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.britishairways.com/travel-partner-connect/en/kr/policies/booking-and-ticketing/distribution-technology-charge-guide
- group: docs
  title: ''
  type: Documentation
  url: https://www.britishairways.com/assets/pdfs/updates/distribution-technology-charge.pdf
- group: start
  title: ''
  type: LegacyPortal
  url: https://developer.iairgroup.com/british_airways
- group: company
  title: ''
  type: Newsroom
  url: https://mediacentre.britishairways.com/
- group: company
  title: ''
  type: Investors
  url: https://www.iairgroup.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/british-airways
created: '2026-07-28'
description: 'British Airways Plc is the United Kingdom''s flag carrier, headquartered at Waterside near London Heathrow and owned since 2011 by International Consolidated Airlines Group (IAG), which also owns Iberia, Aer Lingus, Vueling and LEVEL. In the distribution chain BA is a supplier of its own seat inventory, reached either through the three legacy GDSs, through IATA NDC connections it operates itself, or direct on ba.com. BA was one of the earliest and most aggressive NDC adopters: from 1 November 2017 IAG applied a per-fare-component Distribution Technology Charge to BA and Iberia marketed fares that are not booked through an NDC based connection or a low-cost channel such as ba.com, explicitly pricing GDS intermediation out of the stack. Its API posture is honest to state plainly - the NDC distribution API is real and is built on the IATA EDIST message set, but there is no public specification, no published base URL, no self-serve signup and no exit path. Access requires registration,
  a B1 or B2 certification form, acceptance of the British Airways API and Services Trial Use Agreement plus the Travel Agency Addendum for IATA accredited agents, and signed live API contracts. The older public consumer REST APIs (Flight Information, Flight Offers, Lowest Prices, In-Flight Entertainment, Hotel/Car/Flight packages) on the IAG Developer Programs portal are gone: as of 2026-07-28 developer.iairgroup.com returns HTTP 404 and api.ba.com returns HTTP 596 ERR_596_SERVICE_NOT_FOUND for every documented resource.'
image: https://images.ctfassets.net/nwnmkeyu03hy/1qDtSOnE37fsTzD4GPdfFN/347c175022b9aec007a10630028a4439/British-Airways-logo.png
layout: provider
modified: '2026-07-28'
name: British Airways
nav: Providers
network: true
overview: 'British Airways publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Distribution.


  The British Airways catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  British Airways'' developer surface includes authentication, sandbox, developer portal, documentation, and 18 more developer resources.'
random_paper: 16
scopes:
- name: British Airways Scopes
  scope_count: 4
  slug: british-airways-scopes
  summary_line: 4 scopes · authorizationCode/implicit/deviceCode
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 19.0
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.7
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/british-airways/refs/heads/main/screenshots/british-airways-2026-08-07T162825.png
security:
- kind: authentication
  name: British Airways Authentication
  slug: british-airways-authentication
  summary_line: openIdConnect/apiKey · 2 schemes
- kind: domain-security
  name: British Airways Domain Security
  slug: british-airways-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: British Airways Vulnerability Disclosure
  slug: british-airways-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: british-airways
tags:
- Travel
- United Kingdom
- Aviation
- Airline
- Distribution
- NDC
- Booking
- Corporate Travel
- Airports
website: https://www.britishairways.com/
---

---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Breeze Airways NDC gateway is the airline's direct-connect distribution API for accredited travel partners. It speaks IATA Offers and Orders (NDC) 21.3 XML over HTTPS on a Navitaire-hosted gateway
  name: Breeze Airways NDC Gateway
  slug: breeze-airways-ndc-gateway
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.flybreeze.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ndc.flybreeze.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.flybreeze.com/docs/category/ndc-for-developers
- group: docs
  title: ''
  type: APIReference
  url: https://ndc.flybreeze.com/docs/category/ndc-shopping
- group: start
  title: ''
  type: GettingStarted
  url: https://ndc.flybreeze.com/docs/ndc-for-developers/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://ndc.flybreeze.com/docs/become-a-breeze-partner
- group: operate
  title: ''
  type: Support
  url: https://www.flybreeze.com/support
- group: company
  title: ''
  type: Blog
  url: https://ndc.flybreeze.com/news
- group: operate
  title: ''
  type: StatusPage
  url: https://ndc.flybreeze.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://ndc.flybreeze.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/breeze-airways-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flybreeze.com/page/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://media.flybreeze.com/docs/policies/privacypolicy.pdf
- group: company
  title: ''
  type: Careers
  url: https://jobs.flybreeze.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/breeze-airways-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/breeze-airways-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/breeze-airways-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/breeze-airways-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/breeze-airways-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/breeze-airways-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/breeze-airways-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/breeze-airways-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/breeze-airways-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breeze-airways-domain-security.yml
created: '2026-08-01'
description: Breeze Airways (Breeze Aviation Group, Inc.) is an American low-cost point-to-point airline headquartered in Cottonwood Heights, Utah, founded by David Neeleman and flying since May 2021. Its distribution technology surface is a partner-facing IATA NDC gateway, documented at the Breeze B2B portal (ndc.flybreeze.com), which exposes IATA Offers and Orders 21.3 XML messages — AirlineProfile, AirShopping, OfferPrice, ServiceList, SeatAvailability and OrderCreate for shopping and selling, plus OrderRetrieve, OrderQuote, OrderReshop and OrderChange for servicing — over a Navitaire-hosted, IP-allowlisted gateway secured with a per-partner Azure API Management subscription key and a 30-minute session bearer token. Access is limited to accredited travel-agency partners (OTA, TMC and US federal government) with an IATA/ARC number and an executed commercial agreement; Breeze also distributes over Amadeus and Travelport GDS and via the TravelPro agent booking portal.
image: https://ndc.flybreeze.com/img/breeze-b2b-social-card.jpg
layout: provider
modified: '2026-08-01'
name: Breeze Airways
nav: Providers
network: true
overview: 'Breeze Airways publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Airlines, Travel, Aviation, and NDC.


  Breeze Airways'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 18 more developer resources.'
random_paper: 25
scopes:
- name: Breeze Airways Scopes
  scope_count: 0
  slug: breeze-airways-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Breeze Airways Authentication
  slug: breeze-airways-authentication
  summary_line: apiKey/http-basic/http-bearer/oauth2 · 4 schemes
- kind: domain-security
  name: Breeze Airways Domain Security
  slug: breeze-airways-domain-security
  summary_line: TLSv1.3 · DMARC
slug: breeze-airways
tags:
- Company
- Airlines
- Travel
- Aviation
- NDC
- Distribution
- Booking
- Reservations
- Travel Agencies
- IATA
website: https://www.flybreeze.com/
---

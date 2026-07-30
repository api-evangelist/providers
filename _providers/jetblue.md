---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetblue-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jetblue-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jetblue-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://accounts.jetblue.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jetblue-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jetblue-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jetblue.com/legal/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jetblue-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jetblue-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/jetblue-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.jetblue.com/
- group: company
  title: ''
  type: About
  url: https://www.jetblue.com/our-company
- group: other
  title: ''
  type: Brands
  url: https://www.jetblue.com/our-company/our-brands
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.jetblue.com/travel-agents
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetblue.com/travel-agents/ndc
- group: start
  title: ''
  type: Onboarding
  url: https://www.jetblue.com/travel-agents/ticketing-authority
- group: other
  title: ''
  type: Policies
  url: https://www.jetblue.com/travel-agents/booking-policies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jetblue.com/legal/website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jetblue.com/legal/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://www.jetblue.com/legal
- group: other
  title: ''
  type: ContractOfCarriage
  url: https://legacycms.jetblue.com/public/dam/ui-assets/p/contract_of_carriage.pdf
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.jetblue.com/legal/vulnerability-disclosure-policy
- group: operate
  title: ''
  type: Support
  url: https://www.jetblue.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jetblue
created: '2026-07-28'
description: 'JetBlue Airways (IATA code B6) is a New York-headquartered low-cost United States carrier flying across the U.S., Caribbean, Latin America and Europe, with hubs and focus cities at JFK, Boston, Fort Lauderdale, Orlando and San Juan. In the travel distribution chain JetBlue sits as an inventory owner that sells through three channels: its own direct consumer surface (jetblue.com, the JetBlue app and the TrueBlue loyalty program), the legacy GDS channel where it files fares, seats and EMDs and settles through ARC in the U.S. and IATA BSPs internationally, and an IATA New Distribution Capability program that reaches agencies through GDS/NDC aggregators, corporate booking tools and online booking platforms. JetBlue publishes no public developer portal, no API reference and no downloadable OpenAPI or NDC schema: developer.jetblue.com, developers.jetblue.com and docs.jetblue.com do not resolve, api.jetblue.com answers 404 at every probed path, and the 361-URL public sitemap contains
  no developer or API page. The only published distribution surface is the travel-agent policy section at jetblue.com/travel-agents, including an NDC program page that states JetBlue supplies NDC API documentation, schema and message samples and certification guidelines to onboarded partners only, after business use-case submission, onboarding and certification testing. Selling JetBlue requires ARC accreditation in the U.S. or IATA accreditation plus local BSP participation abroad; JetBlue states it works with only a few OTAs and is not accepting new applications. Public docs, accreditation required, no self-serve access, and no exit path.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: JetBlue
nav: Providers
network: true
overview: 'JetBlue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United States, Aviation, Airline, and Distribution.


  JetBlue''s developer surface includes authentication, documentation, legal docs, support, and 20 more developer resources.'
random_paper: 9
scopes:
- name: Jetblue Scopes
  scope_count: 7
  slug: jetblue-scopes
  summary_line: 7 scopes · authorizationCode/implicit/deviceCode
score:
  band: emerging
  composite: 18.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: authentication
  name: Jetblue Authentication
  slug: jetblue-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Jetblue Domain Security
  slug: jetblue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jetblue Vulnerability Disclosure
  slug: jetblue-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: jetblue
tags:
- Travel
- United States
- Aviation
- Airline
- Distribution
- NDC
- GDS
- Booking
- Loyalty
website: https://www.jetblue.com/
---

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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The direct-connect flight shopping, booking, payment and servicing API that Air Transat publishes to OTA and technology partners under its NDC programme. The only technical contract Transat publishes '
  name: Air Transat NDC Direct Connect API (Radixx ConnectPoint)
  slug: air-transat-ndc-direct-connect-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/transat-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/transat-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/transat-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/transat-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/transat-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/transat-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transat-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.transat.com/
- group: company
  title: ''
  type: Website
  url: https://www.airtransat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.airtransat.com/en-CA/air-transat-ndc
- group: company
  title: ''
  type: Partners
  url: https://www.transatagentdirect.com/
- group: operate
  title: ''
  type: Support
  url: https://www.airtransat.com/en-CA/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airtransat.com/en-CA/legal-notice/terms-of-use-of-the-air-transat-sites
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.transat.com/en-CA/website-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airtransat.com/en-CA/legal-notice/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.airtransat.com/en-CA/legal-notice
- group: commercial
  title: ''
  type: Legal
  url: https://www.airtransat.com/en-CA/legal-notice/conditions-of-carriage-and-tariffs
- group: company
  title: ''
  type: Blog
  url: https://experience.transat.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/air-transat
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AirTransat
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.transat.com/en-CA/corporate/investors
- group: company
  title: ''
  type: About
  url: https://www.transat.com/en-CA/corporate/about-transat
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-28'
description: 'Transat A.T. Inc. (TSX: TRZ) is a Montreal-headquartered, vertically integrated Canadian leisure travel group. It operates Air Transat (IATA carrier code TS), a transatlantic and sun-destination leisure airline, alongside tour-operating brands (Transat / Transat Tours Canada Inc.) and one of Canada''s largest retail travel agency networks (Transat Travel, Voyages Transat, Marlin Travel, Club Voyages). It sits on the supply side of the distribution chain: it owns the seat and package inventory, sells it direct through transat.com and airtransat.com, through its own retail agencies, through GDS/CRS EDIFACT channels governed by IATA Resolution 850m and BSP settlement, and — since its published NDC programme — through an Accelya Farelogix NDC gateway and a named set of NDC aggregators. Its API posture is partner-gated but not opaque: Air Transat publishes a public NDC connectivity page and a publicly downloadable 46-page "Air Transat API specifications" document, but that document
  is a proprietary Radixx ConnectPoint SOAP contract (v2.2.4, May 2023), not an IATA NDC schema. There is no self-serve developer portal, no machine-readable OpenAPI or WSDL, no published base URL, no sandbox, no bulk export operation, and no IATA NDC certification level is claimed. Credentials (a Transat-assigned IATA number, agency login and password) are issued only under a commercial agreement, and the site terms plus the CRS Booking and Ticketing Procedures Policy expressly prohibit scraping and prohibit redistributing Air Transat content to any third-party agent, GDS or metasearch engine without prior written consent.'
image: https://airtransatcommedia.blob.core.windows.net/tswcm/media/tsca/skin/img/logos/logo-airtransat-header-destop-2023.svg
layout: provider
modified: '2026-07-28'
name: Transat
nav: Providers
network: true
overview: 'Transat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Canada, Aviation, Airline, and Distribution.


  Transat''s developer surface includes authentication, changelog, documentation, support, legal docs, engineering blog, and 19 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 21.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 21.1
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: authentication
  name: Transat Authentication
  slug: transat-authentication
  summary_line: vendor-credential-exchange · 2 schemes
- kind: domain-security
  name: Transat Domain Security
  slug: transat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transat
tags:
- Travel
- Canada
- Aviation
- Airline
- Distribution
- NDC
- Booking
- Tour Operator
- Corporate Travel
- GDS
website: https://www.transat.com/
---

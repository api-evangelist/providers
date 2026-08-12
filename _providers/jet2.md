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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jet2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jet2.com/
- group: company
  title: ''
  type: Website
  url: https://www.jet2holidays.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://trade.jet2holidays.com/
- group: commercial
  title: ''
  type: AgencyAgreement
  url: https://www.jet2holidays.com/-/media/pdfs/agency%20agreement_april_2025.pdf
- group: commercial
  title: ''
  type: AgencyAgreement
  url: https://www.jet2holidays.com/-/media/pdfs/new_agencyagreement_jet2holidays.pdf
- group: other
  title: ''
  type: ConsumerProtection
  url: https://www.jet2holidays.com/atol
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.jet2.com/en/carrier-information-and-liability-notice
- group: company
  title: ''
  type: About
  url: https://www.jet2.com/en/about-us
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.jet2plc.com/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Jet2_plc
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Jet2.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jet2plc.com/privacy
- group: company
  title: ''
  type: About
  url: https://jet2traveltech.com/
- group: company
  title: ''
  type: Blog
  url: https://jet2traveltech.com/blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://jet2traveltech.com/blogs/feed/
- group: other
  title: ''
  type: DesignSystem
  url: https://design.jet2.com/
- group: build
  title: ''
  type: SourceCode
  url: https://jet2tfs.visualstudio.com/Jet2Digital
- group: build
  title: ''
  type: Packages
  url: packages/jet2-packages.yml
- group: design
  title: ''
  type: Components
  url: components/jet2-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jet2-llms.txt
created: '2026-07-28'
description: 'Jet2 plc (London Stock Exchange: JET2, formerly Dart Group plc) is a British leisure travel group headquartered at Low Fare Finder House, Leeds Bradford Airport, Yeadon, Leeds, West Yorkshire — an address confirmed verbatim in the Extended Validation TLS certificate served by www.jet2.com, issued to "JET2.COM LIMITED", company serial number 02739537, jurisdiction GB. Its home market is the United Kingdom. The group combines two businesses that are unusual in this sector for being deliberately fused: Jet2.com (IATA code LS, ICAO code EXS), the UK''s third-largest airline, and Jet2holidays, the UK''s largest ATOL holder and leading provider of ATOL-protected package holidays to the Mediterranean, the Canary Islands and European city destinations. For the year ended 31 March 2026 the group reported revenue of £7,482.1 million, operating profit of £439.6 million and a record 20.83 million passengers, flying from 14 UK airport bases including newly added London Luton and London
  Gatwick, with more than 63% of flown passengers buying an end-to-end package holiday and 155 Airbus A321neo aircraft on order. Jet2holidays sells through its own website and through more than 2,500 independent UK travel agent partners, and carries ABTA number Y1256. Where Jet2 sits in the distribution chain is the point of this record. Like easyJet and Ryanair, Jet2.com was built with no Global Distribution System dependency at all: it never filed fares into the GDS rail that Amadeus, Sabre and Travelport have intermediated for forty years, and it therefore never needed IATA''s New Distribution Capability as a remedy. Travelport supports Jet2 in Smartpoint only as a "Direct Payment Carrier" — its low-cost-carrier workaround — point-to-point only, no connecting flights, and with no post-booking change or cancellation possible through the GDS at all ("Requests for changes must be made directly through Jet2"). In June 2025 Jet2.com signed a distribution agreement with airline technology company
  Kyte, whose Kyte Direct Connect (KDC) JSON/REST API "standardises airline NDC and LCC proprietary content", opening Jet2 seats and ancillaries to travel management companies and corporate booking tools for the first time, with the same content reaching agency desktops through AirGateway. Separately, Jet2holidays operates an agency API that lets independent agents sell Jet2 packages on their own bookable websites for commission. Its API posture, stated honestly, is that Jet2 runs real production distribution APIs and publishes nothing about them. There is no developer portal — developer.jet2.com, developers.jet2.com, docs.jet2.com, apis.jet2.com, ndc.jet2.com, partner.jet2.com and trade.jet2.com all fail to resolve — no API reference, no OpenAPI, Swagger, AsyncAPI or GraphQL contract, no security.txt, no .well-known catalogue and no official GitHub organisation. api.jet2.com resolves and answers HTTP 200 with nothing but the stock Microsoft IIS 10.0 default page, 404 on every spec path
  probed. Access is by commercial agreement only, negotiated bilaterally or through Kyte, whose own FAQ states that "Access to airline products is controlled by each airline." This record is an honest stub: apis[] is intentionally empty because no Jet2 API is publicly documented, and listing an undocumented hostname as an API would be fabrication. The evidence, including every URL probed with its HTTP status, is in review.yml. A second enrichment pass on 28 July 2026 found the one genuinely public first-party developer surface Jet2 has, and it is not an API: the Jet2 Design System, published as two npm packages under the @jet2 scope (design tokens for seven brand themes, and a React component library containing a single Button), sourced from Jet2''s private Azure DevOps organisation at jet2tfs.visualstudio.com/Jet2Digital and documented at design.jet2.com behind a Supernova login. Both packages were last published in April 2024. The same pass confirmed no /.well-known/ document on any host
  that answers, no security.txt, no vulnerability disclosure programme, no trust centre, no public Postman collection and no SDK in any package registry. Jet2''s engineering voice, such as it is, comes from Jet2 Travel Technologies (J2TT), its in-house development centre in Pune, India, which runs a public blog with an RSS feed.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Jet2
nav: Providers
network: true
overview: 'Jet2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Low Cost Carrier.


  Jet2''s developer surface includes engineering blog and 20 more developer resources.'
random_paper: 25
score:
  band: minimal
  composite: 9.1
  delta: -0.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jet2/refs/heads/main/screenshots/jet2-2026-08-07T171005.png
security:
- kind: domain-security
  name: Jet2 Domain Security
  slug: jet2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jet2
tags:
- Travel
- United Kingdom
- Aviation
- Airline
- Low Cost Carrier
- Package Holidays
- Tour Operator
- Distribution
- Booking
- Ancillaries
- Partner Gated
website: https://www.jet2.com/
---

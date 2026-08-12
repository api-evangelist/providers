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
  url: security/ihg-hotels-domain-security.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/ihg-hotels-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ihg-hotels-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ihg-hotels-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/ihg-hotels-packages.yml
- group: agent
  title: ''
  type: MCPAssessment
  url: mcp/ihg-hotels-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ihg-hotels-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ihg.com/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.ihgplc.com/
- group: company
  title: ''
  type: PartnerProgram
  url: https://partnerconnect.ihg.com/
- group: operate
  title: ''
  type: PartnerProgramFAQ
  url: https://partnerconnect.ihg.com/wp-content/uploads/2017/04/FAQ-PartnerConnect.pdf
- group: start
  title: ''
  type: SignUp
  url: https://signup.cj.com/member/signup/publisher/?cid=1675692
- group: start
  title: ''
  type: RetiredDeveloperPortal
  url: https://web.archive.org/web/20170503133654/https://pcroomservice.ihg.com/api_description
- group: commercial
  title: ''
  type: RetiredAPITermsOfUse
  url: https://web.archive.org/web/20150926153219/https://pcroomservice.ihg.com/Terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ihg.com/content/us/en/customer-care/privacy_statement
- group: start
  title: ''
  type: PrivacyPortal
  url: https://www.ihg.com/content/us/en/customer-care/privacy-and-cookie-center
- group: commercial
  title: ''
  type: LoyaltyTerms
  url: https://www.ihg.com/content/gb/en/customer-care/member-tc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ihg.com/hotels/gb/en/global/customer_care/tc
- group: other
  title: ''
  type: Brands
  url: https://www.ihg.com/content/gb/en/about/brands
- group: start
  title: ''
  type: TravelAgentPortal
  url: https://www.ihgagent.com/home
- group: company
  title: ''
  type: Careers
  url: https://careers.ihg.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.ihgplc.com/en/investors
- group: operate
  title: ''
  type: Contact
  url: mailto:partnerconnect@ihg.com
- group: operate
  title: ''
  type: Contact
  url: mailto:privacyoffice@ihg.com
- group: operate
  title: ''
  type: Support
  url: https://www.ihgplc.com/en/contact-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.ihgplc.com/en/news-and-media/news-releases
- group: build
  title: ''
  type: PolicyLibrary
  url: https://www.ihgplc.com/en/responsible-business/policies-and-position-statements/policy-documents
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ihg
created: '2026-07-28'
description: 'InterContinental Hotels Group PLC (trading as IHG Hotels & Resorts) is a British asset-light hotel group headquartered at Windsor Dials, 1 Arthur Road, Windsor, Berkshire SL4 1RS, United Kingdom, with an Americas office at 3 Ravinia Drive, Atlanta, Georgia. Its own corporate site states 7,014 hotels and 1,035,589 rooms across more than 100 countries, around 400,000 colleagues, 20 brands and the IHG One Rewards loyalty programme (figures read from ihgplc.com on 2026-07-28). The brand portfolio spans Six Senses, Regent, InterContinental, Vignette Collection, Kimpton, Hotel Indigo, voco, HUALUXE, Crowne Plaza, EVEN Hotels, Holiday Inn, Holiday Inn Express, Holiday Inn Resorts, Holiday Inn Club Vacations, Garner, avid, Atwell Suites, Staybridge Suites, Candlewood Suites, IHG Army Hotels and Iberostar Beachfront Resorts. In the distribution chain IHG sits on the supply side as a franchisor and manager rather than an owner: it aggregates independently owned and operated properties
  into a single central reservation system and pushes that inventory out through its own ihg.com and app direct channels, through the three GDSs and their agency terminals, through OTAs and wholesalers, and through corporate and group channels. Critically, IHG does not run its own reservation platform any more. It announced a partnership with Amadeus in 2015 to build a cloud Guest Reservation System to replace HOLIDEX, its proprietary system in service since 1965, and migrated onto it across 2018 and early 2019 — so the hotel group most likely to be a lock-in vendor is itself a customer of a GDS company''s platform, and group bookings land in Amadeus Delphi and Meeting Broker. Its API posture, stated honestly, is gated and undocumented. There is no live developer portal. The one that existed — PartnerConnect RoomService at pcroomservice.ihg.com, a TIBCO Mashery portal publishing five rate, availability and hotel-content APIs — is decommissioned: the hostname is NXDOMAIN on Google, Cloudflare
  and Quad9 resolvers as of 2026-07-28 and the Internet Archive holds no page capture after 2019. What remains live is partnerconnect.ihg.com (HTTP 200), an affiliate marketing programme whose signup routes to Commission Junction and which still advertises "access to real-time hotel rates, availability and hotel content API''s" without linking to any technical resource. Real API hostnames exist — api.ihg.com CNAMEs to ihg.api.mashery.com with an sb-ihg.mashery.com sandbox, and apis.ihg.com, b2b.ihg.com, mcp.ihg.com, booking.ihg.com and concerto.ihg.com all sit behind Akamai — but every one returns 403 Access Denied or 401 on every path probed, including /openapi.json, /swagger.json, /api-docs and /.well-known/. No OpenAPI, Swagger, AsyncAPI, GraphQL SDL, WSDL, XSD, OpenTravel/OTA or HTNG reference is published anywhere by IHG. apis[] is deliberately empty: listing an Akamai-gated hostname or a decommissioned 2017 portal as a live API would be fabrication. The value of this record is the
  switchingCost block in review.yml, which captures what published IHG documents actually say about what it costs to leave — including the archived RoomService Terms of Use classing "API parameters" as Confidential Information and binding partners to the Master PartnerConnect Terms and Conditions plus the Six Continents Hotels E-commerce Master Service Agreement, and the current IHG One Rewards member terms stating that members whose accounts are cancelled "by IHG or by the Member, will forfeit all Points, Point vouchers, Reward Nights, and any other benefits associated with the account".'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: IHG Hotels & Resorts
nav: Providers
network: true
overview: 'IHG Hotels & Resorts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United Kingdom, Hospitality, Hotels, and Booking.


  IHG Hotels & Resorts'' developer surface includes signup flow, support, and 26 more developer resources.'
random_paper: 84
score:
  band: emerging
  composite: 13.4
  delta: -2.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ihg-hotels/refs/heads/main/screenshots/ihg-hotels-2026-08-07T170619.png
security:
- kind: domain-security
  name: Ihg Hotels Domain Security
  slug: ihg-hotels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ihg-hotels
tags:
- Travel
- United Kingdom
- Hospitality
- Hotels
- Booking
- Distribution
- GDS
- Loyalty
- Affiliate
- Partner Gated
website: https://www.ihg.com/
---

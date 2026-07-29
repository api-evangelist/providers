---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: easyJet's hosted client-side widget platform for partner and white-label sites. Each widget is a script tag on brand.easyjet.com whose behaviour is driven by query-string parameters and scoped to a pa
  name: easyJet Brand Widget Service (easyDom)
  slug: brand-widgets
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/easyjet-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/easyjet-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/easyjet-llms.txt
- group: other
  title: ''
  type: DiscoveryProbe
  url: well-known/easyjet-well-known.yml
- group: operate
  title: ''
  type: Support
  url: https://www.easyjet.com/en/help
- group: start
  title: ''
  type: SignUp
  url: https://www.easyjet.com/en/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.easyjet.com/en/policy/privacy
- group: company
  title: ''
  type: Website
  url: https://www.easyjet.com/
- group: other
  title: ''
  type: DistributionCharter
  url: https://www.easyjet.com/en/business/distribution-charter
- group: other
  title: ''
  type: ApprovedChannels
  url: https://www.easyjet.com/en/business/approved-channels-
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.easyjet.com/en/business/travel-trade-partners
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.easyjet.com/en/policy/acceptable-use
- group: commercial
  title: ''
  type: PrivacyNotice
  url: https://www.easyjet.com/en/policy/privacy
- group: commercial
  title: ''
  type: PrivacyNotice
  url: https://www.easyjet.com/ejcms/cache/medialibrary/Files/Privacy-notice/DL8050-Web-privacy-policy-2023-V3.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.easyjet.com/en/terms-and-conditions
- group: other
  title: ''
  type: BusinessFares
  url: https://www.easyjet.com/en/business/business-fares
- group: operate
  title: ''
  type: Contact
  url: mailto:charters@easyjet.com
- group: operate
  title: ''
  type: Contact
  url: mailto:data.protection@easyJet.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/easyjet
- group: company
  title: ''
  type: Careers
  url: https://careers.easyjet.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://corporate.easyjet.com/
created: '2026-07-28'
description: 'easyJet Airline Company Limited is a British low-cost short-haul carrier registered in England (company number 03034606, registered office Hangar 89, London Luton Airport, Luton, Bedfordshire, LU2 9PF), flying a point-to-point network that its own trade pages describe as connecting more than 155 airports across 35 countries. Its home market is the United Kingdom and its commercial centre of gravity is intra-European leisure and short-haul business traffic, extended by the easyJet holidays package business and by ancillary products (seat selection, hold and large cabin bags, Flex, Pass Extra, Smart+, Inclusive and Inclusive Plus fare bundles). easyJet sits at the direct end of the airline distribution chain. It was built without a GDS dependency and still sells the overwhelming majority of its seats through its own website and app; agency and OTA access exists but is a controlled secondary channel rather than the primary rail. That channel is governed by a published Distribution
  Charter (version March 2026) which permits a Reseller to access easyJet Data in exactly two ways — "via an easyJet Approved Channel which has entered into an API agreement with easyJet" or "directly via the easyJet API, if the Reseller has a Direct API Agreement with easyJet" — and which explicitly forbids screen scraping and any other automated extraction. easyJet publishes the list of Approved Channels and a per-partner functionality matrix current to the end of May 2026: Amadeus, Anaxys, Bewotec, Duffel, JFA Systems, Kyte, Paxport, Peakwork, Sabre, Travelfusion, Travelport, Traveltek, Viaxoft and Ypsilon. Its API posture, stated honestly, is commercial-agreement-gated and undocumented. There is no developer portal — developer, developers, docs, apis, ndc, partner, partners, trade, agent, sandbox, dev, portal, connect and xml subdomains of easyjet.com all fail to resolve — and no machine-readable contract of any kind is published: no OpenAPI, no Swagger, no AsyncAPI, no GraphQL schema,
  no security.txt, no llms.txt and no .well-known API catalogue. Two real API hostnames do exist, api.easyjet.com and b2b.easyjet.com, but both sit behind Akamai and return HTTP 403 Access Denied on every path probed. Just as importantly, easyJet is not an NDC carrier: the March 2026 charter never mentions NDC, easyJet does not appear on ndctracker.com''s list of 73 airlines with launched or in-development NDC programmes, and its aggregators describe the connection as a direct-connect API rather than an NDC one — Duffel labels it "Direct Connect". A reseller therefore integrates against a bilateral, proprietary, unpublished interface under an English-law contract that easyJet may amend without notice and under which it reserves the right to restrict, suspend or terminate access and to cancel bookings already made. A second enrichment pass on 2026-07-28 did find one live, anonymously reachable easyJet integration surface the first pass missed: the easyWidget / easyDom partner component platform
  at brand.easyjet.com, a hosted JavaScript widget service that partner and white-label sites embed for easyJet page chrome and for easyJet customer sign-in, registration and visitor recognition. It is undocumented, partner-scoped by a query-string partner identifier and built on legacy jQuery, but it is real and it is the only easyJet interface that answers a stranger with a 200. The REST hostnames stay closed, and this record stays honest about the difference: only what can be verified is catalogued, and an Akamai-gated hostname is still not listed as an API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: easyJet
nav: Providers
network: true
overview: 'easyJet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Low Cost Carrier.


  easyJet''s developer surface includes support, signup flow, and 19 more developer resources.'
random_paper: 28
score:
  band: emerging
  composite: 17.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: domain-security
  name: Easyjet Domain Security
  slug: easyjet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: easyjet
tags:
- Travel
- United Kingdom
- Aviation
- Airline
- Low Cost Carrier
- Europe
- Distribution
- Booking
- Ancillaries
- Partner Gated
website: https://www.easyjet.com/
---

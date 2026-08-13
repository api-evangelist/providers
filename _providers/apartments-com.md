---
access_model:
  confidence: high
  label: Partner-only · Advertising contract + approved feed vendor
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - documentation
  trial: false
  try_now: false
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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apartments-com-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apartments-com-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/apartments-com-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apartments-com-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.apartments.com
- group: company
  title: ''
  type: About
  url: https://www.apartments.com/about
- group: other
  title: ''
  type: Parent
  url: https://www.costargroup.com/about-us/brands/apartmentscom
- group: operate
  title: ''
  type: Support
  url: https://propertyhelp.apartments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://propertyhelp.apartments.com/collection/1044-ils-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://propertyhelp.apartments.com/collection/1201-mls-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://propertyhelp.apartments.com/article/439-what-is-a-feed
- group: docs
  title: ''
  type: Documentation
  url: https://ecom.apartments.com/advertise/resources/listings-feed-program
- group: company
  title: ''
  type: Partners
  url: https://www.apartments.com/advertise/advfeeds
- group: operate
  title: ''
  type: Contact
  url: mailto:Feeds@apartments.com
- group: operate
  title: ''
  type: Support
  url: https://renterhelp.apartments.com/
- group: other
  title: ''
  type: Product
  url: https://www.apartments.com/rental-manager
- group: start
  title: ''
  type: Login
  url: https://www.apartments.com/prosumer/login/
- group: start
  title: ''
  type: SignUp
  url: https://www.apartments.com/rental-manager/list-property-for-rent
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apartments.com/grow/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apartments.com/grow/about/privacy-notice
- group: commercial
  title: ''
  type: Legal
  url: https://www.apartments.com/grow/about/legal-terms
- group: operate
  title: ''
  type: Contact
  url: mailto:advertise@apartments.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AptsCom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apartments-com
- group: company
  title: ''
  type: Twitter
  url: https://x.com/apartmentscom
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@apartmentscom
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/apartmentscom/
created: '2026-07-26'
description: 'Apartments.com is the largest United States rental-listings marketplace, owned by CoStar Group since its 2014 acquisition and operated from Arlington, Virginia as the anchor of the Apartments.com Network — a group of consumer rental sites that also includes ApartmentFinder.com, ApartmentHomeLiving.com, ForRent.com, ForRentUniversity.com, WestsideRentals.com, Apartamentos.com, After55.com and CorporateHousing.com. It sits on the demand side of the US residential value chain as an Internet Listing Service (ILS): apartment owners and property managers buy advertising, and their inventory, availability, pricing, media, concessions and fee data flows in from property management systems (Yardi, RealPage, Entrata, MRI, AppFolio, ResMan, Rent Manager, Funnel, EliseAI and others) rather than from any public API, while leads flow back out to the advertiser''s CRM. Its API posture is closed. Apartments.com publishes no developer portal, no OpenAPI or OData $metadata contract, no SDK,
  no webhooks and no Postman collection; developer.apartments.com, developers.apartments.com and docs.apartments.com do not resolve in DNS, and api.apartments.com resolves only to the same Akamai edge that returns HTTP 403 Access Denied to every non-browser request, including robots.txt. The one documented machine-to-machine seam is the Digital Feeds Program — an approval-and-contract path in which an approved third-party feed vendor syndicates a paying advertiser''s listings into Apartments.com over FTP using an XML listings feed whose specification guide is available only on request to Feeds@apartments.com. A second inbound seam lets licensed agents opt in to rental-listing syndication through their own MLS (Bright MLS, ARMLS, REcolorado, OneKey MLS, SmartMLS, NorthstarMLS, MLS PIN, Garden State MLS, New Jersey MLS and Aspen Glenwood MLS are documented), which requires MLS membership. On RESO, the honest reading is absence rather than "certified but unreachable": Apartments.com does not
  appear anywhere in the RESO certificates list, and its own property-manager help centre returns zero results for "RESO". It is a consumer of MLS rental feeds, not a certified RESO endpoint, and no unlicensed open dataset is published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apartments-com.png
layout: provider
modified: '2026-07-26'
name: Apartments.com
nav: Providers
network: true
overview: 'Apartments.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United States, Rentals, Property Listings, and Multifamily.


  Apartments.com''s developer surface includes support, documentation, signup flow, legal docs, YouTube channel, and 22 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 17.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 17.4
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apartments-com/refs/heads/main/screenshots/apartments-com-2026-08-07T161441.png
security:
- kind: authentication
  name: Apartments Com Authentication
  slug: apartments-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Apartments Com Domain Security
  slug: apartments-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apartments-com
tags:
- Real Estate
- United States
- Rentals
- Property Listings
- Multifamily
- Internet Listing Service
- Listings Syndication
- Property Management
- MLS
- PropTech
- CoStar Group
website: https://www.apartments.com
---

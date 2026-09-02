---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homes-com-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.costargroup.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/homes-com-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.costargroup.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/homes-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.costargroup.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/homes-com-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/homes-com-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/homes-com-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.homes.com/
- group: company
  title: ''
  type: About
  url: https://www.homes.com/about/
- group: operate
  title: ''
  type: Support
  url: https://support.homes.com/
- group: company
  title: ''
  type: Blog
  url: https://www.homes.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.homes.com/about/homesterms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.homes.com/about/policies/#privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.homes.com/about/accessibility/
- group: operate
  title: ''
  type: Contact
  url: https://www.homes.com/about/contact-us/
- group: other
  title: ''
  type: Sitemap
  url: https://www.homes.com/sitemap/
- group: other
  title: ''
  type: Parent
  url: https://www.costargroup.com/
- group: other
  title: ''
  type: Predecessor
  url: https://www.homesnap.com/
- group: other
  title: ''
  type: StandardsBody
  url: https://www.reso.org/certification/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.homes.com/solutions/membership
- group: start
  title: ''
  type: SignUp
  url: https://www.homes.com/solutions/join-now
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Homesnap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoStarGroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/homes-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/homesdotcom
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/homesdotcom
created: '2026-07-26'
description: 'Homes.com is a United States residential real estate portal owned by CoStar Group, which acquired the property in 2021 and folded the Homesnap agent application into it — homesnap.com now issues an HTTP 301 to www.homes.com. It sits on the consumer-facing portal layer of the US housing value chain, alongside Zillow, Realtor.com, and Redfin: it aggregates for-sale, for-rent, and off-market listings sourced from Multiple Listing Services and broker syndication, and monetises through an agent-first "your listing, your lead" advertising and agent-directory product rather than through data distribution. Its API posture is empty in both directions of the RESO question. Homes.com appears in the RESO organization directory as an active Technology Company (OrganizationUniqueId T00000143), but the Data Dictionary and Web API certification columns for that row are blank — it holds no RESO certification of any version, unlike rival Move/Realtor.com (Data Dictionary 1.7 Passed, Web API
  Core 2.0.0 Passed) or Zillow''s Bridge Interactive (Data Dictionary 1.7 and Web API Core 2.0.0, Certified Legacy). Separately, no developer surface is published at all: developer., developers., api., docs., apis., dev., idx., feeds., and data. subdomains of homes.com do not resolve in DNS, and every path on www.homes.com returns HTTP 403 to non-browser clients behind Akamai bot protection. Listing data moves INTO Homes.com from MLSs and brokers via syndication opt-in, not OUT through any documented API. No OpenAPI, no OData $metadata, no webhooks, no SDK, no Postman collection, and no published authentication scheme were found. The GitHub organizations Homesnap and CoStarGroup contain only archived forks of third-party libraries — including libRETS, which is evidence of consuming MLS feeds rather than publishing them. Third-party "Homes.com APIs" on RapidAPI, Apify, Parse, and RealtyAPI are unofficial scrapers and are not recorded here as provider APIs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-26'
name: Homes.com
nav: Providers
network: true
overview: 'Homes.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, United States, Property Listings, MLS, and RESO.


  Homes.com''s developer surface includes support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 25.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/homes-com/refs/heads/main/screenshots/homes-com-2026-08-07T170252.png
security:
- kind: domain-security
  name: Homes Com Domain Security
  slug: homes-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Homes Com Vulnerability Disclosure
  slug: homes-com-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Homes Com Trust Center
  slug: homes-com-trust-center
  summary_line: PCI DSS, ISO/IEC 27001, NIST CSF, SOC 1 Type 2, SOC 1 Type 2
slug: homes-com
tags:
- Real-Estate
- United States
- Property Listings
- MLS
- RESO
- IDX
- Rentals
- PropTech
- Portal
- Marketplaces
- Residential Real Estate
- Real Estate Agents
- Brokers
- Listings Syndication
- CoStar Group
website: https://www.homes.com/
---

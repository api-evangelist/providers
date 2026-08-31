---
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zolo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zolo.ca/
- group: company
  title: ''
  type: Blog
  url: https://www.zolo.ca/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.zolo.ca/blog/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zolo.ca/legal-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zolo.ca/legal-privacy
- group: operate
  title: ''
  type: Support
  url: https://www.zolo.ca/contact_us.php
- group: commercial
  title: ''
  type: Legal
  url: https://www.zolo.ca/legal
- group: company
  title: ''
  type: Careers
  url: https://www.zolo.ca/careers
- group: other
  title: ''
  type: RSS
  url: https://www.zolo.ca/rss_new_listings.php
- group: other
  title: ''
  type: Sitemap
  url: https://www.zolo.ca/site_map_index_https.php
- group: design
  title: ''
  type: Conventions
  url: conventions/zolo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zolo-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/zolo-packages.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zolo-organization.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/zolo-map-listing.schema.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zolo-llms.txt
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/ca/app/zolo-real-estate-apartments/id898656833
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.ols.zolo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zolocanada
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/zolocanada
- group: other
  title: ''
  type: X
  url: https://www.twitter.com/zolocanada
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/zolocanada
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/ZoloCanada
- group: other
  title: ''
  type: Pinterest
  url: https://www.pinterest.com/zolocanada
created: '2026-07-26'
description: 'Zolo is one of Canada''s largest national residential real estate marketplaces and a licensed brokerage, operating as Zolo Ventures Ltd. with provincial brokerage subsidiaries — Zolo Realty (Ontario), (Alberta), (British Columbia), (Saskatchewan), (Manitoba) and (Quebec) Inc. — plus Zolo Mortgages Ltd. and Zolo Mortgages (Alberta) Ltd., all owned by Questrade Financial Group Inc. Founded in 2012 as a digital-first brokerage and headquartered at 1900-5700 Yonge Street in Toronto, Zolo reports over 10 million monthly visitors, 750+ active REALTORS®, and $1.5B+ in annual transaction volume across British Columbia, Alberta, Saskatchewan and Ontario. It sits in the Canadian challenger layer alongside HouseSigma, Wahi and Properly, below CREA — the single national cooperative that operates REALTOR.ca and the Data Distribution Facility (DDF) that syndicates member boards'' listings — competing on listing speed, sold-price visibility and home-value tooling over data the boards and
  CREA control. Its API posture is closed. There is no developer portal, no API program page, no partner or data-licensing page, and no machine-readable API contract of any kind — no OpenAPI, GraphQL, AsyncAPI or MCP surface. The subdomains api., developer., developers., docs., data. and partners.zolo.ca do not resolve in DNS and have never appeared in Certificate Transparency, and every conventional contract path on www.zolo.ca is answered by a Cloudflare bot challenge (HTTP 403, cf-mitigated: challenge) rather than a specification. What Zolo does publish is syndication, not integration: an unauthenticated RSS 2.0 new-listings feed at /rss_new_listings.php, a family of sitemaps.org XML documents, and a site-wide schema.org JSON-LD block carrying organization identity only. Behind the edge it operates an undocumented JSON endpoint at /gallery_map_json.php and two first-party mobile apps (com.ols.zolo) on a private backend. Zolo''s own robots.txt declares that RSS feed as a sitemap and a
  CREA terms-acceptance route at /crea_accept.php, and Section 23 of its Terms of Use is a Virtual Office Website (VOW) clause requiring registration, a bona fide interest in buying or selling, personal non-commercial use only, and an express prohibition on "scraping" (including "screen scraping" and "database scraping"), data mining, redistribution or sublicensing — enforceable directly by CREA, TRREB, ITSO, REBGV, Pillar9 and OREB. Access is licensed, not open. RESO is absent: Zolo is not among the nineteen Canadian organizations RESO lists as members, and no Web API or Data Dictionary certification, OData $metadata document, or Universal Property Identifier (UPI) usage was found. No open, unlicensed dataset is published.'
image: https://www.zolo.ca/img/zolo-logo-graph.png
json_schemas:
- name: Zolo map-gallery listing
  property_count: 0
  slug: zolo-map-listing.schema
jsonld:
- class_count: 0
  name: Zolo Organization Context
  property_count: 0
  slug: zolo-organization
layout: provider
modified: '2026-07-26'
name: Zolo
nav: Providers
network: true
overview: 'Zolo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Canada, Property Listings, MLS, and IDX.


  The Zolo catalog on APIs.io includes 1 JSON-LD context.


  Zolo''s developer surface includes engineering blog, support, legal docs, YouTube channel, and 21 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 12.9
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Zolo Domain Security
  slug: zolo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zolo
tags:
- Real-Estate
- Canada
- Property Listings
- MLS
- IDX
- Valuation
- AVM
- PropTech
- Rentals
- Mortgage
- Conveyancing
website: https://www.zolo.ca/
---

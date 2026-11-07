---
access_model:
  confidence: low
  gated: partner
  gated_source:
  - tag:Partner Gated
  label: Open access
  onboarding: open
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/suncorp-group/hosts/suncorp-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/suncorp-group-hosts.yml
- group: build
  href: https://artifacts.apis.io/suncorp-group/integrations/suncorp-group-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/suncorp-group-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/suncorp-group/vendors/suncorp-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/suncorp-group-vendors.yml
- group: auth
  href: https://artifacts.apis.io/suncorp-group/security/suncorp-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suncorp-group-domain-security.yml
- group: design
  href: https://artifacts.apis.io/suncorp-group/conformance/suncorp-group-conformance.yml
  title: ''
  type: Conformance
  url: conformance/suncorp-group-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.suncorpgroup.com.au/
- group: company
  title: ''
  type: About
  url: https://www.suncorpgroup.com.au/about
- group: other
  title: ''
  type: Brands
  url: https://www.suncorpgroup.com.au/about/brands
- group: company
  title: ''
  type: Blog
  url: https://www.suncorpgroup.com.au/news/news
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.suncorpgroup.com.au/investors
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.vero.com.au/secure/veroedge.html
- group: operate
  title: ''
  type: Support
  url: https://www.suncorpgroup.com.au/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suncorpgroup.com.au/about/corporate-governance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suncorpgroup.com.au/disclaimer
- group: other
  title: ''
  type: Governance
  url: https://www.suncorpgroup.com.au/about/corporate-governance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suncorp/
created: '2026-07-25'
description: 'Suncorp Group Limited (ASX: SUN) is an Australian general insurance group headquartered in Brisbane, Queensland, serving customers across Australia and New Zealand. Following the sale of Suncorp Bank to ANZ on 31 July 2024 it operates as a pure-play insurer, underwriting personal lines (motor, home and contents, caravan, landlord) and commercial lines (SME packages, commercial motor and motor fleet, property/ISR, liability, professional and financial risks, workers'' compensation, surety, and specialty lines including residential strata and equipment breakdown) through a portfolio of brands: in Australia AAMI, Apia, Bingle, CIL, GIO, Essentials by AAI, Shannons, Suncorp, Terri Scheer and Vero, and in New Zealand Vero and AA Insurance. Its API posture is partner-gated and there is no public API. As of a 2026-07-25 review, Suncorp Group publishes no first-party developer portal, no API reference, and no downloadable OpenAPI/Swagger definition on suncorpgroup.com.au or on any
  brand domain: the developer/developers/docs/api subdomains of suncorpgroup.com.au do not resolve, /developers and /api return HTTP 404 on the brand sites, and the corporate sitemap (803 URLs) plus the AAMI, GIO, Suncorp and Vero brand sitemaps (2,007 URLs) contain zero developer, API or integration paths. The only machine-to-machine integration surface is intermediated and behind a login: the VeroEdge / Vero Intermediary Portal for brokers (Access Single ID), a third-party Uniwriter underwriting portal for Engineers PI and Strata, and distribution through Australian broker trading networks — the Steadfast Client Trading Platform (SCTP), Sunrise Exchange, and direct Broker Management System connections. Australia has no live open-insurance obligation: the Consumer Data Right that opened banking and energy was never switched on for general insurance, so unlike Suncorp Bank there is no mandated public product-reference-data endpoint here. No ACORD, AL3 or NGDS reference was found anywhere
  on Suncorp Group or brand properties.'
image: https://www.suncorp.com.au/content/dam/suncorp/corporate/images/logos/Suncorp_New_Logo.png
layout: provider
modified: '2026-10-20'
name: Suncorp Group
nav: Providers
network: true
overview: 'Suncorp Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Property and Casualty, General Insurance, and Carrier.


  Suncorp Group''s developer surface includes engineering blog, support, and 14 more developer resources.'
plans:
- name: Suncorp Group Plans Pricing
  plan_count: 0
  slug: suncorp-group-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Suncorp Group Rate Limits
  slug: suncorp-group-rate-limits
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.3
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 5.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/suncorp-group/suncorp-group-2026-09-02T161129.png
security:
- kind: authentication
  name: Suncorp Group Authentication
  slug: suncorp-group-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Suncorp Group Domain Security
  slug: suncorp-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: suncorp-group
tags:
- Insurance
- Australia
- Property and Casualty
- General Insurance
- Carrier
- Personal Lines
- Commercial Lines
- Claims
- Underwriting
- New Zealand
website: https://www.suncorpgroup.com.au/
---

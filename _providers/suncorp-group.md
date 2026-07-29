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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suncorp-group-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/suncorp-group-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/suncorp-group-llms.txt
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SuncorpGroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suncorp/
created: '2026-07-25'
description: 'Suncorp Group Limited (ASX: SUN) is an Australian general insurance group headquartered in Brisbane, Queensland, serving customers across Australia and New Zealand. Following the sale of Suncorp Bank to ANZ on 31 July 2024 it operates as a pure-play insurer, underwriting personal lines (motor, home and contents, caravan, landlord) and commercial lines (SME packages, commercial motor and motor fleet, property/ISR, liability, professional and financial risks, workers'' compensation, surety, and specialty lines including residential strata and equipment breakdown) through a portfolio of brands: in Australia AAMI, Apia, Bingle, CIL, GIO, Essentials by AAI, Shannons, Suncorp, Terri Scheer and Vero, and in New Zealand Vero and AA Insurance. Its API posture is partner-gated and there is no public API. As of a 2026-07-25 review, Suncorp Group publishes no first-party developer portal, no API reference, and no downloadable OpenAPI/Swagger definition on suncorpgroup.com.au or on any
  brand domain: the developer/developers/docs/api subdomains of suncorpgroup.com.au do not resolve, /developers and /api return HTTP 404 on the brand sites, and the corporate sitemap (803 URLs) plus the AAMI, GIO, Suncorp and Vero brand sitemaps (2,007 URLs) contain zero developer, API or integration paths. The only machine-to-machine integration surface is intermediated and behind a login: the VeroEdge / Vero Intermediary Portal for brokers (Access Single ID), a third-party Uniwriter underwriting portal for Engineers PI and Strata, and distribution through Australian broker trading networks — the Steadfast Client Trading Platform (SCTP), Sunrise Exchange, and direct Broker Management System connections. Australia has no live open-insurance obligation: the Consumer Data Right that opened banking and energy was never switched on for general insurance, so unlike Suncorp Bank there is no mandated public product-reference-data endpoint here. No ACORD, AL3 or NGDS reference was found anywhere
  on Suncorp Group or brand properties.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Suncorp Group
nav: Providers
network: true
overview: 'Suncorp Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Property and Casualty, General Insurance, and Carrier.


  Suncorp Group''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 37
score:
  band: emerging
  composite: 15.7
  delta: -1.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 17.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Suncorp Group Authentication
  slug: suncorp-group-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Suncorp Group Domain Security
  slug: suncorp-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- Broker
- Partner Gated
- New Zealand
website: https://www.suncorpgroup.com.au/
---

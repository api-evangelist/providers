---
access_model:
  confidence: high
  label: Paid · OnTheMarket agent membership and a data-feed agreement required
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - terms-of-use
  - documentation
  - probes
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: OnTheMarket's member-only feed API for estate-agency CRM software. It is modelled on the Rightmove Real Time Datafeed (RTDF/ADF) specification, with OnTheMarket-specific differences in request and res
  name: OnTheMarket Real Time Datafeed (RTDF) API
  slug: onthemarket-real-time-datafeed-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onthemarket-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onthemarket-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onthemarket-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/onthemarket-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onthemarket-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://expert.onthemarket.com/llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.onthemarket.com/
- group: company
  title: ''
  type: About
  url: https://www.onthemarket.com/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onthemarket.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onthemarket.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.onthemarket.com/content/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.onthemarket.com/content/feed/
- group: operate
  title: ''
  type: HelpCenter
  url: https://expert.onthemarket.com/help-centre/
- group: company
  title: ''
  type: Partners
  url: https://expert.onthemarket.com/our-partners/
- group: operate
  title: ''
  type: Support
  url: https://expert.onthemarket.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://expert.onthemarket.com/join-us/
- group: start
  title: ''
  type: Login
  url: https://expert.onthemarket.com/apps/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OnTheMarket
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onthemarket/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.costargroup.com/
created: '2026-07-26'
description: 'OnTheMarket is the third-largest residential property portal in the United Kingdom, operating onthemarket.com. It was founded in 2013 by Agents'' Mutual Limited as an agent-owned challenger to Rightmove and Zoopla, listed on AIM as OnTheMarket plc, and was acquired outright by CoStar Group in December 2023 for approximately GBP 99 million. In a market with no MLS and no cooperative listing standard, OnTheMarket sits at the demand end of the value chain: consumers search the portal, and listings arrive from member estate agents'' CRM systems rather than from a shared data pool. Its API posture is honest and narrow. There is no public developer portal — developer., developers., api. and docs.onthemarket.com do not resolve, and /developers, /api, /docs, /openapi.json, /swagger.json and /api-docs all return 404 on the main site. What does exist is a member-only integration surface: the OnTheMarket Real Time Datafeed (RTDF), a Rightmove-RTDF-compatible feed API served from the live,
  OnTheMarket-operated host realtime-api.onthemarket.com, used by agency CRM vendors to push listings and pull branch enquiries on behalf of member agents. No machine-readable contract for it is published anywhere; OnTheMarket''s developer guide is distributed under agreement, and every path on the host returns 404 to an anonymous caller. There is no RESO Web API or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier anywhere in the stack — RESO is a North American construct and the UK has never adopted it, so "certified but unreachable" does not apply here; there is no certification layer in this market at all. OnTheMarket publishes no open data. The genuinely open UK property layer belongs to the public sector — HM Land Registry Price Paid Data and Ordnance Survey — and none of it comes from the portals. OnTheMarket''s own Terms of Use go further than most and expressly forbid automated access to any page other than the home page.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onthemarket.png
layout: provider
modified: '2026-07-26'
name: OnTheMarket
nav: Providers
network: true
overview: 'OnTheMarket publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United Kingdom, Property Listings, Property Portal, and PropTech.


  OnTheMarket''s developer surface includes engineering blog, support, signup flow, and 17 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.2
  delta: -0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.4
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onthemarket/refs/heads/main/screenshots/onthemarket-2026-08-07T190422.png
security:
- kind: domain-security
  name: Onthemarket Domain Security
  slug: onthemarket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onthemarket
tags:
- Real Estate
- United Kingdom
- Property Listings
- Property Portal
- PropTech
- Rentals
- Estate Agents
- Data Feed
- New Homes
- Commercial Real Estate
website: https://www.onthemarket.com/
---

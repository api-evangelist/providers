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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/direct-line-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.directline.com/
- group: company
  title: ''
  type: Website
  url: https://www.churchill.com/
- group: company
  title: ''
  type: Website
  url: https://www.greenflag.com/
- group: company
  title: ''
  type: Website
  url: https://www.privilege.com/
- group: company
  title: ''
  type: Website
  url: https://www.darwin-insurance.com/
- group: company
  title: ''
  type: Website
  url: https://www.bymiles.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.directlineforbusiness.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.aviva.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Direct-Line-Group
- group: operate
  title: ''
  type: Support
  url: https://www.directline.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.directline.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brandsprivacypolicy.co.uk/policy
- group: company
  title: ''
  type: Blog
  url: https://www.directline.com/magazine
- group: company
  title: ''
  type: Partners
  url: https://www.bymiles.co.uk/partners
- group: design
  title: ''
  type: Conformance
  url: conformance/direct-line-group-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/direct-line-group-llms.txt
created: '2026-07-25'
description: 'Direct Line Group is a United Kingdom personal-lines and small-commercial general insurance carrier, founded in 1985 as the UK''s first telephone-only motor insurer and listed on the London Stock Exchange from its 2012 IPO until Aviva plc completed its GBP 3.7 billion acquisition of the group on 1 July 2025. The group underwrites motor, home, pet, travel, landlord, breakdown and small-business insurance through the Direct Line, Churchill, Privilege, Darwin, By Miles, Direct Line for Business and Green Flag brands, and is regulated in its home market by the Financial Conduct Authority and the Prudential Regulation Authority. Its distribution is direct-to-consumer via telephone and web plus price-comparison-website placement (notably through the Darwin brand), rather than through broker or agency channels; it sold its brokered commercial business (NIG and FarmWeb) to RSA in September 2023, closing the one channel that would have carried standards-based broker integration. Its
  API posture is accordingly closed and partner-gated: as of 25 July 2026 the corporate domain directlinegroup.co.uk returns HTTP 301 to aviva.com, there is no developer.*, developers.* or docs.* host in DNS, every consumer brand site returns 404 on /developers, /api and /partners, and the only API host that exists — api.directlinegroup.co.uk, resolving to a MuleSoft Anypoint production load balancer — serves HTTP 403 behind an expired TLS certificate and requests a client certificate during the TLS handshake. There is no public self-serve developer portal, no downloadable OpenAPI, no GraphQL, no published webhook or event catalog, no public Postman workspace, and no ACORD reference anywhere in the group''s public material. Quote, bind, issue and FNOL are all consumer web and telephone journeys only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Direct Line Group
nav: Providers
network: true
overview: 'Direct Line Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Property and Casualty, Personal Lines, and Motor Insurance.


  Direct Line Group''s developer surface includes support, engineering blog, and 15 more developer resources.'
random_paper: 12
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
screenshot: https://raw.githubusercontent.com/api-evangelist/direct-line-group/refs/heads/main/screenshots/direct-line-group-2026-07-25T212052.png
security:
- kind: domain-security
  name: Direct Line Group Domain Security
  slug: direct-line-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: direct-line-group
tags:
- Insurance
- United Kingdom
- Property and Casualty
- Personal Lines
- Motor Insurance
- Home Insurance
- Carrier
- Roadside Assistance
- Partner Gated
website: https://www.directline.com/
---

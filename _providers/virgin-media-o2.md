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
api_count: 1
apis:
- description: The anonymous read surface of the Virgin Media O2 press newsroom, served by WordPress at news.virginmediao2.co.uk/wp-json/. It is the only callable, self-describing API Virgin Media O2 serves on a hos
  name: Virgin Media O2 Newsroom Content API (WordPress REST)
  slug: newsroom-content-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virgin-media-o2-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virgin-media-o2-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://news.virginmediao2.co.uk/wp-content/uploads/2026/01/Virgin-Media-O2-Security-Schedule-Version-7.0-Jan-2026.pdf
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virgin-media-o2-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.o2.co.uk
- group: operate
  title: ''
  type: StatusPage
  url: https://www.virginmedia.com/help/service-status
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virgin-media-o2-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.virginmediao2.co.uk/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.o2.co.uk/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virginmediao2.co.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virginmediao2.co.uk/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.virginmediao2.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.virginmediao2business.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.o2.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://news.virginmediao2.co.uk/news-views/
- group: company
  title: ''
  type: BlogRSS
  url: https://news.virginmediao2.co.uk/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VirginMediaO2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virgin-media-o2
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: 'Virgin Media O2 is the United Kingdom''s converged fixed and mobile network operator, formed in 2021 as a 50/50 joint venture between Telefonica and Liberty Global by merging Virgin Media''s cable broadband business with O2 UK''s mobile network. It serves roughly half the UK population across mobile, broadband, and fixed wholesale, and sits at the connectivity layer of the telecom value chain rather than the developer-tools layer. Its API posture is partner-gated and sales-led: probing developer.virginmediao2.co.uk, developers.virginmediao2.co.uk, docs.virginmediao2.co.uk, api.virginmediao2.co.uk, opengateway.virginmediao2.co.uk, developer.o2.co.uk and the virginmediao2business.co.uk equivalents returns DNS failure or HTTP 404 in every case, and neither the o2.co.uk sitemap nor the corporate site contains a developer or API section. Virgin Media O2 is a GSMA Open Gateway participant and on 23 September 2025 joined BT/EE, Vodafone and CK Hutchison (Three UK) in the commercial
  UK launch of CAMARA-standardised KYC Age Verification and KYC Tenure APIs, with SIM Swap already live and KYC Match committed; but developers reach that network-API surface only through third-party aggregators such as JT Group and TMT.ID, never through a Virgin Media O2 portal. There is no public self-serve signup, no downloadable OpenAPI, no sandbox, and no first-party SDK. Its GitHub organisation exists and is empty.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: attachment
  property_count: 33
  slug: virgin-media-o2-newsroom-attachment
- name: category
  property_count: 10
  slug: virgin-media-o2-newsroom-category
- name: page
  property_count: 26
  slug: virgin-media-o2-newsroom-page
- name: post
  property_count: 30
  slug: virgin-media-o2-newsroom-post
- name: tag
  property_count: 8
  slug: virgin-media-o2-newsroom-tag
layout: provider
modified: '2026-07-25'
name: Virgin Media O2
nav: Providers
network: true
overview: 'Virgin Media O2 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, United Kingdom, Mobile Network Operator, Broadband, and Network APIs.


  Virgin Media O2''s developer surface includes support, engineering blog, and 17 more developer resources.'
random_paper: 26
score:
  band: emerging
  composite: 24.5
  delta: -2.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 16.1
    developer_ergonomics: 6.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 26.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 33.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Virgin Media O2 Domain Security
  slug: virgin-media-o2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virgin-media-o2
tags:
- Telecommunications
- United Kingdom
- Mobile Network Operator
- Broadband
- Network APIs
- CAMARA
- Open Gateway
- Identity Verification
- SIM Swap
- Age Verification
- Converged Operator
- Partner Gated
website: https://www.virginmediao2.co.uk/
---

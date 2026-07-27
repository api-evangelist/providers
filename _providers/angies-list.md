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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/angies-list-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.angi.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/angies-list-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/angies-list-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/angies-list-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.angi.com
created: '2026-07-17'
description: 'Angie’s List is a consumer marketplace for finding, reviewing, and hiring local home-service professionals — plumbers, electricians, roofers, landscapers, house cleaners, and hundreds of other trades. Founded in 1995 by Angie Hicks and William Oesterle, it pioneered member-submitted, verified reviews and letter-grade ratings of service providers across U.S. metro markets. In 2017 Angie’s List merged with HomeAdvisor to form ANGI Homeservices (now Angi Inc., NASDAQ: ANGI, part of IAC), and in 2021 the consumer brand and website were rebranded from angieslist.com to angi.com. Angi is a consumer/pro home-services platform and does not currently publish a public developer API program; this API Evangelist profile tracks its public web and security surface. Surfaced as a portfolio company of Battery Ventures.'
image: https://www.angi.com/favicon.ico
layout: provider
modified: '2026-07-17'
name: Angie’s List
nav: Providers
network: true
overview: Angie’s List is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Services, Marketplace, Reviews, and Ratings.
random_paper: 32
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Angies List Domain Security
  slug: angies-list-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Angies List Vulnerability Disclosure
  slug: angies-list-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: angies-list
tags:
- Company
- Home Services
- Marketplace
- Reviews
- Ratings
- Local Services
- Consumer
- Contractors
website: https://www.angi.com
---

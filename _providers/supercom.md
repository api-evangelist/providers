---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The partner-facing hotel search API operated by Super.com under its original SnapTravel brand. The host is live and self-identifies ("Welcome to the Partner Search API for SnapTravel"), but the API is
  name: SnapTravel Partner Search API
  slug: snaptravel-partner-search-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supercom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supercom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.super.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snaptravel
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.super.com/help
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/supercom-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supercom-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supercom-llms.txt
- group: auth
  title: ''
  type: Security
  url: security/supercom-vulnerability-disclosure.yml
coverage:
  checked: '2026-08-05'
  detail: api.snaptravel.com answers 200 with the plain-text line "Welcome to the Partner Search API for SnapTravel" but every documentation path on it 404s, no developer/docs/partner subdomain resolves for super.com, and the hotel search API is only obtainable through a business partnership — so there is no public reference or machine-readable spec to harvest.
  evidence:
  - status: 200
    url: https://api.snaptravel.com/
  - status: 404
    url: https://api.snaptravel.com/openapi.json
  - status: 404
    url: https://api.snaptravel.com/api-docs
  - status: 403
    url: https://www.super.com/
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: 'Super.com (formerly SnapTravel and Snapcommerce) is a consumer savings company founded in 2016 by Hussein Fazal and Henry Shi, headquartered in San Francisco with engineering roots in Toronto. Its app bundles SuperTravel hotel booking, flights, SuperShop savings, SuperCash cash back and credit building, SuperPay, and SuperRx prescription discounts, and the company reports more than $2 billion in sales processed since launch on roughly $150 million raised across seed through Series C. Its only developer-facing surface is the SnapTravel Partner Search API at api.snaptravel.com — a hotel search-and-book integration offered to business partners. No public API reference, developer portal, or machine-readable specification is published: every documentation path on the API host returns 404, no developer/docs subdomain resolves, and the www.super.com HTML surface is served behind a Cloudflare bot challenge. The company does publish an RFC 9116 security.txt naming a security contact
  and an invite-only Bugcrowd program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supercom.png
layout: provider
modified: '2026-08-05'
name: Super.com
nav: Providers
network: true
overview: Super.com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hotels, Booking, and Flights.
random_paper: 133
score:
  band: minimal
  composite: 10.3
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 10.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Supercom Domain Security
  slug: supercom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Supercom Vulnerability Disclosure
  slug: supercom-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: supercom
tags:
- Company
- Travel
- Hotels
- Booking
- Flights
- Consumer Finance
- Cash Back
- Savings
- Prescription Discounts
- Mobile Applications
website: https://www.super.com/
---

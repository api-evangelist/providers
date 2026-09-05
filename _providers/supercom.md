---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-04'
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
random_paper: 17
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 9.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supercom/refs/heads/main/screenshots/supercom-2026-09-02T161225.png
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
- Cashback
- Savings
- Prescription Discounts
- Mobile Applications
website: https://www.super.com/
---

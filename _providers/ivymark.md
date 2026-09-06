---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://ivymark.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.ivy.co/ — a different registrable domain (ivymark.com -> ivy.co), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ivymark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ivymark.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ivy.co/designers/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.ivy.co/builders/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ivy.co/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ivy.co/privacy-policy
created: '2026-07-17'
description: ivymark was surfaced as a portfolio-company lead of Slow Ventures and added to the API Evangelist network as a stub. Enrichment found that the repo domain ivymark.com 301-redirects in full to www.ivy.co — Ivy, a business-management platform for interior designers (product sourcing, proposals, invoices, client mood boards, project and time tracking, online payments, and reporting), now operated as part of Houzz Pro. No public API, developer portal, OpenAPI, or well-known discovery surface was found on either ivymark.com or ivy.co, so no API artifacts could be produced this round; only the identity, verified marketing links, and a live domain-security probe are recorded.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ivymark.png
layout: provider
modified: '2026-07-19'
name: ivymark
nav: Providers
network: true
overview: 'ivymark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Interior Design, Business Management, Design Software, and Product Sourcing.


  ivymark''s developer surface includes pricing, engineering blog, and 4 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ivymark/refs/heads/main/screenshots/ivymark-2026-07-25T223020.png
security:
- kind: domain-security
  name: Ivymark Domain Security
  slug: ivymark-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ivymark
tags:
- Company
- Interior Design
- Business Management
- Design Software
- Product Sourcing
- Invoicing
- Payments
- Software-as-a-Service
website: https://ivymark.com
---

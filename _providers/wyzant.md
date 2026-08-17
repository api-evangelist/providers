---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Wyzant Agentic Access
  operation_count: 2
  slug: wyzant-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: Bulk snapshot download of all active tutors.
  name: Wyzant Data Feed API
  slug: wyzant-data-feed-api
- description: Real-time search against the live tutor database.
  name: Wyzant Search API
  slug: wyzant-search-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wyzant Partner Data Data Feed API
  slug: open-wyzant-data-feed-api
- collection_type: open
  name: Wyzant Partner Data Data Feed Search API
  slug: open-wyzant-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wyzant-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wyzant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wyzant-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wyzant
- group: company
  title: ''
  type: Website
  url: https://www.wyzant.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.wyzant.com/hc/en-us/articles/115005857526-API-Data-Feed-Documentation
- group: company
  title: ''
  type: PartnerProgram
  url: https://highered.wyzant.com/partner
- group: commercial
  title: ''
  type: Plans
  url: plans/wyzant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wyzant-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wyzant-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.wyzant.com/feed
created: '2026-07-03'
description: Wyzant is a US tutoring marketplace that connects students with independent tutors for in-person and online lessons across thousands of subjects. It is a consumer product, not a developer platform - students book and pay for lessons through wyzant.com and pay a service fee on top of each tutor's hourly rate, and there is no public REST API for managing lessons, bookings, messages, or payments. Wyzant does, however, expose a real partner/affiliate data API and data feed at data.wyzant.com for approved affiliates (via the ShareASale-based partner program). These let a partner run real-time keyword/location searches against the live tutor database and download a full snapshot of all active tutors in XML or JSON, keyed by a per-partner API key, so partners can surface Wyzant tutors on their own sites and earn a per-lead bounty. Access requires a partner account; the API is not open to the general public.
finops:
- name: Wyzant Finops
  service_category: Education and Tutoring Marketplace
  slug: wyzant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wyzant.png
layout: provider
modified: '2026-07-03'
name: Wyzant
nav: Providers
network: true
overview: 'Wyzant publishes 2 APIs on the [APIs.io](https://apis.io/) network: Data Feed API and Search API. Tagged areas include Tutoring, Education, Marketplace, Tutors, and EdTech.


  Wyzant''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Wyzant Plans Pricing
  plan_count: 2
  slug: wyzant-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 3
  name: Wyzant Rate Limits
  slug: wyzant-rate-limits
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Wyzant Domain Security
  slug: wyzant-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Wyzant Vulnerability Disclosure
  slug: wyzant-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wyzant
tags:
- Tutoring
- Education
- Marketplace
- Tutors
- EdTech
- Affiliate
- Partner API
- Data Feed
website: https://www.wyzant.com
---

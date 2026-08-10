---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tributetech Agentic Access
  operation_count: 8
  slug: tributetech-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 3
apis:
- description: Exchange a funeral-home credential triple for a bearer token.
  name: Tribute Technology Authentication API
  slug: tributetech-authentication-api
- description: Obituary cases pushed to the Tribute Store, and their retrieval.
  name: Tribute Technology Obituaries API
  slug: tributetech-obituaries-api
- description: Funeral-home rooftops (serving locations) that obituaries attach to.
  name: Tribute Technology Serving Locations API
  slug: tributetech-serving-locations-api
artifact_total: 10
collections:
- collection_type: open
  name: Tribute Store API
  slug: open-tributetech
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tributetech-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tributetech-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tributetech-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tributetechnology
- group: company
  title: ''
  type: Website
  url: https://www.tributetech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://awheeler.funeraltechweb2.com/additional-service-info/file/3/Tribute%20Store%20API%20Documentation%201.1.pdf
- group: commercial
  title: ''
  type: Plans
  url: plans/tributetech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tributetech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tributetech-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tributetech.com/blog
created: '2026-07-03'
description: Tribute Technology is a funeral-home technology company serving over 9,000 funeral homes across the US and Canada with obituary publishing, memorial websites, funeral-home management software, online payments (Tribute Pay), and e-commerce (flowers and personalized products) through the Tribute Store. For partners, Tribute Technology exposes the Tribute Store API - a partner-gated, REST-style JSON API that lets funeral-home case-management systems authenticate a funeral home, push its serving locations (rooftops), and push obituary cases that automatically provision a personalized Tribute Store page for each deceased. Access requires a Provider credential, an IP allowlist, and a per-funeral-home HostName/UserName/Password triple exchanged for a bearer token; there is no public self-service developer portal.
finops:
- name: Tributetech Finops
  service_category: Software and E-commerce
  slug: tributetech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tributetech.png
layout: provider
modified: '2026-07-03'
name: Tribute Technology
nav: Providers
network: true
overview: 'Tribute Technology publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Obituaries API, and Serving Locations API. Tagged areas include Funeral Technology, Obituaries, Memorials, Funeral Homes, and E-commerce.


  Tribute Technology''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Tributetech Plans Pricing
  plan_count: 3
  slug: tributetech-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 4
  name: Tributetech Rate Limits
  slug: tributetech-rate-limits
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Tributetech Authentication
  slug: tributetech-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tributetech Domain Security
  slug: tributetech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tributetech
tags:
- Funeral Technology
- Obituaries
- Memorials
- Funeral Homes
- E-commerce
- Death Care
- Case Management
website: https://www.tributetech.com/
---

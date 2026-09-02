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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tributetech Agentic Access
  operation_count: 8
  slug: tributetech-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
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
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tribute Store Authentication API
  slug: open-tributetech-authentication-api
- collection_type: open
  name: Tribute Store Authentication Obituaries API
  slug: open-tributetech-obituaries-api
- collection_type: open
  name: Tribute Store Authentication Serving Locations API
  slug: open-tributetech-serving-locations-api
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
overview: 'Tribute Technology publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Obituaries API, and Serving Locations API. Tagged areas include Funeral Technology, Obituaries, Memorials, Funeral Homes, and E-Commerce.


  Tribute Technology''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Tributetech Plans Pricing
  plan_count: 3
  slug: tributetech-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Tributetech Rate Limits
  slug: tributetech-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 13.9
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- E-Commerce
- Death Care
- Case Management
website: https://www.tributetech.com/
---

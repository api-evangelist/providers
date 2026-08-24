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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Funeralone Agentic Access
  operation_count: 3
  slug: funeralone-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Create, update, and retrieve funeral cases (obituaries) for an account.
  name: funeralOne Cases API
  slug: funeralone-cases-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: funeralOne Cases API
  slug: open-funeralone-cases-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/funeralone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/funeralone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/funeralone-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.funeralone.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/funeralone
- group: docs
  title: ''
  type: Documentation
  url: https://api.funeralone.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://support.funeralone.com
- group: commercial
  title: ''
  type: Plans
  url: plans/funeralone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/funeralone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/funeralone-finops.yml
created: '2026-07-03'
description: funeralOne is a funeral-home technology company whose f1Connect platform delivers funeral-home websites, memorial/tribute pages, Life Tributes tribute videos, memorial webcasting, and e-commerce for independent funeral homes. funeralOne publishes a partner integration API (base https://api.funeralone.com) that lets funeral-management / case-management systems push deceased, obituary, service-event, tribute-video, and family-administration data into a funeral home's f1Connect account so an At-Need case automatically populates the memorial website and Life Tributes. The API is partner-gated - access requires an API key issued by a funeralOne engineer and per-customer AccountExternalId associations - and uses HTTP Basic authentication. Only the Cases resource is publicly documented; the broader website, e-commerce, and webcasting products are delivered through the f1Connect platform rather than a public API.
finops:
- name: Funeralone Finops
  service_category: Web and Application Hosting
  slug: funeralone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/funeralone.png
layout: provider
modified: '2026-07-03'
name: funeralOne
nav: Providers
network: true
overview: 'funeralOne publishes 1 API on the [APIs.io](https://apis.io/) network: Cases API. Tagged areas include Funeral Homes, Death Care, Obituaries, Tribute Videos, and Memorial Websites.


  funeralOne''s developer surface includes authentication, documentation, support, and 7 more developer resources.'
plans:
- name: Funeralone Plans Pricing
  plan_count: 3
  slug: funeralone-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Funeralone Rate Limits
  slug: funeralone-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.4
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/funeralone/refs/heads/main/screenshots/funeralone-2026-07-25T215318.png
security:
- kind: authentication
  name: Funeralone Authentication
  slug: funeralone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Funeralone Domain Security
  slug: funeralone-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: funeralone
tags:
- Funeral Homes
- Death Care
- Obituaries
- Tribute Videos
- Memorial Websites
- Life Tributes
- Case Management
- Partner API
website: https://www.funeralone.com
---

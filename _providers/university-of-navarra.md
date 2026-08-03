---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: DADUN (Deposito Academico Digital de la Universidad de Navarra) is the university's open-access institutional repository, built on DSpace (reported version 5.3). It exposes a standard OAI-PMH 2.0 inte
  name: DADUN Institutional Repository (OAI-PMH)
  slug: dadun-oai-pmh
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-navarra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.unav.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-de-navarra-cp
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-navarra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-navarra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-navarra-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Navarra (Universidad de Navarra) is a private research university founded in 1952, headquartered in Pamplona, Spain, with additional campuses in San Sebastian and Madrid. It is ranked #249 in the QS World University Rankings 2025. Its public, machine-consumable developer footprint is limited: the principal documented interface is DADUN (Deposito Academico Digital de la Universidad de Navarra), the institutional open-access repository running on DSpace, which exposes metadata harvesting through the OAI-PMH protocol. No general-purpose public developer portal, open-data API platform, or official GitHub organization could be independently confirmed for the institution at the time of review.'
finops:
- name: University Of Navarra Finops
  service_category: Education
  slug: university-of-navarra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-navarra.png
jsonld:
- class_count: 25
  name: University Of Navarra Context
  property_count: 2
  slug: university-of-navarra-context
layout: provider
modified: '2026-06-03'
name: University of Navarra
nav: Providers
network: true
overview: 'University of Navarra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Spain, and Open Access.


  The University of Navarra catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: University Of Navarra Plans Pricing
  plan_count: 2
  slug: university-of-navarra-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 1
  name: University Of Navarra Rate Limits
  slug: university-of-navarra-rate-limits
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-navarra/refs/heads/main/screenshots/university-of-navarra-2026-06-20T200213.png
security:
- kind: domain-security
  name: University Of Navarra Domain Security
  slug: university-of-navarra-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-navarra
tags:
- Education
- Higher Education
- University
- Spain
- Open Access
- Institutional Repository
- OAI-PMH
website: https://en.unav.edu/
---

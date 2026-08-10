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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: University of Melbourne open spatial-data portal hosted on ArcGIS Hub for exploring and downloading campus GIS layers including building, road and tree-canopy footprints. Datasets are served through t
  name: Open Spatial Data Portal (ArcGIS Hub)
  slug: spatial-open-data
- description: The University of Melbourne operates a Boomi-based API management developer portal providing self-service access to internal data APIs for staff and students. This portal is gated behind university au
  name: Internal API Management Developer Portal (Boomi) — Gated
  slug: boomi-developer-portal
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-melbourne-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-melbourne-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unimelb.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/unimelb
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-melbourne/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.unimelb.edu.au/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-melbourne-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-melbourne-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-melbourne-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://minerva-access.unimelb.edu.au/
created: '2026-06-03'
description: 'The University of Melbourne is Australia''s leading research university, ranked #24 in the QS World University Rankings 2025. Its public developer and API footprint is modest and federated rather than centralized: the Library operates the Minerva Access institutional repository on DSpace 7.6, which exposes a public OAI-PMH metadata interface and a DSpace REST API, and the institution publishes campus GIS data through an ArcGIS Hub open spatial-data portal with the standard ArcGIS/Hub query APIs. Internally the university runs a Boomi-based API management developer portal for staff and students, but that portal is gated and not publicly documented. Identity is managed via central SSO (Okta) with OAuth 2.0 / OpenID Connect, but no public API program is offered there. An official GitHub organization (github.com/unimelb) exists with mostly archived projects.'
finops:
- name: University Of Melbourne Finops
  service_category: Education
  slug: university-of-melbourne-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-melbourne.png
jsonld:
- class_count: 29
  name: University Of Melbourne Context
  property_count: 3
  slug: university-of-melbourne-context
layout: provider
modified: '2026-07-25'
name: University of Melbourne
nav: Providers
network: true
overview: 'University of Melbourne publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Australia, and Open Data.


  The University of Melbourne catalog on APIs.io includes 1 JSON-LD context.


  University of Melbourne''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: University Of Melbourne Plans Pricing
  plan_count: 2
  slug: university-of-melbourne-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: University Of Melbourne Rate Limits
  slug: university-of-melbourne-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-melbourne/refs/heads/main/screenshots/university-of-melbourne-2026-06-20T200206.png
security:
- kind: domain-security
  name: University Of Melbourne Domain Security
  slug: university-of-melbourne-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Melbourne Vulnerability Disclosure
  slug: university-of-melbourne-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-melbourne
tags:
- Education
- Higher Education
- University
- Australia
- Open Data
- Research
- Library
- Repository
website: https://www.unimelb.edu.au/
---

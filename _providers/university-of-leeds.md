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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'The institutional research data repository for the University of Leeds, powered by EPrints 3. It exposes a live OAI-PMH 2.0 endpoint for harvesting Dublin Core and related metadata records describing '
  name: Research Data Leeds Repository (OAI-PMH)
  slug: research-data-oai
- description: The University of Leeds Libraries' Cultural Collections are IIIF-enabled through a digital library infrastructure built in partnership with Digirati (IIIF Image API at the access end, OCFL at the pres
  name: Cultural Collections IIIF
  slug: iiif-cultural-collections
- description: University of Leeds Libraries discovery and resource management run on the Ex Libris Alma library services platform with the Primo discovery layer (migrated from Innovative Sierra). Programmatic acces
  name: Library Search (Ex Libris Alma / Primo)
  slug: library-discovery
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-leeds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.leeds.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uol-library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-leeds/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-leeds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-leeds-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-leeds-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Leeds is a public research university in Leeds, United Kingdom, ranked #60 in the QS World University Rankings 2025. With more than 34,000 students and over 7,000 staff, it is a member of the Russell Group of research-intensive universities. Its public developer/API footprint is modest and centered on the Libraries: a live EPrints-based Research Data Leeds Repository exposing an OAI-PMH 2.0 endpoint, IIIF-enabled Cultural Collections delivered via a Digirati-built digital library infrastructure, and an active GitHub organisation (uol-library). Library discovery runs on Ex Libris Alma/Primo, whose APIs are vendor-provided rather than institution-documented. No central, self-service developer portal was found.'
finops:
- name: University Of Leeds Finops
  service_category: Education
  slug: university-of-leeds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-leeds.png
jsonld:
- class_count: 23
  name: University Of Leeds Context
  property_count: 2
  slug: university-of-leeds-context
layout: provider
modified: '2026-06-03'
name: University of Leeds
nav: Providers
network: true
overview: 'University of Leeds publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, United Kingdom, and Research Data.


  The University of Leeds catalog on APIs.io includes 1 JSON-LD context.


  University of Leeds'' developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: University Of Leeds Plans Pricing
  plan_count: 2
  slug: university-of-leeds-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 1
  name: University Of Leeds Rate Limits
  slug: university-of-leeds-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: University Of Leeds Domain Security
  slug: university-of-leeds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-leeds
tags:
- Education
- Higher Education
- University
- United Kingdom
- Research Data
- Libraries
- OAI-PMH
- IIIF
website: https://www.leeds.ac.uk/
---

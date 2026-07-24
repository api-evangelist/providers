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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH 2.0) interface for the Institutional Repository University of Antwerp (IRUA), exposing scholarly publication metadata for harvesting.
  name: IRUA OAI-PMH Metadata API
  slug: irua-oai-pmh
- description: Brocade is the integrated, web-based library management system developed by Anet, the software department of the University of Antwerp Library, since 1998. It powers the catalog of the Anet network of
  name: Brocade Library Services (Anet)
  slug: brocade
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-antwerp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uantwerpen.be/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/anet-be
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-antwerp/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/uantwerpen
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/anet-be
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-antwerp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-antwerp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-antwerp-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Antwerp (Universiteit Antwerpen) is a public research university in Antwerp, Belgium, ranked #267 in the QS World University Rankings 2025. Its public developer and API footprint is centered on its library and scholarly infrastructure: the university library''s software department, Anet, builds the open-source Brocade library management system and publishes code via the anet-be GitHub organization. The Institutional Repository University of Antwerp (IRUA) exposes scholarly metadata through a standards-based OAI-PMH interface. The university does not operate a general-purpose commercial developer portal; administrative, student-information, and identity systems are gated behind institutional affiliation rather than offered as public self-service APIs.'
finops:
- name: University Of Antwerp Finops
  service_category: Education
  slug: university-of-antwerp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-antwerp.png
jsonld:
- class_count: 21
  name: University Of Antwerp Context
  property_count: 10
  slug: university-of-antwerp-context
layout: provider
modified: '2026-06-03'
name: University of Antwerp
nav: Providers
network: true
overview: 'University of Antwerp publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Library, and Institutional Repository.


  The University of Antwerp catalog on APIs.io includes 1 JSON-LD context.


  University of Antwerp''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: University Of Antwerp Plans Pricing
  plan_count: 2
  slug: university-of-antwerp-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: University Of Antwerp Rate Limits
  slug: university-of-antwerp-rate-limits
score:
  band: emerging
  composite: 22.6
  delta: 0.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 20.8
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.4
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-antwerp/refs/heads/main/screenshots/university-of-antwerp-2026-06-20T200126.png
security:
- kind: domain-security
  name: University Of Antwerp Domain Security
  slug: university-of-antwerp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-antwerp
tags:
- Education
- Higher Education
- University
- Library
- Institutional Repository
- OAI-PMH
- Open Data
- Belgium
- Europe
website: https://www.uantwerpen.be/en/
---

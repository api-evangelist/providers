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
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: CKAN action API for the "UPF en Xifres 2.0" (Open Data UPF) portal, providing programmatic access to institutional open datasets such as degree programs, campuses, and study plans. The portal is built
  name: UPF Open Data CKAN API
  slug: open-data-ckan
- description: Virtuoso-backed SPARQL endpoint for querying the linked open data published by the UPF Open Data portal as part of the linked open data movement across universities.
  name: UPF Open Data SPARQL Endpoint
  slug: sparql
- description: Public DSpace 7.6 REST (HAL) API for the e-Repositori, the UPF institutional repository collecting the university's research and academic output. Exposes communities, collections, and items; write ope
  name: UPF Digital Repository REST API (DSpace 7)
  slug: repository-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the e-Repositori (Repositori digital de la UPF), enabling harvesting of repository metadata records. Indexed by BASE, CORE, OpenDOAR, Re3data, and OpenAIRE
  name: UPF Digital Repository OAI-PMH
  slug: repository-oai
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universitat-pompeu-fabra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upf.edu/en/home
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.upf.edu/about
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mtg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitat-pompeu-fabra/
- group: auth
  title: ''
  type: Authentication
  url: https://repositori.upf.edu/shibboleth-login
- group: commercial
  title: ''
  type: Plans
  url: plans/universitat-pompeu-fabra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/universitat-pompeu-fabra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/universitat-pompeu-fabra-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universitat Pompeu Fabra (UPF) is a public research university in Barcelona, Spain, ranked #266 in the QS World University Rankings 2025. Its public developer footprint centers on the "UPF en Xifres 2.0" linked open data portal (data.upf.edu), which exposes institutional datasets via a CKAN action API and a Virtuoso SPARQL endpoint, and on the UPF Digital Repository (e-Repositori), built on DSpace 7.6 with a public REST API and an OAI-PMH harvesting endpoint. Identity is handled through an adAS / Shibboleth SAML single sign-on service. Most other software is published by research groups (e.g. the Music Technology Group) on GitHub rather than as institutional APIs.'
finops:
- name: Universitat Pompeu Fabra Finops
  service_category: Education
  slug: universitat-pompeu-fabra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universitat-pompeu-fabra.png
jsonld:
- class_count: 24
  name: Universitat Pompeu Fabra Context
  property_count: 3
  slug: universitat-pompeu-fabra-context
layout: provider
modified: '2026-06-03'
name: Universitat Pompeu Fabra
nav: Providers
network: true
overview: 'Universitat Pompeu Fabra publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Research.


  The Universitat Pompeu Fabra catalog on APIs.io includes 1 JSON-LD context.


  Universitat Pompeu Fabra''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Universitat Pompeu Fabra Plans Pricing
  plan_count: 2
  slug: universitat-pompeu-fabra-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Universitat Pompeu Fabra Rate Limits
  slug: universitat-pompeu-fabra-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/universitat-pompeu-fabra/refs/heads/main/screenshots/universitat-pompeu-fabra-2026-06-20T200116.png
security:
- kind: domain-security
  name: Universitat Pompeu Fabra Domain Security
  slug: universitat-pompeu-fabra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: universitat-pompeu-fabra
tags:
- Education
- Higher Education
- University
- Open Data
- Research
- Library
- Repository
- SPARQL
- OAI-PMH
- Spain
- Barcelona
website: https://www.upf.edu/en/home
---

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
api_count: 5
apis:
- description: The Academic Bibliography (Biblio) provides programmatic access to UGent research publication metadata via a REST search API (JSON/JSONP), an OAI-PMH 2.0 harvesting endpoint, an SRU 1.1 search service
  name: Ghent University Academic Bibliography API
  slug: biblio
- description: OAI-PMH 2.0 metadata harvesting endpoint for the UGent Academic Bibliography, supporting Identify, ListMetadataFormats and ListRecords verbs for full or selective harvesting of publication records.
  name: Ghent University Academic Bibliography OAI-PMH
  slug: biblio-oai
- description: SRU 1.1 search/retrieve service for the UGent Academic Bibliography using Contextual Query Language (CQL), returning XML records for publication searches with sorting support.
  name: Ghent University Academic Bibliography SRU
  slug: biblio-sru
- description: The Ghent University Library catalog (lib.ugent.be) exposes machine interfaces for its collections, including OAI-PMH metadata harvesting, SRU search with CQL, IIIF (Presentation API v2) for digitized
  name: Ghent University Library Catalog Interfaces
  slug: library-catalog
- description: Open JSON API published by Zeus WPI, the computer-science student working group at Ghent University, powering the Hydra student app. The Resto API (v2.0) serves UGent student-restaurant locations, dai
  name: Hydra Resto API (Zeus WPI)
  slug: hydra-resto
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ghent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ugent.be/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ugent
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ugent-library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ghent-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/ghent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ghent-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ghent-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Ghent University (Universiteit Gent, UGent) is a major public research university in Ghent, Belgium, ranked #169 in the QS World University Rankings 2025. Its public developer footprint centers on the Ghent University Library: the Academic Bibliography (biblio.ugent.be) exposes a documented REST search API plus OAI-PMH, SRU, unAPI and bulk data dumps under an ODbL license, and the library catalog (lib.ugent.be) offers OAI-PMH, SRU, IIIF and OpenSearch interfaces. The university maintains official GitHub organizations (ugent, ugent-library), and the student computer-science group Zeus WPI publishes the open Hydra Resto API for student-restaurant menu data. There is no single centralized, gateway-style institutional developer portal; APIs are documented per service.'
finops:
- name: Ghent Finops
  service_category: Education
  slug: ghent-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ghent.png
jsonld:
- class_count: 19
  name: Ghent Context
  property_count: 3
  slug: ghent-context
layout: provider
modified: '2026-06-03'
name: Ghent University
nav: Providers
network: true
overview: 'Ghent University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Ghent University catalog on APIs.io includes 1 JSON-LD context.


  Ghent University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Ghent Plans Pricing
  plan_count: 2
  slug: ghent-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 1
  name: Ghent Rate Limits
  slug: ghent-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ghent/refs/heads/main/screenshots/ghent-2026-06-20T181815.png
security:
- kind: domain-security
  name: Ghent Domain Security
  slug: ghent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ghent
tags:
- Education
- Higher Education
- University
- Research
- Library
- Open Data
- Belgium
- Europe
website: https://www.ugent.be/en
---

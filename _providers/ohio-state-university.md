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
api_count: 3
apis:
- description: Public REST API for the Knowledge Bank, Ohio State University Libraries' DSpace 7.6 institutional repository. Exposes communities, collections, items, and bitstreams as JSON (HAL) for the digital scho
  name: Knowledge Bank DSpace REST API
  slug: kb-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the Knowledge Bank institutional repository. Supports the standard OAI verbs (Identify, ListRecords, ListSets, etc.) for harvesting Dublin Core and other m
  name: Knowledge Bank OAI-PMH Interface
  slug: kb-oai
- description: Institution-wide web authentication and authorization service operated by the Office of Technology and Digital Innovation, built on Shibboleth and currently supporting the SAML 2.0 standard with InCom
  name: Web Single Sign-On (Shibboleth)
  slug: websso
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ohio-state-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.osu.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/osulibraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-ohio-state-university/
- group: auth
  title: ''
  type: Authentication
  url: https://cybersecurity.osu.edu/services/web-single-sign
- group: commercial
  title: ''
  type: Plans
  url: plans/ohio-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ohio-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ohio-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Ohio State University is a large public land-grant research university in Columbus, Ohio, United States, ranked #208 in the QS World University Rankings 2025. It does not operate a single centralized public developer portal; instead its public, programmatically accessible footprint is fragmented across units. The most clearly documented public APIs come from University Libraries'' Knowledge Bank institutional repository, which exposes a DSpace 7.6 REST API and an OAI-PMH metadata harvesting interface. Institution-wide web authentication is provided through a Shibboleth SAML 2.0 Single Sign-On service, with most enterprise data and the data.world-backed Data Catalog gated to Ohio State affiliates.'
finops:
- name: Ohio State University Finops
  service_category: Education
  slug: ohio-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ohio-state-university.png
jsonld:
- class_count: 16
  name: Ohio State University Context
  property_count: 8
  slug: ohio-state-university-context
layout: provider
modified: '2026-06-03'
name: Ohio State University
nav: Providers
network: true
overview: 'Ohio State University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Ohio State University catalog on APIs.io includes 1 JSON-LD context.


  Ohio State University''s developer surface includes GitHub presence, authentication, and 7 more developer resources.'
plans:
- name: Ohio State University Plans Pricing
  plan_count: 2
  slug: ohio-state-university-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 1
  name: Ohio State University Rate Limits
  slug: ohio-state-university-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ohio-state-university/refs/heads/main/screenshots/ohio-state-university-2026-06-20T190643.png
security:
- kind: domain-security
  name: Ohio State University Domain Security
  slug: ohio-state-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ohio-state-university
tags:
- Education
- Higher Education
- University
- Research
- Library
- Institutional Repository
- Open Access
- United States
website: https://www.osu.edu/
---

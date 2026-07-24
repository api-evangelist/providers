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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Public RESTful (HAL) API for the AUB ScholarWorks institutional repository, running on DSpace 9.1. Exposes communities, collections, items, bitstreams, discovery/search, and metadata over HTTP/JSON. T
  name: AUB ScholarWorks DSpace REST API
  slug: scholarworks-rest
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for the AUB ScholarWorks institutional repository (DSpace 9.1). Supports the standard OAI verbs (Identify, ListRecords, ListSets, GetRecord, etc.) and exposes '
  name: AUB ScholarWorks OAI-PMH
  slug: scholarworks-oai
- description: AUB's institutional single sign-on is provided by a Shibboleth SAML 2.0 identity provider. The SAML metadata is published at the entity endpoint and is used to federate access to AUB web services. Thi
  name: AUB Shibboleth Identity Provider (SAML 2.0)
  slug: shibboleth-idp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aub.edu.lb/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/AUB-CMPS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/american-university-of-beirut
- group: auth
  title: ''
  type: Authentication
  url: https://idp.aub.edu.lb/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/aub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aub-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The American University of Beirut (AUB) is a private research university in Beirut, Lebanon, founded in 1866, and ranked #250 in the QS World University Rankings 2025. AUB''s public, machine-readable developer footprint is centered on its University Libraries: the AUB ScholarWorks institutional repository runs on DSpace 9.1, which exposes a public RESTful API and an OAI-PMH 2.0 metadata harvesting endpoint. Authentication across AUB web services is provided by a Shibboleth SAML 2.0 identity provider. AUB does not publish a centralized developer portal; most other institutional systems (SIS, service desk) are gated behind SSO and are not publicly documented APIs.'
finops:
- name: Aub Finops
  service_category: Education
  slug: aub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aub.png
jsonld:
- class_count: 11
  name: Aub Context
  property_count: 5
  slug: aub-context
layout: provider
modified: '2026-06-03'
name: American University of Beirut
nav: Providers
network: true
overview: 'American University of Beirut publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Lebanon, and Middle East.


  The American University of Beirut catalog on APIs.io includes 1 JSON-LD context.


  American University of Beirut''s developer surface includes GitHub presence, authentication, and 7 more developer resources.'
plans:
- name: Aub Plans Pricing
  plan_count: 2
  slug: aub-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Aub Rate Limits
  slug: aub-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aub/refs/heads/main/screenshots/aub-2026-06-20T172544.png
security:
- kind: domain-security
  name: Aub Domain Security
  slug: aub-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: aub
tags:
- Education
- Higher Education
- University
- Lebanon
- Middle East
- Research
- Libraries
- Open Access
website: https://www.aub.edu.lb/
---

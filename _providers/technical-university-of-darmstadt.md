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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: REST API of TUdatalib, the institutional research-data repository of TU Darmstadt, running on DSpace 8.1. The API root reports dspaceName "TUdatalib System" and exposes HAL-style endpoints for communi
  name: TUdatalib DSpace REST API
  slug: tudatalib-rest
- description: 'OAI-PMH 2.0 metadata harvesting interface for TUdatalib (DSpace 8.1). Verified live: Identify returns repositoryName "TUdatalib System", protocolVersion 2.0, adminEmail tudatalib@ulb.tu-darmstadt.de.'
  name: TUdatalib OAI-PMH
  slug: tudatalib-oai
- description: TUbiblio is the publication bibliography of TU Darmstadt, built on EPrints and registered with an OAI-PMH 2.0 interface for metadata harvesting. The OAI base path is /cgi/oai2. The public site loads i
  name: TUbiblio OAI-PMH (EPrints)
  slug: tubiblio-oai
- description: tuprints is the open-access publication repository of TU Darmstadt, built on EPrints with an OAI-PMH 2.0 interface (base path /cgi/oai2). The repository site returns HTTP 200; the OAI endpoint returne
  name: tuprints OAI-PMH (EPrints)
  slug: tuprints-oai
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/technical-university-of-darmstadt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tu-darmstadt.de/index.en.jsp
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TU-Darmstadt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tu-darmstadt/
- group: auth
  title: ''
  type: Authentication
  url: https://www.hrz.tu-darmstadt.de/sso
- group: commercial
  title: ''
  type: Plans
  url: plans/technical-university-of-darmstadt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/technical-university-of-darmstadt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/technical-university-of-darmstadt-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/technical-university-of-darmstadt-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The Technical University of Darmstadt (Technische Universitat Darmstadt, TU Darmstadt) is a public research university in Darmstadt, Germany, ranked #241 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on the university and state library (ULB) scholarly infrastructure rather than a central developer portal. TUdatalib, the institutional research-data repository, runs DSpace 8.1 and exposes a live REST API and an OAI-PMH 2.0 metadata interface; the TUbiblio publication bibliography and the tuprints open-access repository run on EPrints with OAI-PMH harvesting. Authentication across university services is handled through a central SSO system operated by the Hochschulrechenzentrum (HRZ).'
finops:
- name: Technical University Of Darmstadt Finops
  service_category: Education
  slug: technical-university-of-darmstadt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/technical-university-of-darmstadt.png
jsonld:
- class_count: 19
  name: Technical University Of Darmstadt Context
  property_count: 2
  slug: technical-university-of-darmstadt-context
layout: provider
modified: '2026-06-03'
name: Technical University of Darmstadt
nav: Providers
network: true
overview: 'Technical University of Darmstadt publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The Technical University of Darmstadt catalog on APIs.io includes 1 JSON-LD context.


  Technical University of Darmstadt''s developer surface includes GitHub presence, authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Technical University Of Darmstadt Plans Pricing
  plan_count: 2
  slug: technical-university-of-darmstadt-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Technical University Of Darmstadt Rate Limits
  slug: technical-university-of-darmstadt-rate-limits
score:
  band: emerging
  composite: 22.9
  delta: 0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/technical-university-of-darmstadt/refs/heads/main/screenshots/technical-university-of-darmstadt-2026-06-20T195009.png
security:
- kind: domain-security
  name: Technical University Of Darmstadt Domain Security
  slug: technical-university-of-darmstadt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: technical-university-of-darmstadt
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- Library
- OAI-PMH
- DSpace
- Germany
website: https://www.tu-darmstadt.de/index.en.jsp
---

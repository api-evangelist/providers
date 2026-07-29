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
- description: 'Central university service publishing data feeds to software developers in programming-friendly formats such as JSON and XML (including the course directory, CLIO library catalog, and building access '
  name: Columbia Open Data Service
  slug: opendata
- description: Columbia University Libraries publishes its catalog (bibliographic and holdings data from the Integrated Library System behind CLIO) as open MARCXML bulk extracts, updated monthly and released under a
  name: CLIO Library Catalog Open Data
  slug: clio-opendata
- description: Public web directory of Columbia University class offerings, browsable by subject, department, semester, instruction method, weekday and start time. No official documented API or JSON feed is publishe
  name: CU Directory of Classes
  slug: directory-of-classes
- description: Columbia University Information Technology (CUIT) provides UNI-based web authentication and federation. CAS (Central Authentication Service) supports browser-based single sign-on and MFA, while the Sh
  name: Columbia Identity (CAS / Shibboleth SAML)
  slug: identity
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/columbia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.columbia.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opendataservice.columbia.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cul
- group: build
  title: ''
  type: GitHub
  url: https://github.com/columbia-it
- group: auth
  title: ''
  type: Authentication
  url: https://www.cuit.columbia.edu/web-authentication-federation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/columbia-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/columbia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/columbia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/columbia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Columbia University is a private Ivy League research university in New York City, ranked #18 in the QS World University Rankings 2025. Its public developer and API footprint is modest and largely gated: the central Open Data Service publishes programming-friendly JSON/XML data feeds (course directory, CLIO library catalog, building access, and more) that require a Columbia UNI login, while Columbia University Libraries offers the CLIO catalog as open MARCXML bulk data under CC0. Identity and access integration is provided via CAS and a Shibboleth/SAML 2.0 Identity Provider participating in the InCommon Federation. Source code is published across the cul (Libraries) and columbia-it (CUIT) GitHub organizations.'
finops:
- name: Columbia Finops
  service_category: Education
  slug: columbia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/columbia.png
jsonld:
- class_count: 8
  name: Columbia Context
  property_count: 3
  slug: columbia-context
layout: provider
modified: '2026-06-03'
name: Columbia University
nav: Providers
network: true
overview: 'Columbia University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Library.


  The Columbia University catalog on APIs.io includes 1 JSON-LD context.


  Columbia University''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: Columbia Plans Pricing
  plan_count: 2
  slug: columbia-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 1
  name: Columbia Rate Limits
  slug: columbia-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/columbia/refs/heads/main/screenshots/columbia-2026-06-20T174808.png
security:
- kind: domain-security
  name: Columbia Domain Security
  slug: columbia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: columbia
tags:
- Education
- Higher Education
- University
- Open Data
- Library
- Identity
- United States
website: https://www.columbia.edu/
---

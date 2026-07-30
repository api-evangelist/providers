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
- description: Enterprise API providing authoritative person/identity data for the University of Wisconsin-Madison. Access is gated and requires an approved institutional access request; a Mock Person API is publish
  name: Person API
  slug: person-api
- description: Human resources API exposing institutional HR data such as academic units. Documented on the developer portal, with a Mock HR API published openly for development and testing.
  name: HR API
  slug: hr-api
- description: API exposing UW-Madison's curricular data model (courses, curriculum structures) documented via the DoIT WAMS API hub with OpenAPI/JavaDoc-style reference documentation.
  name: Curricular Data Model API
  slug: curricular-data-model
- description: Degree Audit Reporting System (DARS) API for submitting and retrieving batch degree-audit requests, documented on the UW-Madison developer portal.
  name: DARS API
  slug: dars-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-wisconsin-madison-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wisc.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wisc.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UW-Madison-DoIT
- group: build
  title: ''
  type: SourceCode
  url: https://git.doit.wisc.edu/interop/external-docs/api-program
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uw-madison/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UWMadison
- group: operate
  title: ''
  type: Status
  url: https://www.outages.doit.wisc.edu/
- group: auth
  title: ''
  type: Authentication
  url: https://git.doit.wisc.edu/interop/external-docs/api-program/-/blob/main/practices/apigee.md
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-wisconsin-madison-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-wisconsin-madison-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-wisconsin-madison-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Wisconsin-Madison is a public land-grant research university in Madison, Wisconsin, ranked #46 in the QS World University Rankings 2025. Its Division of Information Technology (DoIT) runs a formal API Program with a public developer portal at developer.wisc.edu, an Apigee-based API gateway, OAuth2 client-credentials authentication, and published API standards based on JSON:API and OpenAPI. Documented enterprise APIs include the Person API, an HR API, the Curricular Data Model API, and the DARS (Degree Audit Reporting System) API. Most production APIs are gated and require institutional access requests, with mock variants published openly for development.'
finops:
- name: University Of Wisconsin Madison Finops
  service_category: Education
  slug: university-of-wisconsin-madison-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-wisconsin-madison.png
jsonld:
- class_count: 13
  name: University Of Wisconsin Madison Context
  property_count: 3
  slug: university-of-wisconsin-madison-context
layout: provider
modified: '2026-06-03'
name: University of Wisconsin-Madison
nav: Providers
network: true
overview: 'University of Wisconsin-Madison publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Identity, and Student Information System.


  The University of Wisconsin-Madison catalog on APIs.io includes 1 JSON-LD context.


  University of Wisconsin-Madison''s developer surface includes GitHub presence, status page, authentication, and 10 more developer resources.'
plans:
- name: University Of Wisconsin Madison Plans Pricing
  plan_count: 2
  slug: university-of-wisconsin-madison-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Wisconsin Madison Rate Limits
  slug: university-of-wisconsin-madison-rate-limits
score:
  band: emerging
  composite: 22.8
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-wisconsin-madison/refs/heads/main/screenshots/university-of-wisconsin-madison-2026-06-20T200421.png
security:
- kind: domain-security
  name: University Of Wisconsin Madison Domain Security
  slug: university-of-wisconsin-madison-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-wisconsin-madison
tags:
- Education
- Higher Education
- University
- Identity
- Student Information System
- Curriculum
- Human Resources
- United States
website: https://www.wisc.edu/
---

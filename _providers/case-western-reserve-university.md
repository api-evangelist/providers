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
- description: Campus single sign-on service for Case Western Reserve University. The login portal runs on CAS (Central Authentication Service), used to authenticate CWRU Network IDs across university web resources.
  name: CWRU Single Sign-On (CAS)
  slug: sso
- description: 'Kelvin Smith Library''s discovery search gateway providing a single interface across the online catalog, licensed databases, and OhioLINK / SearchOhio consortium holdings. Backed by a vendor discovery '
  name: CWRU Libraries Discovery
  slug: libraries-discovery
- description: The official Case Western Reserve University GitHub organization hosts a small set of (now archived) public repositories, primarily web content-management template utilities such as T4Utils and Refres
  name: CWRU GitHub Web Tooling
  slug: github
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/case-western-reserve-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://case.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cwru
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/case-western-reserve-university/
- group: auth
  title: ''
  type: Authentication
  url: https://login.case.edu/
- group: commercial
  title: ''
  type: Plans
  url: plans/case-western-reserve-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/case-western-reserve-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/case-western-reserve-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/case-western-reserve-university-context.jsonld
created: '2026-06-03'
description: 'Case Western Reserve University (CWRU) is a private research university in Cleveland, Ohio, United States, ranked #259 in the QS World University Rankings 2025. CWRU does not operate a public, documented developer or API portal; its outward technical footprint consists of an (archived) institutional GitHub organization focused on web content-template tooling, CAS-based single sign-on for campus identity, and library discovery delivered through the OhioLINK/SearchOhio consortium. Most institutional data is served internally through Tableau dashboards rather than open APIs, so the entries below describe confirmed public surfaces rather than openly documented programmatic endpoints.'
finops:
- name: Case Western Reserve University Finops
  service_category: Education
  slug: case-western-reserve-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/case-western-reserve-university.png
jsonld:
- class_count: 14
  name: Case Western Reserve University Context
  property_count: 4
  slug: case-western-reserve-university-context
layout: provider
modified: '2026-06-03'
name: Case Western Reserve University
nav: Providers
network: true
overview: 'Case Western Reserve University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Cleveland.


  The Case Western Reserve University catalog on APIs.io includes 1 JSON-LD context.


  Case Western Reserve University''s developer surface includes GitHub presence, authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Case Western Reserve University Plans Pricing
  plan_count: 2
  slug: case-western-reserve-university-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Case Western Reserve University Rate Limits
  slug: case-western-reserve-university-rate-limits
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 13.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/case-western-reserve-university/refs/heads/main/screenshots/case-western-reserve-university-2026-06-20T174030.png
security:
- kind: domain-security
  name: Case Western Reserve University Domain Security
  slug: case-western-reserve-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: case-western-reserve-university
tags:
- Education
- Higher Education
- University
- Research
- Cleveland
- Ohio
- United States
website: https://case.edu/
---

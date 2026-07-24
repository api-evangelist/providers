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
- description: 'The Hebrew University Library Authority runs its catalog and discovery on Ex Libris Primo/Alma (HUfind). Ex Libris provides standard Primo and Alma REST APIs and OAI-PMH publishing, but these are not '
  name: HUJI Library Discovery (Ex Libris Primo/Alma)
  slug: library-discovery
- description: OpenScholar is HUJI's Drupal-based website-building and content management platform for faculty, labs, and academic projects, hosting profiles, publications, CVs, courses, and events. It is an interna
  name: OpenScholar @ HUJI
  slug: openscholar
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hebrew-university-of-jerusalem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.huji.ac.il/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/huji-nlp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/hebrew-university-of-jerusalem/
- group: commercial
  title: ''
  type: Plans
  url: plans/hebrew-university-of-jerusalem-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hebrew-university-of-jerusalem-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hebrew-university-of-jerusalem-finops.yml
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
  url: json-ld/hebrew-university-of-jerusalem-context.jsonld
created: '2026-06-03'
description: 'The Hebrew University of Jerusalem (HUJI) is Israel''s leading research university, ranked #272 in the QS World University Rankings 2025. It operates multiple campuses in Jerusalem, Rehovot, and Eilat across the humanities, sciences, medicine, and law. HUJI does not publish a dedicated public developer portal or documented open API program. Its developer-relevant surface is limited to standards-based academic infrastructure: an Ex Libris Primo/Alma library discovery system (whose APIs require institution-issued keys), the OpenScholar profile/CMS platform, Shibboleth/SAML single sign-on (internal/gated), and a number of research-lab open-source GitHub organizations. No public, self-service API endpoints were confirmed.'
finops:
- name: Hebrew University Of Jerusalem Finops
  service_category: Education
  slug: hebrew-university-of-jerusalem-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hebrew-university-of-jerusalem.png
jsonld:
- class_count: 8
  name: Hebrew University Of Jerusalem Context
  property_count: 6
  slug: hebrew-university-of-jerusalem-context
layout: provider
modified: '2026-06-03'
name: Hebrew University of Jerusalem
nav: Providers
network: true
overview: 'Hebrew University of Jerusalem publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Hebrew University of Jerusalem catalog on APIs.io includes 1 JSON-LD context.


  Hebrew University of Jerusalem''s developer surface includes GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Hebrew University Of Jerusalem Plans Pricing
  plan_count: 2
  slug: hebrew-university-of-jerusalem-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Hebrew University Of Jerusalem Rate Limits
  slug: hebrew-university-of-jerusalem-rate-limits
score:
  band: emerging
  composite: 21.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 2.2
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hebrew-university-of-jerusalem/refs/heads/main/screenshots/hebrew-university-of-jerusalem-2026-06-20T182715.png
security:
- kind: domain-security
  name: Hebrew University Of Jerusalem Domain Security
  slug: hebrew-university-of-jerusalem-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hebrew-university-of-jerusalem
tags:
- Education
- Higher Education
- University
- Research
- Library
- Israel
website: https://en.huji.ac.il/
---

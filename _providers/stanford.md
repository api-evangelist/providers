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
api_count: 5
apis:
- description: IIIF Presentation (v2 stable, v3 alpha) and Image v2 APIs for digital image interoperability across the Stanford Digital Repository. Presentation manifests served from purl.stanford.edu; image tiles f
  name: Stanford Libraries IIIF API
  slug: library-iiif
- description: Persistent URLs to Stanford Digital Repository (SDR) content. GET /{id} returns HTML; /{id}.xml returns public XML metadata; /{id}.mods returns MODS XML. Public and open.
  name: Stanford Libraries PURL API
  slug: library-purl
- description: Public API returning operating hours for Stanford library locations.
  name: Stanford Libraries Library Hours API
  slug: library-hours
- description: API over the Community Academic Profiles directory (18,000+ faculty, students, postdocs, and staff profiles). Interactive console available; access requires credentials issued via HelpSU.
  name: CAP / Stanford Profiles API
  slug: cap-profiles
- description: 'University IT MaIS Registry REST APIs — Account, Person, Student, CourseClass, Privilege, and Workgroup — documented publicly but gated: access requires an x509 client certificate signed by the MaIS t'
  name: MaIS Registry APIs
  slug: mais-registry
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/stanford-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stanford-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stanford.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uit.stanford.edu/developers
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.library.stanford.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sul-dlss
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SU-SWS
- group: auth
  title: ''
  type: Authentication
  url: https://login.stanford.edu/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Stanford
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/stanford-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/stanford-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stanford-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stanford-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: About
  url: https://explorecourses.stanford.edu/about
created: '2026-06-03'
description: 'Stanford University is a private research university in Stanford, California (QS World 2025 #6) with a substantial, multi-pronged developer footprint. University IT (UIT) runs a developer hub at uit.stanford.edu/developers exposing certificate-secured MaIS Registry REST APIs (Account, Person, Student, CourseClass, Privilege, Workgroup) plus an AI API Gateway. Stanford Libraries (DLSS) publishes a public API documentation site at api.library.stanford.edu (IIIF, PURL, Embed, Digital Stacks, Library Hours) backing the Stanford Digital Repository, and the Registrar''s ExploreCourses offers a course-data XML query interface.'
finops:
- name: Stanford Finops
  service_category: Education
  slug: stanford-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stanford.png
jsonld:
- class_count: 25
  name: Stanford Context
  property_count: 2
  slug: stanford-context
layout: provider
modified: '2026-07-25'
name: Stanford University
nav: Providers
network: true
overview: 'Stanford University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Stanford University catalog on APIs.io includes 1 JSON-LD context.


  Stanford University''s developer surface includes GitHub presence, authentication, and 13 more developer resources.'
plans:
- name: Stanford Plans Pricing
  plan_count: 2
  slug: stanford-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 1
  name: Stanford Rate Limits
  slug: stanford-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: -2.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stanford/refs/heads/main/screenshots/stanford-2026-06-20T194502.png
security:
- kind: domain-security
  name: Stanford Domain Security
  slug: stanford-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Stanford Trust Center
  slug: stanford-trust-center
  summary_line: HIPAA, GDPR
slug: stanford
tags:
- Education
- Higher Education
- University
- Research
- Library
- Digital Repository
- IIIF
- Courses
website: https://www.stanford.edu/
---

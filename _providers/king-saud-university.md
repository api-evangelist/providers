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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: As of this review, King Saud University exposes no public, documented developer API. University digital services (Edugate SIS, LMS, library catalog, Saudi Digital Library access, manuscripts portal, a
  name: No Public Documented API
  slug: none
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/king-saud-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ksu.edu.sa/en
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/king-saud-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/_KSU
- group: auth
  title: ''
  type: Authentication
  url: https://edugate.ksu.edu.sa/ksu/init
- group: commercial
  title: ''
  type: Plans
  url: plans/king-saud-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/king-saud-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/king-saud-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'King Saud University (KSU) is a public research university in Riyadh, Saudi Arabia, founded in 1957, and ranked #200 in the QS World University Rankings 2025. KSU operates a broad estate of digital services — including the Edugate student information system, an LMS, a library catalog, Saudi Digital Library access, a digitized manuscripts portal, and university e-services — but it does not publish a public, documented developer or API program. The systems found during review are end-user web applications gated behind institutional SSO/login rather than openly documented APIs. No public API reference, OpenAPI definition, developer portal, or open-data API endpoint could be confirmed.'
finops:
- name: King Saud University Finops
  service_category: Education
  slug: king-saud-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/king-saud-university.png
jsonld:
- class_count: 11
  name: King Saud University Context
  property_count: 2
  slug: king-saud-university-context
layout: provider
modified: '2026-06-03'
name: King Saud University
nav: Providers
network: true
overview: 'King Saud University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Saudi Arabia, and Middle East.


  The King Saud University catalog on APIs.io includes 1 JSON-LD context.


  King Saud University''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: King Saud University Plans Pricing
  plan_count: 2
  slug: king-saud-university-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: King Saud University Rate Limits
  slug: king-saud-university-rate-limits
score:
  band: emerging
  composite: 22.0
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/king-saud-university/refs/heads/main/screenshots/king-saud-university-2026-06-20T184048.png
security:
- kind: domain-security
  name: King Saud University Domain Security
  slug: king-saud-university-domain-security
  summary_line: TLSv1.2 · DMARC
slug: king-saud-university
tags:
- Education
- Higher Education
- University
- Saudi Arabia
- Middle East
- Research
website: https://ksu.edu.sa/en
---

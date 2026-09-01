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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
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
- group: design
  title: ''
  type: JSONLD
  url: json-ld/case-western-reserve-university-context.jsonld
- group: other
  title: ''
  type: ProductPage
  url: https://researchguides.case.edu/discovery
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
modified: '2026-07-25'
name: Case Western Reserve University
nav: Providers
network: true
overview: 'Case Western Reserve University is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Cleveland.


  The Case Western Reserve University catalog on APIs.io includes 1 JSON-LD context.


  Case Western Reserve University''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: Case Western Reserve University Plans Pricing
  plan_count: 2
  slug: case-western-reserve-university-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Case Western Reserve University Rate Limits
  slug: case-western-reserve-university-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
